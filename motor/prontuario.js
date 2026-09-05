/* ══════════════════ o motor do prontuário ══════════════════

   Não existe "próxima tela". Existe um paciente, um relógio e uma lista de
   coisas que se pode fazer. O que entra no registro é o que foi feito — e o
   que não foi pedido simplesmente não aparece, nem agora nem depois.

   Três relógios governam tudo:

     · o do caso      quanto tempo passou desde a admissão
     · o de cada exame  quando o resultado dele fica pronto
     · o da doença    que anda sozinha enquanto ninguém a trata

   O motor não sabe nada de vasculite. Ele lê as tabelas que o caso declara em
   Python: quem se pode perguntar, o que se pode examinar, o que se pode
   prescrever, a que velocidade cada número anda sob cada condição, e que
   condição define cada desfecho. */

const D = k => JSON.parse(document.getElementById('d-' + k).textContent);
const PAC = D('paciente'), CAMPOS = D('campos'), SINAIS = D('sinais');
const ACOES = D('acoes'), ESPERA = D('espera'), EVO = D('evolucao');
const DESFECHOS = D('desfechos'), BANCO = D('banco'), REVISAO = D('revisao');
const GATILHOS = D('gatilhos'), IMAGENS = D('imagens');

/* ─────────────────────────── estado ─────────────────────────── */

let EST, REG, PEND, feitos, pedidos, marcados, encerrado;

function comecar(){
  EST = Object.assign({horas: 0, sinalizadores: []}, JSON.parse(JSON.stringify(PAC.estado)));
  REG = [];
  PEND = [];          // exames pedidos e ainda não prontos
  pedidos = [];       // tudo o que já foi pedido, na ordem
  feitos = [];        // chaves de ação já realizadas
  marcados = [];      // marcos de evolução já disparados
  encerrado = null;
  registrar('admissao', 'Admissão', PAC.resumo);
  pintar();
}

const EST0 = () => PAC.estado;

/* ─────────────────────────── o relógio ─────────────────────────── */

const H_ADM = +PAC.admissao.split(':')[0], M_ADM = +PAC.admissao.split(':')[1];

function relogio(min){
  const total = H_ADM * 60 + M_ADM + Math.round(min);
  const dia = Math.floor(total / 1440) + 1;
  const h = Math.floor(total % 1440 / 60), m = Math.round(total % 60);
  return 'D' + dia + ' ' + String(h).padStart(2, '0') + ':' + String(m).padStart(2, '0');
}

function desde(min){
  const h = min / 60;
  if (h < 1) return Math.round(min) + ' min';
  if (h < 48) return (h < 10 ? h.toFixed(1) : Math.round(h)) + ' h';
  return Math.round(h / 24) + ' dias';
}

/* ─────────────────────────── a doença anda ───────────────────────────

   Integrada em passos de quinze minutos: assim um marco de setenta e duas
   horas dispara na hora certa mesmo quando o grupo salta um dia inteiro de
   uma vez, e o número que aparece é o número que a doença produziu naquele
   intervalo, não uma interpolação do fim. */

/* Para onde cada campo caminha agora. Um sinalizador declarado depois do outro
   ganha o campo que os dois miram: é assim que a fibrose sobrepõe a
   recuperação sem que nenhuma regra precise citar a outra. */
function alvosAgora(){
  const a = {};
  Object.keys(EVO.alvos).forEach(s => {
    if (!tem(s)) return;
    Object.keys(EVO.alvos[s]).forEach(c => { a[c] = EVO.alvos[s][c]; });
  });
  return a;
}

/* A taxa base é a da doença não tratada. Onde existe alvo, ela é substituída —
   a trajetória passa a ser a da recuperação. Os bônus de `quando` continuam
   somando por cima: oxigênio ajuda a saturação esteja ela subindo ou caindo. */
function taxasAgora(alvo){
  const t = {};
  Object.keys(EVO.base).forEach(c => { if (!alvo[c]) t[c] = EVO.base[c]; });
  EST.sinalizadores.forEach(s => {
    const q = EVO.quando[s];
    if (q) Object.keys(q).forEach(c => { t[c] = (t[c] || 0) + q[c]; });
  });
  return t;
}

function avancar(minutos, motivo){
  if (encerrado) return;
  const passo = 15;
  let restante = Math.max(0, minutos);
  while (restante > 0){
    const dt = Math.min(passo, restante);
    const alvo = alvosAgora();
    const t = taxasAgora(alvo);
    Object.keys(t).forEach(c => {
      if (EST[c] === undefined) return;
      EST[c] = EST[c] + t[c] * dt / 60;
    });
    Object.keys(alvo).forEach(c => {
      if (EST[c] === undefined) return;
      const v = alvo[c][0], meia = alvo[c][1];
      EST[c] = EST[c] + (v - EST[c]) * (1 - Math.pow(0.5, (dt / 60) / meia));
    });
    EST.horas += dt / 60;
    restante -= dt;
    limites();
    dispararMarcos();
    entregarResultados();
  }
  Object.keys(CAMPOS).forEach(c => {
    EST[c] = Math.round(EST[c] * 100) / 100;
  });
  if (motivo) registrar('tempo', motivo, '');
  // quem faz o relógio andar não precisa lembrar de repintar
  if (typeof pintar === 'function') pintar();
  checarDesfechoAutomatico();
}

/* O corpo tem piso e teto: saturação não passa de 100 nem cai abaixo de 55 com
   o paciente ainda respirando, e a diurese não fica negativa. Sem isto uma
   espera longa produz números impossíveis e a lição vira caricatura. */
function limites(){
  // 100% em cateter nasal com o alvéolo sangrando é caricatura
  EST.spo2 = Math.max(55, Math.min(tem('vm') ? 99 : 97, EST.spo2));
  EST.hb = Math.max(3.5, Math.min(16, EST.hb));
  EST.creatinina = Math.max(0.6, Math.min(14, EST.creatinina));
  EST.potassio = Math.max(2.8, Math.min(8.5, EST.potassio));
  EST.diurese = Math.max(0, Math.min(200, EST.diurese));
}

function dispararMarcos(){
  EVO.marcos.forEach((m, i) => {
    if (marcados.includes(i) || EST.horas < m.h) return;
    if (m.exige.some(s => !tem(s))) return;
    if (m.impede.some(s => tem(s))) return;
    marcados.push(i);
    m.liga.forEach(ligar);
    m.desliga.forEach(desligar);
    registrar('evolucao', 'Evolução', m.x);
  });
}

function entregarResultados(){
  for (let i = PEND.length - 1; i >= 0; i--){
    if (EST.horas * 60 < PEND[i].pronto) continue;
    const e = PEND.splice(i, 1)[0];
    const im = IMAGENS[e.n];
    registrar('resultado', e.n, e.r + (e.ref && e.ref !== '—'
      ? '<span class="ref">referência: ' + e.ref + '</span>' : '')
      + (im ? '<figure><img src="' + im.src + '" alt="' + e.n + '">'
            + '<figcaption>' + im.legenda
            + '<span class="cr">' + im.credito + '</span></figcaption></figure>' : ''),
      {alterado: e.a, quando: e.pronto});
    // resultado que muda o estado do paciente, e não só o que se sabe dele
    (GATILHOS[e.n] || []).forEach(ligar);
  }
}

/* ─────────────────────────── sinalizadores ─────────────────────────── */

const tem = s => EST.sinalizadores.includes(s);
function ligar(s){ if (!tem(s)) EST.sinalizadores.push(s); }
function desligar(s){ const i = EST.sinalizadores.indexOf(s); if (i >= 0) EST.sinalizadores.splice(i, 1); }

/* ─────────────────────────── o registro ─────────────────────────── */

function registrar(tipo, titulo, corpo, extra){
  REG.push(Object.assign({t: tipo, h: (extra && extra.quando !== undefined)
    ? extra.quando : EST.horas * 60, tt: titulo, x: corpo}, extra || {}));
  REG.sort((a, b) => a.h - b.h);
}

/* ─────────────────────────── fazer uma coisa ─────────────────────────── */

function disponivel(a){
  if (a.uma && feitos.includes(a.k)) return false;
  return !a.exige.some(s => !tem(s));
}

function fazer(a){
  if (encerrado || !disponivel(a)) return;
  feitos.push(a.k);
  const antes = EST.horas * 60;
  avancar(a.min);
  const rot = a.t === 'conduta' ? a.r : a.r;
  registrar(a.t, rot, a.x, {quando: antes});
  if (a.ef) Object.keys(a.ef).forEach(c => {
    if (EST[c] !== undefined) EST[c] = Math.round((EST[c] + a.ef[c]) * 100) / 100;
  });
  a.liga.forEach(ligar);
  // o preço de fazer fora de hora entra como nota do próprio prontuário,
  // depois do fato: avisar antes do clique seria decidir pelo grupo
  if (a.p && a.ps.length && a.ps.some(s => !tem(s))){
    (a.pl || []).forEach(ligar);
    registrar('alerta', 'Observação', a.p, {quando: antes});
  }
  limites(); pintar(); checarDesfechoAutomatico();
}

/* ─────────────────────────── pedir exame ─────────────────────────── */

function pedir(e){
  if (encerrado) return;
  const espera = ESPERA[e.c] !== undefined ? ESPERA[e.c] : 120;
  const agora = EST.horas * 60;
  pedidos.push(e.n);
  registrar('pedido', 'Solicitado: ' + e.n,
            'Previsão de resultado em ' + desde(espera) + '.', {quando: agora});
  PEND.push(Object.assign({}, e, {pronto: agora + espera}));
  avancar(5);
  pintar();
}

/* ─────────────────────────── desfecho ─────────────────────────── */

function bate(c){
  if (c.s !== undefined) return tem(c.s) === c.v;
  const v = c.c === 'horas' ? EST.horas : EST[c.c];
  switch (c.op){
    case '<': return v < c.v; case '<=': return v <= c.v;
    case '>': return v > c.v; case '>=': return v >= c.v;
    default: return Math.abs(v - c.v) < 1e-9;
  }
}

function desfechoAgora(){
  return DESFECHOS.find(d => d.quando.every(bate)) || DESFECHOS[DESFECHOS.length - 1];
}

/* Alguns desfechos não esperam o grupo decidir encerrar: o paciente que
   dessatura abaixo do limite com o pulmão cheio de sangue não pergunta. */
function checarDesfechoAutomatico(){
  if (encerrado) return;
  const d = DESFECHOS.find(x => x.auto && x.quando.every(bate));
  if (d) encerrar(d);
}

function encerrar(forcado){
  if (encerrado) return;
  encerrado = forcado || desfechoAgora();
  pintar();
  mostrarDesfecho();
}

/* ══════════════════════════ a tela ══════════════════════════ */

const $ = s => document.querySelector(s);

function pintarCabecalho(){
  $('#pac').innerHTML = '<b>' + PAC.id + '</b><span>' + PAC.leito + '</span>';
  $('#hora').innerHTML = '<b>' + relogio(EST.horas * 60) + '</b>'
    + '<span>' + desde(EST.horas * 60) + ' de internação</span>';
  const v0 = EST0();
  $('#vitais').innerHTML = Object.keys(CAMPOS).map(k => {
    const c = CAMPOS[k], v = EST[k], base = v0[k];
    const dif = Math.abs(v - base) >= c.passo;
    const pior = c.sobe_e_piora ? v > base : v < base;
    return '<span class="v' + (dif ? (pior ? ' pior' : ' melhor') : '') + '">'
      + '<i>' + c.rotulo + '</i>' + v.toFixed(c.casas).replace('.', ',') + c.unidade
      + (dif ? '<u>' + (v > base ? '▲' : '▼') + '</u>' : '') + '</span>';
  }).join('') + EST.sinalizadores.filter(s => SINAIS[s])
      .map(s => '<span class="f">' + SINAIS[s] + '</span>').join('');
}

const ICONE = {admissao: '', anamnese: 'perguntou', exame: 'examinou',
  pedido: 'pediu', resultado: 'resultado', conduta: 'prescreveu',
  evolucao: 'evolução', tempo: 'aguardou', alerta: 'atenção'};

function pintarRegistro(){
  const alvo = $('#reg');
  alvo.innerHTML = REG.map(e =>
    '<article class="e e-' + e.t + (e.alterado ? ' alt' : '') + '">'
    + '<div class="eh"><time>' + relogio(e.h) + '</time>'
    + (ICONE[e.t] ? '<em>' + ICONE[e.t] + '</em>' : '')
    + '<h3>' + e.tt + '</h3></div>'
    + (e.x ? '<div class="ex">' + e.x + '</div>' : '') + '</article>').join('')
    + (PEND.length ? '<div class="pend"><b>Aguardando resultado</b>'
        + PEND.map(p => '<span>' + p.n + ' <i>' + relogio(p.pronto) + '</i></span>').join('')
        + '</div>' : '');
  alvo.scrollTop = alvo.scrollHeight;
}

function pintar(){ pintarCabecalho(); pintarRegistro(); pintarAcoes(); }

/* ─────────────────────────── as ações ─────────────────────────── */

const GRUPOS = ['Anamnese', 'Exame físico', 'Conduta'];

function pintarAcoes(){
  if (encerrado){
    $('#acoes').innerHTML = '<div class="fim-nota">Caso encerrado. '
      + '<button onclick="comecarDeNovo()">Conduzir de novo</button></div>';
    return;
  }
  const porGrupo = {};
  ACOES.filter(disponivel).forEach(a => {
    (porGrupo[a.g] = porGrupo[a.g] || []).push(a);
  });
  let h = '<button class="grande" onclick="abrirExames()">Pedir exame</button>'
        + '<button class="grande" onclick="abrirEspera()">Aguardar</button>';
  GRUPOS.forEach(g => {
    if (!porGrupo[g]) return;
    h += '<div class="grupo"><b>' + g + '</b>'
      + porGrupo[g].map(a => '<button class="a" data-k="' + a.k + '">'
          + a.r + (a.d ? '<i>' + a.d + '</i>' : '') + '</button>').join('')
      + '</div>';
  });
  h += '<div class="grupo fecha"><button class="a enc" onclick="encerrar()">'
     + 'Encerrar o caso<i>calcula o desfecho a partir do estado atual</i>'
     + '</button></div>';
  $('#acoes').innerHTML = h;
  $('#acoes').querySelectorAll('button.a[data-k]').forEach(b => {
    b.onclick = () => fazer(ACOES.find(a => a.k === b.dataset.k));
  });
}

/* ─────────────────────────── a gaveta de exames ─────────────────────────── */

const semAcento = t => t.normalize('NFD').replace(/[̀-ͯ]/g, '').toLowerCase();

function abrirExames(){
  abrirModal('Pedir exame',
    '<input id="busca" placeholder="digite o nome do exame" autocomplete="off">'
    + '<div class="dica">O resultado entra no prontuário quando ficar pronto. '
    + 'Cada categoria tem o seu tempo, e o relógio do caso é o mesmo do paciente.</div>'
    + '<div id="lista"></div>');
  const inp = $('#busca');
  inp.oninput = () => listarExames(inp.value);
  listarExames('');
  inp.focus();
}

function listarExames(q){
  const t = semAcento(q.trim());
  const achados = BANCO.filter(e => !t || semAcento(e.n).includes(t)
      || (e.s || []).some(x => semAcento(x).includes(t)));
  const jaPedido = n => pedidos.includes(n);
  $('#lista').innerHTML = achados.slice(0, 40).map((e, i) => {
    const esp = ESPERA[e.c] !== undefined ? ESPERA[e.c] : 120;
    return '<button class="ex-i" data-i="' + BANCO.indexOf(e) + '"'
      + (jaPedido(e.n) ? ' disabled' : '') + '>'
      + '<span class="n">' + e.n + '</span>'
      + '<span class="c">' + (e.c || '—') + '</span>'
      + '<span class="t">' + (jaPedido(e.n) ? 'já pedido' : desde(esp)) + '</span>'
      + '</button>';
  }).join('') || '<div class="vazio">Nenhum exame com esse nome neste serviço.</div>';
  $('#lista').querySelectorAll('button[data-i]').forEach(b => {
    b.onclick = () => { pedir(BANCO[+b.dataset.i]); fecharModal(); };
  });
}

/* ─────────────────────────── esperar ─────────────────────────── */

function abrirEspera(){
  const prox = PEND.length ? Math.min.apply(null, PEND.map(p => p.pronto)) : null;
  const opcoes = [[60, 'Uma hora'], [360, 'Seis horas'], [720, 'Doze horas'],
                  [1440, 'Um dia']];
  let h = '<div class="dica">O tempo é o único recurso que não se recupera. '
        + 'Enquanto a doença não é tratada, ele custa néfron.</div>';
  if (prox !== null){
    const falta = Math.max(5, prox - EST.horas * 60);
    h += '<button class="esp" data-m="' + falta + '">Até o próximo resultado'
       + '<i>' + desde(falta) + '</i></button>';
  }
  h += opcoes.map(o => '<button class="esp" data-m="' + o[0] + '">' + o[1]
       + '</button>').join('');
  abrirModal('Aguardar', h);
  document.querySelectorAll('button.esp').forEach(b => {
    b.onclick = () => {
      const m = +b.dataset.m;
      fecharModal();
      avancar(m, 'Aguardou ' + desde(m) + '.');
      pintar();
    };
  });
}

/* ─────────────────────────── modal ─────────────────────────── */

function abrirModal(titulo, corpo){
  $('#modal').innerHTML = '<div class="cx"><div class="ch"><h2>' + titulo
    + '</h2><button onclick="fecharModal()">fechar</button></div>'
    + '<div class="cc">' + corpo + '</div></div>';
  $('#modal').classList.add('on');
}
function fecharModal(){ $('#modal').classList.remove('on'); $('#modal').innerHTML = ''; }

/* ─────────────────────────── o desfecho e a revisão ─────────────────────── */

function mostrarDesfecho(){
  const d = encerrado;
  // um item da revisão está satisfeito pelo exame pedido, pela ação feita ou
  // pelo sinalizador que ela acende — colher hemocultura é uma conduta, e não
  // faria sentido cobrá-la como exame não pedido
  const naoPedidos = REVISAO.filter(r => !pedidos.includes(r.chave)
      && !feitos.includes(r.chave) && !(r.sinalizador && tem(r.sinalizador)));
  const h = '<div class="fim q-' + d.q + '">'
    + '<div class="fk">Desfecho</div><h2>' + d.t + '</h2>'
    + d.p.map(x => '<p>' + x + '</p>').join('')
    + '<div class="porque"><b>Por quê</b><p>' + d.porque + '</p></div>'
    + '<div class="linha"><b>A condução, em números</b>'
    + '<span>' + desde(EST.horas * 60) + ' de internação</span>'
    + '<span>' + pedidos.length + ' exames pedidos</span>'
    + '<span>' + feitos.length + ' ações registradas</span>'
    + Object.keys(CAMPOS).map(k => '<span>' + CAMPOS[k].rotulo + ' '
        + EST0()[k].toFixed(CAMPOS[k].casas).replace('.', ',') + ' → '
        + EST[k].toFixed(CAMPOS[k].casas).replace('.', ',') + '</span>').join('')
    + '</div>'
    + (naoPedidos.length
        ? '<div class="faltou"><b>O que não foi pedido</b>'
          + naoPedidos.map(r => '<div><span>' + r.rotulo + '</span><p>' + r.porque
              + '</p></div>').join('') + '</div>'
        : '<div class="faltou ok"><b>Nada essencial ficou de fora.</b></div>')
    + '</div>';
  abrirModal('Fim da condução', h);
}

function comecarDeNovo(){ fecharModal(); comecar(); }

/* ─────────────────────────── atalhos ─────────────────────────── */

addEventListener('keydown', e => {
  if (e.target.tagName === 'INPUT') { if (e.key === 'Escape') fecharModal(); return; }
  if (e.key === 'Escape') fecharModal();
  else if (e.key === 'x' || e.key === 'X') abrirExames();
  else if (e.key === 't' || e.key === 'T') abrirEspera();
});

comecar();

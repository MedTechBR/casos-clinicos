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
  if (h < 48){
    // "1.0 h" é saída de máquina; no prontuário se escreve uma hora
    const n = h < 10 ? Math.round(h * 10) / 10 : Math.round(h);
    if (n === 1) return 'uma hora';
    return String(n).replace('.', ',') + ' h';
  }
  const d = Math.round(h / 24);
  return d === 1 ? 'um dia' : d + ' dias';
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
  // a conduta que diz colher, colhe: o exame entra na fila com o tempo dele
  (a.pede || []).forEach(n => {
    const e = BANCO.find(x => x.n === n);
    if (e && !pedidos.includes(n)) pedir(e);
  });
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

/* ══════════════════════════ a tela ══════════════════════════

   Coluna única, como um prontuário de papel. Nada de lateral com o cardápio
   de condutas à vista: uma lista de doze condutas é uma prova de múltipla
   escolha com doze alternativas, e o grupo escolhe pela lista em vez de
   pensar. O que existe aqui é uma linha em branco — "o que você faz agora?" —
   e, nos momentos em que o caso realmente exige uma decisão, dois ou três
   caminhos concretos oferecidos dentro do próprio registro. */

const $ = s => document.querySelector(s);
const ABERTURA = D('abertura'), DECISOES = D('decisoes');

let aliquota = 0, decididas = [], decisaoAberta = null, ambiguidade = null;

/* ─────────────────────────── cabeçalho ─────────────────────────── */

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
  }).join('');
  const fl = EST.sinalizadores.filter(s => SINAIS[s]);
  $('#flags').innerHTML = fl.map(s => '<span class="f">' + SINAIS[s] + '</span>').join('');
  $('#flags').classList.toggle('on', fl.length > 0);
}

/* ─────────────────────────── registro ─────────────────────────── */

const RUBRICA = {anamnese: 'anamnese', exame: 'exame físico', pedido: 'solicitado',
  resultado: 'resultado', conduta: 'conduta', evolucao: 'evolução',
  tempo: '', alerta: 'observação', decisao: 'decisão'};

function pintarRegistro(){
  const alvo = $('#reg');
  alvo.innerHTML = REG.map(e =>
    '<article class="e e-' + e.t + (e.alterado ? ' alt' : '') + '">'
    + '<div class="eh"><time>' + relogio(e.h) + '</time>'
    + (RUBRICA[e.t] ? '<em>' + RUBRICA[e.t] + '</em>' : '')
    + (e.tt ? '<h3>' + e.tt + '</h3>' : '') + '</div>'
    + (e.x ? '<div class="ex">' + e.x + '</div>' : '') + '</article>').join('')
    + blocoPendentes() + blocoDecisao() + blocoAliquota();
  alvo.scrollTop = alvo.scrollHeight;
}

function blocoPendentes(){
  if (!PEND.length) return '';
  return '<div class="pend"><b>Aguardando resultado</b>'
    + PEND.map(p => '<span>' + p.n + ' <i>' + relogio(p.pronto) + '</i></span>').join('')
    + '</div>';
}

/* A história chega em alíquotas, no ritmo de quem escuta — não como um menu de
   perguntas. O que continua sendo pergunta é só o que o paciente não conta por
   conta própria. */
function blocoAliquota(){
  if (encerrado || decisaoAberta || aliquota >= ABERTURA.length) return '';
  return '<div class="mais"><button onclick="proximaAliquota()">continuar a '
    + 'história &rarr;</button><i>ou faça alguma coisa: a linha de baixo está '
    + 'aberta o tempo todo</i></div>';
}

function proximaAliquota(){
  const a = ABERTURA[aliquota++];
  if (!a) return;
  if (a.min) avancar(a.min);
  registrar('anamnese', a.tt, a.p.map(x => '<p>' + x + '</p>').join(''));
  pintar();
}

/* ─────────────────────────── decisões ─────────────────────────── */

/* Uma decisão volta quando a situação que a criou persiste. `decididas` guarda
   até quando ela fica calada — infinito para a escolha que não se refaz, e o
   `volta_em` do caso para a que se refaz enquanto o número não melhora. */
function decisaoPendente(){
  return DECISOES.find(d => {
    const j = decididas.find(x => x.k === d.k);
    if (j && EST.horas < j.ate) return false;
    return d.quando.every(bate);
  });
}

function blocoDecisao(){
  const d = decisaoAberta;
  if (!d || encerrado) return '';
  return '<div class="dec"><div class="dk">O caso pede uma decisão</div>'
    + (d.c ? '<p class="dc">' + d.c + '</p>' : '')
    + '<h3>' + d.q + '</h3><div class="dcs">'
    + d.caminhos.map((c, i) => '<button data-c="' + i + '">'
        + '<span class="l">' + String.fromCharCode(65 + i) + '</span>'
        + '<span class="r">' + c.r + '</span></button>').join('')
    + '</div><div class="dh">ou ignore os caminhos e escreva a sua conduta na '
    + 'linha de baixo</div></div>';
}

function escolherCaminho(i){
  const d = decisaoAberta;
  if (!d) return;
  const c = d.caminhos[i];
  const antiga = decididas.find(x => x.k === d.k);
  const ate = d.volta ? EST.horas + d.volta : Infinity;
  if (antiga) antiga.ate = ate; else decididas.push({k: d.k, ate: ate});
  decisaoAberta = null;
  registrar('decisao', d.q, '<b>' + c.r + '</b>'
    + (c.porque ? '<p class="pq">' + c.porque + '</p>' : ''));
  c.faz.forEach(k => {
    const a = ACOES.find(x => x.k === k);
    if (a && disponivel(a)) fazer(a);
  });
  if (c.esp) avancar(c.esp, 'Aguardou ' + desde(c.esp) + '.');
  pintar();
}

function abrirDecisaoSeHouver(){
  if (decisaoAberta || encerrado) return;
  const d = decisaoPendente();
  if (d) decisaoAberta = d;
}

/* ══════════════════ a linha de comando ══════════════════

   Uma linha em branco, e o grupo escreve o que faria. Não há menu para
   percorrer com os olhos, e é essa a diferença: quem escreve "peço o
   sedimento" pensou no sedimento; quem clica na terceira linha da lista
   reconheceu a terceira linha da lista.

   O casamento é por dicionário — nome, sinônimos, categoria — e é honesto
   quando não entende: diz que não entendeu, e diz o que dá para fazer. */

const SEM_ACENTO = t => t.normalize('NFD').replace(/[̀-ͯ]/g, '').toLowerCase();
const VAZIAS = new Set(['de','do','da','dos','das','o','a','os','as','e','em',
  'no','na','um','uma','para','pra','por','com','ao','à','que','se','ja','já']);
const VERBOS = {
  pedir: /^(ped|pec|solicit|colh|requisit|manda|quero)/,
  examinar: /^(exam|ausculta|inspecion|palp|percut|avali|olha|ve[jr])/,
  perguntar: /^(pergunt|questio|indag|interrog|investig)/,
  prescrever: /^(prescrev|inici|comec|come|administr|dou|da[rn]|faz|instal|intub|dialis|transfund)/,
};

function fichas(t){
  return SEM_ACENTO(t).replace(/[^a-z0-9\s]/g, ' ').split(/\s+/)
    .filter(w => w.length > 2 && !VAZIAS.has(w));
}

/* O índice é montado uma vez: tudo o que se pode fazer ou pedir, com os nomes
   por que se pode chamar cada coisa. */
const INDICE = [];
function montarIndice(){
  INDICE.length = 0;
  ACOES.forEach(a => INDICE.push({
    tipo: a.t, alvo: a, rotulo: a.r,
    nome: new Set(fichas(a.r)),
    fichas: new Set(fichas(a.r + ' ' + (a.s || []).join(' ')))}));
  BANCO.forEach(e => INDICE.push({
    tipo: 'pedido', alvo: e, rotulo: e.n,
    nome: new Set(fichas(e.n)),
    fichas: new Set(fichas(e.n + ' ' + (e.s || []).join(' ')))}));
}

function casa(w, conjunto){
  if (conjunto.has(w)) return 1;
  // prefixo de cinco letras cobre plural e flexão sem casar por acaso
  for (const g of conjunto)
    if (g.length > 4 && w.length > 4 && (g.startsWith(w.slice(0, 5))
        || w.startsWith(g.slice(0, 5)))) return 0.75;
  return 0;
}

/* Três parcelas, e a ordem delas foi decidida por erro observado:

   · o que a pessoa escreveu está no NOME da coisa — vale mais, porque foi
     assim que "quero ver a urina" passava para "Hematúria", cujo sinônimo
     citava urina, em vez de "Sedimento urinário", cujo nome cita;
   · está no nome ou num sinônimo;
   · quanto do item foi coberto — a menor das três, senão item de nome curto
     ganha de item de nome preciso só por ser curto. */
function pontuar(entrada, item){
  const f = fichas(entrada);
  if (!f.length) return 0;
  let nome = 0, todas = 0;
  f.forEach(w => {
    nome += casa(w, item.nome);
    todas += casa(w, item.fichas);
  });
  if (!todas) return 0;
  return (nome / f.length) * 0.44
       + (todas / f.length) * 0.38
       + (todas / item.fichas.size) * 0.18;
}

const TEMPO = /(aguard|esper|passa|deixa)\w*\s*(?:por\s*|mais\s*|ate\s*)?([a-z0-9]+)?\s*(minuto|min|hora|h\b|dia|d\b)?/;
/* Ninguém escreve "aguardo 2 horas": escreve "aguardo duas horas". */
const NUMERO = {um: 1, uma: 1, dois: 2, duas: 2, tres: 3, quatro: 4, cinco: 5,
  seis: 6, sete: 7, oito: 8, nove: 9, dez: 10, doze: 12, quinze: 15,
  vinte: 20, trinta: 30, meia: 0.5, meio: 0.5};

function interpretar(entrada){
  const t = entrada.trim();
  if (!t) return;

  // "aguardar seis horas", "espero um dia", "aguardar"
  const st = SEM_ACENTO(t);
  const mt = st.match(TEMPO);
  if (mt && fichas(t).length <= 5){
    // "aguardo até o próximo resultado" espera o que está na fila
    if (/proxim|result|ficar pronto|sair/.test(st) && PEND.length){
      const falta = Math.max(5, Math.min.apply(null, PEND.map(p => p.pronto))
                                 - EST.horas * 60);
      responder('Aguardou ' + desde(falta) + ', até o próximo resultado.', 'ok');
      avancar(falta, 'Aguardou até o próximo resultado.');
      pintar();
      return;
    }
    const bruto = mt[2] || '';
    const n = /^\d+$/.test(bruto) ? +bruto : (NUMERO[bruto] || 1);
    const u = mt[3] || 'hora';
    const min = /min/.test(u) ? n : /dia|^d$/.test(u) ? n * 1440 : n * 60;
    responder('Aguardou ' + desde(min) + '.', 'ok');
    avancar(min, 'Aguardou ' + desde(min) + '.');
    pintar();
    return;
  }

  let verbo = null;
  const primeira = SEM_ACENTO(t).split(/\s+/)[0];
  Object.keys(VERBOS).forEach(v => { if (VERBOS[v].test(primeira)) verbo = v; });

  const notas = INDICE
    .filter(i => !(i.tipo !== 'pedido' && !disponivel(i.alvo)))
    .filter(i => !(i.tipo === 'pedido' && pedidos.includes(i.alvo.n)))
    .map(i => ({i: i, p: pontuar(t, i) * peso(verbo, i.tipo)}))
    .filter(x => x.p > 0)
    .sort((a, b) => b.p - a.p);

  if (!notas.length || notas[0].p < 0.34){ naoEntendi(t); return; }
  // dois candidatos muito próximos: perguntar é mais honesto que adivinhar
  if (notas.length > 1 && notas[1].p > notas[0].p * 0.86){
    ambiguidade = notas.slice(0, 4).map(x => x.i);
    responder('', 'ambiguo');
    return;
  }
  executar(notas[0].i);
}

/* O verbo escrito não decide sozinho, mas desempata: "peço tomografia" e
   "examino o tórax" são coisas diferentes com as mesmas palavras. */
function peso(verbo, tipo){
  if (!verbo) return 1;
  if (verbo === 'pedir') return tipo === 'pedido' ? 1.25 : 0.75;
  if (verbo === 'examinar') return tipo === 'exame' ? 1.3 : 0.8;
  if (verbo === 'perguntar') return tipo === 'anamnese' ? 1.3 : 0.8;
  if (verbo === 'prescrever') return tipo === 'conduta' ? 1.3 : 0.8;
  return 1;
}

function executar(item){
  ambiguidade = null;
  if (item.tipo === 'pedido'){ pedir(item.alvo); responder('Pedido: ' + item.rotulo, 'ok'); }
  else { fazer(item.alvo); responder(item.rotulo, 'ok'); }
  pintar();
}

function naoEntendi(t){
  ambiguidade = null;
  responder('Não encontrei isso neste serviço. Você pode pedir um exame pelo '
    + 'nome, examinar um sistema, perguntar alguma coisa ao paciente, '
    + 'prescrever uma conduta, ou aguardar um tempo.', 'erro');
}

function responder(msg, tipo){
  const r = $('#resp');
  if (tipo === 'ambiguo'){
    r.className = 'amb on';
    r.innerHTML = '<b>Qual deles?</b>'
      + ambiguidade.map((i, k) => '<button data-amb="' + k + '">'
          + i.rotulo + '</button>').join('');
  } else {
    r.className = tipo + ' on';
    r.innerHTML = msg;
    clearTimeout(r._t);
    r._t = setTimeout(() => r.classList.remove('on'), tipo === 'erro' ? 7000 : 2600);
  }
}

/* ─────────────────────────── ajuda, sem cardápio ───────────────────────────
   Para o grupo que trava. Mostra CATEGORIAS e exemplos de frase, nunca a lista
   de condutas — dar a lista é dar a resposta. */

function abrirAjuda(){
  const cat = {};
  BANCO.forEach(e => { cat[e.c] = (cat[e.c] || 0) + 1; });
  abrirModal('O que dá para fazer', '<div class="dica">Escreva na linha de '
    + 'baixo, com as suas palavras. Alguns exemplos:</div>'
    + '<ul class="ex-frases">'
    + ['peço o sedimento urinário', 'ausculto o tórax',
       'pergunto que medicamentos ele usa', 'inicio pulso de metilprednisolona',
       'aguardo seis horas', 'peço tomografia de tórax'
      ].map(x => '<li>' + x + '</li>').join('')
    + '</ul><div class="dica">A gaveta do serviço tem '
    + Object.keys(cat).sort().map(c => '<b>' + cat[c] + '</b> em ' + c).join(', ')
    + '. Pergunte pelo nome do exame, não pela categoria.</div>');
}

/* ─────────────────────────── modal ─────────────────────────── */

function abrirModal(titulo, corpo){
  $('#modal').innerHTML = '<div class="cx"><div class="ch"><h2>' + titulo
    + '</h2><button onclick="fecharModal()">fechar</button></div>'
    + '<div class="cc">' + corpo + '</div></div>';
  $('#modal').classList.add('on');
}
function fecharModal(){ $('#modal').classList.remove('on'); $('#modal').innerHTML = ''; }

/* ─────────────────────────── desfecho e revisão ─────────────────────── */

function mostrarDesfecho(){
  const d = encerrado;
  const naoPedidos = REVISAO.filter(r => !pedidos.includes(r.chave)
      && !feitos.includes(r.chave) && !(r.sinalizador && tem(r.sinalizador)));
  abrirModal('Fim da condução', '<div class="fim q-' + d.q + '">'
    + '<div class="fk">Desfecho</div><h2>' + d.t + '</h2>'
    + d.p.map(x => '<p>' + x + '</p>').join('')
    + '<div class="porque"><b>Por quê</b><p>' + d.porque + '</p></div>'
    + '<div class="linha"><b>A condução, em números</b>'
    + '<span>' + desde(EST.horas * 60) + ' de internação</span>'
    + '<span>' + pedidos.length + ' exames pedidos</span>'
    + '<span>' + feitos.length + ' ações</span>'
    + Object.keys(CAMPOS).map(k => '<span>' + CAMPOS[k].rotulo + ' '
        + EST0()[k].toFixed(CAMPOS[k].casas).replace('.', ',') + ' &rarr; '
        + EST[k].toFixed(CAMPOS[k].casas).replace('.', ',') + '</span>').join('')
    + '</div>'
    + (naoPedidos.length
        ? '<div class="faltou"><b>O que não foi pedido</b>'
          + naoPedidos.map(r => '<div><span>' + r.rotulo + '</span><p>' + r.porque
              + '</p></div>').join('') + '</div>'
        : '<div class="faltou ok"><b>Nada essencial ficou de fora.</b></div>')
    + '<button class="denovo" onclick="comecarDeNovo()">Conduzir de novo</button>'
    + '</div>');
}

function comecarDeNovo(){ fecharModal(); comecar(); }

/* ─────────────────────────── pintura e eventos ─────────────────────── */

function pintar(){
  abrirDecisaoSeHouver();
  pintarCabecalho();
  pintarRegistro();
  $('#barra').classList.toggle('off', !!encerrado);
}

document.addEventListener('click', e => {
  const c = e.target.closest('[data-c]');
  if (c){ escolherCaminho(+c.dataset.c); return; }
  const a = e.target.closest('[data-amb]');
  if (a){ executar(ambiguidade[+a.dataset.amb]); return; }
});

addEventListener('keydown', e => {
  if (e.key === 'Escape'){ fecharModal(); return; }
  if (e.target.id === 'cmd') return;
  if (e.key === '?' ) { abrirAjuda(); e.preventDefault(); }
  else if (e.key !== 'Tab') $('#cmd').focus();
});

function ligarBarra(){
  const cmd = $('#cmd');
  cmd.addEventListener('keydown', e => {
    if (e.key !== 'Enter') return;
    const v = cmd.value;
    cmd.value = '';
    interpretar(v);
  });
  $('#ajuda').onclick = abrirAjuda;
  $('#encerrar').onclick = () => encerrar();
  cmd.focus();
}

montarIndice();
ligarBarra();
comecar();

/* ═══════════════ ramificação: estado, caminho e volta ao nó ═══════════════

   Antes, a ordem do DOM era a ordem da apresentação. Com ramos isso deixa de
   valer: o DOM vira repositório de blocos com id, e a navegação vira uma
   PILHA do caminho percorrido. É essa troca que dá a volta ao nó anterior de
   graça, e é ela que faz o contrafactual — "e se tivéssemos feito o outro?" —
   caber numa tecla. */

const EST0 = JSON.parse(document.getElementById('estado0').textContent);
const CAMPOS = JSON.parse(document.getElementById('campos').textContent);
let EST = JSON.parse(JSON.stringify(EST0));

/* Cada passo guarda o slide, o ramo escolhido e o estado ANTES dele: é o que
   permite desfazer a escolha por inteiro, e não só voltar de tela. */
const caminho = [];

function idDoSlide(s){ return s.id.replace(/^s-/, ''); }
function slidePorId(k){ return document.getElementById('s-' + k); }

function aplicar(ef, sinal){
  ['horas', 'creatinina', 'spo2', 'hb'].forEach(c => {
    if (ef[c]) EST[c] = Math.round((EST[c] + sinal * ef[c]) * 10) / 10;
  });
  const liga = sinal > 0 ? ef.liga : ef.desliga;
  const tira = sinal > 0 ? ef.desliga : ef.liga;
  (liga || []).forEach(f => { if (!EST.sinalizadores.includes(f)) EST.sinalizadores.push(f); });
  (tira || []).forEach(f => {
    const i = EST.sinalizadores.indexOf(f);
    if (i >= 0) EST.sinalizadores.splice(i, 1);
  });
  // toda mudança de estado repinta: a barra e os números na prosa saem daqui
  pintarEstado();
}

/* ─────────────────────── a barra de prontuário ─────────────────────── */

const barra = document.getElementById('est');
function pintarEstado(){
  const campos = Object.entries(CAMPOS).map(([k, c]) => {
    const v = EST[k], v0 = EST0[k];
    const piorou = c.sobe_e_piora ? v > v0 : v < v0;
    const mudou = v !== v0;
    return '<span class="ec' + (mudou ? (piorou ? ' pior' : ' melhor') : '') + '">'
      + '<i>' + c.rotulo + '</i>' + v.toFixed(c.casas) + c.unidade
      + (mudou ? '<u>' + (v > v0 ? '▲' : '▼') + '</u>' : '') + '</span>';
  }).join('');
  const flags = EST.sinalizadores.map(f =>
    '<span class="ef">' + (SINAIS[f] || f) + '</span>').join('');
  barra.innerHTML = campos + flags;
  barra.classList.toggle('on', true);
  pintarValoresNaProsa();
}

/* A prosa também tem de dizer a verdade do caminho. Num caso que ramifica,
   "creatinina de 3,8 mg/dL" escrito à mão fica errado em dois dos três ramos:
   quem gastou trinta e quatro horas chega ao mesmo slide com 5,2. Os <<campos>>
   escritos no fonte viram estes vãos, preenchidos a cada mudança de estado. */
function pintarValoresNaProsa(){
  document.querySelectorAll('.ev[data-campo]').forEach(e => {
    const k = e.dataset.campo, c = CAMPOS[k];
    if (!c || EST[k] === undefined) return;
    // vírgula decimal: é prontuário em português, e "3.8" numa frase corrida
    // é o tipo de detalhe que denuncia texto gerado
    e.textContent = EST[k].toFixed(c.casas).replace('.', ',') + c.unidade;
    e.classList.toggle('mudou', EST[k] !== EST0[k]);
  });
}
const SINAIS = JSON.parse(document.getElementById('sinais').textContent);

/* ─────────────────────── escolher um ramo ─────────────────────── */

function escolher(li){
  const ul = li.parentElement;
  if (ul.classList.contains('decidido')) return;
  const ef = JSON.parse(li.dataset.efeito);
  const s = li.closest('.slide');

  caminho.push({ de: idDoSlide(s), ramo: li.dataset.ramo, efeito: ef,
                 antes: JSON.parse(JSON.stringify(EST)),
                 cobradosAte: cobrados.length });
  aplicar(ef, +1);

  ul.classList.add('decidido');
  li.classList.add('escolhido');
  li.querySelector('.wy').hidden = false;
  ul.querySelectorAll('li:not(.escolhido) .wy').forEach(w => { w.hidden = false; });
  const seguir = document.getElementById('seguir');
  seguir.dataset.vai = li.dataset.vai;
  seguir.classList.add('on');
}

function seguirRamo(){
  const k = document.getElementById('seguir').dataset.vai;
  document.getElementById('seguir').classList.remove('on');
  if (k) irPara(k);
}

/* ─────────────────────── navegação por caminho ─────────────────────── */

function irPara(k){
  const alvo = slidePorId(k);
  if (!alvo){ console.warn('destino inexistente:', k); return; }
  show(S.indexOf(alvo));
}

/* Volta ao nó anterior desfazendo o efeito da escolha: em sala é o gesto do
   contrafactual, e sem desfazer o estado o "e se" mentiria. */
function voltarAoNo(){
  const p = caminho.pop();
  if (!p){
    aviso('nenhuma decisão tomada ainda');
    return;
  }
  EST = JSON.parse(JSON.stringify(p.antes));
  // o estado voltou ao que era antes da escolha; os blocos atravessados depois
  // dela deixam de estar pagos, para que a segunda passagem cobre de novo
  cobrados.length = p.cobradosAte;
  pintarEstado();
  const s = slidePorId(p.de);
  const ul = s.querySelector('.ramos');
  ul.classList.remove('decidido');
  ul.querySelectorAll('li').forEach(l => l.classList.remove('escolhido'));
  ul.querySelectorAll('.wy').forEach(w => { w.hidden = true; });
  document.getElementById('seguir').classList.remove('on');
  show(S.indexOf(s));
  aviso('de volta ao nó — o estado do paciente foi desfeito');
}

function aviso(t){
  const a = document.getElementById('aviso');
  a.textContent = t;
  a.classList.add('on');
  clearTimeout(a._t);
  a._t = setTimeout(() => a.classList.remove('on'), 2200);
}

/* ─────────── o preço de atravessar um bloco ───────────
   Nem toda piora vem de um clique. Um ramo que passa dois dias esperando
   sorologia cobra do rim enquanto o grupo assiste; o número tem de andar
   sozinho. Cobrado uma vez por bloco: rever o slide não cobra de novo. */
const cobrados = [];

function cobrarBloco(s){
  if (!s || !s.dataset.custo) return;
  const k = idDoSlide(s);
  if (cobrados.includes(k)) return;
  cobrados.push(k);
  aplicar(JSON.parse(s.dataset.custo), +1);
}

/* ─────────────────────── mapa da árvore ─────────────────────── */

/* O que ainda está ao alcance.

   O baralho tem oito nós, e quatro deles são o mesmo momento — o quinto dia —
   em ramos diferentes: só um pode acontecer. Listar os oito lado a lado sugere
   à turma que todos estão em jogo, o que é falso depois da primeira decisão.
   Estas três funções andam pelo grafo de verdade (data-vai do ramo, data-segue
   do bloco, vizinho do DOM quando não há nenhum dos dois) e dizem o que ainda
   é possível. O resto o mapa mostra apagado: a escolha fechou aquela porta, e
   ver a porta fechada é metade da lição. */

function proximoBloco(s){
  const k = s.dataset.segue;
  if (k) return slidePorId(k);
  return S[S.indexOf(s) + 1] || null;
}

function ateOProximoNo(s){
  for (let n = 0; s && n < 80; n++){
    if (s.classList.contains('no') || s.classList.contains('fim')) return s;
    s = proximoBloco(s);
  }
  return null;
}

function aindaAoAlcance(){
  let raiz = cur();
  if (!raiz.classList.contains('no') && !raiz.classList.contains('fim'))
    raiz = ateOProximoNo(raiz);
  const decidido = raiz && raiz.classList.contains('no')
    && raiz.querySelector('.ramos.decidido');
  const fila = [];
  if (decidido){
    const esc = raiz.querySelector('.rm.escolhido');
    fila.push(raiz, esc ? ateOProximoNo(slidePorId(esc.dataset.vai)) : null);
  } else {
    fila.push(raiz);
  }
  const vistos = new Set();
  while (fila.length){
    const s = fila.shift();
    if (!s || vistos.has(s)) continue;
    vistos.add(s);
    if (s.classList.contains('no'))
      s.querySelectorAll('.rm').forEach(
        r => fila.push(ateOProximoNo(slidePorId(r.dataset.vai))));
  }
  // o que já foi percorrido continua no mapa: é o histórico da sessão
  caminho.forEach(c => { const n = slidePorId(c.de); if (n) vistos.add(n); });
  return vistos;
}

const mapa = document.getElementById('mapa');
function pintarMapa(){
  const nos = [...document.querySelectorAll('.slide.no')];
  const atual = cur();
  const vivos = aindaAoAlcance();
  const linhas = nos.map(n => {
    const k = idDoSlide(n);
    const passo = caminho.find(c => c.de === k);
    const t = n.querySelector('h2').textContent;
    const ramos = [...n.querySelectorAll('.rm')].map(r => {
      const esc = passo && passo.ramo === r.dataset.ramo;
      return '<span class="mr' + (esc ? ' esc' : '') + '" data-ir="' + k + '">'
        + r.querySelector('.tt').textContent + '</span>';
    }).join('');
    return '<div class="mn' + (n === atual ? ' aqui' : '')
      + (passo ? ' feito' : '') + (vivos.has(n) ? '' : ' fora') + '" data-ir="' + k + '">'
      + '<b>' + t + '</b><div class="mrs">' + ramos + '</div></div>';
  }).join('');
  const todos = [...document.querySelectorAll('.slide.fim')];
  const fins = todos.map(f =>
    '<span class="mf ' + [...f.classList].find(c => c.startsWith('q-'))
    + (f === atual ? ' aqui' : '') + (vivos.has(f) ? '' : ' fora')
    + '" data-ir="' + idDoSlide(f) + '">'
    + f.querySelector('h2').textContent + '</span>').join('');
  const vivosFim = todos.filter(f => vivos.has(f)).length;
  const rotulo = vivosFim === todos.length
    ? 'Desfechos possíveis'
    : 'Desfechos ainda possíveis {{' + vivosFim + ' de ' + todos.length + '}}';
  mapa.innerHTML = '<div class="mt">Onde estamos</div>' + linhas
    + '<div class="mt">' + rotulo.replace('{{', '<i>').replace('}}', '</i>')
    + '</div><div class="mfs">' + fins + '</div>'
    + '<div class="mh">clique para pular · V volta ao nó anterior · M fecha</div>';
}
function abrirMapa(v){
  if (v) pintarMapa();
  mapa.classList.toggle('on', v);
}

document.addEventListener('click', e => {
  const li = e.target.closest('.ramos li');
  if (li){ escolher(li); e.stopPropagation(); return; }
  if (e.target.closest('#seguir')){ seguirRamo(); e.stopPropagation(); return; }
  const m = e.target.closest('[data-ir]');
  if (m){ abrirMapa(false); irPara(m.dataset.ir); e.stopPropagation(); }
}, true);

addEventListener('keydown', e => {
  if (e.target.tagName === 'INPUT' || e.target.isContentEditable) return;
  if (e.key === 'm' || e.key === 'M'){
    abrirMapa(!mapa.classList.contains('on'));
    e.preventDefault();
  } else if (e.key === 'v' || e.key === 'V'){
    voltarAoNo();
    e.preventDefault();
  } else if (mapa.classList.contains('on') && e.key === 'Escape'){
    abrirMapa(false);
  }
});

/* ─────────── o exame pedido consome tempo, e o rim sente ───────────
   O terceiro gatilho do estado: cada exame pedido na gaveta adianta o
   relógio pelo tempo que ele leva de verdade. Pedir sedimento custa meia
   hora; pedir sorologia custa dois dias, e é por isso que o caso não pode
   esperar por ela. Pedir tudo "por via das dúvidas" tem preço. */
const CUSTO_HORA = {
  'Urina': 0.5, 'Gasometria': 0.3, 'Hemograma': 0.5, 'Bioquímica': 0.5,
  'Coagulação': 0.5, 'Inflamação': 1, 'Microbiologia': 48, 'Sorologia': 24,
  'Imunologia': 48, 'Imagem': 3, 'Procedimento': 6,
  'Anatomia patológica': 72, 'Neurofisiologia': 12,
};

function custoDoExame(e){
  const h = CUSTO_HORA[e.c];
  if (!h) return;
  EST.horas = Math.round((EST.horas + h) * 10) / 10;
  // a função renal acompanha o relógio enquanto a doença não é tratada
  if (!EST.sinalizadores.includes('imunossupressao') && h >= 12){
    EST.creatinina = Math.round((EST.creatinina + h / 24 * 0.6) * 10) / 10;
  }
  pintarEstado();
  aviso('pedido registrado — ' + (h < 1 ? Math.round(h * 60) + ' min' : h + ' h')
        + ' no relógio do caso');
}

pintarEstado();

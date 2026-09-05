/* ═══════════ o caso em etapas — página a página ═══════════

   Uma folha de cada vez. Nada rola: a página inteira é uma etapa, e passar de
   etapa é virar a folha. O que decide a folha seguinte é o que foi respondido
   na atual.

   Três coisas o motor guarda entre as etapas: os exames marcados em cada
   pedido, as respostas dadas, e o caminho escolhido em cada bifurcação. É com
   os exames marcados que a página de resultados sabe o que devolver — e é por
   isso que o que não foi pedido não aparece. */

const DADOS = JSON.parse(document.getElementById('dados').textContent);
const CASO = DADOS.caso, ETAPAS = DADOS.etapas, BANCO = DADOS.banco;
const REVISAO = DADOS.revisao;

const $ = s => document.querySelector(s);

/* ─────────────────────────── estado da sessão ─────────────────────────── */

let i = 0;                    // índice da etapa atual
const marcados = {};          // ident do pedido -> Set de nomes de exame
const respostas = {};         // ident da pergunta -> {marcadas:[], feita:bool}
const escolhas = {};          // ident da bifurcação -> índice do caminho
let historia = [0];           // pilha de etapas visitadas, para voltar
/* Numa peça página a página, rolar é trapaça. Quando o grupo pede muitos
   exames, os cartões não cabem numa folha — então a folha vira duas, e o
   avançar percorre as folhas antes de sair da etapa. */
const folhaDe = {};           // ident da etapa de resultados -> folha atual
const POR_FOLHA = 8;

const porId = k => ETAPAS.findIndex(e => e.k === k);
const etapa = () => ETAPAS[i];

/* ─────────────────────────── navegação ─────────────────────────── */

function ir(n, empilhar){
  if (n < 0 || n >= ETAPAS.length) return;
  if (ETAPAS[n].t === 'resultados') folhaDe[ETAPAS[n].k] = 0;
  if (empilhar !== false) historia.push(n);
  i = n;
  pintar();
}

function irPara(k){
  const n = porId(k);
  if (n < 0){ console.warn('etapa inexistente:', k); return; }
  ir(n);
}

/* A folha seguinte é a vizinha, a menos que a etapa atual diga outra coisa —
   é assim que a bifurcação muda o rumo sem que a lista de etapas mude. */
function adiante(){
  const e = etapa();
  if (e.t === 'bifurcacao'){
    const esc = escolhas[e.k];
    if (esc === undefined) return;
    irPara(e.caminhos[esc].vai);
    return;
  }
  if (e.t === 'desfecho'){
    if (e.fecho) irPara(e.fecho); else mostrarRevisao();
    return;
  }
  if (e.t === 'resultados'){
    const n = (marcados[e.de] || new Set()).size;
    const folhas = Math.max(1, Math.ceil(n / POR_FOLHA));
    const f = folhaDe[e.k] || 0;
    if (f + 1 < folhas){ folhaDe[e.k] = f + 1; pintar(); return; }
  }
  if (i + 1 >= ETAPAS.length){ mostrarRevisao(); return; }
  ir(i + 1);
}

function atras(){
  const e = etapa();
  if (e.t === 'resultados' && (folhaDe[e.k] || 0) > 0){
    folhaDe[e.k] -= 1; pintar(); return;
  }
  if (historia.length < 2) return;
  historia.pop();
  i = historia[historia.length - 1];
  pintar();
}

/* Quando se pode virar a folha. Pergunta sem resposta e pedido sem nenhum
   exame marcado seguram a página: o caso não anda por cima de uma decisão que
   não foi tomada. */
function podeAdiante(){
  const e = etapa();
  if (e.t === 'pergunta') return !!(respostas[e.k] && respostas[e.k].feita);
  if (e.t === 'bifurcacao') return escolhas[e.k] !== undefined;
  if (e.t === 'pedido') return (marcados[e.k] || new Set()).size > 0;
  return true;
}

/* ─────────────────────────── o trilho ─────────────────────────── */

/* Só as etapas que pedem alguma coisa do grupo entram no trilho: contar
   páginas de prosa transformaria o progresso em barra de rolagem. */
const PASSOS = ETAPAS.map((e, n) => ({e: e, n: n}))
  .filter(x => ['pedido', 'pergunta', 'bifurcacao'].includes(x.e.t));

/* O trilho mostra TODAS as etapas, uma marca cada, colorida pelo tipo — e um
   contador explícito. É assim que o formato antigo do New England fazia, e a
   diferença é real: dá para ver quantas páginas faltam e onde estão as
   perguntas antes de chegar nelas. */
function pintarTrilho(){
  $('#trilho').innerHTML =
    '<span class="tt">' + CASO.titulo + '</span>'
    + '<span class="cnt">' + (i + 1) + ' / ' + ETAPAS.length + '</span>'
    + '<span class="marcas">' + ETAPAS.map((e, k) =>
        // o título só aparece no que já foi percorrido: com o mouse parado
        // sobre uma marca à frente, o trilho entregava os desfechos — inclusive
        // qual deles é o ruim — antes de a bifurcação ser feita
        '<i class="m-' + e.t + (k < i ? ' feita' : k === i ? ' aqui' : '')
        + '" data-n="' + k + '"'
        + (k < i ? ' title="' + (e.tt || e.kicker || '').replace(/"/g, '') + '"' : '')
        + '></i>'
      ).join('') + '</span>';
  // andar para trás pelo trilho é livre; para a frente, não — o caso não pula
  // uma decisão que ainda não foi tomada
  $('#trilho').querySelectorAll('.marcas i').forEach(m => {
    const n = +m.dataset.n;
    if (n < i) m.onclick = () => ir(n);
  });
}

function pintarPe(){
  const e = etapa();
  const fim = e.t === 'desfecho';
  $('#pe').innerHTML =
    '<span class="rod">' + CASO.rodape + '</span>'
    + '<span class="nav">'
    + '<button class="bt" id="voltar"' + (historia.length < 2 ? ' disabled' : '') + '>Voltar</button>'
    + '<button class="bt forte" id="seguir"' + (podeAdiante() ? '' : ' disabled') + '>'
    + (fim ? 'Ver a revisão' : 'Avançar') + '</button></span>';
  $('#voltar').onclick = atras;
  $('#seguir').onclick = adiante;
}

/* ─────────────────────────── desenho das etapas ─────────────────────────── */

const fundoDe = e => e.fundo
  ? '<div class="fundo" style="background-image:url(' + e.fundo + ')"></div>'
  : '<div class="fundo" style="background:#0d1014"></div>';

const laminaDe = l => !l ? '' :
  '<figure class="lamina"><img src="' + l.img + '" alt="' + l.tt + '">'
  + '<figcaption class="cap"><b>' + l.tt + '</b>' + l.lg
  + '<span class="cr">' + l.cr + '</span></figcaption></figure>';

function pintar(){
  const e = etapa();
  $('#palco').innerHTML = '<section class="tela on">' + DESENHO[e.t](e) + '</section>';
  ligar(e);
  pintarTrilho();
  pintarPe();
}

const DESENHO = {

  capa: e =>
    fundoDe(e) + '<div class="veu esq"></div>'
    + '<div class="plano">'
    + (e.kicker ? '<div class="marca"><i></i><span>' + e.kicker + '</span></div>' : '')
    + '<h1>' + e.tt + '</h1><p class="lede">' + e.lede + '</p>'
    + e.nums + e.terrs
    + (e.ressalva ? '<div class="ress">' + e.ressalva + '</div>' : '')
    + '</div>' + laminaDe(e.lamina),

  /* Quando o rótulo é mais informativo que a manchete — "onde dava para ter
     chegado antes" contra "a retrospectiva" — quem sobe a título é o rótulo, e
     a manchete curta sai. O caso declara isso com `so_kicker`. */
  pagina: e =>
    fundoDe(e) + '<div class="veu ' + (e.lamina ? 'esq' : 'tudo') + '"></div>'
    + '<div class="plano' + (e.lamina ? '' : ' centro') + '">'
    + (e.so_kicker
        ? '<h2 class="do-kicker">' + e.kicker + '</h2>'
        : '<div class="marca"><i></i><span>' + e.kicker + '</span></div>'
          + '<h2>' + e.tt + '</h2>')
    + e.corpo + '</div>'
    + laminaDe(e.lamina),

  pedido: e =>
    fundoDe(e) + '<div class="veu tudo"></div>'
    + '<div class="folha">'
    + '<div class="marca"><i></i><span>' + e.kicker + '</span></div>'
    + '<h2>' + e.tt + '</h2><p class="sub">' + e.enunciado + '</p>'
    + '<div class="grupos">' + e.grupos.map(g =>
        '<div class="gr g-' + g.s + '"><b><i></i>' + g.n + '</b>'
        + g.o.map(o =>
            '<label class="it' + (temMarcado(e.k, o.e) ? ' on' : '') + '" '
            + 'data-ex="' + esc(o.e) + '"><span class="cx"></span>'
            + '<span class="n">' + o.e
            + (o.d ? '<span class="d">' + o.d + '</span>' : '') + '</span></label>'
          ).join('') + '</div>').join('')
    + '</div><div class="conta" id="conta"></div></div>',

  // Sem manchete: o rótulo já diz "o que voltou", e o primeiro cartão vira o
  // topo visual. Ganha noventa pixels e a tela começa no dado.
  resultados: e => {
    const todos = [...(marcados[e.de] || [])];
    const folhas = Math.max(1, Math.ceil(todos.length / POR_FOLHA));
    const f = Math.min(folhaDe[e.k] || 0, folhas - 1);
    const pedidos = todos.slice(f * POR_FOLHA, (f + 1) * POR_FOLHA);
    const sobre = (ETAPAS[porId(e.de)] || {}).sobre || {};
    const cartas = pedidos.map(n => {
      // o resultado que o caso declarou vence o do banco: o banco foi escrito
      // para um formato com relógio, e aqui não há relógio
      const x = sobre[n] || BANCO[n];
      if (!x) return '';
      const im = e.laminas[n];
      return '<article class="rc' + (x.a ? ' alt' : '') + '"><b>' + n + '</b>'
        + '<div class="v">' + x.r
        + (x.ref && x.ref !== '—' ? '<span class="rf">referência: ' + x.ref
            + '</span>' : '') + '</div>'
        + (im ? '<figure><img src="' + im.img + '" alt="' + n + '">'
            + '<figcaption>' + im.lg + ' · ' + im.cr + '</figcaption></figure>' : '')
        + '</article>';
    }).join('');
    return fundoDe(e) + '<div class="veu tudo"></div><div class="folha">'
      + '<div class="marca larga"><i></i><span>' + e.kicker
      + (folhas > 1 ? ' · folha ' + (f + 1) + ' de ' + folhas : '') + '</span>'
      + (e.intro ? '<b class="sub-in">' + e.intro + '</b>' : '') + '</div>'
      + '<div class="res">' + (cartas
          || '<div class="vazio">Você não pediu nenhum exame nesta etapa. O caso '
             + 'segue com o que se sabe do leito.</div>') + '</div></div>';
  },

  pergunta: e => {
    const r = respostas[e.k] || {marcadas: [], feita: false};
    return fundoDe(e) + '<div class="veu tudo"></div><div class="folha q">'
      + '<div class="marca"><i></i><span>' + e.kicker + '</span></div>'
      + '<p class="enun">' + e.enunciado + '</p>'
      + '<div class="qdica">' + (r.feita ? e.tr
          : 'selecione ' + (e.escolhas === 1 ? 'uma' : 'duas')) + '</div>'
      + '<ul class="alts' + (r.feita ? ' feita' : '') + '">'
      + e.alts.map((a, k) =>
          '<li data-k="' + k + '" class="' + (a.ok ? 'certa' : 'errada')
          + (r.marcadas.includes(k) ? ' marcada' : '') + '">'
          + '<span class="k">' + String.fromCharCode(65 + k) + '</span>'
          + '<span><span class="tx">' + a.t + '</span>'
          + '<span class="cm">' + a.c + '</span></span></li>').join('')
      + '</ul>'
      + (r.feita ? '' : '<button class="conf" id="conf"'
          + (r.marcadas.length >= e.escolhas ? '' : ' disabled') + '>'
          + 'Confirmar resposta</button>')
      + '</div>';
  },

  bifurcacao: e => {
    const esc = escolhas[e.k];
    return fundoDe(e) + '<div class="veu tudo"></div><div class="folha">'
      + '<div class="marca"><i></i><span>' + e.kicker + '</span></div>'
      + '<h2>' + e.tt + '</h2><p class="sub">' + e.enunciado + '</p>'
      + '<div class="cams' + (esc !== undefined ? ' feita' : '') + '">'
      + e.caminhos.map((c, k) =>
          '<div class="cam' + (esc === k ? ' escolhido' : '') + '" data-k="' + k + '">'
          + '<span class="l">' + String.fromCharCode(65 + k) + '</span>'
          + '<span class="r">' + c.r + '</span>'
          + '<span class="c">' + c.c + '</span></div>').join('')
      + '</div></div>';
  },

  desfecho: e =>
    fundoDe(e) + '<div class="veu tudo q-' + e.q + '"></div>'
    + '<div class="fim ' + e.q + '"><div class="caixa">'
    + '<div class="marca"><i></i><span>' + e.kicker + '</span></div>'
    + '<h1>' + e.tt + '</h1>' + e.corpo
    + '<div class="porque"><b>Por quê</b><p>' + e.porque + '</p></div>'
    + '</div></div>',
};

/* ─────────────────────────── interação ─────────────────────────── */

const esc = s => s.replace(/"/g, '&quot;');
const temMarcado = (k, n) => (marcados[k] || new Set()).has(n);

function ligar(e){
  if (e.t === 'pedido'){
    const conj = marcados[e.k] || (marcados[e.k] = new Set());
    const contar = () => {
      $('#conta').innerHTML = '<b>' + conj.size + '</b> '
        + (conj.size === 1 ? 'exame marcado' : 'exames marcados')
        + ' · nada é obrigatório, e nada é sugerido';
      pintarPe();
    };
    document.querySelectorAll('.it[data-ex]').forEach(l => {
      l.onclick = () => {
        const n = l.dataset.ex;
        if (conj.has(n)) conj.delete(n); else conj.add(n);
        l.classList.toggle('on');
        contar();
      };
    });
    contar();
  }

  if (e.t === 'pergunta'){
    const r = respostas[e.k] || (respostas[e.k] = {marcadas: [], feita: false});
    if (r.feita) return;
    document.querySelectorAll('.alts li').forEach(li => {
      li.onclick = () => {
        const k = +li.dataset.k;
        const j = r.marcadas.indexOf(k);
        // marcar e desmarcar até confirmar: a escolha não é irreversível
        // enquanto o grupo ainda está discutindo
        if (j >= 0) r.marcadas.splice(j, 1);
        else if (r.marcadas.length < e.escolhas) r.marcadas.push(k);
        else { r.marcadas.shift(); r.marcadas.push(k); }
        document.querySelectorAll('.alts li').forEach((x, n) =>
          x.classList.toggle('marcada', r.marcadas.includes(n)));
        const b = $('#conf');
        if (b) b.disabled = r.marcadas.length < e.escolhas;
      };
    });
    const conf = $('#conf');
    if (conf) conf.onclick = () => { r.feita = true; pintar(); };
  }

  if (e.t === 'bifurcacao'){
    if (escolhas[e.k] !== undefined) return;
    document.querySelectorAll('.cam').forEach(c => {
      c.onclick = () => { escolhas[e.k] = +c.dataset.k; pintar(); };
    });
  }
}

/* ─────────────────────────── a revisão do fim ─────────────────────────── */

/* O único lugar em que o caso comenta o que ficou de fora, e ele só fala
   quando não há mais nada a decidir. Durante a condução, apontar o que falta
   é decidir pelo grupo. */
function mostrarRevisao(){
  const pediu = new Set();
  Object.values(marcados).forEach(s => s.forEach(n => pediu.add(n)));
  const faltou = REVISAO.filter(r => !pediu.has(r.chave));
  const acertos = Object.entries(respostas).filter(([k, r]) => {
    const e = ETAPAS[porId(k)];
    return e && r.marcadas.every(x => e.alts[x].ok);
  }).length;
  const total = Object.keys(respostas).length;

  $('#palco').innerHTML = '<section class="tela on">'
    + '<div class="fundo" style="background:#0d1014"></div>'
    + '<div class="veu tudo"></div><div class="folha">'
    + '<div class="marca"><i></i><span>Revisão</span></div>'
    + '<h2>O que ficou para trás</h2>'
    + '<p class="sub">' + acertos + ' de ' + total + ' perguntas com a resposta '
    + 'inteiramente certa · ' + pediu.size + ' exames pedidos ao longo do caso.</p>'
    + '<div class="rev">' + (faltou.length
        ? faltou.map(r => '<div class="li"><b>' + r.rotulo + '</b><p>'
            + r.porque + '</p></div>').join('')
        : '<div class="ok">Nada essencial ficou de fora.</div>')
    + '</div></div></section>';
  $('#pe').innerHTML = '<span class="rod">' + CASO.rodape + '</span>'
    + '<span class="nav"><button class="bt" onclick="recomecar()">'
    + 'Conduzir de novo</button></span>';
  $('#trilho').innerHTML = '<span class="tt">' + CASO.titulo + '</span>';
}

function recomecar(){
  i = 0; historia = [0];
  Object.keys(marcados).forEach(k => delete marcados[k]);
  Object.keys(respostas).forEach(k => delete respostas[k]);
  Object.keys(escolhas).forEach(k => delete escolhas[k]);
  pintar();
}

/* ─────────────────────────── teclado ─────────────────────────── */

addEventListener('keydown', ev => {
  if (ev.key === 'ArrowRight' || ev.key === 'PageDown'){
    if (podeAdiante()) adiante();
    ev.preventDefault();
  } else if (ev.key === 'ArrowLeft' || ev.key === 'PageUp'){
    atras(); ev.preventDefault();
  }
});

pintar();

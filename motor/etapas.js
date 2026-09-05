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
/* As imagens viajam numa tabela à parte, uma vez cada: a etapa guarda
   só o nome do arquivo. */
const IMG = n => (DADOS.imgs || {})[n] || n || '';

const $ = s => document.querySelector(s);

/* ─────────────────────────── estado da sessão ─────────────────────────── */

let i = 0;                    // índice da etapa atual
const marcados = {};          // ident do pedido -> Set de nomes de exame
const respostas = {};         // ident da pergunta -> {marcadas:[], feita:bool}
const escolhas = {};          // ident da bifurcação -> índice do caminho
let historia = [0];           // pilha de etapas visitadas, para voltar
/* Numa peça página a página, rolar é trapaça. A folha vira duas só se os
   cartões não couberem — e desde que o pedido passou a ter teto, não cabem
   nunca: seis exames entram numa folha com folga. A paginação fica como rede
   de segurança para um caso futuro que peça mais. */
const folhaDe = {};           // ident da etapa de resultados -> folha atual
const laudos = new Set();     // exames com imagem cujo laudo já foi revelado
const POR_FOLHA = 9;

const porId = k => ETAPAS.findIndex(e => e.k === k);
/* Tudo o que já foi pedido em qualquer rodada, para os pré-requisitos e para
   as consequências do fim. */
function jaPedido(nome){
  return Object.values(marcados).some(c => c.has(nome));
}
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
  /* A rota é a ramificação de verdade: quem não pediu a prova não recebe a
     página que a discute. Sem isto, a peça perguntava "que exames você pede?" e
     depois seguia contando o resultado de exames que ninguém pediu — que é
     exatamente o vício que este formato existe para não ter. */
  if (e.rota){
    const pedidos = new Set();
    Object.values(marcados).forEach(c => c.forEach(n => pedidos.add(n)));
    const tem = e.rota.pediu.every(n => pedidos.has(n));
    irPara(tem ? e.rota.entao : e.rota.senao);
    return;
  }
  /* A evolução volta a se separar aqui: a página é a mesma para os três
     caminhos até o ponto em que o hemograma deixa de ser o mesmo. */
  if (e.conforme){
    const k = escolhas[e.conforme.de];
    irPara(e.conforme.para[k === undefined ? 0 : k]);
    return;
  }
  // `segue` deixa a ordem do arquivo de ser a única costura entre as páginas:
  // é o que permite três trilhas de tratamento convivendo na mesma lista
  if (e.segue){ irPara(e.segue); return; }
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

/* Desde que o caso ramifica, a lista de etapas deixou de ser o caminho: ela
   contém as páginas das DUAS rotas, e contar 27 num percurso de 19 é mentir
   para quem olha o trilho. Esta função percorre o caso a partir do estado
   atual e devolve só as páginas que este percurso vai ver. */
function rotaAtual(){
  const seq = [], visto = new Set();
  const pedidos = new Set();
  Object.values(marcados).forEach(c => c.forEach(x => pedidos.add(x)));
  let n = 0;
  while (n >= 0 && n < ETAPAS.length && !visto.has(n)){
    visto.add(n); seq.push(n);
    const e = ETAPAS[n];
    if (e.t === 'bifurcacao'){
      const esc = escolhas[e.k];
      n = porId(e.caminhos[esc === undefined ? 0 : esc].vai);
    } else if (e.t === 'desfecho'){
      n = e.fecho ? porId(e.fecho) : -1;
    } else if (e.rota){
      n = porId(e.rota.pediu.every(x => pedidos.has(x))
                ? e.rota.entao : e.rota.senao);
    } else if (e.conforme){
      const k = escolhas[e.conforme.de];
      n = porId(e.conforme.para[k === undefined ? 0 : k]);
    } else if (e.segue){
      n = porId(e.segue);
    } else n = n + 1;
  }
  return seq;
}

/* O trilho mostra as etapas do percurso, uma marca cada, colorida pelo tipo —
   e um contador explícito. É assim que o formato antigo do New England fazia,
   e a diferença é real: dá para ver quantas páginas faltam e onde estão as
   perguntas antes de chegar nelas. */
function pintarTrilho(){
  const seq = rotaAtual();
  const aqui = Math.max(seq.indexOf(i), 0);
  $('#trilho').innerHTML =
    '<span class="tt">' + CASO.titulo + '</span>'
    + '<span class="cnt">' + (aqui + 1) + ' / ' + seq.length + '</span>'
    + '<span class="marcas">' + seq.map(n => ETAPAS[n]).map((e, k) =>
        // o título só aparece no que já foi percorrido: com o mouse parado
        // sobre uma marca à frente, o trilho entregava os desfechos — inclusive
        // qual deles é o ruim — antes de a bifurcação ser feita
        '<i class="m-' + e.t + (k < aqui ? ' feita' : k === aqui ? ' aqui' : '')
        + '" data-n="' + seq[k] + '"'
        + (k < aqui ? ' title="' + (e.tt || e.kicker || '').replace(/"/g, '') + '"' : '')
        + '></i>'
      ).join('') + '</span>';
  // andar para trás pelo trilho é livre; para a frente, não — o caso não pula
  // uma decisão que ainda não foi tomada
  const vistos = new Set(historia);
  $('#trilho').querySelectorAll('.marcas i').forEach(m => {
    const n = +m.dataset.n;
    if (vistos.has(n) && n !== i) m.onclick = () => ir(n);
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
  ? '<div class="fundo" style="background-image:url(' + IMG(e.fundo) + ')"></div>'
  : '<div class="fundo" style="background:#0d1014"></div>';

const laminaDe = l => !l ? '' :
  '<figure class="lamina"><img src="' + IMG(l.img) + '" alt="' + l.tt + '">'
  + '<figcaption class="cap"><b>' + l.tt + '</b>' + l.lg
  + '<span class="cr">' + l.cr + '</span></figcaption></figure>';

/* Figura anotada e boneco vêm do caso como HTML pronto, montado antes de
   existir data: URI. Cada um deixa o nome do arquivo em `data-img` e o
   endereço é resolvido aqui, contra a mesma tabela de imagens. */
function resolverImagens(){
  document.querySelectorAll('[data-img]').forEach(el => {
    const u = IMG(el.dataset.img);
    if (el.tagName.toLowerCase() === 'image') el.setAttribute('href', u);
    else el.setAttribute('src', u);
  });
}

/* ─────────────────────── a lupa ─────────────────────── */

/* Tomografia lida num cartão de 300 px é decoração. Qualquer figura da peça
   abre em tela cheia por clique, com a legenda embaixo, e fecha por clique,
   por Esc ou pelo botão. Enquanto a lupa está aberta as setas do teclado
   param de virar página: elas pertencem à figura, não ao caso. */
let lupaAberta = false;

function abrirLupa(figura){
  const clone = figura.cloneNode(true);
  clone.classList.remove('lamina');
  const cx = document.createElement('div');
  cx.className = 'lupa';
  cx.innerHTML = '<button class="fechar" title="Fechar (Esc)">Fechar ✕</button>';
  const quadro = document.createElement('div');
  quadro.className = 'quadro';
  quadro.appendChild(clone);
  cx.appendChild(quadro);
  document.body.appendChild(cx);
  lupaAberta = true;
  const fechar = () => {
    cx.remove(); lupaAberta = false;
    document.removeEventListener('keydown', porTecla, true);
  };
  const porTecla = ev => {
    if (ev.key === 'Escape'){ ev.stopPropagation(); fechar(); }
  };
  document.addEventListener('keydown', porTecla, true);
  cx.onclick = ev => { if (!quadro.contains(ev.target) || ev.target.tagName === 'IMG') fechar(); };
  cx.querySelector('.fechar').onclick = fechar;
}

function ligarLupa(){
  document.querySelectorAll('#palco figure').forEach(f => {
    if (!f.querySelector('img,svg')) return;
    f.classList.add('amplia');
    f.title = 'Clique para ampliar';
    f.onclick = () => abrirLupa(f);
  });
}

function pintar(){
  const e = etapa();
  $('#palco').innerHTML = '<section class="tela on">' + DESENHO[e.t](e) + '</section>';
  resolverImagens();
  ligarLupa();
  ligar(e);
  pintarTrilho();
  pintarPe();
}

const DESENHO = {

  /* Título e imagem. A imagem sobe do chão para a tela inteira, sem véu de
     leitura por cima dela senão o gradiente que segura o título. */
  capa: e =>
    '<div class="fundo capa-fundo" style="background-image:url(' + IMG(e.fundo) + ')"></div>'
    + '<div class="veu capa-veu"></div>'
    + '<div class="abertura">'
    + (e.kicker ? '<div class="marca"><i></i><span>' + e.kicker + '</span></div>' : '')
    + '<h1>' + e.tt + '</h1>'
    + (e.selo ? '<div class="selo">' + e.selo + '</div>' : '')
    + '</div>',

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
        + g.o.map(o => {
            /* Um exame com pré-requisito continua VISÍVEL e fica travado, com
               o motivo escrito. Esconder ensinaria que ele não existe; o que
               se quer ensinar é que ele ainda não se justifica. */
            const falta = (o.ex || []).filter(x => !jaPedido(x));
            const trava = falta.length > 0;
            return '<label class="it' + (temMarcado(e.k, o.e) ? ' on' : '')
              + (trava ? ' trava' : '') + '" data-ex="' + esc(o.e) + '">'
              + '<span class="cx"></span><span class="n">' + o.e
              + (o.d ? '<span class="d">' + o.d + '</span>' : '')
              + (trava ? '<span class="d trv">' + o.pq + ' — falta: '
                  + falta.join(', ') + '</span>' : '')
              + '</span></label>';
          }).join('') + '</div>').join('')
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
      /* O laudo do sedimento tem cinco achados separados por ponto médio, e
         num parágrafo corrido o cilindro hemático — que é o achado — passava
         no meio da frase. Cada parte vira uma linha. */
      const partes = x.r.split(' · ');
      const valor = partes.length > 1
        ? partes.map(t => '<span class="ln">' + t + '</span>').join('')
        : x.r;
      /* Quando o exame tem imagem, a imagem vem SOZINHA e o laudo fica atrás
         de um botão. Colar o laudo na figura tira do grupo o passo que mais
         ensina em imagem, que é descrever antes de ler o que outro escreveu —
         e é invariante declarada do formato: laudo se revela, não se
         renderiza junto. */
      const laudo = '<div class="v">' + valor
        + (x.ref && x.ref !== '—' ? '<span class="rf">referência: ' + x.ref
            + '</span>' : '') + '</div>';
      if (!im)
        return '<article class="rc' + (x.a ? ' alt' : '') + '"><b>' + n + '</b>'
          + laudo + '</article>';
      const aberto = laudos.has(n);
      return '<article class="rc' + (x.a ? ' alt' : '') + '"><b>' + n + '</b>'
        + '<figure><img src="' + IMG(im.img) + '" alt="' + n + '">'
        + '<figcaption>' + im.lg + ' · ' + im.cr + '</figcaption></figure>'
        + (aberto ? laudo
            : '<button class="verlaudo" data-laudo="' + esc(n) + '">'
              + 'Ver o laudo</button>')
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
    return fundoDe(e) + '<div class="veu tudo"></div>'
      + '<div class="folha q' + (e.alts.length > 6 ? ' densa' : '') + '">'
      + '<div class="marca"><i></i><span>' + e.kicker + '</span></div>'
      + '<p class="enun">' + e.enunciado + '</p>'
      + '<div class="qdica">' + (r.feita ? e.tr
          : (e.escolhas === 1 ? 'selecione uma'
             : 'selecione ' + e.escolhas + ' · marcadas ' + r.marcadas.length))
      + '</div>'
      + '<ul class="alts' + (r.feita ? ' feita' : '')
          + (e.alts.length > 6 ? ' muitas' : '') + '">'
      + e.alts.map((a, k) =>
          '<li data-k="' + k + '" class="' + (a.ok ? 'certa' : 'errada')
          + (r.marcadas.includes(k) ? ' marcada' : '') + '">'
          + '<span class="k">' + String.fromCharCode(65 + k) + '</span>'
          + '<span class="tx">' + a.t + '</span>'
          + '<span class="cm">' + a.c + '</span></li>').join('')
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
      + '</div>'
      /* Sem isto, a ramificação era invisível: as três justificativas abriam,
         o caso seguia, e nada na tela dizia que o rumo tinha mudado. */
      + (esc !== undefined
          ? '<div class="forca">' + e.caminhos.map((c, k) =>
              '<i class="' + (esc === k ? 'on' : '') + '"></i>').join('')
            + '<span>Daqui em diante o caso segue pelo caminho '
            + String.fromCharCode(65 + esc) + '. As próximas páginas — '
            + 'a prescrição, a evolução e o desfecho — são as dele, e são '
            + 'outras nos outros dois.</span></div>'
          : '')
      + '</div>';
  },

  /* O balanço: o que a condução custou, item a item, com o contrafactual ao
     lado. É a única tela do caso que só existe por causa do que VOCÊ fez. */
  balanco: e => {
    const disparadas = e.cons.filter(c => {
      if (c.q.sem) return !c.q.sem.some(n => jaPedido(n));
      if (c.q.escolheu) return escolhas[c.q.escolheu[0]] === c.q.escolheu[1];
      return false;
    });
    const dias = e.bd + disparadas.reduce((s, c) => s + c.d, 0);
    const tfg = e.bt - disparadas.reduce((s, c) => s + c.t, 0);
    return fundoDe(e) + '<div class="veu tudo"></div><div class="folha">'
      + '<div class="marca"><i></i><span>' + e.kicker + '</span></div>'
      + '<h2>' + e.tt + '</h2>' + e.corpo
      + '<div class="bal">'
      + '<div class="placar">'
      +   '<div><b>' + dias + '</b><span>dias de internação</span></div>'
      +   '<div' + (tfg <= 15 ? ' class="grave"' : '') + '><b>' + tfg
      +     '</b><span>mL/min/1,73 m² na alta'
      +     (tfg <= 15 ? ' · saiu em diálise' : '') + '</span></div>'
      +   '<div class="ideal"><b>' + e.bd + ' · ' + e.bt + '</b>'
      +     '<span>o melhor percurso possível</span></div>'
      + '</div>'
      + (disparadas.length
          ? '<div class="cons">' + disparadas.map(c =>
              '<div class="cn"><b>' + c.tt + '</b>'
              + '<span class="pr">' + (c.d ? '+' + c.d + ' dias' : '')
              + (c.d && c.t ? ' · ' : '') + (c.t ? '−' + c.t + ' mL/min' : '')
              + '</span><p>' + c.pq + '</p></div>').join('') + '</div>'
          : '<div class="cons"><div class="cn limpo"><b>Nenhuma decisão desta '
            + 'condução cobrou preço.</b><p>Você chegou ao melhor percurso que '
            + 'este caso permite. É raro, e não é sorte: as decisões que '
            + 'custam caro aqui são todas das primeiras 72 horas.</p></div></div>')
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
    /* O teto é o que faz a pergunta ser uma pergunta. Sem ele, marcar tudo é
       sempre a jogada dominante — e um grupo que marca tudo não decidiu nada,
       além de encerrar a investigação na primeira tela. */
    const teto = e.limite || 0;
    const cheio = () => teto && conj.size >= teto;
    const contar = () => {
      const faltam = teto ? teto - conj.size : 0;
      $('#conta').innerHTML = '<b>' + conj.size
        + (teto ? ' de ' + teto : '') + '</b> '
        + (conj.size === 1 ? 'exame marcado' : 'exames marcados')
        + (teto
            ? (faltam > 0
                ? ' · ainda cabe' + (faltam === 1 ? ' 1' : 'm ' + faltam)
                : ' · o teto desta rodada está completo — desmarque para trocar')
            : ' · nada é obrigatório, e nada é sugerido');
      document.querySelectorAll('.it[data-ex]').forEach(l =>
        l.classList.toggle('bloq', cheio() && !conj.has(l.dataset.ex)));
      pintarPe();
    };
    document.querySelectorAll('.it[data-ex]').forEach(l => {
      l.onclick = () => {
        if (l.classList.contains('trava')) return;
        const n = l.dataset.ex;
        if (conj.has(n)) conj.delete(n);
        else if (cheio()) return;          // o teto não empurra: ele segura
        else conj.add(n);
        l.classList.toggle('on', conj.has(n));
        contar();
      };
    });
    contar();
  }

  if (e.t === 'resultados'){
    document.querySelectorAll('.verlaudo').forEach(b => {
      b.onclick = () => { laudos.add(b.dataset.laudo); pintar(); };
    });
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
  /* `respostas[k]` nasce quando a página é PINTADA, não quando é respondida, e
     `[].every()` é `true`: uma pergunta só visitada entrava no total e no
     acerto. Dava para chegar à revisão com "4 de 4" tendo respondido três. */
  const feitas = Object.entries(respostas).filter(([, r]) => r.feita);
  const acertos = feitas.filter(([k, r]) => {
    const e = ETAPAS[porId(k)];
    return e && r.marcadas.length === e.escolhas
             && r.marcadas.every(x => e.alts[x].ok);
  }).length;
  const total = feitas.length;

  $('#palco').innerHTML = '<section class="tela on">'
    + '<div class="fundo" style="background:#0d1014"></div>'
    + '<div class="veu tudo"></div><div class="folha">'
    + '<div class="marca"><i></i><span>Revisão</span></div>'
    + '<h2>O que ficou para trás</h2>'
    + '<p class="sub">' + acertos + ' de ' + total + ' perguntas de escolha com '
    + 'a resposta inteiramente certa · ' + Object.keys(marcados).length
    + ' rodadas de exames, ' + pediu.size + ' pedidos ao todo · '
    + Object.keys(escolhas).length + ' bifurcação de conduta.</p>'
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
  laudos.clear();
  pintar();
}

/* ─────────────────────────── teclado ─────────────────────────── */

addEventListener('keydown', ev => {
  if (lupaAberta) return;              // as setas são da figura enquanto ela está aberta
  if (ev.key === 'ArrowRight' || ev.key === 'PageDown'){
    if (podeAdiante()) adiante();
    ev.preventDefault();
  } else if (ev.key === 'ArrowLeft' || ev.key === 'PageUp'){
    atras(); ev.preventDefault();
  }
});

pintar();

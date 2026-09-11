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

let emRevisao = false;
let i = 0;                    // índice da etapa atual
const marcados = {};          // ident do pedido -> Set de nomes de exame
const respostas = {};         // ident da pergunta -> {marcadas:[], feita:bool}
const escolhas = {};          // ident da bifurcação -> índice do caminho
let historia = [0];           // pilha de etapas visitadas, para voltar
const laudos = new Set(); // laudos revelados por rodada de investigação

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
  if (empilhar !== false) historia.push(n);
  i = n; parteTela = 0; emRevisao=false;
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
  if (temProximaParte()){ virarParte(1); return; }
  if(emRevisao){recomecar();return;}
  const e = etapa();
  if(e.comentado){
    const r=respostas[e.k];if(!r?.feita)return;
    const alts=e.alts.filter(a=>a.ok);
    marcados[e.k]=new Set(alts.flatMap(a=>a.exames));
    r.conducao='indicados';
  }
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
  if (parteTela > 0){ virarParte(-1); return; }
  if(emRevisao){emRevisao=false;parteTela=0;pintar();return;}
  const e = etapa();
  if (historia.length < 2) return;
  historia.pop();
  i = historia[historia.length - 1];
  pintar();
}

/* Quando se pode virar a folha. Pergunta sem resposta e pedido sem nenhum
   exame marcado seguram a página: o caso não anda por cima de uma decisão que
   não foi tomada. */
function podeAdiante(){
  if (emRevisao || temProximaParte()) return true;
  const e = etapa();
  if (e.t === 'pergunta' || e.t === 'pareamento')
    return !!(respostas[e.k] && respostas[e.k].feita);
  if (e.t === 'bifurcacao') return escolhas[e.k] !== undefined;
  if (e.t === 'pedido') return e.comentado ? !!respostas[e.k]?.feita : (marcados[e.k] || new Set()).size > 0;
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
    '<a class="voltar-biblioteca" href="index.html" aria-label="Voltar à biblioteca"><svg viewBox="0 0 24 24"><rect x="3" y="3" width="7" height="7" rx="2"/><rect x="14" y="3" width="7" height="7" rx="2"/><rect x="3" y="14" width="7" height="7" rx="2"/><rect x="14" y="14" width="7" height="7" rx="2"/></svg><span>Biblioteca</span></a><span class="tt">' + CASO.titulo + '</span>'
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
  const corrigida=e.comentado && respostas[e.k]?.feita;
  $('#pe').innerHTML =
    '<span class="rod">' + CASO.rodape + '</span>'
    + '<span class="nav">'
    + (partesTela.length > 1 ? '<span class="pagina-indice">Página ' + (parteTela + 1) + ' de ' + partesTela.length + '</span>' : '')
    + '<button class="bt" id="voltar"' + (historia.length < 2 && parteTela === 0 ? ' disabled' : '') + '>Voltar</button>'
    + '<button class="bt forte" id="' + (emRevisao && !temProximaParte() ? 'reiniciar' : 'seguir') + '"' + (podeAdiante() ? '' : ' disabled') + '>'
    + (temProximaParte() ? 'Próxima página' : emRevisao ? 'Recomeçar' : e.t === 'capa' ? 'Começar o caso' : corrigida ? 'Realizar indicados' : fim ? 'Continuar' : 'Avançar') + '</button></span>';
  $('#voltar').onclick = atras;
  ($('#seguir') || $('#reiniciar')).onclick = adiante;
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
  document.querySelectorAll('#palco details').forEach((d,n)=>{const key=etapa().k+'::'+n;d.dataset.detalhe=key;d.open=detalhesAbertos.has(key);});
  ligar(e);
  montarFolhas();
  document.querySelectorAll('#palco details').forEach(d=>{const summary=d.querySelector('summary');if(summary)summary.onclick=ev=>{ev.preventDefault();const key=d.dataset.detalhe;d.open?detalhesAbertos.delete(key):detalhesAbertos.add(key);parteTela=0;pintar();};});
  ligarLupa();
  acessibilidadeDaPagina();
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

  pedido: e => e.comentado ? DESENHO.pergunta(e) :
    fundoDe(e) + '<div class="veu tudo"></div>'
    + '<div class="folha pedido">'
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
    const todos = e.todos ? e.todos : [...(marcados[e.de] || [])];
    const origem=respostas[e.de]?.conducao;
    const resumo=origem==='indicados'?'Exames realizados pela equipe após a discussão.':'';
    const pedidos = todos;
    const sobre = e.sobre || (ETAPAS[porId(e.de)] || {}).sobre || {};
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
      /* A legenda descritiva É o laudo. Deixá-la sob a figura enquanto um
         botão promete "ver o laudo" é entregar a leitura e cobrar o clique
         por nada: quem olhava a radiografia já lia "opacidades alveolares
         bilaterais predominando nos campos médios" antes de descrever coisa
         alguma. Sob a figura fica só o crédito; a descrição e o valor saem
         juntos, no clique. */
      const chaveLaudo = (e.de || e.k) + '::' + n;
      const aberto = laudos.has(chaveLaudo);
      return '<article class="rc' + (x.a ? ' alt' : '') + '"><b>' + n + '</b>'
        + '<figure><img src="' + IMG(im.img) + '" alt="' + n + '">'
        + '<figcaption class="soc">' + im.cr + '</figcaption></figure>'
        + (aberto
            ? laudo + '<div class="leglaudo">' + im.lg + '</div>'
            : '<button class="verlaudo" data-laudo="' + esc(chaveLaudo) + '">'
              + 'Ver o laudo</button>')
        + '</article>';
    }).join('');
    return fundoDe(e) + '<div class="veu tudo"></div><div class="folha">'
      + '<div class="marca larga"><i></i><span>' + e.kicker
      + '</span>'
      + (resumo || e.intro ? '<b class="sub-in">' + resumo + ' ' + (e.intro || '').replace(/(?:De novo, só o que foi marcado\.|Só o que foi marcado\.)/g,'') + '</b>' : '') + '</div>'
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
          + '<span class="cm">' + (r.feita ? '<span class="estado-resposta">' + (e.comentado ? a.situacao : (a.ok ? 'Correta' : 'Incorreta')) + (r.marcadas.includes(k) ? ' · sua seleção' : '') + '</span>' : '') + a.c + '</span></li>').join('')
      + '</ul>'
      + (r.feita ? '' : '<button class="conf" id="conf"'
          + (r.marcadas.length >= e.escolhas ? '' : ' disabled') + '>'
          + 'Confirmar resposta</button>')
      + '</div>';
  },

  /* Pareamento: cada item tem a sua linha de letras. Marcar é atribuir uma
     letra ao item; a mesma letra pode servir a mais de um item, porque é
     assim na prova — e porque proibir a repetição entregaria a resposta por
     exclusão. */
  pareamento: e => {
    const r = respostas[e.k] || {marcadas: [], feita: false};
    const L = n => String.fromCharCode(65 + n);
    return fundoDe(e) + '<div class="veu tudo"></div>'
      + '<div class="folha q par-folha">'
      + '<div class="marca"><i></i><span>' + e.kicker + '</span></div>'
      + '<p class="enun">' + e.enunciado + '</p>'
      + '<div class="qdica">' + (r.feita ? e.tr
          : 'atribua uma letra a cada item · ' + r.marcadas.filter(x => x !== undefined && x !== null).length
            + ' de ' + e.itens.length) + '</div>'
      + '<div class="par' + (r.feita ? ' feita' : '') + '">'
      + '<div class="par-ops">' + e.ops.map((o, n) =>
          '<span class="po"><b>' + L(n) + '</b>' + o + '</span>').join('') + '</div>'
      + '<div class="par-itens">' + e.itens.map((it, n) => {
          const esc = r.marcadas[n];
          const certa = r.feita && esc === it.ok;
          return '<div class="pi' + (r.feita ? (certa ? ' certa' : ' errada') : '')
            + '" data-n="' + n + '">'
            + '<span class="pt">' + it.t + '</span>'
            + '<span class="pesc">' + e.ops.map((o, m) =>
                '<i class="pe' + (esc === m ? ' on' : '')
                + (r.feita && m === it.ok ? ' ok' : '') + '" data-m="' + m
                + '" title="' + esc2(o) + '">' + L(m) + '</i>').join('') + '</span>'
            + (r.feita ? '<span class="cm"><span class="estado-resposta">'
                + (certa ? 'Correta' : 'Incorreta · a resposta é ' + L(it.ok)
                    + (esc === undefined || esc === null ? '' : ' · você marcou ' + L(esc)))
                + '</span>' + it.c + '</span>' : '')
            + '</div>';
        }).join('') + '</div></div>'
      + (r.feita ? '' : '<button class="conf" id="conf"'
          + (e.itens.every((_, n) => r.marcadas[n] !== undefined && r.marcadas[n] !== null) ? '' : ' disabled')
          + '>Confirmar resposta</button>')
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
    const bateu = q => {
      if (q.sem) return !q.sem.some(n => jaPedido(n));
      if (q.escolheu) return escolhas[q.escolheu[0]] === q.escolheu[1];
      if (q.escolheu_todos)
        return q.escolheu_todos.every(([k, v]) => escolhas[k] === v);
      return false;
    };
    const disparadas = e.cons.filter(c => bateu(c.q));
    const morreu = e.obito && bateu(e.obito);
    const dias = e.bd + disparadas.reduce((s, c) => s + c.d, 0);
    const tfg = e.bt - disparadas.reduce((s, c) => s + c.t, 0);
    return fundoDe(e) + '<div class="veu tudo"></div><div class="folha">'
      + '<div class="marca"><i></i><span>' + e.kicker + '</span></div>'
      + '<h2>' + e.tt + '</h2>' + e.corpo
      + '<div class="bal">'
      + (morreu
        ? '<div class="placar obito"><div class="cheio"><b>Óbito</b><span>'
          + e.obitotx + '</span></div></div>'
        : '<div class="placar">'
      +   '<div><b>' + dias + '</b><span>dias de internação</span></div>'
      +   '<div' + (tfg <= 15 ? ' class="grave"' : '') + '><b>' + tfg
      +     '</b><span>mL/min/1,73 m² na alta'
      +     (tfg <= 15 ? ' · saiu em diálise' : '') + '</span></div>'
      +   '<div class="ideal"><b>' + e.bd + ' · ' + e.bt + '</b>'
      +     '<span>o melhor percurso possível</span></div>'
      + '</div>')
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
const esc2 = s => String(s).replace(/<[^>]+>/g, '').replace(/"/g, '&quot;');
const temMarcado = (k, n) => (marcados[k] || new Set()).has(n);

function ligar(e){
  if (e.t === 'pedido' && !e.comentado){
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
        pintar();
        const atual=[...document.querySelectorAll('.it')].find(x=>x.dataset.ex===n);
        if(atual?.getClientRects().length)atual.focus({preventScroll:true});
      };
    });
    contar();
  }

  if (e.t === 'resultados'){
    document.querySelectorAll('.verlaudo').forEach(b => {
      b.onclick = () => {
        const nome=b.closest('.rc').querySelector('b').textContent;
        laudos.add(b.dataset.laudo);pintar();
        const cartao=[...document.querySelectorAll('.rc')].find(c=>c.querySelector('b')?.textContent===nome&&c.querySelector('.v'));
        const parte=partesTela.findIndex(p=>p.some(n=>n===cartao||n.contains(cartao)));
        if(parte>=0){parteTela=parte;aplicarParte();pintarPe();}
      };
    });
  }

  if (e.t === 'pergunta' || e.comentado){
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
    if (conf) conf.onclick = () => {
      if(r.marcadas.length!==e.escolhas)return;
      r.feita = true;
      if(e.comentado)marcados[e.k]=new Set(e.alts.filter(a=>a.ok).flatMap(a=>a.exames));
      parteTela=0; pintar();
    };
  }

  if (e.t === 'pareamento'){
    const r = respostas[e.k] || (respostas[e.k] = {marcadas: [], feita: false});
    if (r.feita) return;
    document.querySelectorAll('.par .pe').forEach(ch => {
      ch.onclick = ev => {
        ev.stopPropagation();
        const n = +ch.closest('.pi').dataset.n, m = +ch.dataset.m;
        r.marcadas[n] = (r.marcadas[n] === m) ? undefined : m;
        const linha = ch.closest('.pi');
        linha.querySelectorAll('.pe').forEach(x => x.classList.toggle('on', +x.dataset.m === r.marcadas[n]));
        const completo = e.itens.every((_, k) => r.marcadas[k] !== undefined && r.marcadas[k] !== null);
        const b = $('#conf'); if (b) b.disabled = !completo;
        const d = document.querySelector('.qdica');
        if (d) d.textContent = 'atribua uma letra a cada item · '
          + e.itens.filter((_, k) => r.marcadas[k] !== undefined && r.marcadas[k] !== null).length
          + ' de ' + e.itens.length;
      };
    });
    const conf = $('#conf');
    if (conf) conf.onclick = () => {
      if (!e.itens.every((_, k) => r.marcadas[k] !== undefined && r.marcadas[k] !== null)) return;
      r.feita = true; parteTela = 0; pintar();
    };
  }

  if (e.t === 'bifurcacao'){
    if (escolhas[e.k] !== undefined) return;
    document.querySelectorAll('.cam').forEach(c => {
      c.onclick = () => { escolhas[e.k] = +c.dataset.k; parteTela=0; pintar(); };
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
    if (!e) return false;
    if (e.t === 'pareamento')
      return e.itens.every((it, n) => r.marcadas[n] === it.ok);
    return r.marcadas.length === e.escolhas && r.marcadas.every(x => e.alts[x].ok);
  }).length;
  const total = feitas.length;

  $('#palco').innerHTML = '<section class="tela on">'
    + '<div class="fundo" style="background:#0d1014"></div>'
    + '<div class="veu tudo"></div><div class="folha">'
    + '<div class="marca"><i></i><span>Revisão</span></div>'
    + '<h2>O que ficou para trás</h2>'
    + '<p class="sub">' + acertos + ' de ' + total + ' perguntas de escolha com '
    + 'a resposta inteiramente certa · '
    + (pediu.size ? Object.keys(marcados).length + ' rodadas de exames, ' + pediu.size + ' pedidos ao todo · ' : '')
    + Object.keys(escolhas).length + ' decisões de conduta.</p>'
    + '<div class="rev">' + (faltou.length
        ? faltou.map(r => '<div class="li"><b>' + r.rotulo + '</b><p>'
            + r.porque + '</p></div>').join('')
        : '<div class="ok">Nada essencial ficou de fora.</div>')
    + '</div></div></section>';
  $('#pe').innerHTML = '<span class="rod">' + CASO.rodape + '</span>'
    + '<span class="nav"><button class="bt" onclick="recomecar()">'
    + 'Conduzir de novo</button></span>';
  $('#trilho').innerHTML = '<a class="voltar-biblioteca" href="index.html" aria-label="Voltar à biblioteca"><svg viewBox="0 0 24 24"><rect x="3" y="3" width="7" height="7" rx="2"/><rect x="14" y="3" width="7" height="7" rx="2"/><rect x="3" y="14" width="7" height="7" rx="2"/><rect x="14" y="14" width="7" height="7" rx="2"/></svg><span>Biblioteca</span></a><span class="tt">' + CASO.titulo + '</span>';
  emRevisao=true;parteTela=0;montarFolhas();pintarPe();
}

function recomecar(){
  i = 0; historia = [0]; emRevisao=false;
  Object.keys(marcados).forEach(k => delete marcados[k]);
  Object.keys(respostas).forEach(k => delete respostas[k]);
  Object.keys(escolhas).forEach(k => delete escolhas[k]);
  laudos.clear(); detalhesAbertos.clear(); parteTela=0;
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

let resizeTela;
addEventListener("resize",()=>{clearTimeout(resizeTela);resizeTela=setTimeout(()=>{if(!lupaAberta){if(emRevisao)mostrarRevisao();else pintar();}},120);});
pintar();

function acessibilidadeDaPagina(){
  document.querySelectorAll('.it,.cam,.alts li,figure.amplia,.par .pe').forEach(el=>{
    el.tabIndex=0;el.setAttribute('role',el.classList.contains('it')?'checkbox':'button');
    if(el.classList.contains('it'))el.setAttribute('aria-checked',el.classList.contains('on')?'true':'false');
    el.addEventListener('keydown',ev=>{if(ev.key==='Enter'||ev.key===' '){ev.preventDefault();ev.stopPropagation();el.click();}});
  });
}

const D = JSON.parse(document.getElementById('dados').textContent);
const IC = {
  grade:'<rect x="3" y="3" width="7" height="7" rx="2"/><rect x="14" y="3" width="7" height="7" rx="2"/><rect x="3" y="14" width="7" height="7" rx="2"/><rect x="14" y="14" width="7" height="7" rx="2"/>',
  pergunta:'<circle cx="12" cy="12" r="9"/><path d="M9.6 9.3a2.5 2.5 0 1 1 3.6 2.3c-.8.4-1.2 1-1.2 1.8v.4"/><path d="M12 17h.01"/>',
  decisao:'<circle cx="6" cy="5" r="2"/><circle cx="18" cy="5" r="2"/><circle cx="12" cy="19" r="2"/><path d="M6 7v1a5 5 0 0 0 5 5h2a5 5 0 0 0 5-5V7M12 13v4"/>',
  foto:'<rect x="3" y="5" width="18" height="14" rx="3"/><circle cx="9" cy="10" r="1.6"/><path d="M21 16l-5-5-9 8"/>',
  relogio:'<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
  livro:'<path d="M4 5a2 2 0 0 1 2-2h13v16H6a2 2 0 0 0-2 2z"/><path d="M4 21a2 2 0 0 1 2-2h13"/>',
  seta:'<path d="M5 12h14M13 6l6 6-6 6"/>', play:'<path d="M8 5v14l11-7z"/>',
  check:'<path d="M5 12.5l4.5 4.5L19 7.5"/>', refazer:'<path d="M3 12a9 9 0 1 0 3-6.7"/><path d="M3 4v5h5"/>',
  busca:'<circle cx="10.5" cy="10.5" r="6.5"/><path d="M20 20l-4.5-4.5"/>',
  todos:'<rect x="3" y="3" width="7" height="7" rx="2"/><rect x="14" y="3" width="7" height="7" rx="2"/><rect x="3" y="14" width="7" height="7" rx="2"/><rect x="14" y="14" width="7" height="7" rx="2"/>',
  novo:'<path d="M12 3l2.4 5.6L20 9l-4.3 3.9L17 19l-5-3-5 3 1.3-6.1L4 9l5.6-.4z"/>',
  anda:'<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
  bandeira:'<path d="M5 21V4"/><path d="M5 4h11l-2 4 2 4H5"/>',
  capelo:'<path d="M2 9l10-5 10 5-10 5z"/><path d="M6 11v5c3 2 9 2 12 0v-5"/>',
  info:'<circle cx="12" cy="12" r="9"/><path d="M12 11v5M12 8h.01"/>',
};
const ic = n => '<svg class="ic" viewBox="0 0 24 24" aria-hidden="true">' + IC[n] + '</svg>';
const bola = (n, c, clara) => '<span class="bola' + (clara ? ' clara' : '') + '"' + (c ? ' style="--c:' + c + '"' : '') + '>' + ic(n) + '</span>';
let prog = {};
try { prog = JSON.parse(localStorage.getItem('casos-clinicos:progresso') || '{}'); } catch (_) {}

const prontos = D.casos.filter(c => c.pronto), futuros = D.casos.filter(c => !c.pronto);
const cor = c => c.corv || c.cor;
const estado = c => { const p = prog[c.slug]; if (!p) return 'novo'; if (p.fim) return 'fim'; return p.pos > 1 ? 'anda' : 'novo'; };
const pct = c => { const p = prog[c.slug]; if (!p) return 0; if (p.fim) return 100; return p.total ? Math.min(99, Math.round(100 * p.pos / p.total)) : 0; };
const soma = k => prontos.reduce((s, c) => s + (c[k] || 0), 0);

document.getElementById('topo').innerHTML =
  '<nav class="barra"><span class="identidade">' + bola('grade') + 'Casos clínicos</span>'
  + '<span class="edicao">' + bola('capelo') + 'Internato e residência</span></nav>'
  + '<div class="intro"><div class="entra" style="--i:0"><p class="sobretitulo">' + bola('novo') + 'Investigação, discussão e decisão</p>'
  + '<h1>Biblioteca de <em>casos</em></h1>'
  + '<p class="descricao">Escolha uma história. Cada caso avança por dados novos do paciente e pela pergunta que eles abrem. Suas condutas mudam o rumo e o desfecho.</p></div>'
  + '<div class="numeros">'
  + [['livro', '#4f46e5', prontos.length, 'casos para conduzir'],
     ['pergunta', '#ea580c', soma('perg'), 'perguntas comentadas'],
     ['decisao', '#c026d3', soma('dec'), 'decisões de conduta'],
     ['foto', '#7c3aed', soma('imgs'), 'imagens para discutir']].map((x, n) =>
      '<div class="num entra" style="--c:' + x[1] + ';--i:' + (n + 1) + '">' + bola(x[0], x[1], true)
      + '<div><b data-conta="' + x[2] + '">0</b><span>' + x[3] + '</span></div></div>').join('')
  + '</div></div>'
  + '<div id="seguir"></div>'
  + '<div class="ferramentas"><div class="filtros" role="tablist"></div>'
  + '<label class="busca">' + ic('busca') + '<input id="busca" type="search" placeholder="Buscar caso" aria-label="Buscar casos" autocomplete="off"></label></div>';

const FILTROS = [['todos', 'Todos', 'todos', '#4f46e5'], ['novo', 'Não iniciados', 'novo', '#0891b2'],
                 ['anda', 'Em andamento', 'anda', '#ea580c'], ['fim', 'Concluídos', 'bandeira', '#16a34a']];
let filtro = 'todos';
function pintarFiltros(){
  document.querySelector('.filtros').innerHTML = FILTROS.map(([k, r, n, c]) => {
    const q = k === 'todos' ? prontos.length : prontos.filter(x => estado(x) === k).length;
    return '<button class="filtro' + (filtro === k ? ' on' : '') + '" style="--c:' + c + '" data-f="' + k + '">' + bola(n, c) + r + '<em>' + q + '</em></button>';
  }).join('');
  document.querySelectorAll('.filtro').forEach(b => b.onclick = () => { filtro = b.dataset.f; pintarFiltros(); render(); });
}

const card = (c, n, futuro) => {
  const e = estado(c), p = pct(c);
  const selo = futuro ? '<span class="estado">' + bola('relogio', '#64748b') + 'Em preparo</span>'
    : e === 'fim' ? '<span class="estado">' + bola('check', '#16a34a') + 'Concluído</span>'
    : e === 'anda' ? '<span class="estado">' + bola('anda', '#ea580c') + p + '%</span>' : '';
  const botao = futuro ? 'Em breve' : e === 'fim' ? 'Refazer' : e === 'anda' ? 'Continuar' : 'Começar';
  return '<a class="cs' + (futuro ? ' futuro' : '') + '" ' + (futuro ? '' : 'href="' + c.arq + '"') + ' style="--c:' + cor(c) + ';--i:' + n + '">'
    + '<div class="capa">' + (c.capa ? '<i class="foto" style="background-image:url(' + c.capa + ')"></i>'
        : '<div class="mosaico">' + [['pergunta','#ea580c'],['decisao','#c026d3'],['foto','#7c3aed'],['relogio','#0891b2'],['bandeira','#16a34a'],['livro','#4f46e5']]
            .map(([n, k2]) => bola(n, k2)).join('') + '</div>')
    + '<span class="numero"><span class="bola">' + String(n + 1).padStart(2, '0') + '</span>Caso</span>' + selo + '</div>'
    + '<div class="corpo"><div class="fichas">'
    + '<span>' + bola('relogio', cor(c)) + '≈ ' + c.min + ' min</span>'
    + (c.perg ? '<span>' + bola('pergunta', '#ea580c') + c.perg + ' perguntas</span>' : '')
    + (c.dec ? '<span>' + bola('decisao', '#c026d3') + c.dec + ' decisões</span>' : '')
    + (c.imgs ? '<span>' + bola('foto', '#7c3aed') + c.imgs + '</span>' : '') + '</div>'
    + '<h2>' + c.tt + '</h2><p class="sub">' + c.sub + '</p>'
    + (!futuro && e !== 'novo' ? '<div class="prog"><div class="trilha"><i data-w="' + p + '"></i></div><small><span>' + (e === 'fim' ? 'Percurso concluído' : 'Em andamento') + '</span><span>'
        + (prog[c.slug] && prog[c.slug].feitas ? prog[c.slug].certas + ' de ' + prog[c.slug].feitas + ' certas' : p + '%') + '</span></small></div>' : '')
    + '<div class="rodape-c"><span class="nivel">' + ic('capelo') + (c.niv === 'os dois' ? 'Interno e residente' : c.niv === 'residente' ? 'Residente' : 'Interno') + '</span>'
    + '<span class="abrir">' + botao + ic(futuro ? 'relogio' : e === 'fim' ? 'refazer' : 'seta') + '</span></div></div></a>';
};

function render(){
  const termo = document.getElementById('busca').value.normalize('NFD').replace(/[̀-ͯ]/g, '').toLowerCase();
  const lista = prontos.map((c, n) => ({c, n})).filter(({c}) =>
    (filtro === 'todos' || estado(c) === filtro)
    && (c.tt + ' ' + c.sub).normalize('NFD').replace(/[̀-ͯ]/g, '').toLowerCase().includes(termo));
  const extra = filtro === 'todos' && !termo ? futuros.map((c, k) => card(c, prontos.length + k, true)).join('') : '';
  document.getElementById('grade').innerHTML = (lista.length || extra)
    ? lista.map(({c, n}) => card(c, n)).join('') + extra
    : '<p class="vazio">Nenhum caso aqui ainda.</p>';
  requestAnimationFrame(() => document.querySelectorAll('[data-w]').forEach(el => el.style.width = el.dataset.w + '%'));
}

function continuar(){
  const em = prontos.filter(c => estado(c) === 'anda').sort((a, b) => (prog[b.slug].quando || 0) - (prog[a.slug].quando || 0))[0];
  if (!em) return;
  const p = pct(em);
  document.getElementById('seguir').innerHTML = '<a class="faixa entra" href="' + em.arq + '" style="--c:' + cor(em) + ';--i:3">'
    + '<i class="mini" style="background-image:url(' + em.capa + ')"></i><div class="txt"><small>Continue de onde parou</small><b>' + em.tt + '</b>'
    + '<div class="barra-p"><i style="--p:0%" data-p="' + p + '"></i></div></div>' + bola('play', cor(em)) + '</a>';
  requestAnimationFrame(() => document.querySelectorAll('[data-p]').forEach(el => el.style.setProperty('--p', el.dataset.p + '%')));
}

function contar(){
  document.querySelectorAll('[data-conta]').forEach(el => {
    const alvo = +el.dataset.conta, t0 = performance.now();
    const passo = t => { const f = Math.min(1, (t - t0) / 900); el.textContent = Math.round(alvo * (1 - Math.pow(1 - f, 3))); if (f < 1) requestAnimationFrame(passo); };
    requestAnimationFrame(passo);
  });
}

document.getElementById('busca').addEventListener('input', render);
pintarFiltros(); continuar(); render(); contar();
document.getElementById('rodape').innerHTML = '<div class="nota">' + bola('info', '#475569', true) + '<p>' + D.rodape + '</p></div>';
addEventListener('pageshow', e => { if (e.persisted) location.reload(); });

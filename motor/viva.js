/* ═══════════ camada viva — ícones, cor por página, placar e movimento ═══════════
   Vem depois de etapas.js e embrulha `pintar` e `mostrarRevisao`: o motor
   continua o mesmo, e esta camada só decora o que ele desenhou. */

const VV_IC = {
  historia:'<rect x="6" y="4" width="12" height="17" rx="2"/><path d="M9 4V3h6v1M9 10h6M9 14h6M9 18h3"/>',
  exame:'<path d="M5 3v6a4 4 0 0 0 8 0V3"/><path d="M9 13v3a4 4 0 0 0 8 0v-2"/><circle cx="17" cy="12" r="2"/>',
  exames:'<path d="M9 3h6M10 3v6l-5 9a2 2 0 0 0 1.7 3h10.6a2 2 0 0 0 1.7-3l-5-9V3"/><path d="M7.5 15h9"/>',
  imagem:'<rect x="3" y="5" width="18" height="14" rx="3"/><circle cx="9" cy="10" r="1.6"/><path d="M21 16l-5-5-9 8"/>',
  pergunta:'<circle cx="12" cy="12" r="9"/><path d="M9.6 9.3a2.5 2.5 0 1 1 3.6 2.3c-.8.4-1.2 1-1.2 1.8v.4"/><path d="M12 17h.01"/>',
  pareamento:'<path d="M10 14a4 4 0 0 0 5.7 0l3-3a4 4 0 0 0-5.7-5.7l-1 1"/><path d="M14 10a4 4 0 0 0-5.7 0l-3 3a4 4 0 0 0 5.7 5.7l1-1"/>',
  decisao:'<circle cx="6" cy="5" r="2"/><circle cx="18" cy="5" r="2"/><circle cx="12" cy="19" r="2"/><path d="M6 7v1a5 5 0 0 0 5 5h2a5 5 0 0 0 5-5V7M12 13v4"/>',
  evolucao:'<rect x="4" y="5" width="16" height="16" rx="3"/><path d="M8 3v4M16 3v4M4 10h16M9 14h2v2H9z"/>',
  discussao:'<path d="M9 18h6M10 21h4"/><path d="M12 3a6 6 0 0 0-3.6 10.8c.6.5 1 1.2 1 2.2h5.2c0-1 .4-1.7 1-2.2A6 6 0 0 0 12 3z"/>',
  desfecho:'<path d="M5 21V4"/><path d="M5 4h11l-2 4 2 4H5"/>',
  fecho:'<path d="M4 5a2 2 0 0 1 2-2h13v16H6a2 2 0 0 0-2 2z"/><path d="M4 21a2 2 0 0 1 2-2h13"/>',
  capa:'<path d="M12 3l2.4 5.6L20 9l-4.3 3.9L17 19l-5-3-5 3 1.3-6.1L4 9l5.6-.4z"/>',
  check:'<path d="M5 12.5l4.5 4.5L19 7.5"/>', x:'<path d="M7 7l10 10M17 7L7 17"/>',
  meio:'<path d="M6 12h12"/>', relogio:'<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
  foto:'<rect x="3" y="5" width="18" height="14" rx="3"/><circle cx="9" cy="10" r="1.6"/><path d="M21 16l-5-5-9 8"/>',
  termo:'<path d="M10 14V5a2 2 0 1 1 4 0v9a4 4 0 1 1-4 0z"/><path d="M12 9v6"/>',
  pressao:'<circle cx="12" cy="13" r="8"/><path d="M12 13l4-4M8 5.5A8 8 0 0 1 16 5.5"/>',
  coracao:'<path d="M12 20s-7-4.4-7-10a4 4 0 0 1 7-2.6A4 4 0 0 1 19 10c0 5.6-7 10-7 10z"/>',
  vento:'<path d="M3 8h10a3 3 0 1 0-3-3M3 12h15a3 3 0 1 1-3 3M3 16h7"/>',
  gota:'<path d="M12 3s6 6.5 6 11a6 6 0 0 1-12 0c0-4.5 6-11 6-11z"/>',
  balanca:'<rect x="4" y="4" width="16" height="16" rx="4"/><path d="M9 10a3 3 0 0 1 6 0M12 10l1.5-2"/>',
  regua:'<path d="M4 16L16 4l4 4L8 20z"/><path d="M8 12l2 2M11 9l2 2M14 6l2 2"/>',
  pessoa:'<circle cx="12" cy="8" r="4"/><path d="M4 21a8 8 0 0 1 16 0"/>',
  pulso:'<path d="M3 12h4l3 7 4-14 3 7h4"/>',
  camadas:'<path d="M12 3l9 5-9 5-9-5z"/><path d="M3 13l9 5 9-5"/>',
  raio:'<path d="M13 3L5 14h6l-1 7 8-11h-6z"/>',
  olho:'<path d="M2 12s3.5-7 10-7 10 7 10 7-3.5 7-10 7S2 12 2 12z"/><circle cx="12" cy="12" r="3"/>',
};
const vvIc = (n, cls) => '<svg class="vv-ic' + (cls ? ' ' + cls : '') + '" viewBox="0 0 24 24" aria-hidden="true">' + (VV_IC[n] || VV_IC.pergunta) + '</svg>';
const vvBola = n => '<span class="vv-bola">' + vvIc(n) + '</span>';

function vvTipo(e){
  if (e.t === 'capa') return 'capa';
  if (e.t === 'pergunta' || e.t === 'pedido') return e.t === 'pedido' ? 'exames' : 'pergunta';
  if (e.t === 'pareamento') return 'pareamento';
  if (e.t === 'bifurcacao') return 'decisao';
  if (e.t === 'resultados') return 'exames';
  if (e.t === 'desfecho') return 'desfecho';
  if (e.t === 'balanco') return 'fecho';
  const s = ((e.kicker || '') + ' ' + (e.tt || '')).toLowerCase();
  if (/exame físico|pele, membros|pele e membros/.test(s)) return 'exame';
  if (/imagem|radiograf|tomograf|ultrass|biópsia|eletrocard|\becg\b|lâmina|corpúsculo|microfoto|visual|histolog|arquitetura/.test(s)) return 'imagem';
  if (/retrospectiva|lacuna|procedência|fontes|referênc|onde o caso|créditos|fecho|onde dava/.test(s)) return 'fecho';
  if (/discuss|interpreta|diferencial|mecanismo|fenótipo|laudo|resultado|laborat/.test(s)) return 'discussao';
  if (/dia|semana|evolu|reavalia|pronto|admiss|internação|depois|terapia|alta|seguimento|prescri|conduta|tratamento|retorno|plano|visita|horas/.test(s)) return 'evolucao';
  return 'historia';
}

/* ─────────── placar e progresso ─────────── */
function vvPlacar(){
  const feitas = Object.entries(respostas).filter(([, r]) => r.feita);
  let certas = 0;
  feitas.forEach(([k, r]) => {
    const e = ETAPAS[porId(k)]; if (!e) return;
    if (e.t === 'pareamento'){ if (e.itens.every((it, n) => r.marcadas[n] === it.ok)) certas++; }
    else if (e.alts && r.marcadas.length === e.escolhas && r.marcadas.every(x => e.alts[x].ok)) certas++;
  });
  return {certas, feitas: feitas.length};
}
const VV_CHAVE = 'casos-clinicos:progresso';
function vvGuardar(extra){
  try {
    const todo = JSON.parse(localStorage.getItem(VV_CHAVE) || '{}');
    const slug = CASO.slug || document.title;
    const seq = rotaAtual(); const aqui = Math.max(seq.indexOf(i), 0);
    const velho = todo[slug] || {};
    const pl = vvPlacar();
    todo[slug] = Object.assign({}, velho, {
      pos: Math.max(velho.fim ? 0 : (velho.pos || 0), aqui + 1), total: seq.length,
      certas: pl.certas, feitas: pl.feitas, quando: Date.now()
    }, extra || {});
    localStorage.setItem(VV_CHAVE, JSON.stringify(todo));
  } catch (_) {}
}

let vvUltimo = '', vvPlacarAntes = -1;
function vvAntes(){
  if (emRevisao) return;
  const e = etapa();
  const tipo = vvTipo(e);
  document.body.dataset.tipo = tipo;
  // selo com ícone
  document.querySelectorAll('#palco .marca').forEach(m => {
    if (!m.querySelector('.vv-bola')) m.insertAdjacentHTML('afterbegin', vvBola(tipo));
  });
  const dk = document.querySelector('#palco h2.do-kicker');
  if (dk && !dk.querySelector('.vv-bola')) dk.insertAdjacentHTML('afterbegin', vvBola(tipo));
  if (e.t === 'desfecho'){
    const h = document.querySelector('#palco .fim h1');
    if (h && !h.querySelector('.vv-bola')) h.insertAdjacentHTML('afterbegin', vvBola(e.q === 'melhor' ? 'check' : e.q === 'pior' ? 'x' : 'desfecho'));
  }
  // vitais e aparelhos
  document.querySelectorAll('#palco .vit>div').forEach(d => {
    if (d.querySelector('.vv-ic')) return;
    const r = (d.querySelector('span') || {}).textContent || '';
    const n = /temp/i.test(r) ? 'termo' : /press|^pa$/i.test(r) ? 'pressao' : /card|^fc$/i.test(r) ? 'coracao'
      : /resp|^fr$/i.test(r) ? 'vento' : /spo|satura/i.test(r) ? 'gota' : /peso/i.test(r) ? 'balanca'
      : /altura/i.test(r) ? 'regua' : 'pulso';
    d.insertAdjacentHTML('beforeend', vvIc(n));
  });
  document.querySelectorAll('#palco .tops>div>b').forEach(b => {
    if (b.querySelector('.vv-ic')) return;
    const r = b.textContent;
    const n = /geral/i.test(r) ? 'pessoa' : /cabeça|pescoço/i.test(r) ? 'pessoa' : /cardio/i.test(r) ? 'coracao'
      : /respir|pulm/i.test(r) ? 'vento' : /pele/i.test(r) ? 'camadas' : /neuro/i.test(r) ? 'raio'
      : /olho|ocular/i.test(r) ? 'olho' : 'pulso';
    b.insertAdjacentHTML('afterbegin', vvIc(n));
  });
  // resultado da pergunta
  const r = respostas[e.k];
  if ((e.t === 'pergunta' || e.t === 'pareamento') && r && r.feita){
    let ok, tot;
    if (e.t === 'pareamento'){ tot = e.itens.length; ok = e.itens.filter((it, n) => r.marcadas[n] === it.ok).length; }
    else { tot = e.escolhas; ok = r.marcadas.filter(x => e.alts[x].ok).length; }
    const cls = ok === tot ? 'bom' : ok ? 'parcial' : 'ruim';
    const txt = ok === tot ? (tot === 1 ? 'Resposta certa' : 'Acertou todas') : ok ? 'Acertou ' + ok + ' de ' + tot : (tot === 1 ? 'Resposta incorreta' : 'Nenhuma certa');
    const dica = document.querySelector('#palco .qdica');
    // a frase de efeito do autor sai: o resultado fala por si
    if (dica && !dica.querySelector('.vv-nota')) dica.textContent = '';
    if (dica && !dica.querySelector('.vv-nota'))
      dica.insertAdjacentHTML('afterbegin', '<span class="vv-nota ' + cls + '">' + vvIc(ok === tot ? 'check' : ok ? 'meio' : 'x') + txt + '</span>');
    document.querySelectorAll('#palco .alts li, #palco .pi').forEach((li, n) => li.style.setProperty('--i', n));
  }
  // capa sem ilustração: um mosaico com os ícones do que o caso tem
  if (e.t === 'capa' && !e.fundo && !document.querySelector('#palco .vv-mosaico')){
    const tipos = [['historia','#4f46e5'],['exame','#0d9488'],['exames','#2563eb'],['imagem','#7c3aed'],
                   ['pergunta','#ea580c'],['pareamento','#db2777'],['decisao','#c026d3'],['evolucao','#0891b2'],['desfecho','#16a34a']];
    const tela = document.querySelector('#palco .tela');
    if (tela) tela.insertAdjacentHTML('beforeend', '<div class="vv-mosaico">' + tipos.map(([n, c], k) =>
      '<span style="--c:' + c + ';--i:' + k + '">' + vvIc(n) + '</span>').join('') + '</div>');
  }
  // capa: o que o caso tem
  if (e.t === 'capa'){
    const ab = document.querySelector('#palco .abertura');
    const ks = ab && ab.querySelector('.marca span:not(.vv-bola)'); if (ks) ks.textContent = 'Caso interativo';
    if (ab && !ab.querySelector('.vv-chips')){
      const seq = rotaAtual().map(n => ETAPAS[n]);
      const perg = seq.filter(x => x.t === 'pergunta' || x.t === 'pareamento').length;
      const dec = seq.filter(x => x.t === 'bifurcacao').length;
      const fins = ETAPAS.filter(x => x.t === 'desfecho').length;
      const imgs = Math.max(0, Object.keys(DADOS.imgs || {}).length - 1);
      ab.insertAdjacentHTML('beforeend', '<div class="vv-chips">'
        + '<span style="--c:#ea580c">' + vvIc('pergunta') + perg + ' perguntas</span>'
        + '<span style="--c:#c026d3">' + vvIc('decisao') + dec + ' decisões</span>'
        + '<span style="--c:#16a34a">' + vvIc('desfecho') + fins + ' desfechos</span>'
        + (imgs ? '<span style="--c:#7c3aed">' + vvIc('foto') + imgs + ' imagens</span>' : '') + '</div>');
    }
  }
}

function vvDecorar(){
  const e = etapa();
  const tipo = vvTipo(e);
  document.body.dataset.tipo = tipo;
  if (CASO.cor) document.documentElement.style.setProperty('--caso', CASO.cor);
  // contador com ícone e placar
  const cnt = document.querySelector('#trilho .cnt');
  if (cnt && !cnt.querySelector('.vv-ic')) cnt.insertAdjacentHTML('afterbegin', vvIc(tipo));
  const pl = vvPlacar();
  if (cnt && pl.feitas){
    cnt.insertAdjacentHTML('afterend', '<span class="vv-placar' + (vvPlacarAntes >= 0 && pl.certas > vvPlacarAntes ? ' sobe' : '')
      + '" title="Perguntas com a resposta inteiramente certa">' + vvIc('check') + pl.certas + ' de ' + pl.feitas + '</span>');
  }
  vvPlacarAntes = pl.certas;
  // entrada escalonada, só quando a folha muda
  const chave = e.k + '::' + parteTela;
  if (chave !== vvUltimo){
    let n = 0;
    document.querySelectorAll('#palco .abertura>*, #palco .plano>*:not(.conteudo-paginado), #palco .conteudo-paginado>*, #palco .folha>.marca, #palco .folha>h2, #palco .folha>.sub, #palco .folha>.enun, #palco .alts:not(.feita) li, #palco .cams:not(.feita) .cam, #palco .par:not(.feita) .pi, #palco .laboratorio, #palco .imagens-resultados>*, #palco .vit>div, #palco .tops>div, #palco .fim .caixa>*').forEach(el => {
      if (el.hasAttribute('data-fora') || el.classList.contains('area-paginada')) return;
      el.style.setProperty('--i', Math.min(n++, 14)); el.classList.add('vv-entra');
    });
  }
  vvUltimo = chave;
  vvGuardar();
}

const vvMontarOriginal = montarFolhas;
montarFolhas = function(){ try { vvAntes(); } catch (err) { console.warn(err); } return vvMontarOriginal.apply(this, arguments); };
const vvPintarOriginal = pintar;
pintar = function(){ vvPintarOriginal.apply(this, arguments); try { vvDecorar(); } catch (err) { console.warn(err); } };

/* ─────────── revisão final: anel, números e confete ─────────── */
function vvConfete(){
  const cx = document.createElement('div'); cx.className = 'vv-confete';
  const cores = ['#4f46e5', '#ea580c', '#16a34a', '#db2777', '#0891b2', '#ca8a04', '#7c3aed'];
  for (let k = 0; k < 90; k++){
    const i2 = document.createElement('i');
    i2.style.left = (Math.random() * 100) + 'vw';
    i2.style.background = cores[k % cores.length];
    i2.style.setProperty('--dx', (Math.random() * 30 - 15) + 'vw');
    i2.style.setProperty('--rot', (Math.random() * 720 - 360) + 'deg');
    i2.style.animationDelay = (Math.random() * .5) + 's';
    cx.appendChild(i2);
  }
  document.body.appendChild(cx); setTimeout(() => cx.remove(), 2800);
}
mostrarRevisao = function(){
  const pediu = new Set();
  Object.values(marcados).forEach(s => s.forEach(n => pediu.add(n)));
  const faltou = REVISAO.filter(r => !pediu.has(r.chave));
  const pl = vvPlacar();
  const pct = pl.feitas ? Math.round(100 * pl.certas / pl.feitas) : 0;
  const dec = Object.keys(escolhas).length;
  const R = 54, C = 2 * Math.PI * R;
  document.body.dataset.tipo = 'desfecho';
  $('#palco').innerHTML = '<section class="tela on"><div class="folha">'
    + '<div class="marca">' + vvBola('desfecho') + '<span>Revisão</span></div>'
    + '<h2>' + (pct >= 70 ? 'Caso concluído com boa condução' : 'Caso concluído') + '</h2>'
    + '<div class="vv-fim"><div class="vv-anel"><svg viewBox="0 0 132 132"><circle class="fundo-anel" cx="66" cy="66" r="' + R + '"/>'
    + '<circle class="cheio" cx="66" cy="66" r="' + R + '" stroke-dasharray="' + C + '" stroke-dashoffset="' + C + '"/></svg><b data-conta="' + pct + '">0%</b></div>'
    + '<div class="vv-cards"><div style="--c:#16a34a"><b data-conta="' + pl.certas + '">0</b><span>perguntas inteiramente certas</span></div>'
    + '<div style="--c:#ea580c"><b data-conta="' + pl.feitas + '">0</b><span>perguntas respondidas</span></div>'
    + '<div style="--c:#c026d3"><b data-conta="' + dec + '">0</b><span>decisões de conduta</span></div></div></div>'
    + (faltou.length ? '<div class="rev">' + faltou.map(r => '<div class="li"><b>' + r.rotulo + '</b><p>' + r.porque + '</p></div>').join('') + '</div>' : '')
    + '</div></section>';
  $('#pe').innerHTML = '<span class="rod">' + CASO.rodape + '</span>'
    + '<span class="nav"><a class="bt" href="index.html">Biblioteca</a><button class="bt forte" id="reiniciar" onclick="recomecar()">Conduzir de novo</button></span>';
  $('#trilho').innerHTML = '<a class="voltar-biblioteca" href="index.html" aria-label="Voltar à biblioteca"><svg viewBox="0 0 24 24"><rect x="3" y="3" width="7" height="7" rx="2"/><rect x="14" y="3" width="7" height="7" rx="2"/><rect x="3" y="14" width="7" height="7" rx="2"/><rect x="14" y="14" width="7" height="7" rx="2"/></svg><span>Biblioteca</span></a><span class="tt">' + CASO.titulo + '</span>';
  emRevisao = true; parteTela = 0; montarFolhas(); 
  document.querySelectorAll('#palco .vv-fim, #palco .rev .li').forEach((el, n) => { el.style.setProperty('--i', n); el.classList.add('vv-entra'); });
  requestAnimationFrame(() => {
    const cheio = document.querySelector('.vv-anel .cheio');
    if (cheio) cheio.style.strokeDashoffset = C * (1 - pct / 100);
    document.querySelectorAll('[data-conta]').forEach(el => {
      const alvo = +el.dataset.conta, pc = el.closest('.vv-anel'), t0 = performance.now();
      const passo = t => { const f = Math.min(1, (t - t0) / 900); el.textContent = Math.round(alvo * (1 - Math.pow(1 - f, 3))) + (pc ? '%' : ''); if (f < 1) requestAnimationFrame(passo); };
      requestAnimationFrame(passo);
    });
  });
  vvGuardar({fim: true});
  if (pl.feitas && pct >= 70 && !matchMedia('(prefers-reduced-motion: reduce)').matches) setTimeout(vvConfete, 450);
};

pintar();

/* Motor da apresentação. Sem dependência externa: roda em file://.
   Organizado em blocos: palco, revelação, navegação, gaveta, edição, entrada. */

const S = [...document.querySelectorAll('.slide')];
let i = 0;
const bar = document.getElementById('bar'),
      grid = document.getElementById('grid'),
      gav = document.getElementById('gav'),
      edt = document.getElementById('edt'),
      etp = document.getElementById('etapas');
let editando = false, sujo = false;

/* ───────────────────────── palco ───────────────────────── */
const stage = document.getElementById('stage');
function fit(){
  const k = Math.min(innerWidth / 1280, innerHeight / 720) * 0.985;
  stage.style.transform = 'scale(' + k + ')';
}
addEventListener('resize', fit);
addEventListener('fullscreenchange', fit);
fit();

/* ───────────────────── etapas de revelação ───────────────────── */
function cur(){ return document.querySelector('.slide.on') || S[i]; }
function passos(s){ return [...(s || cur()).querySelectorAll('.rv,.pv,svg.ov.rvov,table.oc')]; }
function feito(el){
  if (el.tagName === 'TABLE')
    return ![...el.querySelectorAll('tbody tr')].some(r => r.classList.contains('hid'));
  return el.classList.contains('on');
}
function abrir(el){
  if (el.tagName === 'TABLE'){
    el.querySelectorAll('tbody tr.hid').forEach(r => r.classList.remove('hid'));
    return;
  }
  el.classList.add('on');
  if (el.tagName === 'svg'){ const f = el.closest('figure'); if (f) f.classList.add('on'); }
  espelhar(el, true);
}
function fechar(el){
  if (el.tagName === 'TABLE'){
    el.querySelectorAll('tbody tr').forEach(r => r.classList.add('hid'));
    return;
  }
  el.classList.remove('on');
  if (el.tagName === 'svg'){ const f = el.closest('figure'); if (f) f.classList.remove('on'); }
  espelhar(el, false);
}
/* Território no desenho e linha na legenda acendem juntos, seja qual for o
   lado por onde a revelação passou. */
function espelhar(el, v){
  const k = el.dataset && el.dataset.terr;
  if (!k) return;
  const m = el.closest('.mapa');
  if (m) m.querySelectorAll('[data-terr="' + k + '"]').forEach(x => x.classList.toggle('on', v));
}
function pintar(){
  const k = S.indexOf(cur()); if (k >= 0) i = k;
  const p = passos();
  if (!p.length){ etp.classList.remove('on'); etp.innerHTML = ''; return; }
  etp.classList.add('on');
  etp.innerHTML = p.map(e => '<i class="' + (feito(e) ? 'f' : '') + '"></i>').join('');
}
function avancar(){
  const n = passos().find(e => !feito(e));
  if (n){ abrir(n); pintar(); return true; }
  return false;
}
function recuar(){
  const p = passos().filter(feito);
  if (p.length){ fechar(p[p.length - 1]); pintar(); return true; }
  return false;
}
function tudo(v){ passos().forEach(e => v ? abrir(e) : fechar(e)); pintar(); }

/* ───────────────────────── navegação ───────────────────────── */
function show(n, fim){
  i = Math.max(0, Math.min(S.length - 1, n));
  S.forEach((s, k) => s.classList.toggle('on', k === i));
  if (!fim) passos(S[i]).forEach(fechar); else tudo(true);
  pintar();
  bar.style.width = ((i + 1) / S.length * 100) + '%';
  location.hash = i + 1;
  if (editando) ligarEdicao();
}

/* ───────────────────────── edição ───────────────────────── */
const ALVOS = 'h1,h2,h3,p,li,td,th,.sub,.meta,.lede,.cap,.rv-lb,figcaption,.tt,.wy,.bt,.step,.qn,.gsub';
function ligarEdicao(){
  cur().querySelectorAll(ALVOS).forEach(el => {
    if (el.closest('.foot')) return;
    el.setAttribute('contenteditable', 'true');
    if (!el.dataset.ed){ el.dataset.ed = '1'; el.addEventListener('input', () => { sujo = true; }); }
  });
}
function desligarEdicao(){
  document.querySelectorAll('[contenteditable]').forEach(el => el.removeAttribute('contenteditable'));
}
function modoEdicao(v){
  editando = v;
  document.body.classList.toggle('editando', v);
  edt.classList.toggle('on', v);
  if (v) ligarEdicao(); else desligarEdicao();
}

/* O salvar não enumera o que precisa esquecer: tudo que é escrito em tempo de
   execução carrega data-runtime, e some por esse atributo. Feature nova não
   exige lembrar de acrescentar uma linha aqui. */
function limpar(c){
  c.querySelectorAll('[data-runtime]').forEach(e => {
    const modo = e.getAttribute('data-runtime');
    if (modo === 'attr'){ e.removeAttribute('style'); }
    else { e.innerHTML = ''; e.removeAttribute('style'); }
  });
  c.querySelectorAll('[contenteditable]').forEach(e => e.removeAttribute('contenteditable'));
  c.querySelectorAll('[data-ed]').forEach(e => e.removeAttribute('data-ed'));
  c.querySelectorAll('.on').forEach(e => e.classList.remove('on'));
  c.querySelectorAll('.slide .sel').forEach(e => e.classList.remove('sel'));
  c.querySelectorAll('table.oc tbody tr').forEach(e => e.classList.add('hid'));
  c.querySelectorAll('.qhint .cnt').forEach(e => {
    e.classList.remove('cheio');
    e.textContent = '0 de ' + e.dataset.max + ' marcada' + (e.dataset.max === '1' ? '' : 's');
  });
  c.querySelectorAll('body').forEach(e => e.classList.remove('editando'));
  const q = c.querySelector('#q'); if (q) q.setAttribute('value', '');
  const bc = c.querySelector('#banco'); if (bc) bc.textContent = JSON.stringify(BANCO);
}
function salvar(){
  const c = document.documentElement.cloneNode(true);
  limpar(c);
  const html = '<!DOCTYPE html>\n<html lang="pt-BR">' + c.innerHTML + '</html>';
  const a = document.createElement('a');
  a.href = URL.createObjectURL(new Blob([html], { type: 'text/html;charset=utf-8' }));
  const d = new Date(), z = n => String(n).padStart(2, '0');
  a.download = SLUG + '-' + d.getFullYear() + z(d.getMonth() + 1) + z(d.getDate())
             + '-' + z(d.getHours()) + z(d.getMinutes()) + '.html';
  document.body.appendChild(a); a.click(); a.remove();
  sujo = false;
  const t = edt.querySelector('.msg');
  if (t){ t.textContent = 'arquivo baixado'; setTimeout(() => t.textContent = '', 2600); }
}
addEventListener('beforeunload', e => { if (sujo){ e.preventDefault(); e.returnValue = ''; } });

/* ──────────────────────── gaveta de exames ──────────────────────── */
const BANCO = JSON.parse(document.getElementById('banco').textContent);
const SLUG = document.getElementById('banco').dataset.slug || 'caso';
const sa = t => t.normalize('NFD').replace(/[̀-ͯ]/g, '').toLowerCase();
const pedidos = [];
function achar(t){
  const q = sa(t).trim(); if (!q) return [];
  const ts = q.split(/\s+/);
  const p = BANCO.map((e, ordem) => {
    const nn = sa(e.n), ss = (e.s || []).map(sa), alvo = nn + ' ' + ss.join(' ') + ' ' + sa(e.c || '');
    if (!ts.every(w => alvo.includes(w))) return null;
    let sc;
    if (nn === q) sc = 100;
    else if (ss.some(x => x === q)) sc = 90;
    else if (nn.startsWith(q)) sc = 72;
    else if (ss.some(x => x.startsWith(q))) sc = 60;
    else if (nn.includes(q)) sc = 45;
    else if (ss.some(x => x.includes(q))) sc = 32;
    else sc = 14;
    return { e, sc, ordem };
  }).filter(Boolean);
  p.sort((a, b) => b.sc - a.sc || a.ordem - b.ordem);
  if (p.length) return p.slice(0, 14).map(x => x.e);
  /* Nada bateu por substring. Em sala, isso quase sempre é erro de digitação —
     "creatnina" — e responder "não está no banco" é mentira. Segunda passada,
     por distância de edição sobre o nome e os sinônimos. */
  const perto = BANCO.map((e, ordem) => {
    const alvos = [sa(e.n), ...(e.s || []).map(sa)];
    const d = Math.min(...alvos.map(a => dist(q, a)));
    return { e, d, ordem };
  }).filter(x => x.d <= Math.max(1, Math.floor(q.length / 4)));
  perto.sort((a, b) => a.d - b.d || a.ordem - b.ordem);
  return perto.slice(0, 8).map(x => x.e);
}

/* Distância de edição do termo digitado contra qualquer janela do alvo:
   "creatnina" tem que achar "creatinina" mesmo dentro de um nome maior. */
function dist(a, b){
  if (b.includes(a)) return 0;
  let melhor = 99;
  const n = a.length;
  for (let i = 0; i + n - 2 <= b.length; i++){
    for (const j of [n - 1, n, n + 1]){
      const t = b.substr(i, j);
      if (!t) continue;
      melhor = Math.min(melhor, lev(a, t, melhor));
      if (!melhor) return 0;
    }
  }
  return melhor;
}
function lev(a, b, teto){
  const m = a.length, n = b.length;
  if (Math.abs(m - n) > teto) return teto + 1;
  let ant = Array.from({ length: n + 1 }, (_, j) => j);
  for (let i = 1; i <= m; i++){
    const cur = [i];
    let min = i;
    for (let j = 1; j <= n; j++){
      cur[j] = Math.min(ant[j] + 1, cur[j - 1] + 1,
                        ant[j - 1] + (a[i - 1] === b[j - 1] ? 0 : 1));
      if (cur[j] < min) min = cur[j];
    }
    if (min > teto) return teto + 1;
    ant = cur;
  }
  return ant[n];
}
function cartao(e){
  if (!pedidos.includes(e.n)) pedidos.push(e.n);
  const ed = editando ? ' contenteditable="true"' : '', ix = BANCO.indexOf(e);
  return '<div class="card" data-ix="' + ix + '">'
    + '<div class="cn">' + e.n + '</div><div class="cc">' + (e.c || '') + '</div>'
    + '<div class="cr' + (e.a ? ' alt' : '') + '" data-f="r"' + ed + '>' + e.r + '</div>'
    + '<div class="cf"><b>Referência</b> <span data-f="ref"' + ed + '>' + (e.ref || '—') + '</span></div>'
    + '</div>';
}
function historico(){
  if (!pedidos.length) return '';
  return '<div class="hist"><div class="ht">Pedidos nesta sessão</div><ol>'
    + pedidos.map(n => '<li>' + n + '</li>').join('') + '</ol></div>';
}
const q = document.getElementById('q'), gb = document.getElementById('gb');
let sel = 0, sugs = [];
function render(){
  const t = q.value.trim();
  if (!t){
    gb.innerHTML = '<div class="vazio">Digite o nome do exame — <b>creatinina</b>, <b>sódio</b>, '
      + '<b>ferritina</b>, <b>líquor</b>. Nomes de painel (hemograma, função renal, gasometria) '
      + 'listam os analitos que os compõem. Acento e abreviação são opcionais.</div>' + historico();
    sel = 0; return;
  }
  sugs = achar(t);
  if (!sugs.length){
    gb.innerHTML = '<div class="vazio"><b>“' + t.replace(/</g, '&lt;')
      + '” não está no banco deste caso.</b><br>Tente outro nome ou a abreviação.</div>' + historico();
    return;
  }
  /* Acerto exato ÚNICO abre o cartão direto: ao vivo, quem digita o nome
     inteiro quer o resultado. Mas "hemograma" é sinônimo de dez analitos —
     nome de painel casa exato com vários, e aí a resposta certa é a lista. */
  const alvo = sa(t.trim());
  const exatos = sugs.filter(e => sa(e.n) === alvo || (e.s || []).some(x => sa(x) === alvo));
  const exato = exatos.length === 1 && exatos[0] === sugs[0];
  if (sugs.length === 1 || exato){
    /* Ao vivo, quem digita o nome inteiro quer o resultado, não uma lista. */
    const outros = sugs.slice(1, 7).map((e, k) => '<div class="sug" data-k="' + (k + 1)
      + '"><b>' + e.n + '</b><span>' + (e.c || '') + '</span></div>').join('');
    gb.innerHTML = cartao(sugs[0])
      + (outros ? '<div class="ht" style="margin:2px 0 6px">Outros com esse termo</div>'
                  + outros : '')
      + historico();
    gb.querySelectorAll('.sug').forEach(d => d.onclick = () => {
      gb.innerHTML = cartao(sugs[+d.dataset.k]) + historico();
    });
    return;
  }
  gb.innerHTML = sugs.map((e, k) => '<div class="sug' + (k === sel ? ' k' : '') + '" data-k="' + k
    + '"><b>' + e.n + '</b><span>' + (e.c || '') + '</span></div>').join('') + historico();
  gb.querySelectorAll('.sug').forEach(d => d.onclick = () => {
    gb.innerHTML = cartao(sugs[+d.dataset.k]) + historico();
  });
}
gb.addEventListener('input', ev => {
  const c = ev.target.closest('[data-f]'); if (!c) return;
  const card = c.closest('.card'), ix = +card.dataset.ix;
  if (ix >= 0){ BANCO[ix][c.dataset.f] = c.innerHTML; sujo = true; }
});
q.addEventListener('input', () => { sel = 0; render(); });
q.addEventListener('keydown', e => {
  e.stopPropagation();
  if (e.key === 'Escape'){ abrirGaveta(false); return; }
  if (e.key === 'ArrowDown'){ sel = Math.min(sel + 1, sugs.length - 1); render(); e.preventDefault(); }
  else if (e.key === 'ArrowUp'){ sel = Math.max(sel - 1, 0); render(); e.preventDefault(); }
  else if (e.key === 'Enter' && sugs.length){ gb.innerHTML = cartao(sugs[sel]) + historico(); e.preventDefault(); }
});
function abrirGaveta(v){
  gav.classList.toggle('on', v);
  if (v){ q.value = ''; render(); setTimeout(() => q.focus(), 90); } else q.blur();
}
document.getElementById('gavb').onclick = () => abrirGaveta(!gav.classList.contains('on'));

/* ───────────────────── seleção de alternativa ───────────────────── */
function marcar(li){
  const ul = li.parentElement, max = +(ul.dataset.max || 0),
        n = ul.querySelectorAll('li.sel').length;
  if (!li.classList.contains('sel') && max && n >= max){
    const c = ul.previousElementSibling?.querySelector('.cnt');
    if (c){ c.classList.add('cheio'); setTimeout(() => c.classList.remove('cheio'), 650); }
    return;
  }
  li.classList.toggle('sel');
  const c = ul.previousElementSibling?.querySelector('.cnt');
  const m = ul.querySelectorAll('li.sel').length;
  if (c) c.textContent = m + ' de ' + max + ' marcada' + (max === 1 ? '' : 's');
}

/* ───────────────────────── entrada ───────────────────────── */
addEventListener('keydown', e => {
  if (e.target === q) return;
  if ((e.ctrlKey || e.metaKey) && (e.key === 's' || e.key === 'S')){ salvar(); e.preventDefault(); return; }
  if (editando && e.target.isContentEditable){
    if (e.key === 'Escape'){ modoEdicao(false); e.preventDefault(); }
    return;
  }
  if (gav.classList.contains('on')){ if (e.key === 'Escape') abrirGaveta(false); return; }
  if (grid.classList.contains('on')){
    if (['Escape', 'o', 'O'].includes(e.key)) grid.classList.remove('on');
    return;
  }
  if (e.key === 'x' || e.key === 'X'){ abrirGaveta(true); e.preventDefault(); return; }
  if (e.key === 'e' || e.key === 'E'){ modoEdicao(!editando); e.preventDefault(); return; }
  if (e.key === 'a' || e.key === 'A'){ tudo(true); return; }
  if (e.key === 'z' || e.key === 'Z'){ tudo(false); return; }
  if (['ArrowRight', 'PageDown', ' ', 'Enter', 'n'].includes(e.key)){
    if (e.shiftKey || !avancar()) show(i + 1);
    e.preventDefault();
  } else if (['ArrowLeft', 'PageUp', 'Backspace', 'p'].includes(e.key)){
    if (e.shiftKey || !recuar()) show(i - 1, true);
    e.preventDefault();
  }
  else if (e.key === 'Home') show(0);
  else if (e.key === 'End') show(S.length - 1);
  else if (e.key === 'f' || e.key === 'F') document.documentElement.requestFullscreen?.();
  else if (e.key === 'o' || e.key === 'O') grid.classList.add('on');
});

document.addEventListener('click', e => {
  const ph = e.target.closest('.rv-ph');
  if (ph){ abrir(ph.parentElement); pintar(); e.stopPropagation(); return; }
  const tr = e.target.closest('table.oc tbody tr.hid');
  if (tr){ tr.classList.remove('hid'); pintar(); e.stopPropagation(); return; }
  const sv = e.target.closest('figure.an');
  if (sv){
    const o = sv.querySelector('svg.ov.rvov');
    if (o && !o.classList.contains('on')){ abrir(o); pintar(); e.stopPropagation(); return; }
  }
  /* mapa de territórios: desenho e legenda são o mesmo botão */
  const lt = e.target.closest('.lt');
  const tg = e.target.closest('.terr');
  const alvoT = lt || tg;
  if (alvoT){
    const chave = alvoT.dataset.terr, mapa = alvoT.closest('.mapa');
    const ligado = alvoT.classList.contains('on');
    mapa.querySelectorAll('[data-terr="' + chave + '"]')
        .forEach(x => x.classList.toggle('on', !ligado));
    pintar();
    e.stopPropagation();
    return;
  }
  const li = e.target.closest('.alts li');
  if (li){ if (!editando) marcar(li); return; }
  if (e.target.closest('#grid') || e.target.closest('#gav') || e.target.closest('#gavb')
      || e.target.closest('#edt') || editando) return;
  if (e.clientX > innerWidth * 0.55){ if (!avancar()) show(i + 1); }
  else if (e.clientX < innerWidth * 0.2){ if (!recuar()) show(i - 1, true); }
});

document.querySelectorAll('#grid .t').forEach(t => t.onclick = () => {
  grid.classList.remove('on');
  show(+t.dataset.n - 1);
});
edt.querySelector('.sv').onclick = salvar;
edt.querySelector('.fc').onclick = () => modoEdicao(false);

let ht; const hp = document.getElementById('help');
function hh(){ hp.style.opacity = 1; clearTimeout(ht); ht = setTimeout(() => hp.style.opacity = 0, 3500); }
addEventListener('mousemove', hh); addEventListener('keydown', hh); hh();

show(location.hash ? parseInt(location.hash.slice(1)) - 1 || 0 : 0);

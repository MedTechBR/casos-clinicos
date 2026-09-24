"""Percursos completos, resultados fixos e limites visuais dos novos casos."""
from pathlib import Path
from itertools import product
from playwright.sync_api import sync_playwright
ROOT=Path(__file__).resolve().parents[1]
SLUGS=('kikuchi','sarcoidose','cmv')
with sync_playwright() as pw:
 b=pw.chromium.launch();page=b.new_page();errors=[];page.on('pageerror',lambda e:errors.append(str(e)));total=0
 for slug in SLUGS:
  page.goto((ROOT/(slug+'.html')).as_uri())
  # Cliques reais: alternativa, confirmação e escolha de ramo.
  page.evaluate('ir(porId("p1"))')
  assert page.locator('#conf').is_disabled()
  n=page.evaluate('etapa().escolhas')
  for j in range(n):page.locator('.alts li').nth(j).click()
  page.locator('#conf').click();assert page.locator('.alts.feita').count()==1
  page.evaluate('ir(porId("b1"))');page.locator('.cam').first.click()
  dest=page.evaluate('etapa().caminhos[0].vai');page.evaluate('adiante()');assert page.evaluate('etapa().k')==dest
  page.reload()
  steps=page.evaluate('ETAPAS')
  ids=[s['k'] for s in steps];assert len(ids)==len(set(ids))
  for s in steps:
   for dest in ([s.get('segue'),s.get('fecho')]+[c['vai'] for c in s.get('caminhos',[])]):
    if dest:assert dest in ids,(slug,dest)
  branches=[s for s in steps if s['t']=='bifurcacao'];seen=set();ends=set()
  for choices in product(*[range(len(s['caminhos'])) for s in branches]):
   page.reload();mapping=dict(zip([s['k'] for s in branches],choices));path=[]
   for _ in range(100):
    k,t=page.evaluate('[etapa().k,etapa().t]');seen.add(k);path.append(k)
    if k=='referencias':break
    if t=='pergunta':
     # Incorrect selection still leads to the authored complete results.
     page.evaluate('()=>{let e=etapa();respostas[e.k]={feita:true,marcadas:[0]};pintar()}')
    if t=='bifurcacao':page.evaluate('([k,n])=>{escolhas[k]=n;pintar()}',[k,mapping[k]])
    if t=='desfecho':ends.add(k)
    if t=='resultados':assert page.locator('.rc').count()==len(next(s for s in steps if s['k']==k)['todos'])
    page.evaluate('adiante()')
   else:raise AssertionError((slug,'loop',path))
  assert seen==set(ids),(slug,'unreachable',set(ids)-seen)
  assert ends=={s['k'] for s in steps if s['t']=='desfecho'}
  for w,h in ((1366,768),(1600,900),(375,812)):
   page.set_viewport_size({'width':w,'height':h})
   for s in steps:
    page.evaluate('(k)=>ir(porId(k))',s['k'])
    page.evaluate('()=>{detalhesAbertos.clear();pintar()}')
    for revealed in (False,True):
     if revealed:page.evaluate('''()=>{document.querySelectorAll('#palco details').forEach(d=>detalhesAbertos.add(d.dataset.detalhe));let e=etapa();if(e.t==='pergunta')respostas[e.k]={feita:true,marcadas:e.alts.map((a,i)=>a.ok?i:-1).filter(i=>i>=0)};if(e.t==='bifurcacao')escolhas[e.k]=0;parteTela=0;pintar()}''')
     if s['t'] in ('pergunta','resultados','bifurcacao') or page.locator('.observacao-imagem').count():assert page.evaluate('partesTela.length===1'),(slug,w,s['k'],'pagination')
     for n in range(page.evaluate('partesTela.length')):
      page.evaluate('(n)=>{parteTela=n;aplicarParte();pintarPe()}',n)
      assert page.evaluate('!areaTela || (areaTela.scrollHeight<=areaTela.clientHeight+2 && areaTela.scrollWidth<=areaTela.clientWidth+2)'),(slug,w,s['k'],revealed)
      total+=1
  page.set_viewport_size({'width':1366,'height':768});page.evaluate('ir(porId("p2"))');page.screenshot(path='/tmp/'+slug+'-pergunta.png')
  print(slug,'todos os percursos, resultados e tamanhos OK',flush=True)
 page.goto((ROOT/'index.html').as_uri());assert page.locator('a.cs').count()==6
 assert not errors,errors
 b.close();print(total,'estados/páginas validados')

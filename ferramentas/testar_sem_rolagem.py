"""Todos os blocos são alcançáveis por páginas; sem recorte nem rolagem interna."""
from pathlib import Path
from ui_paginas import mostrar
from playwright.sync_api import sync_playwright
ROOT=Path(__file__).resolve().parents[1]
with sync_playwright() as pw:
 b=pw.chromium.launch();page=b.new_page();errors=[];page.on('pageerror',lambda e:errors.append(str(e)));total=0
 for w,h in [(1366,768),(1600,900),(375,812)]:
  page.set_viewport_size({'width':w,'height':h})
  for slug in ['pulmao-rim','west-nile','cocaina-levamisol']:
   page.goto((ROOT/(slug+'.html')).as_uri())
   steps=page.evaluate('ETAPAS.map(e=>({k:e.k,t:e.t}))')
   page.evaluate('ETAPAS.filter(e=>e.t==="pedido").forEach(e=>{const res=ETAPAS.find(x=>x.de===e.k&&x.t==="resultados");let opts=e.grupos.flatMap(g=>g.o).sort((a,b)=>Number(!!res?.laminas[b.e])-Number(!!res?.laminas[a.e]));marcados[e.k]=new Set(opts.slice(0,e.limite).map(o=>o.e))})')
   for e in steps:
    page.evaluate('(k)=>ir(porId(k))',e['k'])
    for state in ['inicial','revelado']:
     if state=='revelado':page.evaluate('''()=>{let e=etapa();if(e.t==='pergunta')respostas[e.k]={feita:true,marcadas:e.alts.map((a,i)=>a.ok?i:-1).filter(i=>i>=0)};if(e.t==='bifurcacao')escolhas[e.k]=0;if(e.t==='resultados')document.querySelectorAll('.verlaudo').forEach(b=>laudos.add(b.dataset.laudo));document.querySelectorAll('details').forEach((d,n)=>detalhesAbertos.add(e.k+'::'+n));parteTela=0;pintar()}''')
     assert page.evaluate('!areaTela || new Set(partesTela.flat()).size===areaTela.children.length'),(slug,e['k'],'conteúdo sem página')
     if e['t']=='pedido':assert page.evaluate('new Set([...document.querySelectorAll(".it")].map(x=>x.dataset.ex)).size===etapa().grupos.reduce((n,g)=>n+g.o.length,0)'),(slug,e['k'],'exames ausentes')
     for n in range(page.evaluate('partesTela.length')):
      page.evaluate('(n)=>{parteTela=n;aplicarParte();pintarPe()}',n)
      bounds=page.evaluate('''()=>{let a=areaTela,r=a?.getBoundingClientRect();return a?[a.scrollHeight-a.clientHeight,a.scrollWidth-a.clientWidth,r.bottom-document.querySelector('#pe').getBoundingClientRect().top]:[0,0,0]}''')
      assert max(bounds)<=2,(w,slug,e['k'],state,n,bounds)
      assert page.evaluate('document.documentElement.scrollWidth<=innerWidth'),(w,slug,e['k'],'largura')
      total+=1
   page.evaluate('mostrarRevisao()')
   for n in range(page.evaluate('partesTela.length')):
    page.evaluate('(n)=>{parteTela=n;aplicarParte();pintarPe()}',n)
    assert page.evaluate('areaTela.scrollHeight<=areaTela.clientHeight+2')
   page.locator('#reiniciar').click();assert page.evaluate('etapa().t')=='capa'
  print(w,h,'todas as páginas e estados OK',flush=True)
 # Interação real: catálogo dividido, seleção preservada, limite e retorno.
 page.set_viewport_size({'width':1366,'height':768});page.goto((ROOT/'pulmao-rim.html').as_uri());page.evaluate('ir(porId("ex_mec"))')
 original=page.evaluate('partesTela.length');assert original>1
 names=[]
 for n in range(original):
  for loc in page.locator('.it:not(.trava)').all():
   if loc.is_visible() and len(names)<6:
    names.append(loc.get_attribute('data-ex'));loc.click()
  if n+1<original:page.locator('#seguir').click()
 assert page.evaluate('marcados.ex_mec.size')==6
 for n in range(original-1):page.locator('#voltar').click()
 assert page.evaluate('parteTela')==0
 assert set(page.evaluate('[...marcados.ex_mec]'))==set(names)
 first=page.locator('.it.on').first
 first.click();assert page.evaluate('marcados.ex_mec.size')==5;first.click()
 # Abertura e fechamento da discussão conservam estado após repaginar.
 page.evaluate('ir(porId("crescente"))');mostrar(page,'details summary').click()
 page.wait_for_function('detalhesAbertos.has("crescente::0")')
 assert page.locator('details').first.get_attribute('open') is not None
 mostrar(page,'details summary').click();page.wait_for_function('!detalhesAbertos.has("crescente::0")')
 assert not errors,errors
 b.close();print(total,'páginas/estados sem overflow; catálogo e discussão interativos OK')

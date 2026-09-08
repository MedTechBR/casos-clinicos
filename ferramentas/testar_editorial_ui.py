"""Verifica biblioteca, imagens, discussão revelável e perguntas em três viewports."""
from pathlib import Path
from ui_paginas import mostrar
from playwright.sync_api import sync_playwright
r=Path(__file__).resolve().parents[1]
with sync_playwright() as pw:
 b=pw.chromium.launch();p=b.new_page();errors=[];p.on('pageerror',lambda e:errors.append(str(e)))
 for w,h in [(1600,900),(1366,768),(375,812)]:
  p.set_viewport_size({'width':w,'height':h});p.goto((r/'index.html').as_uri());assert p.locator('a.cs').count()==3
  p.locator('#busca').fill('flor');assert p.locator('a.cs').count()==1
  p.locator('#busca').fill('xyzxyz');assert p.locator('a.cs').count()==0
  p.locator('#busca').fill('');assert p.evaluate('document.documentElement.scrollWidth<=innerWidth')
  for slug in ['pulmao-rim','cocaina-levamisol','west-nile']:
   p.goto((r/(slug+'.html')).as_uri());steps=p.evaluate('ETAPAS.map(e=>({k:e.k,t:e.t}))');images=0
   for e in steps:
    p.evaluate('(k)=>ir(porId(k))',e['k'])
    assert p.evaluate('Array.from(document.querySelectorAll("#palco img")).every(i=>i.complete&&i.naturalWidth>0)'),(slug,e['k'],'image')
    if e['t']=='pergunta':
     assert p.evaluate('document.querySelector("#conf").getBoundingClientRect().bottom <= document.querySelector("#pe").getBoundingClientRect().top'),(slug,e['k'],'confirm')
     if w>900:assert p.evaluate('document.querySelector(".alts").scrollHeight<=document.querySelector(".alts").clientHeight+2')
     if w==1366 and e['k'] in ['p2','q1']:p.screenshot(path=str(r/'saida/revisao'/f'editorial-{slug}-pergunta.png'))
    if p.locator('details.leitura').count():
     assert not p.locator('details.leitura').first.evaluate('(e)=>e.open')
     mostrar(p,'details.leitura summary').click();p.wait_for_function('document.querySelector("details.leitura").open')
     mostrar(p,'figure.amplia').click();assert p.locator('.lupa').count()==1
     p.keyboard.press('Escape');assert p.locator('.lupa').count()==0;images+=1
   assert images>=2,(slug,images)
   p.locator('.voltar-biblioteca').click();p.wait_for_url('**/index.html');p.locator('a.cs').first.wait_for();assert p.locator('a.cs').count()==3
  print('UI OK',w,h,flush=True)
 assert not errors,errors;b.close()

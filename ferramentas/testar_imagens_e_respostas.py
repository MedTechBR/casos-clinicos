"""Regressão: marcador sem pseudo-rótulo; exame da equipe antes da leitura anotada."""
from pathlib import Path
from ui_paginas import mostrar, ultima
from playwright.sync_api import sync_playwright
ROOT=Path(__file__).resolve().parents[1]
with sync_playwright() as pw:
 b=pw.chromium.launch();page=b.new_page();errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
 for w,h in [(1600,900),(1366,768),(375,812)]:
  page.set_viewport_size({'width':w,'height':h});questions=0
  for slug,exam in [('pulmao-rim','rx'),('west-nile','tc'),('cocaina-levamisol','us')]:
   page.goto((ROOT/(slug+'.html')).as_uri())
   for q in page.evaluate('ETAPAS.filter(e=>e.t==="pergunta").map(e=>({k:e.k,n:e.escolhas}))'):
    page.evaluate('(k)=>ir(porId(k))',q['k'])
    for n in range(q['n']):mostrar(page,'.alts li',n).click()
    page.locator('#conf').click()
    assert page.locator('.alts.feita').count()==1
    assert page.locator('.estado-resposta').count()==page.locator('.alts li').count()
    assert page.evaluate('Array.from(document.querySelectorAll(".k")).every(e=>["none","normal"].includes(getComputedStyle(e,"::after").content))'),(slug,q['k'],'pseudo-rótulo')
    assert page.evaluate('Array.from(document.querySelectorAll(".alts li")).every(e=>{let k=e.querySelector(".k").getBoundingClientRect(),c=e.querySelector(".cm").getBoundingClientRect();return k.right<=c.left+1 || k.bottom<=c.top+1})'),(slug,q['k'],'sobreposição')
    assert page.evaluate('document.documentElement.scrollWidth<=innerWidth'),(slug,q['k'],'overflow horizontal')
    # A última explicação pode ser alcançada, mesmo nas questões extensas.
    mostrar(page,'.estado-resposta',page.locator('.estado-resposta').count()-1)
    assert page.locator('.estado-resposta').last.is_visible()
    questions+=1
   for k in ['ecg_evolucao',exam+'_evolucao']:
    page.evaluate('(k)=>ir(porId(k))',k)
    # Um slide só: setas ocultas até o clique, depois setas, achados e laudo.
    if w>900:
     assert page.locator('.vv-estudo').count()==1,(slug,k)
     assert page.locator('.vv-est-fig .sa').count()>=2,(slug,k,'setas')
     assert page.evaluate('getComputedStyle(document.querySelector(".vv-est-fig .an")).visibility')=='hidden'
    before=page.locator('.vv-est-fig svg image').bounding_box()
    mostrar(page,'figure.amplia').click()
    if w>900:
     enlarged=page.locator('.lupa svg image').bounding_box()
     assert enlarged['width']>before['width'] or enlarged['height']>before['height'],(slug,k,'lupa não ampliou')
    assert page.locator('.lupa svg image').get_attribute('href').startswith('data:image/')
    assert page.evaluate('getComputedStyle(document.querySelector(".lupa .an")).visibility')=='hidden',(slug,k,'lupa revelou setas')
    page.keyboard.press('Escape')
    mostrar(page,'.vv-est-rev summary').click();page.wait_for_timeout(200)
    assert page.evaluate('etapa().k')==k
    assert page.evaluate('getComputedStyle(document.querySelector(".vv-est-fig .an")).visibility')=='visible'
    assert page.locator('.vv-achados li').count()==page.locator('.vv-est-fig .sa').count()
    assert page.locator('.vv-laudo').count()==1
    if w>900:
     assert page.evaluate('(()=>{const s=document.querySelector(".vv-est-fig svg").getBoundingClientRect(),i=document.querySelector(".vv-est-fig svg image").getBoundingClientRect();return Math.abs(s.width-i.width)<2&&Math.abs(s.height-i.height)<2})()'),(slug,k,'faixa lateral')
     assert page.evaluate('partesTela.length')==1,(slug,k,'mais de uma parte')
    mostrar(page,'.vv-est-rev summary').click()
   names=page.evaluate('ETAPAS.filter(e=>e.t==="pedido").flatMap(e=>e.grupos.flatMap(g=>g.o.map(o=>o.e)))')
   if slug=='west-nile':assert 'Tomografia de crânio sem contraste' not in names
   if slug=='cocaina-levamisol':assert 'Ultrassonografia renal' not in names
  print(w,h,questions,'questões confirmadas + 6 pares de imagem OK',flush=True)
 assert not errors,errors
 b.close()

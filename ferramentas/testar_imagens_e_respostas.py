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
    assert page.locator('.estudo-imagem aside').count()==0
    assert page.locator('.estudo-imagem .rot').count()==0
    before=page.locator('.estudo-imagem svg image').bounding_box()
    mostrar(page,'figure.amplia').click()
    if w>900:
     enlarged=page.locator('.lupa svg image').bounding_box()
     assert enlarged['width']>before['width'] or enlarged['height']>before['height'],(slug,k,'lupa não ampliou')
    assert page.locator('.lupa svg image').get_attribute('href').startswith('data:image/');page.keyboard.press('Escape')
    ultima(page);page.locator('#seguir').click();assert page.evaluate('etapa().k')==k+'_leitura'
    assert page.locator('.estudo-imagem .rot').count()==2
    assert page.locator('.estudo-imagem aside').count()==1
    if w>900:assert page.locator('.plano').evaluate('(e)=>e.scrollHeight<=e.clientHeight+2'),(slug,k,'leitura cortada')
    mostrar(page,'figure.amplia').click();assert page.locator('.lupa .rot').count()==2;page.keyboard.press('Escape')

    while page.evaluate('parteTela')>0:page.locator('#voltar').click()
    page.locator('#voltar').click();assert page.evaluate('etapa().k')==k
   names=page.evaluate('ETAPAS.filter(e=>e.t==="pedido").flatMap(e=>e.grupos.flatMap(g=>g.o.map(o=>o.e)))')
   if slug=='west-nile':assert 'Tomografia de crânio sem contraste' not in names
   if slug=='cocaina-levamisol':assert 'Ultrassonografia renal' not in names
  print(w,h,questions,'questões confirmadas + 6 pares de imagem OK',flush=True)
 assert not errors,errors
 b.close()

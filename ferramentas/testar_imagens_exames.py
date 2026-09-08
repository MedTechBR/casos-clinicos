"""Exames pedidos, laudos optativos e enunciados clínicos nas três apresentações."""
from pathlib import Path
from ui_paginas import mostrar, ultima
from playwright.sync_api import sync_playwright
ROOT=Path(__file__).resolve().parents[1]
CONFIG={
 'west-nile':[('ex1','res1',['Radiografia de tórax']),('ex2','res2',['Ressonância de encéfalo e medula'])],
 'cocaina-levamisol':[('p1','r1',['Radiografia de tórax'])],
 'pulmao-rim':[('ex_amb','res_amb',['Radiografia de tórax']),('ex_adm','res_adm',['Radiografia de tórax'])]}
with sync_playwright() as pw:
 browser=pw.chromium.launch();page=browser.new_page(viewport={'width':1366,'height':768});errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
 for slug,rounds in CONFIG.items():
  page.goto((ROOT/'saida'/f'{slug}-etapas.html').as_uri())
  for order in page.evaluate('ETAPAS.filter(e=>e.t==="pedido").map(e=>({k:e.k,enunciado:e.enunciado}))'):
   assert '?' in order['enunciado'],(slug,order['k'],'sem pergunta contextual')
   page.evaluate('(k)=>ir(porId(k))',order['k'])
   assert page.locator('.enun').is_visible()
   assert page.evaluate('document.querySelector(".alts").clientHeight>150'),(slug,order['k'],'catálogo sem espaço')
   page.screenshot(path=str(ROOT/'saida/revisao'/f'pedido-{slug}-{order["k"]}.png'))
  for order,result,names in rounds:
   # Um exame de imagem não selecionado não aparece no painel.
   page.evaluate('(k)=>ir(porId(k))',result);assert page.locator('.rc img').count()==0
   page.evaluate('(k)=>ir(porId(k))',order)
   # Teste isolado do renderizador; o fluxo de confirmação tem suíte própria.
   page.evaluate('([order,names,result])=>{marcados[order]=new Set(names);ir(porId(result))}',[order,names,result])
   assert page.locator('.rc').count()==len(names)
   assert page.locator('.verlaudo').count()==len(names)
   assert page.locator('.rc .v').count()==0,(slug,order,'laudo vazou de outra rodada')
   assert page.evaluate('Array.from(document.querySelectorAll(".rc img")).every(i=>i.complete&&i.naturalWidth>0)')
   mostrar(page,'figure.amplia').click();assert page.locator('.lupa').count()==1
   page.keyboard.press('Escape');assert page.locator('.lupa').count()==0
   mostrar(page,'.verlaudo').click();assert page.locator('.rc .v').count()==1
   page.screenshot(path=str(ROOT/'saida/revisao'/f'exames-{slug}-{order}.png'))
  print(slug,'pedidos, imagens, laudos e lupa OK',flush=True)
 assert not errors,errors;browser.close()

"""Regressão: cada escolha de amostragem entrega o procedimento correspondente."""
from pathlib import Path
from playwright.sync_api import sync_playwright
root=Path(__file__).resolve().parents[1]
with sync_playwright() as pw:
 b=pw.chromium.launch();p=b.new_page(viewport={'width':1366,'height':768})
 for label,choice,nextchoice,expected in [('cirurgia',1,None,['avaliacao_cirurgica','microbiologia_tecido']),('ebus_cirurgia',0,0,['coleta_ebus','b_amostra','avaliacao_cirurgica','microbiologia_tecido']),('ebus_repetida',0,1,['coleta_ebus','b_amostra','repetir_ebus','microbiologia_tecido'])]:
  p.goto((root/'saida/sarcoidose-etapas.html').as_uri());p.evaluate('ir(porId("b1"))')
  p.evaluate('(c)=>document.querySelectorAll(".cam")[c].click()',choice);p.evaluate('adiante()')
  visited=[]
  for target in expected:
   assert p.evaluate('etapa().k')==target,(label,target,p.evaluate('etapa().k'))
   visited.append(target)
   p.wait_for_timeout(450)
   if target=='avaliacao_cirurgica':
    txt=p.locator('#areaTela').inner_text() if p.locator('#areaTela').count() else p.evaluate('areaTela.innerText')
    assert 'paratraqueal' in txt
   if target=='b_amostra':p.evaluate('(c)=>document.querySelectorAll(".cam")[c].click()',nextchoice)
   while p.evaluate('temProximaParte()'):p.evaluate('virarParte(1)')
   p.evaluate('adiante()')
  print(label,visited)
 b.close()

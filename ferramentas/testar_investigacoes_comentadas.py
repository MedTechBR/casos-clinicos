"""Confirmação, gabarito velado, resultados exatos e uma tela para cada combinação."""
from itertools import combinations
from pathlib import Path
from playwright.sync_api import sync_playwright
ROOT=Path(__file__).resolve().parents[1]
with sync_playwright() as pw:
 b=pw.chromium.launch();p=b.new_page();errors=[];p.on('pageerror',lambda e:errors.append(str(e)));total=0
 for w,h in [(1366,768),(1600,900),(375,812)]:
  p.set_viewport_size({'width':w,'height':h})
  for slug in ['pulmao-rim','west-nile','cocaina-levamisol']:
   p.goto((ROOT/(slug+'.html')).as_uri())
   pedidos=p.evaluate('ETAPAS.filter(e=>e.comentado).map(e=>({k:e.k,n:e.escolhas,alts:e.alts}))')
   assert len(pedidos)==3
   for e in pedidos:
    for combo in combinations(range(6),e['n']):
     p.evaluate('(k)=>{recomecar();ir(porId(k))}',e['k'])
     assert not p.evaluate('podeAdiante()')
     assert not p.locator('.cm:visible').count()
     assert p.locator('#conf').is_disabled()
     for k in combo:p.locator('.alts li').nth(k).evaluate('(el)=>el.click()')
     assert not p.evaluate('podeAdiante()')
     assert p.evaluate('Object.keys(marcados).length')==0
     p.locator('#conf').evaluate('(el)=>el.click()')
     assert p.evaluate('podeAdiante() && partesTela.length===1')
     assert p.locator('#manter-selecao').count()==0
     assert p.locator('.cm:visible').count()==6
     expected={n for a in e['alts'] if a['ok'] for n in a['exames']}
     assert set(p.evaluate('(k)=>[...marcados[k]]',e['k']))==expected
     assert p.evaluate('areaTela.scrollHeight<=areaTela.clientHeight+2')
     p.locator('#seguir').evaluate('(el)=>el.click()')
     assert p.evaluate('etapa().t')=='resultados'
     assert set(p.locator('.rc>b').all_text_contents())==expected
     assert p.evaluate('partesTela.length===1')
     while p.locator('.verlaudo').count():p.locator('.verlaudo').first.evaluate('(el)=>el.click()')
     assert p.evaluate('areaTela.scrollHeight<=areaTela.clientHeight+2 && partesTela.length===1')
     p.locator('#voltar').evaluate('(el)=>el.click()')
     assert p.locator('#manter-selecao').count()==0
     assert p.locator('.cm:visible').count()==6
     assert set(p.evaluate('(k)=>[...marcados[k]]',e['k']))==expected
     p.locator('#seguir').evaluate('(el)=>el.click()')
     indicados={n for a in e['alts'] if a['ok'] for n in a['exames']}
     assert set(p.locator('.rc>b').all_text_contents())==indicados
     assert 'Exames realizados pela equipe' in p.locator('.sub-in').inner_text()
     assert p.evaluate('areaTela.scrollHeight<=areaTela.clientHeight+2 && partesTela.length===1')
     total+=1
   # Percurso completo pelas questões novas e decisões existentes.
   p.evaluate('recomecar()')
   for _ in range(220):
    if p.evaluate('emRevisao'):break
    p.evaluate('''()=>{let e=etapa();if((e.t==='pergunta'||e.comentado)&&!respostas[e.k]?.feita){e.alts.forEach((a,k)=>{if(a.ok)document.querySelectorAll('.alts li')[k].click()});document.querySelector('#conf').click()}if(e.t==='bifurcacao'&&escolhas[e.k]===undefined)document.querySelector('.cam').click();}''')
    assert p.evaluate('podeAdiante()'),p.evaluate('etapa().k')
    p.locator('#seguir').evaluate('(el)=>el.click()')
   assert p.evaluate('emRevisao'),slug
  print(w,h,'combinações, laudos e percursos OK',flush=True)
 assert not errors,errors
 print(total,'combinações de investigação validadas')
 b.close()

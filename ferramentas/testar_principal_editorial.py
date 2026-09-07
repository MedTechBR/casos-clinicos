"""Percursos reais, teto de exames, resultados, imagens e legibilidade dos casos novos."""
import importlib, json, itertools, sys
from pathlib import Path
from playwright.sync_api import sync_playwright
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
CONFIG={'pulmao_rim': {'full': {'ex_amb': ['Hemoglobina', 'Proteína C reativa', 'Creatinina', 'Sedimento urinário'], 'ex_adm': ['Sedimento urinário', 'Creatinina', 'Hemoglobina', 'Radiografia de tórax', 'Ultrassonografia de rins e vias urinárias', 'Hemocultura'], 'ex_mec': ['Lavado broncoalveolar', 'Cultura do lavado broncoalveolar', 'Biópsia renal', 'ANCA por imunofluorescência indireta', 'Anti-mieloperoxidase', 'Anticorpo anti-membrana basal glomerular']}, 'minimal': {'ex_amb': ['TSH'], 'ex_adm': ['Albumina'], 'ex_mec': ['Ferritina']}}}
report={}
with sync_playwright() as pw:
 b=pw.chromium.launch()
 for slug,cfg in CONFIG.items():
  m=importlib.import_module('casos.'+slug+'.etapas');steps=m.ETAPAS
  ids=[e['k'] for e in steps];assert len(ids)==len(set(ids))
  for e in steps:
   targets=[e.get('segue'),e.get('fecho')]+[c['vai'] for c in e.get('caminhos',[])]
   if e.get('rota'): targets+= [e['rota']['entao'],e['rota']['senao']]
   if e.get('conforme'):targets+=e['conforme']['para']
   assert all(t in ids for t in targets if t),(e['k'],targets)
  branches={e['k']:range(len(e['caminhos'])) for e in steps if e['t']=='bifurcacao'}
  plans=[dict(zip(branches,values)) for values in itertools.product(*branches.values())]
  if '--smoke' in sys.argv: plans=[plans[0],plans[-1]]
  # Every reachable combination is traversed; duplicates are harmless and cheap.
  page=b.new_page(viewport={'width':1600,'height':900});errors=[];page.on('pageerror',lambda err:errors.append(str(err)))
  page.goto((ROOT/'saida'/f'{slug.replace("_","-")}-etapas.html').as_uri())
  endings=set();visited=set();flows=0;layout=[]
  for mode,plan in itertools.product(['full','minimal'],plans):
   page.evaluate('recomecar()');seen=[]
   for turn in range(len(steps)+1):
    if page.locator('#seguir').count()==0:break
    e=page.evaluate('etapa()');k=e['k'];assert k not in seen,(slug,'cycle',seen,k);seen.append(k);visited.add(k)
    if e['t']=='pedido':
     for name in cfg[mode][k]:
      page.evaluate('(name)=>Array.from(document.querySelectorAll(".it")).find(x=>x.dataset.ex===name).click()',name)
     assert page.evaluate('(k)=>marcados[k].size',k)==len(cfg[mode][k]),(slug,k,'selection blocked')
     if mode=='full':
      page.evaluate('()=>{const x=document.querySelector(".it.bloq:not(.trava)");if(x)x.click()}')
      assert page.evaluate('(k)=>marcados[k].size',k)==e['limite']
    elif e['t']=='pergunta':
     bounds=page.evaluate('()=>{let a=document.querySelector(".alts"),f=document.querySelector(".folha"),z=document.querySelector("#conf");return {overflow:a.scrollHeight-a.clientHeight, bottom:z.getBoundingClientRect().bottom, footer:document.querySelector("#pe").getBoundingClientRect().top}}')
     if bounds['overflow']>2 or bounds['bottom']>bounds['footer']:layout.append((k,bounds))
     for n,a in enumerate(e['alts']):
      if a['ok']:page.locator(f'.alts li[data-k="{n}"]').click()
     page.locator('#conf').click()
    elif e['t']=='bifurcacao':page.locator(f'.cam[data-k="{plan[k]}"]').click()
    elif e['t']=='resultados':
     count=page.locator('.rc').count();assert count==len(cfg[mode][e['de']]),(slug,k,count)
    elif e['t']=='desfecho':endings.add(k)
    page.locator('#seguir').click()
   else:raise AssertionError('route exceeded authored step count')
   assert page.locator('#seguir').count()==0,(slug,'not finished')
   flows+=1
  assert not errors,errors
  assert not layout,layout[:4]
  report[slug]={'percursos':flows,'etapas_visitadas':len(visited),'etapas_total':len(steps),'desfechos':sorted(endings),'erros_js':errors,'questoes_cortadas':len(layout)}
  # Inspect all questions, including conditional antibody question absent in the full default choice.
  page.evaluate('recomecar()')
  for e in steps:
   page.evaluate('(k)=>ir(porId(k))',e['k'])
   if e['t']=='pergunta':
    assert page.evaluate('()=>{const a=document.querySelector(".alts");return a.scrollHeight<=a.clientHeight+2}')
  out=ROOT/'saida'/'revisao';out.mkdir(exist_ok=True)
  page.evaluate('recomecar()');page.screenshot(path=str(out/f'{slug}-capa.png'))
  page.evaluate('ir(porId("exame"))');page.screenshot(path=str(out/f'{slug}-exame.png'))
  page.close()
 b.close()
print(json.dumps(report,ensure_ascii=False,indent=2))
(ROOT/'saida'/'revisao'/('principal-qa-smoke.json' if '--smoke' in sys.argv else 'principal-qa.json')).write_text(json.dumps(report,ensure_ascii=False,indent=2))

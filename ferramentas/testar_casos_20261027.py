"""Regressões dos três casos: resultados indicados, fontes e ramos reais."""
import importlib
import sys
from pathlib import Path
from playwright.sync_api import sync_playwright
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from nomes_publicos import PUBLICO
CONFIG={
 'lupus_abdominal':('q3','painel_sistemico',['FAN','C3','Relação proteína/creatinina urinária']),
 'tb_peritoneal':('q2','liquido',['Albumina do sangue','Células nucleadas','Citologia']),
 'b12_microangiopatia':('q1','hemolise',['Reticulócitos','LDH','Haptoglobina']),
}
with sync_playwright() as pw:
 b=pw.chromium.launch();page=b.new_page(viewport={'width':1366,'height':768})
 for slug,(q,painel,nomes) in CONFIG.items():
  mod=importlib.import_module('casos.'+slug+'.etapas')
  ids=[e['k'] for e in mod.ETAPAS]
  assert len(ids)==len(set(ids))
  assert (mod.IMG/'cena.png.json').exists()
  for f in mod.IMG.glob('*'):
   if f.suffix in ('.jpg','.png'):assert (mod.IMG/(f.name+'.json')).exists(),f
  page.goto((ROOT/(PUBLICO[slug]+'.html')).as_uri())
  before=[]
  for correct in [False,True]:
   page.evaluate('''({q,correct})=>{let e=ETAPAS[porId(q)];respostas[q]={feita:true,marcadas:e.alts.map((a,i)=>!!a.ok===correct?i:-1).filter(i=>i>=0).slice(0,e.escolhas)}}''',{'q':q,'correct':correct})
   page.evaluate('(k)=>ir(porId(k))',painel)
   value=page.locator('#palco').inner_text()
   assert all(n in value for n in nomes),(slug,value)
   before.append(value)
  assert before[0]==before[1],(slug,'resultados mudaram conforme resposta')
  for e in mod.ETAPAS:
   if 'vv-estudo' not in e.get('corpo',''):continue
   page.evaluate('(k)=>ir(porId(k))',e['k'])
   assert page.locator('details').get_attribute('open') is None
   assert page.locator('figure svg image').count()==1
   assert page.locator('figure svg image').get_attribute('href').startswith('data:')
   page.locator('figure.amplia').click()
   assert page.locator('.lupa').is_visible()
   page.keyboard.press('Escape')
  if slug=='tb_peritoneal':
   byid={e['k']:e for e in mod.ETAPAS}
   assert byid['core_repetido']['segue']=='histologia'
   assert byid['laparoscopia']['segue']=='imagem_laparoscopia'
   assert byid['imagem_laparoscopia']['segue']=='histologia'
  print(slug,'resultados independentes da resposta; créditos, imagens e ampliação OK',flush=True)
 b.close()

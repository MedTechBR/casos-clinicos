"""Percorre cada caso por todas as combinações de bifurcação, com painel de
exames completo e mínimo, respondendo certo a perguntas e pareamentos.

Confere: destinos existentes, ausência de ciclo, erro de JavaScript, imagem
quebrada, <image> sem data: URI, teto do pedido, resultados devolvidos, e
que nenhuma página transborda (areaTela) em 1600×900 e 1366×768.

Uso:  python3 ferramentas/percorrer_casos.py [slug ...] [--smoke] [--prints]
"""
import importlib, itertools, json, sys
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

CONFIG = {
 'pulmao_rim': dict(
   full={'ex_amb': ['Hemoglobina', 'Proteína C reativa', 'Creatinina', 'Sedimento urinário'],
         'ex_adm': ['Sedimento urinário', 'Ultrassonografia de rins e vias urinárias',
                    'Radiografia de tórax', 'Tomografia de tórax', 'Hemocultura',
                    'Esfregaço de sangue periférico'],
         'ex_mec': ['Lavado broncoalveolar', 'Cultura do lavado broncoalveolar',
                    'Biópsia renal', 'ANCA por imunofluorescência indireta',
                    'Anti-mieloperoxidase', 'Anticorpo anti-membrana basal glomerular']},
   minimal={'ex_amb': ['TSH'], 'ex_adm': ['Lactato'], 'ex_mec': ['Ferritina']}),
 'west_nile': dict(
   full={'ex1': ['Hemograma', 'Eletrólitos e função renal', 'Glicemia', 'Hemoculturas iniciais'],
         'ex2': ['Líquor: celularidade, proteína, glicose e Gram', 'PCR para HSV e VZV no líquor',
                 'Eletroneuromiografia', 'Ressonância de encéfalo e medula'],
         'ex3': ['IgM para vírus do Nilo Ocidental em soro e líquor', 'Nova eletroneuromiografia',
                 'Nova PCR para HSV no líquor', 'Sorologia para encefalite de Saint Louis']},
   minimal={'ex1': ['TSH'], 'ex2': ['Amônia'], 'ex3': ['Cobre sérico']}),
 'cocaina_levamisol': dict(
   full={'p1': ['Hemograma diferencial', 'Hemoculturas iniciais', 'Coagulograma', 'Creatinina inicial'],
         'p2': ['Biópsia cutânea', 'Sedimento urinário', 'Creatinina de reavaliação', 'Anti-MPO'],
         'p3': ['Biópsia renal', 'Creatinina atual', 'Benzoilecgonina urinária',
                'Levamisol urinário por LC-MS/MS']},
   minimal={'p1': ['Lactato'], 'p2': ['Complemento C3'], 'p3': ['Anti-MBG']},
   dupla={'p1': ['Hemograma diferencial', 'Hemoculturas iniciais', 'Lactato', 'Urina inicial'],
          'p2': ['Biópsia cutânea', 'Sedimento urinário', 'Anti-MPO', 'Anti-PR3'],
          'p3': ['Creatinina atual', 'Benzoilecgonina urinária', 'Levamisol urinário por LC-MS/MS',
                 'Hemograma de controle']}),
}

args = [a for a in sys.argv[1:] if not a.startswith('--')]
slugs = args or list(CONFIG)
smoke = '--smoke' in sys.argv
prints = '--prints' in sys.argv

report = {}
with sync_playwright() as pw:
  b = pw.chromium.launch()
  for slug in slugs:
    cfg = CONFIG[slug]
    m = importlib.import_module('casos.' + slug + '.etapas'); steps = m.ETAPAS
    ids = [e['k'] for e in steps]; assert len(ids) == len(set(ids)), 'id repetido'
    for e in steps:
      targets = [e.get('segue'), e.get('fecho')] + [c['vai'] for c in e.get('caminhos', [])]
      if e.get('rota'): targets += [e['rota']['entao'], e['rota']['senao']]
      if e.get('conforme'): targets += e['conforme']['para']
      faltam = [t for t in targets if t and t not in ids]
      assert not faltam, (slug, e['k'], 'destino inexistente', faltam)
    branches = {e['k']: range(len(e['caminhos'])) for e in steps if e['t'] == 'bifurcacao'}
    plans = [dict(zip(branches, v)) for v in itertools.product(*branches.values())]
    if smoke: plans = [plans[0], plans[-1]]
    html = (ROOT / 'saida' / f'{slug.replace("_", "-")}-etapas.html').as_uri()
    errors, layout, visited, endings, flows = [], [], set(), set(), 0
    for (w, h) in ([(1600, 900)] if smoke else [(1600, 900), (1366, 768)]):
      page = b.new_page(viewport={'width': w, 'height': h})
      page.on('pageerror', lambda err: errors.append(str(err)))
      page.on('console', lambda msg: errors.append('console: ' + msg.text) if msg.type == 'error' else None)
      page.goto(html)
      for mode, plan in itertools.product(list(cfg), plans):
        page.evaluate('recomecar()'); seen = []
        for turn in range(len(steps) + 2):
          if page.evaluate('emRevisao'): break
          e = page.evaluate('({t: etapa().t, k: etapa().k})'); k = e['k']
          assert k not in seen, (slug, 'ciclo', seen[-3:], k); seen.append(k); visited.add(k)
          quebradas = page.evaluate('''() => [...document.querySelectorAll('img')]
              .filter(i => !i.complete || i.naturalWidth === 0).map(i => i.alt)''')
          if quebradas: errors.append(f'{slug} {k}: imagem quebrada {quebradas}')
          svgsem = page.evaluate('''() => [...document.querySelectorAll('image')]
              .filter(i => !(i.getAttribute('href')||'').startsWith('data:')).length''')
          if svgsem: errors.append(f'{slug} {k}: {svgsem} <image> sem data: URI')
          if e['t'] == 'pedido':
            for nome in cfg[mode][k]:
              ok = page.evaluate('''n => { const l = [...document.querySelectorAll('.it[data-ex]')]
                  .find(x => x.dataset.ex === n); if (!l) return false; l.click(); return true; }''', nome)
              assert ok, (slug, k, 'rótulo ausente', nome)
            n = page.evaluate('(marcados[etapa().k]||new Set()).size')
            assert n == len(cfg[mode][k]), (slug, k, 'marcou', n)
            if mode == 'full':
              page.evaluate('''() => { const l = [...document.querySelectorAll('.it[data-ex]:not(.on):not(.trava)')][0]; if (l) l.click(); }''')
              assert page.evaluate('(marcados[etapa().k]||new Set()).size') == n, (slug, k, 'teto furado')
          elif e['t'] == 'pergunta':
            page.evaluate('''() => { [...document.querySelectorAll('.alts li.certa')].forEach(li => li.click()); }''')
            assert not page.evaluate('document.getElementById("conf").disabled'), (slug, k, 'confirmar travado')
            page.evaluate('document.getElementById("conf").click()')
          elif e['t'] == 'pareamento':
            page.evaluate('''() => { const e = etapa(); e.itens.forEach((it, n) =>
                document.querySelector('.pi[data-n="'+n+'"] .pe[data-m="'+it.ok+'"]').click()); }''')
            assert not page.evaluate('document.getElementById("conf").disabled'), (slug, k, 'pareamento travado')
            page.evaluate('document.getElementById("conf").click()')
            assert page.evaluate('(k)=>respostas[k].feita', k)
          elif e['t'] == 'bifurcacao':
            page.evaluate('k => document.querySelectorAll(".cam")[k].click()', plan[k])
          elif e['t'] == 'resultados':
            c = page.locator('.rc').count()
            esperado = page.evaluate('()=>{const e=etapa();return e.todos?e.todos.length:(marcados[e.de]||new Set()).size}')
            assert c == esperado, (slug, k, 'cartões', c, esperado)
          elif e['t'] == 'desfecho': endings.add(k)
          # cada parte da página deve caber
          partes = page.evaluate('partesTela.length')
          for n in range(partes):
            page.evaluate('(n)=>{parteTela=n;aplicarParte();pintarPe()}', n)
            bounds = page.evaluate('''() => { const a = areaTela; if (!a) return [0,0,0];
               const r = a.getBoundingClientRect();
               return [a.scrollHeight - a.clientHeight, a.scrollWidth - a.clientWidth,
                       r.bottom - document.querySelector('#pe').getBoundingClientRect().top]; }''')
            if max(bounds) > 2: layout.append((w, mode, k, n, bounds))
          if e['t'] in ('pergunta', 'pareamento', 'resultados', 'bifurcacao'):
            if partes != 1: layout.append((w, mode, k, 'partes', partes))
          while page.evaluate('temProximaParte()'): page.evaluate('virarParte(1)')
          assert page.evaluate('podeAdiante()'), (slug, k, 'travou')
          page.evaluate('adiante()')
        else:
          raise AssertionError((slug, 'percurso não terminou', seen[-5:]))
        assert page.evaluate('emRevisao'), (slug, 'sem revisão')
        flows += 1
      page.close()
    report[slug] = dict(percursos=flows, visitadas=len(visited), total=len(steps),
                        nao_visitadas=sorted(set(ids) - visited), desfechos=sorted(endings),
                        erros=errors, layout=layout[:12], n_layout=len(layout))
    print(json.dumps(report[slug], ensure_ascii=False, indent=1), flush=True)
    if prints:
      out = ROOT / 'saida' / 'revisao'; out.mkdir(exist_ok=True)
      page = b.new_page(viewport={'width': 1600, 'height': 900})
      page.goto(html)
      for e in steps:
        if e['t'] in ('pergunta', 'pareamento', 'pedido', 'bifurcacao'):
          page.evaluate('(k)=>ir(porId(k))', e['k'])
          page.screenshot(path=str(out / f'{slug}-{e["k"]}-a.png'))
          if e['t'] == 'pergunta':
            page.evaluate('''() => { [...document.querySelectorAll('.alts li.certa')].forEach(li => li.click()); document.getElementById('conf').click(); }''')
          elif e['t'] == 'pareamento':
            page.evaluate('''() => { const e = etapa(); e.itens.forEach((it, n) =>
                document.querySelector('.pi[data-n="'+n+'"] .pe[data-m="'+((it.ok+1)%e.ops.length)+'"]').click()); document.getElementById('conf').click(); }''')
          elif e['t'] == 'bifurcacao':
            page.evaluate('document.querySelectorAll(".cam")[0].click()')
          else: continue
          page.screenshot(path=str(out / f'{slug}-{e["k"]}-b.png'))
      page.close()
  b.close()
bad = {s: r for s, r in report.items() if r['erros'] or r['n_layout'] or r['nao_visitadas']}
print('\nRESUMO:', 'tudo limpo' if not bad else json.dumps({s: dict(erros=r['erros'][:5], layout=r['layout'][:8], nao_visitadas=r['nao_visitadas']) for s, r in bad.items()}, ensure_ascii=False, indent=1))

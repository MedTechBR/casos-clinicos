"""Mede a escala do texto (--compacto) em cada tela de um caso, a 1366×768.

Telas de pergunta, pareamento, resultados e imagem encolhem o texto para
caber sem rolagem. Abaixo de 0,85 a letra fica pequena demais para projetar:
a tela deve ser dividida (painel em dois, explicação mais curta, menos
alternativas). Responde as perguntas certo antes de medir, porque a
explicação só aparece depois da resposta.

Uso:  python3 ferramentas/medir_escala.py <slug> [limite]
"""
import sys
from pathlib import Path
from playwright.sync_api import sync_playwright
ROOT = Path(__file__).resolve().parents[1]; sys.path.insert(0, str(ROOT))
from nomes_publicos import PUBLICO

slug = sys.argv[1]; limite = float(sys.argv[2]) if len(sys.argv) > 2 else 0.85
arq = ROOT / (PUBLICO[slug] + '.html'); ruins = 0
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={'width': 1366, 'height': 768})
    pg.goto(arq.as_uri()); pg.wait_for_timeout(300)
    for e in pg.evaluate('ETAPAS.map(e=>({k:e.k,t:e.t}))'):
        pg.evaluate('(k)=>ir(porId(k))', e['k']); pg.wait_for_timeout(120)
        if e['t'] == 'pergunta':
            pg.evaluate("()=>{const e=etapa();respostas[e.k]={feita:true,marcadas:e.alts.map((a,i)=>a.ok?i:-1).filter(i=>i>=0)};pintar()}")
        if e['t'] == 'pareamento':
            pg.evaluate("()=>{const e=etapa();respostas[e.k]={feita:true,marcadas:e.itens.map(it=>it.ok)};pintar()}")
        pg.wait_for_timeout(120)
        c = float(pg.evaluate('getComputedStyle(document.querySelector(".plano,.folha,.fim .caixa")||document.body).getPropertyValue("--compacto")||1') or 1)
        partes = pg.evaluate('partesTela.length')
        if c < limite:
            ruins += 1; print(f'  {e["k"]:18} {e["t"]:12} escala {c:.2f}')
    b.close()
print('OK' if not ruins else f'{ruins} tela(s) abaixo de {limite}')

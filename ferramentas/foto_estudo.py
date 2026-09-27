"""Fotografa a figura de uma tela de imagem com as setas abertas.

Uso:  python3 ferramentas/foto_estudo.py <slug> <id-da-tela> <saida.png>
Serve para conferir, OLHANDO, se cada seta cai na estrutura que o texto diz.
"""
import sys
from pathlib import Path
from playwright.sync_api import sync_playwright
ROOT = Path(__file__).resolve().parents[1]; sys.path.insert(0, str(ROOT))
from nomes_publicos import PUBLICO
slug, k, out = sys.argv[1:4]
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={'width': 1600, 'height': 900}, device_scale_factor=2)
    pg.goto((ROOT / (PUBLICO[slug] + '.html')).as_uri()); pg.evaluate('(k)=>ir(porId(k))', k); pg.wait_for_timeout(400)
    pg.locator('.vv-est-rev summary').click(); pg.wait_for_timeout(3000); pg.mouse.move(2, 2)
    pg.locator('.vv-est-fig .anot svg').screenshot(path=out); b.close()
print(out)

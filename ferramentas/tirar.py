"""Capturas de tela dos slides, para revisão visual antes de entregar.

Uso:
  python3 ferramentas/tirar.py                 todos os slides
  python3 ferramentas/tirar.py 2 4 16 21       só esses
  python3 ferramentas/tirar.py --passos 16     um PNG por passo de revelação
"""

from __future__ import annotations

import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
DEST = RAIZ / "saida" / "revisao"


def tirar(caminho: Path, quais=None, por_passo=False, dest: Path = DEST, sufixo=""):
    from playwright.sync_api import sync_playwright

    dest.mkdir(parents=True, exist_ok=True)
    feitas = []
    with sync_playwright() as pw:
        b = pw.chromium.launch()
        pg = b.new_page(viewport={"width": 1280, "height": 720}, device_scale_factor=2)
        pg.goto(caminho.resolve().as_uri())
        pg.wait_for_timeout(400)
        # palco em escala 1:1, sem a ajuda flutuante
        pg.evaluate("document.getElementById('stage').style.transform='none';"
                    "document.getElementById('help').style.display='none';"
                    "document.getElementById('gavb').style.display='none';")
        total = pg.evaluate("document.querySelectorAll('.slide').length")
        alvos = quais or range(1, total + 1)
        for n in alvos:
            pg.evaluate(f"show({int(n) - 1})")
            if por_passo:
                k = 0
                while True:
                    pg.wait_for_timeout(120)
                    a = dest / f"s{int(n):02d}-passo{k}{sufixo}.png"
                    pg.locator(".slide.on").screenshot(path=str(a))
                    feitas.append(a)
                    if not pg.evaluate("avancar()"):
                        break
                    k += 1
            else:
                pg.keyboard.press("a")  # revisão é com tudo à mostra
                pg.wait_for_timeout(140)
                a = dest / f"s{int(n):02d}{sufixo}.png"
                pg.locator(".slide.on").screenshot(path=str(a))
                feitas.append(a)
        b.close()
    print(f"{len(feitas)} capturas em {dest.relative_to(RAIZ)}")
    return feitas


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    tirar(RAIZ / "saida" / "pulmao-rim.html", [int(a) for a in args] or None,
          "--passos" in sys.argv)

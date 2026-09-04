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


def alvo(caso="pulmao_rim") -> Path:
    """O HTML montado do caso. Cravar o nome aqui faz a ferramenta medir
    um arquivo e escrever em outro quando existir um segundo caso."""
    import importlib
    import sys as _s
    _s.path.insert(0, str(RAIZ))
    m = importlib.import_module(f"casos.{caso}.caso")
    return RAIZ / "saida" / f"{m.SLUG}.html"


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
    caso = next((a for a in args if not a.isdigit()), "pulmao_rim")
    nums = [int(a) for a in args if a.isdigit()]
    tirar(alvo(caso), nums or None, "--passos" in sys.argv)


def folha_de_contato(caminho: Path, dest: Path = None, colunas: int = 5):
    """Uma folha só com todos os slides, para olhar o conjunto de uma vez.

    Revisar slide a slide esconde problema de ritmo: três slides densos
    seguidos, ou quatro slides quase vazios, só aparecem no conjunto.
    """
    from playwright.sync_api import sync_playwright

    dest = dest or DEST / "contato.png"
    dest.parent.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as pw:
        b = pw.chromium.launch()
        pg = b.new_page(viewport={"width": 1280, "height": 720})
        pg.goto(caminho.resolve().as_uri())
        pg.wait_for_timeout(400)
        n = pg.evaluate("document.querySelectorAll('.slide').length")
        pg.evaluate(
            """(cols) => {
            document.querySelectorAll('#help,#gavb,#gav,.bar,#etapas').forEach(e=>e.remove());
            document.querySelectorAll('.slide').forEach(s => {
                s.classList.add('on');
                s.querySelectorAll('.rv,.pv,svg.ov.rvov,.terr,.tl .m').forEach(e=>e.classList.add('on'));
                s.querySelectorAll('figure.an').forEach(e=>e.classList.add('on'));
                s.querySelectorAll('table.oc tbody tr').forEach(r=>r.classList.remove('hid'));
                s.style.cssText = 'position:relative;inset:auto;width:1280px;height:720px;'
                                + 'outline:1px solid #333;flex:none';
            });
            const st = document.getElementById('stage');
            st.style.cssText = 'width:auto;height:auto;transform:none;zoom:.235;'
                             + 'display:grid;box-shadow:none;'
                             + 'grid-template-columns:repeat(' + cols + ',1280px);gap:90px';
            const w = document.getElementById('wrap');
            w.style.cssText = 'position:static;display:block;background:#0d0c0a;padding:18px';
            document.body.style.cssText = 'overflow:visible;background:#0d0c0a;height:auto';
            document.documentElement.style.cssText = 'overflow:visible;height:auto';
        }""",
            colunas,
        )
        pg.wait_for_timeout(900)
        # o palco escalado não empurra o layout: a caixa que o navegador
        # enxerga é a do tamanho original. Fixamos a viewport pela conta.
        larg = int(colunas * (1280 + 90) * 0.235) + 40
        pg.set_viewport_size({"width": max(600, larg), "height": 900})
        pg.wait_for_timeout(700)
        pg.screenshot(path=str(dest), full_page=True)
        b.close()
    print(f"folha de contato: {dest.relative_to(RAIZ)}  ({n} slides)")
    return dest

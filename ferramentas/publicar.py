"""HTML -> PDF, para levar em papel.

Imprime com tudo revelado — no papel não existe clique — e com as notas do
apresentador, que só aparecem em `@media print`. Um slide por página, 1280x720.

Uso:  python3 ferramentas/publicar.py [saida/pulmao-rim.html]
"""

from __future__ import annotations

import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ))


def publicar(caminho: Path, destino: Path = None) -> Path:
    from playwright.sync_api import sync_playwright

    destino = destino or caminho.with_suffix(".pdf")
    with sync_playwright() as pw:
        b = pw.chromium.launch()
        pg = b.new_page()
        pg.goto(caminho.resolve().as_uri())
        pg.wait_for_timeout(500)
        # o CSS de impressão já revela tudo; garantimos o estado no DOM também
        pg.evaluate("document.querySelectorAll('.slide').forEach(s=>{"
                    "s.querySelectorAll('.rv,.pv,svg.ov.rvov').forEach(e=>e.classList.add('on'));"
                    "s.querySelectorAll('table.oc tbody tr').forEach(r=>r.classList.remove('hid'));"
                    "s.querySelectorAll('figure.an').forEach(f=>f.classList.add('on'));});")
        pg.emulate_media(media="print")
        pg.pdf(path=str(destino), width="1280px", height="720px",
               print_background=True, margin={"top": "0", "bottom": "0",
                                              "left": "0", "right": "0"})
        b.close()
    kb = destino.stat().st_size / 1024
    print(f"{destino.relative_to(RAIZ)}  ·  {kb:,.0f} KB")
    return destino


if __name__ == "__main__":
    from ferramentas.tirar import alvo as _alvo
    a = sys.argv[1] if len(sys.argv) > 1 else "pulmao_rim"
    alvo = Path(a) if a.endswith(".html") else _alvo(a)
    publicar(alvo)

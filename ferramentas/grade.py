"""Grade de coordenadas sobre as imagens do caso.

Serve para escolher onde a seta vai: as marcas de `figura_anotada` são escritas
em porcentagem (0 a 100 nos dois eixos), e esta grade mostra exatamente onde
cada porcentagem cai na imagem. Nomear estrutura sem conseguir identificá-la no
plano é o erro que esta ferramenta existe para impedir.

Uso:  python3 ferramentas/grade.py [nome_do_caso]
"""

from __future__ import annotations

import base64
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ))

from motor.imagens import dimensoes  # noqa: E402


def grade(img: Path, destino: Path, passo: int = 10):
    from playwright.sync_api import sync_playwright

    w, h = dimensoes(img)
    b64 = base64.b64encode(img.read_bytes()).decode()
    linhas = []
    for p in range(0, 101, passo):
        x, y = p / 100 * w, p / 100 * h
        forte = p % 50 == 0
        cor = "#ff2d55" if forte else "rgba(0,255,200,.55)"
        lw = 2.4 if forte else 1
        linhas.append(f'<line x1="{x}" y1="0" x2="{x}" y2="{h}" stroke="{cor}" stroke-width="{lw}"/>')
        linhas.append(f'<line x1="0" y1="{y}" x2="{w}" y2="{y}" stroke="{cor}" stroke-width="{lw}"/>')
        linhas.append(
            f'<text x="{x + 4}" y="16" fill="#ff2d55" font-size="15" font-weight="700" '
            f'font-family="monospace" paint-order="stroke" stroke="#000" stroke-width="3">{p}</text>'
        )
        linhas.append(
            f'<text x="4" y="{y - 4}" fill="#ff2d55" font-size="15" font-weight="700" '
            f'font-family="monospace" paint-order="stroke" stroke="#000" stroke-width="3">{p}</text>'
        )

    html = (
        f'<body style="margin:0;background:#000">'
        f'<div style="position:relative;width:{w}px;height:{h}px">'
        f'<img src="data:image/jpeg;base64,{b64}" style="width:{w}px;height:{h}px;display:block">'
        f'<svg style="position:absolute;inset:0" width="{w}" height="{h}" '
        f'viewBox="0 0 {w} {h}">{"".join(linhas)}</svg></div></body>'
    )
    tmp = destino.parent / f"_grade_{img.stem}.html"
    tmp.write_text(html)
    with sync_playwright() as pw:
        b = pw.chromium.launch()
        pg = b.new_page(viewport={"width": w, "height": h})
        pg.goto(tmp.resolve().as_uri())
        pg.wait_for_timeout(250)
        pg.screenshot(path=str(destino))
        b.close()
    tmp.unlink()
    return destino


def main(caso="pulmao_rim"):
    src = RAIZ / "casos" / caso / "img"
    dest = RAIZ / "saida" / "revisao" / "grade"
    dest.mkdir(parents=True, exist_ok=True)
    for img in sorted(list(src.glob("*.jpg")) + list(src.glob("*.png"))):
        a = grade(img, dest / f"{img.stem}.png")
        print(f"  {a.relative_to(RAIZ)}  ({'x'.join(map(str, dimensoes(img)))})")


if __name__ == "__main__":
    main(*sys.argv[1:])

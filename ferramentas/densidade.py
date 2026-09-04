"""Escolhe a densidade tipográfica de cada slide pela medida, não pelo palpite.

O autor escreve prosa; quem decide o corpo da fonte é a régua. Para cada slide
que transborda com tudo revelado, sobe um degrau de densidade e mede de novo.
Se nem o degrau mais apertado couber, o slide tem texto demais e isso é dito —
apertar mais seria ilegível no datashow.

Uso:
  python3 ferramentas/densidade.py            mede e relata
  python3 ferramentas/densidade.py --aplicar  reescreve caso.py com o que coube
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ))

DEGRAUS = [None, "dense", "xd"]


def medir(caminho: Path):
    """Devolve, por slide, o excesso em pixels com tudo revelado."""
    from playwright.sync_api import sync_playwright

    with sync_playwright() as pw:
        b = pw.chromium.launch()
        pg = b.new_page(viewport={"width": 1400, "height": 820})
        pg.goto(caminho.resolve().as_uri())
        pg.wait_for_timeout(300)
        n = pg.evaluate("document.querySelectorAll('.slide').length")
        fora = {}
        for i in range(n):
            pg.evaluate(f"show({i})")
            pg.keyboard.press("a")
            pg.wait_for_timeout(45)
            r = pg.evaluate(
                """(k) => {
                const s = document.querySelectorAll('.slide')[k];
                const b = s.querySelector('.body') || s;
                const t = s.querySelector('h1,h2');
                return {titulo: t ? t.textContent.trim() : '',
                        classes: [...s.classList],
                        excesso: Math.max(b.scrollHeight - b.clientHeight,
                                          s.scrollHeight - s.clientHeight)};
            }""",
                i,
            )
            if r["excesso"] > 1:
                fora[i + 1] = r
        b.close()
    return fora


def _atual(classes):
    for d in ("xd", "dense"):
        if d in classes:
            return d
    return None


def sobe(d):
    return DEGRAUS[min(DEGRAUS.index(d) + 1, len(DEGRAUS) - 1)]


def aplicar(titulo: str, nova: str) -> bool:
    """Troca a densidade do slide cujo título é `titulo`, dentro de caso.py."""
    f = RAIZ / "casos/pulmao_rim/caso.py"
    src = f.read_text()
    alvo = titulo.replace('"', '\\"')
    i = src.find(f'"{alvo}"')
    if i < 0:
        print(f"  ?? não achei o slide “{titulo}” em caso.py")
        return False
    fim = src.find("\n    ),", i)
    trecho = src[i:fim]
    if "densidade=" in trecho:
        novo = re.sub(r'densidade="[a-z]*"', f'densidade="{nova}"', trecho)
    else:
        novo = trecho + f'\n        densidade="{nova}",'
    f.write_text(src[:i] + novo + src[fim:])
    return True


def _construir() -> Path:
    """Em processo separado: o módulo do caso é lido do disco a cada volta.
    Reconstruir no mesmo processo devolveria o caso em cache e a medida seria
    sempre a da versão anterior."""
    import subprocess

    subprocess.run([sys.executable, "build.py"], cwd=RAIZ, check=True,
                   capture_output=True)
    return RAIZ / "saida" / "pulmao-rim.html"


def main(aplicar_mudanca=False):
    for volta in range(1, len(DEGRAUS) + 1):
        alvo = _construir()
        fora = medir(alvo)
        if not fora:
            print(f"\nnenhum slide transborda com tudo revelado.")
            return 0
        print(f"\nvolta {volta}: {len(fora)} slide(s) transbordando")
        mudou = False
        for n, r in sorted(fora.items()):
            atual = _atual(r["classes"])
            nova = sobe(atual)
            print(f"  slide {n:2d} “{r['titulo'][:44]}” excesso {r['excesso']:3d}px "
                  f"· densidade {atual or 'normal'} → {nova}")
            if not aplicar_mudanca:
                continue
            if nova == atual:
                print(f"     !! já está na densidade mais apertada. "
                      f"Este slide tem texto demais: corte conteúdo ou divida em dois.")
                continue
            mudou |= aplicar(r["titulo"], nova)
        if not aplicar_mudanca or not mudou:
            return 1 if fora else 0
    return 1


if __name__ == "__main__":
    sys.exit(main("--aplicar" in sys.argv))

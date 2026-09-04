#!/usr/bin/env python3
"""Monta o HTML de um caso.  Uso:  python3 build.py [nome_do_caso]"""

import importlib
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent
sys.path.insert(0, str(RAIZ))

from motor.engine import build  # noqa: E402


def main(nome="pulmao_rim"):
    caso = importlib.import_module(f"casos.{nome}.caso")
    destino = RAIZ / "saida" / f"{caso.SLUG}.html"
    build(caso, destino)
    kb = destino.stat().st_size / 1024
    print(f"{destino.relative_to(RAIZ)}  ·  {len(caso.SLIDES)} entradas  ·  {kb:,.0f} KB")
    sys.stdout.flush()
    return destino


if __name__ == "__main__":
    main(*sys.argv[1:])

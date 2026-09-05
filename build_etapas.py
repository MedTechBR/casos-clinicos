"""Monta o caso em etapas.

Uso:  python3 build_etapas.py [caso]
"""

import importlib
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent
sys.path.insert(0, str(RAIZ))


def construir(caso="pulmao_rim") -> Path:
    from motor.etapas import montar
    m = importlib.import_module(f"casos.{caso}.etapas")
    destino = RAIZ / "saida" / f"{caso.replace('_', '-')}-etapas.html"
    destino.parent.mkdir(parents=True, exist_ok=True)
    destino.write_text(montar(m), encoding="utf-8")
    tipos = {}
    for e in m.ETAPAS:
        tipos[e["t"]] = tipos.get(e["t"], 0) + 1
    kb = destino.stat().st_size / 1024
    print(f"{destino.relative_to(RAIZ)}  ·  {len(m.ETAPAS)} etapas  ·  "
          + " · ".join(f"{v} {k}" for k, v in sorted(tipos.items()))
          + f"  ·  {kb:,.0f} KB")
    return destino


if __name__ == "__main__":
    construir(sys.argv[1] if len(sys.argv) > 1 else "pulmao_rim")

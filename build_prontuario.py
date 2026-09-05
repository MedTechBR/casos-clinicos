"""Monta o prontuário interativo de um caso.

Uso:  python3 build_prontuario.py [caso]
"""

import importlib
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent
sys.path.insert(0, str(RAIZ))


def construir(caso="pulmao_rim") -> Path:
    from motor.prontuario import montar
    m = importlib.import_module(f"casos.{caso}.prontuario")
    destino = RAIZ / "saida" / f"{m.SLUG}-prontuario.html"
    destino.parent.mkdir(parents=True, exist_ok=True)
    destino.write_text(montar(m), encoding="utf-8")
    kb = destino.stat().st_size / 1024
    print(f"{destino.relative_to(RAIZ)}  ·  {len(m.ACOES)} ações  ·  "
          f"{len(m.BANCO)} exames  ·  {len(m.DESFECHOS)} desfechos  ·  {kb:,.0f} KB")
    return destino


if __name__ == "__main__":
    construir(sys.argv[1] if len(sys.argv) > 1 else "pulmao_rim")

"""Entrada do banco de exames."""

from __future__ import annotations


def an(nome: str, resultado: str, *, ref: str = "—", cat: str = "",
       alterado: bool = False, sin=()) -> dict:
    """Um analito. `sin` são os nomes alternativos e os painéis a que pertence."""
    return {"n": nome, "s": list(sin), "c": cat, "r": resultado,
            "ref": ref, "a": 1 if alterado else 0}

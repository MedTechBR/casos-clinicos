"""Extrai o que o caso AFIRMA sobre cada imagem, para auditoria independente.

O risco de uma imagem ilustrativa é ela não mostrar o que a legenda diz que
mostra — e isso passa despercebido porque quem escreveu a legenda é quem
escolheu a imagem. A conferência precisa vir de fora.

Este arquivo só monta o dossiê: para cada imagem, o arquivo, a legenda, o
crédito e **a afirmação clínica que depende dela**. Quem julga são dois
auditores independentes, e a imagem só é aceita se os dois concordarem.

Uso:  python3 ferramentas/manifesto_imagens.py [caso]
"""

from __future__ import annotations

import importlib
import json
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ))


def _limpo(t: str) -> str:
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", t or "")).strip()


def manifesto(caso: str = "pulmao_rim") -> list[dict]:
    m = importlib.import_module(f"casos.{caso}.etapas")
    itens: dict[str, dict] = {}

    def registrar(arquivo, titulo, legenda, credito, onde, afirmacao=""):
        """A primeira ocorrência de uma imagem quase sempre é como FUNDO de
        tela, que não tem título, legenda nem crédito. Com `setdefault` puro, o
        vazio do fundo congelava e a lâmina verdadeira — com a legenda e o
        crédito — nunca chegava ao dossiê. O auditor recebia justamente sem os
        campos que a ferramenta existe para submeter a julgamento, e podia
        rejeitar a imagem por falta de crédito que existe no caso.

        Agora cada campo é preenchido pela primeira ocorrência que o tiver.
        """
        if not arquivo:
            return
        it = itens.setdefault(arquivo, {
            "arquivo": arquivo,
            "caminho": str((m.IMG / arquivo).resolve()),
            "titulo": "", "legenda": "", "credito": "",
            "aparece_em": [], "afirmacoes": [],
        })
        for campo, valor in (("titulo", titulo), ("legenda", legenda),
                             ("credito", credito)):
            if not it[campo] and _limpo(valor):
                it[campo] = _limpo(valor)
        it["aparece_em"].append(onde)
        if afirmacao and afirmacao not in it["afirmacoes"]:
            it["afirmacoes"].append(_limpo(afirmacao))

    for e in m.ETAPAS:
        k = e.get("k", "?")
        if e.get("fundo"):
            registrar(e["fundo"], "", "", "", f"{k} (fundo)")
        lam = e.get("lamina")
        if lam:
            registrar(lam["img"], lam["tt"], lam["lg"], lam["cr"], k)
        for nome, l in (e.get("laminas") or {}).items():
            # a afirmação que a imagem sustenta é o resultado do exame no banco
            banco = {x["n"]: x for x in m.BANCO}
            registrar(l["img"], l["tt"], l["lg"], l["cr"], f"{k} · {nome}",
                      afirmacao=_limpo(banco.get(nome, {}).get("r", "")))

    return sorted(itens.values(), key=lambda x: x["arquivo"])


if __name__ == "__main__":
    caso = sys.argv[1] if len(sys.argv) > 1 else "pulmao_rim"
    dados = manifesto(caso)
    destino = RAIZ / "saida" / f"manifesto-imagens-{caso}.json"
    destino.parent.mkdir(parents=True, exist_ok=True)
    destino.write_text(json.dumps(dados, ensure_ascii=False, indent=2))
    print(f"{len(dados)} imagens · {destino.relative_to(RAIZ)}\n")
    for d in dados:
        print(f"  {d['arquivo']}")
        print(f"     título   {d['titulo'] or '—'}")
        print(f"     legenda  {d['legenda'][:96] or '—'}")
        print(f"     afirma   {(d['afirmacoes'][0][:96] if d['afirmacoes'] else '—')}")
        print(f"     aparece  {', '.join(d['aparece_em'])}\n")

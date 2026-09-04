"""Gera casos/pulmao_rim/{caso.py,perguntas.py} a partir do HTML original."""

from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from ferramentas._extrair import cita, gerar_slide, inline, parse  # noqa: E402

RAIZ = Path(__file__).resolve().parent.parent
LETRAS = "ABCDE"


def extrair_pergunta(qsec, asec, n):
    enunciado = inline(qsec.busca("h2"))
    ul = qsec.busca("ul", "alts")
    maxsel = int(ul.attrs.get("data-max", "1"))
    duas = "duas" in ul.classes

    textos = []
    for li in ul.filhos:
        if li.tag != "li":
            continue
        k = li.busca("span", "k")
        resto = [f for f in li.filhos if f is not k]
        no = type(li)(li.tag)
        no.filhos = resto
        textos.append(inline(no))

    body = asec.busca("div", "body")
    fb = body.busca("ul", "alts")
    alts = []
    for k, li in enumerate([f for f in fb.filhos if f.tag == "li"]):
        ft = li.busca("div", "ft")
        alts.append(
            {
                "t": textos[k],
                "porque": inline(ft.busca("div", "wy")),
                "certa": "ok" in li.classes,
            }
        )
        conf = inline(ft.busca("div", "tt"))
        if conf != textos[k]:
            print(f"  !! P{n} alternativa {LETRAS[k]}: texto diverge entre os dois slides")
            print(f"     pergunta: {textos[k]}")
            print(f"     resposta: {conf}")

    certas = sum(1 for a in alts if a["certa"])
    linhas = [f"    pergunta(", f"        {n},", f"        {cita(enunciado, 8)},", "        ["]
    for a in alts:
        certa = ", certa=True" if a["certa"] else ""
        linhas.append(f"            alt(")
        linhas.append(f"                {cita(a['t'], 16)},")
        linhas.append(f"                {cita(a['porque'], 16)}{certa},")
        linhas.append(f"            ),")
    linhas.append("        ],")
    if maxsel != certas:
        linhas.append(f"        escolhas={maxsel},")
    if duas:
        linhas.append("        duas_colunas=True,")
    linhas.append("    ),")
    return "\n".join(linhas)


def main():
    origem = Path(sys.argv[1])
    src = origem.read_text()
    corpo = src[src.find("<body>") : src.find("<div id='grid'")]
    secs = [s for s in re.split(r'(?=<section class="slide)', corpo) if s.startswith("<section")]

    itens, perguntas = [], []
    i = 0
    while i < len(secs):
        sec = parse(secs[i]).filhos[0]
        c = sec.classes
        if "cover" in c:
            meta = sec.busca("div", "meta")
            spans = [f for f in meta.filhos if f.tag == "span"]
            ressalva = inline(spans[-1]) if spans else ""
            m = type(meta)(meta.tag)
            m.filhos = [f for f in meta.filhos if f not in spans]
            itens.append(
                "    capa(\n"
                f"        {cita(inline(sec.busca('h1')), 8)},\n"
                f"        {cita(inline(sec.busca('div', 'sub')), 8)},\n"
                f"        {cita(inline(m), 8)},\n"
                f"        {cita(ressalva, 8)},\n"
                "    ),"
            )
        elif "q" in c:
            n = len(perguntas) + 1
            perguntas.append(extrair_pergunta(sec, parse(secs[i + 1]).filhos[0], n))
            itens.append(f"    P{n},")
            i += 1
        else:
            itens.append(gerar_slide(sec, i + 1))
        i += 1

    cab_p = '''"""Perguntas do caso pulmão-rim.

Cada pergunta é escrita uma vez e gera os dois slides — a escolha e a resposta
comentada. A letra anunciada é calculada a partir de quem tem `certa=True`, e o
texto da alternativa é o mesmo objeto nos dois slides: não há como divergirem.

Regra editorial: 4 ou 5 alternativas, 1 ou 2 corretas, coluna única. O enunciado
começa pelo dado e termina pelo pedido. A pergunta 1 nunca lista as hipóteses
diagnósticas — a lista é o destino, não o ponto de partida.
"""

from motor.perguntas import alt, pergunta

'''
    for k, q in enumerate(perguntas, 1):
        cab_p += f"\nP{k} = " + q[4:].rstrip(",").replace("\n    ", "\n") + "\n"

    cab_c = '''"""Caso pulmão-rim — os slides, em prosa.

Homem de 63 anos com hemoptise, púrpura e queda de função renal.
Paciente ficcional, construído para ensino.

Regra editorial: história e exame físico em parágrafos corridos, como no NEJM.
Nunca em tópicos. Marcos temporais dentro da frase. Sinais vitais narrados.
Títulos são substantivos simples, sem efeito.
"""

from pathlib import Path

from motor.conteudo import (
    box, cap, cols, exame, figura, h3, lista, nota, p, painel, passo,
    revelar, sinais, tabela,
)
from motor.slides import bloco, capa, discussao, narrativa, tela

from .banco import BANCO
from .perguntas import P1, P2, P3, P4, P5, P6, P7, P8, P9

TITULO = "Homem de 63 anos com hemoptise, púrpura e queda de função renal"
SLUG = "pulmao-rim"
RODAPE = "Síndrome pulmão-rim · caso interativo"
IMG = Path(__file__).parent / "img"

SLIDES = [
'''
    saida_c = cab_c + "\n".join(itens) + "\n]\n"

    (RAIZ / "casos/pulmao_rim/perguntas.py").write_text(cab_p)
    (RAIZ / "casos/pulmao_rim/caso.py").write_text(saida_c)
    print(f"caso.py: {len(itens)} entradas · perguntas.py: {len(perguntas)} perguntas")


if __name__ == "__main__":
    main()

"""Ramificação: nós de decisão, ramos e estado do paciente.

O caso deixa de correr em linha reta. A conduta escolhida e os exames pedidos
levam o paciente por caminhos que **não reconvergem** e terminam em desfechos
distintos.

Quatro coisas alimentam o estado, que persiste entre os slides:

1. a conduta escolhida em cada nó;
2. os exames pedidos na gaveta — e os que se deixou de pedir;
3. o tempo gasto, que a função renal sente;
4. a reavaliação clínica, que libera informação nova.

Erro é recuperável, com custo. Nenhum ramo termina no nó: a escolha ruim
produz piora visível e imediata, o caso continua, e dentro do ramo ruim existe
pelo menos uma decisão de resgate. Mas o melhor final daquele ramo é pior que
o do ramo certo. O aluno nunca fica travado; ele paga.
"""

from __future__ import annotations

import json

from .conteudo import texto
from .slides import _slide

# ─────────────────────────── estado do paciente ───────────────────────────

# Prontuário, não jogo: sem pontuação, sem estrela, sem barra de vida.
CAMPOS = {
    "horas": dict(rotulo="Tempo", unidade=" h", casas=0, sobe_e_piora=True),
    "creatinina": dict(rotulo="Creatinina", unidade=" mg/dL", casas=1, sobe_e_piora=True),
    "spo2": dict(rotulo="SpO₂", unidade="%", casas=0, sobe_e_piora=False),
    "hb": dict(rotulo="Hemoglobina", unidade=" g/dL", casas=1, sobe_e_piora=False),
}

SINALIZADORES = {
    "dialise": "em diálise",
    "vm": "em ventilação mecânica",
    "plasmaferese": "plasmaférese em curso",
    "imunossupressao": "imunossupressão iniciada",
    "culturas_prejudicadas": "culturas colhidas após o corticoide",
    "antibiotico": "antibiótico de amplo espectro",
}


def estado(horas=0, creatinina=3.8, spo2=88, hb=7.8, sinalizadores=()) -> dict:
    """O estado inicial do paciente, na admissão."""
    desconhecidos = set(sinalizadores) - set(SINALIZADORES)
    if desconhecidos:
        raise ValueError(f"sinalizador desconhecido: {sorted(desconhecidos)}")
    return {
        "horas": horas, "creatinina": creatinina, "spo2": spo2, "hb": hb,
        "sinalizadores": list(sinalizadores),
    }


def efeito(horas=0, creatinina=0, spo2=0, hb=0, liga=(), desliga=()) -> dict:
    """O que uma escolha faz com o paciente. Valores são somados ao estado."""
    for s in (*liga, *desliga):
        if s not in SINALIZADORES:
            raise ValueError(f"sinalizador desconhecido: {s!r}")
    return {"horas": horas, "creatinina": creatinina, "spo2": spo2, "hb": hb,
            "liga": list(liga), "desliga": list(desliga)}


# ─────────────────────────── ramos e nós ───────────────────────────


def ramo(chave: str, texto_: str, vai_para: str, porque: str,
         efeito_: dict = None, rotulo: str = "") -> dict:
    """Um caminho a partir de um nó.

    `porque` é a justificativa fisiológica mostrada DEPOIS da escolha: a
    consequência tem de ser explicada, não só sofrida.
    """
    if not porque.strip():
        raise ValueError(f"ramo {chave!r} sem justificativa fisiológica")
    return {"chave": chave, "texto": texto_, "vai": vai_para, "porque": porque,
            "efeito": efeito_ or efeito(), "rotulo": rotulo}


def custa(slide: dict, efeito_: dict) -> dict:
    """Marca um bloco com o preço que a passagem por ele cobra do paciente.

    O quarto gatilho do estado. Nem toda deterioração vem de uma escolha
    errada: um ramo em que a investigação demora dois dias cobra do rim
    enquanto o grupo apenas assiste, e o número na barra tem de mostrar isso
    sem que ninguém tenha clicado em nada. O efeito é aplicado uma vez, na
    primeira vez que o bloco aparece — voltar ao slide não cobra de novo.
    """
    return dict(slide, custo=efeito_)


def no(ident: str, kicker: str, titulo: str, pergunta: str, ramos,
       contexto=(), densidade="dense") -> dict:
    """Um nó de decisão. De 2 a 3 ramos, que não reconvergem."""
    if not 2 <= len(ramos) <= 3:
        raise ValueError(f"nó {ident!r}: use 2 ou 3 ramos, não {len(ramos)}")
    chaves = [r["chave"] for r in ramos]
    if len(set(chaves)) != len(chaves):
        raise ValueError(f"nó {ident!r}: ramos com a mesma chave")

    itens = "".join(
        f'<li class="rm" data-ramo="{r["chave"]}" data-vai="{r["vai"]}" '
        f"data-efeito='{json.dumps(r['efeito'], ensure_ascii=False)}'>"
        f'<span class="k">{chr(65 + i)}</span>'
        f'<div class="ft"><div class="tt">{texto(r["texto"])}</div>'
        + (f'<div class="rt">{texto(r["rotulo"])}</div>' if r["rotulo"] else "")
        + f'<div class="wy" hidden>{texto(r["porque"])}</div></div></li>'
        for i, r in enumerate(ramos)
    )
    corpo = (
        f'<div class="kicker">{texto(kicker)}</div>\n<h2>{texto(titulo)}</h2>\n'
        f'<div class="body">{"".join(contexto)}'
        f'<div class="qhint">Decisão — a escolha muda o rumo do caso, '
        f'e não há volta automática</div>'
        f'<ul class="ramos">{itens}</ul></div>'
    )
    return _slide(tipo="no", classes=["no", densidade], corpo=corpo,
                  ident=ident, titulo=titulo, kicker=kicker,
                  grid=f"NÓ — {titulo}")


def desfecho(ident: str, titulo: str, *conteudo: str, qualidade: str = "medio",
             kicker: str = "Desfecho", densidade="dense") -> dict:
    """Fim de um ramo. `qualidade` situa o final entre os possíveis do caso."""
    if qualidade not in ("melhor", "medio", "pior"):
        raise ValueError("qualidade deve ser 'melhor', 'medio' ou 'pior'")
    corpo = (
        f'<div class="kicker">{texto(kicker)}</div>\n<h2>{texto(titulo)}</h2>\n'
        f'<div class="body">{"".join(conteudo)}</div>'
    )
    return _slide(tipo="desfecho", classes=["fim", f"q-{qualidade}", densidade],
                  corpo=corpo, ident=ident, titulo=titulo,
                  grid=f"FIM — {titulo}")

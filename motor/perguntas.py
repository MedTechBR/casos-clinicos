"""Perguntas.

Uma pergunta é escrita uma única vez e gera os dois slides — o de escolha e o
de resposta comentada. Antes, o texto das alternativas existia duplicado nos
dois slides e era mantido à mão; a letra anunciada no título da resposta também.
Aqui a letra é calculada e o texto é o mesmo objeto, então pergunta e resposta
não têm como divergir.
"""

from __future__ import annotations

from .conteudo import texto
from .slides import _slide

LETRAS = "ABCDE"


def alt(txt: str, porque: str, certa: bool = False) -> dict:
    """Uma alternativa. `porque` é obrigatório: toda alternativa é comentada,
    inclusive as erradas — é onde mora a discussão."""
    if not porque.strip():
        raise ValueError(f"alternativa sem justificativa: {txt!r}")
    return {"t": txt, "porque": porque, "certa": certa}


def _letras(alts) -> str:
    ls = [LETRAS[i] for i, a in enumerate(alts) if a["certa"]]
    if not ls:
        raise ValueError("pergunta sem alternativa correta")
    if len(ls) == 1:
        return ls[0]
    return " e ".join([", ".join(ls[:-1]), ls[-1]]) if len(ls) > 2 else f"{ls[0]} e {ls[1]}"


def pergunta(
    n: int,
    enunciado: str,
    alternativas,
    *,
    escolhas: int = None,
    titulo_resposta: str = "",
    duas_colunas: bool = False,
    ident: str = None,
) -> list:
    """Devolve o par [slide de pergunta, slide de resposta].

    `escolhas` é quantas o grupo pode marcar; por omissão, o número de corretas.
    """
    if not 4 <= len(alternativas) <= 5:
        raise ValueError(f"pergunta {n}: use 4 ou 5 alternativas, não {len(alternativas)}")
    certas = [a for a in alternativas if a["certa"]]
    if not 1 <= len(certas) <= 2:
        raise ValueError(f"pergunta {n}: use 1 ou 2 corretas, não {len(certas)}")
    maxsel = escolhas or len(certas)
    duas = " duas" if duas_colunas else ""

    plural = "" if maxsel == 1 else "s"
    dica = (
        f'<div class="qhint">Selecione <b>até {maxsel}</b> '
        f'<span class="cnt" data-max="{maxsel}">0 de {maxsel} marcada{plural}</span></div>'
    )
    itens = "".join(
        f'<li><span class="k">{LETRAS[i]}</span><span>{texto(a["t"])}</span></li>'
        for i, a in enumerate(alternativas)
    )
    corpo_q = (
        f'<div class="qn">Pergunta {n}</div>\n'
        f"<h2>{texto(enunciado)}</h2> {dica}"
        f'<ul class="alts multi{duas}" data-max="{maxsel}">{itens}</ul>'
    )

    fb = "".join(
        f'<li class="{"ok" if a["certa"] else "no"}"><span class="k">{LETRAS[i]}</span>'
        f'<div class="ft"><div class="tt">{texto(a["t"])}</div>'
        f'<div class="wy">{texto(a["porque"])}</div></div>'
        f'<span class="mk">&#{10003 if a["certa"] else 10007};</span></li>'
        for i, a in enumerate(alternativas)
    )
    corpo_a = (
        f'<div class="tag">Resposta {n}</div>\n<h2>{_letras(alternativas)}</h2>\n'
        f'<div class="body"><ul class="alts fb{duas}">{fb}</ul>'
        + (f'<div class="cap">{texto(titulo_resposta)}</div>' if titulo_resposta else "")
        + "</div>"
    )

    base = ident or f"p{n}"
    return [
        _slide(tipo="pergunta", classes=["q"], corpo=corpo_q, ident=base, titulo=enunciado,
               numero=n, grid=f"P{n} — {enunciado}"),
        _slide(tipo="resposta", classes=["ans", "dense"], corpo=corpo_a, ident=f"{base}_r",
               titulo=titulo_resposta or enunciado, numero=n,
               grid=f"R{n} — {titulo_resposta or _letras(alternativas)}"),
    ]

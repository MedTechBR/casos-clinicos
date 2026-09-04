"""Tipos de slide.

Cada função devolve um dicionário: o build monta a `<section>`, numera e coloca
o rodapé. O identificador é obrigatório na prática (derivado do título quando
omitido) porque é por ele que a árvore de ramificação vai apontar destinos.
"""

from __future__ import annotations

import re
import unicodedata

from .conteudo import texto

DENSIDADES = (None, "dense", "xd")


def _id(t: str) -> str:
    t = unicodedata.normalize("NFD", t).encode("ascii", "ignore").decode()
    t = re.sub(r"[^a-zA-Z0-9]+", "_", t).strip("_").lower()
    return t[:48]


def _slide(*, tipo, classes, corpo, ident=None, titulo="", **extra) -> dict:
    s = {
        "tipo": tipo,
        "classes": [c for c in classes if c],
        "corpo": corpo,
        "id": ident or _id(titulo or tipo),
        "titulo": titulo,
    }
    s.update(extra)
    return s


def _dens(d):
    if d not in DENSIDADES:
        raise ValueError(f"densidade inválida: {d!r}; use {DENSIDADES}")
    return d


def capa(titulo: str, subtitulo: str, meta: str, ressalva: str, kicker: str = "Caso clínico interativo") -> dict:
    corpo = (
        f'<div class="kicker">{texto(kicker)}</div>\n'
        f"<h1>{texto(titulo)}</h1>\n"
        f'<div class="sub">{texto(subtitulo)}</div>\n'
        f'<div class="meta">{texto(meta)}<br>\n'
        f'<span style="opacity:.72">{texto(ressalva)}</span></div>'
    )
    return _slide(tipo="capa", classes=["cover"], corpo=corpo, ident="capa", titulo="Capa")


def momento(passo: str, titulo: str, lede: str = "", ident=None) -> dict:
    """Divisor vermelho de página inteira, para marcar virada de fase."""
    corpo = (
        f'<div class="step">{texto(passo)}</div>\n<h1>{texto(titulo)}</h1>'
        + (f'\n<div class="lede">{texto(lede)}</div>' if lede else "")
    )
    return _slide(tipo="momento", classes=["mom"], corpo=corpo, ident=ident, titulo=titulo)


def _generico(tipo, base, kicker, titulo, conteudo, densidade, ident):
    corpo = (
        (f'<div class="kicker">{texto(kicker)}</div>\n' if kicker else "")
        + f"<h2>{texto(titulo)}</h2>\n"
        + f'<div class="body">\n{"".join(conteudo)}\n</div>'
    )
    return _slide(
        tipo=tipo,
        classes=[base, _dens(densidade)],
        corpo=corpo,
        ident=ident,
        titulo=titulo,
        kicker=kicker,
    )


def narrativa(kicker: str, titulo: str, *conteudo: str, densidade=None, ident=None) -> dict:
    """Prosa longa: história, exame físico, evolução. Corpo em corpo maior."""
    return _generico("narrativa", "narr", kicker, titulo, conteudo, densidade, ident)


def tela(kicker: str, titulo: str, *conteudo: str, densidade=None, ident=None) -> dict:
    """Tela de sistema: painéis de resultado sobre fundo de prontuário."""
    return _generico("tela", "screen", kicker, titulo, conteudo, densidade, ident)


def bloco(kicker: str, titulo: str, *conteudo: str, densidade=None, ident=None) -> dict:
    """Bloco comum: imagem com laudo, tabela, síntese, anexo."""
    return _generico("bloco", "", kicker, titulo, conteudo, densidade, ident)


def discussao(titulo: str, *conteudo: str, densidade="dense", ident=None) -> dict:
    # prefixo próprio: uma discussão costuma ter o mesmo título do bloco que
    # comenta ("Sedimento urinário"), e os identificadores não podem colidir.
    return _generico("discussao", "", "Discussão", titulo, conteudo, densidade,
                     ident or "d_" + _id(titulo))

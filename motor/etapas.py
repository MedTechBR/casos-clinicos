"""O caso em etapas — direção Atlas.

Uma página de cada vez. O caso se apresenta, faz uma pergunta, e a resposta
decide a página seguinte. Sem relógio e sem espera: o resultado está na virada
da folha.

A pergunta que carrega o caso é a de exames — grupos com caixas de seleção, e
só o que foi marcado volta na página de resultados. O que não foi pedido não
aparece; a revisão do fim é o único lugar em que o caso comenta o que faltou, e
ela vem quando não há mais o que decidir.

Cada tela tem um chão: a imagem médica ocupa a tela inteira, escurecida e
recuada no espaço, e o conteúdo flutua acima dela. A cor não é enfeite — cada
sistema tem a sua, e ela reaparece em todo lugar onde aquele sistema é citado.

    capa()          abertura
    pagina()        prosa, painel, figura
    pedido()        "que exames você pede?", em grupos, marcação múltipla
    resultados()    devolve só o que foi marcado
    pergunta()      escolha comentada, com o comentário de cada alternativa
    bifurcacao()    a escolha que muda a página seguinte
    desfecho()      o fim, e por quê
"""

from __future__ import annotations

import base64
import json
import mimetypes
from pathlib import Path

from .conteudo import texto

# Um sistema, uma cor. A mesma em toda a peça: no marcador do território, na
# borda do grupo de exames, no número do painel, na barra do desfecho.
SISTEMAS = {
    "via": "via aérea superior",
    "pulmao": "pulmão",
    "rim": "rim",
    "pele": "pele",
    "nervo": "nervo periférico",
    "sangue": "sangue",
    "geral": "sistêmico",
}


def _s(nome):
    if nome not in SISTEMAS:
        raise ValueError(f"sistema desconhecido: {nome!r}; use {sorted(SISTEMAS)}")
    return nome


# ─────────────────────────── blocos de conteúdo ───────────────────────────


def p(*partes) -> str:
    return f"<p>{texto(' '.join(partes))}</p>"


def lead(*partes) -> str:
    return f'<p class="lede">{texto(" ".join(partes))}</p>'


def lista(itens, ordenada=False) -> str:
    tag = "ol" if ordenada else "ul"
    return f"<{tag}>" + "".join(f"<li>{texto(i)}</li>" for i in itens) + f"</{tag}>"


def numeros(*trios) -> str:
    """Três a quatro números grandes, cada um na cor do sistema a que pertence."""
    return '<div class="nums">' + "".join(
        f'<div class="n-{_s(sis)}"><b>{texto(valor)}</b>'
        f"<span>{texto(rotulo)}</span></div>"
        for valor, rotulo, sis in trios) + "</div>"


def territorios(*itens, colunas=1) -> str:
    """Marcadores de território: cor, nome e o achado.

    O nome e o achado moram num mesmo filho: com três filhos diretos numa grade
    de duas colunas, o achado caía para a linha de baixo, na coluna estreita do
    marcador, e a prosa saía uma palavra por linha.
    """
    return f'<div class="terrs c{colunas}">' + "".join(
        f'<div class="terr t-{_s(sis)}"><i></i><div>'
        f"<b>{texto(nome)}</b><span>{texto(achado)}</span></div></div>"
        for sis, nome, achado in itens) + "</div>"


def quadro(titulo, *blocos, sistema="geral") -> str:
    return (f'<div class="qd q-{_s(sistema)}"><b>{texto(titulo)}</b>'
            f'{"".join(blocos)}</div>')


def tabela(cabecalho, linhas) -> str:
    th = "".join(f"<th>{texto(c)}</th>" for c in cabecalho)
    tr = "".join("<tr>" + "".join(f"<td>{texto(c)}</td>" for c in l) + "</tr>"
                 for l in linhas)
    return (f'<table class="tb"><thead><tr>{th}</tr></thead>'
            f"<tbody>{tr}</tbody></table>")


def lamina(arquivo, titulo, legenda, credito) -> dict:
    """A imagem em destaque, inclinada no espaço, ao lado do conteúdo."""
    return {"img": arquivo, "tt": texto(titulo), "lg": texto(legenda),
            "cr": texto(credito)}


# ─────────────────────────── páginas ───────────────────────────


def _pag(tipo, ident, **extra):
    return dict({"t": tipo, "k": ident}, **extra)


def capa(titulo, lede, *, fundo, lamina_=None, numeros_="", territorios_="",
         kicker="", ressalva="") -> dict:
    return _pag("capa", "capa", tt=texto(titulo), lede=texto(lede),
                fundo=fundo, lamina=lamina_, nums=numeros_,
                terrs=territorios_, kicker=texto(kicker),
                ressalva=texto(ressalva))


def pagina(ident, kicker, titulo, *blocos, fundo="", lamina_=None,
           nota="", sistema="geral", so_kicker=False) -> dict:
    """`so_kicker` promove o rótulo a título e descarta a manchete.

    Serve às telas em que o rótulo longo diz mais que o título curto — "onde
    dava para ter chegado antes" contra "a retrospectiva". Ter os dois é o que
    faz onze telas parecerem a mesma máquina de quatro compartimentos.
    """
    return _pag("pagina", ident, kicker=texto(kicker), tt=texto(titulo),
                corpo="".join(blocos), fundo=fundo, lamina=lamina_,
                nota=texto(nota), sis=_s(sistema),
                so_kicker=1 if so_kicker else 0)


# ─────────────────────────── o pedido de exames ───────────────────────────


def op(exame, detalhe="", *, resultado=None, referencia=None,
       alterado=None) -> dict:
    """Uma linha marcável. `exame` é o nome exato no banco do caso.

    `resultado` sobrepõe o valor do banco. É necessário porque o banco foi
    escrito para um formato com relógio, em que a hemocultura vira positiva no
    quinto dia: aqui, sem relógio, ela precisa devolver o resultado da coleta
    daquela etapa, e não o desfecho de uma complicação futura.
    """
    o = {"e": exame, "d": texto(detalhe)}
    if resultado is not None:
        o["r"] = texto(resultado)
        o["ref"] = texto(referencia) if referencia is not None else "—"
        o["a"] = 1 if alterado else 0
    return o


def grupo(nome, sistema, opcoes) -> dict:
    return {"n": texto(nome), "s": _s(sistema), "o": opcoes}


def pedido(ident, kicker, titulo, enunciado, grupos, *, fundo="",
           nota="", banco=None) -> dict:
    """Marcação múltipla, sem limite e sem sugestão."""
    vistos = set()
    for g in grupos:
        for o in g["o"]:
            if o["e"] in vistos:
                raise ValueError(f"exame repetido no pedido {ident!r}: {o['e']}")
            vistos.add(o["e"])
    sobre = {o["e"]: {"n": o["e"], "r": o["r"], "ref": o["ref"], "a": o["a"]}
             for g in grupos for o in g["o"] if "r" in o}
    # Um rótulo que não existe no banco e não traz resultado próprio é marcável,
    # soma no contador, e devolve NADA na página seguinte — sem erro e sem
    # aviso. O caso chegava a dizer "você não pediu nenhum exame" para quem
    # tinha marcado quatro. Isso passa a explodir no build.
    if banco is not None:
        nomes = {e["n"] for e in banco}
        orfaos = sorted(o["e"] for g in grupos for o in g["o"]
                        if o["e"] not in nomes and "r" not in o)
        if orfaos:
            raise ValueError(
                f"pedido {ident!r}: rótulo sem entrada no banco e sem "
                f"resultado próprio — devolveria nada: {', '.join(orfaos)}")
    return _pag("pedido", ident, kicker=texto(kicker), tt=texto(titulo),
                enunciado=texto(enunciado), grupos=grupos, fundo=fundo,
                nota=texto(nota), sobre=sobre)


def resultados(ident, kicker, titulo, de, *, fundo="", introducao="",
               nota="", laminas=None) -> dict:
    """Devolve os exames marcados no pedido `de` — e só eles.

    `laminas` associa nome de exame à imagem que ele devolve: quem pede a
    tomografia recebe a tomografia, e quem não pede não vê nada.
    """
    return _pag("resultados", ident, kicker=texto(kicker), tt=texto(titulo),
                de=de, fundo=fundo, intro=texto(introducao), nota=texto(nota),
                laminas=laminas or {})


# ─────────────────────────── perguntas ───────────────────────────


def alt(txt, porque, *, certa=False) -> dict:
    if not porque.strip():
        raise ValueError(f"alternativa sem comentário: {txt!r}")
    return {"t": texto(txt), "c": texto(porque), "ok": 1 if certa else 0}


def pergunta(ident, kicker, enunciado, alternativas, *, fundo="",
             titulo_resposta="", nota="") -> dict:
    certas = [a for a in alternativas if a["ok"]]
    if not 1 <= len(certas) <= 2:
        raise ValueError(f"pergunta {ident!r}: use 1 ou 2 corretas")
    if not 4 <= len(alternativas) <= 5:
        raise ValueError(f"pergunta {ident!r}: use 4 ou 5 alternativas")
    if not titulo_resposta.strip():
        raise ValueError(f"pergunta {ident!r}: sem título de resposta")
    return _pag("pergunta", ident, kicker=texto(kicker),
                enunciado=texto(enunciado), alts=alternativas,
                escolhas=len(certas), fundo=fundo,
                tr=texto(titulo_resposta), nota=texto(nota))


def caminho(rotulo, vai_para, porque, *, rotulo_curto="") -> dict:
    if not porque.strip():
        raise ValueError(f"caminho {rotulo!r} sem justificativa")
    return {"r": texto(rotulo), "vai": vai_para, "c": texto(porque),
            "rc": texto(rotulo_curto)}


def bifurcacao(ident, kicker, titulo, enunciado, caminhos, *, fundo="",
               nota="") -> dict:
    if not 2 <= len(caminhos) <= 3:
        raise ValueError(f"bifurcação {ident!r}: use 2 ou 3 caminhos")
    return _pag("bifurcacao", ident, kicker=texto(kicker), tt=texto(titulo),
                enunciado=texto(enunciado), caminhos=caminhos, fundo=fundo,
                nota=texto(nota))


def desfecho(ident, titulo, *blocos, qualidade, porque, fundo="",
             kicker="Desfecho", fecho="") -> dict:
    """`fecho` é a página para onde o caso vai depois do desfecho.

    Os passos que o documento de referência chama de INCERTEZA e RETROSPECTIVA
    — o que ficou sem explicação, e onde dava para ter chegado antes — são os
    dois que quase toda imitação esquece, e são justamente os que transformam o
    material em ensino de raciocínio. Eles vêm depois do desfecho, iguais para
    os três ramos, porque a lição não muda com a escolha."""
    if qualidade not in ("melhor", "medio", "pior"):
        raise ValueError("qualidade: 'melhor', 'medio' ou 'pior'")
    if not porque.strip():
        raise ValueError(f"desfecho {ident!r} sem explicação fisiológica")
    return _pag("desfecho", ident, kicker=texto(kicker), tt=texto(titulo),
                corpo="".join(blocos), q=qualidade, porque=texto(porque),
                fundo=fundo, fecho=fecho)


# ─────────────────────────── montagem ───────────────────────────


def montar(caso) -> str:
    raiz = Path(__file__).parent
    css = (raiz / "etapas.css").read_text(encoding="utf-8")
    js = (raiz / "etapas.js").read_text(encoding="utf-8")

    cache: dict[str, str] = {}

    def embutir(nome: str) -> str:
        if nome not in cache:
            caminho_img = caso.IMG / nome
            if not caminho_img.exists():
                raise FileNotFoundError(f"imagem não encontrada: {caminho_img}")
            tipo = mimetypes.guess_type(nome)[0] or "image/jpeg"
            cache[nome] = ("data:" + tipo + ";base64,"
                           + base64.b64encode(caminho_img.read_bytes()).decode())
        return cache[nome]

    def resolver(v):
        """Anota que a imagem é usada, mas deixa o NOME no lugar do arquivo.

        Inlinear o data: URI aqui custava caro: a cena de admissão é o fundo de
        quase todas as etapas, e cada ocorrência carregava uma cópia inteira do
        base64 — o mesmo quarto de megabyte, vinte vezes. O arquivo saía com
        8 MB de imagem repetida. Agora cada imagem viaja uma vez, numa tabela,
        e a etapa guarda só a chave.
        """
        if isinstance(v, dict):
            for k, x in v.items():
                if k in ("fundo", "img") and x:
                    embutir(x)
            return {k: (x if k in ("fundo", "img") and x else resolver(x))
                    for k, x in v.items()}
        if isinstance(v, list):
            return [resolver(x) for x in v]
        return v

    dados = {
        "caso": {"titulo": caso.TITULO, "rodape": caso.RODAPE,
                 "sistemas": SISTEMAS},
        "etapas": resolver(caso.ETAPAS),
        "banco": {e["n"]: e for e in caso.BANCO},
        "revisao": [dict(r, rotulo=texto(r["rotulo"]), porque=texto(r["porque"]))
                    for r in getattr(caso, "REVISAO", [])],
    }
    dados["imgs"] = cache          # cada imagem uma vez só, no fim

    return (
        '<!doctype html>\n<html lang="pt-BR">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width,initial-scale=1">\n'
        f"<title>{caso.TITULO}</title>\n<style>\n{css}\n</style>\n</head>\n"
        '<body>\n<div id="trilho"></div>\n<div id="palco"></div>\n'
        '<div id="pe"></div>\n'
        '<script type="application/json" id="dados">'
        + json.dumps(dados, ensure_ascii=False).replace("</", "<\\/")
        + f"</script>\n<script>\n{js}\n</script>\n</body>\n</html>\n"
    )

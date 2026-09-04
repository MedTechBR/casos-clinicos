"""Montagem do arquivo final.

Um `.html` autossuficiente: CSS, JS, conteúdo, banco e imagens em base64 dentro
do próprio arquivo. Roda em `file://`, sem servidor e sem internet.
"""

from __future__ import annotations

import base64
import json
import mimetypes
import re
from pathlib import Path

from .imagens import dimensoes

MOTOR = Path(__file__).parent


def _b64(caminho: Path) -> str:
    tipo = mimetypes.guess_type(caminho.name)[0] or "image/jpeg"
    return f"data:{tipo};base64," + base64.b64encode(caminho.read_bytes()).decode()


def _grid_rotulo(s: dict) -> str:
    if "grid" in s:
        return s["grid"]
    if s["tipo"] == "capa":
        return "Capa"
    if s["tipo"] == "discussao":
        return f"D — {s['titulo']}"
    k = s.get("kicker") or ""
    if k.lower().startswith("o caso"):
        return f"CASO · {s['titulo'].lower()}"
    return s["titulo"]


def _corta(t: str, n: int = 46) -> str:
    """Corta na palavra, não no meio dela."""
    t = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", t)).strip()
    if len(t) <= n:
        return t
    corte = t[:n].rsplit(" ", 1)[0]
    return (corte or t[:n]).rstrip(" ,;:.") + "…"


def montar(*, titulo, slug, rodape, slides, banco, img_dir: Path, css=None, js=None) -> str:
    slides = [s for grupo in slides for s in (grupo if isinstance(grupo, list) else [grupo])]
    total = len(slides)

    ids = [s["id"] for s in slides]
    dup = {x for x in ids if ids.count(x) > 1}
    if dup:
        raise ValueError(f"identificadores de slide repetidos: {sorted(dup)}")

    css = css or (MOTOR / "estilo.css").read_text()
    js = js or (MOTOR / "runtime.js").read_text()

    secoes = []
    for n, s in enumerate(slides, 1):
        cls = " ".join(["slide", *s["classes"]]).rstrip()
        pe = (
            f'<div class="foot"><span>{rodape}</span>'
            f'<span>{n} / {total}</span></div>'
        )
        secoes.append(
            f'<section class="{cls}" id="s-{s["id"]}" data-n="{n}">{s["corpo"]}{pe}</section>'
        )
    corpo = "".join(secoes)

    # imagens: um data: URI por arquivo, reaproveitado se a mesma imagem repetir
    cache: dict[str, str] = {}

    def troca(m):
        nome = m.group(1)
        if nome not in cache:
            caminho = img_dir / nome
            if not caminho.exists():
                raise FileNotFoundError(f"imagem não encontrada: {caminho}")
            cache[nome] = _b64(caminho)
        return cache[nome]

    corpo = re.sub(r"@@IMG:([^@]+)@@", troca, corpo)

    # Anotação: as marcas são escritas em porcentagem da imagem e viram
    # coordenada real aqui, onde o build conhece o arquivo. O viewBox é o da
    # própria imagem, para a sobreposição casar com o object-fit: contain.
    dim: dict[str, tuple[int, int]] = {}

    def _dim(nome):
        if nome not in dim:
            dim[nome] = dimensoes(img_dir / nome)
        return dim[nome]

    def anotar(secao: str) -> str:
        def uma(m):
            nome = m.group(1)
            w, h = _dim(nome)
            return f"0 0 {w} {h}"

        secao = re.sub(r"@@VIEWBOX:([^@]+)@@", uma, secao)
        for fig in re.findall(r'<figure class="an"[^>]*data-img="([^"]+)"', secao):
            w, h = _dim(fig)
            menor = min(w, h)
            i = secao.index(f'data-img="{fig}"')
            j = secao.index("</figure>", i)
            trecho = secao[i:j]
            trecho = re.sub(r"@@X:([-\d.]+)@@", lambda m: f"{float(m.group(1)) / 100 * w:.1f}", trecho)
            trecho = re.sub(r"@@Y:([-\d.]+)@@", lambda m: f"{float(m.group(1)) / 100 * h:.1f}", trecho)
            trecho = re.sub(r"@@R:([-\d.]+)@@", lambda m: f"{float(m.group(1)) / 100 * menor:.1f}", trecho)
            trecho = re.sub(r"@@W:([-\d.]+)@@", lambda m: f"{float(m.group(1)) / 100 * menor:.2f}", trecho)
            trecho = re.sub(r"@@F:([-\d.]+)@@", lambda m: f"{float(m.group(1)) / 100 * menor:.1f}", trecho)
            secao = secao[:i] + trecho + secao[j:]
        return secao

    corpo = anotar(corpo)
    sobrou = re.findall(r"@@[A-Z]+:[^@]+@@", corpo)
    if sobrou:
        raise ValueError(f"marcador não resolvido no build: {sorted(set(sobrou))[:3]}")

    miniaturas = "".join(
        f'<div class="t" data-n="{n}"><span class="n">{n:02d}</span>'
        f"<b>{_corta(_grid_rotulo(s))}</b></div>"
        for n, s in enumerate(slides, 1)
    )

    ajuda = (
        "&larr; &rarr; revelar e navegar &nbsp;·&nbsp; X pedir exame &nbsp;·&nbsp; "
        "E editar &nbsp;·&nbsp; O visão geral &nbsp;·&nbsp; F tela cheia"
    )
    barra_edicao = (
        '<div id="edt"><b>Modo de edição</b><span>clique em qualquer texto do slide e '
        'digite por cima</span><span class="sp"></span><span class="msg"></span>'
        '<button class="sv">Salvar HTML &nbsp;(Ctrl+S)</button>'
        '<button class="fc">Sair &nbsp;(E)</button></div>'
    )
    gaveta = (
        '<button id="gavb">Pedir exame &nbsp;·&nbsp; X</button>'
        '<div id="gav"><div class="gh"><div class="gt">Pedir exame</div>'
        '<div class="gsub">A turma sugere, você digita — um exame por vez. '
        'Valores em <b>vermelho</b> estão fora da referência.</div>'
        '<input id="q" type="text" autocomplete="off" spellcheck="false" '
        'placeholder="creatinina, sódio, ferritina, líquor…"></div>'
        '<div class="gb" id="gb" data-runtime></div></div>'
    )

    return (
        "<!DOCTYPE html><html lang='pt-BR'><head><meta charset='utf-8'>"
        "<meta name='viewport' content='width=device-width,initial-scale=1'>"
        f"<title>{titulo}</title><style>\n{css}</style></head><body>"
        f"{barra_edicao}"
        f'<div id="wrap"><div id="stage" data-runtime="attr">{corpo}'
        f'<div class="bar" id="bar" data-runtime="attr"></div>'
        f'<div id="etapas" data-runtime></div></div></div>'
        f'<div id="grid"><div class="g">{miniaturas}</div></div>'
        f"{gaveta}"
        f'<div id="help">{ajuda}</div>'
        f"<script type=\"application/json\" id=\"banco\" data-slug=\"{slug}\">"
        f"{json.dumps(banco, ensure_ascii=False).replace(chr(60) + chr(47), chr(60) + chr(92) + chr(47))}</script>"
        f"<script>\n{js}</script></body></html>"
    )


def build(caso, destino: Path) -> Path:
    html = montar(
        titulo=caso.TITULO,
        slug=caso.SLUG,
        rodape=caso.RODAPE,
        slides=caso.SLIDES,
        banco=caso.BANCO,
        img_dir=caso.IMG,
    )
    destino.parent.mkdir(parents=True, exist_ok=True)
    destino.write_text(html, encoding="utf-8")
    return destino

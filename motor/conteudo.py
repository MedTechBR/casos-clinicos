"""Helpers de conteúdo.

Cada helper devolve um fragmento de HTML. A regra é: o autor escreve prosa e
estrutura clínica, nunca marcação. Se um caso precisar de uma tag que não existe
aqui, o helper que falta se acrescenta aqui — não se escreve HTML no caso.
"""

from __future__ import annotations

import html as _html
import re

# ─────────────────────────── texto ───────────────────────────

_ENFASE = re.compile(r"\*\*(.+?)\*\*")
_MARCA = re.compile(r"==(.+?)==")
_DISCRETO = re.compile(r"\{\{(.+?)\}\}")
_DIA = re.compile(r"\[\[(.+?)\]\]")
_ITALICO = re.compile(r"//(?!/)(.+?)//")


def texto(t: str) -> str:
    """Converte a marcação mínima permitida na prosa e normaliza espaços.

    Quatro marcadores, e só eles:

        **assim**   negrito — use pouco, só onde o olho precisa parar
        ==assim==   marca-texto
        {{assim}}   discreto, para o valor anterior entre parênteses
        [[assim]]   etiqueta temporal dentro da prosa
        //assim//   itálico — só nome científico e título de periódico

    Itálico, listas e títulos em markdown não são reconhecidos de propósito,
    para que `verificar.py` possa acusar markdown cru como erro em vez de
    renderizá-lo silenciosamente.
    """
    t = re.sub(r"\s+", " ", t).strip()
    t = _ENFASE.sub(r"<b>\1</b>", t)
    t = _MARCA.sub(r"<mark>\1</mark>", t)
    t = _DISCRETO.sub(r'<span class="mut">\1</span>', t)
    t = _DIA.sub(r'<span class="day">\1</span>', t)
    t = _ITALICO.sub(r"<i>\1</i>", t)
    return t


def p(*partes: str, classe: str = "") -> str:
    c = f' class="{classe}"' if classe else ""
    return f"<p{c}>{texto(' '.join(partes))}</p>"


def lead(*partes: str) -> str:
    """Primeiro parágrafo de um bloco narrativo, com capitular."""
    return p(*partes, classe="lead")


def h3(t: str) -> str:
    return f"<h3>{texto(t)}</h3>"


def mut(t: str) -> str:
    return f'<span class="mut">{texto(t)}</span>'


def dia(t: str) -> str:
    """Etiqueta temporal dentro da prosa: 'Dia 5', 'Admissão'."""
    return f'<span class="day">{texto(t)}</span>'


def lista(itens, ordenada: bool = False) -> str:
    tag = "ol" if ordenada else "ul"
    li = "".join(f"<li>{texto(i)}</li>" for i in itens)
    return f"<{tag}>{li}</{tag}>"


def bruto(h: str) -> str:
    """Escape hatch. Toda ocorrência é uma dívida: ou vira helper, ou some."""
    return h


# ─────────────────────────── revelação ───────────────────────────


def passo(*blocos: str) -> str:
    """Um passo da revelação em ordem: aparece com → ou clique à direita."""
    return f'<div class="pv">{"".join(blocos)}</div>'


def revelar(rotulo: str, *blocos: str) -> str:
    """Bloco velado atrás de um rótulo clicável — o laudo, o resultado."""
    return (
        '<div class="rv">'
        f'<div class="rv-ph"><span class="rv-ic">+</span>'
        f'<span class="rv-lb">{texto(rotulo)}</span></div>'
        f'<div class="rv-in">{"".join(blocos)}</div>'
        "</div>"
    )


# ─────────────────────────── caixas ───────────────────────────

_TIPOS = {"neutro": "grey", "pausa": "pause", "erro": "err", "regra": "rule", "alerta": "red"}


def box(titulo: str, *blocos: str, tipo: str = "neutro") -> str:
    if tipo not in _TIPOS:
        raise ValueError(f"tipo de caixa desconhecido: {tipo!r}; use {sorted(_TIPOS)}")
    return (
        f'<div class="box {_TIPOS[tipo]}"><b class="bt">{texto(titulo)}</b>'
        f'{"".join(blocos)}</div>'
    )


def nota(titulo: str, *blocos: str) -> str:
    """Nota do apresentador: invisível na tela, impressa no PDF."""
    return f'<div class="pnote"><b class="bt">{texto(titulo)}</b>{"".join(blocos)}</div>'


def aliquotas(*blocos: str) -> str:
    return f'<div class="box aliq"><b class="bt">Alíquotas</b>{"".join(blocos)}</div>'


# ─────────────────────────── layout ───────────────────────────


def cols(*colunas) -> str:
    """Duas ou três colunas. Cada coluna é uma lista de blocos."""
    saida = []
    for c in colunas:
        blocos = c if isinstance(c, (list, tuple)) else [c]
        saida.append(f'<div>{"".join(blocos)}</div>')
    return f'<div class="cols">{"".join(saida)}</div>'


def cap(t: str) -> str:
    """Rótulo pequeno acima de uma tabela ou painel."""
    return f'<div class="cap">{texto(t)}</div>'


# ─────────────────────────── tabelas ───────────────────────────


def tabela(cabecalho, linhas, tamanho: str = "") -> str:
    """Tabela comum. `tamanho` aceita '', 'sm' ou 'xs'."""
    if tamanho not in ("", "sm", "xs"):
        raise ValueError("tamanho de tabela deve ser '', 'sm' ou 'xs'")
    c = f' class="{tamanho}"' if tamanho else ""
    th = "".join(f"<th>{texto(x)}</th>" for x in cabecalho)
    tr = "".join(
        "<tr>" + "".join(f"<td>{texto(x)}</td>" for x in linha) + "</tr>" for linha in linhas
    )
    return f"<table{c}><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table>"


def exame(nome: str, valor: str, referencia: str = "—", estado: str = "normal") -> dict:
    """Uma linha de painel laboratorial.

    `estado` é 'normal', 'alterado' (âmbar) ou 'critico' (vermelho). É o único
    julgamento que o sistema faz, e é o mesmo que qualquer laboratório imprime:
    dentro ou fora da referência. Interpretação é do grupo.
    """
    if estado not in ("normal", "alterado", "critico"):
        raise ValueError(f"estado inválido: {estado!r}")
    return {"n": nome, "v": valor, "r": referencia, "e": estado}


def painel(linhas, velado: bool = True) -> str:
    """Painel laboratorial. Velado, os valores aparecem linha a linha ao clique."""
    cls = {"normal": "", "alterado": "alt", "critico": "crit"}
    tr = []
    for L in linhas:
        classes = [c for c in (cls[L["e"]], "hid" if velado else "") if c]
        cl = f' class="{" ".join(classes)}"' if classes else ""
        tr.append(
            f'<tr{cl}><td>{texto(L["n"])}</td>'
            f'<td class="v"><span class="dots">— — —</span>'
            f'<span class="vv">{texto(L["v"])}</span></td>'
            f'<td class="r">{texto(L["r"])}</td></tr>'
        )
    oc = " oc" if velado else ""
    return (
        f'<table class="lab{oc}"><thead><tr><th>Exame</th><th>Resultado</th>'
        f'<th>Referência</th></tr></thead><tbody>{"".join(tr)}</tbody></table>'
    )


def sinais(*itens: str) -> str:
    """Sinais vitais em pílulas. Use com parcimônia: a regra editorial é narrá-los."""
    return '<div class="vitals">' + "".join(f"<span>{texto(i)}</span>" for i in itens) + "</div>"


# ─────────────────────────── figuras ───────────────────────────


def figura(arquivo: str, legenda: str, credito: str, altura: int = 330) -> str:
    """Figura simples. `arquivo` é o nome dentro de img/; o build embute em base64."""
    return (
        f'<figure style="--fh:{altura}px" data-img="{_html.escape(arquivo, quote=True)}">'
        f"<img alt=\"\" src=\"@@IMG:{arquivo}@@\"/>"
        f"<figcaption>{texto(legenda)}"
        f'<span class="cred">{texto(credito)}</span></figcaption></figure>'
    )


def seta(x1: float, y1: float, x2: float, y2: float, rotulo: str = "") -> dict:
    """Uma seta da anotação, em coordenadas de 0 a 100 sobre a imagem."""
    return {"tipo": "seta", "x1": x1, "y1": y1, "x2": x2, "y2": y2, "rotulo": rotulo}


def circulo(x: float, y: float, r: float, rotulo: str = "") -> dict:
    return {"tipo": "circulo", "x": x, "y": y, "r": r, "rotulo": rotulo}


def figura_anotada(
    arquivo: str,
    legenda: str,
    credito: str,
    marcas,
    altura: int = 330,
    legenda_anotada: str = "",
) -> str:
    """Figura com sobreposição SVG revelada ao clique.

    As marcas são declaradas em coordenadas relativas (0 a 100) para que a
    anotação continue certa qualquer que seja a altura de renderização.
    `ferramentas/tirar.py --anotadas` renderiza a figura com a sobreposição
    aberta, que é a única forma de conferir se a seta bate com o achado.
    """
    partes = []
    for m in marcas:
        if m["tipo"] == "seta":
            partes.append(
                f'<line x1="{m["x1"]}" y1="{m["y1"]}" x2="{m["x2"]}" y2="{m["y2"]}" '
                'stroke="#ffd166" stroke-width="1.1" marker-end="url(#pta)"/>'
            )
            if m["rotulo"]:
                partes.append(
                    f'<text x="{m["x1"]}" y="{m["y1"] - 1.6}" fill="#ffd166" '
                    'font-size="3.2" font-weight="700" text-anchor="middle">'
                    f'{texto(m["rotulo"])}</text>'
                )
        elif m["tipo"] == "circulo":
            partes.append(
                f'<circle cx="{m["x"]}" cy="{m["y"]}" r="{m["r"]}" fill="none" '
                'stroke="#ffd166" stroke-width="1.1"/>'
            )
            if m["rotulo"]:
                partes.append(
                    f'<text x="{m["x"]}" y="{m["y"] - m["r"] - 1.4}" fill="#ffd166" '
                    'font-size="3.2" font-weight="700" text-anchor="middle">'
                    f'{texto(m["rotulo"])}</text>'
                )
    defs = (
        '<defs><marker id="pta" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="5" '
        'markerHeight="5" orient="auto-start-reverse">'
        '<path d="M0 0 L10 5 L0 10 z" fill="#ffd166"/></marker></defs>'
    )
    capin = f'<span class="capin"> {texto(legenda_anotada)}</span>' if legenda_anotada else ""
    return (
        f'<figure class="an" style="--fh:{altura}px" '
        f'data-img="{_html.escape(arquivo, quote=True)}"><div class="ib">'
        f"<img alt=\"\" src=\"@@IMG:{arquivo}@@\"/>"
        f'<svg class="ov rvov" viewBox="0 0 100 100" preserveAspectRatio="none">'
        f'{defs}{"".join(partes)}</svg></div>'
        f"<figcaption>{texto(legenda)}{capin}"
        f'<span class="cred">{texto(credito)}</span></figcaption></figure>'
    )

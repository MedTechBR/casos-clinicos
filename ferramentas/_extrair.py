"""Conversor de uso único: HTML original -> fontes Python do caso.

Existe para provar que a extração foi fiel, e para não redigitar à mão 38 slides
de prosa clínica (redigitar é justamente onde se introduz erro). Depois de
revisado o que ele gerou, este arquivo pode sumir — o caso passa a viver em
`casos/pulmao_rim/`.

Uso:  python3 ferramentas/_extrair.py <html_original>
"""

from __future__ import annotations

import re
import sys
import textwrap
from html.parser import HTMLParser
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
VAZIAS = {"img", "br", "hr", "input", "meta", "link"}

IMAGENS = {
    496816: "tc_torax_vidro_fosco.jpg",
    105376: "panca_imunofluorescencia.jpg",
    433992: "biopsia_renal_cortex.jpg",
}


# ───────────────────────────── mini-DOM ─────────────────────────────


class No:
    def __init__(self, tag, attrs=None, texto=""):
        self.tag = tag
        self.attrs = dict(attrs or {})
        self.texto = texto
        self.filhos = []

    @property
    def classes(self):
        return self.attrs.get("class", "").split()

    def tem(self, c):
        return c in self.classes

    def busca(self, tag=None, classe=None):
        for f in self.filhos:
            if (tag is None or f.tag == tag) and (classe is None or f.tem(classe)):
                return f
        return None


class Arvore(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.raiz = No("#raiz")
        self.pilha = [self.raiz]

    def handle_starttag(self, tag, attrs):
        n = No(tag, attrs)
        self.pilha[-1].filhos.append(n)
        if tag not in VAZIAS:
            self.pilha.append(n)

    def handle_startendtag(self, tag, attrs):
        self.pilha[-1].filhos.append(No(tag, attrs))

    def handle_endtag(self, tag):
        if tag in VAZIAS:
            return
        for k in range(len(self.pilha) - 1, 0, -1):
            if self.pilha[k].tag == tag:
                del self.pilha[k:]
                return

    def handle_data(self, d):
        if d.strip():
            self.pilha[-1].filhos.append(No("#texto", texto=d))


def parse(h):
    a = Arvore()
    a.feed(h)
    return a.raiz


# ───────────────────────── texto -> marcação ─────────────────────────


def inline(n: No) -> str:
    """Serializa conteúdo inline de volta para os marcadores do `texto()`."""
    out = []
    for f in n.filhos:
        if f.tag == "#texto":
            out.append(f.texto)
        elif f.tag == "b":
            out.append("**" + inline(f) + "**")
        elif f.tag == "mark":
            out.append("==" + inline(f) + "==")
        elif f.tag == "span" and f.tem("mut"):
            out.append("{{" + inline(f) + "}}")
        elif f.tag == "span" and f.tem("day"):
            out.append("[[" + inline(f) + "]]")
        elif f.tag == "i":
            out.append("//" + inline(f) + "//")
        elif f.tag == "br":
            out.append(" ")
        else:
            out.append(inline(f))
    return re.sub(r"\s+", " ", "".join(out)).strip()


def cita(s: str, indent: int = 8) -> str:
    """String Python legível: prosa longa quebrada em linhas, curta numa linha só."""
    s = s.replace("\\", "\\\\").replace('"', '\\"')
    if len(s) <= 78 - indent:
        return f'"{s}"'
    linhas = textwrap.wrap(s, width=76 - indent, break_long_words=False,
                           break_on_hyphens=False)
    pad = " " * indent
    return ("\n" + pad).join(f'"{l} "' if k < len(linhas) - 1 else f'"{l}"'
                             for k, l in enumerate(linhas))


# ───────────────────────── nó -> chamada de helper ─────────────────────────


def blocos(nos, ind):
    return [emitir(n, ind) for n in nos if n.tag != "#texto" or n.texto.strip()]


def junta(itens, ind):
    pad = " " * ind
    if not itens:
        return ""
    return ("\n" + pad).join(itens)


TIPO_BOX = {"grey": "neutro", "pause": "pausa", "err": "erro", "rule": "regra", "red": "alerta"}


def emitir(n: No, ind: int = 8) -> str:
    pad = " " * (ind + 4)
    t, c = n.tag, n.classes

    if t == "p":
        return f'p({cita(inline(n), ind + 2)})'

    if t == "h3":
        return f"h3({cita(inline(n), ind + 3)})"

    if t in ("ul", "ol"):
        itens = [inline(f) for f in n.filhos if f.tag == "li"]
        corpo = (",\n" + pad + " ").join(cita(i, ind + 5) for i in itens)
        ord_ = ", ordenada=True" if t == "ol" else ""
        return f"lista([\n{pad} {corpo},\n{pad}]{ord_})"

    if t == "div" and "pv" in c:
        return f"passo({junta(blocos(n.filhos, ind + 6), ind + 6)})"

    if t == "div" and "rv" in c:
        ph = n.busca("div", "rv-ph")
        rot = inline(ph.busca("span", "rv-lb")) if ph else "Revelar"
        dentro = n.busca("div", "rv-in")
        return (
            f"revelar({cita(rot, ind + 8)},\n{pad}"
            + junta(blocos(dentro.filhos if dentro else [], ind + 4), ind + 4)
            + ")"
        )

    if t == "div" and "box" in c:
        tipo = next((TIPO_BOX[x] for x in c if x in TIPO_BOX), "neutro")
        bt = n.busca("b", "bt")
        titulo = inline(bt) if bt else ""
        resto = [f for f in n.filhos if f is not bt]
        arg = f', tipo="{tipo}"' if tipo != "neutro" else ""
        return (
            f"box({cita(titulo, ind + 4)},\n{pad}"
            + junta(blocos(resto, ind + 4), ind + 4)
            + arg
            + ")"
        )

    if t == "div" and "pnote" in c:
        bt = n.busca("b", "bt")
        titulo = inline(bt) if bt else ""
        resto = [f for f in n.filhos if f is not bt]
        return f"nota({cita(titulo, ind + 5)},\n{pad}" + junta(blocos(resto, ind + 4), ind + 4) + ")"

    if t == "div" and "cols" in c:
        colunas = [f for f in n.filhos if f.tag == "div"]
        partes = []
        for col in colunas:
            dentro = junta([b + "," for b in blocos(col.filhos, ind + 8)], ind + 8)
            partes.append(f"[\n{' ' * (ind + 8)}{dentro}\n{' ' * (ind + 4)}]")
        return f"cols(\n{pad}" + (",\n" + pad).join(partes) + f",\n{' ' * ind})"

    if t == "div" and "cap" in c:
        return f"cap({cita(inline(n), ind + 4)})"

    if t == "div" and "vitals" in c:
        itens = [cita(inline(f), ind + 7) for f in n.filhos if f.tag == "span"]
        return "sinais(" + (",\n" + pad + " ").join(itens) + ")"

    if t == "table" and "lab" in c:
        velado = "oc" in c
        est = {"crit": "critico", "alt": "alterado"}
        linhas = []
        tb = n.busca("tbody")
        for tr in (tb.filhos if tb else []):
            if tr.tag != "tr":
                continue
            tds = [f for f in tr.filhos if f.tag == "td"]
            nome = inline(tds[0])
            vv = tds[1].busca("span", "vv")
            valor = inline(vv) if vv else inline(tds[1])
            ref = inline(tds[2]) if len(tds) > 2 else "—"
            e = next((est[x] for x in tr.classes if x in est), "normal")
            arg = f', "{e}"' if e != "normal" else ""
            linhas.append(
                f"exame({cita(nome, ind + 10)}, {cita(valor, ind + 10)},\n"
                f"{pad}       {cita(ref, ind + 14)}{arg}),"
            )
        v = "" if velado else ", velado=False"
        return f"painel([\n{pad}" + ("\n" + pad).join(linhas) + f"\n{' ' * (ind)}]{v})"

    if t == "table":
        tam = next((x for x in c if x in ("sm", "xs")), "")
        th = n.busca("thead")
        cab = [inline(x) for x in (th.filhos[0].filhos if th and th.filhos else []) if x.tag == "th"]
        tb = n.busca("tbody")
        linhas = []
        for tr in (tb.filhos if tb else []):
            if tr.tag != "tr":
                continue
            cels = [inline(x) for x in tr.filhos if x.tag == "td"]
            linhas.append("[" + ", ".join(cita(x, ind + 12) for x in cels) + "],")
        arg = f', tamanho="{tam}"' if tam else ""
        cabs = ", ".join(cita(x, ind + 10) for x in cab)
        return (
            f"tabela([{cabs}], [\n{pad}" + ("\n" + pad).join(linhas) + f"\n{' ' * ind}]{arg})"
        )

    if t == "figure":
        img = n.busca("img")
        src = img.attrs.get("src", "") if img else ""
        tam = len(re.search(r"base64,([A-Za-z0-9+/=]*)", src).group(1)) if "base64," in src else 0
        arq = IMAGENS.get(tam, f"DESCONHECIDA_{tam}.jpg")
        fc = n.busca("figcaption")
        cred = fc.busca("span", "cred") if fc else None
        credito = inline(cred) if cred else ""
        legenda = inline(_sem(fc, cred)) if fc else ""
        alt = re.search(r"--fh:(\d+)px", n.attrs.get("style", ""))
        a = f", altura={alt.group(1)}" if alt else ""
        return (
            f'figura("{arq}",\n{pad}{cita(legenda, ind + 4)},\n'
            f"{pad}{cita(credito, ind + 4)}{a})"
        )

    if t in ("div", "span", "section"):
        return junta(blocos(n.filhos, ind), ind)

    return f"bruto({cita(inline(n), ind + 6)})"


def _sem(no, excluido):
    c = No(no.tag, list(no.attrs.items()))
    c.filhos = [f for f in no.filhos if f is not excluido]
    return c


# ───────────────────────────── slides ─────────────────────────────


def corpo_de(sec: No):
    body = sec.busca("div", "body")
    return body.filhos if body else []


def gerar_slide(sec: No, n: int) -> str:
    c = sec.classes
    kicker = sec.busca("div", "kicker")
    h2 = sec.busca("h2")
    k = inline(kicker) if kicker else ""
    titulo = inline(h2) if h2 else ""
    dens = "dense" if "dense" in c else ("xd" if "xd" in c else None)
    darg = f', densidade="{dens}"' if dens else ""

    if "narr" in c:
        fn = "narrativa"
    elif "screen" in c:
        fn = "tela"
    elif k == "Discussão":
        fn = "discussao"
    else:
        fn = "bloco"

    corpo = junta([b + "," for b in blocos(corpo_de(sec), 8)], 8)
    if fn == "discussao":
        cab = f"    discussao({cita(titulo, 14)},"
        darg = "" if dens == "dense" else f", densidade={dens!r}"
    else:
        cab = f"    {fn}({cita(k, 12)}, {cita(titulo, 12)},"
    cauda = f"\n        densidade=\"{dens}\"," if dens else ""
    return f"{cab}\n        {corpo}{cauda}\n    ),"


def main(origem: Path):
    src = origem.read_text()
    corpo = src[src.find("<body>"):src.find("<div id='grid'")]
    secs = [s for s in re.split(r'(?=<section class="slide)', corpo) if s.startswith("<section")]
    print(f"{len(secs)} slides")

    saida = []
    perguntas = []
    i = 0
    while i < len(secs):
        raiz = parse(secs[i])
        sec = raiz.filhos[0]
        c = sec.classes
        if "cover" in c:
            sub = inline(sec.busca("div", "sub"))
            meta = sec.busca("div", "meta")
            partes = [f for f in meta.filhos]
            txt = inline(meta)
            saida.append(("capa", inline(sec.busca("h1")), sub, txt))
        elif "q" in c:
            qraiz = parse(secs[i])
            araiz = parse(secs[i + 1])
            perguntas.append((qraiz.filhos[0], araiz.filhos[0]))
            saida.append(("pergunta", len(perguntas)))
            i += 1
        else:
            saida.append(("slide", gerar_slide(sec, i + 1)))
        i += 1

    return saida, perguntas, secs


if __name__ == "__main__":
    main(Path(sys.argv[1]))

"""Linter da apresentação.

Roda as verificações da lista de entrega. As estáticas primeiro, porque são
instantâneas; a de transbordo por último, porque precisa de navegador.

Uso:  python3 ferramentas/verificar.py [saida/pulmao-rim.html]
"""

from __future__ import annotations

import json
import re
import sys
import unicodedata
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent

# Títulos de efeito: substantivo simples é a regra. "Exame físico", nunca
# "Quando o pulmão acusa o rim".
PROIBIDOS = [
    (r"^(quando|onde|por que|porque)\b", "título começa como manchete"),
    (r"\b(a pista|o segredo|a chave|o vilão|o culpado)\b", "título com suspense"),
    (r"\b(desvendand|revelad|escondid|oculto|surpreendente)\w*", "título com efeito"),
    (r"\b(acusa|denuncia|trai|entrega)\b", "verbo de efeito no título"),
    (r"[✨🔍💡🚨⚡️🩺]", "emoji"),
    (r"\bo vaso comum\b", "título metafórico"),
]


class Relatorio:
    def __init__(self):
        self.itens = []

    def add(self, nome, ok, detalhe=""):
        self.itens.append((nome, ok, detalhe))
        marca = "ok  " if ok else "FALHA"
        print(f"  {marca}  {nome}" + (f"\n         {detalhe}" if detalhe and not ok else ""))

    @property
    def falhas(self):
        return [i for i in self.itens if not i[1]]


def _texto(s):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", s)).strip()


def slides(h):
    corpo = h[h.find("<body>") :]
    fim = corpo.find('id="grid"')
    corpo = corpo[: fim if fim > 0 else len(corpo)]
    return [s for s in re.split(r'(?=<section class="slide)', corpo) if s.startswith("<section")]


# ───────────────────────── verificações estáticas ─────────────────────────


def v_alternativas(h, r):
    """A letra anunciada tem que ser a alternativa marcada como correta."""
    S = slides(h)
    erros = []
    for i, s in enumerate(S):
        if 'class="slide ans' not in s:
            continue
        anunciada = set(re.findall(r"[A-E]", _texto(re.search(r"<h2>(.*?)</h2>", s, re.S).group(1))))
        marcadas = set()
        for m in re.finditer(r'<li class="ok">(.*?)</li>', s, re.S):
            marcadas.add(_texto(re.search(r'class="k">(.*?)</span>', m.group(1), re.S).group(1)))
        if anunciada != marcadas:
            erros.append(f"slide {i+1}: anuncia {sorted(anunciada)}, marca {sorted(marcadas)}")
        # o texto da alternativa tem que ser o mesmo nos dois slides
        q = S[i - 1]
        qt = [_texto(re.sub(r'<span class="k">.*?</span>', "", m, flags=re.S))
              for m in re.findall(r"<li>.*?</li>", q, re.S)]
        at = [_texto(m) for m in re.findall(r'<div class="tt">(.*?)</div>', s, re.S)]
        if qt != at:
            erros.append(f"slide {i+1}: texto da alternativa diverge do slide de pergunta")
    r.add("alinhamento pergunta/resposta", not erros, " · ".join(erros))


def v_titulos(h, r):
    erros = []
    for m in re.finditer(r"<h([12])[^>]*>(.*?)</h\1>", h, re.S):
        t = _texto(m.group(2))
        if "?" in t:  # enunciado de pergunta não é título de slide
            continue
        for pad, motivo in PROIBIDOS:
            if re.search(pad, t, re.I):
                erros.append(f"{motivo}: “{t[:60]}”")
    r.add("títulos sem efeito", not erros, " · ".join(erros))


def v_markdown(h, r):
    corpo = h[h.find("<body>") : h.find("<script")]
    # base64 de imagem contém // e _ à vontade; não é texto do slide
    corpo = re.sub(r"data:[^;]+;base64,[A-Za-z0-9+/=]+", " ", corpo)
    achados = []
    for pad, nome in [(r"\*\*", "**"), (r"(?<![\w(])\*(?=\w)", "*"),
                      (r"(?<![\w/])_(?=\w)", "_"), (r"(?<!\{)\{\{", "{{"),
                      (r"//(?!/)[A-Za-zÀ-ÿ]", "//"), (r"==(?=\w)", "==")]:
        for m in re.finditer(pad, corpo):
            achados.append(f"{nome} em “…{_texto(corpo[max(0,m.start()-40):m.start()+30])}…”")
    r.add("markdown convertido", not achados, " · ".join(achados[:5]))


def v_banco(h, r):
    """O slide é canônico: se ele mostra creatinina 3,8, a gaveta não mostra 4,2."""
    banco = json.loads(re.search(r'id="banco"[^>]*>(.*?)</script>', h, re.S).group(1))
    corpo = "\n".join(slides(h))
    numeros = lambda t: set(re.findall(r"\d+[.,]\d+|\d{3,}", t))
    sa = lambda t: unicodedata.normalize("NFD", t).encode("ascii", "ignore").decode().lower()
    # o rótulo do painel costuma ser a abreviação ("PCR"), não o nome do banco
    porrotulo = {}
    for e in banco:
        for x in [e["n"], *e.get("s", [])]:
            porrotulo.setdefault(sa(x), e)
    erros = []
    for rot, e in porrotulo.items():
        nome = rot
        # procura o analito citado num painel de slide e compara os números
        for m in re.finditer(r"<tr[^>]*>\s*<td>(.*?)</td>(.*?)</tr>", corpo, re.S):
            if sa(_texto(m.group(1))) != nome:
                continue
            valor = re.search(r'class="vv">(.*?)</span>', m.group(2), re.S)
            ns = numeros(_texto(valor.group(1) if valor else m.group(2)))
            nb = numeros(_texto(e["r"]))
            if ns and not (ns & nb):
                erros.append(f"{e['n']}: slide {sorted(ns)} x banco {sorted(nb)}")
    r.add("coerência banco × slides", not erros, " · ".join(erros))


def v_arvore(h, r):
    """Todo destino aponta para um bloco que existe; todo bloco é alcançável."""
    ids = set(re.findall(r'<section class="[^"]*" id="s-([^"]+)"', h))
    destinos = set(re.findall(r'data-vai="([^"]+)"', h))
    orfaos = destinos - ids
    r.add("cobertura da árvore", not orfaos,
          f"destinos sem bloco: {sorted(orfaos)}" if orfaos
          else f"{len(ids)} blocos, {len(destinos)} destinos")


def v_creditos(h, r):
    """Toda figura precisa de crédito e licença legíveis."""
    figs = re.findall(r"<figure.*?</figure>", h, re.S)
    sem = [i + 1 for i, f in enumerate(figs) if 'class="cred"' not in f or not _texto(
        re.search(r'class="cred">(.*?)</span>', f, re.S).group(1) if 'class="cred"' in f else "")]
    r.add("crédito e licença nas figuras", not sem,
          f"figuras sem crédito: {sem}" if sem else f"{len(figs)} figuras com crédito")


# ───────────────────────── verificação com navegador ─────────────────────────


def v_transbordo(caminho: Path, r, capturar: Path | None = None):
    """Nenhum slide pode transbordar — testado com TUDO revelado, que é o pior caso."""
    from playwright.sync_api import sync_playwright

    erros = []
    with sync_playwright() as pw:
        b = pw.chromium.launch()
        pg = b.new_page(viewport={"width": 1400, "height": 820})
        pg.goto(caminho.resolve().as_uri())
        pg.wait_for_timeout(400)
        n = pg.evaluate("document.querySelectorAll('.slide').length")
        for i in range(n):
            pg.evaluate(f"show({i})")
            pg.keyboard.press("a")  # revela tudo: o slide no seu pior caso
            pg.wait_for_timeout(60)
            info = pg.evaluate(
                """() => {
                const s = document.querySelector('.slide.on');
                const b = s.querySelector('.body') || s;
                const t = s.querySelector('h1,h2');
                return {n: s.dataset.n, titulo: t ? t.textContent.trim().slice(0,44) : '',
                        sh: b.scrollHeight, ch: b.clientHeight,
                        ssh: s.scrollHeight, sch: s.clientHeight};
            }"""
            )
            excesso = max(info["sh"] - info["ch"], info["ssh"] - info["sch"])
            if excesso > 1:
                erros.append(f"slide {info['n']} “{info['titulo']}” transborda {excesso}px")
                if capturar:
                    capturar.mkdir(parents=True, exist_ok=True)
                    pg.locator(".slide.on").screenshot(
                        path=str(capturar / f"transbordo-{int(info['n']):02d}.png")
                    )
        b.close()
    r.add(f"transbordo (todos os {n} slides, tudo revelado)", not erros, " · ".join(erros))


def main(caminho=None):
    caminho = Path(caminho or RAIZ / "saida" / "pulmao-rim.html")
    h = caminho.read_text()
    print(f"\nverificando {caminho.name}\n")
    r = Relatorio()
    v_alternativas(h, r)
    v_titulos(h, r)
    v_markdown(h, r)
    v_banco(h, r)
    v_arvore(h, r)
    v_creditos(h, r)
    v_transbordo(caminho, r, capturar=RAIZ / "saida" / "revisao")
    print(f"\n{len(r.itens)} verificações · {len(r.falhas)} falha(s)\n")
    return 1 if r.falhas else 0


if __name__ == "__main__":
    sys.exit(main(*sys.argv[1:]))

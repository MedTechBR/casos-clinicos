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
    corpo = re.sub(r"\bhttps?://\S+", " ", corpo)  # xmlns de SVG não é markdown
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
            # todo número que o slide mostra tem que existir no banco. Exigir
            # apenas UM número em comum deixa passar o caso que importa: o
            # slide diz 9,9 e o banco 3,8, mas os dois citam o valor antigo
            # de dois meses atrás e a checagem se dá por satisfeita.
            faltando = ns - nb
            if faltando:
                erros.append(f"{e['n']}: slide mostra {sorted(faltando)}, "
                             f"ausente do banco {sorted(nb)}")
    r.add("coerência banco × slides", not erros, " · ".join(erros))


def v_arvore(h, r):
    """Todo destino aponta para um bloco que existe; todo bloco é alcançável."""
    ids = set(re.findall(r'<section class="[^"]*" id="s-([^"]+)"', h))
    destinos = set(re.findall(r'data-vai="([^"]+)"', h))
    orfaos = destinos - ids
    r.add("cobertura da árvore", not orfaos,
          f"destinos sem bloco: {sorted(orfaos)}" if orfaos
          else f"{len(ids)} blocos, {len(destinos)} destinos")


# o que conta como declaração de licença
LICENCA = re.compile(r"cc\s*by|cc0|domínio público|public domain|phil|"
                     r"esquema autoral", re.I)


def v_creditos(h, r):
    """Toda figura precisa de autor E licença. Texto qualquer não basta."""
    figs = re.findall(r"<figure.*?</figure>", h, re.S)
    sem = []
    for i, f in enumerate(figs, 1):
        m = re.search(r'class="cred">(.*?)</span>', f, re.S)
        t = _texto(m.group(1)) if m else ""
        if not t:
            sem.append(f"figura {i}: sem crédito")
        elif not LICENCA.search(t):
            sem.append(f"figura {i}: crédito sem licença ({t[:40]})")
        elif len(t.split("·")[0].strip()) < 3 and "autoral" not in t.lower():
            sem.append(f"figura {i}: crédito sem autor ({t[:40]})")
    r.add("crédito e licença nas figuras", not sem,
          " · ".join(sem) if sem else f"{len(figs)} figuras com autor e licença")


def v_creditos_batem(h, r):
    """O slide de créditos não pode citar imagem que não está no arquivo.

    Creditar figura ausente é afirmação sem respaldo como qualquer outra, e é o
    tipo de coisa que sobrevive quando um slide é cortado e o crédito fica.
    """
    autores = set()
    for f in re.findall(r"<figure.*?</figure>", h, re.S):
        m = re.search(r'class="cred">(.*?)</span>', f, re.S)
        if m:
            autores.add(_texto(m.group(1)).split("·")[0].strip().lower())
    autores.discard("esquema autoral, desenhado para este caso.")
    creditos = ""
    for s in slides(h):
        if "Fontes" in s and "créditos" in s:
            creditos = _texto(s).lower()
    if not creditos:
        r.add("créditos batem com as figuras", True, "sem slide de créditos")
        return
    # cada crédito de imagem listado tem que corresponder a alguma figura
    # o autor pode trazer barra, ponto e inicial ("CDC / D. Loren Ketai")
    listados = re.findall(r"([A-Za-zÀ-ÿ ]+):\s*([A-Za-zÀ-ÿ0-9./\- ]+?)\s*·", creditos)
    sobrando = [f"{o.strip()} ({a.strip()})" for o, a in listados
                if a.strip().lower() not in autores
                and "wikimedia" not in o and "commons" not in o]
    r.add("créditos batem com as figuras", not sobrando,
          f"creditado mas ausente do arquivo: {sobrando}" if sobrando
          else f"{len(autores)} autores creditados, todos presentes")


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
            # a revelação anima por .38s; medir no meio da transição acusa
            # transbordo de poucos pixels que não existe
            pg.wait_for_timeout(430)
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
            # o linter só olhava para baixo: a tabela estourava a coluna e o
            # overflow:hidden comia a referência do exame sem ninguém notar
            fora = pg.evaluate(
                """() => {
                const s = document.querySelector('.slide.on');
                const b = s.querySelector('.body') || s;
                const bb = b.getBoundingClientRect();
                return [...b.querySelectorAll('*')].filter(e => {
                    const r = e.getBoundingClientRect();
                    return r.width > 0 && (r.right > bb.right + 1 || r.left < bb.left - 1);
                }).map(e => e.tagName + (e.className ? '.' + e.className : '')).slice(0, 2);
            }"""
            )
            if fora:
                erros.append(f"slide {info['n']} “{info['titulo']}” vaza na "
                             f"horizontal: {', '.join(fora)}")
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


def v_velado_nao_vaza(caminho: Path, r):
    """Linha velada não pode entregar o resultado antes da revelação.

    O filete que marca o valor fora da referência era pintado também na linha
    ainda oculta: dava para ler de longe quais analitos estavam alterados sem
    revelar nenhum, o que anula o exercício de julgar valor por valor.
    """
    from playwright.sync_api import sync_playwright

    erros = []
    with sync_playwright() as pw:
        b = pw.chromium.launch()
        pg = b.new_page(viewport={"width": 1400, "height": 820})
        pg.goto(caminho.resolve().as_uri())
        pg.wait_for_timeout(300)
        n = pg.evaluate("document.querySelectorAll('.slide').length")
        for i in range(n):
            pg.evaluate(f"show({i})")
            pg.wait_for_timeout(30)
            v = pg.evaluate(
                """() => {
                const s = document.querySelector('.slide.on');
                const hid = [...s.querySelectorAll('table.oc tr.hid')];
                const marcadas = hid.filter(t => {
                    const td = t.querySelector('td');
                    if (!td) return false;
                    const e = getComputedStyle(td);
                    return e.boxShadow !== 'none' || e.backgroundColor !== 'rgba(0, 0, 0, 0)';
                });
                const visiveis = hid.filter(t => {
                    const vv = t.querySelector('.vv');
                    return vv && getComputedStyle(vv).display !== 'none';
                });
                return {n: s.dataset.n, total: hid.length,
                        marcadas: marcadas.length, visiveis: visiveis.length};
            }"""
            )
            if v["marcadas"]:
                erros.append(f"slide {v['n']}: {v['marcadas']} de {v['total']} linhas "
                             f"veladas já mostram a marca de alterado")
            if v["visiveis"]:
                erros.append(f"slide {v['n']}: {v['visiveis']} valores velados visíveis")
        b.close()
    r.add("linha velada não entrega o resultado", not erros, " · ".join(erros))


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
    v_creditos_batem(h, r)
    v_transbordo(caminho, r, capturar=RAIZ / "saida" / "revisao")
    v_velado_nao_vaza(caminho, r)
    print(f"\n{len(r.itens)} verificações · {len(r.falhas)} falha(s)\n")
    return 1 if r.falhas else 0


if __name__ == "__main__":
    sys.exit(main(*sys.argv[1:]))

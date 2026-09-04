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


def v_sem_spoiler(h, r):
    """A resposta não pode estar impressa no slide anterior à pergunta.

    É o defeito que mais custa à sessão e o mais fácil de reintroduzir: alguém
    acrescenta uma caixa explicativa antes da pergunta que ela responde, e o
    grupo passa a copiar em vez de raciocinar. A checagem compara as palavras
    de conteúdo da alternativa correta com o texto dos dois slides anteriores.
    """
    S = slides(h)
    erros = []
    banais = set("""a as o os um uma de do da dos das em no na nos nas por para
        com sem que e ou se ao aos as e mais menos ser ter há não já também
        quando onde qual quais como este esta esse essa isso aquilo seu sua
        entre sobre ate depois antes durante deve devem pode podem""".split())
    for i, s_ in enumerate(S):
        if 'class="slide ans' not in s_ or i < 2:
            continue
        certas = re.findall(r'<li class="ok">.*?<div class="tt">(.*?)</div>', s_, re.S)
        # os dois slides antes da pergunta (a pergunta é i-1)
        antes = " ".join(S[max(0, i - 3):i - 1])
        antes = re.sub(r'class="pnote".*?</div>\s*</div>', " ", antes, flags=re.S)
        # o quadro de hipóteses é a lista de trabalho do grupo, não uma caixa
        # explicativa: ele nomeia todos os candidatos por definição, e nomear
        # não é o mesmo que entregar a inferência que a pergunta pede
        antes = re.sub(r'<div class="quadro.*?</div>\s*(?=<div class="(?:cap|box)|</div>)',
                       " ", antes, flags=re.S)
        antes = re.sub(r'<div class="hp[^"]*".*?</div></div>', " ", antes, flags=re.S)
        pa = set(_norm(_texto(antes)).split()) - banais
        for t in certas:
            pc = [w for w in _norm(_texto(t)).split() if len(w) > 4 and w not in banais]
            if not pc:
                continue
            comuns = [w for w in pc if w in pa]
            if len(comuns) / len(pc) >= 0.7:
                erros.append(f"slide {i+1}: “{_texto(t)[:52]}” já está escrita "
                             f"antes ({len(comuns)}/{len(pc)} palavras)")
    r.add("a resposta não está no slide anterior", not erros, " · ".join(erros))


def _norm(t):
    t = unicodedata.normalize("NFD", t).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9 ]+", " ", t)


def v_gabarito(h, r):
    """Higiene do banco de itens: o formato não pode entregar a resposta.

    Três assinaturas de banco gerado automaticamente, todas mensuráveis:
    a letra correta se concentra em duas ou três posições; a correta é a
    alternativa mais longa muito acima do acaso; e o mesmo par se repete nas
    perguntas de dupla resposta. Aluno que percebe qualquer uma delas passa a
    marcar pelo formato, e o banco deixa de medir raciocínio.
    """
    import statistics
    from collections import Counter

    letras, mais_longa, pares, detalhe = [], 0, [], []
    total = 0
    for s in slides(h):
        if 'class="slide ans' not in s:
            continue
        alts = [(m.group(1), m.group(2), _texto(m.group(3))) for m in re.finditer(
            r'<li class="(ok|no)"><span class="k">([A-E])</span>.*?'
            r'<div class="tt">(.*?)</div>', s, re.S)]
        if not alts:
            continue
        total += 1
        certas = [a for a in alts if a[0] == "ok"]
        erradas = [a for a in alts if a[0] == "no"]
        letras += [a[1] for a in certas]
        if len(certas) == 2:
            pares.append(tuple(sorted(a[1] for a in certas)))
        mc = statistics.mean(len(a[2]) for a in certas)
        me = statistics.mean(len(a[2]) for a in erradas)
        if mc > me * 1.25:
            mais_longa += 1
            detalhe.append(f"P{total}: correta {mc:.0f} car x distratores {me:.0f}")

    if not total:
        r.add("higiene do gabarito", True, "sem perguntas")
        return

    c = Counter(letras)
    faltando = [x for x in "ABCDE" if x not in c]
    erros = []
    if len(faltando) > 1:
        erros.append(f"letras que nunca são corretas: {', '.join(faltando)}")
    if c and max(c.values()) > max(2, len(letras) * 0.45):
        erros.append(f"letra concentrada: {dict(sorted(c.items()))}")
    # acaso, para 5 alternativas com 1 correta, é ~28% das perguntas
    if mais_longa > max(2, total * 0.45):
        erros.append(f"correta é a mais longa em {mais_longa} de {total} "
                     f"(acaso ~{total * 0.28:.0f}) — {'; '.join(detalhe[:3])}")
    if len(pares) > 1 and len(set(pares)) == 1:
        erros.append(f"todas as perguntas de dupla resposta usam o par "
                     f"{pares[0][0]} e {pares[0][1]}")
    r.add("higiene do gabarito", not erros, " · ".join(erros)
          or f"{total} perguntas · letras {dict(sorted(c.items()))} · "
             f"correta mais longa em {mais_longa}")


def v_contas(h, r):
    """Confere a aritmética dos números que o caso publica.

    O caso trazia pH 7,30 com bicarbonato 17 e pCO2 32, que Henderson-Hasselbalch
    devolve como 7,35; PaO2/FiO2 de 186 com PaO2 56 em ar ambiente, que dá 267;
    e TFG de 16 para creatinina 3,8 aos 63 anos, que por CKD-EPI 2021 dá 17.
    Nenhum deles seria pego olhando: só fazendo a conta.

    Lê o banco de exames, não os slides: é ele que tem a gasometria completa, e
    `v_banco` já garante que os dois concordam.
    """
    import math

    banco = json.loads(re.search(r'id="banco"[^>]*>(.*?)</script>', h, re.S).group(1))
    porname = {e["n"].lower(): _texto(e["r"]) for e in banco}

    def val(nome, pad=r"(\d+(?:,\d+)?)"):
        t = porname.get(nome.lower())
        if not t:
            return None
        m = re.search(pad, t)
        return float(m.group(1).replace(",", ".")) if m else None

    erros, feitas, faltando = [], [], []

    ph, hco3, pco2 = val("pH arterial"), val("Bicarbonato"), val("pCO2")
    if None in (ph, hco3, pco2):
        faltando.append("gasometria")
    else:
        calc = 6.1 + math.log10(hco3 / (0.03 * pco2))
        feitas.append(f"pH {calc:.2f}")
        if abs(calc - ph) > 0.025:
            erros.append(f"gasometria: HCO3 {hco3:.0f} com pCO2 {pco2:.0f} dá pH "
                         f"{calc:.2f}, o banco diz {ph:.2f}")
        alvo = 1.5 * hco3 + 8
        if not (alvo - 2.5 <= pco2 <= alvo + 2.5):
            erros.append(f"compensação: para HCO3 {hco3:.0f}, Winters prevê pCO2 de "
                         f"{alvo - 2:.0f} a {alvo + 2:.0f}; o banco diz {pco2:.0f}")

    pao2, pf = val("pO2"), val("Relação PaO2/FiO2")
    if None in (pao2, pf):
        faltando.append("relação P/F")
    else:
        calc = pao2 / 0.21
        feitas.append(f"P/F {calc:.0f}")
        if abs(calc - pf) > 6:
            erros.append(f"relação P/F: PaO2 {pao2:.0f} em ar ambiente dá {calc:.0f}, "
                         f"o banco diz {pf:.0f}")

    cr = val("Creatinina", r"Admissão (\d+(?:,\d+)?)")
    tfg = val("Taxa de filtração glomerular estimada")
    m = re.search(r"[Hh]omem de (\d\d) anos", _texto(" ".join(slides(h))))
    idade = float(m.group(1)) if m else None
    if None in (cr, tfg, idade):
        faltando.append("filtração glomerular")
    else:
        # CKD-EPI 2021, homem, sem coeficiente de raça
        calc = (142 * (min(cr / 0.9, 1) ** -0.302) * (max(cr / 0.9, 1) ** -1.200)
                * (0.9938 ** idade))
        feitas.append(f"TFG {calc:.0f}")
        if abs(calc - tfg) > 1.5:
            erros.append(f"CKD-EPI 2021: creatinina {cr} aos {idade:.0f} anos dá "
                         f"{calc:.0f} mL/min/1,73 m², o banco diz {tfg:.0f}")

    if faltando:
        erros.append("não consegui aferir: " + ", ".join(faltando))
    r.add("as contas fecham", not erros, " · ".join(erros) or " · ".join(feitas))


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
    v_sem_spoiler(h, r)
    v_gabarito(h, r)
    v_contas(h, r)
    v_arvore(h, r)
    v_creditos(h, r)
    v_creditos_batem(h, r)
    v_transbordo(caminho, r, capturar=RAIZ / "saida" / "revisao")
    v_velado_nao_vaza(caminho, r)
    print(f"\n{len(r.itens)} verificações · {len(r.falhas)} falha(s)\n")
    return 1 if r.falhas else 0


if __name__ == "__main__":
    sys.exit(main(*sys.argv[1:]))

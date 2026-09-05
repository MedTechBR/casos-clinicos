"""Verificações do modo prontuário.

O baralho tinha `verificar.py`; a condução precisa das suas. As perguntas aqui
são outras: o exame citado existe na gaveta? o sinalizador usado foi declarado?
existe desfecho inalcançável? uma condução ruim chega mesmo a um final ruim?

As oito primeiras são estáticas e leem o caso em Python. As quatro últimas
abrem o arquivo montado e conduzem o paciente de verdade, porque a única prova
de que a física funciona é ela funcionando.

Uso:  python3 ferramentas/verificar_prontuario.py [caso]
"""

from __future__ import annotations

import importlib
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ))


class Placar:
    def __init__(self):
        self.falhas = 0
        self.total = 0

    def add(self, nome, ok, detalhe=""):
        self.total += 1
        if ok:
            print(f"  ok    {nome}" + (f"  {detalhe}" if detalhe else ""))
        else:
            self.falhas += 1
            print(f"  FALHA  {nome}")
            if detalhe:
                for linha in str(detalhe).split(" · "):
                    print(f"         {linha}")


# ─────────────────────────── estáticas ───────────────────────────


def v_acoes(c, r):
    """Ação sem texto ou sem custo de tempo é ação que não aconteceu."""
    erros = []
    vistas = set()
    for a in c.ACOES:
        if a["k"] in vistas:
            erros.append(f"chave repetida: {a['k']}")
        vistas.add(a["k"])
        if not a["x"].strip():
            erros.append(f"{a['k']}: sem o que escrever no prontuário")
        if a["min"] <= 0:
            erros.append(f"{a['k']}: custo de tempo zero")
        if not a["r"].strip():
            erros.append(f"{a['k']}: sem rótulo")
    r.add("toda ação tem texto, rótulo e custo de tempo", not erros,
          " · ".join(erros) or f"{len(c.ACOES)} ações")


def v_sinalizadores(c, r):
    """Sinalizador usado e não declarado vira condição que nunca é verdadeira —
    e o desfecho que depende dela vira inalcançável em silêncio."""
    from motor.prontuario import SINAIS
    usados = set()
    for a in c.ACOES:
        usados |= set(a["exige"]) | set(a["liga"]) | set(a.get("ps", [])) | set(a.get("pl", []))
    for m in c.EVOLUCAO["marcos"]:
        usados |= set(m["liga"]) | set(m["desliga"]) | set(m["exige"]) | set(m["impede"])
    usados |= set(c.EVOLUCAO["quando"]) | set(c.EVOLUCAO["alvos"])
    for d in c.DESFECHOS:
        usados |= {x["s"] for x in d["quando"] if "s" in x}
    for v in c.GATILHOS.values():
        usados |= set(v)
    orfaos = sorted(usados - set(SINAIS))
    r.add("todo sinalizador usado foi declarado", not orfaos,
          ", ".join(orfaos) or f"{len(usados)} em uso")


def v_sinalizadores_mortos(c, r):
    """O contrário: sinalizador que ninguém acende é regra que nunca vale."""
    acesos = set()
    for a in c.ACOES:
        acesos |= set(a["liga"]) | set(a.get("pl", []))
    for m in c.EVOLUCAO["marcos"]:
        acesos |= set(m["liga"])
    for v in c.GATILHOS.values():
        acesos |= set(v)
    lidos = set(c.EVOLUCAO["quando"]) | set(c.EVOLUCAO["alvos"])
    for d in c.DESFECHOS:
        lidos |= {x["s"] for x in d["quando"] if "s" in x}
    for a in c.ACOES:
        lidos |= set(a["exige"])
    for m in c.EVOLUCAO["marcos"]:
        lidos |= set(m["exige"]) | set(m["impede"])
    mortos = sorted(lidos - acesos)
    r.add("todo sinalizador lido é aceso por alguma coisa", not mortos,
          ", ".join(mortos) or f"{len(acesos)} acesos")


def v_gatilhos(c, r):
    """Gatilho apontando para exame que não existe na gaveta nunca dispara."""
    nomes = {e["n"] for e in c.BANCO}
    fora = sorted(set(c.GATILHOS) - nomes)
    r.add("todo gatilho aponta para exame da gaveta", not fora,
          ", ".join(fora) or f"{len(c.GATILHOS)} gatilhos")


def v_imagens(c, r):
    nomes = {e["n"] for e in c.BANCO}
    fora = sorted(set(getattr(c, "IMAGENS", {})) - nomes)
    faltando = [s["arquivo"] for s in getattr(c, "IMAGENS", {}).values()
                if not (c.IMG / s["arquivo"]).exists()]
    sem_credito = [n for n, s in getattr(c, "IMAGENS", {}).items()
                   if not s.get("credito", "").strip()]
    erros = ([f"exame inexistente: {n}" for n in fora]
             + [f"arquivo inexistente: {a}" for a in faltando]
             + [f"sem crédito: {n}" for n in sem_credito])
    r.add("toda imagem tem exame, arquivo e crédito", not erros,
          " · ".join(erros) or f"{len(getattr(c, 'IMAGENS', {}))} imagens")


def v_revisao(c, r):
    """A revisão do fim cobra coisas que existem — exame da gaveta ou ação."""
    nomes = {e["n"] for e in c.BANCO} | {a["k"] for a in c.ACOES}
    erros = []
    for item in c.REVISAO:
        if item["chave"] not in nomes:
            erros.append(f"cobra o que não existe: {item['chave']}")
        if not item["porque"].strip():
            erros.append(f"{item['chave']}: sem o motivo")
    r.add("a revisão do fim cobra o que existe", not erros,
          " · ".join(erros) or f"{len(c.REVISAO)} itens")


def v_espera(c, r):
    """Categoria do banco sem tempo declarado cai num padrão silencioso."""
    from motor.prontuario import ESPERA
    cats = {e["c"] for e in c.BANCO if e["c"]}
    fora = sorted(cats - set(ESPERA))
    r.add("toda categoria de exame tem tempo de resultado", not fora,
          ", ".join(fora) or f"{len(cats)} categorias")


def v_desfechos(c, r):
    """O último desfecho tem de ser incondicional, e todos precisam do porquê."""
    erros = []
    if not c.DESFECHOS:
        erros.append("nenhum desfecho")
    elif c.DESFECHOS[-1]["quando"]:
        erros.append("o último desfecho não é incondicional: existe estado sem final")
    for d in c.DESFECHOS:
        if not d["porque"].strip():
            erros.append(f"{d['k']}: sem explicação fisiológica")
        if not d["p"]:
            erros.append(f"{d['k']}: sem texto")
    qualidades = {d["q"] for d in c.DESFECHOS}
    if len(qualidades) < 3:
        erros.append(f"só {len(qualidades)} qualidade(s) de desfecho: "
                     "sem gradação, a condução não distingue nada")
    r.add("os desfechos fecham o espaço de estados", not erros,
          " · ".join(erros) or f"{len(c.DESFECHOS)} desfechos")


def v_markdown(c, r):
    """A marcação mínima tem de ter sido convertida; asterisco cru é erro."""
    alvo = RAIZ / "saida" / f"{c.SLUG}-prontuario.html"
    h = alvo.read_text(encoding="utf-8")
    corpo = re.sub(r"data:[^;]+;base64,[A-Za-z0-9+/=]+", " ", h)
    achados = [m for m in (r"\*\*", r"(?<![\w/])//(?=[A-Za-zÀ-ÿ])", r"==(?=\w)")
               if re.search(m, corpo)]
    r.add("marcação convertida", not achados, ", ".join(achados))


# ─────────────────────────── conduzindo de verdade ───────────────────────────

# Cada roteiro é uma condução plausível de sala de aula, com o final que ela
# tem de produzir. É a prova de que a física do caso não é decorativa.
ROTEIROS = [
    ("beira do leito, tratou cedo", "melhor", [
        ("acao", "hda"), ("acao", "medicacoes"), ("acao", "respiratorio"),
        ("exame", "Sedimento urinário"), ("esperar", 45),
        ("exame", "ANCA por imunofluorescência indireta"),
        ("exame", "Anticorpo anti-membrana basal glomerular"),
        ("exame", "Complemento C3"),
        ("acao", "oxigenio"), ("acao", "culturas"),
        ("exame", "Lavado broncoalveolar"), ("esperar", 300),
        ("acao", "pulso"), ("acao", "rituximabe"), ("acao", "pjp"),
        ("esperar", 2880), ("esperar", 4320),
    ]),
    ("esperou a sorologia para tratar", "medio", [
        ("acao", "hda"), ("exame", "ANCA por imunofluorescência indireta"),
        ("esperar", 2880), ("acao", "pulso"), ("acao", "rituximabe"),
        ("acao", "pjp"), ("esperar", 4320),
    ]),
    ("só observou", "pior", [
        ("acao", "hda"), ("acao", "respiratorio"),
        ("esperar", 1440), ("esperar", 1440), ("esperar", 1440),
        ("esperar", 1440), ("esperar", 1440),
    ]),
    ("ciclofosfamida em dose plena, sem profilaxia", "medio", [
        ("acao", "hda"), ("exame", "Sedimento urinário"),
        ("exame", "ANCA por imunofluorescência indireta"),
        ("acao", "culturas"), ("acao", "oxigenio"), ("acao", "pulso"),
        ("acao", "cfx_plena"),
        ("esperar", 2880), ("esperar", 2880), ("esperar", 2880),
    ]),
]


def conduzir(pg, roteiro):
    pg.evaluate("() => comecar()")
    for tipo, arg in roteiro:
        if tipo == "acao":
            achou = pg.evaluate(
                "(k) => { const a = ACOES.find(x => x.k === k); "
                "if (!a) return false; fazer(a); return true; }", arg)
            if not achou:
                return {"erro": f"ação inexistente: {arg}"}
        elif tipo == "exame":
            achou = pg.evaluate(
                "(n) => { const e = BANCO.find(x => x.n === n); "
                "if (!e) return false; pedir(e); return true; }", arg)
            if not achou:
                return {"erro": f"exame inexistente: {arg}"}
        elif tipo == "esperar":
            pg.evaluate("(m) => avancar(m, 'Aguardou.')", arg)
    pg.evaluate("() => encerrar()")
    return pg.evaluate(
        "() => ({fim: encerrado && encerrado.k, q: encerrado && encerrado.q, "
        "h: EST.horas, cr: EST.creatinina, reg: REG.length})")


def dinamicas(c, r):
    from playwright.sync_api import sync_playwright
    alvo = RAIZ / "saida" / f"{c.SLUG}-prontuario.html"
    with sync_playwright() as pw:
        b = pw.chromium.launch()
        pg = b.new_page(viewport={"width": 1440, "height": 900})
        erros = []
        pg.on("pageerror", lambda e: erros.append(str(e)))
        pg.on("console", lambda m: erros.append("console: " + m.text)
              if m.type == "error" else None)
        pg.goto(alvo.resolve().as_uri())
        pg.wait_for_timeout(300)

        resultados, alcancados = [], set()
        problemas = []
        for nome, esperado, roteiro in ROTEIROS:
            res = conduzir(pg, roteiro)
            if res.get("erro"):
                problemas.append(f"{nome}: {res['erro']}")
                continue
            resultados.append((nome, res))
            alcancados.add(res["fim"])
            if res["q"] != esperado:
                problemas.append(
                    f"{nome}: esperava desfecho {esperado}, veio {res['q']} "
                    f"({res['fim']})")
        r.add("cada condução chega ao desfecho que ela merece", not problemas,
              " · ".join(problemas) or " · ".join(
                  f"{n}: {x['fim']}" for n, x in resultados))

        r.add("conduções diferentes não terminam no mesmo lugar",
              len(alcancados) == len(resultados),
              f"{len(alcancados)} desfechos distintos em {len(resultados)} conduções")

        # o relógio custa: a mesma conduta, mais tarde, dá um paciente pior
        pg.evaluate("() => comecar()")
        pg.evaluate("() => { fazer(ACOES.find(a=>a.k==='pulso')); "
                    "fazer(ACOES.find(a=>a.k==='rituximabe')); avancar(5760); }")
        cedo = pg.evaluate("() => EST.creatinina")
        pg.evaluate("() => comecar()")
        pg.evaluate("() => { avancar(5760); fazer(ACOES.find(a=>a.k==='pulso')); "
                    "fazer(ACOES.find(a=>a.k==='rituximabe')); avancar(5760); }")
        tarde = pg.evaluate("() => EST.creatinina")
        r.add("o mesmo tratamento, mais tarde, devolve menos rim", tarde > cedo + 0.5,
              f"tratado na primeira hora: Cr {cedo:.1f} · "
              f"tratado no quarto dia: Cr {tarde:.1f}")

        # nada do que não foi pedido pode aparecer no registro
        pg.evaluate("() => comecar()")
        pg.evaluate("() => { fazer(ACOES.find(a=>a.k==='hda')); avancar(4320); }")
        vazou = pg.evaluate("""() => {
            const nomes = REG.filter(e => e.t === 'resultado').map(e => e.tt);
            return nomes.filter(n => !pedidos.includes(n));
        }""")
        r.add("nada aparece no registro sem ter sido pedido", not vazou,
              ", ".join(vazou) or "três dias de espera, zero resultado espontâneo")

        r.add("nenhuma condução gera erro de JavaScript", not erros,
              " · ".join(erros[:4]))
        b.close()


def main(caso="pulmao_rim"):
    c = importlib.import_module(f"casos.{caso}.prontuario")
    print(f"\nverificando {c.SLUG}-prontuario.html\n")
    r = Placar()
    for f in (v_acoes, v_sinalizadores, v_sinalizadores_mortos, v_gatilhos,
              v_imagens, v_revisao, v_espera, v_desfechos, v_markdown):
        f(c, r)
    dinamicas(c, r)
    print(f"\n{r.total} verificações · {r.falhas} falha(s)")
    return 1 if r.falhas else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "pulmao_rim"))

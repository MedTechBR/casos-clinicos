"""Teste de fumaça da interatividade.

Exercita o que o apresentador usa ao vivo. Cada teste mede um efeito observável
— não basta clicar e tirar foto: se a revelação não mudou nada no DOM, falhou.

Uso:  python3 ferramentas/testar.py [saida/pulmao-rim.html]
"""

from __future__ import annotations

import re
import sys
import tempfile
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent


class Testes:
    def __init__(self):
        self.n = 0
        self.falhas = []

    def checa(self, nome, cond, detalhe=""):
        self.n += 1
        if cond:
            print(f"  ok     {nome}" + (f"  ({detalhe})" if detalhe else ""))
        else:
            print(f"  FALHA  {nome}" + (f"  ({detalhe})" if detalhe else ""))
            self.falhas.append(nome)


def rodar(caminho: Path) -> int:
    from playwright.sync_api import sync_playwright

    t = Testes()
    print(f"\ntestando {caminho.name}\n")
    with sync_playwright() as pw:
        b = pw.chromium.launch()
        ctx = b.new_context(
            viewport={"width": 1400, "height": 820},
            accept_downloads=True,
        )
        pg = ctx.new_page()
        erros_js = []
        pg.on("pageerror", lambda e: erros_js.append(str(e)))
        pg.on("console", lambda m: erros_js.append(m.text) if m.type == "error" else None)
        pg.goto(caminho.resolve().as_uri())
        pg.wait_for_timeout(400)

        total = pg.evaluate("document.querySelectorAll('.slide').length")
        t.checa("carregou sem erro de JS", not erros_js, "; ".join(erros_js[:2]))
        t.checa("slides presentes", total >= 38, f"{total} slides")

        # ── navegação e revelação por passos ──────────────────────────────
        pg.evaluate("show(1)")  # bloco 1: prosa em 5 passos
        antes = pg.evaluate("document.querySelectorAll('.slide.on .pv.on').length")
        pg.keyboard.press("ArrowRight")
        depois = pg.evaluate("document.querySelectorAll('.slide.on .pv.on').length")
        t.checa("→ revela um passo por vez", antes == 0 and depois == 1, f"{antes} → {depois}")

        pg.keyboard.press("ArrowLeft")
        t.checa(
            "← esconde o último passo",
            pg.evaluate("document.querySelectorAll('.slide.on .pv.on').length") == 0,
        )

        pg.keyboard.press("a")
        tudo = pg.evaluate(
            "document.querySelectorAll('.slide.on .pv').length ==="
            " document.querySelectorAll('.slide.on .pv.on').length"
        )
        t.checa("A revela tudo do slide", tudo)
        pg.keyboard.press("z")
        t.checa(
            "Z esconde tudo",
            pg.evaluate("document.querySelectorAll('.slide.on .pv.on').length") == 0,
        )

        n0 = pg.evaluate("document.querySelector('.slide.on').dataset.n")
        pg.keyboard.press("a")
        pg.keyboard.press("ArrowRight")  # sem passos pendentes, avança de slide
        n1 = pg.evaluate("document.querySelector('.slide.on').dataset.n")
        t.checa("→ avança de slide quando não há mais passos", int(n1) == int(n0) + 1)

        # ── laudo velado ─────────────────────────────────────────────────
        i_rv = pg.evaluate(
            "[...document.querySelectorAll('.slide')].findIndex(s=>s.querySelector('.rv'))"
        )
        pg.evaluate(f"show({i_rv})")
        oculto = pg.evaluate(
            "getComputedStyle(document.querySelector('.slide.on .rv-in')).display"
        )
        pg.click(".slide.on .rv-ph")
        visivel = pg.evaluate(
            "getComputedStyle(document.querySelector('.slide.on .rv-in')).display"
        )
        t.checa("laudo velado abre ao clique", oculto == "none" and visivel != "none",
                f"{oculto} → {visivel}")

        # ── tabela velada ────────────────────────────────────────────────
        i_oc = pg.evaluate(
            "[...document.querySelectorAll('.slide')].findIndex(s=>s.querySelector('table.oc'))"
        )
        pg.evaluate(f"show({i_oc})")
        h0 = pg.evaluate("document.querySelectorAll('.slide.on table.oc tr.hid').length")
        pg.click(".slide.on table.oc tbody tr.hid")
        h1 = pg.evaluate("document.querySelectorAll('.slide.on table.oc tr.hid').length")
        t.checa("tabela velada abre linha a linha", h1 == h0 - 1, f"{h0} → {h1} linhas ocultas")
        valor = pg.evaluate(
            "document.querySelector('.slide.on table.oc tbody tr:not(.hid) .vv').textContent.trim()"
        )
        t.checa("linha revelada mostra o valor", bool(valor), valor[:40])

        # ── seleção de alternativa com limite ────────────────────────────
        i_q = pg.evaluate(
            "[...document.querySelectorAll('.slide')].findIndex(s=>s.classList.contains('q'))"
        )
        pg.evaluate(f"show({i_q})")
        pg.click(".slide.on .alts li:nth-child(1)")
        t.checa(
            "alternativa marca ao clique",
            pg.evaluate("document.querySelectorAll('.slide.on .alts li.sel').length") == 1,
        )
        pg.click(".slide.on .alts li:nth-child(2)")
        t.checa(
            "limite de marcações respeitado",
            pg.evaluate("document.querySelectorAll('.slide.on .alts li.sel').length") == 1,
            "data-max=1",
        )
        t.checa(
            "contador concorda com a marcação",
            "1 de 1" in pg.evaluate("document.querySelector('.slide.on .cnt').textContent"),
            pg.evaluate("document.querySelector('.slide.on .cnt').textContent"),
        )

        # ── mapa de territórios ──────────────────────────────────────────
        i_mapa = pg.evaluate(
            "[...document.querySelectorAll('.slide')].findIndex(s=>s.querySelector('.mapa'))"
        )
        if i_mapa >= 0:
            pg.evaluate(f"show({i_mapa})")
            pg.wait_for_timeout(120)
            t.checa("mapa começa sem território aceso",
                    pg.evaluate("document.querySelectorAll('.slide.on .terr.on').length") == 0)
            pg.keyboard.press("ArrowRight")
            pg.wait_for_timeout(160)
            par = pg.evaluate(
                """() => {
                const t = document.querySelector('.slide.on .terr.on');
                if (!t) return null;
                const k = t.dataset.terr;
                const l = document.querySelector('.slide.on .lt[data-terr="' + k + '"]');
                return {chave: k, legenda: !!(l && l.classList.contains('on'))};
            }"""
            )
            t.checa("→ acende desenho e legenda juntos",
                    bool(par and par["legenda"]), par and par["chave"])
            pg.click('.slide.on .lt[data-terr="pele"]')
            pg.wait_for_timeout(160)
            t.checa("clicar na legenda acende o território no desenho",
                    pg.evaluate(
                        "document.querySelector('.slide.on .terr[data-terr=\\'pele\\']')"
                        ".classList.contains('on')"))
            t.checa("nenhum território sem legenda correspondente",
                    pg.evaluate(
                        "[...document.querySelectorAll('.slide.on .terr')].every(x=>"
                        "document.querySelector('.slide.on .lt[data-terr=\\''+x.dataset.terr+'\\']'))"))

        # ── figuras anotadas ─────────────────────────────────────────────
        anot = pg.evaluate(
            """() => [...document.querySelectorAll('figure.an')].map(f => {
                const img = f.querySelector('img'), svg = f.querySelector('svg');
                return {vb: svg.getAttribute('viewBox'),
                        par: svg.getAttribute('preserveAspectRatio')};
            })"""
        )
        t.checa("toda anotação usa o viewBox da própria imagem",
                bool(anot) and all(a["vb"] and a["vb"] != "0 0 100 100" for a in anot),
                f"{len(anot)} figuras")
        t.checa("anotação enquadrada como a imagem (contain)",
                all(a["par"] == "xMidYMid meet" for a in anot),
                "senão o círculo vira elipse e a seta erra o alvo")

        # ── gaveta de exames ─────────────────────────────────────────────
        pg.keyboard.press("x")
        pg.wait_for_timeout(220)
        t.checa("X abre a gaveta", pg.evaluate("document.getElementById('gav').classList.contains('on')"))
        pg.fill("#q", "creatinina")
        pg.wait_for_timeout(120)
        cartao = pg.evaluate(
            "(document.querySelector('#gb .card .cr')||{}).textContent||''"
        )
        t.checa("busca exata devolve o cartão", "3,8" in cartao, cartao[:60])
        t.checa("valor alterado sai em vermelho",
                pg.evaluate("!!document.querySelector('#gb .card .cr.alt')"))
        t.checa("cartão traz a referência",
                bool(pg.evaluate("(document.querySelector('#gb .cf')||{}).textContent||''")))

        pg.fill("#q", "hemograma")
        pg.wait_for_timeout(120)
        sug = pg.evaluate("document.querySelectorAll('#gb .sug').length")
        t.checa("nome de painel lista os componentes", sug >= 8, f"{sug} analitos")

        pg.fill("#q", "creatnina")  # erro de digitação
        pg.wait_for_timeout(150)
        achou = pg.evaluate(
            "[...document.querySelectorAll('#gb .card .cn,#gb .sug b')].map(e=>e.textContent)"
        )
        t.checa("busca tolera erro de digitação",
                any("reatinina" in x for x in achou), ", ".join(achou[:3]) or "nada")

        pg.fill("#q", "sodio")
        pg.wait_for_timeout(120)
        t.checa("busca insensível a acento",
                "136" in (pg.evaluate("(document.querySelector('#gb .card .cr')||{}).textContent||''")))
        t.checa("histórico registra os pedidos",
                pg.evaluate("document.querySelectorAll('.hist li').length") >= 2)
        pg.keyboard.press("Escape")
        pg.wait_for_timeout(220)
        t.checa("Escape fecha a gaveta",
                not pg.evaluate("document.getElementById('gav').classList.contains('on')"))

        # ── visão geral ──────────────────────────────────────────────────
        pg.keyboard.press("o")
        t.checa("O abre a visão geral", pg.evaluate("document.getElementById('grid').classList.contains('on')"))
        t.checa("miniaturas cobrem todos os slides",
                pg.evaluate("document.querySelectorAll('#grid .t').length") == total)
        cortados = pg.evaluate(
            """() => {
            const ts = [...document.querySelectorAll('#grid .t b')];
            const ruins = [];
            ts.forEach((b, k) => {
                const txt = b.textContent;
                if (!txt.endsWith('…')) return;
                const s = document.querySelectorAll('.slide')[k];
                const h = s.querySelector('h1,h2');
                const cheio = (h ? h.textContent : '').replace(/\\s+/g, ' ').trim();
                const pref = txt.slice(0, -1);
                // o corte só é legítimo se o caractere seguinte no título for espaço
                const i = cheio.toLowerCase().indexOf(pref.toLowerCase());
                if (i === 0 && cheio[pref.length] && cheio[pref.length] !== ' ')
                    ruins.push(txt);
            });
            return ruins;
        }"""
        )
        t.checa("miniatura não corta no meio da palavra", not cortados, "; ".join(cortados[:3]))
        pg.click("#grid .t:nth-child(9)")
        pg.wait_for_timeout(120)
        t.checa("clicar na miniatura pula para o slide",
                pg.evaluate("document.querySelector('.slide.on').dataset.n") == "9")

        # ── modo de edição e round-trip do Ctrl+S ────────────────────────
        pg.keyboard.press("e")
        t.checa("E entra no modo de edição", pg.evaluate("document.body.classList.contains('editando')"))
        pg.evaluate(
            """() => {
            const p = document.querySelector('.slide.on [contenteditable]');
            p.textContent = 'TEXTO EDITADO NO TESTE';
            p.dispatchEvent(new Event('input', {bubbles: true}));
        }"""
        )
        # edição do banco pela gaveta
        pg.keyboard.press("x")
        pg.wait_for_timeout(200)
        pg.fill("#q", "ferritina")
        pg.wait_for_timeout(150)
        pg.evaluate(
            """() => {
            const c = document.querySelector('#gb .card [data-f="r"]');
            c.textContent = '999 ng/mL EDITADO';
            c.dispatchEvent(new Event('input', {bubbles: true}));
        }"""
        )
        t.checa("banco aceita edição pela gaveta",
                "EDITADO" in pg.evaluate("BANCO.find(e=>e.n==='Ferritina').r"))
        pg.keyboard.press("Escape")
        pg.wait_for_timeout(200)

        with pg.expect_download() as dl:
            pg.keyboard.press("Control+s")
        arq = Path(tempfile.gettempdir()) / "roundtrip.html"
        dl.value.save_as(arq)
        salvo = arq.read_text()
        t.checa("Ctrl+S baixa um HTML", len(salvo) > 500_000, f"{len(salvo)/1024:,.0f} KB")
        t.checa("edição do slide vai no arquivo salvo", "TEXTO EDITADO NO TESTE" in salvo)
        t.checa("edição do banco vai no arquivo salvo", "999 ng/mL EDITADO" in salvo)
        # o CSS e o JS embutidos citam "contenteditable" e "data-runtime" no
        # próprio código: a checagem tem que olhar só a marcação do corpo.
        marcacao = re.sub(r"<(style|script)\b.*?</\1>", " ", salvo, flags=re.S)
        marcacao = marcacao[marcacao.find("<body") :]
        t.checa("arquivo salvo não carrega slide aberto",
                "slide on" not in marcacao and 'class="on"' not in marcacao)
        t.checa("arquivo salvo não carrega bolinhas de etapa",
                re.search(r'id="etapas"[^>]*>\s*</div>', marcacao) is not None)
        t.checa("arquivo salvo não carrega contenteditable",
                "contenteditable" not in marcacao and "data-ed" not in marcacao)
        t.checa("arquivo salvo não carrega alternativa marcada", "sel" not in
                re.sub(r'class="([^"]*)"', lambda m: m.group(1),
                       "".join(re.findall(r'<li class="[^"]*sel[^"]*"', marcacao))))
        t.checa("tabelas voltam veladas no arquivo salvo",
                marcacao.count("<tr") - marcacao.count("<tr>") ==
                len(re.findall(r'<tr class="[^"]*\bhid\b', marcacao)),
                f"{len(re.findall(chr(60)+chr(116)+chr(114)+chr(32)+chr(99)+'lass=\"[^\"]*.hid', marcacao))} linhas veladas")

        # o arquivo salvo tem que continuar funcionando
        pg2 = ctx.new_page()
        erros2 = []
        pg2.on("pageerror", lambda e: erros2.append(str(e)))
        pg2.goto(arq.resolve().as_uri())
        pg2.wait_for_timeout(400)
        t.checa("arquivo salvo abre sem erro de JS", not erros2, "; ".join(erros2[:2]))
        t.checa("arquivo salvo tem os mesmos slides",
                pg2.evaluate("document.querySelectorAll('.slide').length") == total)
        pg2.keyboard.press("x")
        pg2.wait_for_timeout(200)
        pg2.fill("#q", "ferritina")
        pg2.wait_for_timeout(150)
        t.checa("a edição do banco sobreviveu ao round-trip",
                "999" in pg2.evaluate("(document.querySelector('#gb .card .cr')||{}).textContent||''"))

        b.close()

    print(f"\n{t.n} verificações · {len(t.falhas)} falha(s)")
    if t.falhas:
        print("falharam: " + ", ".join(t.falhas))
    return 1 if t.falhas else 0


if __name__ == "__main__":
    alvo = Path(sys.argv[1]) if len(sys.argv) > 1 else RAIZ / "saida" / "pulmao-rim.html"
    sys.exit(rodar(alvo))

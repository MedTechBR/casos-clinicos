"""HTML -> PDF, para levar em papel.

Imprime com tudo revelado — no papel não existe clique — e com as notas do
apresentador, que só aparecem em `@media print`. Um slide por página, 1280x720.

Uso:  python3 ferramentas/publicar.py [saida/pulmao-rim.html]
"""

from __future__ import annotations

import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ))


def publicar(caminho: Path, destino: Path = None) -> Path:
    from playwright.sync_api import sync_playwright

    destino = destino or caminho.with_suffix(".pdf")
    with sync_playwright() as pw:
        b = pw.chromium.launch()
        pg = b.new_page()
        pg.goto(caminho.resolve().as_uri())
        pg.wait_for_timeout(500)
        # o CSS de impressão já revela tudo; garantimos o estado no DOM também
        pg.evaluate("document.querySelectorAll('.slide').forEach(s=>{"
                    "s.querySelectorAll('.rv,.pv,svg.ov.rvov').forEach(e=>e.classList.add('on'));"
                    "s.querySelectorAll('table.oc tbody tr').forEach(r=>r.classList.remove('hid'));"
                    "s.querySelectorAll('figure.an').forEach(f=>f.classList.add('on'));});")
        # No papel não há caminho percorrido: todos os ramos são impressos de
        # uma vez. Sem isto, os valores de estado escritos na prosa sairiam com
        # o número da admissão em todas as páginas — inclusive na do ramo que
        # gastou trinta e quatro horas. A varredura abaixo percorre a árvore
        # inteira e carimba cada slide com o estado do caminho que chega a ele;
        # slide alcançável por mais de um caminho fica com o primeiro, que é o
        # do tronco.
        pg.evaluate("""() => {
            const S = [...document.querySelectorAll('.slide')];
            const byId = k => document.getElementById('s-' + k);
            const prox = s => s.dataset.segue ? byId(s.dataset.segue)
                                              : (S[S.indexOf(s) + 1] || null);
            const feito = new Set();
            const ap = (est, ef) => {
              const e = JSON.parse(JSON.stringify(est));
              ['horas','creatinina','spo2','hb'].forEach(k => {
                if (ef[k]) e[k] = Math.round((e[k] + ef[k]) * 10) / 10; });
              (ef.liga || []).forEach(f => {
                if (!e.sinalizadores.includes(f)) e.sinalizadores.push(f); });
              (ef.desliga || []).forEach(f => {
                const i = e.sinalizadores.indexOf(f);
                if (i >= 0) e.sinalizadores.splice(i, 1); });
              return e;
            };
            const carimbar = (s, est) => {
              if (feito.has(s)) return;
              feito.add(s);
              s.querySelectorAll('.ev[data-campo]').forEach(e => {
                const c = CAMPOS[e.dataset.campo], v = est[e.dataset.campo];
                if (c && v !== undefined)
                  e.textContent = v.toFixed(c.casas).replace('.', ',') + c.unidade;
              });
            };
            const andar = (s, est, n) => {
              while (s && n-- > 0){
                if (s.dataset.custo) est = ap(est, JSON.parse(s.dataset.custo));
                carimbar(s, est);
                if (s.classList.contains('fim')) return;
                if (s.classList.contains('no')){
                  [...s.querySelectorAll('.rm')].forEach(r => andar(
                    byId(r.dataset.vai), ap(est, JSON.parse(r.dataset.efeito)), 150));
                  return;
                }
                s = prox(s);
              }
            };
            andar(S[0], JSON.parse(JSON.stringify(EST0)), 250);
        }""")
        pg.emulate_media(media="print")
        pg.pdf(path=str(destino), width="1280px", height="720px",
               print_background=True, margin={"top": "0", "bottom": "0",
                                              "left": "0", "right": "0"})
        b.close()
    kb = destino.stat().st_size / 1024
    print(f"{destino.relative_to(RAIZ)}  ·  {kb:,.0f} KB")
    return destino


if __name__ == "__main__":
    from ferramentas.tirar import alvo as _alvo
    a = sys.argv[1] if len(sys.argv) > 1 else "pulmao_rim"
    alvo = Path(a) if a.endswith(".html") else _alvo(a)
    publicar(alvo)

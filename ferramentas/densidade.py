"""Escolhe a densidade tipográfica de cada slide pela medida, não pelo palpite.

O autor escreve prosa; quem decide o corpo da fonte é a régua, e ela trabalha
nos dois sentidos:

- slide que transborda sobe um degrau de densidade (corpo menor);
- slide que ocupa pouco da área útil desce um degrau (corpo maior).

O segundo é o que estava faltando. Slide após slide preenchido pela metade,
sempre com o mesmo corpo, é justamente o que faz um baralho parecer template —
e num datashow ruim corpo pequeno num campo vazio é desperdício duplo.

Se nem o degrau mais apertado couber, o slide tem texto demais e isso é dito:
apertar mais seria ilegível projetado.

Uso:
  python3 ferramentas/densidade.py [caso]            mede e relata
  python3 ferramentas/densidade.py [caso] --aplicar  reescreve caso.py
"""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ))

# do mais folgado ao mais apertado
DEGRAUS = [None, "dense", "xd"]

# faixa-alvo de ocupação da área útil pelo conteúdo do slide
PISO, TETO = 0.58, 1.0


def _medir_js() -> str:
    return """(k) => {
        const s = document.querySelectorAll('.slide')[k];
        const b = s.querySelector('.body') || s;
        const t = s.querySelector('h1,h2');
        const sr = s.getBoundingClientRect(), br = b.getBoundingClientRect();
        // da borda de cima do corpo até o rodapé: é o que o conteúdo pode usar
        const rodape = s.querySelector('.foot');
        const limite = rodape ? rodape.getBoundingClientRect().top - 10 : sr.bottom - 40;
        const disponivel = Math.max(1, limite - br.top);
        const ocupado = Math.max(b.scrollHeight, br.height);
        const fora = [...b.querySelectorAll('*')].filter(e => {
            const r = e.getBoundingClientRect();
            return r.width > 0 && (r.right > br.right + 1 || r.left < br.left - 1);
        }).length;
        return {
            titulo: t ? t.textContent.trim() : '',
            classes: [...s.classList],
            // pergunta, resposta, capa e divisor não são governados por esta
            // régua: não têm .body, são centrados de propósito, e o texto deles
            // vive em perguntas.py, não em caso.py
            regido: !['q', 'ans', 'cover', 'mom'].some(c => s.classList.contains(c)),
            excesso: Math.max(b.scrollHeight - b.clientHeight, s.scrollHeight - s.clientHeight),
            horizontal: fora,
            ocupacao: ocupado / disponivel,
            // slide com figura de altura fixa não se estica trocando a fonte
            fixo: !!b.querySelector('figure,svg,.mapa'),
        };
    }"""


def medir(caminho: Path):
    from playwright.sync_api import sync_playwright

    with sync_playwright() as pw:
        b = pw.chromium.launch()
        pg = b.new_page(viewport={"width": 1400, "height": 860})
        pg.goto(caminho.resolve().as_uri())
        pg.wait_for_timeout(300)
        # medir em escala 1:1: com o palco escalado, getBoundingClientRect e
        # scrollHeight ficam em unidades diferentes e a fração sai errada
        pg.evaluate("document.getElementById('stage').style.transform='none'")
        n = pg.evaluate("document.querySelectorAll('.slide').length")
        out = {}
        for i in range(n):
            pg.evaluate(f"show({i})")
            pg.keyboard.press("a")
            # a revelação anima por .38s; medir antes disso lê a caixa no meio
            # da transição e acusa transbordo de poucos pixels que não existe
            pg.wait_for_timeout(430)
            out[i + 1] = pg.evaluate(_medir_js(), i)
        b.close()
    return out


def _atual(classes):
    for d in ("xd", "dense"):
        if d in classes:
            return d
    return None


def _mover(d, passo):
    i = DEGRAUS.index(d)
    return DEGRAUS[max(0, min(len(DEGRAUS) - 1, i + passo))]


def aplicar(caso: str, titulo: str, nova) -> bool:
    f = RAIZ / "casos" / caso / "caso.py"
    src = f.read_text()
    alvo = titulo.replace('"', '\\"')
    i = src.find(f'"{alvo}"')
    if i < 0:
        print(f"       ?? não achei o slide “{titulo}” em {f.name}")
        return False
    fim = src.find("\n    ),", i)
    trecho = src[i:fim]
    if nova is None:
        novo = re.sub(r'\n\s*densidade="[a-z]*",', "", trecho)
    elif "densidade=" in trecho:
        novo = re.sub(r'densidade="[a-z]*"', f'densidade="{nova}"', trecho)
    else:
        novo = trecho + f'\n        densidade="{nova}",'
    f.write_text(src[:i] + novo + src[fim:])
    return True


def _construir(caso: str) -> Path:
    """Em processo separado: o módulo do caso é lido do disco a cada volta.
    Reconstruir no mesmo processo devolveria o caso em cache e a medida seria
    sempre a da versão anterior."""
    r = subprocess.run([sys.executable, "build.py", caso], cwd=RAIZ,
                       check=True, capture_output=True, text=True)
    return RAIZ / "saida" / r.stdout.split()[0].split("/")[-1]


def main(caso="pulmao_rim", aplicar_mudanca=False):
    for volta in range(1, 2 * len(DEGRAUS) + 2):
        alvo = _construir(caso)
        m = medir(alvo)
        apertar = {n: r for n, r in m.items()
                   if r["regido"] and (r["excesso"] > 1 or r["horizontal"])}
        folgar = {n: r for n, r in m.items()
                  if r["regido"] and not r["fixo"] and r["ocupacao"] < PISO
                  and _atual(r["classes"]) is not None
                  and n not in apertar}
        if not apertar and not folgar:
            reg = [r for r in m.values() if r["regido"]]
            media = sum(r["ocupacao"] for r in reg) / max(1, len(reg))
            print(f"\n{len(m)} slides ({len(reg)} regidos pela régua) · "
                  f"ocupação média {media:.0%} · nenhum transborda, nenhum vazio")
            return 0

        print(f"\nvolta {volta}: {len(apertar)} apertando, {len(folgar)} folgando")
        mudou = False
        for n, r in sorted(apertar.items()):
            atual = _atual(r["classes"])
            nova = _mover(atual, +1)
            motivo = ("vaza na horizontal" if r["horizontal"]
                      else f"excesso {r['excesso']}px")
            print(f"  {n:2d} ↑ “{r['titulo'][:40]}” {motivo} · {atual or 'normal'} → {nova}")
            if aplicar_mudanca:
                if nova == atual:
                    print("       !! já está no degrau mais apertado. Corte "
                          "conteúdo ou divida o slide em dois.")
                else:
                    mudou |= aplicar(caso, r["titulo"], nova)
        for n, r in sorted(folgar.items()):
            atual = _atual(r["classes"])
            nova = _mover(atual, -1)
            print(f"  {n:2d} ↓ “{r['titulo'][:40]}” ocupa {r['ocupacao']:.0%} "
                  f"· {atual} → {nova or 'normal'}")
            if aplicar_mudanca:
                mudou |= aplicar(caso, r["titulo"], nova)
        if not aplicar_mudanca or not mudou:
            return 1 if apertar else 0
    print("\n!! não convergiu: algum slide está oscilando entre dois degraus")
    return 1


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    sys.exit(main(args[0] if args else "pulmao_rim", "--aplicar" in sys.argv))

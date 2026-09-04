"""Testes das próprias verificações.

Uma checagem que não pega o defeito que ela existe para pegar é pior do que
nenhuma: ela dá licença para parar de olhar. Cada verificação de
`verificar.py` é exercitada aqui contra um arquivo deliberadamente quebrado.

Uso:  python3 ferramentas/autoteste.py
"""

from __future__ import annotations

import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ))

import re  # noqa: E402

import ferramentas.verificar as V  # noqa: E402


def _quebra(h, alvo, veneno, antes=True):
    assert h.count(alvo) >= 1, f"âncora não encontrada: {alvo[:40]}"
    return h.replace(alvo, (veneno + alvo) if antes else (alvo + veneno), 1)


def _antes_da_pergunta(h, n, veneno):
    """Injeta o texto no fim do slide ANTERIOR à pergunta n.

    A checagem ignora de propósito o próprio slide da pergunta — envenenar ali
    não prova nada.
    """
    i = h.index(f'<div class="qn">Pergunta {n}</div>')
    fim = h.rindex("</section>", 0, i)
    return h[:fim] + veneno + h[fim:]


CASOS = [
    (
        "alinhamento pergunta/resposta",
        V.v_alternativas,
        lambda h: h.replace('<li class="ok">', '<li class="no">', 1),
    ),
    (
        "títulos sem efeito",
        V.v_titulos,
        lambda h: h.replace("<h2>Exame físico</h2>",
                            "<h2>Quando o pulmão acusa o rim</h2>", 1),
    ),
    (
        "markdown convertido",
        V.v_markdown,
        lambda h: _quebra(h, "<h2>Exame físico</h2>", "<p>texto com **negrito** cru</p>"),
    ),
    (
        "coerência banco × slides",
        V.v_banco,
        lambda h: h.replace('<span class="vv">3,8 mg/dL', '<span class="vv">9,9 mg/dL', 1),
    ),
    (
        "crédito e licença nas figuras",
        V.v_creditos,
        lambda h: re.sub(r'<span class="cred">.*?</span>', '<span class="cred"></span>',
                         h, count=1, flags=re.S),
    ),
    (
        "a resposta não está no slide anterior",
        V.v_sem_spoiler,
        lambda h: _antes_da_pergunta(h, 3,
                                     "<p>O sangramento é glomerular.</p>"),
    ),
    (
        "higiene do gabarito",
        V.v_gabarito,
        # devolve todos os gabaritos para a letra D, como no banco original
        lambda h: re.sub(r'<li class="(ok|no)"><span class="k">[A-E]</span>',
                         lambda m: f'<li class="{m.group(1)}"><span class="k">D</span>',
                         h),
    ),
    (
        "as contas fecham",
        V.v_contas,
        # devolve o bicarbonato ao valor que tornava o trio impossível:
        # com HCO3 17 e pCO2 32, Henderson-Hasselbalch dá 7,35, não 7,29
        lambda h: h.replace("15 mEq/L", "17 mEq/L"),
    ),
    (
        "créditos batem com as figuras",
        V.v_creditos_batem,
        lambda h: _quebra(h, "<li>Imunofluorescência p-ANCA: Simon Caulton",
                          "<li>Radiografia de tórax: CDC / D. Loren Ketai · PHIL.</li>"),
    ),
]


def main(caminho=None):
    caminho = Path(caminho or RAIZ / "saida" / "pulmao-rim.html")
    h = caminho.read_text()
    print(f"\ntestando as verificações contra {caminho.name}\n")
    falhas = []
    for nome, fn, veneno in CASOS:
        limpo = V.Relatorio()
        limpo.add = lambda *a, **k: V.Relatorio.add(limpo, *a, **k)
        sujo = V.Relatorio()
        import contextlib
        import io

        with contextlib.redirect_stdout(io.StringIO()):
            fn(h, limpo)
        try:
            with contextlib.redirect_stdout(io.StringIO()):
                fn(veneno(h), sujo)
        except AssertionError as e:
            print(f"  ?      {nome}: não consegui envenenar ({e})")
            falhas.append(nome)
            continue
        ok = not limpo.falhas and sujo.falhas
        print(f"  {'ok   ' if ok else 'FALHA'}  {nome}"
              + ("" if ok else
                 f"  (limpo={'falha' if limpo.falhas else 'ok'}, "
                 f"envenenado={'falha' if sujo.falhas else 'ok'})"))
        if not ok:
            falhas.append(nome)
    print(f"\n{len(CASOS)} verificações exercitadas · {len(falhas)} sem serventia")
    return 1 if falhas else 0


if __name__ == "__main__":
    sys.exit(main(*sys.argv[1:]))

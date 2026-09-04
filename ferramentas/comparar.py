"""Compara o HTML reconstruído com o original, slide a slide.

Não compara bytes: compara o que importa — o texto visível de cada slide, na
ordem, e a estrutura interativa (quantos passos de revelação, quantas tabelas
veladas, quantas figuras). É a prova de que a extração para Python não perdeu
nem inventou conteúdo.

Uso:  python3 ferramentas/comparar.py <original.html> <reconstruido.html>
"""

from __future__ import annotations

import difflib
import re
import sys
import unicodedata
from pathlib import Path


def slides(caminho: Path):
    h = caminho.read_text()
    corpo = h[h.find("<body>") :]
    corpo = corpo[: corpo.find('id="grid"') if 'id="grid"' in corpo else corpo.find("id='grid'")]
    return [s for s in re.split(r'(?=<section class="slide)', corpo) if s.startswith("<section")]


def visivel(s: str) -> str:
    s = re.sub(r"<figcaption.*?</figcaption>", " ", s, flags=re.S)
    s = re.sub(r'<div class="foot">.*?</div>', " ", s, flags=re.S)
    s = re.sub(r"<[^>]+>", " ", s)
    s = unicodedata.normalize("NFC", s)
    s = s.replace(" ", " ").replace("—", "-").replace("–", "-")
    return re.sub(r"\s+", " ", s).strip()


def estrutura(s: str) -> dict:
    return {
        "passos": len(re.findall(r'class="pv"', s)),
        "revelacoes": len(re.findall(r'class="rv"', s)),
        "tabelas_veladas": len(re.findall(r'class="lab oc"', s)),
        "linhas_veladas": len(re.findall(r"<tr[^>]*\bhid\b", s)),
        "figuras": len(re.findall(r"<figure", s)),
        "imagens": len(re.findall(r"<img", s)),
        "alternativas": len(re.findall(r'<ul class="alts', s)),
        "notas": len(re.findall(r'class="pnote"', s)),
        "caixas": len(re.findall(r'class="box ', s)),
        "tabelas": len(re.findall(r"<table", s)),
    }


def main(orig: Path, novo: Path) -> int:
    A, B = slides(orig), slides(novo)
    problemas = 0

    if len(A) != len(B):
        print(f"!! contagem de slides: original {len(A)}, reconstruído {len(B)}")
        problemas += 1

    for n, (a, b) in enumerate(zip(A, B), 1):
        ta, tb = visivel(a), visivel(b)
        if ta != tb:
            problemas += 1
            print(f"\n!! slide {n}: texto visível diverge")
            for linha in difflib.unified_diff(
                ta.split(". "), tb.split(". "), "original", "reconstruído", n=0, lineterm=""
            ):
                if linha.startswith(("+", "-")) and not linha.startswith(("+++", "---")):
                    print("   " + linha[:200])
        ea, eb = estrutura(a), estrutura(b)
        if ea != eb:
            problemas += 1
            dif = {k: (ea[k], eb[k]) for k in ea if ea[k] != eb[k]}
            print(f"!! slide {n}: estrutura diverge {dif}")

    # imagens: mesmos bytes, mesma quantidade
    b64 = lambda p: re.findall(r"base64,([A-Za-z0-9+/=]{500,})", p.read_text())
    ia, ib = b64(orig), b64(novo)
    if ia != ib:
        problemas += 1
        print(f"!! imagens divergem: {len(ia)} no original, {len(ib)} no reconstruído")
        for k, (x, y) in enumerate(zip(ia, ib), 1):
            if x != y:
                print(f"   imagem {k}: {len(x)} vs {len(y)} caracteres de base64")
    else:
        print(f"imagens: {len(ia)} idênticas byte a byte")

    banco = lambda p: re.search(r"id=[\"']banco[\"'][^>]*>(.*?)</script>", p.read_text(), re.S).group(1)
    import json

    ba, bb = json.loads(banco(orig)), json.loads(banco(novo))
    if ba != bb:
        problemas += 1
        print(f"!! banco diverge: {len(ba)} vs {len(bb)} analitos")
        for x, y in zip(ba, bb):
            if x != y:
                print(f"   {x['n']}: {x} != {y}")
                break
    else:
        print(f"banco: {len(ba)} analitos idênticos")

    print(f"\n{len(A)} slides comparados · {problemas} divergência(s)")
    return 1 if problemas else 0


if __name__ == "__main__":
    sys.exit(main(Path(sys.argv[1]), Path(sys.argv[2])))

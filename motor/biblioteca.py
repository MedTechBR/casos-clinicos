"""A biblioteca: a tela que lista os casos.

Outra linguagem, de propósito. O caso aberto é escuro e cinematográfico; a
biblioteca é clara, de papel, e pertence à família de aplicativos que já existe
— ícone arredondado, tipografia limpa, nada de gradiente decorativo.

Como num aplicativo de streaming: prateleira clara, reprodutor escuro.

Cada cartão diz o que custa entrar: duração, número de decisões e número de
desfechos. Não há nota, não há estrela e não há barra de progresso — é uma
prateleira de casos, não um jogo.
"""

from __future__ import annotations

import base64
import json
import mimetypes
from pathlib import Path

from .conteudo import texto

# Cada caso tem uma cor canônica, como cada aplicativo do portal tem a sua.
CORES = {
    "vermelho": "#c2455e", "azul": "#2f6fa8", "laranja": "#c96a2e",
    "verde": "#2f7d55", "roxo": "#6a5acd", "ocre": "#b08324",
}


def _contar(slug):
    """Números reais do caso, lidos do próprio roteiro: o cartão não promete
    o que a apresentação não tem."""
    import importlib, re
    try:
        m = importlib.import_module(f"casos.{slug}.etapas")
    except Exception:
        return {}
    E = m.ETAPAS
    por = {e["k"]: n for n, e in enumerate(E)}
    seq, n, visto = [], 0, set()
    while 0 <= n < len(E) and n not in visto:
        visto.add(n); e = E[n]; seq.append(e)
        if e["t"] == "bifurcacao": n = por.get(e["caminhos"][0]["vai"], -1)
        elif e["t"] == "desfecho": n = por.get(e.get("fecho"), -1) if e.get("fecho") else -1
        elif e.get("rota"): n = por.get(e["rota"]["entao"], -1)
        elif e.get("conforme"): n = por.get(e["conforme"]["para"][0], -1)
        elif e.get("segue"): n = por.get(e["segue"], -1)
        else: n += 1
    imgs = set()
    def varrer(v):
        if isinstance(v, dict):
            for k, x in v.items():
                if k in ("img", "fundo") and isinstance(x, str) and x: imgs.add(x)
                else: varrer(x)
        elif isinstance(v, (list, tuple)):
            for x in v: varrer(x)
        elif isinstance(v, str):
            imgs.update(re.findall(r'data-img="([^"]+)"', v))
    varrer(E)
    imgs = {x for x in imgs if not x.startswith("cena")}
    return {"perg": sum(e["t"] in ("pergunta", "pareamento") for e in seq),
            "dec": sum(e["t"] == "bifurcacao" for e in seq),
            "fins": sum(e["t"] == "desfecho" for e in E),
            "imgs": len(imgs), "paginas": len(seq),
            "corv": getattr(m, "COR", "")}


def caso(*, slug, titulo, subtitulo, especialidade, minutos, decisoes,
         desfechos, nivel, cor, capa="", arquivo="", pronto=True,
         resumo="") -> dict:
    if cor not in CORES:
        raise ValueError(f"cor desconhecida: {cor!r}; use {sorted(CORES)}")
    if nivel not in ("interno", "residente", "os dois"):
        raise ValueError("nível: 'interno', 'residente' ou 'os dois'")
    return {"slug": slug, "tt": texto(titulo), "sub": texto(subtitulo),
            "esp": texto(especialidade), "min": minutos, "dec": decisoes,
            "des": desfechos, "niv": nivel, "cor": CORES[cor],
            "capa": capa, "arq": arquivo, "pronto": 1 if pronto else 0,
            "resumo": texto(resumo), **_contar(slug)}


def montar(*, titulo, subtitulo, casos, img_dir: Path, rodape="") -> str:
    raiz = Path(__file__).parent
    css = (raiz / "biblioteca.css").read_text(encoding="utf-8")
    js = (raiz / "biblioteca.js").read_text(encoding="utf-8")

    cache: dict[str, str] = {}

    def embutir(nome: str) -> str:
        if not nome:
            return ""
        if nome not in cache:
            caminho = img_dir / nome
            if not caminho.exists():
                raise FileNotFoundError(f"capa não encontrada: {caminho}")
            dados = caminho.read_bytes()
            tipo = mimetypes.guess_type(nome)[0] or "image/jpeg"
            # A cena vem em PNG de 2 MB; no cartão ela ocupa 420 px. Uma
            # miniatura em JPEG leva a biblioteca de 13 MB para menos de 1.
            if len(dados) > 250_000:
                import subprocess, tempfile
                mini = Path(tempfile.gettempdir()) / ("capa_" + caminho.parent.parent.name + ".jpg")
                subprocess.run(["sips", "-Z", "960", "-s", "format", "jpeg", "-s",
                                "formatOptions", "72", str(caminho), "--out", str(mini)],
                               capture_output=True, check=True)
                dados, tipo = mini.read_bytes(), "image/jpeg"
            cache[nome] = ("data:" + tipo + ";base64," + base64.b64encode(dados).decode())
        return cache[nome]

    dados = {"titulo": titulo, "subtitulo": texto(subtitulo),
             "rodape": texto(rodape),
             "casos": [dict(c, capa=embutir(c["capa"])) for c in casos]}

    return (
        '<!doctype html>\n<html lang="pt-BR">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width,initial-scale=1">\n'
        f"<title>{titulo}</title>\n<style>\n{css}\n</style>\n</head>\n"
        '<body>\n<header id="topo"></header>\n<main id="grade"></main>\n'
        '<footer id="rodape"></footer>\n'
        '<script type="application/json" id="dados">'
        + json.dumps(dados, ensure_ascii=False).replace("</", "<\\/")
        + f"</script>\n<script>\n{js}\n</script>\n</body>\n</html>\n"
    )

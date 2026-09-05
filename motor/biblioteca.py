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
            "resumo": texto(resumo)}


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
            tipo = mimetypes.guess_type(nome)[0] or "image/jpeg"
            cache[nome] = ("data:" + tipo + ";base64,"
                           + base64.b64encode(caminho.read_bytes()).decode())
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

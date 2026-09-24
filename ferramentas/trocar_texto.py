"""Troca um texto de alternativa no .py do caso, mesmo quando o literal está
quebrado em várias strings concatenadas. Uso: from ferramentas.trocar_texto import trocar"""
import io, tokenize, textwrap
from pathlib import Path


def _literal(txt, recuo):
    partes = textwrap.wrap(txt, 66, drop_whitespace=False, break_on_hyphens=False)
    q = "'" if "'" not in txt else '"'
    return ('\n' + ' ' * recuo).join(q + p_.replace('\\', '\\\\') + q for p_ in partes)


def trocar(caminho, pares):
    caminho = Path(caminho)
    fonte = caminho.read_text()
    linhas = fonte.splitlines(keepends=True)
    inicio = [0]
    for l in linhas: inicio.append(inicio[-1] + len(l))
    off = lambda pos: inicio[pos[0] - 1] + pos[1]
    toks = list(tokenize.generate_tokens(io.StringIO(fonte).readline))
    corridas, atual = [], []
    for t in toks:
        if t.type == tokenize.STRING:
            atual.append(t)
        elif t.type in (tokenize.NL, tokenize.COMMENT) or (t.type == tokenize.NEWLINE and not atual):
            continue
        else:
            if atual: corridas.append(atual)
            atual = []
    if atual: corridas.append(atual)
    trocas, faltou = [], []
    for velho, novo in pares:
        achou = False
        for c in corridas:
            try:
                valor = ''.join(eval(t.string) for t in c)
            except Exception:
                continue
            if valor == velho:
                trocas.append((off(c[0].start), off(c[-1].end), _literal(novo, c[0].start[1])))
                achou = True
                break
        if not achou: faltou.append(velho[:60])
    for a, b, novo in sorted(trocas, reverse=True):
        fonte = fonte[:a] + novo + fonte[b:]
    caminho.write_text(fonte)
    return len(trocas), faltou

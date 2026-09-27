"""Nome público de cada caso: o endereço que o aluno vê.

O nome do módulo (pasta em casos/) é o diagnóstico, e o endereço não pode
ser. Aqui cada caso ganha um nome tirado do título. Os endereços antigos
viram páginas de redirecionamento (ver `publicar_local`).
"""
from pathlib import Path

PUBLICO = {
    'pulmao_rim': 'o-sangue-que-nao-saiu',
    'cocaina_levamisol': 'a-flor-da-pele',
    'west_nile': 'o-peso-dos-dias',
    'kikuchi': 'o-que-ficou-no-pescoco',
    'sarcoidose': 'entre-a-sede-e-o-folego',
    'leptospirose': 'febre-de-abril',
    'endocardite': 'pequenos-sinais',
    'adrenal': 'oito-meses-de-cansaco',
    'cmv': 'depois-da-travessia',
}

RAIZ = Path(__file__).resolve().parent


def arquivo(modulo):
    return PUBLICO[modulo] + '.html'


def publicar_local():
    """Copia cada saida/<modulo>-etapas.html para o nome público e deixa no
    nome antigo um redirecionamento, para links já compartilhados."""
    for mod, nome in PUBLICO.items():
        src = RAIZ / 'saida' / (mod.replace('_', '-') + '-etapas.html')
        (RAIZ / (nome + '.html')).write_bytes(src.read_bytes())
        antigo = RAIZ / (mod.replace('_', '-') + '.html')
        antigo.write_text(
            '<!doctype html><meta charset="utf-8"><title>Casos clínicos</title>'
            '<meta name="robots" content="noindex">'
            f'<meta http-equiv="refresh" content="0;url={nome}.html">'
            f'<script>location.replace("{nome}.html"+location.hash)</script>'
            f'<a href="{nome}.html">Abrir o caso</a>', encoding='utf-8')
    (RAIZ / 'index.html').write_bytes((RAIZ / 'saida' / 'biblioteca.html').read_bytes())


if __name__ == '__main__':
    publicar_local()
    print('publicado localmente:', ', '.join(arquivo(m) for m in PUBLICO))

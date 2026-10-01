"""Ritmo do caso: quanto é conteúdo e quanto é pergunta, no caminho padrão.

Imprime a sequência de telas (C = conteúdo, I = imagem, E = exames, P = pergunta,
M = pareamento, B = decisão, F = desfecho) e mede: número de perguntas, razão
conteúdo/interação, maior sequência de telas interativas sem conteúdo entre elas,
e as perguntas da primeira metade com as alternativas (para conferir se só
classificam, localizam ou interpretam, sem nomear doença ou exame específico).

Uso:  python3 ferramentas/ritmo.py [slug ...] [--alts]
"""
import importlib, re, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]; sys.path.insert(0, str(ROOT)); sys.path.insert(0, str(ROOT / 'ferramentas'))
from pistas import rota
TAG = re.compile(r'<[^>]+>')
LETRA = {'pergunta': 'P', 'pareamento': 'M', 'bifurcacao': 'B', 'desfecho': 'F', 'resultados': 'E', 'capa': '·'}
INTER = {'P', 'M', 'B'}
# Metas (pedido do Matheus em 30/09: "mais slides de conteúdo e menos de perguntas")
MAX_PERGUNTAS, MIN_RAZAO, MAX_SEGUIDAS = 6, 2.0, 1

def letra(e):
    if e['t'] in LETRA: return LETRA[e['t']]
    return 'I' if 'vv-estudo' in str(e) else 'C'

def medir(slug, alts=False):
    m = importlib.import_module('casos.' + slug + '.etapas'); r = rota(m.ETAPAS)
    seq = ''.join(letra(e) for e in r)
    n_int = sum(c in INTER for c in seq); n_cont = sum(c in 'CIE' for c in seq)
    n_perg = sum(c in 'PM' for c in seq)
    run = max((len(x) for x in re.findall('[PMB]+', seq)), default=0)
    ok = n_perg <= MAX_PERGUNTAS and n_cont >= MIN_RAZAO * n_int and run <= MAX_SEGUIDAS
    print(f"{'OK  ' if ok else 'REVER'} {slug:18} perguntas {n_perg}  interativas {n_int}  conteúdo {n_cont}"
          f"  razão {n_cont / max(1, n_int):.1f}  seguidas {run}\n      {seq}")
    if alts:
        for n, e in enumerate(r[:len(r) // 2]):
            if e['t'] == 'pergunta':
                print(f"      [{n}] {TAG.sub('', e.get('enunciado', ''))[:110]}")
                print('          ' + ' | '.join(TAG.sub('', a['t']) for a in e['alts']))
    return ok

if __name__ == '__main__':
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    from nomes_publicos import PUBLICO
    slugs = args or [s for s in PUBLICO if (ROOT / 'casos' / s / 'etapas.py').exists()]
    ruins = [s for s in slugs if not medir(s, '--alts' in sys.argv)]
    sys.exit(1 if ruins else 0)

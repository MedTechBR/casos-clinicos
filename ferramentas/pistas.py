"""Quando o diagnóstico aparece e quanto pesam os comentários.

Percorre o caminho padrão de cada caso (primeira opção em cada decisão) e
informa: em que página, e em que fração do percurso, o nome do diagnóstico
aparece pela primeira vez; onde ele aparece (enunciado, alternativa,
comentário, título da resposta, página); e o tamanho dos comentários das
alternativas. No molde do //New England//, o nome não deve surgir antes do
meio do caso, e nunca num comentário de alternativa antes da virada.

Uso:  python3 ferramentas/pistas.py [slug ...]
"""
import importlib, json, re, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]; sys.path.insert(0, str(ROOT))

DX = {
 'pulmao_rim': r'granulomatose com poliangi|\bGPA\b|poliangiite microsc|vasculite associada|\bANCA\b|Wegener',
 'cocaina_levamisol': r'levamisol',
 'west_nile': r'Nilo Ocidental|West Nile|flavivír',
 'kikuchi': r'Kikuchi|necrosante histioc',
 'sarcoidose': r'sarcoid|Löfgren|Lofgren|Heerfordt',
 'cmv': r'citomegalo|\bCMV\b|olho de coruja',
 'leptospirose': r'leptosp|\bWeil\b',
 'endocardite': r'endocardite|vegeta[çc]|\bDuke\b',
 'adrenal': r'adrenal|Addison|hidrocortisona|cortisol|ACTH',
}
TAG = re.compile(r'<[^>]+>')

def textos(e):
    """(onde, texto) de uma etapa."""
    t = e['t']; out = []
    def add(onde, s):
        if isinstance(s, str) and s.strip(): out.append((onde, TAG.sub(' ', s)))
    for c in ('tt', 'kicker', 'corpo', 'enunciado', 'intro', 'nota', 'tr', 'sobre', 'fecho_txt'):
        add(c, e.get(c) if not isinstance(e.get(c), dict) else json.dumps(e.get(c), ensure_ascii=False))
    for a in e.get('alts', []):
        add('alternativa', a.get('t')); add('comentário', a.get('c'))
    for it in e.get('itens', []):
        add('pareamento', json.dumps(it, ensure_ascii=False))
    for o in e.get('opcoes', []) if isinstance(e.get('opcoes'), list) else []:
        add('pareamento', o if isinstance(o, str) else json.dumps(o, ensure_ascii=False))
    for c in e.get('caminhos', []):
        add('caminho', json.dumps(c, ensure_ascii=False))
    if t == 'resultados':
        add('resultado', json.dumps(e.get('todos', ''), ensure_ascii=False))
        add('resultado', json.dumps(e.get('laminas', ''), ensure_ascii=False))
    if t not in ('pergunta',):
        rest = {k: v for k, v in e.items() if k not in ('alts', 'caminhos', 'itens')}
        add('outros', json.dumps(rest, ensure_ascii=False))
    return out

def rota(steps):
    por = {e['k']: i for i, e in enumerate(steps)}; i = 0; vistos = []
    while i is not None and i < len(steps) and steps[i]['k'] not in vistos:
        e = steps[i]; vistos.append(e['k'])
        if e['t'] == 'desfecho': break
        if e.get('caminhos'): i = por[e['caminhos'][0]['vai']]; continue
        c = e.get('conforme')
        if c: i = por[c[1][0]] if isinstance(c, (list, tuple)) else i + 1; continue
        i = por[e['segue']] if e.get('segue') else i + 1
    return [steps[por[k]] for k in vistos]

def analisar(slug):
    m = importlib.import_module('casos.' + slug + '.etapas'); r = rota(m.ETAPAS)
    pat = re.compile(DX[slug], re.I); primeira = None; locais = []
    for n, e in enumerate(r):
        for onde, s in textos(e):
            if pat.search(s):
                locais.append((n, e['k'], onde))
                if primeira is None: primeira = (n, e['k'], onde)
    coms = [len(a['c'].split()) for e in r if e['t'] == 'pergunta' for a in e.get('alts', []) if a.get('c')]
    pergs = [n for n, e in enumerate(r) if e['t'] in ('pergunta', 'pareamento')]
    return dict(paginas=len(r), primeira=primeira,
                fracao=round(primeira[0] / len(r), 2) if primeira else None,
                antes_do_meio=sorted({(n, k, o) for n, k, o in locais if n < len(r) / 2}),
                palavras_por_comentario=round(sum(coms) / max(1, len(coms)), 1),
                maior_comentario=max(coms) if coms else 0, perguntas_em=pergs)

CORTE = 0.45          # fração do percurso antes da qual o nome não aparece
MEDIA_MAX, MAX_COMENT = 16, 26

def conferir(slug, a):
    """Regras: antes do corte, o nome só pode aparecer como TEXTO de
    alternativa, e numa única pergunta (o diferencial). Comentários curtos."""
    m = importlib.import_module('casos.' + slug + '.etapas'); r = rota(m.ETAPAS)
    pat = re.compile(DX[slug], re.I); corte = len(r) * CORTE; falhas = []
    pergs_com_nome = set()
    for n, e in enumerate(r):
        if n >= corte: break
        for onde, s in textos(e):
            if not pat.search(s): continue
            if onde == 'alternativa': pergs_com_nome.add(e['k'])
            elif onde != 'outros' or e['t'] != 'pergunta':
                falhas.append(f'pág {n} {e["k"]}: nome em {onde}')
    if len(pergs_com_nome) > 1: falhas.append(f'nome como alternativa em {sorted(pergs_com_nome)} antes do corte')
    if a['palavras_por_comentario'] > MEDIA_MAX: falhas.append(f'comentários longos: média {a["palavras_por_comentario"]}')
    if a['maior_comentario'] > MAX_COMENT: falhas.append(f'comentário com {a["maior_comentario"]} palavras')
    return sorted(set(falhas))

if __name__ == '__main__':
    for slug in (sys.argv[1:] or list(DX)):
        a = analisar(slug)
        f = conferir(slug, a)
        print(('OK   ' if not f else 'FALHA'), slug)
        for x in f: print('      ', x)
        print(f"{slug:18} pág {a['paginas']:2}  1ª menção: {a['primeira']}  ({a['fracao']})  "
              f"coment {a['palavras_por_comentario']} pal (máx {a['maior_comentario']})")
        for x in a['antes_do_meio']: print('     antes do meio:', x)

"""Atalhos de autoria para casos sindrômicos. Sem regras clínicas no motor."""
from motor.etapas import pagina, pergunta, alt, op, p, desfecho, vitais as _vitais

def pg(k, titulo, *textos, segue='', conforme=None):
    if isinstance(conforme, dict):
        conforme=(conforme['de'], conforme['para'])
    return pagina(k, titulo, '', *(p(t) for t in textos), so_kicker=True,
                  segue=segue, conforme=conforme)

def Q(k, numero, enunciado, opcoes, explicacao, segue=''):
    return pergunta(k, f'Pergunta {numero}', enunciado,
        [alt(t, certa=ok) for t, ok in opcoes], explicacao=explicacao, segue=segue)

def ex(nome, valor, ref='—', alt_=False):
    return op(nome, resultado=valor, referencia=ref, alterado=alt_)

def fim(k, titulo, textos, porque, qualidade='medio', fecho='retrospectiva'):
    return desfecho(k, titulo, *(p(t) for t in textos), porque=porque,
                    qualidade=qualidade, fecho=fecho)

def vitais(*pares):
    return _vitais(*(tuple(p) if len(p)==3 else (*p,False) for p in pares))

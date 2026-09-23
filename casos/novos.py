"""Convenções de autoria dos casos adicionados em setembro de 2026."""
from motor.etapas import p, pagina, pergunta, alt, painel, op, bifurcacao, caminho, desfecho

def pg(k, titulo, *textos, segue=''):
    return pagina(k, titulo, '', *(p(t) for t in textos), so_kicker=True, segue=segue)

def q(k, n, enunciado, itens):
    return pergunta(k, f'Pergunta {n}', enunciado,
        [alt(t, c, certa=ok) for t, ok, c in itens], titulo_resposta='Discussão')

def labs(k, titulo, linhas, intro=''):
    return painel(k, 'Investigação', titulo,
        [op(n, resultado=v, referencia=r, alterado=a) for n,v,r,a in linhas], introducao=intro)

def bif(k, texto, opcoes):
    return bifurcacao(k, 'Decisão clínica', 'Conduta', texto,
        [caminho(t, dest, motivo) for t,dest,motivo in opcoes])

def fim(k, titulo, texto, motivo, qualidade):
    return desfecho(k, titulo, p(texto), qualidade=qualidade, porque=motivo, fecho='retrospectiva')

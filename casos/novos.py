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


def substituir(etapas, k, *novas):
    i=next(i for i,e in enumerate(etapas) if e['k']==k)
    etapas[i:i+1]=list(novas)


def antes(etapas, k, *novas):
    """Insere uma alíquota preservando entradas por saltos e ramos."""
    primeiro=novas[0]['k']
    for e in etapas:
        for attr in ('segue','fecho'):
            if e.get(attr)==k:e[attr]=primeiro
        for c in e.get('caminhos',[]):
            if c['vai']==k:c['vai']=primeiro
    i=next(i for i,e in enumerate(etapas) if e['k']==k)
    etapas[i:i]=list(novas)


def imagem(k, titulo, contexto, arquivo, legenda, credito, leitura, pontos=()):
    """Exame e contexto juntos; leitura e setas só após ação do apresentador."""
    from motor.desenhos import anotada, seta
    from html import escape
    fig=anotada(arquivo,*[seta(a,r,str(n+1)) for n,(a,r) in enumerate(pontos)],legenda=legenda,credito=credito)
    corpo=('<div class="observacao-imagem figura-discussao">'+p(contexto)
           +'<div class="estudo-imagem">'+fig+'</div>'
           +'<details class="leitura-imagem"><summary>Revelar leitura e marcações</summary>'
           +''.join(p(t) for t in leitura)+'</details></div>')
    return pagina(k,'Discussão de exame',titulo,corpo)


def referencia_imagem(meta):
    import json
    from pathlib import Path
    m=json.loads(Path(meta).read_text())
    version=m['licenca'].split()[-1]
    return (m['autor']+' · <a href="'+m['fonte']+'" target="_blank" rel="noopener">Fonte</a> · '
            +'<a href="https://creativecommons.org/licenses/by-sa/'+version+'/" target="_blank" rel="noopener">'
            +m['licenca']+'</a>. Setas editoriais sob a mesma licença; arquivo sem recorte adicional.')

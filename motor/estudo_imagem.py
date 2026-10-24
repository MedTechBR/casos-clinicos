"""Discussão de imagem num slide só.

A figura fica à direita, do tamanho exato da imagem, sem faixas laterais. À
esquerda, o contexto e um botão: ao abri-lo, as setas se desenham sobre a
figura, cada achado aparece numerado ao lado da seta de mesmo número e, logo
depois, o laudo. Nada muda de página, e quem apresenta controla o momento.
"""
from .etapas import pagina, p
from .desenhos import anotada, seta


def estudo(ident, titulo, contexto, arquivo, legenda, credito, achados, laudo, *,
           kicker='Discussão de imagem', fundo='', segue='', botao='Mostrar os achados'):
    """`achados`: (alvo, rótulo, texto) ou (alvo, rótulo, texto, curva).

    Alvo e rótulo em milésimos da largura da imagem (ver `desenhos.seta`). O
    texto de cada achado descreve o que a seta de mesmo número aponta; o laudo
    é a leitura de conjunto, uma frase ou uma lista delas.
    """
    setas = [seta(a[0], a[1], str(n + 1), curva=a[3] if len(a) > 3 else 12)
             for n, a in enumerate(achados)]
    figura = anotada(arquivo, *setas, legenda=legenda, credito=credito)
    itens = ''.join('<li data-n="%d" style="--n:%d"><span class="vv-num">%d</span><div>%s</div></li>'
                    % (n + 1, n, n + 1, p(a[2])) for n, a in enumerate(achados))
    laudos = [laudo] if isinstance(laudo, str) else list(laudo)
    corpo = ('<div class="observacao-imagem figura-discussao vv-estudo" style="--q:%d">' % len(achados)
             + '<div class="vv-est-txt">' + p(contexto)
             + '<details class="leitura-imagem vv-est-rev"><summary>' + botao + '</summary>'
             + '<ol class="vv-achados">' + itens + '</ol>'
             + '<div class="vv-laudo" style="--q:%d"><b>Laudo</b>' % len(achados) + ''.join(p(t) for t in laudos) + '</div>'
             + '</details></div>'
             + '<div class="vv-est-fig">' + figura + '</div></div>')
    return pagina(ident, kicker, titulo, corpo, fundo=fundo, segue=segue)


def sequencia(ident, titulo, contexto, arquivo, credito, legenda, achados, laudo, junto=False):
    """Mantida pelo nome: agora devolve um slide só (ver `estudo`)."""
    return [estudo(ident, titulo, contexto, arquivo, legenda, credito, achados, laudo)]


def inserir_antes(etapas, destino, novas):
    """Inclui a sequência também quando há saltos explícitos para o destino."""
    ids = {e['k'] for e in etapas}
    assert destino in ids and not ids.intersection(e['k'] for e in novas)
    for e in etapas:
        if e.get('segue') == destino:
            e['segue'] = novas[0]['k']
    idx = next(i for i, e in enumerate(etapas) if e['k'] == destino)
    etapas[idx:idx] = novas


def ecg(ident, contexto, img, discussao):
    return sequencia(ident, 'Eletrocardiograma', contexto, img / 'ecg_taquicardia.jpg',
        'Ewingdo · Wikimedia Commons · CC BY-SA 4.0. Setas adicionadas sob a mesma licença.',
        'Traçado ilustrativo de outro paciente; não é um registro deste caso. 25 mm/s; 10 mm/mV.',
        [((579, 386), (520, 300), '**S profunda em V3**: voltagem precordial elevada.', -12),
         ((832, 238), (920, 310), '**R alta em V6**, compondo o padrão de grandes voltagens.', 12),
         ((596, 159), (470, 92), '**T proeminente em V2**; também chama atenção em V3–V4.', 8)],
        ['Taquicardia regular, provável origem sinusal, cerca de 125 bpm; '
         'QRS estreito. Altas voltagens, T anteriores proeminentes e discreto '
         'desnível de J/ST lateral.',
         'Correlacionar com clínica, eletrólitos e ECG prévio; não concluir '
         'hipertrofia ou isquemia pela imagem isolada. Os achados deste '
         'traçado comparativo não são automaticamente do paciente ficcional.', discussao])

"""Duas páginas: observar um exame da evolução e discutir seus pontos visíveis."""
from .etapas import pagina, p
from .desenhos import anotada, seta


def sequencia(ident, titulo, contexto, arquivo, credito, legenda, pontos, discussao):
    """Pontos em coordenadas proporcionais da imagem original; não alteram o arquivo."""
    def quadro(anotacoes=(), notas=()):
        figura = anotada(arquivo, *anotacoes, legenda=legenda, credito=credito)
        coluna = '<aside>' + ''.join(p(t) for t in notas) + '</aside>' if notas else ''
        return '<div class="estudo-imagem">' + figura + coluna + '</div>'
    return [
        pagina(ident, 'Evolução', titulo, p(contexto), quadro()),
        pagina(ident + '_leitura', 'Discussão de imagem', titulo,
               quadro([seta(a, r, str(n + 1)) for n, (a, r) in enumerate(pontos)], discussao)),
    ]


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
        'Ewingdo · Wikimedia Commons · CC BY-SA 4.0. Setas adicionadas na discussão sob a mesma licença.',
        'Traçado ilustrativo de outro paciente; não é um registro deste caso. 25 mm/s; 10 mm/mV.',
        [((110, 408), (80, 350)), ((157, 405), (195, 350))],
        ['1 e 2. Dois complexos QRS consecutivos na tira longa de II. Compare a distância entre eles com os demais intervalos RR.',
         'O traçado ilustra taquicardia sinusal, cerca de 125 bpm, com QRS estreitos e ritmo regular. A identificação do ritmo exige avaliar também a atividade atrial nas demais derivações.', discussao])

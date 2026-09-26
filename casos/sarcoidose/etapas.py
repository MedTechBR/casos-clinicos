"""Sarcoidose com hipercalcemia por calcitriol, lesão renal e uveíte anterior.

Alíquota → pergunta, no molde dos casos interativos do //New England//. Oito
perguntas no percurso, uma rodada de exames com gabarito e painel, um
pareamento dos mecanismos de hipercalcemia e duas decisões de conduta com
consequência. Paciente ficcional.

Condução: a hipercalcemia com PTH suprimido e depois o calcitriol alto são
investigados com diferencial amplo (PTHrP, linfoma, micobactéria, fungo,
vitamina D, mieloma, leite-álcali). O nome só entra no diferencial da
tomografia e se firma depois do tecido. A queixa ocular e a história de
exposição vêm em alíquotas posteriores.
"""
from pathlib import Path

from motor.estudo_imagem import estudo

from motor.etapas import (alt, bifurcacao, caminho, capa, desfecho, op, p,
                          pagina, painel, par, pareamento, pergunta, tabela,
                          topicos, vitais, lamina)
from casos.novos import imagem, referencia_imagem

TITULO = 'Entre a sede e o fôlego'
RODAPE = 'Paciente ficcional · evoluções simuladas para ensino'
COR = '#0d9488'
IMG = Path(__file__).parent / 'img'
BANCO = []
CENA = 'cena.png'


def pg(k, titulo, *textos, segue=''):
    return pagina(k, titulo, '', *(p(t) for t in textos), so_kicker=True, segue=segue)


def Q(k, n, enunciado, itens, titulo, segue=''):
    return pergunta(k, f'Pergunta {n}', enunciado,
                    [alt(t, c, certa=ok) for t, c, ok in itens],
                    titulo_resposta=titulo, segue=segue)


def ex(nome, valor, ref='—', alt_=False):
    return op(nome, resultado=valor, referencia=ref, alterado=alt_)


def fim(k, titulo, texto, porque, qualidade):
    return desfecho(k, titulo, p(texto), qualidade=qualidade, porque=porque,
                    fecho='retrospectiva')


def sem_setas(meta):
    return referencia_imagem(meta).replace(
        'Setas editoriais sob a mesma licença; arquivo sem recorte adicional.',
        'Sem setas ou recorte adicional.')


def credito_curto(meta):
    """Autor e licença, sem o link da fonte: o nome do arquivo no Commons
    diz o diagnóstico. A fonte completa fica na última tela."""
    import json
    m = json.loads(Path(meta).read_text())
    versao = m['licenca'].split()[-1]
    return (m['autor'] + ' · Wikimedia Commons · '
            '<a href="https://creativecommons.org/licenses/by-sa/' + versao
            + '/" target="_blank" rel="noopener">' + m['licenca'] + '</a>. '
            'Setas editoriais sob a mesma licença; fonte completa na última tela.')


def _fonte(meta, rotulo):
    import json
    m = json.loads(Path(meta).read_text())
    return '<a href="' + m['fonte'] + '" target="_blank" rel="noopener">' + rotulo + '</a>'


ETAPAS = [
    capa(TITULO, fundo=CENA, kicker='Caso interativo',
         selo='Paciente ficcional · procedência e créditos na última tela'),

    pg('historia', 'Apresentação',
       'Rafael, 41 anos, analista administrativo, é trazido pela esposa ao '
       'pronto-socorro por náuseas, intestino preso há cinco dias e '
       'dificuldade para se concentrar. Há uma semana bebe água o tempo todo e '
       'acorda três vezes à noite para urinar.',
       'Antes disso, vinha encurtando as caminhadas do fim de semana por '
       'cansaço. Atribuiu ao trabalho, assim como uma tosse seca que começou '
       'há dois meses e vai e volta.'),

    pg('hda', 'História da doença atual',
       'A tosse não tem catarro nem sangue. Subir dois lances de escada deixa '
       'Rafael sem fôlego, sem ortopneia e sem dor no peito. Não mediu febre. '
       'Perdeu 4 kg em oito semanas. A sede veio antes das náuseas.',
       'Nega vômitos repetidos, diarreia e cólica renal. Não teve desmaio nem '
       'palpitação. Não notou caroços no pescoço nem suor noturno.'),

    pg('antecedentes', 'Antecedentes',
       'Hipertenso há cinco anos, usa hidroclorotiazida 25 mg/dia. Há três '
       'meses, por conta própria, começou colecalciferol 5.000 UI/dia porque '
       'ouviu que "dava disposição". Não usa carbonato de cálcio, lítio nem '
       'antiácido.',
       'Nunca teve cálculo renal. Não fuma e bebe pouco. Não conhece contato '
       'com tuberculose e nunca viajou para fora do Nordeste. O pai teve '
       'câncer de próstata aos 70 anos.'),

    pagina('exame', 'Exame físico', '',
           vitais(('Pressão arterial', '104/66', True), ('Frequência cardíaca', '102', True),
                  ('Frequência respiratória', '20', False), ('Temperatura', '36,8 °C', False),
                  ('SpO₂ em ar ambiente', '95%', False)),
           topicos(('Estado geral', 'Desidratado, orientado, com atenção lenta; sem déficit focal.'),
                   ('Cardiovascular', 'Ritmo regular, sem sopros, sem turgência jugular.'),
                   ('Respiratório', 'Murmúrio presente, raros estertores finos nas bases.'),
                   ('Abdome', 'Ruídos diminuídos, indolor, sem massas nem visceromegalias.'),
                   ('Linfonodos', 'Sem adenomegalia cervical, axilar ou inguinal palpável.'),
                   ('Pele e membros', 'Sem edema, sem lesões cutâneas, sem sinovite.')),
           so_kicker=True),

    painel('res0', 'Na chegada', 'A bancada da emergência', [
        ex('Cálcio total', '13,6 mg/dL', '8,5–10,5 mg/dL', True),
        ex('Albumina', '4,0 g/dL', '3,5–5,0 g/dL'),
        ex('Cálcio ionizado', '1,72 mmol/L', '1,12–1,32 mmol/L', True),
        ex('Creatinina', '2,0 mg/dL {{(1,0 há um ano)}}', '0,7–1,3 mg/dL', True),
        ex('Ureia', '72 mg/dL', '15–45 mg/dL', True),
        ex('Sódio / potássio / bicarbonato', '143 / 3,5 / 25 mmol/L', '135–145 / 3,5–5,0 / 22–28'),
        ex('Glicemia', '98 mg/dL', '70–99 mg/dL'),
        ex('Hemoglobina', '12,8 g/dL', '13,5–17,5 g/dL', True),
        ex('Eletrocardiograma', 'Ritmo sinusal, 102 bpm · QT corrigido curto (360 ms)', '—', True),
    ], introducao='A equipe colhe bioquímica, gasometria venosa e ECG antes de qualquer outra coisa.'),

    Q('p1', 1,
      'Cálcio de 13,6 mg/dL, sintomas neurológicos e creatinina que dobrou. '
      '**Quais três** medidas são prioritárias agora?', [
      ('Soro fisiológico com meta de diurese',
       'A hipercalcemia causa poliúria e desidratação; sem volume, o rim não '
       'excreta cálcio.', True),
      ('Furosemida antes de repor volume',
       'Aumenta a calciúria só com volume restaurado; antes disso, agrava a '
       'desidratação e o rim.', False),
      ('Suspender tiazídico e colecalciferol',
       'O tiazídico retém cálcio no túbulo e a vitamina D aumenta a absorção '
       'intestinal.', True),
      ('Dosar o PTH junto com o cálcio',
       'Separa as hipercalcemias em dois grupos: PTH alto ou inapropriado, e '
       'PTH suprimido.', True),
      ('Hemodiálise de urgência pela creatinina',
       'Reservada à hipercalcemia refratária ou à oligúria que impede volume; '
       'ainda não é o caso.', False),
      ('Restrição hídrica pela poliúria',
       'A poliúria é consequência do cálcio; restringir água piora a '
       'desidratação e a creatinina.', False),
      ('Prednisona empírica já na emergência',
       'Sem causa definida, pode mascarar linfoma e agravar infecção; não '
       'substitui o volume.', False),
      ('Denosumabe antes de hidratar',
       'Não corrige a desidratação e, sem causa conhecida, arrisca '
       'hipocalcemia prolongada depois.', False),
     ], 'Volume, retirar o que soma e dosar o PTH'),

    pg('evolucao1', 'Primeiras 24 horas',
       'Com soro e sem as duas medicações, Rafael fica mais atento. O cálcio '
       'cai para 12,4 mg/dL e a creatinina para 1,6 mg/dL. O PTH é **6 '
       'pg/mL** (referência 15–65).',
       'A melhora parcial não explica a causa. A tosse, a perda de peso e o '
       'fôlego curto continuam sem explicação.'),

    Q('ex2', 2,
      'Hipercalcemia com PTH suprimido. **Quais quatro** exames são os '
      'mais apropriados agora?', [
      ('Peptídeo relacionado ao PTH (PTHrP)',
       'Mediador da hipercalcemia humoral maligna, a causa mais comum de '
       'hipercalcemia grave em internados.', True),
      ('Cintilografia com sestamibi das paratireoides',
       'Localiza adenoma de paratireoide, e um PTH de 6 pg/mL afasta '
       'hiperparatireoidismo.', False),
      ('25-hidroxivitamina D e 1,25-di-hidroxivitamina D',
       'A primeira mede o estoque; a segunda, a forma ativa, que pode ser '
       'produzida fora do rim.', True),
      ('Eletroforese de proteínas com cadeias leves livres',
       'Mieloma causa hipercalcemia por osteólise, com PTH baixo e lesão '
       'renal.', True),
      ('Radiografia de tórax',
       'Tosse há dois meses, perda de peso e estertores pedem imagem do '
       'tórax.', True),
      ('Cintilografia óssea',
       'Não capta bem a lesão lítica do mieloma e não é o primeiro passo com '
       'PTH suprimido.', False),
      ('Tomografia de crânio pela confusão',
       'A confusão tem causa metabólica e melhorou com volume; imagem não '
       'muda a conduta.', False),
      ('Calcitonina sérica',
       'Marcador de carcinoma medular de tireoide; não explica '
       'hipercalcemia.', False),
      ('Ultrassonografia cervical das paratireoides',
       'Mesma lógica do sestamibi: com PTH suprimido, não há adenoma a '
       'procurar.', False),
     ], 'PTH baixo manda procurar PTHrP, vitamina D, paraproteína e o tórax'),

    painel('res2', 'Investigação', 'O que a equipe pediu', [
        ex('PTHrP', 'Não detectado', 'não detectado'),
        ex('25-hidroxivitamina D', '38 ng/mL', '20–50 ng/mL'),
        ex('1,25-di-hidroxivitamina D', '104 pg/mL', '18–72 pg/mL', True),
        ex('Eletroforese de proteínas', 'Sem componente monoclonal · gamaglobulina policlonal discretamente elevada', 'sem pico'),
        ex('Cadeias leves livres', 'Relação kappa/lambda 1,3', '0,26–1,65'),
        ex('Fósforo', '3,6 mg/dL', '2,5–4,5 mg/dL'),
        ex('Calciúria de 24 horas', '410 mg', 'abaixo de 300 mg', True),
        ex('Radiografia de tórax', 'Hilos alargados dos dois lados · parênquima sem consolidação', '—', True),
    ], introducao='Clique na imagem para ampliar; o laudo abre no botão.',
       laminas={'Radiografia de tórax': lamina('rx_hilos.jpg', 'Radiografia de tórax, PA e perfil',
                'Imagem de outro paciente, usada para ilustrar o achado; não pertence a Rafael.',
                'Hellerhoff · Wikimedia Commons · CC BY-SA 4.0')}),

    pareamento('p3', 'Pergunta 3',
      'O 1,25-di-hidroxivitamina D está alto e o 25-hidroxi, normal. Associe '
      'cada perfil laboratorial ao mecanismo da hipercalcemia.', [
      par('PTH 95 pg/mL, fósforo 2,2 mg/dL, calciúria alta',
          'Hiperparatireoidismo primário',
          'O PTH reabsorve cálcio e espolia fósforo; é a causa mais comum no '
          'ambulatório.'),
      par('PTH 48 pg/mL, fração de excreção de cálcio abaixo de 0,01',
          'Hipercalcemia hipocalciúrica familiar',
          'O sensor de cálcio mal regulado mantém PTH normal e calciúria muito '
          'baixa.'),
      par('PTH suprimido, PTHrP alto, 1,25-(OH)₂D baixo',
          'Hipercalcemia humoral maligna',
          'O PTHrP imita o PTH no osso e no rim, mas não ativa a vitamina D.'),
      par('PTH suprimido, 1,25-(OH)₂D alto, 25-OH-D normal',
          'Produção extrarrenal de calcitriol',
          'É o perfil de Rafael: uma 1-alfa-hidroxilase fora do rim, que não '
          'obedece ao PTH.'),
      par('PTH suprimido, 25-OH-D de 180 ng/mL',
          'Intoxicação por vitamina D',
          'Exige doses muito altas por meses; o 25-OH de Rafael é 38.'),
      par('PTH suprimido, bicarbonato 34 mmol/L, carbonato de cálcio diário',
          'Síndrome leite-álcali',
          'Cálcio oral, alcalose e lesão renal se alimentam; o bicarbonato de '
          'Rafael é normal.'),
    ], opcoes=['Hiperparatireoidismo primário', 'Hipercalcemia hipocalciúrica familiar',
               'Hipercalcemia humoral maligna', 'Produção extrarrenal de calcitriol',
               'Intoxicação por vitamina D', 'Síndrome leite-álcali',
               'Mieloma múltiplo'],
    titulo_resposta='O calcitriol alto com estoque normal aponta para fora do rim',
    nota='A opção que sobrou, mieloma, teria paraproteína ou cadeias leves '
         'alteradas; as de Rafael são normais.'),

    estudo('rx_hilos', 'Radiografia de tórax',
           'Com o calcitriol alto, a equipe revê a radiografia. Observe os '
           'hilos nas incidências frontal e lateral antes de ler a descrição.',
           IMG / 'rx_hilos.jpg',
           'Radiografia frontal e lateral de outro paciente · comparação didática.',
           credito_curto(IMG / 'rx_hilos.jpg.json'),
        [
         ((176, 280), (70, 180), '**Hilo direito** aumentado, de contorno lobulado.', 12),
         ((353, 273), (470, 180), '**Hilo esquerdo** também aumentado: o alargamento é bilateral e simétrico.', -12),
         ((735, 315), (900, 240), 'Na incidência lateral, a **massa hilar** se sobrepõe à sombra cardíaca.', 12),
        ],
        ['Adenopatia hilar bilateral e simétrica, com parênquima pulmonar sem opacidades.',
         'O diferencial inclui linfoma, infecção granulomatosa, doença granulomatosa não infecciosa e metástase; a tomografia é o próximo passo.']),

    pg('tomografia', 'Tomografia de tórax',
       'Antes do exame, a residente refaz a história ocupacional. Rafael '
       'nunca trabalhou com pedra, areia, fundição ou metais. Há cinco meses, '
       'ajudou a limpar um galinheiro abandonado no sítio do sogro, no '
       'sertão.',
       'O laudo descreve linfonodos hilares e mediastinais bilaterais e '
       'simétricos, até 2,4 cm, **sem necrose central**, e pequenos nódulos ao '
       'longo dos feixes broncovasculares, das fissuras e da pleura. Sem '
       'cavitação e sem derrame. Nos cortes do abdome superior, fígado e baço '
       'de tamanho normal.'),

    Q('p4', 4,
      'Adenopatia hilar e mediastinal simétrica, nódulos perilinfáticos, '
      'calcitriol alto e um galinheiro há cinco meses. **Quais quatro** '
      'diagnósticos precisam ser considerados?', [
      ('Sarcoidose',
       'Adenopatia simétrica, nódulos perilinfáticos e calcitriol alto são '
       'compatíveis; o diagnóstico exige tecido.', True),
      ('Tuberculose',
       'Faz granuloma, linfonodo mediastinal e, raramente, calcitriol alto. '
       'No Brasil, excluí-la precede imunossupressão.', True),
      ('Linfoma',
       'Adenopatia mediastinal, perda de peso e calcitriol alto: o tecido '
       'linfomatoso também expressa 1-alfa-hidroxilase.', True),
      ('Histoplasmose',
       'Galinheiro é exposição típica; faz adenopatia mediastinal, granuloma '
       'e, às vezes, calcitriol alto.', True),
      ('Silicose',
       'Faz adenopatia com calcificação em casca de ovo, mas exige anos de '
       'exposição à sílica.', False),
      ('Beriliose crônica',
       'Imita doença granulomatosa na imagem e na lâmina, mas depende de '
       'berílio, que ele nega.', False),
      ('Pneumonite de hipersensibilidade',
       'Dá nódulos centrolobulares e aprisionamento aéreo, não perilinfáticos, '
       'e não produz calcitriol.', False),
      ('Carcinoma de pulmão com metástase linfonodal',
       'Não há massa pulmonar, o PTHrP é negativo e a adenopatia simétrica '
       'seria atípica.', False),
     ], 'Quatro hipóteses que só o tecido separa; a exposição afasta duas'),

    bifurcacao('b1', 'Decisão', 'Como chegar ao tecido',
      'Rafael está estável depois da hidratação, sem ameaça respiratória. '
      'Como conduzir a definição etiológica?', [
      caminho('Ecobroncoscopia com punção dos linfonodos (EBUS), com '
              'histologia, citometria e culturas', 'tecido',
              'Chega aos linfonodos mediastinais sem cirurgia e colhe material '
              'para micobactéria, fungo e linfoma antes de imunossuprimir.'),
      caminho('Iniciar prednisona sem amostra e tomar a resposta como '
              'confirmação', 'empirico',
              'Doença granulomatosa, linfoma e até tuberculose podem melhorar '
              'por semanas com corticoide.'),
      caminho('Atribuir tudo ao suplemento e observar', 'suplemento',
              'O colecalciferol soma, mas não produz linfonodo nem '
              'calcitriol alto com 25-OH normal.'),
    ]),

    pg('empirico', 'Dez dias de prednisona',
       'O cálcio cai e a tosse melhora. Mas ninguém excluiu tuberculose, '
       'histoplasmose nem linfoma, e a pneumologia se recusa a manter o '
       'corticoide sem tecido. O EBUS é feito com o paciente já sob '
       'prednisona; o patologista é avisado.',
       segue='tecido'),

    pg('suplemento', 'Uma semana depois',
       'Sem suplemento e sem tiazídico, o cálcio volta a **13,1 mg/dL**. '
       'Rafael retorna com dor nos olhos e fotofobia. É readmitido, hidratado '
       'de novo e avaliado pela oftalmologia no mesmo dia; o EBUS é marcado '
       'para depois da estabilização.',
       segue='tecido'),

    pg('tecido', 'O EBUS',
       'Punções dos linfonodos subcarinal e hilar direito mostram '
       '**granulomas não necrosantes**, compactos, sem células malignas. A '
       'citometria de fluxo não mostra população clonal.',
       'Colorações para bacilo álcool-ácido resistente e fungos, teste '
       'molecular para tuberculose e imunodifusão para //Histoplasma// são '
       'negativos. As culturas seguem em incubação por seis a oito semanas.'),

    estudo('granuloma', 'Granuloma pulmonar',
           'Compare com esta microfotografia de tecido pulmonar de outro '
           'paciente. Descreva o granuloma antes de ler a interpretação.',
           IMG / 'granuloma.jpg',
           'Tecido pulmonar de outro paciente · comparação morfológica.',
           referencia_imagem(IMG / 'granuloma.jpg.json'),
        [
         ((420, 330), (330, 55), '**Histiócitos epitelioides**: citoplasma amplo e pálido, núcleo oval, agrupados de forma compacta.', -12),
         ((500, 628), (330, 700), '**Coroa de linfócitos**, pequenos e escuros, na periferia do granuloma.', 12),
         ((540, 470), (800, 670), '**Centro celular, sem necrose**: é o que define o granuloma como não necrosante.', 12),
        ],
        ['Granuloma não necrosante: agregado compacto de histiócitos epitelioides com coroa linfocitária, sem necrose central.', 'Descreve morfologia, não causa. Não exclui micobactéria nem fungo: o diagnóstico junta lâmina, cultura e exposição.']),

    Q('p5', 5,
      'Granulomas não necrosantes no EBUS, citometria sem clone, BAAR, '
      'fungos, teste molecular e imunodifusão negativos, culturas pendentes. '
      'Qual a interpretação mais adequada?', [
      ('Tuberculose excluída pelo teste molecular negativo',
       'Em doença paucibacilar a sensibilidade cai; o negativo reduz a '
       'probabilidade, não a zera.', False),
      ('Sarcoidose provável, a confirmar pelas culturas finais',
       'Quadro compatível, granuloma não necrosante e alternativas '
       'razoavelmente excluídas: os três critérios da ATS 2020.', True),
      ('Ausência de necrose exclui micobactéria e fungo',
       'Há sobreposição morfológica; histoplasmose e tuberculose podem ter '
       'granuloma sem necrose.', False),
      ('Granuloma confirma sarcoidose e dispensa as culturas',
       'Granuloma é padrão de resposta; a exclusão de infecção faz parte do '
       'diagnóstico.', False),
      ('Biópsia pulmonar cirúrgica antes de qualquer conduta',
       'O EBUS rendeu tecido suficiente; cirurgia fica para quando o quadro '
       'divergir.', False),
      ('Esquema RIPE empírico até sair a cultura',
       'Sem necrose e com pesquisa e teste molecular negativos, tratar às '
       'cegas só acrescenta toxicidade.', False),
     ], 'Tecido compatível, exclusão ainda em curso'),

    pg('ocular', 'Avaliação oftalmológica',
       'Rafael conta agora que, há semanas, a luz do computador incomoda e os '
       'olhos avermelham no fim do dia; ninguém tinha perguntado. A '
       'oftalmologia examina no mesmo dia.',
       'Na lâmpada de fenda: **células 2+ na câmara anterior dos dois olhos** '
       'e precipitados ceráticos, sem sinéquias. Acuidade 20/25 em cada olho, '
       'pressão intraocular 16 e 17 mmHg, fundo sem vitreíte e tomografia de '
       'coerência óptica sem edema macular. Uveíte anterior bilateral: '
       'colírio de corticoide e cicloplégico.'),

    Q('p6', 6,
      'Sarcoidose com pulmão, linfonodo, cálcio, rim e olho. **Quais três** '
      'avaliações a ATS indica para todo paciente ao diagnóstico, mesmo sem '
      'sintomas?', [
      ('Eletrocardiograma de 12 derivações',
       'É a triagem cardíaca de base; bloqueio ou arritmia levam à '
       'ressonância.', True),
      ('Ressonância cardíaca de rotina em todos',
       'Sem sintoma e com ECG normal, não é recomendada como rastreio.',
       False),
      ('Exame oftalmológico com lâmpada de fenda',
       'Uveíte pode ser assintomática e deixar sequela; examina-se com ou sem '
       'queixa.', True),
      ('Cálcio, creatinina e fosfatase alcalina',
       'Rastreiam alteração do cálcio, acometimento renal e hepático.', True),
      ('PET-CT de corpo inteiro para todos',
       'Não é rastreio; serve para doença cardíaca ou para escolher o sítio '
       'de biópsia.', False),
      ('Biópsia hepática',
       'Com fosfatase alcalina e transaminases normais, não há indicação.',
       False),
      ('Holter de 24 horas em assintomáticos',
       'A ATS não recomenda Holter de rotina; é guiado por sintoma ou ECG '
       'alterado.', False),
      ('Enzima conversora seriada para monitorar',
       'Oscila e não orienta o tratamento com segurança.', False),
     ], 'Coração, olho e metabolismo, em todos'),

    pg('extensao', 'Outros órgãos',
       'ECG sem bloqueio nem arritmia. Fosfatase alcalina e transaminases '
       'normais. Creatinina 1,5 mg/dL, sedimento sem cilindros. Capacidade '
       'vital forçada 83% e difusão de monóxido de carbono 64% do previsto.'),

    estudo('rx_tc', 'Sarcoidose avançada',
           'Outro paciente, com sarcoidose pulmonar avançada. Não é a '
           'tomografia de Rafael; mostra o que a doença pode fazer quando '
           'progride no parênquima.',
           IMG / 'rx_tc.jpg',
           'Radiografia e TC coronal de outro paciente · doença parenquimatosa avançada.',
           referencia_imagem(IMG / 'rx_tc.jpg.json'),
        [
         ((360, 110), (470, 35), '**Opacidades reticulonodulares** densas, que predominam nos campos superiores.', -12),
         ((638, 257), (575, 420), 'Na TC coronal, **conglomerado peri-hilar** com espessamento peribroncovascular.', 12),
         ((905, 170), (985, 60), '**Micronódulos** difusos, de distribuição perilinfática.', -12),
        ],
        ['Doença parenquimatosa extensa, com predomínio superior e peri-hilar e conglomerados: o estágio IV de Scadding, a fibrose.', 'O tratamento mira a inflamação antes que ela vire fibrose, que não regride.']),

    Q('p7', 7,
      'A prednisona vai começar. **Quais quatro** afirmações estão corretas?', [
      ('A indicação é a hipercalcemia com lesão renal',
       'Adenopatia hilar isolada muitas vezes se observa; cálcio e rim são '
       'indicação clara.', True),
      ('Cálcio e vitamina D devem ser repostos pelo corticoide, como de rotina',
       'Com calcitriol alto, a reposição automática piora a hipercalcemia; a '
       'proteção óssea é individual.', False),
      ('A uveíte segue com colírio e seguimento ocular',
       'O corticoide sistêmico não substitui o colírio nem a lâmpada de '
       'fenda.', True),
      ('Dose inicial de 20 a 40 mg/dia',
       'A ERS sugere dose moderada: doses altas não mostraram benefício e '
       'somam toxicidade.', True),
      ('Suspender quando a radiografia normalizar',
       'A meta é a função dos órgãos acometidos, não a imagem.', False),
      ('Infliximabe como primeira linha, pela gravidade',
       'É terceira linha, depois do corticoide e do metotrexato.', False),
      ('Pode começar antes das culturas finais',
       'O risco renal não espera oito semanas; alguém fica responsável por '
       'conferir as culturas.', True),
     ], 'Trata-se o órgão ameaçado, em dose moderada, olhando cada um'),

    pg('evolucao2', 'Oito semanas depois',
       'Cálcio 9,8 mg/dL, creatinina 1,1 mg/dL. Culturas finais sem '
       'crescimento. A inflamação ocular está controlada e Rafael voltou a '
       'caminhar. Começa a redução da prednisona.',
       'Quatro semanas depois, durante a redução, a dor no olho direito '
       'volta. Os exames de sangue estão normais, e Rafael quer manter o '
       'esquema porque "o resto melhorou".'),

    Q('p8', 8,
      'A dor ocular voltou durante a redução. Se for recidiva da uveíte, '
      '**quais duas** estratégias são as mais adequadas?', [
      ('Metotrexato como poupador de corticoide',
       'Segunda linha da ERS na recidiva ou na dependência de corticoide, com '
       'ácido fólico e controle hepático.', True),
      ('Manter prednisona 40 mg/dia por tempo indeterminado',
       'A toxicidade cumulativa em osso, glicemia, catarata e glaucoma é o '
       'que o poupador evita.', False),
      ('Conferir adesão ao colírio e excluir infecção',
       'Recidiva também é colírio que acabou, ou uma infecção ocular que '
       'imita inflamação.', True),
      ('Iniciar infliximabe antes de tentar metotrexato',
       'Anti-TNF é terceira linha, depois de corticoide e metotrexato.',
       False),
      ('Suspender o sistêmico porque a espirometria melhorou',
       'Cada órgão tem a sua meta, e o olho está ativo.', False),
      ('Hidroxicloroquina para a uveíte',
       'Tem papel na pele e na hipercalcemia; não é o poupador da uveíte.',
       False),
     ], 'Poupar corticoide, mas primeiro conferir o colírio'),

    bifurcacao('b2', 'Decisão', 'O olho durante a redução',
      'Como responder à volta da dor ocular?', [
      caminho('Reavaliar na oftalmologia no mesmo dia e ajustar pelo exame',
              'controle',
              'Cada órgão tem seu marcador; o do olho é a lâmpada de fenda.'),
      caminho('Manter a redução e antecipar só o cálcio e a espirometria',
              'visao',
              'Nenhum desses exames vê a câmara anterior.'),
    ]),

    pg('controle', 'No mesmo dia',
       'Células 2+ no olho direito, pressão 18 mmHg, sem edema macular. '
       'Recidiva anterior. O colírio é intensificado, a redução sistêmica '
       'desacelera e começa o metotrexato.',
       segue='f1'),

    pg('visao', 'Três semanas depois',
       'Rafael volta com visão turva no olho direito. Acuidade 20/80, células '
       '3+, **sinéquias posteriores novas**, pressão de 28 mmHg e **edema '
       'macular** na tomografia de coerência óptica.',
       segue='b_resgate'),

    bifurcacao('b_resgate', 'Decisão', 'Edema macular e pressão alta',
      'Qual resgate organizar?', [
      caminho('Oftalmologia urgente: controlar inflamação e pressão, com '
              'tratamento local e sistêmico', 'resgate',
              'Edema macular ameaça a visão central e pede tratamento '
              'dirigido.'),
      caminho('Só colírio hipotensor e aguardar', 'resgate_tardio',
              'A pressão é parte do problema; a inflamação e o edema '
              'continuam.'),
    ]),

    pg('resgate', 'Duas semanas depois',
       'Pressão 18 mmHg e acuidade 20/40, com edema em regressão. A recidiva '
       'grave acelera o metotrexato.',
       segue='f1b'),

    pg('resgate_tardio', 'Uma semana depois',
       'A pressão caiu, mas a dor e o borramento continuam: células e edema '
       'macular seguem ativos. O resgate integrado começa com uma semana de '
       'atraso.',
       segue='f2'),

    fim('f1', 'Controle com visão preservada',
        'Com metotrexato, a redução da prednisona chega a 5 mg/dia em seis '
        'meses. Cálcio e creatinina normais, visão 20/20, espirometria '
        'estável.',
        'Cada órgão foi examinado com o seu instrumento, e a recidiva ocular '
        'foi vista no dia em que apareceu.', 'melhor'),

    fim('f1b', 'Controle após recidiva grave',
        'A visão do olho direito volta a 20/25 em três meses. Metotrexato '
        'mantido, prednisona em redução.',
        'O resgate imediato do edema macular preservou a visão, mas a '
        'recidiva grave poderia ter sido vista três semanas antes.', 'medio'),

    fim('f2', 'Perda visual residual',
        'A inflamação e a pressão estão controladas, mas a acuidade direita '
        'estabiliza em 20/50, com alterações maculares documentadas.',
        'Tratar só a pressão deixou o edema macular ativo por mais uma '
        'semana. A lesão foi documentada no seguimento, não presumida.', 'pior'),

    pagina('retrospectiva', 'Retrospectiva', '',
        tabela(['Momento', 'O dado', 'O que decidiu'], [
            ['Na emergência', 'Cálcio 13,6, creatinina dobrada, QT curto',
             'Volume antes de diurético; tirar tiazídico e vitamina D'],
            ['Primeiras 24 h', 'PTH 6 pg/mL', 'PTHrP, vitamina D, paraproteína e tórax'],
            ['Investigação', '1,25-(OH)₂D alto, 25-OH normal, hilos bilaterais',
             'Calcitriol produzido fora do rim: granuloma ou linfoma'],
            ['Tomografia', 'Adenopatia simétrica, nódulos perilinfáticos, galinheiro',
             'Quatro hipóteses, e só o tecido separa'],
            ['EBUS', 'Granuloma não necrosante, culturas pendentes',
             'Sarcoidose provável, tratada pelo rim e pelo cálcio'],
            ['Redução', 'Dor ocular com exames de sangue normais',
             'O olho se examina com lâmpada de fenda, não com cálcio'],
        ]),
        so_kicker=True),

    pg('referencias', 'Fontes e limites',
       'Caso autoral e ficcional; valores, intervalos e desfechos simulados.',
       'Crouser e cols. Diagnosis and detection of sarcoidosis, ATS, 2020. '
       'Baughman e cols. ERS clinical practice guidelines on treatment of '
       'sarcoidosis, 2021. Mochizuki e cols. Revised criteria of the '
       'International Workshop on Ocular Sarcoidosis, 2019. Walker e Shane. '
       'Hypercalcemia: a review, JAMA, 2022. Tebben e cols. Vitamin '
       'D-mediated hypercalcemia, Endocrine Reviews, 2016.',
       'Imagens de outros pacientes: Hellerhoff (CC BY-SA 4.0; '
       + _fonte(IMG / 'rx_hilos.jpg.json', 'radiografia dos hilos') + ' e '
       + _fonte(IMG / 'rx_tc.jpg.json', 'radiografia e TC') + ') e Yale Rosen '
       '(CC BY-SA 2.0; ' + _fonte(IMG / 'granuloma.jpg.json', 'granuloma')
       + '), Wikimedia Commons. Cena: ilustração gerada por IA.'),
]

REVISAO = []

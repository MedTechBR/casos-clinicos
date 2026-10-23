"""Caso ficcional para raciocínio clínico em residência de clínica médica.

Revisão editorial: integração de dados, seleção limitada de exames e
explicações após a resposta. Fontes clínicas ao final deste arquivo.
"""
from pathlib import Path

from motor.estudo_imagem import ecg, estudo
from motor.etapas import (alt, bifurcacao, caminho, capa, desfecho, op, p,
                          pagina, painel, par, pareamento, pergunta, pontos,
                          topicos, vitais)

TITULO = 'O peso dos dias'
RODAPE = 'Paciente ficcional · evoluções simuladas para ensino'
COR = '#2563eb'
IMG = Path(__file__).parent / 'img'
BANCO = []
MOLDE = 'nejm'


def credito_meta(meta):
    import json
    m = json.loads(Path(meta).read_text())
    return m['autor'] + ' · Wikimedia Commons · ' + m['licenca'] + ' · setas adicionadas'


def pg(k, titulo, *textos, segue='', conforme=None):
    return pagina(k, titulo, '', *(p(t) for t in textos), so_kicker=True,
                  segue=segue, conforme=conforme)


def Q(k, n, enunciado, opcoes, explicacao, segue=''):
    """Pergunta no molde do NEJM: alternativas curtas e uma explicação só,
    em seções (subtítulo, texto)."""
    return pergunta(k, f'Pergunta {n}', enunciado,
                    [alt(t, certa=ok) for t, ok in opcoes],
                    explicacao=explicacao, segue=segue)


def ex(nome, valor, ref='—', alt_=False):
    return op(nome, resultado=valor, referencia=ref, alterado=alt_)


def fim(k, titulo, texto, porque, qualidade):
    return desfecho(k, titulo, p(texto), qualidade=qualidade, porque=porque,
                    fecho='retrospectiva')


ETAPAS = [
    capa(TITULO, fundo='cena.png', kicker='Caso interativo',
         selo='Paciente ficcional · procedência e créditos na última tela'),

    pg('historia', 'Apresentação',
       'Um homem de 71 anos é trazido pela esposa ao pronto-socorro no quinto '
       'dia de febre. Tem dor de cabeça desde o início e, desde ontem, demora a '
       'responder e troca as datas. Hoje de manhã a perna direita cedeu quando '
       'ele tentou levantar, e ele não conseguiu ir sozinho ao banheiro.',
       'No segundo dia de febre passou numa unidade básica: o exame de urina foi '
       'normal, e ele saiu com paracetamol e orientação de beber líquidos. Desde '
       'então come pouco, mas tem tomado água e chá.',
       'Nega tosse, dor torácica, ardor ao urinar, diarreia, vômitos, '
       'convulsão, queda com batida na cabeça, dor nas costas, manchas na pele '
       'e remédio novo.'),

    pagina('ficha', 'Ficha do paciente', '',
           topicos(('Antecedentes', 'Hipertensão há 14 anos e diabetes tipo 2 '
                    'há 7, sem lesão de órgão conhecida. Catarata operada nos '
                    'dois olhos. Herniorrafia inguinal há 20 anos. Dengue há '
                    'seis anos, sem internação.'),
                   ('Medicações', 'Losartana 50 mg pela manhã e metformina 850 '
                    'mg duas vezes ao dia. Nenhum diurético. Paracetamol desde o '
                    'início da febre.'),
                   ('Vacinas', 'Febre amarela em 2018. Gripe e covid-19 em dia.'),
                   ('Hábitos', 'Parou de fumar há 20 anos. Uma ou duas cervejas '
                    'no fim de semana. Caminha 40 minutos todas as manhãs.'),
                   ('Vida social', 'Bancário aposentado, mora com a esposa e '
                    'cuida do neto duas tardes por semana. Voltaram há nove dias '
                    'de três semanas na casa da filha, nos Estados Unidos.'),
                   ('Família', 'Pai morreu de infarto aos 68 anos; a mãe teve '
                    'AVC aos 80. Um irmão tem doença de Parkinson.')),
           so_kicker=True),

    pagina('exame', 'Exame físico', '',
           vitais(('Temperatura', '38,7 °C', True),
                  ('Pressão arterial', '146/84', True),
                  ('Frequência cardíaca', '124', True),
                  ('Frequência respiratória', '20', False),
                  ('SpO₂ em ar ambiente', '96%', False),
                  ('Peso', '78 kg', False)),
           topicos(('Estado geral', 'Sonolento, abre os olhos quando chamado, '
                    'desorientado no tempo. Mucosas úmidas, jugulares planas, '
                    'sem edema.'),
                   ('Pele', 'Sem exantema, petéquias ou vesículas.'),
                   ('Cardiopulmonar', 'Ritmo regular, taquicárdico, sem sopros. '
                    'Murmúrio vesicular presente, sem ruídos adventícios.'),
                   ('Abdome', 'Flácido e indolor, sem visceromegalias. Bexiga '
                    'não palpável.'),
                   ('Neurológico', 'Rigidez de nuca discreta. Pupilas isocóricas, '
                    'face simétrica, fala lenta, sem afasia. Não sustenta a perna '
                    'direita elevada no leito; move os outros três membros contra '
                    'a gravidade. Reflexo cutâneo-plantar em flexão dos dois '
                    'lados.')),
           so_kicker=True),

    painel('res1', 'Primeiros exames', 'Sangue', [
        ex('Hemoglobina', '14,1 g/dL', '13,5–17,5 g/dL'),
        ex('Leucócitos', '11.800/mm³ · neutrófilos 84% · linfócitos 850/mm³',
           '4.000–11.000 · linfócitos 1.000–4.000', True),
        ex('Plaquetas', '176.000/mm³', '150.000–450.000/mm³'),
        ex('Sódio / potássio', '129 / 4,0 mmol/L', 'Na 135–145 · K 3,5–5,0', True),
        ex('Ureia / creatinina', '26 / 1,1 mg/dL {{(TFGe 72 mL/min/1,73 m², CKD-EPI 2021)}}',
           'até 42 / 0,7–1,3 mg/dL'),
        ex('Glicose', '138 mg/dL', '70–99 mg/dL em jejum', True),
        ex('Osmolalidade sérica', '270 mOsm/kg', '275–295 mOsm/kg', True),
        ex('Ácido úrico', '2,6 mg/dL', '3,4–7,0 mg/dL', True),
        ex('Proteína C reativa', '38 mg/L', 'até 5 mg/L', True),
    ], introducao='Duas hemoculturas foram colhidas na chegada.'),

    painel('res1b', 'Primeiros exames', 'Urina e outros', [
        ex('Urina', 'Densidade 1.018 · sem leucócitos · nitrito negativo · sem '
           'sangue · sem glicose'),
        ex('Osmolalidade urinária', '456 mOsm/kg', '—', True),
        ex('Sódio urinário', '52 mmol/L', '—', True),
        ex('AST / ALT', '34 / 29 U/L', 'até 40 / 41 U/L'),
        ex('Creatinoquinase', '160 U/L', 'até 190 U/L'),
        ex('Lactato', '1,3 mmol/L', 'até 2,0 mmol/L'),
        ex('TSH', '2,1 µUI/mL', '0,4–4,5 µUI/mL'),
    ]),

    Q('p1', 1,
      'Na 129, osmolalidade sérica 270 e urinária 456, Na urinário 52, sem diurético ou sinais de depleção. Quais duas hipóteses ainda explicam esse padrão?', [
      ('Antidiurese inapropriada associada à doença aguda', True),
      ('Deficiência de cortisol', True),
      ('Hiponatremia translocacional pela glicose de 138', False),
      ('Polidipsia primária como mecanismo isolado', False),
      ('Baixo volume arterial efetivo por insuficiência cardíaca', False),
     ], [
      ('Duas possibilidades', 'A hipotonicidade com urina não diluída e Na urinário alto, em aparente euvolemia, favorece SIAD na doença neurológica aguda. Deficiência de cortisol pode produzir o mesmo padrão e ainda não foi investigada; não se pode fechar SIAD só com esses números.'),
      ('O que pesa contra as demais', 'Glicose 138 altera pouco o sódio e não explica osmolalidade baixa. Polidipsia isolada deveria permitir urina muito diluída. Insuficiência cardíaca não encontra congestão no exame. TSH normal torna hipotireoidismo primário grave improvável, mas não substitui avaliação adrenal.'),
     ]),

    estudo('rx_adm', 'Radiografia de tórax',
           'Radiografia feita na chegada, à procura de um foco para a febre e a '
           'confusão.',
           IMG / 'rx_torax_normal.jpg',
           'Radiografia de outro paciente · comparação didática.',
           'Mikael Häggström · Wikimedia Commons · CC0 · setas adicionadas',
        [
         ((112, 972), (60, 820), '**Seio costofrênico** direito agudo e livre: sem derrame.', 12),
         ((300, 700), (160, 560), '**Pulmão direito** com trama vascular normal, sem consolidação.', -12),
         ((735, 820), (880, 700), '**Silhueta cardíaca** de tamanho normal.', 12),
        ],
        ['Campos pulmonares limpos, seios costofrênicos livres, área cardíaca '
         'normal.',
         'Sem foco pulmonar e com urina normal, a febre continua sem origem fora '
         'do sistema nervoso.']),

    *ecg('ecg_evolucao',
         'A frequência cardíaca segue em 124 depois do antitérmico. A equipe '
         'registra um ECG.',
         IMG,
         'Com febre de 38,7 °C, a taquicardia sinusal é esperada e não explica a '
         'confusão nem a perna que cedeu.'),

    bifurcacao('b1', 'Decisão', 'Antes da tomografia',
      'Febre, confusão, rigidez de nuca discreta e uma perna fraca. A tomografia '
      'vai levar uma hora. O que você faz enquanto isso?', [
      caminho('Ceftriaxona, ampicilina e aciclovir agora, antes da tomografia',
              'tratado',
              'Com déficit focal, a punção espera a imagem, mas o tratamento '
              'empírico não. Acima dos 50 anos, a ampicilina cobre Listeria; o '
              'aciclovir cobre o herpes simples.'),
      caminho('Tomografia e punção primeiro; tratar conforme o líquor',
              'atraso',
              'O líquor fica pronto horas depois, e cada hora de atraso do '
              'antibiótico na meningite bacteriana aumenta a mortalidade.'),
      caminho('Ceftriaxona agora; aciclovir só se a ressonância mostrar o lobo '
              'temporal', 'sem_aciclovir',
              'A ressonância pode demorar um dia, e o atraso do aciclovir piora '
              'o prognóstico da encefalite herpética.'),
    ]),

    pg('atraso', 'Seis horas depois',
       'A fila da tomografia leva uma hora e meia, e a punção só sai no fim da '
       'tarde. Nesse tempo ele fica mais sonolento. Ceftriaxona, ampicilina e '
       'aciclovir começam seis horas depois da chegada, quando chega a '
       'citologia do líquor.',
       segue='tc_evolucao'),

    pg('sem_aciclovir', 'Primeiras horas',
       'Ceftriaxona 2 g e ampicilina 2 g entram antes da tomografia. O aciclovir '
       'fica esperando a ressonância, marcada para o dia seguinte, até que o '
       'plantonista da noite o inicia, 14 horas depois da chegada.',
       segue='tc_evolucao'),

    pg('tratado', 'Primeiras horas',
       'Ceftriaxona 2 g, ampicilina 2 g e aciclovir 780 mg (10 mg/kg) pela veia '
       'em 40 minutos. Com a TFG estimada de 72, o aciclovir não precisa de '
       'ajuste. A água livre fica restrita a um litro por dia, e o soro '
       'fisiológico, só para diluir as medicações.'),

    estudo('tc_evolucao', 'Tomografia de crânio',
        'Tomografia sem contraste antes da punção, pelo déficit focal e pela '
        'sonolência.',
        IMG / 'tc_cranio.png',
        'Corte axial e localizador de outro adulto · comparação didática.',
        'Mikael Häggström · Wikimedia Commons · CC0 · setas adicionadas',
        [
         ((268, 380), (35, 340), '**Ventrículos laterais**, escuros neste corte, sem dilatação.', 12),
         ((282, 210), (400, 100), '**Fissura inter-hemisférica** anterior na linha média: sem desvio.', -12),
         ((766, 466), (560, 250), '**Localizador**: a linha amarela marca o nível do corte, que passa pelos ventrículos laterais.', 12),
        ],
        ['Sem hemorragia, hidrocefalia, efeito de massa ou desvio da linha média.',
         'A tomografia libera a punção; não afasta encefalite nem isquemia '
         'recente.']),

    painel('lcr', 'Líquor', 'Punção lombar', [
        ex('Pressão de abertura', '19 cmH₂O', '10–20 cmH₂O'),
        ex('Aspecto', 'Límpido, incolor'),
        ex('Células', '86/mm³ · neutrófilos 58% · linfócitos 42%', 'até 5/mm³', True),
        ex('Hemácias', '4/mm³'),
        ex('Proteína', '92 mg/dL', '15–45 mg/dL', True),
        ex('Glicose', '74 mg/dL {{(sérica 138 · relação 0,54)}}', 'relação acima de 0,4'),
        ex('Gram', 'Sem bactérias'),
    ], introducao='Punção lombar feita logo depois da tomografia.'),

    Q('p2', 2,
      'Líquor com 86 células, 58% neutrófilos, proteína 92 e relação glicose 0,54. Qual interpretação melhor pondera as hipóteses infecciosas nesta fase?', [
      ('Perfil compatível com virose inicial, mantendo cobertura bacteriana enquanto se esclarece a etiologia', True),
      ('Perfil predominantemente piogênico, tornando a investigação viral uma prioridade posterior', False),
      ('Perfil sugestivo de meningite tuberculosa, pela combinação de proteína elevada e pleocitose moderada', False),
      ('Perfil favorece Listeria sobre virose, pelo predomínio neutrofílico no paciente idoso', False),
      ('Perfil favorece infecção fúngica crônica, pela glicorraquia de 74 mg/dL', False),
     ], [
      ('Probabilidade e cobertura', 'Pleocitose moderada, proteína elevada e glicose relativamente preservada cabem em virose inicial, inclusive com neutrófilos. O conjunto não exclui bactéria: idade, quadro clínico e antibiótico pré-punção justificam manter cobertura enquanto se obtêm testes etiológicos.'),
      ('Concorrentes', 'Meningite piogênica costuma ter maior celularidade e menor relação de glicose, embora haja sobreposição. Idade justifica cobrir Listeria, mas 58% de neutrófilos não a distingue de virose. TB e fungos permanecem diferenciais conforme contexto, porém evolução aguda e relação de glicose 0,54 não os priorizam; proteína 92 isoladamente também não os separa.'),
     ]),
    pg('reexame', 'Na manhã seguinte',
       'A equipe registra meningoencefalite viral, herpética até prova em '
       'contrário, mantém o aciclovir e envia o líquor para PCR. As hemoculturas '
       'não cresceram. A febre continua, e o sódio subiu para 132 com a '
       'restrição de água.',
       'Mais acordado, ele colabora com o exame. Força grau 1 na perna direita, '
       '4 na esquerda, 4 no braço direito e 5 no esquerdo, com tônus flácido na '
       'perna direita. Patelar e aquileu abolidos à direita e diminuídos à '
       'esquerda; bicipitais presentes. Sensibilidade tátil, dolorosa e '
       'vibratória normais e simétricas, sem nível. Plantar em flexão. Urina '
       'espontaneamente. Há tremor de ação nas duas mãos.'),

    Q('p3', 3,
      'Fraqueza flácida muito assimétrica, arreflexia, sensibilidade preservada, tremor e pleocitose. Quais três exames melhor localizam o processo?', [
      ('Ressonância do encéfalo', True),
      ('Ressonância da medula', True),
      ('Eletroneuromiografia com conduções motoras e sensitivas', True),
      ('Repetir CK como principal teste localizatório', False),
      ('Anticorpo antirreceptor de acetilcolina', False),
      ('Nova tomografia de crânio sem contraste', False),
     ], [
      ('Localizações a testar', 'RM de encéfalo: investiga a encefalite e o tremor, que uma neuropatia isolada não explica. RM de medula: procura acometimento de substância cinzenta e exclui compressão. ENMG: distingue padrão motor axonal de desmielinização e testa a preservação sensitiva; sozinha não separa sempre corno anterior de neuropatia motora axonal.'),
      ('Por que não estes agora', 'CK repetida: a inicial normal e o padrão focal/arreflexo tornam miopatia menos provável. Anti-AChR: miastenia não integra febre, pleocitose e arreflexia assimétrica. Nova TC: sem mudança aguda sugestiva de hemorragia, acrescenta menos que RM para estas localizações.'),
     ]),

    estudo('rm_encefalo', 'Ressonância de encéfalo',
           'Ressonância feita à tarde, à procura do lobo temporal da encefalite '
           'herpética e de uma causa para a paresia. Sequência FLAIR.',
           IMG / 'rm_encefalo_flair.png',
           'Ressonância de outro paciente · FLAIR axial · as setas brancas são '
           'do original.',
           credito_meta(IMG / 'rm_encefalo_flair.png.json'),
        [
         ((288, 300), (300, 170), '**Substância negra** com hipersinal, dos dois lados do mesencéfalo.', -12),
         ((342, 272), (450, 190), '**Lobo temporal mesial** esquerdo com hipersinal discreto.', 12),
         ((690, 300), (800, 175), '**Tálamo posterior** direito com hipersinal.', 12),
        ],
        ['Hipersinal em FLAIR na substância negra dos dois lados, no tálamo '
         'posterior direito e, discreto, no lobo temporal mesial esquerdo. Sem '
         'sangramento nem efeito de massa.']),

    estudo('rm_medula', 'Ressonância da medula',
           'No mesmo exame, cortes da medula cervical e lombar, pela paresia de '
           'neurônio motor inferior.',
           IMG / 'rm_medula_t2.jpg',
           'Ressonância de outro paciente · T2 axial da medula cervical · os '
           'círculos são do original.',
           credito_meta(IMG / 'rm_medula_t2.jpg.json'),
        [
         ((497, 835), (230, 760), '**Hipersinal central** na medula: a substância cinzenta está acometida.', 12),
         ((500, 255), (220, 140), 'Num nível acima, **medula de sinal normal**, para comparação.', -12),
        ],
        ['Hipersinal em T2 na substância cinzenta central da medula cervical, '
         'sem expansão e sem compressão.',
         'Na série completa, alteração semelhante na substância cinzenta do '
         'cone medular, fora destes cortes.']),

    Q('p4', 4,
      'A RM reúne substância negra, tálamo, discreto temporal mesial e substância cinzenta medular. Quais duas interpretações melhor integram imagem, exame e cronologia?', [
      ('Encefalomielite infecciosa integra a encefalopatia, o tremor e a paresia assimétrica', True),
      ('O acometimento temporal mantém HSV como concorrente enquanto se amplia a investigação etiológica', True),
      ('Encefalite temporal por HSV com paresia de origem hemisférica é a melhor localização unificadora', False),
      ('Polirradiculoneuropatia pós-infecciosa explica melhor a fraqueza durante a fase febril', False),
      ('Mielite transversa inflamatória explica melhor a paresia pela alteração intramedular', False),
     ], [
      ('O conjunto', 'Núcleos profundos, tremor e substância cinzenta medular com fraqueza flácida assimétrica favorecem encefalomielite infecciosa, como a produzida por alguns arbovírus ou enterovírus. O discreto achado temporal mantém HSV em investigação e sustenta manter aciclovir até esclarecimento adequado.'),
      ('Localizações concorrentes', 'Uma paresia hemisférica explica mal a arreflexia e as lesões medulares. Polirradiculoneuropatia pós-infecciosa costuma aparecer após a infecção, com maior simetria; aqui a paresia acompanha a febre e há lesão intramedular. Mielite transversa pode ser aguda, mas o predomínio motor assimétrico sem nível sensitivo ou disfunção vesical favorece substância cinzenta motora em vez de síndrome transversa.'),
     ]),

    pg('respiracao', 'Segundo dia de internação',
       'No fim da tarde, a tosse fica fraca e ele engasga com água. Frequência '
       'respiratória de 22, SpO₂ de 96% em ar ambiente, gasometria com pH 7,43 '
       'e pCO₂ de 38 mmHg. A capacidade vital caiu de 24 para 17 mL/kg em oito '
       'horas; pressão inspiratória máxima de −22 cmH₂O e expiratória de 34 '
       'cmH₂O.'),

    Q('p5', 5,
      'Capacidade vital caiu de 24 para 17 mL/kg em oito horas, com engasgos; SpO₂ 96% e pCO₂ 38. Quais duas interpretações devem orientar o suporte?', [
      ('A tendência da capacidade vital indica reserva ventilatória em deterioração', True),
      ('A disfunção bulbar reduz a segurança do suporte por máscara', True),
      ('A pCO₂ normal demonstra reserva ventilatória suficiente para a noite', False),
      ('A saturação preservada favorece oxigênio como tratamento da falência da bomba', False),
      ('Aguardar capacidade vital abaixo de 10 mL/kg é seguro com vigilância', False),
     ], [
      ('O risco vem da evolução', 'A queda de quase 30% da capacidade vital, somada a PImax −22 e PEmax 34, indica perda de reserva; os números não devem ser usados como limiares automáticos isolados. Tosse ineficaz e engasgo acrescentam risco de secreção e aspiração, limitando a VNI.'),
      ('Por que os dados normais não tranquilizam', 'SpO₂ mede oxigenação, não força nem proteção da via aérea; oxigênio não corrige a bomba fraca. pCO₂ pode permanecer normal antes da descompensação. Esperar outro limiar ignora a queda rápida e a disfunção bulbar.'),
     ]),

    pg('enmg', 'A eletroneuromiografia',
       'Chega o laudo da eletroneuromiografia feita de manhã: potenciais '
       'motores de amplitude reduzida, mais à direita, com velocidades de '
       'condução normais e potenciais sensitivos preservados.',
       'Amplitude baixa com condução normal indica perda de axônios motores; a '
       'desmielinização reduziria a velocidade. Com os potenciais sensitivos '
       'normais, há um processo motor sem perda sensitiva demonstrável. Em '
       'conjunto com a assimetria e a RM, favorece o corno anterior; a ENMG '
       'isolada não distingue toda neuropatia motora axonal.'),

    bifurcacao('b2', 'Decisão', 'Suporte respiratório',
      'De volta ao leito: tosse fraca, engasgo com água e capacidade vital de '
      '17 mL/kg, em queda. Como você conduz?', [
      caminho('UTI e intubação planejada agora', 'r_via',
              'A progressão bulbar e ventilatória permite antecipar a via aérea '
              'em vez de esperar o colapso.'),
      caminho('Ventilação não invasiva com vigilância intensiva', 'r_vni',
              'Disfagia e secreções tiram a margem de segurança da máscara.'),
      caminho('Oxigênio e vigilância na enfermaria', 'r_atraso',
              'A saturação não mede a reserva ventilatória nem a proteção '
              'contra aspiração.'),
    ]),

    pg('r_vni', 'Na UTI, com máscara',
       'Com ventilação não invasiva, acumula secreções e não consegue '
       'expectorar. Engasga de novo. A oxigenação se mantém, mas a proteção da '
       'via aérea piora.',
       segue='b_resgate'),

    pg('r_atraso', 'Na enfermaria',
       'De madrugada, engasga e passa a respirar com esforço. É levado à sala de '
       'emergência com saturação de 88%.',
       segue='b_resgate'),

    bifurcacao('b_resgate', 'Decisão', 'A estratégia falhou',
      'Ele não elimina secreções e já aspirou uma vez. Qual a próxima conduta?', [
      caminho('Intubar agora', 'r_resgate',
              'A falha em proteger a via aérea é a indicação.'),
      caminho('Manter o suporte não invasivo e reavaliar', 'f_obito',
              'Insistir num suporte que já falhou numa via aérea desprotegida.'),
    ]),

    pg('r_resgate', 'Terceiro dia',
       'Intubado em urgência, depois de aspirar, e tratado para pneumonia '
       'aspirativa. Precisa de pressão expiratória alta por três dias.',
       segue='exposicao'),

    pg('r_via', 'Terceiro dia',
       'Intubação planejada, sem aspiração, e ventilação protetora na UTI. A '
       'febre começa a ceder; a força não muda.'),

    pg('exposicao', 'A esposa conta a viagem',
       'Com ele sedado, a esposa conta a viagem com calma. A filha mora nos '
       'arredores de Baton Rouge, na Louisiana, no sul dos Estados Unidos. Era '
       'agosto, fazia calor, e ele passava o fim de tarde no quintal, ao lado '
       'de um canal de drenagem, sem repelente. Os dois foram muito picados por '
       'mosquitos. Na última semana, a filha achou dois pássaros mortos no '
       'gramado.',
       'Não houve contato com morcegos nem mordida de animal, e ninguém na '
       'família adoeceu. A PCR do líquor para herpes simples, colhida no quinto '
       'dia de sintomas, veio negativa, assim como as PCR para varicela-zóster e '
       'enterovírus. As hemoculturas seguem negativas em 72 horas.'),

    Q('p6', 6,
      'D7, imunocompetente, viagem à Louisiana, encefalomielite e PCR para HSV/VZV/enterovírus negativas. Com dengue prévia e vacina de febre amarela, quais dois exames priorizar?', [
      ('IgM para Nilo Ocidental no líquor e no soro', True),
      ('Neutralização por redução de placas em laboratório de referência', True),
      ('RT-PCR de Nilo Ocidental no sangue como teste principal', False),
      ('IgG isolada para Nilo Ocidental no soro', False),
      ('Repetição imediata da PCR de enterovírus no mesmo material', False),
      ('NS1 de dengue como confirmação da etiologia neurológica', False),
     ], [
      ('Rendimento e especificidade', 'IgM no líquor e soro: maior rendimento nesta fase; no líquor apoia neuroinvasão, mas exige interpretação clínica. Neutralização: ajuda a discriminar reatividade entre flavivírus diante de dengue prévia e vacinação; o laboratório de referência integra títulos, amostras e epidemiologia.'),
      ('Por que não os demais', 'RT-PCR sanguínea: baixa sensibilidade após a viremia curta no imunocompetente; negativa não exclui. IgG isolada: não data infecção nem resolve reatividade cruzada. Repetir enterovírus no mesmo material: sem falha técnica ou nova informação, rende menos que ampliar a etiologia. NS1: pesquisa dengue aguda, não confirma Nilo Ocidental nem neuroinvasão.'),
     ]),

    pg('virada', 'O diagnóstico',
       'Laboratório de referência: **IgM contra o vírus do Nilo Ocidental '
       'reagente no líquor e no soro**; IgM para dengue, febre amarela e '
       'encefalite de Saint Louis não reagentes. Dez dias depois, o teste de '
       'neutralização mostra título oito vezes maior para o vírus do Nilo '
       'Ocidental que para a dengue.',
       'É doença neuroinvasiva pelo vírus do Nilo Ocidental, com encefalite e '
       'poliomielite. O vírus circula entre aves e mosquitos do gênero Culex, e '
       'o homem é hospedeiro acidental. Cerca de uma infecção em 150 atinge o '
       'sistema nervoso, com risco maior depois dos 60 anos e em diabéticos e '
       'hipertensos; na forma neuroinvasiva, cerca de um em cada dez morre. O '
       'vírus prefere neurônios profundos, do tálamo, da substância negra e do '
       'corno anterior: daí o tremor e a paralisia flácida assimétrica.',
       'Nas Américas desde 1999, é endêmico nos Estados Unidos, com pico no fim '
       'do verão. No Brasil, o Ministério da Saúde confirmou 17 casos humanos '
       'entre 2014 e 2026, a maioria no Piauí, e em 2026 houve transmissão local '
       'em Santa Catarina e em São Paulo.'),

    pg('tratamento', 'O tratamento a partir de agora',
       'Com a PCR para herpes negativa em líquor colhido depois de 72 horas de '
       'sintomas e outro diagnóstico confirmado, o aciclovir é suspenso. '
       'Hemoculturas negativas em 72 horas e um líquor que não é bacteriano '
       'permitem suspender ceftriaxona e ampicilina.',
       'Não há antiviral específico. Ribavirina, interferon, corticoide e '
       'imunoglobulina foram usados sem benefício conclusivo; o único ensaio '
       'randomizado de imunoglobulina rica em anticorpos contra o vírus foi '
       'inconclusivo (Gnann e cols., 2019).',
       'O desfecho depende do suporte: ventilação, prevenção de aspiração, '
       'trombose e úlcera por pressão, nutrição por via segura, controle do '
       'sódio e fisioterapia desde a UTI. A recuperação motora da poliomielite '
       'é lenta e muitas vezes incompleta.'),

    pg('recuperacao', 'Segunda e terceira semanas',
       'A febre acaba no sexto dia de internação. O tremor diminui, e ele volta '
       'a conversar, lúcido. O braço direito recupera força; a perna direita '
       'continua sem vencer a gravidade. A eletroneuromiografia da terceira '
       'semana mostra fibrilações na perna direita, sinal de denervação.'),

    pg('vigilancia', 'Vigilância e orientação na alta',
       'A febre do Nilo Ocidental é de notificação compulsória imediata no '
       'Brasil: o caso suspeito vai à vigilância em até 24 horas, antes da '
       'sorologia. Mesmo num caso importado, a vigilância investiga se houve '
       'exposição local, porque o vírus já circula no país.',
       'Não há transmissão por contato, e ele não precisa de isolamento em '
       'casa. A transmissão é pela picada e, raramente, por transfusão, '
       'transplante e via transplacentária; por isso ele não deve doar sangue '
       'por 120 dias, como recomenda o CDC. Não há vacina humana, e a esposa, '
       'sem sintomas, não precisa de exame.',
       'Fisioterapia, fonoaudiologia e acompanhamento neurológico continuam '
       'depois da alta; fraqueza e cansaço podem durar meses.'),

    pg('alta', 'Preparando a alta',
       'A equipe revê com ele e a esposa o que aconteceu: a viagem, a doença, a '
       'intubação e o que esperar da perna direita nos próximos meses.',
       conforme=('b2', ['f_reab', 'f_longa', 'f_longa'])),

    fim('f_reab', 'Alta para reabilitação',
        'Extubado no nono dia, sem pneumonia, ele sai no 21.º dia para um centro '
        'de reabilitação. Aos três meses anda com andador; a perna direita vence '
        'a gravidade, mas não a resistência.',
        'A intubação planejada evitou aspiração e pneumonia. O suporte não '
        'devolve o neurônio motor destruído; a força que volta vem dos que '
        'sobreviveram.', 'melhor'),

    fim('f_longa', 'Internação prolongada',
        'A pneumonia aspirativa custou dez dias de antibiótico e uma '
        'traqueostomia. Ele sai no 38.º dia para cuidados de continuidade, '
        'dependente para se mover e com alimentação por sonda.',
        'Aspiração e falência ventilatória somaram morbidade à lesão '
        'neurológica, que já era grave.', 'medio'),

    fim('f_obito', 'Óbito no quarto dia',
        'Mantido na máscara, ele aspira de novo, tem parada hipóxica e não '
        'sobrevive. A causa da encefalite não chegou a ser definida.',
        'Manter um suporte não invasivo numa via aérea que já não se protege '
        'levou à parada. Na fraqueza bulbar, a intubação vem antes da queda da '
        'saturação.', 'pior'),

    pagina('retrospectiva', 'Pontos de ensino', '',
        pontos(
            'Na hiponatremia do paciente neurológico, osmolalidade sérica, '
            'osmolalidade e sódio urinários e o volume classificam; secreção '
            'inapropriada de ADH num idoso febril e confuso aponta para o '
            'sistema nervoso.',
            'Com déficit focal, a tomografia vem antes da punção, e o '
            'antibiótico e o aciclovir vêm antes da tomografia.',
            'Paresia flácida, arrefléxica e assimétrica, com sensibilidade '
            'normal e sem nível, localiza no corno anterior: é poliomielite até '
            'que se ache a causa.',
            'Tálamo, substância negra e corno anterior na ressonância não são '
            'território do herpes e pedem a história de exposição, a começar '
            'pelo destino da viagem.',
            'Na fraqueza neuromuscular, a intubação é indicada pela regra '
            '20/30/40 e pela tosse, não pela saturação.',
            'Na doença neuroinvasiva pelo vírus do Nilo Ocidental, a IgM no '
            'líquor sustenta o diagnóstico; dengue prévia e vacina de febre '
            'amarela exigem a neutralização. O tratamento é suporte, e a '
            'notificação é imediata.'),
        so_kicker=True),

    pagina('referencias', 'Fontes e limites', '',
       p('Paciente, valores e percursos são ficcionais. A cena de abertura é '
         'uma ilustração gerada por inteligência artificial para este caso; não '
         'é fotografia nem documentação clínica.'),
       p('Ministério da Saúde, Nota Técnica n.º 79/2026-CGARB/DEDT/SVSA/MS '
         '(cenário epidemiológico, notificação imediata e critérios de caso). '
         'CDC, páginas para profissionais sobre diagnóstico e tratamento, '
         'consultadas em 26/09/2026. Sejvar e cols., //Emerg Infect Dis// 2003 '
         '(paralisia flácida). Tunkel e cols., IDSA, //Clin Infect Dis// 2004 e '
         '2008 (meningite bacteriana e encefalite). Lawn e cols., //Arch '
         'Neurol// 2001 (regra 20/30/40). Gnann e cols., //Clin Infect Dis// '
         '2019 (imunoglobulina). Spasovski e cols., //Eur J Endocrinol// 2014 '
         '(hiponatremia).'),
       '<p><a href="https://www.cdc.gov/west-nile-virus/hcp/diagnosis-testing/index.html" '
       'target="_blank" rel="noopener">CDC: diagnóstico</a> · '
       '<a href="https://www.cdc.gov/west-nile-virus/hcp/treatment-prevention/index.html" '
       'target="_blank" rel="noopener">CDC: tratamento</a> · '
       '<a href="https://www.gov.br/saude/pt-br/centrais-de-conteudo/publicacoes/notas-tecnicas/2026/nota-tecnica-no-79-2026.pdf" '
       'target="_blank" rel="noopener">Nota Técnica 79/2026</a></p>',
       p('Imagens, todas de outros pacientes, com setas adicionadas: '
         'radiografia de tórax e tomografia de crânio, Mikael Häggström, '
         'Wikimedia Commons, CC0; ressonância de encéfalo, James J. Sejvar '
         '(//Viruses// 2014), Wikimedia Commons, CC BY 3.0; ressonância da '
         'medula, JasonRobertYoungMD, Wikimedia Commons, CC BY-SA 4.0; '
         'eletrocardiograma, Ewingdo, Wikimedia Commons, CC BY-SA 4.0.'),
       so_kicker=True),
]

REVISAO = []

# Fontes conferidas na revisão das questões (22/10/2026):
# https://www.cdc.gov/west-nile-virus/hcp/diagnosis-testing/index.html
# https://www.cdc.gov/west-nile-virus/hcp/clinical-signs/index.html
# https://academic.oup.com/ejendo/article/170/3/G1/6668028
# https://pubmed.ncbi.nlm.nih.gov/12545029/

# Referência de construção dos itens (aplicação e opções plausíveis):
# https://www.nbme.org/sites/default/files/2021-02/NBME_Item%20Writing%20Guide_R_6.pdf
# https://pubmed.ncbi.nlm.nih.gov/15661693/
# https://jamanetwork.com/journals/jamaneurology/fullarticle/784803

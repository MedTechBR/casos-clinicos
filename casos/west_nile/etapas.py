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
                    'de três semanas na casa da filha, perto de Baton Rouge, Louisiana, em agosto. Ficava no quintal ao entardecer e sofreu muitas picadas de mosquito. Sem contato com morcegos, mordidas ou transfusões recentes.'),
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
        ex('Proteína C reativa', '38 mg/L', 'até 5 mg/L', True),
    ], introducao='Coleta inicial de rotina. Pela síndrome neurofebril, hemoculturas e tratamento empírico são providenciados em paralelo; as telas não representam espera entre essas medidas.'),

    painel('res1b', 'Primeiros exames', 'Urina e bioquímica', [
        ex('Urina', 'Densidade 1.018 · sem leucócitos · nitrito negativo · sem '
           'sangue · sem glicose'),
        ex('AST / ALT', '34 / 29 U/L', 'até 40 / 41 U/L'),
        ex('Lactato', '1,3 mmol/L', 'até 2,0 mmol/L'),
    ]),

    estudo('rx_adm', 'Radiografia de tórax',
           'Radiografia feita na chegada, à procura de um foco para a febre e a '
           'confusão.',
           IMG / 'rx_torax_normal.jpg',
           'Radiografia.',
           'Mikael Häggström · Wikimedia Commons · CC0 · setas adicionadas',
        [
         ((112, 972), (60, 820), '**Seio costofrênico** direito agudo e livre: sem derrame.', 12),
         ((300, 700), (160, 560), '**Pulmão direito** com trama vascular normal, sem consolidação.', -12),
         ((735, 820), (880, 700), '**Silhueta cardíaca** de tamanho normal.', 12),
        ],
        ['Campos pulmonares limpos, seios costofrênicos livres, área cardíaca '
         'normal.',
         'Sem opacidade focal ou derrame pleural visível.']),

    *ecg('ecg_evolucao',
         'A frequência cardíaca segue em 124 depois do antitérmico. A equipe '
         'registra um ECG.',
         IMG,
         'No caso, reavaliam-se febre, dor, volume e oxigenação; a frequência '
         'isolada não esclarece o quadro neurológico.'),

    pg('cobertura', 'Enquanto se organiza a punção',
       'Após hemoculturas, iniciam-se ceftriaxona, ampicilina e aciclovir intravenosos, com avaliação de dexametasona junto à primeira dose antibacteriana enquanto meningite bacteriana permanece possível. A imagem precede a punção pelo déficit focal; o tratamento não espera a tomografia.',
       'O sódio de 129 não explica sozinho o déficit focal. Monitoram-se sódio, diurese e balanço. A investigação da hiponatremia corre em paralelo à assistência neurológica; não se espera sua conclusão para colher líquor ou tratar.'),

    estudo('tc_evolucao', 'Tomografia de crânio',
        'Tomografia sem contraste antes da punção, pelo déficit focal e pela '
        'sonolência.',
        IMG / 'tc_cranio.png',
        'Corte axial e localizador.',
        'Mikael Häggström · Wikimedia Commons · CC0 · setas adicionadas',
        [
         ((268, 380), (35, 340), '**Ventrículos laterais**, escuros neste corte, sem dilatação.', 12),
         ((282, 210), (400, 100), '**Fissura inter-hemisférica** anterior na linha média: sem desvio.', -12),
         ((766, 466), (560, 250), '**Localizador**: a linha amarela marca o nível do corte, que passa pelos ventrículos laterais.', 12),
        ],
        ['Sem hemorragia, hidrocefalia, efeito de massa ou desvio da linha média.',
         'Sem alteração estrutural aguda identificada neste estudo.']),

    bifurcacao('b1', 'Decisão', 'Avaliação neurológica',
      'A TC não mostra lesão expansiva. A confusão oscila e a paresia persiste. Qual exame você prioriza?', [
      caminho('Punção lombar', 'lcr_prioritario',
              'Prioriza inflamação e infecção do sistema nervoso. O tratamento empírico já foi iniciado e o resultado não é presumido pela viagem.'),
      caminho('Eletroencefalograma', 'eeg_prioritario',
              'Pesquisa atividade epiléptica como causa da flutuação. É complementar: não substitui o líquor neste quadro febril e não deve atrasar sua coleta.'),
    ]),

    pg('lcr_prioritario', 'Coleta inicial',
       'A punção é realizada após revisão das contraindicações. Solicitam-se celularidade, glicose, proteína, Gram e cultura, além de investigação viral. Soro e alíquotas de líquor são reservados para estudos dirigidos pela exposição, em articulação com o laboratório de referência.',
       'A viagem e as picadas ampliam as possibilidades; não estabelecem uma causa. O histórico de dengue e vacina de febre amarela acompanha as amostras para orientar a interpretação sorológica.',
       segue='lcr'),

    pg('eeg_prioritario', 'Avaliação à beira do leito',
       'O EEG mostra lentificação difusa, sem crise eletrográfica no período registrado. Isso documenta disfunção cerebral, mas não determina a causa nem exclui eventos fora do registro.',
       'Enquanto o exame é organizado, a equipe prepara a punção, sem adiar antimicrobianos. O líquor segue para estudo celular, bioquímico, microbiológico e viral; soro e alíquotas são reservados para investigação relacionada à exposição.',
       segue='lcr'),

    painel('lcr', 'Líquor', 'Punção lombar', [
        ex('Pressão de abertura', '19 cmH₂O', '10–20 cmH₂O'),
        ex('Aspecto', 'Límpido, incolor'),
        ex('Células', '86/mm³ · neutrófilos 58% · linfócitos 42%', 'até 5/mm³', True),
        ex('Hemácias', '4/mm³'),
        ex('Proteína', '92 mg/dL', '15–45 mg/dL', True),
        ex('Glicose', '74 mg/dL {{(sérica 138 · relação 0,54)}}', 'relação acima de 0,4'),
        ex('Gram', 'Sem bactérias'),
    ], introducao='Punção lombar feita logo depois da tomografia.'),

    Q('p2', 1,
      'Como você interpreta o primeiro líquor?', [
      ('Perfil compatível com virose inicial, mantendo cobertura bacteriana enquanto se esclarece a causa', True),
      ('Perfil predominantemente piogênico, tornando a investigação viral uma prioridade posterior', False),
      ('Perfil sugestivo de meningite tuberculosa, pela combinação de proteína elevada e pleocitose moderada', False),
      ('Perfil favorece Listeria sobre virose, pelo predomínio neutrofílico no paciente idoso', False),
      ('Perfil favorece infecção fúngica crônica, pela glicorraquia de 74 mg/dL', False),
     ], [('Probabilidade e cobertura', 'A TC sem alteração aguda não exclui encefalite nem isquemia recente; após revisão das contraindicações clínicas, permite prosseguir com a punção. A radiografia não mostrou foco pulmonar. Pleocitose moderada, proteína elevada e glicose relativamente preservada cabem em virose inicial, inclusive com neutrófilos. O conjunto não exclui bactéria: idade, quadro clínico e antibiótico pré-punção justificam manter cobertura enquanto se obtêm testes para investigar a causa.'), ('Concorrentes', 'Meningite piogênica costuma ter maior celularidade e menor relação de glicose, embora haja sobreposição. Idade justifica cobrir Listeria, mas 58% de neutrófilos não a distingue de virose. TB e fungos permanecem diferenciais conforme contexto, porém evolução aguda e relação de glicose 0,54 não os priorizam; proteína 92 isoladamente também não os separa.'), ('Diagnósticos a comparar', 'Líquor inflamatório pode acompanhar infecção viral, bacteriana e outras inflamações. Neutrófilos podem predominar no início de uma virose. A duração dos sintomas, a glicose pareada com o sangue e a evolução ajudam; uma única proporção celular não decide a causa.')]),
    pg('reavaliacao_sodio', 'Reavaliação nas primeiras horas',
       'Após antitérmico, a frequência cai para 108, mas ele continua desorientado e a perna direita segue fraca. Não aparecem sinais de hipovolemia ou congestão, e a glicemia não explica a hiponatremia. O exame neurológico mantém prioridade, com tratamento e punção já realizados.',
       'Para classificar o sódio baixo, a equipe solicita osmolalidade sérica, osmolalidade e sódio urinários. TSH complementa a investigação; eventual avaliação adrenal considera horário de coleta e exposição a corticoide, sem retardar tratamento indicado.'),

    painel('sodio_dirigido', 'Investigação dirigida', 'Hiponatremia', [
        ex('Osmolalidade sérica', '270 mOsm/kg', '275–295 mOsm/kg', True),
        ex('Osmolalidade urinária', '456 mOsm/kg', '—', True),
        ex('Sódio urinário', '52 mmol/L', '—', True),
        ex('TSH', '2,1 µUI/mL', '0,4–4,5 µUI/mL'),
    ], introducao='Exames dirigidos pela hiponatremia identificada no painel básico, não um rastreio indiscriminado na admissão.'),

    Q('p1', 2,
      'Quais duas causas você mantém para a alteração do sódio?', [
      ('Antidiurese inapropriada associada à doença aguda', True),
      ('Deficiência de cortisol', True),
      ('Hiponatremia translocacional pela glicose de 138', False),
      ('Polidipsia primária', False),
      ('Baixo volume arterial efetivo por insuficiência cardíaca', False),
     ], [
      ('Duas possibilidades', 'A hipotonicidade com urina não diluída e Na urinário alto, em aparente euvolemia, favorece SIAD na doença neurológica aguda. Deficiência de cortisol pode produzir o mesmo padrão e ainda não foi investigada; não se pode fechar SIAD só com esses números.'),
      ('O que pesa contra as demais', 'Glicose 138 altera pouco o sódio e não explica osmolalidade baixa. Polidipsia isolada deveria permitir urina muito diluída. Insuficiência cardíaca não encontra congestão no exame. TSH normal torna hipotireoidismo primário grave improvável, mas não substitui avaliação adrenal.'),
     ]),

    pg('reexame', 'Na manhã seguinte',
       'Na manhã seguinte, a cefaleia e a desorientação diminuem, o sódio está em 132 e a febre é menos alta. Apesar disso, agora ele não consegue dobrar o joelho direito nem elevar o braço direito como fazia na admissão. Não é apenas um exame mais confiável: a esposa e a enfermagem observaram perda motora durante a noite.',
       'Mais acordado, ele colabora com o exame. Força grau 1 na perna direita, '
       '4 na esquerda, 4 no braço direito e 5 no esquerdo, com tônus flácido na '
       'perna direita. Patelar e aquileu abolidos à direita e diminuídos à '
       'esquerda; bicipitais presentes. Sensibilidade tátil, dolorosa e '
       'vibratória normais e simétricas, sem nível. Plantar em flexão. Urina '
       'espontaneamente. Há tremor de ação nas duas mãos.'),

    Q('p3', 3,
      'Quais três exames você prioriza após o novo exame neurológico?', [
      ('Ressonância do encéfalo', True),
      ('Ressonância da medula', True),
      ('Eletroneuromiografia com conduções motoras e sensitivas', True),
      ('Creatinoquinase', False),
      ('Anticorpo antirreceptor de acetilcolina', False),
      ('Nova tomografia de crânio sem contraste', False),
     ], [('Localizações a testar', 'RM de encéfalo: investiga a encefalite e o tremor, que uma neuropatia isolada não explica. RM de medula: procura acometimento de substância cinzenta e exclui compressão. ENMG: distingue padrão motor axonal de desmielinização e testa a preservação sensitiva; sozinha não separa sempre corno anterior de neuropatia motora axonal.'), ('Por que não estes agora', 'CK: pode investigar lesão muscular, mas não localiza adequadamente este padrão motor assimétrico com pleocitose. Anti-AChR: miastenia não integra febre, pleocitose e arreflexia assimétrica. Nova TC: sem mudança aguda sugestiva de hemorragia, acrescenta menos que RM para estas localizações.'), ('Onde está a lesão', 'Fraqueza pode vir do cérebro, da medula, dos nervos ou do músculo. Distribuição da força, reflexos, sensibilidade e líquor orientam a localização. A eletroneuromiografia e as imagens testam essa localização antes de definir o agente.')]),

    estudo('rm_encefalo', 'Ressonância de encéfalo',
           'Ressonância feita à tarde, à procura do lobo temporal da encefalite '
           'herpética e de uma causa para a paresia. Sequência FLAIR.',
           IMG / 'rm_encefalo_flair.png',
           'Ressonância · FLAIR axial · as setas brancas são do original.',
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
           'Ressonância · T2 axial da medula cervical · os círculos são do original.',
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
      'Quais duas hipóteses melhor integram a evolução e as imagens?', [
      ('Encefalomielite infecciosa integra a encefalopatia, o tremor e a paresia assimétrica', True),
      ('O acometimento temporal mantém HSV como concorrente enquanto se amplia a investigação da causa', True),
      ('Encefalite temporal por HSV com paresia de origem hemisférica é a melhor localização unificadora', False),
      ('Polirradiculoneuropatia pós-infecciosa explica melhor a fraqueza durante a fase febril', False),
      ('Mielite transversa inflamatória explica melhor a paresia pela alteração intramedular', False),
     ], [
      ('O conjunto', 'Núcleos profundos, tremor e substância cinzenta medular com fraqueza flácida assimétrica favorecem encefalomielite infecciosa, como a produzida por alguns arbovírus ou enterovírus. O discreto achado temporal mantém HSV em investigação e sustenta manter aciclovir até esclarecimento adequado.'),
      ('Localizações concorrentes', 'Uma paresia hemisférica explica mal a arreflexia e as lesões medulares. Polirradiculoneuropatia pós-infecciosa costuma aparecer após a infecção, com maior simetria; aqui a paresia acompanha a febre e há lesão intramedular. Mielite transversa pode ser aguda, mas o predomínio motor assimétrico sem nível sensitivo ou disfunção vesical favorece substância cinzenta motora em vez de síndrome transversa.'),
     ]),

    pg('respiracao', 'Segundo dia de internação',
       'Embora esteja mais atento e com menos cefaleia, no fim da tarde a tosse fica fraca e ele engasga com água. Frequência '
       'respiratória de 22, SpO₂ de 96% em ar ambiente, gasometria com pH 7,43 '
       'e pCO₂ de 38 mmHg. A capacidade vital caiu de 24 para 17 mL/kg em oito '
       'horas; pressão inspiratória máxima de −22 cmH₂O e expiratória de 34 '
       'cmH₂O.'),

    Q('p5', 5,
      'Quais duas conclusões orientam o suporte neste momento?', [
      ('A tendência da capacidade vital indica reserva ventilatória em deterioração', True),
      ('A disfunção bulbar reduz a segurança do suporte por máscara', True),
      ('A pCO₂ atual favorece manter o suporte sem intubação', False),
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
      caminho('Intubação planejada', 'r_via',
              'A progressão bulbar e ventilatória permite antecipar a via aérea '
              'em vez de esperar o colapso.'),
      caminho('Ventilação não invasiva', 'r_vni',
              'Disfagia e secreções tiram a margem de segurança da máscara.'),
      caminho('Observação na enfermaria', 'r_atraso',
              'A saturação não mede a reserva ventilatória nem a proteção '
              'contra aspiração.'),
    ]),

    pg('r_vni', 'Na UTI, com máscara',
       'Com ventilação não invasiva, acumula secreções e não consegue '
       'expectorar. Engasga de novo. A oxigenação se mantém, mas a proteção da '
       'via aérea piora.',
       segue='b_resgate'),

    pg('r_atraso', 'Reavaliação ainda na mesma noite',
       'A enfermagem percebe fala entrecortada, tosse ineficaz e fadiga ao sustentar a cabeça. A equipe transfere para UTI e interrompe a oferta oral. A saturação preservada não muda o risco bulbar.',
       segue='b_resgate'),

    pg('b_resgate', 'Mudança de estratégia',
       'Na UTI, a retenção de secreções persiste apesar do suporte inicial. A equipe realiza intubação após reconhecer a falha de proteção da via aérea. O manejo passa a incluir aspiração de secreções, via segura para alimentação e vigilância de infecção respiratória.',
       segue='exposicao'),

    pg('r_via', 'Terceiro dia',
       'Intubação planejada e ventilação na UTI. A febre começa a ceder, mas a fraqueza bulbar e dos membros persiste. A melhora da encefalopatia não permite suspender a vigilância respiratória.',
       segue='exposicao'),

    pg('exposicao', 'Quarto dia: evolução e resultados',
       'No quarto dia, a redução da sedação permite reconhecer a esposa e obedecer a comandos. Persistem a paresia assimétrica e a dificuldade para eliminar secreções. A família pergunta sobre extubação; a equipe explica que cognição e função motora podem recuperar em ritmos diferentes.',
       'A PCR do primeiro líquor para HSV, colhido no quinto dia de sintomas, é negativa; VZV e enterovírus também negativos. Pela alteração temporal discreta, mantém-se aciclovir até reavaliação e uma nova PCR para HSV, três dias após a primeira, também negativa. IgM para arbovírus está em processamento desde a admissão.'),

    Q('p6', 6,
      'Após rever a viagem e os resultados, quais dois exames você acrescenta?', [
      ('IgM para Nilo Ocidental no líquor', True),
      ('IgM para Nilo Ocidental no sangue', True),
      ('RT-PCR para Nilo Ocidental no sangue', False),
      ('IgG para Nilo Ocidental no soro', False),
      ('Repetição imediata da PCR de enterovírus no mesmo material', False),
      ('Antígeno NS1 de dengue', False),
     ], [
      ('Rendimento e especificidade', 'A pesquisa de IgM no sangue e no líquor é o primeiro passo nesta fase. Como o paciente já teve dengue e recebeu vacina contra febre amarela, um resultado positivo pode precisar de confirmação. O laboratório de referência escolhe o teste confirmatório; não é necessário conhecer sua técnica para reconhecer a suspeita e enviar as amostras.'),
      ('Por que não os demais', 'O envio é organizado com a rede de referência, conforme a disponibilidade local. O tratamento de suporte não espera esses resultados. Teste molecular no sangue (RT-PCR): baixa sensibilidade após a viremia curta no imunocompetente; negativa não exclui. IgG isolada: não data infecção nem resolve reatividade cruzada. Repetir enterovírus no mesmo material: sem falha técnica ou nova informação, rende menos que investigar outras causas. NS1: pesquisa dengue aguda, não confirma Nilo Ocidental nem infecção do sistema nervoso.'),
     ]),

    pg('virada', 'O diagnóstico',
       'Laboratório de referência: **IgM contra o vírus do Nilo Ocidental '
       'reagente no líquor e no soro**; IgM para dengue, febre amarela e '
       'encefalite de Saint Louis não reagentes. O laboratório interpreta como doença neuroinvasiva por Nilo Ocidental no contexto compatível. O teste de neutralização segue em processamento; o suporte e as decisões de antimicrobianos não aguardam sua conclusão.',
       'É doença neuroinvasiva pelo vírus do Nilo Ocidental, com encefalite e '
       'poliomielite. O vírus circula entre aves e mosquitos do gênero Culex, e '
       'o homem é hospedeiro acidental. Cerca de uma infecção em 150 atinge o '
       'sistema nervoso, com risco maior depois dos 60 anos e em diabéticos e '
       'hipertensos; na forma neuroinvasiva, cerca de um em cada dez morre. O '
       'vírus prefere neurônios profundos, do tálamo, da substância negra e do '
       'corno anterior: daí o tremor e a paralisia flácida assimétrica.',
       'O vínculo epidemiológico é a viagem recente, com exposição a mosquitos. Não se deduz o local de transmissão apenas do lugar de residência. A confirmação é discutida com o laboratório de referência, considerando reatividade cruzada entre flavivírus.'),

    pg('tratamento', 'O tratamento a partir de agora',
       'Com duas PCR para HSV negativas, reavaliação do achado temporal e causa alternativa sustentada, o aciclovir é suspenso. '
       'Culturas de sangue e líquor negativas, evolução, perfil liquórico e causa alternativa sustentada permitem suspender ceftriaxona e ampicilina após revisão conjunta; antibiótico antes da punção limita a sensibilidade da cultura.',
       'Não há antiviral específico. Ribavirina, interferon, corticoide e '
       'imunoglobulina foram usados sem benefício conclusivo; o único ensaio '
       'randomizado de imunoglobulina rica em anticorpos contra o vírus foi '
       'inconclusivo (Gnann e cols., 2019).',
       'O desfecho depende do suporte: ventilação, prevenção de aspiração, '
       'trombose e úlcera por pressão, nutrição por via segura, controle do '
       'sódio e fisioterapia desde a UTI. A recuperação motora da poliomielite '
       'é lenta e pode ser incompleta.'),

    pg('recuperacao', 'Segunda e terceira semanas',
       'A febre acaba no sexto dia de internação. O tremor diminui, e ele volta '
       'a conversar, lúcido. O braço direito recupera força; a perna direita '
       'continua sem vencer a gravidade. A eletroneuromiografia da terceira '
       'semana mostra fibrilações na perna direita, sinal de denervação. A neutralização solicitada ao laboratório de referência retorna no seguimento, com título oito vezes maior para Nilo Ocidental que para os demais flavivírus testados em paralelo, reforçando a identificação da causa.'),

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
       'Extubado no nono dia após recuperar tosse eficaz, ele ainda precisa de ajuda para transferências e avaliação de deglutição. Na terceira semana, a perna direita continua muito mais fraca que a esquerda. A alta depende da segurança funcional e do apoio disponível.',
       conforme=('b2', ['f_reab', 'f_longa', 'f_longa'])),

    fim('f_reab', 'Alta para reabilitação',
        'Sai no 21.º dia para reabilitação. Aos três meses usa andador e a perna direita vence a gravidade, mas não a resistência. Persistem fadiga e necessidade de adaptações em casa.',
        'O suporte antecipado controlou riscos respiratórios; a recuperação motora lenta decorre da doença. Este percurso não demonstra que a escolha determine uma recuperação específica.', 'melhor'),

    fim('f_longa', 'Reabilitação após reavaliação do suporte',
        'Após a mudança de estratégia respiratória, também é extubado e encaminhado à reabilitação. Há fraqueza e dependência para transferências, com seguimento de deglutição e força.',
        'O percurso exigiu reconhecer a limitação do suporte inicial. Aspiração é um risco, não uma consequência obrigatória; não se atribui uma sequela neurológica à escolha de máscara.', 'medio'),

    pagina('retrospectiva', 'Pontos de ensino', '',
        pontos(
            'Na hiponatremia do paciente neurológico, osmolalidade sérica, '
            'osmolalidade e sódio urinários e o volume classificam; secreção '
            'inapropriada de ADH num idoso febril e confuso aponta para o '
            'sistema nervoso.',
            'Com déficit focal, a tomografia vem antes da punção, e o '
            'antibiótico e o aciclovir vêm antes da tomografia.',
            'Paresia flácida, arrefléxica e assimétrica, com sensibilidade '
            'normal e sem nível, sugere acometimento motor, inclusive de corno anterior; a localização exige integrar exame, imagem e ENMG.',
            'O padrão de núcleos profundos e substância cinzenta medular amplia a causa além de HSV; a história de exposição precisa ser colhida desde a admissão.',
            'Na fraqueza neuromuscular, tendência da força ventilatória, tosse e proteção da via aérea orientam o suporte; números isolados não substituem a reavaliação.',
            'Na doença neuroinvasiva pelo vírus do Nilo Ocidental, a IgM no '
            'líquor sustenta o diagnóstico; dengue prévia e vacina de febre '
            'amarela exigem a neutralização. O tratamento é suporte, e a '
            'notificação é imediata.'),
        so_kicker=True),

    pagina('referencias', 'Fontes e limites', '',
       p('Paciente, valores e percursos são ficcionais. A cena de abertura é '
         'uma ilustração gerada por inteligência artificial para este caso; não '
         'é fotografia nem documentação clínica.'),
       p('Revisão em 23/10/2026: CDC, diagnóstico, manifestações e suporte; Ministério da Saúde, Nota Técnica 79/2026, notificação e classificação de caso. OMS, diretriz de meningite 2025, assistência inicial. Sejvar et al., 2003, PMID 12890318, série histórica sobre paralisia flácida; não é guideline atual. Gnann et al., 2019, ensaio de imunoglobulina. A classificação da hiponatremia usa osmolalidades, contexto e exclusões clínicas; não transforma SIAD em diagnóstico da causa.'),
       '<p><a href="https://www.cdc.gov/west-nile-virus/hcp/diagnosis-testing/index.html" '
       'target="_blank" rel="noopener">CDC: diagnóstico</a> · '
       '<a href="https://www.cdc.gov/west-nile-virus/hcp/treatment-prevention/index.html" '
       'target="_blank" rel="noopener">CDC: tratamento</a> · '
       '<a href="https://www.gov.br/saude/pt-br/centrais-de-conteudo/publicacoes/notas-tecnicas/2026/nota-tecnica-no-79-2026.pdf" '
       'target="_blank" rel="noopener">Nota Técnica 79/2026</a></p>',
       p('Imagens, com setas adicionadas: radiografia de tórax e tomografia de crânio, Mikael Häggström, Wikimedia Commons, CC0; ressonância de encéfalo, James J. Sejvar (//Viruses// 2014), Wikimedia Commons, CC BY 3.0; ressonância da medula, JasonRobertYoungMD, Wikimedia Commons, CC BY-SA 4.0; eletrocardiograma, Ewingdo, Wikimedia Commons, CC BY-SA 4.0.'),
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

# Revisão de evolução 23/10/2026: CDC diagnóstico, clínica e suporte;
# Sejvar et al., PMID 12890318 (fenótipo, série histórica, não guideline).

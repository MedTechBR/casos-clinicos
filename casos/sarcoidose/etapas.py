"""Hipercalcemia com PTH suprimido, calcitriol alto e adenopatia hilar.

Molde do //New England// lido em 26/09/2026 (ver
Artifacts/nejm-casos-classicos/GRAMATICA_LIDA_2026-09-26.md), no desenho do
piloto da leptospirose: apresentação curta, ficha do paciente com uma pista
enterrada (o colírio lubrificante), exame físico com os sinais vitais como
primeiro item e primeiros exames entregues prontos. Antes da metade, só duas
perguntas, de leitura e de categoria (o cálcio, o divisor do PTH); a urina e
os exames pedidos com o PTH suprimido são páginas de discussão. A âncora
é a da equipe naquele momento: adenopatia hilar, perda de peso, DHL alta e
calcitriol alto num homem de 41 anos são linfoma até a biópsia. O granuloma
não necrosante do EBUS vira o caso; o nome aparece pela primeira vez na
pergunta que interpreta o tecido, depois da metade. O olho, que estava na
ficha, só é examinado no rastreio de base.

Paciente ficcional. Critérios e condutas: ATS 2020 (diagnóstico e
rastreio), ERS 2021 (tratamento), Walker e Shane, JAMA 2022 (hipercalcemia).
"""
from pathlib import Path

from motor.estudo_imagem import estudo
from motor.etapas import (alt, bifurcacao, caminho, capa, desfecho, op, p,
                          pagina, painel, par, pareamento, pergunta, pontos,
                          topicos, vitais)

TITULO = 'Entre a sede e o fôlego'
RODAPE = 'Paciente ficcional · evoluções simuladas para ensino'
COR = '#0d9488'
IMG = Path(__file__).parent / 'img'
BANCO = []
MOLDE = 'nejm'
CENA = 'cena.png'


def credito_meta(meta):
    """Autor e licença, sem o link: o nome do arquivo no Commons diz o
    diagnóstico. A fonte completa fica na última tela."""
    import json
    m = json.loads(Path(meta).read_text())
    return m['autor'] + ' · Wikimedia Commons · ' + m['licenca'] + ' · setas adicionadas'


def _fonte(meta, rotulo):
    import json
    m = json.loads(Path(meta).read_text())
    return '<a href="' + m['fonte'] + '" target="_blank" rel="noopener">' + rotulo + '</a>'


def pg(k, titulo, *textos, segue='', conforme=None):
    return pagina(k, titulo, '', *(p(t) for t in textos), so_kicker=True,
                  segue=segue, conforme=conforme)


def disc(k, titulo, *textos, segue=''):
    """Página didática sem pergunta, no estilo das do NEJM."""
    return pagina(k, 'Discussão', titulo, *(p(t) for t in textos), segue=segue)


def Q(k, n, enunciado, opcoes, explicacao, segue=''):
    """Pergunta no molde do NEJM: alternativas curtas, sem comentário cada
    uma, e uma explicação só, em seções (subtítulo, texto)."""
    return pergunta(k, f'Pergunta {n}', enunciado,
                    [alt(t, certa=ok) for t, ok in opcoes],
                    explicacao=explicacao, segue=segue)


def ex(nome, valor, ref='—', alt_=False):
    return op(nome, resultado=valor, referencia=ref, alterado=alt_)


def fim(k, titulo, texto, porque, qualidade):
    return desfecho(k, titulo, p(texto), qualidade=qualidade, porque=porque,
                    fecho='retrospectiva')


ETAPAS = [
    capa(TITULO, fundo=CENA, kicker='Caso interativo',
         selo='Paciente ficcional · procedência e créditos na última tela'),

    pg('historia', 'Apresentação',
       'Rafael, 41 anos, analista administrativo em Fortaleza, é trazido pela '
       'esposa ao pronto-socorro com náuseas, intestino preso há cinco dias e '
       'dificuldade para se concentrar no trabalho. Há uma semana tem sede o '
       'tempo todo e acorda três vezes à noite para urinar.',
       'Há dois meses tem tosse seca, que vai e volta, e se cansa nas '
       'caminhadas do fim de semana. Perdeu 4 kg. Há três semanas, numa '
       'unidade de pronto atendimento, recebeu xarope e o diagnóstico de tosse '
       'pós-viral.',
       'Nega febre, suor noturno, escarro com sangue, dor no peito, vômitos '
       'repetidos, diarreia, cólica renal e caroços no pescoço.'),

    pagina('ficha', 'Ficha do paciente', '',
           topicos(('Antecedentes', 'Hipertenso há cinco anos. Nunca teve '
                    'cálculo renal. Nunca internou.'),
                   ('Medicações', 'Hidroclorotiazida 25 mg/dia. Colecalciferol '
                    '5.000 UI/dia há três meses, por conta própria, porque ouviu '
                    'que dava disposição. Colírio lubrificante há um mês, pelos '
                    'olhos vermelhos e ardendo no fim do dia, que atribui ao '
                    'computador. Não usa carbonato de cálcio, lítio nem antiácidos.'),
                   ('Hábitos', 'Não fuma. Uma ou duas cervejas no fim de semana. '
                    'Caminhava 5 km aos sábados até dois meses atrás.'),
                   ('Vida social', 'Casado, dois filhos. Trabalha em escritório '
                    'e nunca lidou com pedra, areia, fundição ou metais. Há cinco '
                    'meses ajudou a limpar um galinheiro abandonado no sítio do '
                    'sogro, no sertão central. Nunca saiu do Nordeste. Não conhece '
                    'contato com tuberculose.'),
                   ('Família', 'Pai com câncer de próstata aos 70 anos. Mãe com '
                    'hipotireoidismo. Um irmão saudável.')),
           so_kicker=True),

    pagina('exame', 'Exame físico', '',
           vitais(('Pressão arterial', '104/66', False),
                  ('Frequência cardíaca', '102', True),
                  ('Frequência respiratória', '20', False),
                  ('Temperatura', '36,8 °C', False),
                  ('SpO₂ em ar ambiente', '95%', False),
                  ('Peso', '74 kg', False)),
           topicos(('Estado geral', 'Mucosas secas. Orientado, com atenção lenta; '
                    'sem déficit focal.'),
                   ('Pescoço e linfonodos', 'Tireoide normal. Sem adenomegalia '
                    'cervical, supraclavicular, axilar ou inguinal.'),
                   ('Respiratório', 'Murmúrio presente, raros estertores finos '
                    'nas bases.'),
                   ('Coração', 'Rítmico, sem sopros, sem turgência jugular.'),
                   ('Abdome', 'Ruídos diminuídos, indolor, sem massas nem '
                    'visceromegalias.'),
                   ('Pele e membros', 'Sem lesões de pele, sem edema, sem sinovite.')),
           so_kicker=True),

    painel('res1', 'Primeiros exames', 'Sangue', [
        ex('Hemoglobina', '12,8 g/dL', '13,5–17,5 g/dL', True),
        ex('Leucócitos / linfócitos', '5.200 / 780 por mm³', '4.000–11.000 / 1.000–4.800', True),
        ex('Cálcio total / albumina', '13,6 mg/dL / 4,0 g/dL', 'Ca 8,5–10,5 · albumina 3,5–5,0', True),
        ex('Cálcio ionizado', '1,72 mmol/L', '1,12–1,32 mmol/L', True),
        ex('Fósforo', '4,1 mg/dL', '2,5–4,5 mg/dL'),
        ex('Ureia / creatinina', '72 / 2,0 mg/dL {{(creatinina 1,0 há um ano)}}', 'até 45 / 1,3 mg/dL', True),
        ex('Sódio / potássio / cloro', '146 / 3,5 / 106 mmol/L', 'Na 135–145 · K 3,5–5,0 · Cl 98–107', True),
        ex('Glicemia', '98 mg/dL', '70–99 mg/dL'),
        ex('Desidrogenase láctica', '268 U/L', '135–225 U/L', True),
    ]),

    painel('res1b', 'Primeiros exames', 'Urina, gasometria e ECG', [
        ex('Débito urinário na emergência', '220 mL/h nas duas primeiras horas, antes do soro', '—', True),
        ex('Urina', 'Densidade 1.004 · sem glicose · sem proteína · sedimento sem cilindros', '—', True),
        ex('Osmolalidade urinária / sérica', '190 / 302 mOsm/kg', 'sérica 275–295', True),
        ex('Fração de excreção de ureia', '29%', 'abaixo de 35% sugere pré-renal', True),
        ex('Gasometria venosa', 'pH 7,40 · pCO₂ 41 mmHg · HCO₃ 25 mmol/L', '—'),
        ex('Eletrocardiograma', 'Ritmo sinusal, 102 bpm · QTc 340 ms · sem bloqueios', '—', True),
    ]),

    estudo('rx_hilos', 'Radiografia de tórax',
           'Radiografia feita na chegada, pela tosse de dois meses e pela perda '
           'de peso. Olhe os hilos nas duas incidências antes de ler os achados.',
           IMG / 'rx_hilos.jpg',
           'Radiografia frontal e lateral de outro paciente · comparação didática.',
           credito_meta(IMG / 'rx_hilos.jpg.json'),
        [
         ((176, 280), (70, 180), '**Hilo direito** aumentado, de contorno lobulado.', 12),
         ((353, 273), (470, 180), '**Hilo esquerdo** também aumentado: o alargamento é bilateral e simétrico.', -12),
         ((735, 315), (900, 240), 'Na incidência lateral, a **massa hilar** se sobrepõe à sombra cardíaca.', 12),
        ],
        ['Adenopatia hilar bilateral e simétrica, com parênquima sem '
         'opacidades e sem derrame.',
         'Com perda de peso e tosse, a equipe pensa primeiro em linfoma; '
         'tuberculose ganglionar, histoplasmose e metástase ficam no '
         'diferencial.']),

    Q('p1', 1,
      'Diante da poliúria e da lesão renal, qual mecanismo integra melhor os primeiros exames?', [
      ('Diurese aquosa por defeito de concentração, com depleção de volume', True),
      ('Diurese osmótica por solutos filtrados, com lesão renal secundária', False),
      ('Polidipsia primária, com hipercalcemia por hemoconcentração', False),
      ('Lesão glomerular, com perda urinária de proteínas e cálcio total elevado', False),
      ('Retenção de cálcio pela lesão renal como evento inicial', False),
    ], [('Integração', 'Urina a 190 mOsm/kg diante de plasma a 302 e Na 146 indica perda de água apesar do estímulo para concentrar. A hipercalcemia pode reduzir a resposta renal ao ADH; desidratação e vasoconstrição renal contribuem para a creatinina.'), ('Comparação', 'A diurese osmótica costuma elevar a osmolalidade urinária; não há glicosúria. Polidipsia não explica bem a hiperosmolalidade, e o ionizado alto afasta aumento apenas por hemoconcentração. Sedimento e proteinúria não sustentam lesão glomerular. Não é preciso esperar Ca 14 para tratar este paciente sintomático.')]),

    disc('urina', 'O que a urina diz',
         'Rafael está desidratado, com mucosas secas e sódio de 146 mmol/L. '
         'Nessa situação o rim deveria poupar água, e a urina sai a 220 mL/h, '
         'com densidade de 1.004 e osmolalidade de 190 mOsm/kg, mais diluída '
         'que o plasma de 302. Glicemia de 98 mg/dL e urina sem glicose afastam '
         'diurese osmótica; na polidipsia primária o sódio seria normal ou baixo.',
         'O conjunto é compatível com defeito de concentração, ao qual a hipercalcemia pode contribuir: '
         'ele ativa o receptor sensor de cálcio na alça de Henle e no ducto '
         'coletor e pode reduzir a resposta ao hormônio antidiurético. A melhora da concentração urinária após corrigir o cálcio apoiaria esse mecanismo. O tiazídico não '
         'explica a urina diluída; ele é usado, ao contrário, para reduzir esse '
         'tipo de poliúria.',
         'A creatinina dobrou em relação à de um ano atrás. A fração de excreção '
         'de ureia de 29% indica componente pré-renal e substitui a de sódio, que '
         'o tiazídico distorce. Somam-se a água perdida na urina e a '
         'vasoconstrição renal causada pelo cálcio. Sedimento sem cilindros não '
         'sugere necrose tubular.'),

    pg('evolucao1', 'Primeiras 24 horas',
       'Com soro fisiológico guiado pela diurese e sem hidroclorotiazida nem '
       'colecalciferol, Rafael fica mais atento. O cálcio cai para 12,4 mg/dL, '
       'a creatinina para 1,6 mg/dL e o sódio para 141 mmol/L.',
       'O PTH, colhido na chegada, é de 6 pg/mL (referência 15 a 65).'),

    Q('p3', 2,
      'PTH 6 pg/mL e hipercalcemia persistente. Quais três exames você prioriza agora?', [
      ('PTHrP', True),
      ('25-OH-D e 1,25-(OH)₂D, em conjunto', True),
      ('Eletroforese e cadeias leves livres séricas', True),
      ('Cintilografia de paratireoides com sestamibi', False),
      ('Cintilografia óssea para pesquisar mieloma', False),
      ('Repetição do PTH após semanas sem tiazídico', False),
    ], [('Indicados', 'PTHrP pesquisa mecanismo humoral tumoral; as duas formas da vitamina D separam excesso de estoque de produção de calcitriol. Eletroforese e cadeias leves investigam doença plasmocitária diante de anemia, hipercalcemia e disfunção renal.'), ('Menor rendimento agora', 'Sestamibi localiza glândulas após diagnóstico bioquímico dependente de PTH, incompatível com esta supressão. Cintilografia óssea tem baixo rendimento nas lesões puramente líticas do mieloma. Repetir PTH semanas depois não deve adiar a investigação: os medicamentos podem agravar, mas não encerram a investigação desta hipercalcemia persistente.')]),

    disc('pedidos', 'A próxima rodada', 'A equipe encaminha as dosagens e a investigação de proteínas séricas. Acrescenta calciúria de 24 horas e revê a radiografia realizada na chegada pela tosse e perda de peso. A necessidade de tomografia será definida por esses achados.'),

    painel('res2', 'Investigação', 'Segundo e terceiro dias', [
        ex('PTHrP', 'Não detectado', 'não detectado'),
        ex('25-hidroxivitamina D', '38 ng/mL', '20–50 ng/mL'),
        ex('1,25-di-hidroxivitamina D', '104 pg/mL', '18–72 pg/mL', True),
        ex('Eletroforese de proteínas', 'Sem componente monoclonal · gamaglobulina policlonal discretamente elevada', 'sem pico'),
        ex('Cadeias leves livres', 'Relação kappa/lambda 1,3', '0,26–1,65'),
        ex('Calciúria de 24 horas', '410 mg', 'abaixo de 300 mg', True),
    ]),

    disc('leitura', 'O que voltou', 'Calciúria de 410 mg em 24 horas. PTHrP não detectado, eletroforese sem componente monoclonal e relação kappa/lambda de 1,3. A equipe compara os mecanismos possíveis antes de escolher o alvo da biópsia.'),

    Q('p4', 3,
      'Calcitriol 104, 25-OH-D 38, PTHrP não detectado. Quais duas hipóteses ainda integram hipercalcemia e adenopatia?', [
      ('Doença granulomatosa com produção extrarrenal de calcitriol', True),
      ('Linfoma com produção aumentada de calcitriol', True),
      ('Intoxicação por colecalciferol como explicação unificadora', False),
      ('Hipercalcemia humoral por PTHrP', False),
      ('Hiperparatireoidismo primário agravado pelo tiazídico', False),
    ], [('O mecanismo não é a etiologia', 'Calcitriol alto com PTH suprimido favorece produção pouco regulada, possível tanto em granulomas quanto em linfomas. A simetria hilar favorece a primeira categoria, mas perda de peso e adenopatia justificam tecido.'), ('Alternativas próximas', '25-OH-D normal enfraquece intoxicação por colecalciferol; o suplemento ainda pode fornecer substrato. PTHrP não detectado e PTH suprimido tornam os outros dois mecanismos menos prováveis, sem excluir neoplasia por outra via.')]),

    estudo('tc', 'Tomografia de tórax',
           'No quarto dia, com creatinina de 1,3 mg/dL, a equipe faz tomografia '
           'de tórax e abdome com contraste para estadiar a adenopatia e '
           'escolher onde biopsiar. Com perda de peso, DHL alta e calcitriol '
           'produzido fora do rim, a hematologia registra linfoma como hipótese '
           'principal.',
           IMG / 'tc_mediastino.jpg',
           'Tomografia com contraste de outro paciente, janela de mediastino · comparação didática.',
           credito_meta(IMG / 'tc_mediastino.jpg.json'),
        [
         ((357, 336), (250, 262), 'Linfonodos **hilares direitos** aumentados e confluentes, sem necrose central.', 12),
         ((668, 395), (742, 470), 'O mesmo no **hilo esquerdo**: a adenopatia é bilateral e simétrica.', -12),
         ((493, 392), (392, 482), 'Linfonodo **subcarinal** aumentado, entre os brônquios principais.', 12),
        ],
        ['Linfonodos hilares bilaterais, subcarinais e paratraqueais, simétricos, '
         'até 2,4 cm, sem necrose e sem calcificação. Na janela de pulmão, '
         'pequenos nódulos ao longo dos feixes broncovasculares e das fissuras. '
         'No abdome, fígado e baço normais, sem linfonodos retroperitoneais.',
         'Os linfonodos do mediastino são o alvo da biópsia. O diferencial '
         'registrado: linfoma, tuberculose ganglionar e histoplasmose.']),

    bifurcacao('b1', 'Decisão', 'Como chegar ao tecido',
      'Rafael está estável, com cálcio de 11,6 mg/dL e sem ameaça '
      'respiratória. Como conduzir a definição da causa?', [
      caminho('Ecobroncoscopia com punção dos linfonodos, citometria e '
              'culturas', 'tecido',
              'Chega aos linfonodos do mediastino sem cirurgia e colhe material '
              'para linfoma, micobactéria e fungo antes de qualquer '
              'imunossupressão.'),
      caminho('Prednisona agora; biópsia só se o cálcio não cair',
              'empirico',
              'A resposta ao corticoide não define a causa. Ele pode modificar a amostra e agravar infecções ainda não reconhecidas; o risco depende da doença e da exposição.'),
      caminho('Atribuir ao suplemento, dar alta e reavaliar', 'suplemento',
              'O colecalciferol soma, mas não produz linfonodo nem calcitriol '
              'alto com 25-hidroxi normal.'),
    ]),

    pg('empirico', 'Dez dias depois',
       'Com prednisona 40 mg/dia, o cálcio cai e a tosse melhora. A causa continua sem confirmação. A equipe organiza a amostragem e informa ao patologista o tratamento recebido.',
       segue='amostra_limitada'),

    pg('suplemento', 'Dez semanas depois',
       'Rafael saiu com hidratação oral, sem suplemento e sem tiazídico, e '
       'retorno marcado para dois meses. O retorno previsto não ocorre. Na décima semana, volta com cálcio de 13,1 mg/dL, '
       'creatinina de 1,9 mg/dL, falta de ar ao caminhar no plano e dor nos '
       'dois olhos com a luz. É readmitido e hidratado de novo; a radiografia e '
       'a tomografia são repetidas.'),

    estudo('rx_tc', 'Radiografia e tomografia na readmissão',
           'Exames repetidos pela falta de ar nova. Compare com a radiografia '
           'da chegada, que mostrava só os hilos, com o parênquima limpo.',
           IMG / 'rx_tc.jpg',
           'Radiografia e TC coronal de outro paciente · comparação didática.',
           credito_meta(IMG / 'rx_tc.jpg.json'),
        [
         ((360, 110), (470, 35), '**Opacidades reticulonodulares** densas, que predominam nos campos superiores.', -12),
         ((638, 257), (575, 420), 'Na TC coronal, **conglomerado peri-hilar** com espessamento peribroncovascular.', 12),
         ((905, 170), (985, 60), '**Micronódulos** difusos, de distribuição perilinfática.', -12),
        ],
        ['Progressão do acometimento pulmonar: opacidades reticulonodulares de '
         'predomínio superior, conglomerados peri-hilares e micronódulos '
         'perilinfáticos.',
         'A TC inicial já mostrava pequenos nódulos no pulmão. Na readmissão, a extensão e a confluência aumentaram; não se trata apenas de linfonodos aumentados. A ecobroncoscopia é feita na mesma internação.'],
        segue='tecido'),

    pg('tecido', 'A ecobroncoscopia',
       'Punções dos linfonodos subcarinal e hilar direito: granulomas não '
       'necrosantes, compactos, sem células atípicas. A citometria de fluxo não '
       'mostra população clonal.',
       'Pesquisa de bacilo álcool-ácido resistente e de fungos, teste molecular '
       'rápido para tuberculose e imunodifusão para //Histoplasma// negativos. '
       'Prova tuberculínica de 0 mm. Anti-HIV não reagente. As culturas para '
       'micobactéria e fungo seguem em incubação por seis a oito semanas.'),

    estudo('granuloma', 'O granuloma',
           'Lâmina do bloco celular da punção. Para comparação, microfotografia '
           'de tecido de outro paciente com o mesmo padrão. Descreva o granuloma '
           'antes de ler a interpretação.',
           IMG / 'granuloma.jpg',
           'Tecido de outro paciente · comparação morfológica.',
           credito_meta(IMG / 'granuloma.jpg.json'),
        [
         ((420, 330), (330, 55), '**Histiócitos epitelioides**: citoplasma amplo e pálido, núcleo oval, agrupados de forma compacta.', -12),
         ((500, 628), (330, 700), '**Coroa de linfócitos**, pequenos e escuros, na periferia do granuloma.', 12),
         ((540, 470), (800, 670), '**Centro celular, sem necrose**: é o que define o granuloma como não necrosante.', 12),
        ],
        ['Granuloma não necrosante: agregado compacto de histiócitos '
         'epitelioides com coroa linfocitária, sem necrose central.',
         'A lâmina descreve uma forma de reação, não a causa. O diagnóstico '
         'junta a lâmina, as culturas e a história.']),

    Q('p5', 4,
      'Como o EBUS com granulomas não necrosantes e citometria sem clone modifica o diferencial?', [
      ('Favorece sarcoidose; infecções granulomatosas ainda exigem seguimento', True),
      ('Favorece histoplasmose sobre as demais causas pela exposição ao galinheiro', False),
      ('Mantém linfoma como primeira hipótese, pois a citometria tem pouco valor', False),
      ('Favorece tuberculose sobre sarcoidose pela frequência regional', False),
      ('Permite atribuir o cálcio ao suplemento, com adenopatia incidental', False),
    ], [('Peso relativo', 'Adenopatia simétrica, nódulos perilinfáticos e granulomas favorecem sarcoidose. Culturas negativas não a confirmam: ajudam a excluir alternativas; resultados pendentes mantêm incerteza.'), ('O que persiste', 'Galinheiro sustenta pesquisa de fungos, sem tornar histoplasmose a primeira hipótese. Teste molecular negativo não exclui tuberculose. Citometria sem clone reduz alguns linfomas, mas não elimina Hodgkin; progressão discordante pode exigir nova biópsia. O suplemento não integra a histologia e o tórax.')]),

    pg('virada', 'O diagnóstico',
       'O conjunto de manifestações clínicas, distribuição torácica e granulomas não necrosantes favorece sarcoidose. A investigação das alternativas não encontrou outra causa mais consistente até aqui; a equipe acompanhará as culturas e reavaliará o diagnóstico se houver evolução discordante.',
       'A sarcoidose é uma doença granulomatosa de causa desconhecida. Atinge '
       'pulmão e linfonodos do tórax em mais de 90% dos casos e, com frequência, '
       'olho, pele, fígado, rim e coração. Os macrófagos do granuloma expressam '
       'a 1-alfa-hidroxilase e convertem 25-hidroxivitamina D em calcitriol sem '
       'obedecer ao PTH: sobem a absorção intestinal de cálcio, a reabsorção '
       'óssea e a calciúria.',
       'É o que se viu: calcitriol alto com estoque normal, calciúria de 410 mg, '
       'linfopenia compatível com inflamação sistêmica e adenopatia '
       'hilar simétrica com nódulos ao longo dos feixes. O colecalciferol deu '
       'substrato para essa via, e o tiazídico pode reduzir a excreção renal de cálcio. Ambos podem ter agravado a hipercalcemia, sem explicar sozinhos a doença do tórax.'),

    Q('p6', 5,
      'Com os exames iniciais disponíveis, quais três avaliações priorizar para extensão e referência funcional?', [
      ('Lâmpada de fenda', True),
      ('Espirometria e DLCO', True),
      ('Fosfatase alcalina', True),
      ('Holter de 24 horas', False),
      ('PET-CT cardíaco', False),
      ('Enzima conversora de angiotensina seriada', False),
    ], [('Prioridades', 'Lâmpada de fenda pesquisa uveíte: o olho vermelho persistente já torna a avaliação dirigida. Espirometria e DLCO quantificam o comprometimento diante de tosse e dispneia. Fosfatase alcalina pesquisa acometimento hepático pouco sintomático.'), ('Sem indicação inicial', 'Holter e PET cardíaco ficam para suspeita cardíaca; não há síncope, palpitações ou bloqueio no ECG já disponível. Enzima conversora seriada não define atividade nem deve guiar tratamento isoladamente. Não é necessário pedir de novo o ECG normal apenas para completar uma lista.')]),

    pg('extensao', 'O rastreio',
       'ECG sem bloqueio nem arritmia. Fosfatase alcalina e transaminases '
       'normais. Creatinina de 1,2 mg/dL. Capacidade vital forçada de 83% e '
       'difusão de monóxido de carbono de 64% do previsto.',
       'Na consulta oftalmológica, Rafael conta que o colírio lubrificante não '
       'resolveu e que a luz do computador passou a incomodar. Na lâmpada de '
       'fenda, células 2+ na câmara anterior dos dois olhos e precipitados '
       'ceráticos grandes, sem sinéquias. Acuidade 20/25 em cada olho, pressão '
       'intraocular de 16 e 17 mmHg, fundo sem vitreíte e tomografia de '
       'coerência óptica sem edema macular.',
       'Uveíte anterior granulomatosa bilateral: colírio de prednisolona 1% e '
       'cicloplégico.'),

    Q('p7', 6,
      'Qual dado pesa mais para tratar sistemicamente, em vez de acompanhar apenas o tórax?', [
      ('Hipercalcemia sintomática com repercussão renal', True),
      ('Linfonodos mediastinais de até 2,4 cm', False),
      ('DLCO de 64% isoladamente, sem considerar a evolução', False),
      ('Uveíte anterior com acuidade preservada, isoladamente', False),
      ('Linfopenia periférica de 780/mm³', False),
    ], [('Indicação', 'A ameaça metabólica e renal já demonstrada é a indicação mais forte. A extensão radiológica e a DLCO ajudam a acompanhar, mas não substituem sintomas, trajetória e risco de órgão.'), ('Olho e segurança', 'A uveíte anterior descrita recebe tratamento tópico e avaliação oftalmológica; não determina, sozinha, prednisona sistêmica. Se iniciada antes das culturas finais, a decisão exige revisão da probabilidade de infecção e conferência dos resultados. Evitar reposição automática de cálcio e vitamina D neste contexto.')]),

    disc('reducao', 'O plano da redução',
         'A prednisona sai devagar, ao longo de meses, e a doença pode voltar '
         'no caminho. Antes de chamar de recidiva e escalar, confere-se a '
         'adesão, sobretudo ao tratamento local, e se exclui infecção, que o '
         'corticoide facilita e que pode imitar inflamação.',
         'Recidivas persistentes apesar do tratamento local adequado ou dependência de corticoide podem justificar um poupador. Pela ERS '
         '(2021), o metotrexato é a segunda linha, com ácido fólico e controle de '
         'hemograma, função hepática e renal; o anti-TNF, como o infliximabe, vem '
         'depois dele. A hidroxicloroquina tem papel na pele e na '
         'hipercalcemia, não na uveíte.',
         'Voltar a doses altas por tempo indefinido é o que o poupador evita: '
         'perda óssea, hiperglicemia, catarata e glaucoma.'),

    pg('evolucao2', 'Oito semanas depois',
       'Cálcio 9,8 mg/dL, creatinina 1,1 mg/dL. Culturas finais sem '
       'crescimento. A inflamação ocular está controlada e Rafael voltou a '
       'caminhar. Começa a redução da prednisona.',
       'Quatro semanas depois, durante a redução, a dor no olho direito '
       'volta. Os exames de sangue estão normais, e Rafael quer manter o '
       'esquema porque o resto melhorou.'),

    bifurcacao('b2', 'Decisão', 'O olho durante a redução',
      'Como responder à volta da dor ocular?', [
      caminho('Reavaliar na oftalmologia no mesmo dia e ajustar pelo exame',
              'controle',
              'Cada órgão tem seu marcador; o do olho é a lâmpada de fenda.'),
      caminho('Manter a redução e antecipar só o cálcio e a espirometria',
              'visao',
              'Nenhum desses exames vê a câmara anterior.'),
    ]),

    pg('controle', 'Reavaliação oftalmológica',
       'No mesmo dia, há células 2+ no olho direito, pressão de 18 mmHg e ausência de edema macular. O colírio tinha acabado havia uma semana. O tratamento tópico é retomado e ajustado, com reavaliação próxima; esse episódio isolado não determina novo imunossupressor.',
       'Nos dois meses seguintes, apesar de adesão confirmada, há novas recidivas documentadas durante tentativas de redução do tratamento e dificuldade de reduzir a prednisona. Após discussão entre as equipes, inicia-se metotrexato como poupador, com ácido fólico e monitorização.', segue='f1'),

    pg('visao', 'Três semanas depois',
       'Rafael volta com visão turva no olho direito. Acuidade 20/80, células '
       '3+, sinéquias posteriores novas, pressão de 28 mmHg e edema macular na '
       'tomografia de coerência óptica.',
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
       'Pressão de 18 mmHg e acuidade 20/40, com edema em regressão. A recidiva '
       'grave antecipa o metotrexato.',
       segue='f1b'),

    pg('resgate_tardio', 'Uma semana depois',
       'A pressão caiu, mas a dor e o borramento continuam: células e edema '
       'macular seguem ativos. O resgate integrado começa com uma semana de '
       'atraso.',
       segue='f2'),

    fim('f1', 'Controle com visão preservada',
        'Nos seis meses seguintes ao início do metotrexato, a prednisona chega a 5 mg/dia. Cálcio e '
        'creatinina normais, visão 20/20, espirometria estável.',
        'A causa foi avaliada com tecido adequado e investigação das alternativas. O seguimento de cada órgão permitiu reconhecer a recidiva ocular no dia em que apareceu.',
        'melhor'),

    fim('f1b', 'Controle após recidiva grave',
        'A visão do olho direito volta a 20/25 em três meses. Metotrexato '
        'mantido, prednisona em redução.',
        'O resgate imediato do edema macular preservou a visão, mas a '
        'recidiva grave poderia ter sido vista três semanas antes.', 'medio'),

    fim('f2', 'Perda visual residual',
        'A inflamação e a pressão estão controladas, mas a acuidade direita '
        'estabiliza em 20/50, com alterações maculares documentadas.',
        'Tratar só a pressão deixou o edema macular ativo por mais uma '
        'semana.', 'pior'),

    pagina('retrospectiva', 'Pontos de ensino', '',
        pontos(
            'Na hipercalcemia confirmada, interpretar o PTH separa os mecanismos. PTH suprimido direciona exames conforme a hipótese; cintilografia de paratireoides não substitui o diagnóstico bioquímico.',
            'Urina diluída apesar da desidratação sugere defeito de concentração. A hipercalcemia pode contribuir; evolução e resposta à correção ajudam a interpretar a lesão renal.',
            '1,25-di-hidroxivitamina D alta com 25-hidroxi normal indica '
            'calcitriol produzido fora do rim, por granuloma ou linfoma. '
            'Tiazídico e suplemento de vitamina D descompensam essa produção.',
            'Adenopatia mediastinal com suspeita de linfoma pede tecido antes do '
            'corticoide; a ecobroncoscopia colhe histologia, citometria e '
            'culturas de uma vez.',
            'Granuloma não necrosante é padrão, não diagnóstico: a sarcoidose '
            'exige quadro compatível, tecido e exclusão de micobactéria, fungo '
            'e linfoma.',
            'Ao diagnóstico, todos fazem ECG, exame oftalmológico, cálcio, '
            'creatinina e fosfatase alcalina. A uveíte pode estar lá sem queixa, '
            'ou escondida num colírio lubrificante.'),
        so_kicker=True),

    pg('referencias', 'Fontes e limites',
       'Paciente, valores e percursos são ficcionais. A cena de abertura é uma '
       'ilustração autoral gerada por inteligência artificial para este caso; '
       'não é fotografia nem documentação clínica.',
       'Crouser e cols. Diagnosis and detection of sarcoidosis, official ATS '
       'clinical practice guideline, 2020. Baughman e cols. ERS clinical practice '
       'guidelines on treatment of sarcoidosis, 2021. Mochizuki e cols. Revised '
       'criteria of the International Workshop on Ocular Sarcoidosis, 2019. '
       'Walker e Shane. Hypercalcemia: a review, JAMA, 2022. Tebben e cols. '
       'Vitamin D-mediated hypercalcemia, Endocrine Reviews, 2016.',
       'Imagens de outros pacientes, todas do Wikimedia Commons e com setas '
       'adicionadas: radiografia dos hilos e radiografia com TC coronal, '
       'Hellerhoff, CC BY-SA 4.0 ('
       + _fonte(IMG / 'rx_hilos.jpg.json', 'hilos') + '; '
       + _fonte(IMG / 'rx_tc.jpg.json', 'radiografia e TC') + '); tomografia '
       'do mediastino e granuloma, Yale Rosen, CC BY-SA 2.0 ('
       + _fonte(IMG / 'tc_mediastino.jpg.json', 'tomografia') + '; '
       + _fonte(IMG / 'granuloma.jpg.json', 'granuloma') + ').'),
]

REVISAO = []

# Revisão das perguntas: fontes consultadas em 22/10/2026.
# https://www.nbme.org/sites/default/files/2021-02/NBME_Item%20Writing%20Guide_R_6.pdf
# https://pmc.ncbi.nlm.nih.gov/articles/PMC7159433/

# Revisão sindrômica de 23/10/2026: a imagem torácica estreita o diferencial
# depois do primeiro eixo bioquímico, sem mudar o layout ou os arquivos de imagem.
_rx = next(e for e in ETAPAS if e['k'] == 'rx_hilos')
ETAPAS.remove(_rx)
_idx = next(i for i,e in enumerate(ETAPAS) if e['k'] == 'p4')
ETAPAS.insert(_idx, _rx)

_idx = next(i for i,e in enumerate(ETAPAS) if e['k'] == 'p3')
ETAPAS.insert(_idx, Q('hipoteses_calcio', 2,
    'Cálcio ionizado alto e PTH suprimido: quais três mecanismos permanecem prioritários?', [
      ('Produção tumoral de mediadores que elevam o cálcio', True),
      ('Aumento da ação da vitamina D, por excesso de oferta ou produção de calcitriol', True),
      ('Contribuição dos medicamentos à retenção de cálcio', True),
      ('Secreção autônoma de PTH por uma paratireoide', False),
      ('Hipercalcemia familiar hipocalciúrica como explicação principal', False),
      ('Aumento apenas do cálcio ligado à albumina', False),
    ], [
      ('Prioridades', 'PTH suprimido desloca a investigação para mecanismos independentes dele. Perda de peso e tosse sustentam procurar doença sistêmica; o suplemento e o tiazídico precisam ser revistos, sem presumir que expliquem todo o quadro.'),
      ('Por que as outras perdem força', 'Secreção autônoma de PTH e hipercalcemia familiar hipocalciúrica costumam manter PTH não suprimido. A instalação sintomática e a falta de história pessoal ou familiar também desfavorecem esta última. Cálcio ionizado elevado com albumina normal afasta uma elevação apenas da fração ligada à proteína.'),
    ]))

_idx = next(i for i,e in enumerate(ETAPAS) if e['k'] == 'tecido')
ETAPAS[_idx:_idx] = [
    pg('amostra_limitada', 'Resultado da amostragem',
       'Neste percurso alternativo, a punção produz pouco material. Há linfócitos e histiócitos, sem arquitetura suficiente para uma conclusão. A citometria é limitada pela baixa celularidade; as pesquisas iniciais de microrganismos são negativas e as culturas seguem em incubação.',
       'O laudo é inconclusivo. Isso pode decorrer da amostragem e do tratamento recebido, sem que se possa atribuir o resultado apenas ao corticoide.', segue='b_nova_amostra'),
    bifurcacao('b_nova_amostra', 'Decisão', 'Após a amostra inconclusiva',
       'O cálcio e a tosse melhoraram. Como prosseguir?', [
        caminho('Organizar nova amostra representativa, discutindo a técnica com a equipe', 'nova_amostra',
                'A melhora sob corticoide é compartilhada por doenças diferentes. O primeiro material não respondeu à suspeita de doença sistêmica; é preciso ponderar nova amostragem e risco de cada técnica.'),
        caminho('Adotar a resposta ao corticoide como base do diagnóstico e manter seguimento', 'f_incerteza',
                'A observação pode ser apropriada em apresentações selecionadas, mas aqui há hipercalcemia com repercussão renal, perda de peso e amostra inconclusiva. A resposta isolada não resolve as alternativas infecciosas e neoplásicas.'),
       ]),
    pg('nova_amostra', 'Nova coleta',
       'Pneumologia e patologia revisam o alvo e o material necessário. É feita nova ecobroncoscopia, com amostragem ampliada para bloco celular, histologia e microbiologia. Desta vez o material permite interpretação; se permanecesse inconclusivo, seria discutida outra técnica. A equipe registra o atraso e revê a exposição ao corticoide.', segue='tecido'),
    fim('f_incerteza', 'Diagnóstico ainda indefinido',
        'Neste encerramento alternativo, Rafael mantém melhora sintomática sob tratamento, mas a causa não foi confirmada. As alternativas infecciosas e neoplásicas permanecem em avaliação; a investigação do quadro sistêmico está incompleta e precisa ser retomada.',
        'Melhora terapêutica não equivale a confirmação da causa. O custo desta decisão é manter incerteza durante uma exposição a tratamento com riscos, não uma complicação obrigatória.', 'medio'),
]
for _n, _e in enumerate((e for e in ETAPAS if e['t'] in ('pergunta','pareamento')), 1):
    _e['kicker'] = f'Pergunta {_n}'

_idx = next(i for i,e in enumerate(ETAPAS) if e['k'] == 'reducao')
ETAPAS.insert(_idx, pg('inicio_tratamento', 'Tratamento sistêmico',
    'Após obtenção de tecido adequado e revisão das hipóteses infecciosas, a equipe inicia prednisona 40 mg/dia pela hipercalcemia sintomática com lesão renal. Se já havia corticoide no percurso, a dose é revista neste momento. Mantêm-se a suspensão do suplemento e do tiazídico e a hidratação orientada clinicamente.',
    'Cálcio, creatinina, eletrólitos, sintomas e efeitos adversos são reavaliados em uma a duas semanas para ajustar a dose. A decisão de tratar antes das culturas finais considera a ameaça aos órgãos e a probabilidade residual de infecção, que não foi zerada pelos testes iniciais. Os resultados pendentes serão conferidos.',
    'O tratamento ocular tópico e o acompanhamento oftalmológico continuam. A redução sistêmica será guiada pela resposta clínica e laboratorial, em vez de um prazo fixo independente da evolução.'))

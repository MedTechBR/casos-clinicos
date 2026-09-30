"""Febre ictérica grave com lesão renal e hemorragia pulmonar.

PILOTO do molde do //New England// lido em 26/09/2026 (ver
Artifacts/nejm-casos-classicos/GRAMATICA_LIDA_2026-09-26.md), no desenho de
"An Unusual Case of Abdominal Pain": apresentação curta, ficha do paciente,
exame por sistema e primeiros exames entregues prontos; as primeiras
leituras classificam os dados sem nomear doença; a exposição chega
depois, com o irmão; o nome do diagnóstico aparece pela primeira vez na
pergunta do exame confirmatório, perto de 60% do caso. Cada pergunta tem uma
explicação só, em seções com subtítulo. As decisões de conduta continuam
mudando o desfecho, a pedido do Matheus.

Revisão de 30/09: seis perguntas no caminho padrão, nunca duas telas
interativas seguidas; o padrão hepático e os critérios de gravidade viraram
páginas de discussão, e a primeira pergunta só classifica a lesão renal.

Paciente ficcional; doses e critérios segundo o Guia de Vigilância em Saúde
do Ministério da Saúde, 6.ª edição revisada, 2024.
"""
from pathlib import Path

from motor.estudo_imagem import estudo
from motor.etapas import (alt, bifurcacao, caminho, capa, desfecho, op, p,
                          pagina, painel, par, pareamento, pergunta, pontos,
                          topicos, vitais, lamina)

TITULO = 'O sexto dia'
RODAPE = 'Paciente ficcional · evoluções simuladas para ensino'
COR = '#0891b2'
IMG = Path(__file__).parent / 'img'
BANCO = []
MOLDE = 'nejm'
CREDITO_RX = 'Samir · Wikimedia Commons · CC BY-SA 3.0'
CREDITO_RX_ADM = 'Mikael Häggström · Wikimedia Commons · CC0'


def credito_meta(meta):
    import json
    m = json.loads(Path(meta).read_text())
    return m['autor'] + ' · Wikimedia Commons · ' + m['licenca'] + ' · setas adicionadas'


def pg(k, titulo, *textos, segue='', conforme=None):
    return pagina(k, titulo, '', *(p(t) for t in textos), so_kicker=True,
                  segue=segue, conforme=conforme)


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
    capa(TITULO, fundo='cena.png', kicker='Caso interativo',
         selo='Paciente ficcional · procedência e créditos na última tela'),

    pg('historia', 'Apresentação',
       'Um homem de 38 anos, morador de Fortaleza, chega à emergência trazido '
       'pelo irmão no sexto dia de febre, com calafrios, dor de cabeça e dor no '
       'corpo. Há dois dias a tosse, até então seca, passou a ter raias de '
       'sangue, e desde ontem ele fica sem ar para ir ao banheiro.',
       'No segundo dia foi a uma unidade de pronto atendimento, onde '
       'disseram que era virose: soro oral, paracetamol e repouso. A febre '
       'cedeu no quarto dia e voltou. O irmão acha que ele está com os olhos '
       'amarelados desde ontem e que urinou pouco hoje.',
       'Nega dor torácica, dor abdominal forte, diarreia, manchas na pele, '
       'viagem, transfusão e uso de remédios além do paracetamol.'),

    pagina('ficha', 'Ficha do paciente', '',
           topicos(('Antecedentes', 'Nenhuma doença conhecida. Nunca internou.'),
                   ('Medicações', 'Paracetamol 750 mg até quatro vezes ao dia '
                    'desde o segundo dia. Nenhuma outra, nem chás.'),
                   ('Vacinas', 'Febre amarela há seis anos. Não sabe informar '
                    'as outras.'),
                   ('Hábitos', 'Três a quatro latas de cerveja nos fins de '
                    'semana. Não fuma. Nega drogas injetáveis.'),
                   ('Vida social', 'Mora sozinho. Servidor da prefeitura, em '
                    'trabalho de rua. O irmão mora em outro bairro e não sabe '
                    'detalhar a rotina dele.'),
                   ('Família', 'Pais vivos, hipertensos. Sem doença hepática ou '
                    'renal na família.')),
           so_kicker=True),

    pagina('exame', 'Exame físico', '',
           vitais(('Temperatura', '38,4 °C', True),
                  ('Pressão arterial', '94/56', True),
                  ('Frequência cardíaca', '116', True),
                  ('Frequência respiratória', '30', True),
                  ('SpO₂ em ar ambiente', '90%', True)),
           topicos(('Estado geral', 'Prostrado, sonolento, orientado no tempo e no '
                    'espaço. Escleras ictéricas.'),
                   ('Respiratório', 'Crepitações nas bases dos dois pulmões.'),
                   ('Coração', 'Rítmico, taquicárdico, sem sopros.'),
                   ('Abdome', 'Fígado a 2 cm do rebordo, doloroso. Baço não palpável. '
                    'Sem sinal de Murphy.'),
                   ('Pele e membros', 'Algumas petéquias nas pernas. Sem edema.'),
                   ('Neurológico', 'Sem rigidez de nuca, sem déficit focal.')),
           so_kicker=True),

    painel('res1', 'Primeiros exames', 'Sangue', [
        ex('Hemoglobina / hematócrito', '12,8 g/dL / 38%', 'Hb 13,5–17,5 g/dL', True),
        ex('Leucócitos', '15.600/mm³ · neutrófilos 90%', '4.000–11.000/mm³', True),
        ex('Plaquetas', '88.000/mm³ {{(145.000 na UPA)}}', '150.000–450.000/mm³', True),
        ex('Ureia / creatinina', '148 / 2,6 mg/dL {{(creatinina 1,0 na UPA)}}', 'até 42 / 1,3 mg/dL', True),
        ex('Sódio / potássio / cloro', '133 / 3,1 / 100 mmol/L', 'Na 135–145 · K 3,5–5,0 · Cl 98–107', True),
        ex('Bilirrubina total / direta', '6,4 / 5,3 mg/dL', 'até 1,2 / 0,3 mg/dL', True),
        ex('AST / ALT', '96 / 70 U/L', 'até 40 / 41 U/L', True),
        ex('Fosfatase alcalina / GGT', '190 / 160 U/L', 'até 129 / 60 U/L', True),
        ex('Creatinoquinase', '2.380 U/L', 'até 190 U/L', True),
    ], introducao='Duas hemoculturas foram colhidas antes de qualquer antibiótico, e '
                  'uma alíquota de sangue da admissão ficou guardada no laboratório.'),

    painel('res1b', 'Primeiros exames', 'Gasometria e urina', [
        ex('Gasometria arterial em ar ambiente', 'pH 7,33 · pCO₂ 31 · HCO₃ 16 · pO₂ 58 mmHg · lactato 3,1 mmol/L', '—', True),
        ex('Urina', 'Densidade 1.012 · sangue ++ · proteína + · 3 a 5 hemácias e cilindros granulosos por campo · sem cilindros hemáticos', '—', True),
        ex('Sódio / creatinina / potássio urinários', '64 mmol/L / 50 mg/dL / 38 mmol/L · FENa 2,5%', '—', True),
    ]),

    estudo('rx_adm', 'Radiografia de tórax na admissão',
           'Radiografia feita na chegada. Descreva a localização e o tipo da '
           'opacidade antes de ler os achados.',
           IMG / 'rx_consolidacao.jpg',
           'Radiografia de outro paciente · comparação didática.',
           CREDITO_RX_ADM,
        [
         ((190, 478), (70, 330), '**Consolidação alveolar** no terço inferior do pulmão direito.', 12),
         ((68, 622), (175, 745), '**Seio costofrênico** direito livre: sem derrame.', -12),
         ((690, 290), (900, 200), '**Pulmão esquerdo** sem opacidades.', 12),
        ],
        ['Consolidação alveolar em base direita, sem derrame pleural e sem '
         'aumento da área cardíaca.',
         'Com febre, tosse, leucocitose e neutrofilia, é o quadro de uma '
         'pneumonia comunitária, e é essa a hipótese que a equipe registra.']),

    estudo('us_adm', 'Ultrassonografia de abdome',
           'Ultrassonografia feita na chegada, pela icterícia e pela dor no '
           'hipocôndrio direito.',
           IMG / 'us_vias_biliares.jpg',
           'Ultrassonografia de outro paciente · comparação didática.',
           credito_meta(IMG / 'us_vias_biliares.jpg.json'),
        [
         ((447, 150), (330, 60), '**Parênquima hepático** de ecotextura homogênea.', 12),
         ((600, 215), (790, 110), '**Vesícula** de parede fina, sem cálculos nem lama.', -12),
        ],
        ['Fígado discretamente aumentado e homogêneo. Vesícula normal, vias '
         'biliares intra e extra-hepáticas sem dilatação. Rins de tamanho '
         'normal, sem hidronefrose.',
         'Sem obstrução biliar nem urinária: a icterícia e a lesão renal são '
         'de dentro do fígado e do rim.']),

    pagina('figado', 'Discussão', 'O padrão hepático',
        p('A bilirrubina total é de 6,4 mg/dL, 5,3 dela direta, com fosfatase '
          'alcalina de 190 e GGT de 160 U/L. As transaminases, 96 e 70 U/L, '
          'ficam abaixo de três vezes o limite. A icterícia é desproporcional à '
          'lesão do hepatócito, e esse é o padrão colestático.'),
        p('O ultrassom sem dilatação das vias biliares põe a colestase dentro do '
          'fígado. Uma obstrução extra-hepática dilataria as vias, e a hemólise '
          'elevaria a fração indireta. Uma hepatite viral, isquêmica ou tóxica '
          'com essa icterícia teria transaminases nas centenas altas ou nos '
          'milhares, e a infiltração do fígado sobe a fosfatase alcalina muito '
          'mais que a bilirrubina.'),
        p('Colestase intra-hepática aparece na sepse de qualquer foco, inclusive '
          'o pulmonar, em infecções sistêmicas e na lesão por fármacos. Sozinha, '
          'ainda cabe na hipótese de pneumonia com sepse.')),

    Q('p3', 1,
      'Creatinina de 2,6 mg/dL, que era 1,0 há quatro dias. Qual a '
      'interpretação mais adequada da lesão renal?', [
      ('Pré-renal por hipovolemia', False),
      ('Lesão tubular aguda', True),
      ('Glomerulonefrite aguda', False),
      ('Obstrução urinária', False),
      ('Doença renal crônica agudizada', False),
     ], [
      ('A classificação', 'Com densidade urinária de 1.012, sódio urinário de '
       '64 mmol/L, fração de excreção de sódio de 2,5% e cilindros granulosos, '
       'o túbulo já não reabsorve sódio: é lesão intrínseca tubular. Na '
       'pré-renal, a FENa fica abaixo de 1% e a urina vem concentrada.'),
      ('Por que não as outras', 'Sem cilindros hemáticos nem proteinúria '
       'importante, glomerulonefrite é pouco provável. O ultrassom sem '
       'hidronefrose afasta obstrução, e a creatinina normal quatro dias antes '
       'afasta doença crônica.'),
      ('Dois achados que não combinam com a sepse comum', 'O potássio está '
       'baixo, 3,1, com potássio urinário de 38 mmol/L: o rim está perdendo '
       'potássio, quando na lesão renal habitual ele o retém. E a fita mostra '
       'sangue ++ com poucas hemácias, o que, com CK de 2.380, indica pigmento '
       'muscular na urina.'),
     ]),

    pagina('gravidade', 'Discussão', 'A gravidade antes da causa',
        p('Com a hipótese de pneumonia comunitária, a equipe aplica os critérios '
          'menores de gravidade da IDSA/ATS: frequência respiratória de 30 ou '
          'mais, PaO₂/FiO₂ de 250 ou menos, infiltrados multilobares, confusão, '
          'ureia acima de cerca de 42 mg/dL, leucócitos abaixo de 4.000/mm³, '
          'plaquetas abaixo de 100.000/mm³, temperatura abaixo de 36 °C e '
          'hipotensão que exige volume agressivo.'),
        p('Ele preenche três: ureia de 148, plaquetas de 88.000 e frequência '
          'respiratória de 30. A PaO₂/FiO₂ é 58 dividido por 0,21, igual a 276, '
          'a consolidação ocupa um lobo só e ele está sonolento, mas orientado. '
          'A leucocitose de 15.600 não conta, porque o critério é a leucopenia.'),
        p('Três ou mais critérios menores indicam terapia intensiva. A regra '
          'orienta o local de tratamento e nada diz sobre a causa. Ureia alta, '
          'plaquetas baixas e icterícia num quadro pulmonar pedem que se '
          'pergunte se a pneumonia explica tudo.')),

    bifurcacao('b1', 'Decisão', 'As primeiras horas',
      'Hipotenso, hipoxêmico, com lesão tubular e colestase, três critérios '
      'menores de gravidade. As hemoculturas já foram colhidas. Como você '
      'conduz?', [
      caminho('Ceftriaxona 2 g e azitromicina agora, oxigênio e vaga de UTI',
              'tratado',
              'Pneumonia grave com sepse pede betalactâmico com macrolídeo no '
              'primeiro atendimento, e três critérios menores indicam UTI.'),
      caminho('Oxigênio e hidratação; escolher o antibiótico quando saírem as '
              'hemoculturas', 'espera',
              'Culturas levam dias, e a mortalidade da sepse sobe a cada hora '
              'sem antibiótico.'),
      caminho('Conduzir como dengue grave: cristaloide 20 mL/kg em bolus '
              'repetidos, sem antibiótico', 'volume',
              'Crepitações e hipoxemia pedem cautela com volume, e a colestase '
              'com lesão tubular não é o padrão da dengue.'),
    ]),

    pg('volume', 'Quatro horas depois',
       'Depois de três litros de cristaloide, a pressão sobe para 102/60, mas '
       'a saturação cai para 84% com cateter nasal e as crepitações chegam '
       'aos terços médios. A plantonista suspende o volume e inicia '
       'ceftriaxona e azitromicina com quatro horas de atraso.',
       segue='tratado'),

    pg('espera', 'Dezoito horas depois',
       'Sob soro e oxigênio, a saturação cai para 85% e a urina para 20 mL '
       'por hora. As hemoculturas ainda não cresceram. A plantonista inicia '
       'ceftriaxona e azitromicina com dezoito horas de atraso.',
       segue='tratado'),

    pg('tratado', 'Primeiras horas de antibiótico',
       'Duas horas depois da primeira dose, ele tem calafrios, febre de 40 °C '
       'e queda da pressão para 84/50. Com 500 mL de cristaloide e '
       'antitérmico, melhora em quatro horas. A equipe mantém os antibióticos.',
       'Na madrugada, a tosse fica úmida e ele expectora sangue vivo.'),

    pg('hemorragia', 'Segundo dia de internação',
       'Saturação de 83% com máscara com reservatório, frequência '
       'respiratória de 36, hemoptise de 150 mL em seis horas. Diurese de 280 '
       'mL em 24 horas.',
       'Hemoglobina 9,6 g/dL (12,8 na admissão), plaquetas 38.000/mm³, INR '
       '1,4, fibrinogênio 390 mg/dL, esfregaço sem esquizócitos. Bilirrubina '
       'total 17,8 mg/dL, creatinina 4,6 mg/dL, potássio 3,0 mmol/L. A '
       'radiografia é repetida.'),

    estudo('rx_hemorragia', 'Radiografia de tórax',
           'Radiografia ilustrativa de outro paciente, com o padrão descrito '
           'no laudo dele no segundo dia. Compare com a da admissão, que '
           'mostrava consolidação só na base direita.',
           IMG / 'rx_torax_alveolar.jpg',
           'Radiografia de outro paciente · comparação didática.',
           CREDITO_RX,
        [
         ((308, 427), (110, 345), '**Opacidades alveolares** no pulmão direito, em mancha e confluentes.', 12),
         ((704, 430), (912, 320), 'O mesmo padrão no **pulmão esquerdo**: a doença é bilateral.', -12),
         ((620, 160), (760, 60), '**Ápices relativamente poupados**: o predomínio é central e inferior.', 12),
        ],
        ['Opacidades alveolares bilaterais e confluentes, que em 24 horas '
         'passaram da base direita para os dois pulmões.',
         'Com hemoptise e queda de 3,2 g/dL na hemoglobina, o que enche os '
         'alvéolos é sangue: hemorragia alveolar difusa.']),

    Q('p4', 2,
      'Hemorragia alveolar com plaquetas de 38.000, INR de 1,4, fibrinogênio '
      'de 390 e esfregaço sem esquizócitos. **Quais três** afirmações estão '
      'corretas?', [
      ('Não há coagulação intravascular disseminada', True),
      ('O sangramento é sobretudo de lesão capilar', True),
      ('Transfundir plaquetas se abaixo de 50.000', True),
      ('As plaquetas explicam sozinhas a hemorragia', False),
      ('Plasma fresco pelo INR de 1,4', False),
      ('Microangiopatia trombótica provável', False),
     ], [
      ('A coagulação', 'Fibrinogênio normal, INR pouco alterado e esfregaço '
       'sem esquizócitos afastam CIVD descompensada e microangiopatia '
       'trombótica. Esquizócitos seriam o achado da microangiopatia, não a '
       'ausência deles.'),
      ('O mecanismo', 'Plaquetas de 38.000 raramente causam sangramento '
       'espontâneo grave; o risco sobe abaixo de 10 a 20 mil. Um sangramento '
       'alveolar difuso com esses números aponta para lesão do endotélio '
       'capilar, em que a plaquetopenia soma, mas não causa.'),
      ('A transfusão', 'No sangramento ativo, a meta é manter plaquetas acima '
       'de 50.000. Plasma com INR de 1,4 não corrige nada que importe e soma '
       'volume a um pulmão que já está cheio.'),
     ]),

    pg('suporte', 'Uma hora depois',
       'Ele recebe uma dose de plaquetas e um concentrado de hemácias, sem '
       'plasma. As plaquetas sobem para 61.000/mm³ e a hemoglobina para 10,4 '
       'g/dL, mas a hemoptise continua.',
       'A saturação não passa de 83% com a máscara com reservatório. A '
       'frequência respiratória é de 38, com uso da musculatura acessória, e a '
       'sonda vesical drenou 10 mL na última hora.'),

    bifurcacao('b2', 'Decisão', 'O pulmão que sangra',
      'Saturação de 83% com máscara, hemoptise e oligúria. O que você faz?', [
      caminho('UTI: intubação precoce com ventilação protetora e diálise '
              'precoce e diária', 'uti',
              'Proteger o pulmão com volumes baixos e dialisar cedo reduz a '
              'mortalidade.'),
      caminho('Ventilação não invasiva e furosemida em dose alta', 'vni',
              'A máscara não protege uma via aérea que sangra, e o diurético '
              'não muda o curso da lesão renal.'),
      caminho('Pulso de metilprednisolona e observação na enfermaria', 'pulso',
              'O corticoide na hemorragia pulmonar é controverso e não '
              'substitui suporte intensivo.'),
    ]),

    pg('pulso', 'Seis horas depois',
       'Na enfermaria, sob corticoide, a saturação cai para 78%. O time de '
       'resposta rápida é chamado.',
       segue='vni'),

    pg('vni', 'Na sala de emergência',
       'Com ventilação não invasiva, ele enche a máscara de sangue e não '
       'consegue manter a saturação acima de 80%. Está agitado e confuso.',
       segue='b3'),

    bifurcacao('b3', 'Decisão', 'A máscara falhou',
      'Qual a próxima conduta?', [
      caminho('Intubar agora, ventilação protetora e UTI com diálise',
              'uti_tardia', 'A falha da ventilação não invasiva é a indicação.'),
      caminho('Manter a máscara e aumentar a fração inspirada de oxigênio',
              'parada', 'Insistir num suporte que já falhou.'),
    ]),

    pg('parada', 'Vinte minutos depois',
       'Ele para em atividade elétrica sem pulso, hipoxêmico. É intubado '
       'durante a reanimação, com sangue saindo pelo tubo. O retorno da '
       'circulação acontece depois de 18 minutos.',
       segue='f_obito'),

    pg('uti_tardia', 'Na UTI',
       'Intubado em emergência, com ventilação protetora, pressão expiratória '
       'alta e sedação profunda. A hemodiálise começa no mesmo dia. A '
       'hipoxemia grave dura quatro dias.',
       segue='irmao'),

    pg('uti', 'Na UTI',
       'Intubação planejada, ventilação com volume corrente de 6 mL/kg de '
       'peso predito e pressão expiratória elevada. Hemodiálise no mesmo dia, '
       'depois diária, com reposição de potássio.',
       'A hemoptise diminui no terceiro dia.'),

    pg('irmao', 'O irmão volta',
       'O irmão volta com os documentos, depois de conversar com os colegas de '
       'trabalho. Ele é agente de limpeza urbana. Doze dias antes da febre, '
       'depois de três dias de chuva forte, passou um turno dentro de um canal '
       'alagado, desobstruindo a passagem da água, com uma bota furada.',
       'Revisto com calma, o exame mostra conjuntivas hiperemiadas, sem '
       'secreção, dor à compressão muito maior nas panturrilhas e um corte '
       'cicatrizado na planta do pé direito. Os colegas dizem que o depósito '
       'da equipe tem ratos.',
       'As hemoculturas seguem sem crescimento em 48 horas.'),

    Q('p5', 3,
      'Com essa exposição, a equipe quer confirmar a hipótese a partir da '
      'alíquota guardada da admissão, colhida no sexto dia e antes do '
      'antibiótico. Qual exame confirma o diagnóstico nessa amostra?', [
      ('PCR para Leptospira no sangue', True),
      ('ELISA IgM para leptospira', False),
      ('Microaglutinação em amostra única', False),
      ('Cultura de urina para leptospira', False),
      ('Hemocultura em meio convencional', False),
     ], [
      ('O tempo da doença', 'Na primeira semana a leptospira circula no '
       'sangue, e o anticorpo ainda pode não ter aparecido. Pelo Guia de '
       'Vigilância em Saúde, PCR detectável em sangue colhido até o sétimo '
       'dia confirma o caso.'),
      ('Por que não as outras', 'ELISA IgM antes do sétimo dia pode vir '
       'negativo e não descarta; só a partir do sétimo dia um resultado '
       'negativo pesa contra. A microaglutinação precisa de amostras pareadas, '
       'a segunda entre 14 e 60 dias. A leptospira aparece na urina mais '
       'tarde e cresce devagar, em semanas. Hemocultura convencional não '
       'isola o agente.'),
     ]),

    pg('virada', 'O diagnóstico',
       'Laboratório de referência: **PCR para Leptospira no sangue, DNA '
       'detectado.** ELISA IgM na mesma amostra: não reagente.',
       'É leptospirose na forma grave, a síndrome de Weil: icterícia, lesão '
       'renal e hemorragia pulmonar. A leptospira entra por pele lesada ou '
       'mucosa em contato com água ou lama contaminada pela urina de roedores. '
       'A vasculite capilar difusa explica o que se viu: colestase sem '
       'necrose, lesão tubular com perda de potássio, miosite e sangramento '
       'alveolar. A hemorragia pulmonar é a complicação que mais mata, com '
       'letalidade acima de 50% em várias séries.',
       'A ceftriaxona dada para a pneumonia já tratava a doença, e a febre '
       'com hipotensão duas horas depois da primeira dose ganha agora outro '
       'sentido.'),

    pareamento('p6', 'Pergunta 4',
      'As febres ictéricas e hemorrágicas do Brasil se sobrepõem. Associe '
      'cada quadro à doença que ele sugere.', [
      par('Sufusão conjuntival, dor na panturrilha e contato com enchente',
          'Leptospirose',
          'A combinação dele. A sufusão é congestão sem secreção.'),
      par('Dor abdominal, vômitos e hematócrito subindo na defervescência',
          'Dengue grave',
          'O extravasamento plasmático começa quando a febre cai.'),
      par('Febre, icterícia e pulso lento para a febre, sem vacina, após mata',
          'Febre amarela',
          'Sinal de Faget e transaminases na casa dos milhares.'),
      par('Febre em picos, anemia e esplenomegalia depois de viagem ao Pará',
          'Malária por Plasmodium vivax',
          'A gota espessa decide. No Ceará, quase sempre importada.'),
      par('Icterícia com transaminases acima de 1.000 e pouca febre',
          'Hepatite A aguda',
          'Hepatite hepatocelular pura, sem rim nem pulmão.'),
    ], opcoes=['Leptospirose', 'Dengue grave', 'Febre amarela',
               'Malária por Plasmodium vivax', 'Hepatite A aguda', 'Hantavirose'],
    titulo_resposta='O detalhe da história decide mais que o laboratório',
    nota='A opção que sobrou, hantavirose, é cardiopulmonar, de exposição '
         'rural, com hemoconcentração e sem icterícia importante.'),

    pg('recuperacao', 'Segunda semana',
       'A diurese volta com poliúria de 4 litros por dia. O potássio cai para '
       '2,9 mmol/L apesar de 80 mEq por dia de reposição, e o magnésio para '
       '1,4 mg/dL. A icterícia regride devagar. A segunda amostra, no 14.º '
       'dia, tem ELISA IgM reagente e microaglutinação com título de 1:1.600 '
       'para o sorogrupo Icterohaemorrhagiae.'),

    Q('p7', 5,
      'Sobre o tratamento, **quais três** afirmações estão corretas?', [
      ('Antibiótico endovenoso por pelo menos 7 dias', True),
      ('Diálise precoce e diária', True),
      ('Reposição de potássio pelos controles', True),
      ('Suspender a ceftriaxona pela reação febril', False),
      ('Furosemida para evitar a diálise', False),
      ('Antibiótico só na primeira semana', False),
      ('Corticoide de rotina na forma grave', False),
     ], [
      ('O antibiótico', 'Na forma grave, ceftriaxona ou penicilina cristalina '
       'endovenosa, por pelo menos sete dias; doxiciclina oral fica para a '
       'forma leve. O benefício é maior na primeira semana, mas o antibiótico '
       'está indicado em qualquer fase.'),
      ('A reação da primeira dose', 'Calafrios, febre alta e hipotensão '
       'poucas horas após a primeira dose são a reação de Jarisch-Herxheimer, '
       'descrita nas infecções por espiroquetas. Trata-se o sintoma e o '
       'antibiótico continua.'),
      ('O rim', 'Diálise precoce e diária reduziu a mortalidade frente à '
       'diálise em dias alternados num ensaio brasileiro. Furosemida não muda '
       'a necessidade de diálise.'),
      ('O potássio', 'A perda tubular de potássio continua na fase poliúrica, '
       'como o potássio de 2,9 com 80 mEq por dia mostrou. A reposição segue '
       'os controles, e o magnésio baixo precisa ser corrigido junto, ou o '
       'potássio não se sustenta.'),
      ('O que não entra', 'Não há evidência que sustente corticoide de rotina '
       'na forma grave.'),
     ]),

    pg('terceira', 'Terceira semana',
       'Com o magnésio corrigido, o potássio se sustenta acima de 3,5 mmol/L '
       'com reposição oral. A bilirrubina e a creatinina caem a cada dia, e ele '
       'volta a comer.',
       'Na visita, ele pergunta quando pode voltar ao trabalho e se os colegas '
       'da equipe correm o mesmo risco. O irmão quer saber se pode ter se '
       'contaminado cuidando dele.'),

    Q('p8', 6,
      'Na alta, **quais três** medidas estão corretas?', [
      ('Notificar à vigilância epidemiológica', True),
      ('Investigar o local de trabalho', True),
      ('Acompanhar creatinina e potássio', True),
      ('Isolamento de contato em casa', False),
      ('Antibiótico profilático por três meses', False),
      ('Vacinar os colegas de trabalho', False),
      ('Repetir a microaglutinação todo mês', False),
     ], [
      ('Vigilância e trabalho', 'Leptospirose é de notificação compulsória. '
       'A vigilância investiga os colegas expostos e o depósito, e a '
       'prevenção está em botas íntegras, luvas e controle de roedores.'),
      ('O seguimento', 'A função renal costuma se recuperar em semanas, e a '
       'fase poliúrica perde potássio; creatinina e potássio guiam as '
       'consultas seguintes.'),
      ('O que não entra', 'Não há transmissão entre pessoas, nem vacina humana '
       'disponível no Brasil. Antibiótico profilático depois da infecção '
       'tratada não tem indicação, e repetir a microaglutinação não muda a '
       'conduta num caso confirmado.'),
     ]),

    pg('alta', 'Preparando a alta',
       'A equipe revê com ele e o irmão o que aconteceu: a exposição, a '
       'doença, as sessões de diálise e o que esperar do rim e dos músculos '
       'nas próximas semanas.',
       conforme=('b2', ['alta_cedo', 'f2', 'f2'])),

    pg('alta_cedo', 'Última visita',
       'A diálise foi suspensa no nono dia e a creatinina cai todos os dias. '
       'Ele já caminha pelo corredor sem oxigênio.',
       conforme=('b1', ['f1', 'f2', 'f2'])),

    fim('f1', 'Alta sem diálise',
        'Ele sai no 16.º dia, sem diálise desde o 9.º, com creatinina de 1,6 '
        'mg/dL e bilirrubina em queda. Retoma o trabalho em seis semanas.',
        'Antibiótico no primeiro contato, UTI antes da falência e diálise '
        'precoce foram as três decisões que mudam a mortalidade da síndrome '
        'de Weil.', 'melhor'),

    fim('f2', 'Alta depois de internação prolongada',
        'Ele sai no 27.º dia, com creatinina de 2,1 mg/dL e fraqueza muscular '
        'que leva dois meses para passar.',
        'O atraso do antibiótico ou do suporte intensivo acrescentou dias de '
        'hipoxemia e de diálise, numa forma de letalidade alta.',
        'medio'),

    fim('f_obito', 'Óbito no terceiro dia',
        'Depois da parada, ele evolui com choque refratário e hemorragia '
        'pulmonar maciça, e morre no terceiro dia de internação.',
        'A ventilação não invasiva numa via aérea que sangra, mantida depois '
        'de falhar, levou à parada hipóxica. A hemorragia pulmonar pede '
        'intubação precoce.', 'pior'),

    pagina('retrospectiva', 'Pontos de ensino', '',
        pontos(
            'Na icterícia febril, a primeira leitura é o padrão: bilirrubina '
            'direta muito alta com transaminases abaixo de três vezes o limite '
            'é colestase, e afasta as hepatites virais agudas.',
            'Na lesão renal aguda, FENa acima de 2% com cilindros granulosos '
            'indica lesão tubular. Potássio baixo com potássio urinário alto '
            'é perda tubular, incomum e útil para o diagnóstico.',
            'Hemoptise, queda de hemoglobina e infiltrado alveolar difuso são '
            'hemorragia alveolar até prova em contrário, e pedem suporte '
            'intensivo antes do nome da causa.',
            'A exposição à água e à lama muda a hipótese; ela precisa ser '
            'perguntada, porque o paciente grave raramente a conta.',
            'Na primeira semana, PCR no sangue confirma a leptospirose; o '
            'ELISA IgM negativo antes do sétimo dia não descarta.',
            'Na forma grave: antibiótico endovenoso sem esperar a '
            'confirmação, intubação precoce com ventilação protetora na '
            'hemorragia pulmonar e diálise precoce e diária.'),
        so_kicker=True),

    pg('referencias', 'Fontes e limites',
       'Paciente, valores e percursos são ficcionais. A cena de abertura é uma ilustração autoral gerada por inteligência artificial para este caso; não é fotografia nem documentação clínica.',
       'Ministério da Saúde. Guia de Vigilância em Saúde, 6.ª edição '
       'revisada, 2024, volume 3, capítulo de leptospirose (critérios de '
       'confirmação e antibioticoterapia), e Leptospirose: diagnóstico e '
       'manejo clínico, 2014. Andrade e cols., Clin J Am Soc Nephrol 2007 '
       '(diálise diária). Spichler e cols., Am J Trop Med Hyg 2008 '
       '(preditores de mortalidade). Radiografias: Mikael Häggström, '
       'Wikimedia Commons, CC0 (admissão), e Samir, Wikimedia Commons, CC '
       'BY-SA 3.0 (segundo dia). Ultrassonografia: Ptrump16, Wikimedia '
       'Commons, CC BY-SA 4.0. Todas de outros pacientes, com setas '
       'adicionadas.'),
]

REVISAO = []

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
         ((47, 700), (175, 745), '**Seio costofrênico** direito livre: sem derrame.', -12),
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
      'Qual interpretação integra creatinina 2,6, cilindros granulosos e hipocalemia com K urinário 38?', [
      ('Lesão tubular com perda de eletrólitos, possivelmente somada à hipoperfusão', True),
      ('Hipoperfusão isolada com túbulos preservados', False),
      ('Nefropatia por pigmentos como explicação suficiente de todos os achados', False),
      ('Glomerulonefrite como mecanismo predominante', False),
      ('Obstrução urinária com diurese paradoxal', False),
    ], [('Integração', 'Cilindros granulosos, FENa 2,5% e urina pouco concentrada favorecem lesão tubular. A hipotensão pode contribuir, mas não explica sozinha o padrão urinário. K urinário 38 durante hipocalemia sugere perda renal inadequada, interpretada com diurese e reposição.'), ('Concorrentes', 'CK 2.380 e sangue na fita com poucas hemácias sustentam contribuição de pigmento muscular, sem provar que seja o mecanismo dominante. Pouca proteína e ausência de cilindros hemáticos enfraquecem glomerulonefrite; ultrassom sem dilatação reduz obstrução. FENa não é um divisor infalível na sepse.')]),

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
      'Hemoptise, Hb em queda e plaquetas 38.000, com INR 1,4 e fibrinogênio 390. Quais duas interpretações se sustentam?', [
      ('Lesão da barreira alveolocapilar pode somar-se à trombocitopenia', True),
      ('CIVD permanece possível, mas não demonstrada por estes dados', True),
      ('Consumo sistêmico de fatores é o mecanismo comprovado do sangramento', False),
      ('Microangiopatia trombótica é a explicação mais forte para rim e pulmão', False),
      ('A contagem plaquetária permite atribuir a hemorragia apenas à hemostasia primária', False),
    ], [('Limite da inferência', 'A gravidade pulmonar não deve ser atribuída apenas às plaquetas: lesão capilar pode coexistir. Fibrinogênio preservado, reagente de fase aguda, não exclui CIVD; faltam tendência do coagulograma e marcadores de fibrina para caracterizar consumo.'), ('Comparação', 'Sem esquizócitos nem demonstração de hemólise microangiopática, a microangiopatia perde força, sem ser impossibilidade. A hemorragia exige suporte e pode justificar plaquetas; INR 1,4 isolado não fundamenta plasma.')]),

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
      'Há sangue do sexto dia, pré-antibiótico. Quais duas estratégias laboratoriais priorizar para a hipótese ligada à enchente?', [
      ('PCR para Leptospira na amostra guardada', True),
      ('IgM na amostra aguda e repetição na convalescença se negativa', True),
      ('Microaglutinação isolada na amostra aguda como único teste', False),
      ('Cultura urinária para decisão nas próximas horas', False),
      ('Nova hemocultura convencional para identificar Leptospira', False),
    ], [('Prioridades', 'PCR sanguínea aproveita a primeira semana de leptospiremia e pode confirmar rapidamente. IgM aguda fornece referência; negativa nessa fase não afasta a doença e deve ser repetida. Os resultados agudo e convalescente aparecem na sequência.'), ('Alternativas', 'Microaglutinação isolada tem sensibilidade limitada cedo; amostras pareadas são mais informativas. Cultura urinária é lenta e a eliminação urinária tende a ser posterior. Hemocultura convencional não é o método de isolamento para este agente; as já negativas não o excluem. Nenhum resultado deve atrasar o tratamento.')]),

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

    Q('p6', 4,
      'Antes da diálise, creatinina 4,6 e K 3,0, após K 3,1 com K urinário 38 na admissão. Qual interpretação integra melhor essa evolução?', [
      ('Redução da filtração coexistindo com perda tubular de potássio', True),
      ('Perda digestiva de potássio com conservação renal apropriada', False),
      ('Liberação muscular de potássio como mecanismo predominante', False),
      ('Redistribuição intracelular isolada, sem perda corporal relevante', False),
      ('Recuperação da filtração já estabelecida pela queda do potássio', False),
    ], [('Integração', 'K urinário de 38 durante hipocalemia sugere excreção renal inadequada, embora a concentração isolada dependa do fluxo urinário. Lesão tubular pode produzir perda de K mesmo com filtração muito reduzida; creatinina alta não garante hipercalemia.'), ('Comparação', 'Perda digestiva e redistribuição podem contribuir, mas isoladamente explicam pior a excreção urinária descrita. Miosite com lise celular tende a liberar K, não explica a hipocalemia persistente. Potássio baixo não documenta recuperação da filtração: pode persistir perda tubular durante lesão renal grave.')]),

    pg('recuperacao', 'Segunda semana',
       'A diurese volta com poliúria de 4 litros por dia. O potássio cai para '
       '2,9 mmol/L apesar de 80 mEq por dia de reposição, e o magnésio para '
       '1,4 mg/dL. A icterícia regride devagar. A segunda amostra, no 14.º '
       'dia, tem ELISA IgM reagente e microaglutinação com título de 1:1.600 '
       'para o sorogrupo Icterohaemorrhagiae.'),

    Q('p7', 5,
      'K 2,9 apesar de 80 mEq/dia, Mg 1,4 e diurese de 4 L/dia. Qual ajuste é mais apropriado?', [
      ('Corrigir magnésio e titular potássio com controles frequentes', True),
      ('Aumentar apenas o potássio, mantendo o magnésio para reavaliação após a alta', False),
      ('Reduzir a reposição de potássio por ter necessitado de diálise', False),
      ('Associar furosemida para acelerar a recuperação tubular', False),
      ('Manter diálise diária pela poliúria, independentemente dos demais parâmetros', False),
    ], [('Integração', 'Magnésio baixo favorece perda renal persistente de potássio; corrigir ambos é mais efetivo que aumentar apenas K. O risco muda com a recuperação renal, exigindo controles e ajuste, não dose fixa.'), ('Suporte individualizado', 'Necessidade prévia de diálise não implica retenção atual de K. Furosemida aumenta perdas e não recupera túbulos. Poliúria não determina diálise: decidir por volume, depuração e distúrbios metabólicos. O estudo brasileiro de diálise diária foi pequeno e comparou períodos de tratamento; não sustenta calendário obrigatório para todo caso.')]),

    pg('terceira', 'Terceira semana',
       'Com o magnésio corrigido, o potássio se sustenta acima de 3,5 mmol/L '
       'com reposição oral. A bilirrubina e a creatinina caem a cada dia, e ele '
       'volta a comer.',
       'Na visita, ele pergunta quando pode voltar ao trabalho e se os colegas '
       'da equipe correm o mesmo risco. O irmão quer saber se pode ter se '
       'contaminado cuidando dele.'),

    Q('p8', 6,
      'Qual interpretação deve orientar a investigação dos colegas e a orientação ao irmão?', [
      ('Os colegas podem compartilhar a exposição ambiental; cuidar do paciente raramente transmite a doença', True),
      ('A negatividade das hemoculturas indica baixo risco ocupacional para os colegas', False),
      ('O título de microaglutinação define quais colegas devem receber antibiótico', False),
      ('O contato domiciliar deve ser tratado como exposição equivalente à água do canal', False),
      ('A recuperação clínica dispensa investigação do ambiente de trabalho', False),
    ], [('Exposição', 'Canal alagado, bota furada e roedores sustentam risco compartilhado no trabalho e justificam notificação e investigação ambiental. Hemocultura convencional negativa não mede esse risco.'), ('Contato e seguimento', 'Transmissão entre pessoas é rara; cuidar dele não equivale à exposição ao canal. Título sorológico do paciente não define profilaxia de terceiros. A recuperação não elimina a fonte ambiental, e o paciente ainda precisa acompanhar função renal e eletrólitos.')]),

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

# Revisão das perguntas: fontes consultadas em 22/10/2026.
# https://www.nbme.org/sites/default/files/2021-02/NBME_Item%20Writing%20Guide_R_6.pdf
# https://www.cdc.gov/yellow-book/hcp/travel-associated-infections-diseases/leptospirosis.html
# https://pubmed.ncbi.nlm.nih.gov/17699490/
# https://www.nice.org.uk/guidance/ng148/chapter/Recommendations

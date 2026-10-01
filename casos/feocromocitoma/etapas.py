"""Crises de cefaleia e palpitação tratadas como pânico, até a crise que parou no coração.

Escrito em 01/10/2026 no molde do //New England// (pilotos: leptospirose e
endocardite; gramática em Artifacts/nejm-casos-classicos/GRAMATICA_LIDA_2026-09-26.md).
Contadora de 41 anos, em Fortaleza, com seis meses de crises chamadas de
transtorno de pânico (sertralina) e de enxaqueca (amitriptilina), chega à
emergência depois de uma ampola de metoclopramida com pressão de 228/124,
dor no peito e troponina subindo. As perguntas da primeira metade só
classificam e interpretam: a crise (emergência pela lesão aguda), o mecanismo
da lesão miocárdica (atordoamento adrenérgico) e o hematócrito alto (volume
plasmático contraído). As âncoras são da equipe, registradas em texto: pânico
com hipertensão reativa, tireotoxicose (afastada pelo TSH) e síndrome de
takotsubo com gatilho emocional. A virada é a urotomografia pedida pela dor
lombar e pela hematúria de um cálculo, que mostra a massa adrenal, logo
depois da metade; o nome aparece na pergunta dos exames da massa (54%). Depois
vêm o preparo com alfabloqueio, a adrenalectomia, o teste genético (RET C634R,
NEM2A, com o "bócio operado" da mãe) e o rastreio da família. As decisões de
conduta mudam o desfecho: betabloqueio antes do alfa, operar sem preparo e não
testar a genética.

Paciente ficcional. Lenders e cols., Endocrine Society, J Clin Endocrinol
Metab 2014; Nölting e cols., Endocr Rev 2022; Fassnacht e cols., ESE/ENSAT,
Eur J Endocrinol 2023 (incidentaloma); Buitenwerf e cols., PRESCRIPT, J Clin
Endocrinol Metab 2020; Wells e cols., ATA, Thyroid 2015; Brandão e cols.,
Diretriz Brasileira de Hipertensão Arterial 2025; van den Born e cols., ESC
2019 (emergências hipertensivas). Filtração pelo CKD-EPI 2021.
"""
import json
from pathlib import Path

from motor.estudo_imagem import estudo
from motor.etapas import (alt, bifurcacao, caminho, capa, desfecho, op, p,
                          pagina, painel, par, pareamento, pergunta, pontos,
                          topicos, vitais)

TITULO = 'Pressão de nervoso'
RODAPE = 'Paciente ficcional · evoluções simuladas para ensino'
COR = '#a16207'
IMG = Path(__file__).parent / 'img'
BANCO = []
MOLDE = 'nejm'


def credito_meta(meta):
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
    capa(TITULO, fundo='cena.jpg', kicker='Caso interativo',
         selo='Paciente ficcional · procedência e créditos na última tela'),

    pg('historia', 'Apresentação',
       'Patrícia, contadora de 41 anos, moradora de Fortaleza, chega à emergência '
       'trazida pelo SAMU com dor de cabeça intensa, palpitação, suor frio e dor no '
       'peito em aperto. A crise começou às 10 horas, no escritório, com vômitos. '
       'Numa unidade de pronto atendimento recebeu metoclopramida endovenosa; '
       'quinze minutos depois a dor de cabeça virou "a pior da vida" e o peito '
       'começou a doer.',
       'Há seis meses tem crises parecidas e mais curtas, de 15 a 40 minutos, duas '
       'ou três vezes por semana: cefaleia em pressão, coração disparado, suor, '
       'tremor nas mãos e a sensação de que vai morrer. A psiquiatria diagnosticou '
       'transtorno de pânico e iniciou sertralina há quatro meses. A neurologia '
       'tratou a cefaleia como enxaqueca e iniciou amitriptilina há três semanas; '
       'desde então as crises ficaram mais frequentes. Perdeu 6 kg no período.',
       'Nega febre, diarreia, alteração menstrual e uso de cocaína, anfetaminas, '
       'descongestionantes ou remédios para emagrecer.'),

    pagina('ficha', 'Ficha do paciente', '',
           topicos(('Antecedentes', 'Duas medidas de 146/92 mmHg na unidade básica no '
                    'último ano, atribuídas ao nervosismo, sem tratamento. Glicemia de '
                    'jejum de 118 mg/dL há dois meses, com orientação de dieta. '
                    'Enxaqueca "desde o ano passado". Uma cesárea.'),
                   ('Medicações', 'Sertralina 50 mg pela manhã. Amitriptilina 25 mg à '
                    'noite, há três semanas. Dipirona nas crises de dor.'),
                   ('Hábitos', 'Não fuma, não bebe. Quatro xícaras de café por dia. '
                    'Caminha na Beira-Mar três vezes por semana.'),
                   ('Trabalho', 'Contadora num escritório do centro. As crises vêm na '
                    'semana de fechamento, mas também em casa, de madrugada e nos fins '
                    'de semana; duas começaram quando se abaixou para pegar caixas de '
                    'arquivo.'),
                   ('Família', 'Mãe de 66 anos, que "operou um bócio" aos 40 e toma '
                    'hormônio da tireoide. Pai diabético. Um tio materno morreu aos 44 '
                    'anos de derrame, "com a pressão nas alturas". Dois filhos, de 13 e '
                    '8 anos, saudáveis.')),
           so_kicker=True),

    pagina('exame', 'Exame físico', '',
           vitais(('Pressão arterial', '228/124', True),
                  ('Frequência cardíaca', '128', True),
                  ('Frequência respiratória', '24', True),
                  ('Temperatura', '37,4 °C', False),
                  ('SpO₂ em ar ambiente', '95%', False),
                  ('Peso · IMC', '54 kg · 20,3', False)),
           topicos(('Estado geral', 'Ansiosa, pálida, com sudorese fria e tremor fino '
                    'das mãos. Pele sem manchas.'),
                   ('Pescoço', 'Nódulo de 1,5 cm no lobo direito da tireoide, firme, '
                    'móvel com a deglutição, indolor. Sem linfonodos palpáveis.'),
                   ('Coração', 'Ritmo regular, taquicárdico, com quarta bulha. Sem '
                    'sopros.'),
                   ('Pulmões', 'Crepitações finas nas duas bases.'),
                   ('Abdome', 'Flácido, indolor, sem massas palpáveis.'),
                   ('Neurológico e fundo de olho', 'Sem déficit focal nem rigidez de '
                    'nuca. Arteríolas estreitadas, sem hemorragias, exsudatos ou '
                    'papiledema.')),
           so_kicker=True),

    painel('res1', 'Primeiros exames', 'Sangue', [
        ex('Hemoglobina / hematócrito', '16,2 g/dL / 49%', 'Hb 12–16 g/dL · Ht 36–46%', True),
        ex('Leucócitos', '14.200/mm³ · neutrófilos 82%', '4.000–11.000/mm³', True),
        ex('Plaquetas', '312.000/mm³', '150.000–450.000/mm³'),
        ex('Glicemia', '214 mg/dL', '70–99 mg/dL em jejum', True),
        ex('Sódio / potássio', '141 / 3,4 mmol/L', 'Na 135–145 · K 3,5–5,0', True),
        ex('Ureia / creatinina', '46 / 0,8 mg/dL {{(TFG 95, CKD-EPI 2021)}}', 'até 42 / 0,6–1,1', True),
        ex('Albumina', '5,2 g/dL', '3,5–5,0 g/dL', True),
        ex('Troponina I ultrassensível', '1.840 ng/L na chegada · 3.260 ng/L em 3 horas', 'até 16 ng/L em mulheres', True),
        ex('Gasometria venosa', 'pH 7,34 · bicarbonato 21 mmol/L · lactato 2,8 mmol/L', 'lactato até 2,0', True),
    ], introducao='Colhidos na chegada, com a pressão ainda acima de 200/110 mmHg.'),

    estudo('ecg', 'Eletrocardiograma',
           'Feito na segunda hora, quando a crise já cedia: pressão de 172/100 mmHg e '
           'frequência de 78. Traçado de outro paciente com o mesmo laudo. Olhe a '
           'voltagem das precordiais e o que vem depois do QRS em V5.',
           IMG / 'ecg_admissao.jpg',
           'Traçado de outro paciente · comparação didática · 25 mm/s, 10 mm/mV.',
           credito_meta(IMG / 'ecg_admissao.jpg.json'),
        [
         ((558, 246), (470, 25), '**Onda S profunda em V2**, que atravessa a linha de V3: '
          'mais de 30 mm.', 12),
         ((763, 211), (930, 240), '**V5**: onda R alta, cortada no alto da linha, seguida '
          'de infradesnivelamento do ST com onda T de baixa amplitude.', -12),
         ((231, 386), (150, 440), '**Onda P** antes de cada QRS na tira longa de DII, com '
          'intervalo PR constante.', 12),
        ],
        ['Ritmo sinusal, cerca de 75 bpm. Critério de voltagem para sobrecarga '
         'ventricular esquerda (S de V2 somada à R de V5 acima de 35 mm), com '
         'infradesnivelamento do ST e T aplainada nas derivações laterais. Sem '
         'supradesnivelamento do ST.',
         'Hipertrofia do ventrículo esquerdo leva meses a anos para se formar.']),

    Q('p1', 1,
      'Pressão de 228/124 mmHg, dor no peito, crepitações nas bases, troponina de '
      '1.840 subindo para 3.260 ng/L em três horas. Como classificar a crise?', [
      ('Emergência hipertensiva', True),
      ('Elevação importante sem lesão aguda', False),
      ('Pseudocrise por dor ou ansiedade', False),
      ('Hipertensão acelerada-maligna', False),
      ('Hipertensão do avental branco', False),
     ], [
      ('A classificação', 'A Diretriz Brasileira de Hipertensão Arterial de 2025 '
       'separa as crises pela lesão aguda de órgão-alvo, e não pelo número. Com '
       'pressão de 180/110 mmHg ou mais, há emergência quando um órgão está sendo '
       'lesado agora: aqui, dor torácica com troponina que quase dobra em três '
       'horas e congestão pulmonar. Sem lesão aguda, é elevação importante da '
       'pressão, termo que a diretriz adotou no lugar de urgência hipertensiva, e o '
       'tratamento é oral, sem pressa.'),
      ('O eletrocardiograma', 'A voltagem alta e a alteração da repolarização em V5 '
       'são de sobrecarga do ventrículo esquerdo, dano que leva anos para se formar. '
       'Numa mulher de 41 anos cuja pressão "só subia de nervoso", ele diz que a '
       'hipertensão não é só das crises.'),
      ('Por que não as outras', 'Pseudocrise é a elevação reativa a dor ou medo, sem '
       'lesão, e a troponina a afasta. A forma acelerada-maligna exige retinopatia '
       'com hemorragias, exsudatos ou papiledema, que o fundo de olho não mostrou. '
       'Avental branco não explica troponina que sobe em três horas.'),
      ('A meta', 'Na lesão miocárdica aguda, o documento da Sociedade Europeia de '
       'Cardiologia de 2019 indica nitroglicerina endovenosa e sistólica abaixo de '
       '140 mmHg de imediato. Nas demais emergências, a pressão média cai no máximo '
       '25% na primeira hora.'),
     ]),

    pg('primeira_hora', 'Primeira hora',
       'A equipe inicia nitroglicerina endovenosa em bomba, ondansetrona para os '
       'vômitos e furosemida 20 mg pelas crepitações. Em uma hora a dor cede e a '
       'pressão chega a 162/96 mmHg. Recebe ácido acetilsalicílico e heparina como '
       'síndrome coronariana aguda sem supradesnivelamento do ST.',
       'O metoprolol endovenoso é discutido pela taquicardia e pela troponina, e '
       'fica para depois, por causa da congestão. Com a troponina em ascensão, o '
       'cateterismo é feito na mesma tarde.'),

    estudo('vent', 'Cateterismo e ventriculografia',
           'Primeiro dia, à tarde. As coronárias não têm obstrução. A ventriculografia '
           'esquerda, em oblíqua anterior direita, é mostrada no quadro da sístole. '
           'Imagem de outro paciente com o mesmo padrão do laudo de Patrícia.',
           IMG / 'ventriculografia.jpg',
           'Imagem de outro paciente · comparação didática · quadro da sístole.',
           credito_meta(IMG / 'ventriculografia.jpg.json'),
        [
         ((820, 720), (930, 900), '**Ápice e segmentos médios** dilatados e parados em '
          'sístole, cheios de contraste: a imagem em balão.', 12),
         ((668, 545), (430, 330), '**Alça do cateter** dentro do ventrículo. Em volta '
          'dela, a porção basal da cavidade fica estreita em sístole: a base contrai '
          'com força.', -12),
        ],
        ['Coronárias sem lesões obstrutivas. Acinesia dos segmentos médios e '
         'apicais, nas paredes anterior, inferior e lateral, com hipercinesia basal; '
         'fração de ejeção estimada em 35%. Pressão diastólica final do ventrículo '
         'esquerdo de 24 mmHg.']),

    Q('p2', 2,
      'Coronárias sem obstrução e, na ventriculografia, acinesia médio-apical em '
      'todas as paredes, com base hipercontrátil. Qual o mecanismo mais provável da '
      'lesão miocárdica?', [
      ('Oclusão aterotrombótica de uma coronária', False),
      ('Espasmo prolongado de uma coronária', False),
      ('Atordoamento por descarga adrenérgica', True),
      ('Inflamação do miocárdio', False),
      ('Infiltração do miocárdio', False),
      ('Embolia para uma coronária', False),
     ], [
      ('O padrão', 'Uma coronária ocluída, em espasmo ou com êmbolo produz disfunção '
       'no território dela. Aqui a acinesia dá a volta no ventrículo, nas paredes '
       'anterior, inferior e lateral, no mesmo nível, o que nenhuma artéria irriga '
       'sozinha. Esse desenho, com o ápice que se dilata e a base que contrai com '
       'força, é o da cardiomiopatia de estresse, a síndrome de takotsubo.'),
      ('O mecanismo', 'Uma descarga adrenérgica intensa atordoa o miocárdio por '
       'toxicidade direta, sobrecarga de cálcio e espasmo da microcirculação. O '
       'ápice tem mais receptores beta e sofre mais. A disfunção é reversível em '
       'dias a semanas.'),
      ('Por que não as outras', 'A inflamação do miocárdio costuma vir depois de um '
       'quadro viral e dar disfunção irregular, sem esse desenho circunferencial; a '
       'ressonância separa as duas. Infiltração não se instala em horas.'),
     ]),

    pagina('estresse', 'Discussão', 'O gatilho',
      p('Em nove de cada dez casos, a síndrome de takotsubo atinge mulheres, a maioria '
        'depois da menopausa. O gatilho pode ser emocional, como luto, discussão ou '
        'medo, ou físico, como cirurgia, crise de asma, sepse e alguns remédios. Em '
        'cerca de um terço não se encontra nenhum.'),
      p('Entre os critérios da Clínica Mayo estão a disfunção transitória além do '
        'território de uma coronária, coronárias sem lesão que a explique, alteração '
        'nova do eletrocardiograma ou da troponina e a ausência de miocardite.'),
      p('Para a equipe, o gatilho estava na história: seis meses de crises de pânico '
        'e uma crise maior hoje, no escritório, em semana de fechamento. A cardiologia '
        'registra "síndrome de takotsubo, provável gatilho emocional" e marca '
        'ecocardiograma de controle para o sétimo dia.')),

    painel('res2', 'Segundo dia', 'Sangue e urina', [
        ex('TSH', '1,6 mUI/L', '0,4–4,0 mUI/L'),
        ex('T4 livre', '1,2 ng/dL', '0,9–1,8 ng/dL'),
        ex('Glicemia de jejum', '132 mg/dL', '70–99 mg/dL', True),
        ex('Hemoglobina glicada', '6,2%', 'até 5,6%', True),
        ex('NT-proBNP', '2.450 pg/mL', 'até 125 pg/mL', True),
        ex('Cálcio total', '9,6 mg/dL', '8,6–10,2 mg/dL'),
        ex('Urina', 'Densidade 1.024 · sangue 1+ · 8 hemácias por campo, de forma normal · sem proteína', '—', True),
    ]),

    pagina('tireoide', 'Discussão', 'A tireoide',
      p('Tremor, sudorese, palpitação, perda de 6 kg e um nódulo palpável levaram o '
        'plantão a pensar em tireotoxicose, que também precipita a síndrome de '
        'takotsubo e crises de taquicardia.'),
      p('TSH de 1,6 mUI/L com T4 livre de 1,2 ng/dL afasta essa hipótese. No '
        'hipertireoidismo primário, o TSH fica suprimido, quase sempre abaixo de 0,1. '
        'A exceção, o adenoma hipofisário produtor de TSH, é rara e eleva o T4 livre.'),
      p('O nódulo de 1,5 cm do lobo direito fica para ultrassonografia no ambulatório, '
        'com a classificação de risco que decide se precisa de punção.')),

    Q('p3', 3,
      'Na chegada, hemoglobina de 16,2 g/dL, hematócrito de 49% e albumina de 5,2 '
      'g/dL, numa mulher que não fuma e satura 95% em ar ambiente. Qual a leitura '
      'mais provável?', [
      ('Contração do volume plasmático', True),
      ('Aumento da massa de hemácias', False),
      ('Resposta à hipóxia crônica', False),
      ('Erro pré-analítico da coleta', False),
      ('Variação normal para mulheres', False),
     ], [
      ('A leitura', 'Hematócrito e albumina sobem juntos quando o que falta é plasma: '
       'os dois ficam mais concentrados num volume menor. Numa massa de hemácias '
       'aumentada, a albumina seria normal. A ureia de 46 mg/dL com creatinina de 0,8 '
       'aponta no mesmo sentido, de um volume circulante contraído.'),
      ('De onde vem', 'Vasoconstrição intensa e prolongada reduz o leito venoso, e a '
       'pressão alta aumenta a perda renal de sódio e água, a natriurese pressórica. '
       'O resultado é um volume plasmático cronicamente baixo, que passa despercebido '
       'enquanto a pressão está alta.'),
      ('Por que não as outras', 'Hipóxia crônica exige saturação baixa ou doença '
       'pulmonar, e ela satura 95% sem fumar. Em mulheres, o hematócrito vai até '
       'cerca de 46%. Erro de coleta não explicaria albumina e ureia altas juntas.'),
      ('O que isso muda', 'Um volume contraído tolera mal vasodilatadores e '
       'diuréticos: a pressão pode despencar quando a vasoconstrição cede.'),
     ]),

    pg('equipe', 'O que a equipe registra',
       'Evolução do segundo dia: "Síndrome de takotsubo com gatilho emocional, em '
       'paciente com transtorno de pânico. Emergência hipertensiva na admissão, '
       'resolvida. Hipertensão arterial provavelmente antiga, com sobrecarga '
       'ventricular, sem tratamento. Pré-diabetes. Nódulo de tireoide a esclarecer. '
       'Tireotoxicose afastada."',
       'Conduta: enalapril 5 mg duas vezes ao dia; metoprolol a iniciar no terceiro '
       'dia, quando a congestão tiver passado. A psiquiatria suspende a amitriptilina '
       'e mantém a sertralina. Com 2 litros de soro nas primeiras 24 horas, o '
       'hematócrito caiu para 43%.'),

    pagina('sobras', 'Discussão', 'O que sobra',
      p('Lida de novo, a internação deixa dados que a hipótese registrada explica mal.'),
      p('A sobrecarga ventricular, aos 41 anos, pede pressão alta sustentada por anos. '
        'As medidas de 146/92 mmHg na unidade básica foram atribuídas ao nervosismo.'),
      p('A glicemia de jejum já era 118 mg/dL há dois meses, e a hemoglobina glicada é '
        '6,2%, numa mulher magra que perdeu 6 kg sem dieta.'),
      p('As crises vinham também em casa, de madrugada e nos fins de semana, longe do '
        'trabalho; duas começaram ao se abaixar; e ficaram mais frequentes depois da '
        'amitriptilina. A pior delas começou quinze minutos depois de uma ampola de '
        'metoclopramida.'),
      p('A equipe anota os quatro pontos para a consulta de retorno.')),

    pg('madrugada', 'Segunda noite, 4 horas',
       'Patrícia acorda com cefaleia em pressão, palpitação, suor e mãos frias. A '
       'enfermagem mede 204/118 mmHg e frequência de 132. Em 25 minutos, antes que a '
       'medicação chegue, a crise passa sozinha.',
       'Às 7 horas, ao levantar para o banheiro, tem tontura e quase cai: 136/84 '
       'mmHg deitada, 92/60 em pé. O plantão atribui a crise ao pânico e a queda ao '
       'enalapril e aos dois dias de leito.'),

    pg('lombar', 'Terceiro dia',
       'Pela manhã, dor lombar esquerda em peso, sem febre e sem disúria. A urina do '
       'segundo dia tinha 8 hemácias por campo, de forma normal, sem proteína: '
       'sangue que não vem do glomérulo.',
       'Com dor lombar e hematúria, a equipe pede urotomografia, com fase sem '
       'contraste, para procurar cálculo e lesão das vias urinárias. O metoprolol, '
       'programado para hoje, fica para depois do exame.'),

    estudo('tc', 'Urotomografia',
           'Terceiro dia. Corte coronal da fase nefrográfica, de outro paciente com '
           'achado semelhante ao laudo de Patrícia. Olhe acima do rim esquerdo, que '
           'fica à direita de quem vê a imagem.',
           IMG / 'tc_abdome.jpg',
           'Tomografia de outro paciente · comparação didática · corte coronal com contraste.',
           credito_meta(IMG / 'tc_abdome.jpg.json'),
        [
         ((640, 310), (880, 230), '**Massa** arredondada acima e por dentro do rim '
          'esquerdo, heterogênea, com área central menos densa.', 12),
         ((715, 470), (880, 560), '**Rim esquerdo** de contorno e realce normais, '
          'separado da massa por um plano de gordura: a massa não nasce do rim.', -12),
         ((300, 340), (130, 460), '**Fígado** homogêneo, sem nódulos.', 12),
        ],
        ['Massa sólida de 5,1 × 4,6 cm na adrenal esquerda, heterogênea, com área '
         'central de menor densidade; 38 UH na fase sem contraste e realce intenso '
         'na fase venosa. Adrenal direita e fígado sem lesões. Cálculo de 4 mm no '
         'cálice inferior esquerdo, sem dilatação, fora deste corte.',
         'O cálculo explica a dor e a hematúria. A massa é achado de um exame pedido '
         'por outra razão.']),

    Q('p4', 4,
      'Massa adrenal esquerda de 5,1 cm, heterogênea, com 38 UH sem contraste, numa '
      'mulher hipertensa. **Quais três** exames vêm antes de qualquer decisão sobre a '
      'massa?', [
      ('Metanefrinas livres no plasma', True),
      ('Cortisol após 1 mg de dexametasona', True),
      ('Aldosterona e renina', True),
      ('Biópsia percutânea guiada por tomografia', False),
      ('PET-CT com FDG', False),
      ('Ressonância magnética das adrenais', False),
      ('Cintilografia com MIBG', False),
     ], [
      ('A avaliação hormonal', 'Pela diretriz da Sociedade Europeia de Endocrinologia '
       'de 2023, todo incidentaloma adrenal faz o teste de supressão com 1 mg de '
       'dexametasona, à procura de cortisol autônomo. Metanefrinas livres no plasma, '
       'ou fracionadas na urina, entram sempre que a densidade sem contraste passa de '
       '10 UH; abaixo disso, o tumor da medula adrenal é tão improvável que a '
       'diretriz dispensa o exame. Hipertensão ou potássio baixo pedem aldosterona e '
       'renina. Patrícia tem os três motivos.'),
      ('A imagem', 'Densidade acima de 10 UH afasta o adenoma rico em gordura, a '
       'lesão benigna mais comum. Mais de 4 cm e heterogeneidade obrigam a pensar '
       'também em carcinoma adrenocortical. Ressonância e PET não substituem a '
       'dosagem hormonal, e a cintilografia com MIBG estadia, não diagnostica.'),
      ('Por que não biopsiar', 'A biópsia não separa adenoma de carcinoma '
       'adrenocortical e, num tumor que secreta catecolaminas, pode desencadear crise '
       'hipertensiva grave e hemorragia. Só entra na suspeita de metástase de outro '
       'câncer, e sempre depois de metanefrinas normais.'),
     ]),

    painel('res3', 'Investigação da massa', 'Dosagens hormonais', [
        ex('Metanefrina livre plasmática', '1.240 pg/mL', 'até 90 pg/mL', True),
        ex('Normetanefrina livre plasmática', '2.860 pg/mL', 'até 180 pg/mL', True),
        ex('3-metoxitiramina plasmática', '14 pg/mL', 'até 18 pg/mL'),
        ex('Cortisol após 1 mg de dexametasona', '1,1 µg/dL', 'até 1,8 µg/dL'),
        ex('Aldosterona / atividade de renina', '8 ng/dL / 1,3 ng/mL/h · relação 6', 'relação até 30'),
        ex('Potássio', '3,8 mmol/L', '3,5–5,0 mmol/L'),
    ], introducao='Colhidos no quinto dia, deitada, depois de 30 minutos de repouso. '
                  'A amitriptilina estava suspensa havia três dias.'),

    pagina('leitura', 'Discussão', 'A leitura das metanefrinas',
      p('Metanefrina e normetanefrina são produzidas dentro da célula do tumor, de '
        'forma contínua. Por isso sobem também entre as crises, quando as '
        'catecolaminas no sangue podem estar normais, e por isso são o exame de '
        'escolha.'),
      p('Valores acima de três a quatro vezes o limite praticamente confirmam o '
        'diagnóstico; os dela estão 14 e 16 vezes acima. A coleta deitada evita o '
        'falso-positivo da postura. A amitriptilina eleva a normetanefrina, mas não '
        'chega a esses números nem explica a metanefrina.'),
      p('A metanefrina alta, e não só a normetanefrina, é o fenótipo adrenérgico: '
        'tumor da adrenal que fabrica adrenalina, comum em algumas formas '
        'hereditárias. A 3-metoxitiramina normal fala contra tumor produtor de '
        'dopamina, de maior risco de metástase. Cortisol suprimido e relação '
        'aldosterona/renina baixa afastam outra secreção.')),

    pg('diagnostico', 'O diagnóstico',
       'É **feocromocitoma** da adrenal esquerda, tumor das células cromafins da '
       'medula adrenal que produz catecolaminas. Fora da adrenal, nos gânglios '
       'simpáticos ou parassimpáticos, a mesma célula forma o paraganglioma. A '
       'incidência gira em torno de 0,6 por 100 mil pessoas por ano, e boa parte dos '
       'casos hoje é achada em imagem pedida por outro motivo.',
       'Cefaleia, sudorese e palpitação em crises formam a tríade clássica. Os dados '
       'que sobravam se explicam: hipertensão sustentada com sobrecarga ventricular, '
       'glicemia alta e emagrecimento, volume plasmático contraído e queda da '
       'pressão ao levantar. A cardiomiopatia também: os critérios da Clínica Mayo '
       'para takotsubo exigem afastar feocromocitoma, que produz o mesmo atordoamento.',
       'Os gatilhos estavam na lista de remédios. Metoclopramida e outros '
       'antagonistas da dopamina liberam catecolaminas do tumor; tricíclicos como a '
       'amitriptilina bloqueiam a recaptação de noradrenalina; a sertralina, '
       'raramente; corticoide e betabloqueador sem alfabloqueio prévio também. A '
       'compressão do abdome, ao se abaixar, é outro gatilho conhecido. O metoprolol '
       'do terceiro dia foi suspenso antes da primeira dose.'),

    bifurcacao('b1', 'Decisão', 'O preparo',
      'Feocromocitoma de 5,1 cm, sem sinal de metástase. O ecocardiograma do sétimo '
      'dia mostra fração de ejeção de 50%, já em recuperação. A adrenalectomia está '
      'indicada. Como preparar Patrícia?', [
      caminho('Doxazosina titulada por 10 a 14 dias, com sal e líquidos; '
              'betabloqueador só depois, se a frequência subir', 'preparo',
              'O alfabloqueio primeiro tira a vasoconstrição e deixa o volume se '
              'refazer; o betabloqueador entra só para a taquicardia reflexa.'),
      caminho('Propranolol agora, pela taquicardia, e doxazosina a partir da '
              'semana que vem', 'beta_primeiro',
              'Sem o alfabloqueio, o betabloqueador deixa os receptores alfa sem '
              'oposição e tira a vasodilatação beta-2.'),
      caminho('Adrenalectomia nesta internação, sem bloqueio prévio, com '
              'nitroprussiato na sala', 'sem_preparo',
              'A anestesia e a manipulação do tumor liberam catecolaminas num '
              'paciente com volume contraído e sem receptor bloqueado.'),
    ]),

    pg('beta_primeiro', 'Duas horas depois',
       'Duas horas depois de 40 mg de propranolol, cefaleia explosiva, pressão de '
       '248/138 mmHg e falta de ar: edema pulmonar, com saturação de 84%. Vai para a '
       'UTI com nitroprussiato e ventilação não invasiva por 36 horas, e a fração de '
       'ejeção volta a 30%. A doxazosina começa na UTI, e a cirurgia é adiada em três '
       'semanas.',
       segue='preparo'),

    pg('sem_preparo', 'Centro cirúrgico, segundo dia',
       'Na laringoscopia, a pressão vai a 280/150 mmHg. Com o pneumoperitônio, antes '
       'de tocar o tumor, aparecem salvas de taquicardia ventricular e a pressão '
       'chega a 300/160, apesar do nitroprussiato em dose alta.',
       segue='b3'),

    bifurcacao('b3', 'Decisão', 'A sala de cirurgia',
      'A pressão não cede e a dissecção nem começou. O que fazer?', [
      caminho('Suspender a cirurgia, estabilizar na UTI e preparar com '
              'alfabloqueio', 'abortada',
              'Sem bloqueio, cada manipulação libera mais catecolaminas; a '
              'cirurgia volta depois do preparo.'),
      caminho('Prosseguir com a ressecção o mais rápido possível', 'colapso',
              'Retirar o tumor sem preparo troca a crise hipertensiva por um '
              'colapso num volume que nunca foi refeito.'),
    ]),

    pg('abortada', 'UTI',
       'A cirurgia é suspensa. Três dias de UTI, com nova subida da troponina e '
       'fração de ejeção de 30%. A doxazosina começa no segundo dia, e a cirurgia '
       'volta a ser marcada três semanas depois.',
       segue='preparo'),

    pg('colapso', 'Depois da veia adrenal',
       'A veia adrenal é ligada aos 40 minutos. Em cinco minutos a pressão cai de '
       '240/130 para 50/30 mmHg e não responde a volume, noradrenalina e '
       'vasopressina em doses altas; a glicemia cai a 38 mg/dL. Patrícia para em '
       'atividade elétrica sem pulso na sala, com retorno da circulação depois de 22 '
       'minutos.',
       segue='f_obito'),

    pg('preparo', 'Duas semanas de preparo',
       'Doxazosina 2 mg à noite, com aumento de 2 mg a cada dois ou três dias, até 8 '
       'mg duas vezes ao dia. Dieta com sal liberado e 2,5 a 3 litros de líquido por '
       'dia. As metas, pela Endocrine Society de 2014: pressão sentada abaixo de '
       '130/80 mmHg, sistólica em pé acima de 90, frequência de 60 a 70 sentada e de '
       '70 a 80 em pé.',
       'No nono dia a frequência chega a 104, e entra atenolol 25 mg. O nariz entope '
       'e há tontura leve ao levantar, sinais de bloqueio efetivo. O hematócrito cai '
       'de 46% para 41%, à medida que o volume se refaz. No 14.º dia: 118/76 mmHg '
       'sentada, 102/68 em pé, frequência de 72, sem crises há seis dias.',
       'No ensaio PRESCRIPT, a doxazosina e a fenoxibenzamina, que não é '
       'comercializada no Brasil, deram estabilidade semelhante na cirurgia.'),

    pg('cirurgia', 'A cirurgia',
       'Adrenalectomia esquerda por videolaparoscopia, com anestesista avisada. Na '
       'manipulação do tumor a pressão sobe a 190/100 mmHg e é controlada com '
       'nitroprussiato. Depois da ligadura da veia adrenal, cai a 82/50 e pede volume '
       'e noradrenalina em dose baixa por seis horas.',
       'Na terceira hora do pós-operatório, glicemia de 52 mg/dL, pelo rebote da '
       'insulina que as catecolaminas mantinham suprimida; a glicemia capilar segue de '
       'hora em hora por 48 horas. Doxazosina e atenolol são suspensos, e ela recebe '
       'alta no terceiro dia, sem anti-hipertensivo. As metanefrinas de seis semanas '
       'são normais.'),

    estudo('histo', 'Anatomia patológica',
           'Tumor de 5,1 cm, encapsulado, castanho, com hemorragia central. '
           'Hematoxilina-eosina, grande aumento. Lâmina de outro paciente, com o '
           'mesmo aspecto do laudo de Patrícia.',
           IMG / 'lamina_peca.jpg',
           'Lâmina de outro paciente · comparação didática.',
           credito_meta(IMG / 'lamina_peca.jpg.json'),
        [
         ((525, 75), (380, 30), '**Ninho de células** envolto por septo fino, o padrão '
          'em ninhos (Zellballen).', 12),
         ((775, 329), (900, 200), '**Capilar** com hemácias entre os ninhos: a rede '
          'vascular fina e rica do tumor.', -12),
         ((322, 429), (150, 560), '**Núcleo** redondo de cromatina finamente granular, '
          'em "sal e pimenta", com citoplasma amplo e granular em volta.', 12),
        ],
        ['Feocromocitoma: ninhos de células com citoplasma granular e núcleos de '
         'cromatina pontilhada, separados por rede capilar fina. Cromogranina A '
         'positiva. Cápsula íntegra, margens livres, sem invasão vascular.',
         'Pela classificação da OMS de 2022, todo feocromocitoma tem potencial '
         'metastático; nenhum escore histológico garante comportamento benigno, e o '
         'seguimento é por toda a vida.']),

    bifurcacao('b2', 'Decisão', 'A genética',
      'Patrícia tem 41 anos, um tumor único, sem outras lesões na tomografia. Pedir '
      'teste genético?', [
      caminho('Painel germinativo com aconselhamento genético, como para todo '
              'paciente', 'genetica',
              'Até 30 a 40% dos feocromocitomas e paragangliomas têm variante '
              'germinativa, inclusive sem história familiar conhecida.'),
      caminho('Não testar: tumor único, mais de 40 anos e família sem diagnóstico',
              'sem_genetica',
              'Idade e tumor único não afastam síndrome hereditária, e a família '
              'dela tem um bócio operado e uma morte precoce por pressão alta.'),
    ]),

    pg('sem_genetica', 'Quatro anos depois',
       'O nódulo de tireoide foi puncionado no ambulatório, com resultado de '
       'neoplasia folicular, e a lobectomia direita mostrou carcinoma medular de 1,6 '
       'cm. Sem calcitonina antes da cirurgia e sem teste genético, a tireoidectomia '
       'não foi completada e a família não foi chamada.',
       'Quatro anos depois, Patrícia nota um caroço no pescoço: calcitonina de 4.800 '
       'pg/mL, linfonodos cervicais dos dois lados e metástases no fígado. Só então o '
       'painel genético: variante patogênica do RET no códon 634. A filha, com 17 '
       'anos, tem a mesma variante e carcinoma medular com linfonodo comprometido.',
       segue='f_tardio'),

    pg('genetica', 'O painel genético',
       'Painel germinativo (RET, VHL, SDHA, SDHB, SDHC, SDHD, SDHAF2, NF1, TMEM127, '
       'MAX e FH): variante patogênica do RET no códon 634 (C634R), em heterozigose. '
       'É neoplasia endócrina múltipla tipo 2A.',
       'A mãe encontra em casa o laudo da cirurgia de 26 anos atrás: carcinoma '
       'medular de tireoide. O tio que morreu aos 44 anos teve o derrame numa crise '
       'hipertensiva, sem diagnóstico.',
       'Calcitonina de 96 pg/mL (até 5) e CEA de 6,8 ng/mL (até 5). Cálcio de 9,6 '
       'mg/dL com PTH normal. A ultrassonografia mostra o nódulo de 1,5 cm, '
       'hipoecoico e com microcalcificações, sem linfonodo suspeito.'),

    pareamento('p5', 'Pergunta 5',
      'Outros pacientes com feocromocitoma ou paraganglioma. Associe cada quadro ao '
      'gene ou síndrome mais provável.', [
      par('Carcinoma medular de tireoide e hiperparatireoidismo', 'NEM2 (RET)',
          'O quadro de Patrícia: tumor adrenal, adrenérgico, muitas vezes bilateral.'),
      par('Hemangioblastoma de cerebelo e cistos renais', 'von Hippel-Lindau',
          'Também carcinoma renal de células claras; o tumor é noradrenérgico.'),
      par('Paraganglioma abdominal com metástase óssea aos 30 anos', 'SDHB',
          'Extra-adrenal e com o maior risco de metástase entre os genes conhecidos.'),
      par('Manchas café com leite e neurofibromas', 'Neurofibromatose tipo 1',
          'O diagnóstico é clínico; o feocromocitoma aparece em poucos por cento.'),
      par('Paragangliomas do pescoço, herdados do pai', 'SDHD',
          'Só se manifesta quando a variante vem do pai, por impressão genômica.'),
    ], opcoes=['NEM2 (RET)', 'von Hippel-Lindau', 'SDHB', 'Neurofibromatose tipo 1',
               'SDHD', 'NEM1 (MEN1)'],
    titulo_resposta='O gene muda o seguimento',
    nota='A opção que sobrou, NEM1, dá tumores de paratireoide, hipófise e pâncreas; '
         'feocromocitoma nela é raro.'),

    pg('familia', 'Dois meses depois',
       'Com o tumor adrenal já retirado, Patrícia faz tireoidectomia total com '
       'esvaziamento do compartimento central. Na NEM2, a adrenal vem antes do '
       'pescoço: operar a tireoide com um feocromocitoma no lugar arrisca a crise da '
       'anestesia.',
       'Anatomia patológica: carcinoma medular de 1,2 cm no lobo direito e '
       'hiperplasia de células C nos dois lobos; nenhum dos 11 linfonodos '
       'comprometido. A calcitonina de três meses é indetectável.',
       'A equipe chama a família para uma conversa com a genética: a mãe, os dois '
       'filhos e os irmãos de Patrícia.'),

    Q('p6', 6,
      'Sobre o seguimento de Patrícia e da família, **quais quatro** afirmações '
      'estão corretas?', [
      ('Testar a variante nos dois filhos', True),
      ('Metanefrinas anuais por toda a vida', True),
      ('Calcitonina e CEA no seguimento', True),
      ('Cálcio e PTH todo ano', True),
      ('Na filha, esperar nódulo palpável', False),
      ('Alta do seguimento após cinco anos', False),
      ('Cintilografia anual de corpo inteiro', False),
     ], [
      ('A família', 'A NEM2A tem herança autossômica dominante: cada filho de '
       'portador tem 50% de chance de ter a variante. Pela Associação Americana de '
       'Tireoide de 2015, o códon 634 é de alto risco, com tireoidectomia indicada '
       'até os 5 anos de idade, guiada pela calcitonina, e rastreio do '
       'feocromocitoma a partir dos 11. Quem não tem a variante sai do rastreio.'),
      ('O seguimento de Patrícia', 'Metanefrinas todo ano por toda a vida: na NEM2, '
       'o tumor pode aparecer na outra adrenal, às vezes anos '
       'depois. Calcitonina e CEA a cada 6 a 12 meses, porque calcitonina indetectável '
       'marca a cura e a que sobe marca a volta da doença. Cálcio e PTH todo ano, '
       'pelo risco de hiperparatireoidismo no códon 634.'),
      ('O que não entra', 'Esperar nódulo palpável na filha deixa o câncer chegar aos '
       'linfonodos. Não há alta depois de cinco anos, e cintilografia não é exame '
       'de rastreio.'),
     ]),

    pg('alta', 'Seis meses depois',
       'A mãe, de 66 anos, tem a mesma variante; a calcitonina dela é indetectável e '
       'as metanefrinas são normais. A filha de 13 anos também é portadora: a '
       'tireoidectomia total mostra um carcinoma medular de 3 mm, sem linfonodos, e as '
       'metanefrinas dela são normais. O filho de 8 anos não tem a variante.',
       conforme=('b1', ['alta_cedo', 'f2', 'f2'])),

    pg('alta_cedo', 'A consulta',
       'Patrícia não teve nenhuma crise desde a cirurgia. Pressão de 118/74 mmHg sem '
       'remédio, hemoglobina glicada de 5,4% e ecocardiograma normal. A psiquiatria '
       'retira a sertralina aos poucos.'),

    fim('f1', 'Sem crises, com a família rastreada',
        'Patrícia está curada do tumor adrenal, com o carcinoma medular retirado '
        'pequeno e calcitonina indetectável. A filha foi operada antes de o câncer '
        'sair da tireoide.',
        'Alfabloqueio antes da cirurgia, ressecção sem instabilidade grave e teste '
        'genético que achou a NEM2A: as três decisões contaram, para ela e para a '
        'filha.', 'melhor'),

    fim('f2', 'Curada, depois de um percurso mais longo',
        'Patrícia também está sem crises e sem remédio, e a família foi rastreada. O '
        'caminho custou dias de UTI, uma nova queda da fração de ejeção e semanas a '
        'mais até a cirurgia.',
        'Betabloqueador sem alfabloqueio prévio deixa os receptores alfa sem '
        'oposição, e anestesia sem preparo expõe o miocárdio a picos de pressão; os '
        'dois caminhos acrescentaram dano a um coração que se recuperava.', 'medio'),

    fim('f_tardio', 'Carcinoma medular com metástases',
        'Patrícia vive com carcinoma medular metastático, em tratamento com inibidor '
        'de RET, e a filha foi operada com linfonodo já comprometido.',
        'Sem teste genético, a NEM2A ficou escondida atrás de um tumor adrenal tido '
        'como esporádico. O carcinoma medular, curável quando pequeno, foi achado '
        'com metástases, e a família não foi rastreada a tempo.', 'pior'),

    fim('f_obito', 'Óbito no centro cirúrgico',
        'Depois da parada, Patrícia evolui com choque refratário e morre na UTI no '
        'mesmo dia.',
        'Operar sem alfabloqueio e insistir na ressecção durante a crise levou a '
        'picos de pressão e, depois da ligadura da veia, a um colapso num volume '
        'plasmático que nunca tinha sido refeito.', 'pior'),

    pagina('retrospectiva', 'Pontos de ensino', '',
        pontos(
            'Crises de cefaleia, sudorese e palpitação com pressão alta pedem '
            'metanefrinas antes do rótulo de pânico. Pânico não produz sobrecarga '
            'ventricular, hiperglicemia nem perda de peso.',
            'Emergência hipertensiva é definida pela lesão aguda de órgão-alvo, e não '
            'pelo número da pressão.',
            'A síndrome de takotsubo só se fecha depois de afastado o feocromocitoma, '
            'que produz o mesmo atordoamento miocárdico.',
            'Metoclopramida, tricíclicos, corticoide e betabloqueador sem alfabloqueio '
            'podem precipitar uma crise grave.',
            'Massa adrenal com mais de 10 UH sem contraste pede metanefrinas, e nunca '
            'se biopsia antes delas.',
            'O preparo é alfabloqueio por 10 a 14 dias, com sal e líquidos; o '
            'betabloqueador entra depois, só para a taquicardia.',
            'Todo paciente com feocromocitoma faz teste genético. Na NEM2, a adrenal '
            'é operada antes da tireoide, e a família é rastreada.'),
        so_kicker=True),

    pg('referencias', 'Fontes e limites',
       'Paciente, valores e percursos são ficcionais. A foto de abertura é da orla '
       'de Fortaleza, sem relação com o caso.',
       'Lenders e cols. Pheochromocytoma and paraganglioma: an Endocrine Society '
       'clinical practice guideline, J Clin Endocrinol Metab 2014. Nölting e cols. '
       'Personalized management of pheochromocytoma and paraganglioma, Endocr Rev '
       '2022. Fassnacht e cols. European Society of Endocrinology clinical practice '
       'guidelines on the management of adrenal incidentalomas, Eur J Endocrinol '
       '2023. Buitenwerf e cols. PRESCRIPT, J Clin Endocrinol Metab 2020. Wells e '
       'cols. Revised American Thyroid Association guidelines for the management of '
       'medullary thyroid carcinoma, Thyroid 2015. Brandão e cols. Diretriz '
       'Brasileira de Hipertensão Arterial 2025, Arq Bras Cardiol 2025. van den Born '
       'e cols. ESC Council on Hypertension position document on the management of '
       'hypertensive emergencies, Eur Heart J Cardiovasc Pharmacother 2019. Ghadri e '
       'cols. International Expert Consensus Document on Takotsubo Syndrome, Eur '
       'Heart J 2018.',
       'Imagens, todas de outros pacientes, com setas adicionadas, do Wikimedia '
       'Commons: eletrocardiograma, Michael Rosengarten (CardioNetworks ECGpedia), CC '
       'BY-SA 3.0, recortado (commons.wikimedia.org/wiki/File:E242_(CardioNetworks_ECGpedia).jpg); '
       'ventriculografia, Gangadhar, Von der Lohe, Sawada e Helft, CC BY 2.0 '
       '(commons.wikimedia.org/wiki/File:Takotsubo_ventriculography.gif); '
       'tomografia, Drahreg01, CC BY-SA 3.0 '
       '(commons.wikimedia.org/wiki/File:Phaeochromozytoma_CT_coronal.jpg); lâmina, '
       'Nephron, CC BY-SA 3.0 '
       '(commons.wikimedia.org/wiki/File:Pheochromocytoma_high_mag.jpg); orla de '
       'Fortaleza, RonaldoMorais, CC BY-SA 4.0 '
       '(commons.wikimedia.org/wiki/File:Calçadão_na_orla_da_praia-_Fortaleza.jpg).'),
]

REVISAO = []

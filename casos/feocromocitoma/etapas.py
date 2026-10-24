"""Revisão editorial de 23/10/2026: evolução clínica, decisões precoces e
urgências preservadas. Paciente e cronologia ficcionais; fontes na última tela.
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

    capa(TITULO, fundo='cena-paciente.png', kicker='Caso interativo',
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

    pg('socorro', 'Avaliação e tratamento imediatos',
 'Patrícia recebe monitorização e nitroglicerina EV titulada pela emergência hipertensiva com congestão e dor torácica. Recebe furosemida 20 mg, com reavaliação do volume. A cefaleia abrupta exige investigação paralela: TC de crânio e angiotomografia não mostram hemorragia ou aneurisma; neurologia acompanha, sem atribuir automaticamente a dor ao nervosismo.',
 'Para possível síndrome coronariana, a equipe realiza avaliação de risco e inicia tratamento antitrombótico após a avaliação neurológica. Betabloqueador EV é evitado na insuficiência cardíaca aguda. A amitriptilina é suspensa; a exposição à metoclopramida fica registrada. As telas seguintes recuperam dados desta avaliação, sem representar atraso no cuidado.'),

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

    pg('primeira_resposta', 'Ao fim das primeiras duas horas',
 'A dor no peito e a cefaleia cedem, pressão 162/96 e frequência 88. As crepitações diminuem. A troponina, entretanto, continua subindo e o ecocardiograma mostra FE de 35%, com acinesia médio-apical além de um único território coronariano e sem obstrução da via de saída.',
 'A melhora dos sintomas não eliminou lesão miocárdica aguda. A equipe precisa distinguir doença coronariana tratável de causas de disfunção ventricular sem obstrução.'),

    Q('p1', 1, 'Após estabilizar pressão e congestão, qual exame priorizar nesta apresentação de alto risco, com troponina dinâmica e disfunção ventricular?', [
 ('Coronariografia invasiva', True), ('Angiotomografia coronariana', False),
 ('Ressonância cardíaca', False), ('Cintilografia de perfusão em repouso', False)
 ], [('Prioridade', 'A estratégia invasiva é favorecida pela possibilidade de síndrome coronariana de alto risco e de intervenção. Eco já orientou função e complicações. RM poderá esclarecer miocardite e padrão de lesão se persistir dúvida; angio-TC tem lugar em pacientes selecionados de menor risco. A escolha depende da estabilidade e da avaliação cardiológica.')]),

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

    pg('recuperacao', 'Segundo dia',
 'Sem dor e sem dispneia em repouso, caminha até a poltrona. Pulmões agora sem crepitações. Não há obstrução coronariana e a distribuição ventricular favorece padrão de takotsubo; a etiologia do estímulo ainda está aberta.',
 'A equipe considera gatilho emocional, miocardite e excesso de catecolaminas. As crises de meses, a perda de peso e o agravamento após medicações motivam investigação endócrina durante a internação. Não é preciso esperar uma massa incidental para solicitá-la.'),

    painel('res2', 'Segundo dia', 'Sangue e urina', [
        ex('TSH', '1,6 mUI/L', '0,4–4,0 mUI/L'),
        ex('T4 livre', '1,2 ng/dL', '0,9–1,8 ng/dL'),
        ex('Glicemia de jejum', '132 mg/dL', '70–99 mg/dL', True),
        ex('Hemoglobina glicada', '6,2%', 'até 5,6%', True),
        ex('NT-proBNP', '2.450 pg/mL', 'até 125 pg/mL', True),
        ex('Cálcio total', '9,6 mg/dL', '8,6–10,2 mg/dL'),
        ex('Urina', 'Densidade 1.024 · sangue 1+ · 8 hemácias por campo, de forma normal · sem proteína', '—', True),
    ]),

    Q('p2', 2, 'Quais duas hipóteses merecem maior prioridade para explicar as crises anteriores à internação, nesta fase?', [
 ('Tumor produtor de catecolaminas', True), ('Transtorno de pânico coexistente', True),
 ('Tireotoxicose primária', False), ('Síndrome serotoninérgica persistente por seis meses', False),
 ('Hipoglicemia recorrente documentada', False)
 ], [('Hierarquia', 'A recorrência estereotipada, a hipertensão e a lesão cardíaca tornam prioritária a pesquisa de excesso catecolaminérgico. Pânico permanece possibilidade ou comorbidade; não deve ser usado para encerrar a investigação. TSH e T4 livre normais pesam contra tireotoxicose. Não há clônus ou hipertermia sustentada, e a glicose observada está elevada.')]),

    pg('madrugada', 'Segunda noite',
 'Enquanto dormia, acorda pálida, suando, com cefaleia e palpitação. PA 204/118 e frequência 132. A equipe a reavalia ao leito; a crise cede em cerca de 20 minutos, sem nova congestão. Permanece monitorizada. Na manhã seguinte, ao levantar, quase cai: PA 136/84 deitada e 92/60 em pé.',
 'A recorrência em repouso e o ortostatismo entre crises mudam a segurança de apenas intensificar anti-hipertensivos de longa ação. O diurético não é repetido na ausência de congestão; a reposição de volume será cautelosa pela disfunção ventricular recente.'),

    bifurcacao('b1', 'Investigação', 'Primeiro teste bioquímico',
 'O laboratório dispõe de dois métodos validados. Qual você escolhe para iniciar o rastreio das crises?', [
 caminho('Metanefrinas livres plasmáticas', 'coleta_plasma', 'É possível coletar após repouso e registrar interferentes; o resultado deve ser interpretado no contexto da doença aguda.'),
 caminho('Metanefrinas fracionadas urinárias de 24 horas', 'coleta_urina', 'Alternativa válida se a coleta for completa e o método adequado; o prazo de coleta é considerado na avaliação do paciente internado.')]),

    pg('coleta_plasma', 'Preparo da coleta',
 'Com Patrícia estável, colhe-se sangue após 30 minutos de repouso deitada. A amitriptilina havia sido suspensa na admissão, cerca de dois dias antes; o intervalo pode ser insuficiente para eliminar interferência. O laboratório registra método e limites próprios. A avaliação anatômica ocorrerá em paralelo, se indicada pela queixa lombar.', segue='lombar'),

    pg('coleta_urina', 'Uma coleta completa',
 'A coleta urinária começa no terceiro dia e termina no quarto, enquanto a investigação da dor lombar descrita adiante ocorre em paralelo. Creatinina e volume tornam a coleta plausivelmente completa. Metanefrina 2.400 µg/24 h (referência 30–350) e normetanefrina 3.600 µg/24 h (referência 88–444). Pela doença aguda e pelo tricíclico recente, a equipe programa confirmação plasmática em condições controladas. A intensidade da elevação impede encerrar a avaliação como ansiedade.', segue='lombar'),

    pg('lombar', 'Terceiro dia',
 'Surge dor lombar esquerda, sem febre ou disúria, e hematúria microscópica. A equipe avalia via urinária com tomografia, incluindo fase sem contraste. A pesquisa de excesso catecolaminérgico já está em andamento; a imagem não foi condição para lembrar dessa hipótese.',
 'A dor cede com analgesia, sem expulsão de cálculo observada. Um cálculo calicial pequeno pode acompanhar hematúria, mas sua presença sem obstrução não prova que causou toda a dor.'),

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
         'O cálculo pode acompanhar a hematúria; sem obstrução, não prova a causa da dor. A massa adrenal exige integração com as crises e a investigação hormonal já indicada.']),

    pg('antes_resultado', 'Recuperação desigual',
 'No quarto dia, a FE já chega a 45% e Patrícia anda sem falta de ar. Ao tomar banho, entretanto, volta a ter suor e palpitação com PA 188/106; o episódio dura dez minutos. Não há dor torácica ou nova elevação significativa da troponina.',
 'A melhora cardíaca e a persistência das crises seguem ritmos diferentes. A equipe mantém internação monitorizada e evita betabloqueio isolado até esclarecer a secreção hormonal. Não propõe biópsia da massa vascular antes dessa avaliação.'),

    painel('res3', 'Bioquímica', 'Resultados plasmáticos', [
 ex('Metanefrina livre plasmática', '1.240 pg/mL', 'até 90 pg/mL', True),
 ex('Normetanefrina livre plasmática', '2.860 pg/mL', 'até 180 pg/mL', True)
 ], introducao='Resultados da coleta em repouso, disponíveis a todos os percursos. No ramo urinário, correspondem à coleta confirmatória no quinto dia; no outro, à coleta inicial no terceiro dia. Não foram omitidos resultados indicados para prolongar a investigação.'),

    Q('p3', 3, 'Considerando massa adrenal, elevação acentuada dos dois metabólitos e tricíclico recentemente suspenso, qual interpretação tem maior sustentação?', [
 ('Forte evidência de tumor produtor de catecolaminas', True),
 ('Interferência farmacológica como explicação suficiente do conjunto', False),
 ('Massa não funcionante com crises independentes do achado adrenal', False),
 ('Elevação transitória explicada suficientemente pela cardiomiopatia', False)
 ], [('Probabilidade e limite', 'A magnitude, a elevação de ambos os metabólitos e a concordância clínica e anatômica tornam a secreção tumoral muito provável. Estresse, método e remédios precisam ser reconhecidos: repouso reduz interferência postural, mas não elimina todos os falsos positivos. Não é correto afirmar que tricíclicos nunca geram elevações importantes.'),
 ('Ação', 'O conjunto permite organizar manejo especializado sem biópsia. Resultado limítrofe ou discordante pediria repetição após recuperação e revisão de interferentes; não é a situação apresentada.')]),

    pg('diagnostico', 'Integração diagnóstica',
 'O conjunto é de feocromocitoma da adrenal esquerda, com excesso catecolaminérgico e disfunção miocárdica no padrão de takotsubo. Os critérios InterTAK admitem o feocromocitoma como gatilho; não é necessário negar a síndrome cardíaca para reconhecer a causa endócrina.',
 'A hipótese explica as crises e a contração do volume circulante; não torna cada sintoma específico. O nódulo tireoidiano e o bócio operado da mãe exigem recuperar documentos e aconselhamento genético já nesta fase, sem aguardar anos de seguimento.'),

    pg('preparo_inicial', 'Primeira semana de preparo',
 'A equipe inicia doxazosina em dose baixa e titula conforme pressão sentada/em pé e sintomas. Com o pulmão seco e função ventricular em recuperação, ajusta sal e líquidos gradualmente, sem meta fixa de litros para quem teve congestão.',
 'As crises ficam menos frequentes. No quinto dia de bloqueio, ao aumentar a dose, Patrícia volta a sentir tontura em pé; PA 88/56, sem dispneia ou edema. O plano precisa ser ajustado antes de prosseguir a escalada.'),

    bifurcacao('b2', 'Preparo', 'Ortostatismo durante a titulação',
 'Qual medida você prioriza na próxima reavaliação do preparo?', [
 caminho('Reavaliar a velocidade de titulação da doxazosina', 'ajuste_dose', 'A dose pode exceder a tolerância naquele momento; não se deve usar tontura como meta de bloqueio.'),
 caminho('Reavaliar o volume circulante à beira do leito', 'ajuste_volume', 'Reposição insuficiente pode contribuir, mas congestão recente exige avaliação antes de aumentar sal e líquido.')]),

    pg('ajuste_dose', 'Titulação individualizada',
 'A escalada é pausada e a dose, revista. No dia seguinte a PA em pé sobe para 102/66 e a tontura diminui, sem retorno de crises intensas. A equipe completa também avaliação de volume e tolerância cardíaca antes de novos ajustes.', segue='preparo'),

    pg('ajuste_volume', 'Volume e função cardíaca',
 'Sem edema, crepitações ou sinais ultrassonográficos de congestão, permite-se aumento cauteloso da ingestão. O ortostatismo melhora; a equipe também pausa a escalada da doxazosina até tolerância adequada. Não se usa reposição agressiva automática.', segue='preparo'),

    pg('preparo', 'Duas semanas depois',
 'Patrícia está há seis dias sem crises, PA sentada 118/76 e em pé 102/68, frequência 72. A FE é 55%. Taquicardia persistente foi tratada apenas depois de alfabloqueio estabelecido. O preparo e o momento da cirurgia são pactuados com endocrinologia, cardiologia, cirurgia e anestesia.',
 'Após recuperação da fase aguda, cortisol pós-dexametasona de 1 mg é 1,1 µg/dL. Aldosterona 8 ng/dL e atividade de renina 1,3 ng/mL/h foram avaliadas com potássio corrigido e revisão dos interferentes: não sustentam hiperaldosteronismo, sem excluir todo distúrbio em qualquer condição de coleta.'),

    pg('cirurgia', 'Adrenalectomia e vigilância inicial',
 'É feita adrenalectomia esquerda videolaparoscópica. Há oscilação pressórica transitória tratada pela anestesia. No pós-operatório, hipotensão leve responde a suporte cuidadosamente titulado; a glicemia cai a 52 mg/dL, é prontamente corrigida com glicose e permanece monitorizada.',
 'A ocorrência ilustra riscos de retirada da fonte de catecolaminas, sem exigir colapso ou parada cardíaca para justificar o preparo. Doxazosina e o betabloqueador são suspensos conforme pressão e frequência.'),

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

    pg('genetica', 'A investigação familiar',
 'O aconselhamento iniciado no preparo é seguido de painel germinativo: variante patogênica RET C634R em heterozigose, sustentando NEM2A. A mãe encontra o laudo do bócio operado: carcinoma medular da tireoide. A morte do tio por derrame não permite atribuir retrospectivamente um tumor sem comprovação.',
 'Patrícia tem calcitonina 96 pg/mL (até 5), CEA 6,8 ng/mL (até 5), cálcio 9,6 mg/dL e PTH normal. O ultrassom mostra nódulo tireoidiano direito de 1,5 cm, hipoecoico, com microcalcificações. A equipe organiza tratamento cervical após controlar o feocromocitoma.'),

    Q('p4', 4, 'A variante familiar já é conhecida. Qual exame tem maior rendimento para identificar quais filhos herdaram esse risco?', [
 ('Pesquisa dirigida de RET C634R', True), ('Calcitonina basal', False),
 ('Ultrassonografia cervical', False), ('Metanefrinas plasmáticas', False)
 ], [('Finalidades', 'A pesquisa dirigida responde à herança; exames bioquímicos e imagem avaliam doença já expressa e podem estar normais em portadores. Encaminhamento dos filhos de 13 e 8 anos é prioritário, com aconselhamento e conduta conforme idade, variante e avaliação clínica, sem esperar sintomas.')]),

    pg('familia', 'Depois do controle adrenal',
 'Patrícia faz tireoidectomia total com esvaziamento central. Há carcinoma medular de 1,2 cm e hiperplasia bilateral de células C, sem comprometimento dos 11 linfonodos. Calcitonina de três meses indetectável.',
 'A mãe e a filha de 13 anos têm a variante; o filho de 8 anos não. A avaliação especializada da filha identifica carcinoma medular de 3 mm, sem linfonodos. Não se presume que toda família terá a mesma expressão ou evolução.'),

    pg('seguimento', 'Seis meses depois',
 'Sem novas crises, PA 118/74 sem anti-hipertensivos, HbA1c 5,4% e ecocardiograma normal. Metanefrinas pós-operatórias de seis semanas normais documentam resposta bioquímica; a histologia não garante risco zero de recorrência ou metástase.',
 'Mantém vigilância prolongada, neste contexto hereditário por toda a vida: metanefrinas, acompanhamento do carcinoma medular e avaliação de cálcio/PTH conforme indicação. A sertralina é revista com a psiquiatria, sem afirmar que qualquer ansiedade futura terá causa tumoral.'),

    fim('f1', 'Recuperação e vigilância familiar',
 'Patrícia recuperou função cardíaca e controle bioquímico após ressecção, com NEM2A reconhecida e família avaliada.',
 'A melhora inicial não explicou as crises noturnas; sua recorrência antecipou a investigação. O ortostatismo mudou o preparo, e a história familiar mudou o alcance do cuidado.', 'melhor'),

    pagina('retrospectiva', 'Pontos de ensino', '', pontos(
 'Emergência hipertensiva exige lesão aguda de órgão, com tratamento e investigação paralelos.',
 'Recuperação ventricular não encerra a pesquisa de crises autonômicas recorrentes.',
 'Metanefrinas plasmáticas ou urinárias fracionadas são opções de rastreio; revisar método, postura e medicamentos.',
 'InterTAK admite feocromocitoma como gatilho de takotsubo.',
 'Alfabloqueio precede betabloqueio; reposição de volume respeita tolerância cardíaca.',
 'Genética e avaliação do nódulo não devem depender de complicações tardias.'), so_kicker=True),

    pg('referencias', 'Fontes e limites',
 'Paciente, cronologia e percursos ficcionais. Imagens clínicas são de outras pessoas; a abertura é a orla de Fortaleza.',
 'Revisão: <a href="https://pubmed.ncbi.nlm.nih.gov/41083371/">Japan Endocrine Society, diretriz 2025, publicação em volume de 2026</a>; <a href="https://pubmed.ncbi.nlm.nih.gov/37318239/">ESE/ENSAT, incidentalomas, 2023</a>; <a href="https://pubmed.ncbi.nlm.nih.gov/24893135/">Endocrine Society, 2014</a>; <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC5991216/">InterTAK, 2018</a>; ATA, carcinoma medular, 2015. A diretriz japonesa é contextualizada; acesso e recomendações locais não são presumidos iguais no Brasil.',
 'Wikimedia Commons, setas preservadas: ECG, Michael Rosengarten (CardioNetworks ECGpedia), CC BY-SA 3.0, recortado (File:E242_(CardioNetworks_ECGpedia).jpg); ventriculografia, Gangadhar, Von der Lohe, Sawada e Helft, CC BY 2.0 (File:Takotsubo_ventriculography.gif); TC, Drahreg01, CC BY-SA 3.0 (File:Phaeochromozytoma_CT_coronal.jpg); lâmina, Nephron, CC BY-SA 3.0 (File:Pheochromocytoma_high_mag.jpg). Abertura: ilustração original da paciente ficcional, gerada com OpenAI imagegen para o projeto em 24/10/2026; não é fotografia clínica.')
]

REVISAO = []

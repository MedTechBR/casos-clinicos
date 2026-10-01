"""Tosse, rouquidão e uma ferida no lábio num lavrador de café de Rondônia.

Escrito em 01/10/2026 no molde do //New England// aprovado (modelos:
endocardite e leptospirose; ver
Artifacts/nejm-casos-classicos/GRAMATICA_LIDA_2026-09-26.md). Apresentação
curta, ficha com a pista enterrada no ruído (roça de café desde criança,
derrubada de mata em Rondônia, omeprazol por conta própria, dobras palmares
escuras), exame com os vitais em cima e primeiros exames entregues prontos.
Seis perguntas no caminho padrão, com um pareamento; as três antes da
virada só interpretam (mecanismo da hipoxemia, compartimento e extensão na
radiografia, grupo de processos das lesões), com alternativas que são
categorias. A equipe registra duas âncoras razoáveis: tuberculose com
baciloscopia e teste molecular negativos, e carcinoma epidermoide de lábio
ou laringe num fumante de 40 maços-ano. A virada é a biópsia do lábio, com
leveduras de parede espessa e brotos múltiplos na prata; o nome aparece na
página "O diagnóstico", logo depois da metade do percurso. Depois: forma
crônica multifocal, gravidade pelos critérios do consenso, insuficiência
adrenal primária, itraconazol e critérios de cura, sequelas e cigarro.
Três decisões de conduta mudam o desfecho.

Paciente ficcional. Fonte principal: II Consenso Brasileiro em
Paracoccidioidomicose (Shikanai-Yasuda e cols., Epidemiol Serv Saúde 2018;
versão em inglês, Rev Soc Bras Med Trop 2017). Insuficiência adrenal:
Bornstein e cols., Endocrine Society 2016. Tuberculose: Manual de
Recomendações para o Controle da Tuberculose no Brasil, 2.ª ed., 2019.
Filtração pelo CKD-EPI 2021.
"""
import json
from pathlib import Path

from motor.estudo_imagem import estudo
from motor.etapas import (alt, bifurcacao, caminho, capa, desfecho, op, p,
                          pagina, painel, par, pareamento, pergunta, pontos,
                          topicos, vitais)

TITULO = 'A ferida do lábio'
RODAPE = 'Paciente ficcional · evoluções simuladas para ensino'
COR = '#a16207'
IMG = Path(__file__).parent / 'img'
BANCO = []
MOLDE = 'nejm'
CENA = 'cena.jpg'


def credito_meta(meta):
    m = json.loads(Path(meta).read_text())
    return m['autor'] + ' · Wikimedia Commons · ' + m['licenca'] + ' · setas adicionadas'


def pg(k, titulo, *textos, segue='', conforme=None):
    return pagina(k, titulo, '', *(p(t) for t in textos), so_kicker=True,
                  segue=segue, conforme=conforme)


def disc(k, titulo, *textos):
    return pagina(k, 'Discussão', titulo, *(p(t) for t in textos))


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
    capa(TITULO, fundo=CENA, kicker='Caso interativo',
         selo='Paciente ficcional · procedência e créditos na última tela'),

    pg('historia', 'Apresentação',
       'Valdir, lavrador de 52 anos, é encaminhado pela unidade básica de '
       'Cacoal, em Rondônia, ao ambulatório de clínica médica do hospital '
       'regional. Tosse há quatro meses e perdeu o fôlego para subir o morro '
       'do cafezal. Pesava 70 kg; hoje pesa 61.',
       'Há três meses apareceu uma ferida no lábio inferior que dói para '
       'comer e não fecha, e há dois meses a voz ficou rouca. A tosse tem '
       'pouco catarro claro.',
       'Na unidade básica recebeu amoxicilina por sete dias e nistatina para '
       'a boca, sem mudança. Duas baciloscopias de escarro foram negativas, e '
       'o teste rápido molecular para tuberculose no escarro não detectou o '
       'bacilo. Nega febre medida, suor noturno, sangue no catarro, dor no '
       'peito, dificuldade para engolir e diarreia.'),

    pagina('ficha', 'Ficha do paciente', '',
           topicos(('Antecedentes', 'Hipertensão diagnosticada há três anos na '
                    'unidade básica. Uma pneumonia aos 40 anos, tratada em casa. '
                    'Nunca fez endoscopia nem exame de pulmão.'),
                   ('Medicações', 'Hidroclorotiazida 25 mg ao dia, quando lembra. '
                    'Omeprazol 20 mg comprado na farmácia, quase todo dia, para '
                    'queimação. Dipirona para a dor da boca.'),
                   ('Hábitos', 'Fuma desde os 12 anos, um maço por dia, hoje mais '
                    'cigarro de palha: cerca de 40 maços-ano. Três a quatro doses '
                    'de cachaça por dia, mais no fim de semana.'),
                   ('Trabalho e moradia', 'Nasceu no norte do Paraná e trabalha na '
                    'roça de café desde os 9 anos. Aos 24 veio para Rondônia, '
                    'onde ajudou a derrubar mata para abrir o sítio. Hoje planta '
                    'café e mandioca e colhe e abana o café à mão. Na colheita, '
                    'o alojamento do sítio recebe trabalhadores de fora.'),
                   ('Família', 'Pai morreu aos 61 anos de "câncer na garganta"; '
                    'fumava. Mãe viva, diabética. Um colega do alojamento tratou '
                    'tuberculose há dois anos.')),
           so_kicker=True),

    pagina('exame', 'Exame físico', '',
           vitais(('Temperatura', '37,4 °C', False),
                  ('Pressão arterial', '112/70', False),
                  ('Frequência cardíaca', '94', False),
                  ('Frequência respiratória', '22', True),
                  ('SpO₂ em ar ambiente', '93%', True),
                  ('Peso', '61 kg', True)),
           topicos(('Estado geral', 'Emagrecido, descorado, voz rouca e soprosa. '
                    'Altura de 1,70 m.'),
                   ('Boca e face', 'No lábio inferior, à esquerda, lesão de 1,5 cm, '
                    'endurecida, de superfície granulosa com pontos vermelho-escuros '
                    'e crosta central. Duas lesões menores, de 5 a 8 mm, no sulco '
                    'nasolabial direito e no mento. Na gengiva inferior, área '
                    'granulosa que sangra ao toque. Dentes em mau estado.'),
                   ('Linfonodos', 'Submandibulares e cervicais anteriores dos dois '
                    'lados, de 1 a 2 cm, endurecidos, pouco dolorosos, móveis, sem '
                    'fístula.'),
                   ('Pulmões', 'Murmúrio diminuído. Estertores finos nas regiões '
                    'infraescapulares e entre as escápulas, dos dois lados.'),
                   ('Coração e abdome', 'Ritmo regular, sem sopros. Fígado no '
                    'rebordo, baço não palpável.'),
                   ('Pele', 'Queimada de sol no rosto, no pescoço e nos antebraços. '
                    'As dobras das palmas são mais escuras que o resto da mão.')),
           so_kicker=True),

    painel('res1', 'Primeiros exames', 'Sangue', [
        ex('Hemoglobina / hematócrito', '11,6 g/dL / 35% · VCM 86 fL', 'Hb 13,5–17,5 g/dL', True),
        ex('Leucócitos', '9.400/mm³ · neutrófilos 68% · eosinófilos 6% {{(564/mm³)}}', '4.000–11.000 · eos até 500', True),
        ex('Plaquetas', '412.000/mm³', '150.000–450.000/mm³'),
        ex('VHS / proteína C reativa', '62 mm/h / 38 mg/L', 'até 20 / até 5', True),
        ex('Sódio / potássio', '133 / 5,0 mmol/L', '135–145 / 3,5–5,1', True),
        ex('Ureia / creatinina', '30 / 0,9 mg/dL {{(TFG 103, CKD-EPI 2021)}}', 'até 42 / 0,7–1,3'),
        ex('Proteínas totais / albumina', '7,9 / 3,1 g/dL {{(globulinas 4,8)}}', '6,0–8,0 / 3,5–5,0', True),
        ex('AST / ALT / fosfatase alcalina', '28 / 22 / 96 U/L', 'até 40 / 41 / 129'),
        ex('Glicemia de jejum', '84 mg/dL', '70–99 mg/dL'),
    ], introducao='Colhidos na primeira consulta, com a nova amostra de escarro '
                  'para cultura de micobactérias.'),

    painel('res1b', 'Primeiros exames', 'Gasometria e outros', [
        ex('Gasometria arterial em ar ambiente', 'pH 7,45 · pCO₂ 33 · pO₂ 64 mmHg · HCO₃ 22,5 · SatO₂ 93%', '—', True),
        ex('Teste rápido para HIV', 'Não reagente', 'não reagente'),
        ex('Urina', 'Sem alterações', '—'),
        ex('Eletrocardiograma', 'Ritmo sinusal, 92 bpm, sem alterações', '—'),
    ]),

    Q('p1', 1,
      'Em ar ambiente, pO₂ de 64 mmHg com pCO₂ de 33 mmHg, num homem de 52 '
      'anos, em Cacoal. Qual o mecanismo principal da hipoxemia?', [
      ('Hipoventilação alveolar', False),
      ('Baixa pressão inspirada de oxigênio', False),
      ('Desequilíbrio ventilação-perfusão no parênquima', True),
      ('Shunt intracardíaco', False),
      ('Transporte reduzido pela anemia', False),
      ('Fadiga da musculatura respiratória', False),
     ], [
      ('O cálculo', 'A pressão alveolar de oxigênio em ar ambiente é cerca de '
       '150 menos a pCO₂ dividida por 0,8: 150 − 33/0,8, perto de 109 mmHg. '
       'Com pO₂ de 64, o gradiente alvéolo-arterial é de cerca de 45 mmHg, '
       'quando o esperado para 52 anos fica perto de 17 (idade dividida por '
       '4, mais 4). O oxigênio chega ao alvéolo e não passa para o sangue.'),
      ('Por que não as outras', 'Hipoventilação, por qualquer causa, inclusive '
       'fadiga, elevaria a pCO₂, que está baixa: ele hiperventila. Cacoal fica '
       'a cerca de 200 m de altitude, sem queda da pressão inspirada. A anemia '
       'reduz o conteúdo de oxigênio, não a pO₂. Shunt intracardíaco é '
       'improvável sem sopro nem cianose e não explicaria os estertores.'),
      ('O que isso indica', 'Gradiente alargado com estertores finos dos dois '
       'lados põe o problema no parênquima: alvéolos mal ventilados para a '
       'perfusão que recebem e, no esforço, troca lenta por uma membrana '
       'espessada. É doença difusa do pulmão; a radiografia dirá de que tipo.'),
     ]),

    estudo('rx_adm', 'Radiografia de tórax',
           'Radiografia em incidência posteroanterior, feita na primeira '
           'consulta. Antes de abrir os achados, compare a extensão da imagem '
           'com a saturação de 93% e os estertores discretos.',
           IMG / 'rx_torax.jpg',
           'Radiografia de outro paciente · comparação didática.',
           credito_meta(IMG / 'rx_torax.jpg.json'),
        [
         ((300, 650), (90, 560), '**Linhas finas e pequenos nódulos** que se somam junto ao hilo '
          'direito, no terço inferior.', 12),
         ((849, 700), (935, 560), 'O mesmo desenho no **pulmão esquerdo**, em espelho.', -12),
         ((349, 131), (150, 80), '**Ápice direito** com transparência preservada.', 12),
        ],
        ['Opacidades reticulares e micronodulares nos dois pulmões, simétricas, '
         'mais densas junto aos hilos e nos terços médio e inferior; ápices '
         'relativamente preservados.',
         'Sem cavidade evidente, sem derrame pleural, área cardíaca normal.']),

    Q('p2', 2,
      'Pela radiografia e pelo exame, **quais duas** leituras estão '
      'corretas?', [
      ('Acometimento do interstício, com micronódulos', True),
      ('Extensão maior do que o exame sugere', True),
      ('Consolidação do espaço aéreo', False),
      ('Padrão de reativação apical', False),
      ('Padrão de congestão cardíaca', False),
      ('Doença pleural predominante', False),
     ], [
      ('O compartimento', 'Linhas finas que formam rede e nódulos de poucos '
       'milímetros são a expressão do interstício: septos, espaço em volta dos '
       'brônquios e vasos, e granulomas pequenos. O espaço aéreo cheio daria '
       'opacidade confluente, com broncograma aéreo.'),
      ('A dissociação', 'Opacidades nos dois pulmões, do hilo à periferia, num '
       'homem com saturação de 93% em repouso e estertores discretos. Imagem '
       'maior que a clínica é a dissociação clínico-radiológica, comum nas '
       'doenças granulomatosas crônicas do pulmão e nas pneumoconioses, em que '
       'a lesão se instala devagar e o pulmão se adapta.'),
      ('Por que não as outras', 'A reativação típica da tuberculose ocupa os '
       'segmentos apicais e posteriores, muitas vezes com cavidade; aqui os '
       'ápices estão relativamente preservados, o que pesa contra, sem '
       'afastar. Congestão traria área cardíaca aumentada, linhas septais nas '
       'bases e derrame. Não há derrame nem espessamento pleural.'),
     ]),

    disc('escarro', 'Duas baciloscopias e um teste molecular',
         'Com quatro meses de tosse, emagrecimento, um colega tratado no '
         'alojamento, cigarro e cachaça, a tuberculose pulmonar está na frente '
         'da lista, como estaria em qualquer unidade de Rondônia. Os exames '
         'negativos não a encerram.',
         'A baciloscopia precisa de muitos bacilos por mililitro de escarro, e '
         'perde uma parte grande dos casos. O teste rápido molecular é mais '
         'sensível, mas nos pacientes com baciloscopia negativa deixa passar '
         'cerca de um quarto a um terço dos que a cultura confirma. Pelo manual '
         'do Ministério da Saúde, o caso com clínica e imagem compatíveis segue '
         'investigado com cultura, que leva até oito semanas.',
         'Contra a hipótese, a radiografia sem cavidade e com ápices '
         'preservados, e a rouquidão, que na tuberculose laríngea costuma vir '
         'com escarro cheio de bacilos. A favor, a epidemiologia e a duração. A '
         'equipe colhe escarro induzido para cultura e espera.'),

    estudo('lesoes', 'As lesões do rosto',
           'Fotografia de outro paciente, com lesões do mesmo tipo das de '
           'Valdir, porém mais numerosas. A lesão do lábio dele, as duas da face '
           'e a área da gengiva têm essa mesma superfície.',
           IMG / 'lesoes_periorais.jpg',
           'Fotografia de outro paciente · recortada na região da boca.',
           credito_meta(IMG / 'lesoes_periorais.jpg.json'),
        [
         ((370, 260), (230, 110), '**Fundo granuloso**, salpicado de pontos vermelho-escuros e '
          'amarelados.', 12),
         ((712, 290), (875, 385), '**Centro ulcerado com crosta escura**, cercado por borda '
          'elevada e violácea.', -12),
         ((560, 565), (390, 640), 'Lesão na **junção do lábio com a pele**, com o mesmo fundo.', 12),
        ],
        ['Pápulas e placas infiltradas, de borda elevada e violácea, com centro '
         'ulcerado de fundo granuloso, pontilhado de vermelho-escuro, e crostas.',
         'No caso de Valdir: uma lesão de 1,5 cm no lábio, duas menores na face '
         'e uma área granulosa na gengiva, todas com meses de evolução.']),

    Q('p3', 3,
      'Lesões de lábio, face e gengiva, com meses de evolução, nesse aspecto. '
      'Em que grupo de processos elas se encaixam melhor?', [
      ('Inflamação granulomatosa crônica', True),
      ('Neoplasia epitelial primária', False),
      ('Infecção bacteriana superficial', False),
      ('Doença bolhosa autoimune', False),
      ('Vasculite de pequenos vasos', False),
      ('Dano solar crônico do lábio', False),
     ], [
      ('O padrão', 'Várias lesões em sítios diferentes, infiltradas, de fundo '
       'granuloso com pontos hemorrágicos, que crescem em meses, num homem com '
       'linfonodos cervicais, doença intersticial bilateral e rouquidão. Isso '
       'é um processo inflamatório crônico que se espalha, e a superfície '
       'granulosa é a do tecido de granulação sobre granulomas.'),
      ('O que cabe no grupo', 'No Brasil, úlceras granulomatosas de boca e '
       'face vêm de micobactérias, de leishmânia, de micoses profundas e, mais '
       'raramente, de sífilis tardia ou sarcoidose. Quase todas pedem tecido '
       'para cultura e histologia, além da coloração especial.'),
      ('Por que não as outras', 'O carcinoma do lábio costuma ser lesão única, '
       'endurecida, de borda em rolete, e pode coexistir com um processo '
       'granulomatoso; só a biópsia separa. Infecção bacteriana superficial '
       'dura dias e forma crosta amarelada sem infiltração. Doença bolhosa '
       'começa por bolhas e erosões, e vasculite por púrpura palpável. O dano '
       'solar do lábio dá placa descamativa, sem úlcera granulosa.'),
     ]),

    pg('laringe', 'Terceiro dia',
       'A otorrinolaringologia faz a videolaringoscopia: pregas vocais '
       'espessadas, de superfície granulosa, esbranquiçada e salpicada de '
       'pontos avermelhados, nas duas pregas e na face laríngea da epiglote. '
       'Mobilidade preservada, sem massa vegetante.',
       'O otorrino registra "aspecto inflamatório granulomatoso, não afasta '
       'neoplasia" e programa biópsia da laringe sob anestesia geral. A fila '
       'do centro cirúrgico é de três semanas.'),

    pg('plano', 'O que a equipe registra',
       'Na evolução, o residente escreve: "Doença pulmonar intersticial '
       'bilateral, lesões granulosas de lábio, face, gengiva e laringe, '
       'linfonodos cervicais e emagrecimento de 13% em quatro meses. '
       'Hipóteses: tuberculose pulmonar com baciloscopia negativa, com '
       'acometimento laríngeo e orificial; carcinoma epidermoide de lábio ou '
       'de laringe, com doença pulmonar à parte; leishmaniose mucosa."',
       'A tuberculose explica o pulmão, a laringe, a boca e os linfonodos numa '
       'doença só, e há um contato. O carcinoma explica o lábio endurecido, a '
       'voz, os linfonodos duros e a história do pai, num homem de 40 '
       'maços-ano que bebe todo dia. A leishmaniose mucosa é comum em Rondônia, '
       'mas começa pelo nariz e não faria a radiografia.',
       'Plano: cultura do escarro induzido, biópsia de laringe quando sair a '
       'vaga e consulta com a cirurgia de cabeça e pescoço para o lábio.'),

    disc('tabaco', 'O lábio, a laringe e o cigarro',
         'O carcinoma epidermoide do lábio inferior é o câncer de boca do '
         'trabalhador rural: soma o sol de décadas ao cigarro, sobretudo o de '
         'palha, que se apoia no mesmo ponto do lábio. O da laringe vem do '
         'cigarro, e o álcool multiplica o risco. Num fumante assim, toda a '
         'mucosa das vias aerodigestivas sofreu a mesma agressão, e um segundo '
         'tumor, na laringe ou no pulmão, não é raro.',
         'O que não combina com a âncora: o carcinoma costuma ser lesão única, e '
         'Valdir tem quatro sítios na boca e na face, além da laringe, todos com '
         'a mesma superfície granulosa. Os linfonodos são bilaterais e móveis. '
         'A radiografia não mostra massa, e sim doença difusa.',
         'As duas âncoras exigem a mesma coisa antes de qualquer tratamento: '
         'tecido.'),

    pg('semana', 'Uma semana depois',
       'Valdir volta mais magro, com 60 kg. A cultura do escarro segue '
       'incubando.',
       'O pneumologista de plantão propõe iniciar o esquema básico para '
       'tuberculose: "quadro compatível, contato no alojamento, a cultura '
       'demora e ele está perdendo peso". O cirurgião de cabeça e pescoço vê o '
       'lábio e os linfonodos duros e propõe ressecção em cunha do lábio com '
       'esvaziamento cervical, em quatro semanas.',
       'A lesão do lábio está ao alcance de uma biópsia com anestesia local, no '
       'próprio ambulatório.'),

    bifurcacao('b1', 'Decisão', 'Antes de tratar',
      'Pulmão, laringe, boca, face e linfonodos, com duas âncoras na mesa. '
      'O que você faz agora?', [
      caminho('Biopsiar a lesão do lábio no ambulatório, com fragmento para '
              'histologia e outro para cultura', 'biopsia',
              'O tecido está ao alcance da mão e decide entre as hipóteses em '
              'dias, sem anestesia geral.'),
      caminho('Iniciar o esquema básico para tuberculose e reavaliar em dois '
              'meses', 'rhze',
              'Tratar sem confirmação, com a cultura a caminho e um tecido '
              'acessível, atrasa o diagnóstico se a hipótese estiver errada.'),
      caminho('Encaminhar para ressecção do lábio com esvaziamento cervical',
              'cirurgia_cp',
              'Nenhuma cirurgia oncológica se faz sem diagnóstico histológico.'),
    ]),

    pg('rhze', 'Dois meses de esquema básico',
       'Valdir toma rifampicina, isoniazida, pirazinamida e etambutol por dois '
       'meses. As lesões da boca crescem, a rouquidão piora e ele chega a 57 '
       'kg. A cultura do escarro termina negativa em oito semanas.',
       'Sem resposta, a equipe biopsia a lesão do lábio no ambulatório. A '
       'rifampicina é suspensa, e o efeito dela sobre as enzimas do fígado '
       'ainda dura cerca de duas semanas.',
       segue='biopsia'),

    pg('cirurgia_cp', 'Cinco semanas depois',
       'A consulta da cirurgia de cabeça e pescoço sai em cinco semanas. Nesse '
       'tempo Valdir perde mais 3 kg e passa a engasgar com líquidos. O '
       'cirurgião não opera sem tecido: faz a biópsia do lábio no ambulatório, '
       'no mesmo dia.',
       segue='biopsia'),

    pg('biopsia', 'A biópsia',
       'Biópsia com punch de 4 mm na borda da lesão do lábio e na gengiva, com '
       'anestesia local. Um fragmento vai em formol; o outro, em soro '
       'fisiológico, para cultura.',
       'Três dias depois, o patologista liga. O epitélio tem hiperplasia '
       'pseudoepiteliomatosa, que imita o carcinoma, mas sem atipia que o '
       'configure. Na derme, granulomas epitelioides com células gigantes e '
       'microabscessos de neutrófilos. Dentro das células gigantes há '
       'estruturas arredondadas, de parede espessa. A coloração de Ziehl-Neelsen '
       'é negativa. Ele pede a coloração pela prata.'),

    estudo('lamina', 'Coloração pela prata',
           'Lâmina de outro paciente, com o mesmo achado da biópsia de Valdir, '
           'em aumento maior. A prata (Grocott) cora de preto a parede dos '
           'fungos.',
           IMG / 'lamina_prata.jpg',
           'Lâmina de outro paciente · comparação didática.',
           credito_meta(IMG / 'lamina_prata.jpg.json'),
        [
         ((447, 470), (250, 600), '**Célula-mãe** grande, de parede espessa, com o centro '
          'claro.', 12),
         ((650, 475), (820, 400), '**Broto** pequeno preso à célula-mãe por uma base estreita; '
          'há vários em volta dela.', -12),
         ((321, 175), (150, 80), '**Células menores em cadeia**, também com brotos, de '
          'tamanhos diferentes.', 12),
        ],
        ['Leveduras de tamanho variado, de parede espessa, com vários brotos '
         'ao redor da mesma célula-mãe, como os raios de uma roda de leme.',
         'Brotamento múltiplo é a marca de um fungo só, entre os que causam '
         'doença granulomatosa no Brasil.']),

    pg('virada', 'O diagnóstico',
       'É **paracoccidioidomicose**, na forma crônica multifocal, do adulto: '
       'pulmão, laringe, boca, pele da face e linfonodos cervicais.',
       'O fungo vive no solo de áreas úmidas, e o homem inala os conídios ao '
       'mexer na terra, em geral nas duas primeiras décadas de vida. A '
       'infecção fica latente por anos e reativa como forma crônica entre os 30 '
       'e os 60 anos, em homens, numa proporção de mais de 20 para cada mulher. '
       'Fumar mais de 20 cigarros por dia por mais de 20 anos e beber mais de '
       '50 g de álcool por dia são associações frequentes. Valdir mexe com café '
       'desde os 9 anos, no Paraná, e derrubou mata em Rondônia, que tem hoje '
       'algumas das maiores incidências do país.',
       'O pulmão quase sempre está acometido, com a imagem maior que a '
       'clínica. Na boca, a úlcera de fundo granuloso com pontilhado '
       'hemorrágico é a estomatite moriforme, e a laringe dá a rouquidão. As '
       'âncoras eram razoáveis: tuberculose coexiste em 2 a 20% dos casos, e '
       'carcinoma de boca e laringe também. Um exame direto do escarro com '
       'hidróxido de potássio teria mostrado as leveduras em um dia.'),

    pareamento('p4', 'Pergunta 4',
      'Lesões granulomatosas crônicas de pele e mucosa têm poucas causas no '
      'Brasil, e elas se confundem. Associe cada paciente à causa mais '
      'provável.', [
      par('Úlcera do palato e perfuração do septo nasal, anos após uma ferida '
          'na perna', 'Leishmaniose mucosa',
          'A lesão mucosa aparece anos depois da cutânea e começa pelo nariz.'),
      par('Úlcera única do lábio inferior, de borda endurecida, em lavrador '
          'fumante', 'Carcinoma epidermoide',
          'Lesão única em área de sol e fumo. Pode coexistir com a micose, no '
          'mesmo sítio.'),
      par('Úlcera dolorosa da língua, bacilos no escarro e cavidade no ápice',
          'Tuberculose',
          'A lesão oral costuma acompanhar a doença pulmonar bacilífera.'),
      par('Úlcera oral com aids e CD4 baixo; leveduras pequenas dentro de '
          'macrófagos', 'Histoplasmose disseminada',
          'Leveduras de 2 a 4 µm, intracelulares, sem brotamento múltiplo.'),
      par('Nódulos em fila no antebraço, semanas após arranhão de gato',
          'Esporotricose',
          'Disseminação linfangítica a partir da inoculação na pele.'),
    ], opcoes=['Leishmaniose mucosa', 'Carcinoma epidermoide', 'Tuberculose',
               'Histoplasmose disseminada', 'Esporotricose',
               'Cromoblastomicose', 'Sífilis terciária'],
    titulo_resposta='O tecido com cultura separa o que o olho junta',
    nota='As que sobraram: cromoblastomicose dá placa verrucosa no pé ou na '
         'perna, com corpos castanhos na biópsia; sífilis terciária dá goma que '
         'perfura o palato, com sorologia reagente.'),

    disc('formas', 'Forma e gravidade',
         'O consenso brasileiro separa a forma aguda ou subaguda, do jovem, '
         'com linfonodos, fígado, baço e pouca doença pulmonar, da forma '
         'crônica do adulto, que responde por 74 a 96% dos casos e se instala '
         'em meses, com pulmão, mucosas das vias aerodigestivas e pele. Na '
         'crônica, unifocal ou multifocal, a gravidade orienta o tratamento.',
         'É grave quem tem três ou mais destes: perda de peso acima de 10%; '
         'comprometimento pulmonar intenso; acometimento de adrenais, sistema '
         'nervoso ou ossos; linfonodos em várias cadeias, maiores que 2 cm ou '
         'supurados; títulos de anticorpos elevados. É leve quem perdeu menos '
         'de 5% do peso, com um órgão acometido e sem disfunção.',
         'Valdir perdeu 10 kg de 70, ou 14%: um critério. Tem hipoxemia leve em '
         'repouso, sem insuficiência respiratória, e linfonodos de até 2 cm, sem '
         'supuração. Faltam os títulos e a adrenal, que o consenso manda '
         'avaliar na forma crônica pela frequência com que é atingida.'),

    painel('estadio', 'Avaliação da extensão', 'Duas semanas depois', [
        ex('Exame direto do escarro com hidróxido de potássio', 'Leveduras de parede espessa, com brotos múltiplos', 'ausentes', True),
        ex('Imunodifusão dupla para //Paracoccidioides//', 'Reagente, 1:16', 'não reagente', True),
        ex('Cultura de escarro para micobactérias', 'Sem crescimento em quatro semanas {{(final em oito)}}', '—'),
        ex('Cortisol sérico às 8 h', '7,4 µg/dL', '5–25 µg/dL'),
        ex('ACTH plasmático', '112 pg/mL', 'até 46 pg/mL', True),
        ex('Cortisol 60 min após 250 µg de cosintropina', '11,8 µg/dL', 'pico ≥ 18 µg/dL', True),
        ex('Sódio / potássio', '132 / 5,1 mmol/L', '135–145 / 3,5–5,1', True),
        ex('Espirometria', 'VEF₁/CVF 0,63 · VEF₁ 61% do previsto · sem resposta ao broncodilatador', '—', True),
    ], introducao='Pedidos depois do diagnóstico, antes de começar o antifúngico.'),

    Q('p5', 5,
      'Cortisol às 8 h de 7,4 µg/dL, ACTH de 112 pg/mL, pico de 11,8 µg/dL '
      'após cosintropina, sódio de 132 e potássio de 5,1. Qual a '
      'interpretação?', [
      ('Insuficiência adrenal primária', True),
      ('Insuficiência adrenal central', False),
      ('Eixo normal: cortisol dentro da faixa', False),
      ('Supressão por corticoide exógeno', False),
      ('Efeito do diurético tiazídico', False),
     ], [
      ('A leitura', 'Um cortisol de 7,4 µg/dL cabe na faixa do laboratório, '
       'mas é baixo para um homem doente, e o pico de 11,8 após 250 µg de '
       'cosintropina fica abaixo de 18, o corte clássico; com os ensaios mais '
       'novos o corte cai para 14 a 15, e ele continua abaixo. Com o ACTH alto, '
       'a falha está na própria glândula.'),
      ('O que se soma', 'Sódio baixo e potássio no limite sugerem falta também '
       'de aldosterona, que só a doença da adrenal produz. As dobras palmares '
       'escuras são o ACTH alto estimulando o melanócito, e no rosto queimado '
       'de sol passariam despercebidas.'),
      ('Por que não as outras', 'Na insuficiência central e na supressão por '
       'corticoide, o ACTH está baixo ou normal, sem escurecimento da pele e '
       'sem potássio alto. A tiazida baixa o sódio, mas baixa também o '
       'potássio e não mexe no cortisol.'),
      ('Na micose', 'Granulomas destroem o córtex adrenal. Pelo consenso, 15 a '
       '50% dos pacientes avaliados têm reserva reduzida sem sintomas, e 3,5% '
       'chegam à doença de Addison.'),
     ]),

    disc('adrenal', 'A adrenal de Valdir',
         'Com a reserva reduzida e sinais de falta de aldosterona, a '
         'endocrinologia inicia hidrocortisona 15 mg ao dia, 10 mg ao acordar e '
         '5 mg no início da tarde, dentro da faixa de 15 a 25 mg da diretriz da '
         'Endocrine Society de 2016, e fludrocortisona 0,05 mg, guiada por '
         'sódio, potássio e pressão. A hidroclorotiazida é suspensa: piora o '
         'sódio, e a pressão está em 112/70.',
         'Ele leva para casa a regra da doença intercorrente: dobrar ou '
         'triplicar a dose com febre, e hidrocortisona injetável se vomitar. '
         'Recebe um cartão que diz que usa corticoide e não pode ficar sem.',
         'A função adrenal às vezes melhora com o tratamento da micose, mas na '
         'maioria a reposição continua. O cetoconazol, usado no passado contra '
         'esse fungo, bloqueia a síntese de cortisol e fica fora de cogitação.'),

    bifurcacao('b2', 'Decisão', 'O antifúngico',
      'Forma crônica multifocal, com dois critérios de gravidade, perda de peso '
      'e adrenal, sem instabilidade, com a reposição já iniciada. Como '
      'tratar?', [
      caminho('Itraconazol 200 mg por via oral, em casa, por 9 a 18 meses, '
              'guiado pelos critérios de cura', 'tratamento',
              'É o tratamento de escolha do consenso para as formas leves e '
              'moderadas.'),
      caminho('Internar para anfotericina B desoxicolato por quatro semanas',
              'anfo',
              'Anfotericina é para as formas graves e instáveis, e cobra rim e '
              'potássio.'),
    ]),

    pg('anfo', 'Duas semanas de internação',
       'Anfotericina B desoxicolato 0,6 mg/kg ao dia. Na segunda semana, a '
       'creatinina sobe de 0,9 para 1,9 mg/dL e o potássio cai para 2,9 mmol/L, '
       'com reposição endovenosa diária e uma flebite no braço. No 14.º dia a '
       'equipe suspende a anfotericina e passa para itraconazol.',
       segue='tratamento'),

    pg('tratamento', 'Primeira consulta de tratamento',
       'A farmácia do hospital dispensa o itraconazol 200 mg ao dia, sem custo '
       'para ele. Valdir mora a 40 minutos do hospital e mantém o omeprazol '
       'que comprou na farmácia. '
       'Pergunta se pode parar quando a boca sarar.',
       'A cultura de escarro para micobactérias ainda corre, e a equipe '
       'conversa com ele sobre o cigarro e a cachaça.'),

    Q('p6', 6,
      'Na orientação do itraconazol para Valdir, **quais quatro** afirmações '
      'estão corretas?', [
      ('Cápsula inteira, uma vez ao dia, após refeição', True),
      ('Suspender o omeprazol durante o tratamento', True),
      ('Não associar rifampicina ao itraconazol', True),
      ('Sorologia e radiografia a cada seis meses', True),
      ('Dividir a dose em duas tomadas, em jejum', False),
      ('Suspender quando as lesões cicatrizarem', False),
      ('Nova biópsia para comprovar a cura', False),
     ], [
      ('A absorção', 'O itraconazol em cápsula precisa de ácido no estômago e '
       'de comida. O consenso recomenda a cápsula inteira, numa tomada só, '
       'depois do almoço ou do jantar; suco cítrico ajuda, e antiácido, '
       'bloqueador H2, omeprazol e alimentos alcalinos atrapalham. Dividir a '
       'dose piora a absorção.'),
      ('As interações', 'Rifampicina, fenitoína e barbitúricos derrubam o nível '
       'do itraconazol. Se a cultura confirmar tuberculose ao lado da micose, o '
       'esquema troca o itraconazol por sulfametoxazol-trimetoprima, que pode '
       'correr com a rifampicina.'),
      ('O seguimento', 'Consultas mensais nos três primeiros meses e depois '
       'trimestrais; sorologia e radiografia a cada seis meses. As lesões de '
       'pele e boca cicatrizam em cerca de 30 dias, e os linfonodos em dois a '
       'três meses, mas o tratamento dura de 9 a 18 meses, em média 12, e '
       'termina pelos critérios clínicos, radiológicos e sorológicos de cura. '
       'Não é preciso repetir biópsia.'),
     ]),

    pg('seguimento', 'Do primeiro ao sexto mês',
       'Em 30 dias as lesões do lábio, da face e da gengiva cicatrizam. Os '
       'linfonodos regridem no terceiro mês, e a voz melhora, sem voltar a ser '
       'a de antes. A cultura de escarro termina negativa em oito semanas.',
       'Com adesivo de nicotina e o grupo de cessação da unidade básica, ele '
       'para de fumar no segundo mês e reduz a cachaça para o fim de semana. '
       'No sexto mês pesa 68 kg, a imunodifusão caiu para 1:4 e as '
       'opacidades da radiografia estão menores e mais lineares.',
       'Ele voltou ao cafezal e pergunta, de novo, se pode parar o remédio.'),

    bifurcacao('b3', 'Decisão', 'Quando parar',
      'Sexto mês: lesões cicatrizadas, peso quase recuperado, imunodifusão em '
      '1:4. O que você responde?', [
      caminho('Manter até cumprir os critérios clínicos, radiológicos e '
              'sorológicos de cura', 'cura',
              'Cicatrizar a boca é o primeiro critério, não o último.'),
      caminho('Suspender agora, porque as lesões cicatrizaram e o peso voltou',
              'recaida',
              'Seis meses ficam abaixo do tempo mínimo, com a sorologia ainda '
              'positiva e a radiografia ainda mudando.'),
    ]),

    pg('recaida', 'Onze meses depois',
       'Cinco meses depois de suspenso o itraconazol, a rouquidão volta, '
       'depois a falta de ar e uma nova área granulosa na gengiva. Valdir '
       'perde 6 kg e a imunodifusão sobe para 1:64. O itraconazol é retomado.',
       'A laringe cicatriza com fibrose e estreita: ele passa a ter estridor ao '
       'esforço e precisa de traqueostomia enquanto a otorrino planeja a '
       'correção. A espirometria mostra VEF₁ de 44% do previsto.',
       segue='f_pior'),

    pg('cura', 'Do 12.º ao 18.º mês',
       'A imunodifusão é de 1:2 no 12.º mês e não reagente no 18.º. As '
       'radiografias do 12.º e do 18.º mês são iguais, com linhas finas '
       'residuais. O peso estabiliza em 70 kg, sem lesão nova.',
       'Com os critérios clínico, radiológico e sorológico cumpridos, o '
       'itraconazol é suspenso no 18.º mês. Como a falta de ar aos esforços '
       'continua, a equipe pede tomografia de tórax para separar sequela de '
       'atividade.'),

    estudo('tc_seq', 'Tomografia de tórax no fim do tratamento',
           'Corte axial nos lobos superiores, em janela de pulmão. A pergunta é '
           'se há sinal de atividade, como nódulos, cavidades ou vidro fosco, '
           'ou só cicatriz.',
           IMG / 'tc_controle.jpg',
           'Tomografia de outro paciente · comparação didática.',
           credito_meta(IMG / 'tc_controle.jpg.json'),
        [
         ((246, 399), (110, 610), 'Parênquima salpicado de **pequenas áreas escuras, sem '
          'parede**, em todo o lobo: enfisema centrolobular.', 12),
         ((313, 268), (150, 150), '**Ponto branco**: ramo da artéria pulmonar cortado de través.', -12),
         ((786, 469), (900, 300), '**Pulmão esquerdo** com o mesmo padrão difuso, sem nódulo nem '
          'consolidação.', 12),
        ],
        ['Enfisema centrolobular difuso nos lobos superiores. Sem nódulos, '
         'cavidades, consolidação ou vidro fosco neste corte.',
         'No tratado, a tomografia mostra enfisema e distorção cicatricial em '
         'mais de 80% dos casos, somando a micose ao cigarro. A espirometria '
         'obstrutiva justifica broncodilatador como na doença pulmonar '
         'obstrutiva crônica.']),

    pg('alta', 'Seguimento depois do tratamento',
       'Valdir passa a consultas semestrais por dois anos, com sorologia e '
       'radiografia, e segue com broncodilatador inalatório e a '
       'hidrocortisona, porque a reserva adrenal reavaliada no fim continua '
       'baixa.',
       conforme=('b1', ['alta2', 'f2', 'f2'])),

    pg('alta2', 'Dois anos depois',
       'Sem fumar, ele sobe o morro do cafezal parando uma vez. A voz ficou '
       'um pouco mais grave.',
       conforme=('b2', ['f1', 'f2'])),

    fim('f1', 'Cura clínica com sequela pequena',
        'Sem recaída dois anos depois de suspenso o itraconazol, com '
        'sorologia não reagente, sem cigarro, com a adrenal compensada pela '
        'reposição e uma obstrução moderada que o broncodilatador controla.',
        'A biópsia antes de qualquer tratamento, o antifúngico oral certo para '
        'a gravidade e o tratamento até os critérios de cura foram as três '
        'decisões que contaram.', 'melhor'),

    fim('f2', 'Cura depois de um percurso mais longo',
        'Valdir chega aos critérios de cura, mas com mais semanas de doença '
        'ativa antes do diagnóstico ou com uma lesão renal que custou duas '
        'semanas de internação, e com mais fibrose e mais falta de ar do que '
        'teria.',
        'Tratar tuberculose sem tecido, esperar uma cirurgia sem diagnóstico '
        'ou usar anfotericina numa forma moderada acrescentou dano sem '
        'acrescentar cura.', 'medio'),

    fim('f_pior', 'Recaída com sequela de laringe',
        'Ele completa um segundo curso de itraconazol, mais longo, mas fica com '
        'traqueostomia por meses, voz muito alterada e obstrução grave ao '
        'esforço.',
        'Cicatrizar a boca em 30 dias não é cura. Suspender aos seis meses, com '
        'a sorologia positiva e a radiografia mudando, deixou o fungo voltar, e '
        'cada atividade nova soma fibrose.', 'pior'),

    pagina('retrospectiva', 'Pontos de ensino', '',
        pontos(
            'Num lavrador de área endêmica com tosse longa, emagrecimento, '
            'rouquidão e lesão de boca, a micose entra na lista ao lado da '
            'tuberculose e do carcinoma, e o exame direto do escarro com '
            'hidróxido de potássio custa um dia.',
            'Radiografia com doença intersticial bilateral, peri-hilar, maior '
            'que a clínica, é a dissociação clínico-radiológica das doenças '
            'granulomatosas crônicas.',
            'Baciloscopia e teste molecular negativos não afastam tuberculose, '
            'e a coinfecção acontece em 2 a 20% dos casos; a cultura segue até o '
            'fim.',
            'Lesão acessível se biopsia antes de tratar, e o fragmento vai '
            'também para cultura. A hiperplasia pseudoepiteliomatosa imita '
            'carcinoma na biópsia superficial.',
            'Na forma crônica, avaliar a adrenal sempre: reserva reduzida é '
            'frequente e silenciosa, e a reposição costuma ser definitiva.',
            'Itraconazol 200 mg ao dia, cápsula inteira após refeição, sem '
            'omeprazol nem rifampicina, por 9 a 18 meses, até os critérios '
            'clínico, radiológico e sorológico de cura. Anfotericina fica para '
            'as formas graves.',
            'Parar de fumar faz parte do tratamento: o cigarro soma enfisema à '
            'fibrose e aumenta o risco de carcinoma no mesmo sítio da micose.'),
        so_kicker=True),

    pg('referencias', 'Fontes e limites',
       'Paciente, valores e percursos são ficcionais.',
       'Shikanai-Yasuda e cols. II Consenso Brasileiro em Paracoccidioidomicose '
       '2017, Epidemiol Serv Saúde 2018;27(núm. esp.):e0500001 (versão em '
       'inglês: Brazilian guidelines for the clinical management of '
       'paracoccidioidomycosis, Rev Soc Bras Med Trop 2017;50:715–40): formas '
       'clínicas, critérios de gravidade, doses, interações, seguimento, '
       'critérios de cura, adrenal e sequelas. Bornstein e cols. Diagnosis and '
       'Treatment of Primary Adrenal Insufficiency, Endocrine Society, J Clin '
       'Endocrinol Metab 2016. Ministério da Saúde. Manual de Recomendações '
       'para o Controle da Tuberculose no Brasil, 2.ª ed., 2019. Inker e cols. '
       'CKD-EPI 2021, N Engl J Med 2021.',
       'Imagens, todas de outros pacientes, com setas adicionadas. Capa: José '
       'Palahv Gavião, CC BY-SA 4.0, commons.wikimedia.org/wiki/'
       'File:Plantação_de_café_(1)_01.jpg. Radiografia: CDC/M. Renz, domínio '
       'público, commons.wikimedia.org/wiki/'
       'File:Chest_X-ray_acute_pulmonary_histoplasmosis_PHIL_3954.jpg (usada '
       'pelo padrão intersticial). Lesões da face: CDC/Dr. Martins Castro e Dr. '
       'Lucille K. Georg, domínio público, recortada na região da boca, '
       'commons.wikimedia.org/wiki/File:Paracoccidioidomycosis_lesions.png. '
       'Prata: CDC/Dr. Lucille K. Georg, domínio público, '
       'commons.wikimedia.org/wiki/File:Paracoccidioides_brasiliensis_01.jpg. '
       'Tomografia: Hellerhoff, CC BY-SA 4.0, commons.wikimedia.org/wiki/'
       'File:Zentrilobulaeres_Lungenemphysem_61W_-_CT_axial_-_001.jpg.'),
]

REVISAO = []

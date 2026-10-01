"""Púrpura retiforme, neutropenia febril, ANCA de dois alvos e glomerulonefrite.

Reescrito no molde do //New England// lido em 26/09/2026 (ver
Artifacts/nejm-casos-classicos/GRAMATICA_LIDA_2026-09-26.md), no desenho do
piloto aprovado (casos/leptospirose): apresentação curta, ficha do paciente,
exame por sistema com os sinais vitais primeiro e primeiros exames entregues
prontos. Seis perguntas, nunca duas telas interativas seguidas: as duas
primeiras classificam (padrão da lesão de pele, mecanismo da neutropenia)
sem nomear doença; a leitura da coagulação, da biópsia renal e do
tratamento são páginas de discussão. A âncora é a registrada pela equipe e correta naquele
momento: agranulocitose por dipirona com lesão necrótica de provável causa
infecciosa num neutropênico febril. No terceiro dia, a orelha, a urina e o
ANCA viram o caso; a exposição aparece na entrevista a sós e o nome da causa
só na página "O diagnóstico". Cada pergunta tem uma explicação só, em seções.

Paciente ficcional; desfechos são cenários didáticos. Neutropenia febril:
IDSA 2010 e ASCO/IDSA 2018. Vasculite ANCA: KDIGO 2024.
"""
from pathlib import Path

from motor.estudo_imagem import ecg, estudo
from motor.etapas import (alt, bifurcacao, caminho, capa, desfecho, op, p,
                          pagina, painel, par, pareamento, pergunta, pontos,
                          topicos, vitais)

TITULO = 'À flor da pele'
RODAPE = 'Paciente ficcional · evoluções simuladas para ensino'
COR = '#7c3aed'
IMG = Path(__file__).parent / 'img'
BANCO = []
MOLDE = 'nejm'
CENA = 'cena.png'


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
    capa(TITULO, fundo=CENA, kicker='Caso interativo',
         selo='Paciente ficcional · procedência e créditos na última tela'),

    pg('historia', 'Apresentação',
       'Marina, 34 anos, vendedora numa loja de roupas, chega ao pronto-socorro '
       'com a irmã por manchas dolorosas nas coxas há três dias e febre desde '
       'ontem, com calafrios. Começaram como duas áreas avermelhadas na face '
       'externa das coxas, que ela atribuiu ao atrito da calça; outras '
       'surgiram ao lado, escureceram, e hoje doem em repouso.',
       'Há dor nos punhos e tornozelos, sem inchaço. Tomou paracetamol. Não '
       'usou antibiótico nem pomada.',
       'Nega queda, picada, exercício intenso, falta de ar, tosse, dor '
       'abdominal, diarreia, ardor ao urinar, sangramento de gengiva e aumento '
       'do fluxo menstrual.'),

    pagina('ficha', 'Ficha do paciente', '',
           topicos(('Antecedentes', 'Apendicectomia aos 16 anos. Uma gestação a '
                    'termo. Rinite desde o ano passado, com crostas e sangramento '
                    'discreto pelo nariz. Há quatro meses teve manchas pequenas '
                    'nas pernas, que sumiram em duas semanas sem consulta.'),
                   ('Medicações', 'Dipirona 1 g quando tem cólica ou dor de '
                    'cabeça, a última há cinco dias. Soro fisiológico nasal. Sem '
                    'anticoncepcional hormonal, fórmulas para emagrecer ou chás.'),
                   ('Hábitos', 'Fuma cinco cigarros por dia. Bebe nos fins de '
                    'semana. Nega drogas ilícitas; a entrevista é feita com a '
                    'irmã no quarto.'),
                   ('Vida social', 'Mora com a filha de 9 anos. Sai com amigas '
                    'aos sábados. Sem viagem nos últimos meses, sem animais em '
                    'casa.'),
                   ('Família', 'Mãe com hipotireoidismo. Pai hipertenso. Sem '
                    'trombose, doença autoimune ou renal na família.')),
           so_kicker=True),

    pagina('exame', 'Exame físico', '',
           vitais(('Temperatura', '38,6 °C', True),
                  ('Pressão arterial', '108/68', False),
                  ('Frequência cardíaca', '112', True),
                  ('Frequência respiratória', '18', False),
                  ('SpO₂ em ar ambiente', '98%', False)),
           topicos(('Estado geral', 'Lúcida, orientada, com dor ao movimentar as '
                    'pernas.'),
                   ('Cabeça e pescoço', 'Orofaringe sem aftas nem placas. Mucosa '
                    'nasal com crostas, septo íntegro. Sem linfonodos palpáveis.'),
                   ('Coração e pulmões', 'Ritmo regular, sem sopro. Murmúrio '
                    'vesicular sem ruídos adventícios.'),
                   ('Abdome', 'Indolor. Fígado e baço não palpáveis.'),
                   ('Pele', 'Nas faces laterais das coxas, cinco placas violáceas '
                    'de 2 a 6 cm, dolorosas, que não clareiam à digitopressão, com '
                    'bordas anguladas e ramificadas; duas têm centro enegrecido. '
                    'Sem bolhas nem crepitação. Pulsos distais presentes.'),
                   ('Articulações', 'Dor à mobilização dos punhos, sem sinovite.')),
           so_kicker=True),

    estudo('pele', 'Fotografia de pele',
           'A equipe fotografa as placas para acompanhar a evolução. Esta '
           'fotografia é de outro paciente, com o mesmo tipo de lesão, de outra '
           'causa e em outra região do corpo; a régua está em centímetros.',
           IMG / 'pele_placa.jpg',
           'Fotografia de outro paciente, com lesão do mesmo tipo · régua em centímetros.',
           'Niels Olson · Wikimedia Commons · CC BY-SA 3.0 · setas adicionadas',
        [
         ((336, 71), (215, 175), '**Desenho em rede** na periferia: traços violáceos finos e ramificados, que seguem a malha de vasos da derme.', 12),
         ((684, 345), (560, 560), '**Centro enegrecido**: a pele que dependia do vaso ocluído necrosou.', -12),
         ((714, 441), (860, 560), '**Borda angulada**, que termina em ponta, sem o contorno arredondado da púrpura comum.', 12),
        ],
        ['Placa violácea de cerca de 4 cm, de borda angulada e '
         'ramificada, com centro enegrecido e traços em rede na periferia.',
         'É o desenho descrito nas coxas de Marina: placas violáceas de 2 a '
         '6 cm, dolorosas, que não clareiam, com bordas anguladas e '
         'ramificadas, duas com centro enegrecido.']),

    Q('q1', 1,
      'Pela descrição do exame e pela fotografia, qual o padrão das lesões '
      'de Marina?', [
      ('Petéquias', False),
      ('Púrpura palpável arredondada', False),
      ('Púrpura retiforme', True),
      ('Equimoses', False),
      ('Livedo reticular', False),
      ('Eritema nodoso', False),
     ], [
      ('O padrão', 'Placas purpúricas que não clareiam, de borda angulada e '
       'ramificada, dolorosas e com centro necrótico são púrpura retiforme, '
       'como na fotografia. O desenho reproduz a rede de vasos da derme '
       'profunda e do subcutâneo: o sangue sai porque o vaso foi ocluído, e a '
       'pele que dependia dele necrosa.'),
      ('Por que não as outras', 'Petéquias são pontos planos de até 2 mm. A '
       'púrpura palpável da vasculite de pequeno vaso superficial forma lesões '
       'pequenas e arredondadas, sem rede. Equimose é mancha plana '
       'de contorno liso. Livedo reticular é rede violácea que clareia e não '
       'necrosa. Eritema nodoso forma nódulos dolorosos nas pernas, sem púrpura.'),
      ('O que esse padrão pede', 'Púrpura retiforme é oclusão até prova em '
       'contrário: trombo, êmbolo, microrganismo que invade o vaso, crioproteína '
       'ou vasculite que fecha a luz. Com febre, a causa infecciosa é a que não '
       'pode esperar.'),
     ]),

    painel('res1', 'Primeiros exames', 'Sangue', [
        ex('Hemoglobina / hematócrito', '12,1 g/dL / 36%', 'Hb 12–16 g/dL'),
        ex('Volume corpuscular médio', '88 fL', '80–100 fL'),
        ex('Leucócitos', '900/mm³ · neutrófilos 20% · linfócitos 70% · monócitos 10%',
           '4.000–11.000/mm³', True),
        ex('Plaquetas', '238.000/mm³', '150.000–450.000/mm³'),
        ex('Esfregaço de sangue periférico', 'Sem blastos, sem esquizócitos'),
        ex('INR / TTPa', '1,0 / 29 s', 'INR até 1,2 · TTPa 25–35 s'),
        ex('Fibrinogênio', '410 mg/dL', '200–400 mg/dL', True),
        ex('Ureia / creatinina', '28 / 0,9 mg/dL', 'até 42 / 1,1 mg/dL'),
        ex('Proteína C reativa / lactato', '96 mg/L / 1,7 mmol/L', 'PCR < 5 · lactato até 2,0', True),
    ], introducao='Dois pares de hemoculturas foram colhidos antes de qualquer '
                  'antibiótico.'),

    painel('res1b', 'Primeiros exames', 'Urina e bioquímica', [
        ex('Urina', 'Densidade 1.020 · sangue negativo · proteína negativa · 0 a 2 hemácias por campo · sem cilindros'),
        ex('Sódio / potássio', '137 / 4,1 mmol/L', 'Na 135–145 · K 3,5–5,0'),
        ex('AST / ALT', '31 / 26 U/L', 'até 40 / 41 U/L'),
        ex('Bilirrubina total', '0,6 mg/dL', 'até 1,2 mg/dL'),
        ex('Beta-hCG sérico', 'Negativo'),
    ]),

    estudo('rx_adm', 'Radiografia de tórax',
           'Radiografia feita na chegada, à procura de um foco para a febre '
           'numa paciente com poucos neutrófilos.',
           IMG / 'rx_torax_normal.jpg',
           'Radiografia de outro adulto · comparação didática.',
           'Mikael Häggström · Wikimedia Commons · CC0 · setas adicionadas',
        [
         ((250, 560), (90, 440), '**Pulmão direito** transparente, sem consolidação.', 12),
         ((110, 975), (250, 1080), '**Seio costofrênico** direito livre: sem derrame.', -12),
         ((745, 800), (900, 700), '**Contorno cardíaco** esquerdo nítido, de tamanho normal.', 12),
        ],
        ['Sem opacidade focal, sem derrame, área cardíaca normal.',
         'No neutropênico a radiografia pode vir limpa mesmo com pneumonia, '
         'porque falta a célula que forma o infiltrado. Sem tosse e com '
         'saturação normal, o pulmão não é o foco provável.']),

    *ecg('ecg_evolucao',
         'Uma hora depois do antitérmico, a frequência cardíaca continua acima '
         'de 110 e a equipe registra um eletrocardiograma. Qual é o ritmo?', IMG,
         'Febre e dor explicam o ritmo; o traçado não aponta outra causa para a '
         'taquicardia.'),

    Q('q2', 2,
      'Qual o mecanismo mais provável da queda dos neutrófilos?', [
      ('Reação idiossincrática a fármaco', True),
      ('Infiltração da medula óssea', False),
      ('Sequestro esplênico', False),
      ('Carência nutricional da medula', False),
      ('Neutropenia constitucional', False),
      ('Consumo periférico pela infecção', False),
     ], [
      ('A contagem', 'Neutrófilos absolutos são leucócitos vezes a fração de '
       'neutrófilos: 900 × 0,20 = 180/mm³. Abaixo de 500 a neutropenia é '
       'grave, e febre com essa contagem é neutropenia febril, uma emergência.'),
      ('O mecanismo', 'Queda de uma linhagem só, abrupta, numa adulta '
       'hígida, com hemoglobina, plaquetas, VCM e esfregaço normais, é o '
       'retrato da agranulocitose idiossincrática: uma exposição recente '
       'lesa os precursores ou os neutrófilos maduros. O passo seguinte é '
       'listar tudo o que ela tomou ou usou nas semanas anteriores e suspender '
       'o que for suspeito.'),
      ('Por que não as outras', 'Infiltração medular derruba mais de uma '
       'linhagem e costuma mostrar blastos. O baço não é palpável. A carência '
       'nutricional aumenta o VCM e atinge as três séries. A neutropenia constitucional '
       'raramente cai abaixo de 1.000 e não surge aos 34 anos com febre. '
       'Consumo pela infecção acontece na sepse grave, com choque, e '
       'raramente isola 180 neutrófilos com lactato normal.'),
     ]),

    pagina('coag', 'Discussão', 'O que a coagulação diz',
      p('Diante de púrpura que oclui vasos, a equipe relê o sangue da chegada '
        'à procura de consumo. Plaquetas de 238.000/mm³, INR de 1,0, TTPa de '
        '29 s e fibrinogênio de 410 mg/dL: não há gasto de plaquetas nem de '
        'fatores, e a oclusão não vem de coagulação intravascular '
        'disseminada.'),
      p('O esfregaço sem esquizócitos, com plaquetas normais, afasta a '
        'hemólise mecânica das microangiopatias trombóticas. O fibrinogênio '
        'pouco acima do limite acompanha a PCR de 96 mg/L: é inflamação, não '
        'consumo.'),
      p('Sobram as oclusões que não gastam fatores: microrganismo que invade '
        'a parede, anticorpo que trombosa, crioproteína que precipita e '
        'inflamação da própria parede. No neutropênico febril, a primeira a '
        'excluir é a infecção que invade o vaso, e isso pede tecido: biópsia '
        'profunda da borda de uma placa, com colorações e cultura para '
        'bactérias e fungos, sem atrasar o antibiótico.')),

    bifurcacao('b1', 'Decisão', 'As primeiras horas',
      'Febril, com 180 neutrófilos e placas necróticas nas coxas. As '
      'hemoculturas já foram colhidas. Como você conduz?', [
      caminho('Cefepima em até uma hora, vancomicina e biópsia da pele',
              'protecao',
              'Neutropenia febril pede betalactâmico antipseudomonas na primeira '
              'hora; infecção de pele e partes moles é critério para somar '
              'vancomicina.', rotulo_curto='Tratar agora'),
      caminho('Biópsia e culturas primeiro; antibiótico conforme o resultado',
              'espera',
              'Cultura de tecido leva dias, e a mortalidade da neutropenia '
              'febril sobe a cada hora sem antibiótico.', rotulo_curto='Esperar'),
      caminho('Filgrastim e observação, sem antibiótico por ora', 'gcsf',
              'O fator estimulador pode encurtar a agranulocitose, mas não '
              'trata a infecção que já pode estar presente.',
              rotulo_curto='Só filgrastim'),
    ]),

    pg('espera', 'Doze horas depois',
       'Ainda sem antibiótico, Marina tem novo calafrio. A pressão cai para '
       '86/50 mmHg e o lactato sobe para 3,4 mmol/L. A plantonista faz '
       'cristaloide e inicia cefepima e vancomicina com doze horas de atraso.',
       segue='internacao'),

    pg('gcsf', 'Oito horas depois',
       'Depois do filgrastim, a febre chega a 39,5 °C e a pressão cai para '
       '88/52 mmHg. A equipe da noite inicia cefepima e vancomicina com oito '
       'horas de atraso, com expansão volêmica.',
       segue='internacao'),

    pg('protecao', 'Primeira hora',
       'Cefepima 2 g endovenosa de 8 em 8 horas começa 40 minutos depois da '
       'triagem, com vancomicina por peso e nível sérico. A dipirona é '
       'suspensa e anotada no prontuário como suspeita de reação.',
       'A dermatologia retira um fragmento profundo da borda de uma placa para '
       'histologia e cultura de bactérias e fungos.'),

    pg('internacao', 'Na enfermaria',
       'Marina é internada em quarto individual, com hemograma diário. A '
       'hipótese registrada é agranulocitose por dipirona com lesões necróticas '
       'de provável causa infecciosa.'),

    pg('dia3', 'Terceiro dia',
       'A febre cedeu no segundo dia. Os neutrófilos estão em 240/mm³ e as '
       'hemoculturas seguem sem crescimento em 48 horas. A biópsia mostra '
       'trombos de fibrina nos pequenos vasos da derme, necrose da epiderme e '
       'leucocitoclasia focal; as colorações para bactérias e fungos não '
       'mostram microrganismos, e a cultura do tecido não cresceu.',
       'No reexame da manhã há uma placa purpúrica nova, pequena e dolorosa, '
       'na hélice da orelha esquerda. Marina conta que a urina ficou cor de '
       'chá desde a noite anterior.'),

    painel('res2', 'Terceiro dia', 'Rim e urina', [
        ex('Ureia / creatinina', '52 / 1,6 mg/dL {{(0,9 na admissão)}}', 'até 42 / 1,1 mg/dL', True),
        ex('Urina', 'Sangue +++ · proteína ++', '—', True),
        ex('Sedimento urinário', '50 hemácias por campo, 60% dismórficas, com acantócitos · cilindros hemáticos', '—', True),
        ex('Leucócitos na urina', '4 por campo · sem cilindros leucocitários', 'até 5 por campo'),
        ex('Proteína / creatinina urinária', '1,1 g/g', '< 0,2 g/g', True),
        ex('Fração de excreção de sódio', '0,8%'),
        ex('Vancomicina, nível de vale', '12 mg/L', '10–20 mg/L'),
        ex('Creatinoquinase', '96 U/L', 'até 170 U/L'),
        ex('Neutrófilos absolutos', '240/mm³', '1.500–7.500/mm³', True),
    ]),

    estudo('us_evolucao', 'Ultrassonografia renal',
        'Com a creatinina em alta e a urina escura, a equipe pede '
        'ultrassonografia dos rins para afastar obstrução e medir o tamanho '
        'deles.',
        IMG / 'us_rim.jpg',
        'Rim de outro adulto. Asteriscos da fonte: um, coluna de Bertin; '
        'dois, pirâmide; três, córtex; quatro, seio renal. Os cálipers também '
        'são da fonte.',
        'Hansen, Nielsen e Ewertsen · Wikimedia Commons · CC BY 4.0 · setas adicionadas',
        [
         ((495, 288), (620, 105), '**Córtex** renal (três asteriscos), de espessura preservada.', 12),
         ((447, 400), (720, 550), '**Seio renal** (quatro asteriscos), ecogênico, sem dilatação do sistema coletor.', -12),
         ((472, 357), (330, 160), '**Pirâmide medular** (dois asteriscos), hipoecoica: a diferenciação entre córtex e medula está preservada.', 12),
        ],
        ['Rins de 11 cm, com córtex preservado e sem hidronefrose.',
         'Sem obstrução e sem rim pequeno de doença antiga: a lesão é aguda e '
         'está dentro do rim.']),

    Q('q4', 3,
      'Qual a interpretação mais adequada da lesão renal?', [
      ('Glomerulonefrite aguda', True),
      ('Necrose tubular pela vancomicina', False),
      ('Nefrite intersticial pelo betalactâmico', False),
      ('Pré-renal pela febre', False),
      ('Pigmentúria por rabdomiólise', False),
      ('Obstrução urinária', False),
     ], [
      ('O sedimento', 'Hemácias dismórficas, acantócitos e cilindros hemáticos '
       'só se formam quando a hemácia atravessa o glomérulo lesado. Com '
       'proteinúria de 1,1 g/g e creatinina que quase dobrou em dois dias, é '
       'glomerulonefrite aguda, de curso rapidamente progressivo se não '
       'tratada.'),
      ('Por que não as outras', 'A vancomicina está com vale de 12 mg/L, e a '
       'lesão tubular dá cilindros granulosos e FENa alta, não 0,8%. A nefrite '
       'intersticial por betalactâmico traz leucocitúria e cilindros '
       'leucocitários. Pré-renal não tem hemácias dismórficas. A CK de 96 '
       'afasta rabdomiólise, e o ultrassom, obstrução.'),
      ('O que muda', 'Púrpura retiforme, lesão nova na orelha e '
       'glomerulonefrite na mesma semana formam uma doença sistêmica de vasos '
       'pequenos. A dipirona explica a neutropenia, mas não o rim nem a '
       'orelha: a equipe pede anticorpos e complemento.'),
     ]),

    painel('res3', 'Terceiro dia', 'Anticorpos e complemento', [
        ex('ANCA por imunofluorescência', 'Padrão perinuclear (p-ANCA), título 1:1.280', 'Não reagente', True),
        ex('Anti-MPO', '128 U/mL', '< 20 U/mL', True),
        ex('Anti-PR3', '46 U/mL', '< 20 U/mL', True),
        ex('Anti-membrana basal glomerular', 'Não reagente', 'Não reagente'),
        ex('C3 / C4', '104 / 22 mg/dL', 'C3 90–180 · C4 10–40'),
        ex('Crioglobulinas (colheita a 37 °C)', 'Não detectadas', 'Não detectadas'),
        ex('Anticardiolipina e anti-β2-glicoproteína I', 'Não reagentes', 'Não reagentes'),
        ex('Anticoagulante lúpico', 'Não detectado', 'Não detectado'),
        ex('HIV, HBsAg e anti-HCV', 'Não reagentes', 'Não reagentes'),
    ]),

    Q('q5', 4,
      'Qual a interpretação mais provável desse perfil de anticorpos?', [
      ('Poliangeíte microscópica', False),
      ('Granulomatose com poliangeíte', False),
      ('Vasculite ANCA induzida por substância', True),
      ('Endocardite com ANCA positivo', False),
      ('Lúpus com vasculite', False),
      ('Crioglobulinemia mista', False),
     ], [
      ('Dois alvos', 'Na vasculite primária, o ANCA tem um alvo: MPO na '
       'poliangeíte microscópica, PR3 na granulomatose com poliangeíte. MPO e '
       'PR3 juntos, com título alto, aparecem em poucos por cento das formas '
       'primárias e são a marca das vasculites induzidas por exposição: '
       'propiltiouracila, hidralazina, minociclina e algumas substâncias de uso '
       'recreativo.'),
      ('Por que não as outras', 'Endocardite pode positivar o ANCA, mas as '
       'hemoculturas colhidas antes do antibiótico estão negativas e não há '
       'sopro. Lúpus consome complemento, e C3 e C4 estão normais. '
       'Crioglobulinemia exige a crioproteína, não detectada em amostra '
       'colhida a 37 °C, e costuma baixar o C4.'),
      ('O que isso pede', 'A dipirona não está entre as drogas que induzem '
       'ANCA. É hora de refazer a história de exposição a sós, perguntando '
       'também pelo que a paciente não chama de remédio.'),
     ]),

    pg('entrevista', 'Entrevista a sós',
       'A médica volta ao quarto no fim da tarde, quando a irmã saiu. Explica '
       'que o que for dito fica no prontuário e na equipe, e que a pergunta '
       'muda o tratamento.',
       'Marina conta que usa cocaína aspirada aos sábados há cerca de oito '
       'meses, a última vez dois dias antes de vir ao hospital, e que as '
       'manchas de quatro meses atrás vieram depois de um fim de semana de uso '
       'maior. Não sabe o que há no pó. Nunca injetou. A rinite com crostas '
       'começou na mesma época.'),

    pg('diagnostico', 'O diagnóstico',
       'Púrpura retiforme com predileção pela orelha, agranulocitose, ANCA com '
       'dois alvos e glomerulonefrite pauci-imune numa usuária de cocaína '
       'formam a síndrome associada ao levamisol, o adulterante mais comum da '
       'cocaína. No Brasil ele apareceu em mais da metade das amostras '
       'apreendidas pela Polícia Federal para tráfico internacional e das '
       'amostras de fluido oral positivas para cocaína em festas.',
       'O levamisol é um anti-helmíntico veterinário com efeito imunomodulador. '
       'Causa agranulocitose idiossincrática, oclusão trombótica e vasculite de '
       'pequenos vasos da derme, com predomínio em mulheres, nas orelhas, '
       'bochechas, nariz e coxas. Induz ANCA contra MPO, PR3 e elastase, e '
       'anticorpos antifosfolípides. A pele e a medula melhoram em duas a três '
       'semanas sem exposição e pioram a cada nova exposição; o ANCA pode '
       'levar meses para negativar.',
       'A dipirona continua suspensa, mas a neutropenia que ela explicaria tem '
       'agora outra causa provável.'),

    Q('q6', 5,
      'A urina do terceiro dia, cinco dias depois do último uso, vai para '
      'toxicologia. **Quais duas** afirmações estão corretas?', [
      ('Levamisol negativo agora não exclui exposição', True),
      ('A benzoilecgonina documenta só a cocaína', True),
      ('Benzoilecgonina positiva comprova o adulterante', False),
      ('A biópsia de pele identifica a substância', False),
      ('ANCA de dois alvos dispensa toxicologia', False),
      ('Levamisol persiste semanas na urina', False),
     ], [
      ('A janela', 'O levamisol tem meia-vida de cerca de 5,6 horas, e só 2% '
       'a 5% saem inalterados na urina. A pesquisa por cromatografia com '
       'espectrometria de massa rende nas primeiras 48 horas; cinco dias '
       'depois, o negativo é o esperado e não afasta nada.'),
      ('O que a toxicologia mostra', 'A benzoilecgonina é o metabólito da '
       'cocaína e fica detectável por dias, mais em quem usa com frequência. '
       'Positiva, confirma o uso de cocaína, não a presença do adulterante.'),
      ('Por que não as outras', 'A biópsia mostra o dano do vaso, não a '
       'molécula que o causou. O ANCA sustenta a hipótese, mas não substitui '
       'a história e a toxicologia. O diagnóstico final continua clínico e '
       'provável, e é assim na maior parte dos casos publicados.'),
     ]),

    painel('res4', 'Quarto e quinto dias', 'Toxicologia e biópsia renal', [
        ex('Benzoilecgonina urinária, confirmada por cromatografia', 'Detectada', 'Não detectada', True),
        ex('Levamisol urinário (LC-MS/MS)', 'Não detectado', 'Não detectado'),
        ex('Biópsia renal, microscopia', 'Glomerulonefrite necrosante com crescentes celulares em 5 de 18 glomérulos · fibrose intersticial mínima', '—', True),
        ex('Biópsia renal, imunofluorescência', 'Pauci-imune', '—', True),
        ex('Creatinina', '2,6 mg/dL', '0,6–1,1 mg/dL', True),
        ex('Neutrófilos absolutos', '1.100/mm³', '1.500–7.500/mm³', True),
    ], introducao='A biópsia renal foi feita no quarto dia, com plaquetas e '
                  'coagulação normais.'),

    pareamento('q7', 'Pergunta 6',
      'Exposições que produzem vasculite ou vasculopatia. Associe cada uma à '
      'síndrome que ela costuma produzir.', [
      par('Levamisol, adulterando cocaína',
          'Púrpura retiforme de orelhas, agranulocitose e ANCA duplo',
          'O quadro de Marina; a pele regride em semanas de abstinência, o '
          'anticorpo em meses.'),
      par('Cocaína inalada por anos',
          'Lesão destrutiva de linha média, com ANCA anti-elastase',
          'Destrói septo e palato e imita a granulomatose com poliangeíte.'),
      par('Propiltiouracila por meses',
          'Vasculite anti-MPO com glomerulonefrite',
          'É a droga que mais induz ANCA; suspender é a base do tratamento.'),
      par('Hidralazina por anos',
          'Lúpus induzido, com anti-histona',
          'Dose alta e acetilação lenta aumentam o risco; parte tem também '
          'ANCA anti-MPO.'),
      par('Anfetaminas e metanfetamina',
          'Vasculite necrosante de vaso médio, tipo poliarterite',
          'Descrita em usuários, sem ANCA, com acometimento cerebral e '
          'sistêmico.'),
      ], opcoes=[
      'Púrpura retiforme de orelhas, agranulocitose e ANCA duplo',
      'Lesão destrutiva de linha média, com ANCA anti-elastase',
      'Vasculite anti-MPO com glomerulonefrite',
      'Lúpus induzido, com anti-histona',
      'Vasculite necrosante de vaso médio, tipo poliarterite',
      'Arterite de células gigantes',
      ], titulo_resposta='Exposição, vaso e anticorpo',
      nota='A opção que sobrou, arterite de células gigantes, não se associa '
           'a essas exposições e é rara antes dos 50 anos.'),

    pagina('sobre_biopsia', 'Discussão', 'Sobre a biópsia renal',
      p('Crescente é a proliferação de células no espaço de Bowman, em torno '
        'de um tufo glomerular cuja parede se rompeu. Celular, é lesão recente '
        'e ainda pode regredir; fibrosa, é cicatriz. Em Marina, 5 de 18 '
        'glomérulos têm crescentes celulares, com fibrose intersticial mínima.'),
      p('Pauci-imune quer dizer imunofluorescência com pouco ou nenhum '
        'depósito de imunoglobulina ou complemento. É o padrão das vasculites '
        'ANCA e combina com o C3 e o C4 normais; a lesão por imunocomplexo ou '
        'por anticorpo antimembrana basal teria outro desenho.'),
      p('A creatinina foi de 0,9 na admissão a 1,6 no terceiro dia e a 2,6 '
        'agora. O ritmo da piora e a proporção de crescentes ativos são o que '
        'pesa na decisão sobre o rim.')),

    bifurcacao('b2', 'Decisão', 'O rim',
      'Glomerulonefrite crescêntica pauci-imune, creatinina de 2,6 mg/dL, '
      'neutrófilos em 1.100 e subindo, culturas negativas, sem cocaína há '
      'sete dias. O que você propõe?', [
      caminho('Pulso de corticoide e rituximabe, mantendo o antibiótico',
              'renal',
              'Crescentes celulares são lesão ativa e reversível; tratar agora '
              'preserva néfrons, com a infecção coberta enquanto os neutrófilos '
              'sobem.', rotulo_curto='Tratar o rim'),
      caminho('Só abstinência e suporte, esperando a regressão', 'suporte',
              'A pele e a medula respondem à abstinência; o glomérulo com '
              'crescente ativo nem sempre.', rotulo_curto='Esperar'),
      caminho('Pulso e ciclofosfamida em dose plena, suspendendo o antibiótico',
              'infeccao',
              'Ciclofosfamida é mielotóxica e ela ainda está neutropênica; '
              'suspender a cobertura soma risco.', rotulo_curto='Pulso sem cobertura'),
    ]),

    pg('renal', 'Tratamento dirigido',
       'Metilprednisolona 500 mg por dia por três dias, depois prednisona em '
       'esquema de redução, e rituximabe. A cefepima segue até os neutrófilos '
       'passarem de 500 e a febre ficar para trás; entra profilaxia para '
       '//Pneumocystis//.',
       'A equipe oferece acompanhamento para o uso de cocaína sem condicionar '
       'o cuidado à abstinência, e Marina autoriza a irmã a participar do '
       'plano.'),

    pagina('tratamento', 'Discussão', 'O que entra no tratamento',
      p('A exposição vem primeiro. Sem novo uso, a pele e a medula se '
        'recuperam na maioria dos casos publicados, sem imunossupressor, e '
        'cada recaída descrita veio de um novo uso.'),
      p('O rim não segue a pele. As séries de glomerulonefrite associada ao '
        'levamisol trataram os crescentes ativos com corticoide e rituximabe ou '
        'ciclofosfamida, como a KDIGO 2024 indica na vasculite ANCA. Numa '
        'mulher de 34 anos que acaba de sair da agranulocitose, o rituximabe '
        'poupa a fertilidade e a medula; a ciclofosfamida, quando usada, é '
        'ajustada pela contagem de leucócitos.'),
      topicos(('Troca plasmática', 'A KDIGO 2024 reserva para creatinina '
               'acima de 3,4 mg/dL, diálise, queda rápida da função ou '
               'hemorragia alveolar com hipoxemia.'),
              ('Anticoagulação', 'Sem antifosfolípide, trombo de pequeno vaso '
               'da pele não a indica, e a biópsia renal é recente.'),
              ('Seguimento', 'O ANCA persiste meses depois da remissão e não '
               'guia a duração. Quem guia é a creatinina, o sedimento e a '
               'proteinúria, com vigilância de infecção durante a '
               'imunossupressão.'))),

    pg('seguimento', 'Segunda semana',
       'Não surgem placas novas. As áreas necróticas das coxas delimitam e '
       'recebem curativo; a da orelha cicatriza. Os neutrófilos passam de '
       '2.000 no décimo dia, e a creatinina começa a cair.',
       conforme=('b2', ['alta_cedo', 'f2', 'f2'])),

    pg('alta_cedo', 'Última visita',
       'A creatinina está em 1,4 mg/dL e o sedimento tem menos hemácias. Ela '
       'aprendeu a trocar os curativos e tem consultas marcadas com '
       'nefrologia, dermatologia e o serviço de álcool e drogas.',
       conforme=('b1', ['f1', 'f2', 'f2'])),

    pg('suporte', 'Cinco dias depois',
       'A pele melhora e os neutrófilos passam de 1.500, mas a creatinina sobe '
       'para 3,8 mg/dL e a diurese cai. O sedimento segue com cilindros '
       'hemáticos.', segue='b3'),

    bifurcacao('b3', 'Decisão', 'O rim não seguiu a pele',
      'Creatinina de 3,8 mg/dL e subindo, sem cocaína há doze dias. E agora?', [
      caminho('Pulso de corticoide e rituximabe agora', 'tardio',
              'A lesão ativa ainda responde, embora parte dos néfrons já tenha '
              'sido perdida.', rotulo_curto='Tratar agora'),
      caminho('Manter a espera por mais uma semana', 'dialise',
              'Esperar a regressão espontânea com a função caindo transforma '
              'crescente celular em fibrose.', rotulo_curto='Esperar mais'),
    ]),

    pg('tardio', 'Tratamento tardio',
       'Metilprednisolona por três dias e rituximabe. A creatinina para de '
       'subir no quinto dia de tratamento, em 4,1 mg/dL, sem necessidade de '
       'diálise.', segue='tratamento'),

    pg('dialise', 'Uma semana depois',
       'A creatinina chega a 6,2 mg/dL, com potássio de 6,1 mmol/L e '
       'sobrecarga de volume. Ela começa hemodiálise. A nova biópsia mostra '
       'crescentes fibrosos na maior parte dos glomérulos.', segue='f_dialise'),

    pg('infeccao', 'Quatro dias depois',
       'Os neutrófilos, que estavam em 1.100, caem para 300 depois da '
       'ciclofosfamida. Marina tem febre de 39,4 °C, pressão de 80/46 mmHg e '
       'hemocultura com bacilo gram-negativo. Vai para a terapia intensiva.',
       segue='f_infeccao'),

    fim('f1', 'Alta no 16.º dia',
        'Marina sai com creatinina de 1,4 mg/dL, neutrófilos normais e as '
        'feridas das coxas cicatrizando. Três meses depois, sem uso, não há '
        'lesões novas e a creatinina está em 1,1 mg/dL; o ANCA segue '
        'positivo, em título menor.',
        'Antibiótico na primeira hora, a história de exposição refeita a sós e '
        'o tratamento da glomerulonefrite enquanto os crescentes eram celulares '
        'foram as decisões que preservaram o rim.', 'melhor'),

    fim('f2', 'Alta depois de internação prolongada',
        'Marina sai no 27.º dia, com creatinina de 2,2 mg/dL e cicatrizes '
        'retráteis nas coxas. Segue com nefrologia, com filtração glomerular '
        'reduzida.',
        'O atraso do antibiótico ou do tratamento do rim acrescentou dias de '
        'internação e néfrons perdidos, numa doença que responde bem quando '
        'tratada cedo.', 'medio'),

    fim('f_dialise', 'Alta em hemodiálise',
        'Marina sai no 30.º dia em hemodiálise três vezes por semana. Três '
        'meses depois, a função renal não voltou.',
        'A pele e a medula melhoraram com a abstinência, e isso tranquilizou a '
        'equipe. O glomérulo seguiu inflamado, e em duas semanas os crescentes '
        'celulares viraram fibrosos.', 'pior'),

    fim('f_infeccao', 'Choque séptico na terapia intensiva',
        'Com meropeném, vasopressor e retirada da ciclofosfamida, ela sai do '
        'choque em cinco dias e deixa a UTI no décimo. A glomerulonefrite '
        'segue ativa, e o tratamento do rim recomeça do zero.',
        'Ciclofosfamida em dose plena numa medula que mal se recuperava, com a '
        'cobertura antimicrobiana suspensa, derrubou de novo os neutrófilos e '
        'abriu caminho para a bacteremia.', 'pior'),

    pagina('retrospectiva', 'Pontos de ensino', '',
        pontos(
            'Púrpura dolorosa, angulada e ramificada, com centro necrótico, é '
            'púrpura retiforme: oclusão de vaso da derme até prova em '
            'contrário.',
            'Neutrófilos absolutos se calculam. Febre com menos de 500 é '
            'neutropenia febril e pede betalactâmico antipseudomonas na '
            'primeira hora; lesão de pele e partes moles justifica somar '
            'vancomicina.',
            'Coagulação e plaquetas normais afastam púrpura fulminante e '
            'microangiopatia; no neutropênico, a infecção angioinvasiva é a '
            'primeira a excluir, com biópsia e cultura do tecido.',
            'Hemácias dismórficas e cilindros hemáticos localizam a lesão no '
            'glomérulo, e o dano renal pode não seguir o curso da pele.',
            'ANCA contra MPO e PR3 ao mesmo tempo sugere vasculite induzida. A '
            'história de exposição precisa ser refeita a sós.',
            'O levamisol sai da urina em cerca de 48 horas: o negativo tardio '
            'não exclui. Abstinência trata a pele e a medula; crescentes '
            'ativos pedem imunossupressão com a infecção vigiada.'),
        so_kicker=True),

    pg('referencias', 'Fontes e limites',
       'Paciente, valores e percursos são ficcionais. A cena de abertura é uma '
       'ilustração autoral gerada por inteligência artificial para este caso; '
       'não é fotografia nem documentação clínica.',
       'Levamisol: '
       '<a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC2780984/" '
       'target="_blank" rel="noopener">Knowles e cols., 2009</a>; '
       '<a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC3255368/" '
       'target="_blank" rel="noopener">McGrath e cols., 2011</a> (dupla '
       'positividade MPO/PR3); '
       '<a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC4602417/" '
       'target="_blank" rel="noopener">Carlson e cols., 2014</a> '
       '(glomerulonefrite); '
       '<a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC5821816/" '
       'target="_blank" rel="noopener">revisão de vasculite induzida por '
       'levamisol</a> (meia-vida e janela urinária). Adulterantes no Brasil: '
       '<a href="https://pubmed.ncbi.nlm.nih.gov/25544694/" target="_blank" '
       'rel="noopener">Polícia Federal, Forensic Sci Int 2015</a> e estudo de '
       'fluido oral em festas, Drug Alcohol Depend 2021.',
       'Neutropenia febril: IDSA 2010 (Freifeld e cols.) e ASCO/IDSA 2018 '
       '(Taplitz e cols.). Vasculite ANCA: KDIGO 2024 e PEXIVAS (Walsh e '
       'cols., 2020). O manejo antimicrobiano é extrapolado da neutropenia '
       'febril oncológica; não há ensaio que compare imunossupressores nesta '
       'síndrome.',
       'Imagens de outros pacientes, com setas adicionadas: fotografia de '
       'pele, placa por calcifilaxia no abdome, Niels Olson, '
       '<a href="https://commons.wikimedia.org/wiki/File:Calciphylaxis.png" '
       'target="_blank" rel="noopener">Wikimedia Commons</a>, CC BY-SA 3.0; '
       'radiografia de tórax, Mikael '
       'Häggström, Wikimedia Commons, CC0; eletrocardiograma, Ewingdo, '
       'Wikimedia Commons, CC BY-SA 4.0; ultrassonografia renal, Hansen, '
       'Nielsen e Ewertsen, Wikimedia Commons, CC BY 4.0.'),
]

REVISAO = []

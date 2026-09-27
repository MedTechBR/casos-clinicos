"""Encefalite febril com paresia flácida assimétrica num homem de 71 anos.

Reescrito em 26/09/2026 no molde do //New England// (piloto: leptospirose;
ver Artifacts/nejm-casos-classicos/GRAMATICA_LIDA_2026-09-26.md). A âncora é
a meningoencefalite em idoso, herpética até prova em contrário, tratada
empiricamente como se deve. As primeiras perguntas classificam a
hiponatremia, leem o líquor, localizam a lesão e leem a ressonância; a
virada vem depois da metade, com a PCR para herpes negativa e a história da
viagem contada pela esposa. O nome do diagnóstico aparece pela primeira vez
na pergunta do exame confirmatório. As decisões de via aérea mudam o
desfecho.

Paciente ficcional. Vigilância e critérios de caso: Ministério da Saúde,
Nota Técnica n.º 79/2026-CGARB/DEDT/SVSA/MS; diagnóstico e tratamento: CDC,
páginas para profissionais consultadas em 26/09/2026.
"""
from pathlib import Path

from motor.estudo_imagem import ecg, estudo
from motor.etapas import (alt, bifurcacao, caminho, capa, desfecho, op, p,
                          pagina, painel, par, pareamento, pergunta, pontos,
                          topicos)

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
           topicos(('Sinais vitais', 'Temperatura 38,7 °C · pressão 146/84 mmHg '
                    '· frequência cardíaca 124 · frequência respiratória 20 · '
                    'SpO₂ 96% em ar ambiente · peso 78 kg.'),
                   ('Estado geral', 'Sonolento, abre os olhos quando chamado, '
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

    Q('p1', 1,
      'Sódio de 129 mmol/L. Pelos exames e pelo exame físico, qual a '
      'classificação mais provável da hiponatremia?', [
      ('Hipovolêmica, por pouca ingestão', False),
      ('Secreção inapropriada de ADH', True),
      ('Pseudo-hiponatremia', False),
      ('Hiperglicemia com desvio de água', False),
      ('Baixa ingestão de solutos', False),
      ('Hipervolêmica', False),
     ], [
      ('Passo a passo', 'A osmolalidade sérica de 270 mOsm/kg confirma '
       'hiponatremia hipotônica, o que afasta a pseudo-hiponatremia, e a glicose '
       'de 138 mg/dL muda o sódio em menos de 1 mmol/L. A urina com 456 mOsm/kg '
       'mostra que o ADH está agindo: na polidipsia e na dieta pobre em solutos, '
       'ela viria abaixo de 100.'),
      ('O volume', 'Mucosas úmidas, jugulares planas e nenhum edema indicam '
       'euvolemia. Sódio urinário de 52 mmol/L sem diurético e ácido úrico baixo, '
       'de 2,6 mg/dL, tornam a hipovolemia improvável: nela o rim poupa sódio, '
       'abaixo de 30 mmol/L. O TSH normal ajuda; a insuficiência adrenal ainda '
       'precisa ser afastada com cortisol.'),
      ('O que muda', 'Restrição de água livre, nada de soro hipotônico e '
       'correção de no máximo 8 a 10 mmol/L em 24 horas. E a causa: no idoso '
       'febril e confuso, a secreção inapropriada aponta para o sistema nervoso '
       'ou para o pulmão, e a radiografia está limpa.'),
     ]),

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

    pareamento('p2', 'Pergunta 2',
      'O líquor dele e o de outros quatro pacientes. Associe cada perfil ao '
      'diagnóstico que ele sugere.', [
      par('86 células, 58% neutrófilos, proteína 92, glicose 74/138, Gram '
          'negativo (o dele)',
          'Meningoencefalite viral em fase inicial',
          'Dezenas de células, glicose preservada e Gram negativo. Neutrófilos '
          'nos primeiros dias ocorrem em várias viroses.'),
      par('2.400 células, 95% neutrófilos, proteína 240, glicose 20/110',
          'Meningite bacteriana',
          'Milhares de neutrófilos, proteína alta e relação de glicose abaixo '
          'de 0,4.'),
      par('180 células, 90% linfócitos, proteína 110, glicose 35/100, ADA '
          'elevada',
          'Meningite tuberculosa',
          'Linfocitário, proteína alta e glicose baixa: separa tuberculose e '
          'fungo dos vírus.'),
      par('5 células, proteína 180, glicose normal',
          'Guillain-Barré (dissociação albuminocitológica)',
          'Proteína alta sem células; pode levar uma a duas semanas para '
          'aparecer.'),
      par('60 células, linfócitos, proteína 80, glicose normal, 300 hemácias '
          'sem punção traumática',
          'Encefalite herpética',
          'Hemácias sem trauma de agulha sugerem necrose hemorrágica temporal.'),
      ], opcoes=[
      'Meningoencefalite viral em fase inicial',
      'Meningite bacteriana',
      'Meningite tuberculosa',
      'Guillain-Barré (dissociação albuminocitológica)',
      'Encefalite herpética',
      'Meningite criptocócica',
      ], titulo_resposta='Célula, proteína e glicose, nessa ordem de leitura',
      nota='A opção que sobrou, criptococo, teria poucas células, pressão de '
           'abertura alta e tinta da China positiva.'),

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
      'Onde está a lesão que explica a fraqueza?', [
      ('Corno anterior da medula', True),
      ('Raízes e nervos, por desmielinização', False),
      ('Cápsula interna', False),
      ('Junção neuromuscular', False),
      ('Medula inteira, em nível torácico', False),
      ('Músculo', False),
     ], [
      ('O padrão', 'Flacidez com reflexos abolidos é lesão de neurônio motor '
       'inferior. Sensibilidade normal nos três modos, sem nível e sem retenção '
       'urinária, com distribuição assimétrica e salteada, que atinge muito um '
       'membro e pouco outro: o alvo é o corpo do neurônio motor, no corno '
       'anterior. É o padrão da poliomielite.'),
      ('Por que não as outras', 'A polirradiculoneuropatia desmielinizante '
       'costuma ser simétrica, com parestesias e perda da vibração. Uma lesão '
       'da cápsula interna daria hiperreflexia e Babinski passados os primeiros '
       'dias. Miastenia e botulismo preservam os reflexos. A lesão medular '
       'transversa daria nível sensitivo e bexiga neurogênica. Miosite daria '
       'fraqueza proximal e simétrica, e a CK é de 160.'),
      ('O que muda', 'Lesão do corpo neuronal recupera pouco e devagar, ao '
       'contrário da desmielinização, que se refaz em semanas. A ressonância '
       'passa a incluir a medula, e a eletroneuromiografia entra no pedido.'),
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
      '**Quais três** achados da ressonância pesam contra encefalite '
      'herpética?', [
      ('Hipersinal no tálamo', True),
      ('Hipersinal na substância negra', True),
      ('Lesão na substância cinzenta medular', True),
      ('Hipersinal no temporal mesial', False),
      ('Ausência de efeito de massa', False),
      ('Tomografia sem alteração', False),
     ], [
      ('O território do herpes', 'O herpes simples tipo 1 chega pelo trato '
       'olfatório e acomete o lobo temporal mesial, a ínsula, o giro do cíngulo '
       'e a face orbitária do frontal, em geral de forma assimétrica, com edema '
       'e às vezes sangramento. Tálamo, núcleos da base e tronco costumam ser '
       'poupados, e a medula quase nunca entra.'),
      ('Por que não as outras', 'O hipersinal temporal mesial é o achado típico '
       'do herpes e o mantém na lista. Tomografia normal nos primeiros dias é a '
       'regra na encefalite herpética, e a falta de efeito de massa não afasta '
       'a doença.'),
      ('O que muda', 'Tálamo, substância negra e corno anterior, juntos, são o '
       'padrão de vírus que infectam neurônios profundos, como alguns arbovírus '
       'e enterovírus. A substância negra acometida combina com o tremor. O '
       'aciclovir continua até a PCR, e a história de exposição volta a '
       'importar.'),
     ]),

    pg('respiracao', 'Segundo dia de internação',
       'No fim da tarde, a tosse fica fraca e ele engasga com água. Frequência '
       'respiratória de 22, SpO₂ de 96% em ar ambiente, gasometria com pH 7,43 '
       'e pCO₂ de 38 mmHg. A capacidade vital caiu de 24 para 17 mL/kg em oito '
       'horas; pressão inspiratória máxima de −22 cmH₂O e expiratória de 34 '
       'cmH₂O.',
       'A eletroneuromiografia do mesmo dia mostra potenciais motores de '
       'amplitude reduzida, mais à direita, com velocidades de condução normais '
       'e potenciais sensitivos preservados.'),

    Q('p5', 5,
      '**Quais quatro** dados dele indicam intubação eletiva agora?', [
      ('Capacidade vital de 17 mL/kg', True),
      ('Pressão inspiratória máxima de −22 cmH₂O', True),
      ('Pressão expiratória máxima de 34 cmH₂O', True),
      ('Tosse fraca e engasgo com água', True),
      ('SpO₂ de 96% em ar ambiente', False),
      ('pCO₂ de 38 mmHg', False),
      ('Frequência respiratória de 22', False),
     ], [
      ('A regra 20/30/40', 'Na fraqueza neuromuscular, capacidade vital abaixo '
       'de 20 mL/kg, pressão inspiratória máxima menos negativa que −30 cmH₂O e '
       'expiratória abaixo de 40 cmH₂O anunciam falência ventilatória. Ele tem '
       '17, −22 e 34, e a capacidade vital caiu quase 30% em oito horas.'),
      ('A via aérea', 'Tosse fraca e engasgo com água indicam disfunção bulbar: '
       'o risco é aspirar, qualquer que seja a espirometria.'),
      ('O que engana', 'Saturação e pCO₂ normais são a regra até perto do fim. '
       'A bomba fraca hipoventila tarde, e quando a pCO₂ sobe e a saturação cai '
       'a intubação já é de emergência. Frequência respiratória de 22 é '
       'inespecífica.'),
     ]),

    bifurcacao('b2', 'Decisão', 'Suporte respiratório',
      'Como você conduz essa mudança?', [
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
      'A equipe suspeita de infecção pelo vírus do Nilo Ocidental adquirida na '
      'viagem. No sétimo dia de doença, qual exame sustenta melhor o '
      'diagnóstico?', [
      ('IgM específica no líquor', True),
      ('RT-PCR no líquor', False),
      ('RT-PCR no sangue', False),
      ('IgG específica no soro', False),
      ('Cultura viral do líquor', False),
      ('Pesquisa do antígeno NS1', False),
     ], [
      ('O tempo da doença', 'A viremia é curta e costuma acabar quando os '
       'sintomas neurológicos começam, por isso a RT-PCR tem sensibilidade baixa '
       'no imunocompetente: positiva, confirma; negativa, não afasta. A IgM '
       'aparece entre o terceiro e o oitavo dia de doença.'),
      ('Por que no líquor', 'A IgM não atravessa a barreira hematoencefálica: '
       'no líquor, foi produzida ali, o que indica doença neuroinvasiva. No '
       'soro, pode persistir por meses depois de uma infecção antiga.'),
      ('A armadilha deste paciente', 'Ele teve dengue e tomou a vacina de febre '
       'amarela, e os flavivírus dão reação cruzada. Pela Nota Técnica 79/2026 '
       'do Ministério da Saúde, IgM no líquor confirma o caso quando os outros '
       'flavivírus testados são não reagentes; havendo reatividade cruzada, '
       'decide o teste de neutralização por redução de placas, com título pelo '
       'menos quatro vezes maior para o vírus do Nilo Ocidental.'),
      ('Por que não as outras', 'IgG sozinha não data a infecção, a cultura '
       'viral é lenta e pouco sensível, e o NS1 é antígeno da dengue.'),
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

    Q('p7', 7,
      'Sobre o tratamento a partir de agora, **quais três** afirmações estão '
      'corretas?', [
      ('Suspender aciclovir e antibióticos', True),
      ('Não há antiviral com benefício comprovado', True),
      ('Reabilitação motora e respiratória desde a UTI', True),
      ('Imunoglobulina endovenosa muda o desfecho', False),
      ('Corticoide em dose alta acelera a recuperação', False),
      ('Ribavirina pela gravidade', False),
      ('Manter o aciclovir por 14 dias', False),
     ], [
      ('O que sai', 'PCR para herpes negativa em líquor colhido depois de 72 '
       'horas de sintomas, com outro diagnóstico confirmado, permite suspender '
       'o aciclovir. Hemoculturas negativas em 72 horas e um líquor que não é '
       'bacteriano permitem suspender ceftriaxona e ampicilina.'),
      ('O que não entra', 'Ribavirina, interferon, corticoide e imunoglobulina '
       'foram testados ou usados sem benefício conclusivo. O único ensaio '
       'randomizado de imunoglobulina rica em anticorpos contra o vírus foi '
       'inconclusivo (Gnann e cols., 2019). Não há antiviral específico.'),
      ('O que muda o desfecho', 'O suporte: ventilação, prevenção de '
       'aspiração, trombose e úlcera por pressão, nutrição por via segura, '
       'controle do sódio e fisioterapia desde a UTI. A recuperação motora da '
       'poliomielite é lenta e muitas vezes incompleta.'),
     ]),

    pg('recuperacao', 'Segunda e terceira semanas',
       'A febre acaba no sexto dia de internação. O tremor diminui, e ele volta '
       'a conversar, lúcido. O braço direito recupera força; a perna direita '
       'continua sem vencer a gravidade. A eletroneuromiografia da terceira '
       'semana mostra fibrilações na perna direita, sinal de denervação.'),

    Q('p8', 8,
      'Sobre vigilância e orientação na alta, **quais três** medidas estão '
      'corretas?', [
      ('Notificação imediata, já na suspeita', True),
      ('Não doar sangue por 120 dias', True),
      ('Reabilitação continuada depois da alta', True),
      ('Isolamento de contato em casa', False),
      ('Vacinar a esposa', False),
      ('Sorologia de rotina para a esposa', False),
      ('Antiviral profilático para a família', False),
     ], [
      ('Vigilância', 'A febre do Nilo Ocidental é de notificação compulsória '
       'imediata no Brasil: todo caso suspeito vai à vigilância em até 24 horas, '
       'antes da sorologia. Mesmo num caso importado, a vigilância investiga se '
       'houve exposição local, porque o vírus já circula no país.'),
      ('Transmissão', 'Não há transmissão por contato. Ela ocorre pela picada '
       'e, raramente, por transfusão, transplante e via transplacentária; por '
       'isso ele não deve doar sangue por 120 dias, como recomenda o CDC. Não '
       'há vacina humana, e a esposa, sem sintomas, não precisa de exame.'),
      ('Seguimento', 'Fisioterapia, fonoaudiologia e acompanhamento neurológico '
       'continuam depois da alta; fraqueza e cansaço podem durar meses.'),
     ]),

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

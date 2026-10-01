"""Primeiro episódio psicótico numa estudante de 24 anos, em Teresina.

Escrito em 01/10/2026 no molde do //New England// aprovado (modelos:
endocardite e leptospirose; ver Artifacts/nejm-casos-classicos/
GRAMATICA_LIDA_2026-09-26.md). Apresentação curta, ficha com a pista
enterrada (um cisto de ovário de dois anos antes, sem controle), exame com
os vitais em cima, primeiros exames entregues prontos.

Âncoras registradas pela equipe: primeiro episódio psicótico com rastreio
orgânico negativo (haloperidol, leito de saúde mental) e, no segundo dia,
síndrome neuroléptica maligna. A reação não explica as discinesias
orofaciais, a crise e a hipoventilação; líquor com pleocitose linfocítica
leve, PCR para herpes negativa, ressonância normal e eletroencefalograma com
delta e atividade rápida sobreposta. As perguntas antes da virada só
classificam e localizam (sinais de alerta, mecanismo da reação, sítio da
doença). A virada é o anticorpo no líquor, depois da metade do percurso; a
imagem da pelve vem com a decisão de procurar o tumor. Decisões: o que fazer
com o antipsicótico, tratar e procurar o tumor já ou esperar, e escalar
para a segunda linha.

Paciente ficcional. Critérios de Graus e cols. (Lancet Neurol 2016);
desfechos de Titulaer e cols. (Lancet Neurol 2013); consenso brasileiro de
encefalites autoimunes (Dutra e cols., Arq Neuropsiquiatr 2024); filtração
pelo CKD-EPI 2021.
"""
import json
from pathlib import Path

from motor.estudo_imagem import estudo
from motor.etapas import (alt, bifurcacao, caminho, capa, desfecho, op, p,
                          pagina, painel, par, pareamento, pergunta, pontos,
                          topicos, vitais)

TITULO = 'Dez noites'
RODAPE = 'Paciente ficcional · evoluções simuladas para ensino'
COR = '#7c3aed'
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
       'Camila, de 24 anos, estudante do último ano de arquitetura em Teresina, '
       'é trazida à emergência pela mãe e pelo irmão. Há dez dias dorme duas ou '
       'três horas por noite, anda pela casa de madrugada e diz que os vizinhos '
       'instalaram câmeras para filmá-la. Nos últimos três dias a fala ficou '
       'rápida e difícil de acompanhar. "Ela não é assim", diz a mãe.',
       'Há cinco dias a família a levou a uma unidade de pronto atendimento, '
       'onde o quadro foi atribuído à ansiedade com o trabalho de conclusão de '
       'curso; recebeu clonazepam 0,5 mg à noite, sem melhora do sono. Ontem '
       'saiu de casa descalça, às 3 horas, e foi trazida de volta por um vizinho.',
       'A mãe lembra que, cerca de duas semanas antes de tudo começar, Camila '
       'passou quatro dias com dor de cabeça, febre baixa e dor no corpo, '
       'tratados em casa como virose. A família nega uso de drogas, trauma na '
       'cabeça e remédios novos além do clonazepam.'),

    pagina('ficha', 'Ficha do paciente', '',
           topicos(('Antecedentes', 'Rinite alérgica. Nunca consultou psiquiatra. Aos '
                    '22 anos, uma ultrassonografia transvaginal pedida por cólica '
                    'menstrual descreveu um cisto de 3 cm no ovário direito, "de '
                    'aspecto benigno"; o controle sugerido não foi feito.'),
                   ('Medicações', 'Anticoncepcional oral combinado há quatro anos. '
                    'Clonazepam 0,5 mg à noite há cinco dias. Loratadina nas crises de '
                    'rinite.'),
                   ('Hábitos', 'Duas a três latas de cerveja nos fins de semana. Fumou '
                    'maconha algumas vezes aos 19 anos; a família e as amigas dizem que '
                    'não usa há anos. Não fuma tabaco.'),
                   ('Vida social', 'Mora com a mãe e o irmão. Entrega o trabalho de '
                    'conclusão em três semanas; a orientadora achou a última versão '
                    '"desconexa". Não viajou nos últimos meses.'),
                   ('Família', 'Tia materna em tratamento para depressão. Pai '
                    'hipertenso. Sem epilepsia, esquizofrenia ou transtorno bipolar '
                    'conhecidos.')),
           so_kicker=True),

    pagina('exame', 'Exame físico', '',
           vitais(('Temperatura', '37,4 °C', False),
                  ('Pressão arterial', '132/84', False),
                  ('Frequência cardíaca', '108', True),
                  ('Frequência respiratória', '18', False),
                  ('SpO₂ em ar ambiente', '98%', False),
                  ('Glicemia capilar', '94 mg/dL', False)),
           topicos(('Estado geral', 'Inquieta, levanta da maca várias vezes. Corada e '
                    'hidratada.'),
                   ('Exame mental', 'Vígil. Diz o próprio nome e reconhece a mãe; diz '
                    'que estamos em março, quando é agosto, e não sabe o nome do '
                    'hospital. A atenção se perde no meio das perguntas. Fala '
                    'acelerada, com saltos de assunto, e ideias de perseguição pelos '
                    'vizinhos. Nega ouvir vozes, mas olha várias vezes para o canto da '
                    'sala.'),
                   ('Neurológico', 'Pupilas isocóricas e fotorreagentes, sem rigidez de '
                    'nuca, força e reflexos simétricos, marcha normal. Em dois '
                    'momentos para no meio da frase por cerca de dez segundos, com o '
                    'olhar parado, e retoma sem lembrar do que dizia.'),
                   ('Coração e pulmões', 'Taquicardia regular, sem sopros. Murmúrio '
                    'presente, sem ruídos adventícios.'),
                   ('Pele', 'Sem lesões e sem marcas de agulha.')),
           so_kicker=True),

    Q('p1', 1,
      'Dez dias de insônia, perseguição e fala desorganizada, sem psiquiatria '
      'prévia. **Quais três** achados pedem que se procure uma causa orgânica '
      'antes de fechar um transtorno psiquiátrico primário?', [
      ('Quadro febril com cefaleia semanas antes', True),
      ('Desorientação no tempo e atenção flutuante', True),
      ('Pausas com olhar parado no meio da fala', True),
      ('Ideias de perseguição pelos vizinhos', False),
      ('Primeiro episódio aos 24 anos', False),
      ('Estresse do trabalho de conclusão', False),
     ], [
      ('O que pesa', 'A psicose primária costuma deixar o sensório claro: a '
       'pessoa delira, mas sabe onde está e acompanha a conversa. Desorientação '
       'no tempo e atenção que se perde indicam que o cérebro inteiro funciona '
       'mal, o padrão do delirium. Pausas de segundos com olhar parado e sem '
       'memória do que se dizia podem ser crises focais com alteração da '
       'consciência. E febre com cefaleia pouco antes do início sugere que algo '
       'aconteceu ao próprio cérebro.'),
      ('O que pesa pouco', 'Ideias persecutórias aparecem na psicose primária e '
       'na secundária e não ajudam a separar. Aos 24 anos, Camila '
       'está na faixa típica do primeiro episódio de esquizofrenia, e estresse '
       'acadêmico não explica nenhum quadro.'),
      ('A consequência', 'Com sinais como esses, o primeiro episódio só deve ser '
       'chamado de primário depois de uma avaliação clínica e neurológica '
       'dirigida. Exames de sangue e tomografia normais ajudam, mas não encerram '
       'a busca.'),
     ]),

    pagina('rastreio', 'Discussão', 'O primeiro episódio na emergência',
      p('Em todo primeiro episódio psicótico, a emergência procura causas '
        'tratáveis: glicemia, eletrólitos, função renal e hepática, tireoide, '
        'hemograma, triagem toxicológica, teste de gravidez e, no Brasil, testes '
        'rápidos para HIV e sífilis. A tomografia de crânio entra quando há '
        'déficit, trauma, idade mais alta ou alteração da consciência.'),
      p('O que separa a psicose primária da secundária quase sempre está na beira '
        'do leito: o tempo de instalação, o nível de consciência, a atenção, o '
        'exame neurológico e a história das semanas anteriores. Nenhum exame de '
        'rastreio substitui essa leitura, e um rastreio normal não a desfaz.'),
      p('Camila colhe os exames na chegada e vai para a tomografia.')),

    painel('res1', 'Primeiros exames', 'Sangue', [
        ex('Hemoglobina / leucócitos', '13,4 g/dL / 9.800/mm³ · neutrófilos 72%', 'Hb 12–16 · 4.000–11.000'),
        ex('Plaquetas', '254.000/mm³', '150.000–450.000/mm³'),
        ex('Proteína C reativa', '4 mg/L', 'até 5 mg/L'),
        ex('Sódio / potássio / cálcio', '138 / 4,1 mmol/L / 9,4 mg/dL', 'Na 135–145 · K 3,5–5,0 · Ca 8,5–10,5'),
        ex('Glicose', '96 mg/dL', '70–99 mg/dL'),
        ex('Ureia / creatinina', '24 / 0,7 mg/dL {{(TFG 124, CKD-EPI 2021)}}', 'até 42 / 0,6–1,1'),
        ex('AST / ALT', '22 / 18 U/L', 'até 32 / 33 U/L'),
        ex('TSH', '1,9 mUI/L', '0,4–4,0 mUI/L'),
        ex('Creatinoquinase', '210 U/L', 'até 170 U/L', True),
    ], introducao='Colhidos na chegada à emergência.'),

    painel('res1b', 'Primeiros exames', 'Urina, triagem e eletrocardiograma', [
        ex('Beta-hCG sérico', 'Negativo', 'negativo'),
        ex('Urina tipo 1', 'Sem alterações', '—'),
        ex('Triagem toxicológica na urina', 'Benzodiazepínicos positivos · cocaína, canabinoides e anfetaminas negativos', '—', True),
        ex('Etanol sérico', 'Não detectado', 'não detectado'),
        ex('Testes rápidos para HIV e sífilis', 'Não reagentes', 'não reagentes'),
        ex('Eletrocardiograma', 'Taquicardia sinusal, 106 bpm · QTc 428 ms · sem outras alterações', '—'),
    ]),

    estudo('tc_cranio', 'Tomografia de crânio sem contraste',
           'Feita na emergência, pela desorientação. Corte axial na altura dos '
           'átrios dos ventrículos laterais.',
           IMG / 'tc_cranio.jpg',
           'Tomografia de outro paciente · comparação didática · recortada no corte axial.',
           credito_meta(IMG / 'tc_cranio.jpg.json'),
        [
         ((335, 345), (130, 420), '**Parênquima frontal** com diferenciação normal entre '
          'substância cinzenta e branca, sem hipodensidade.', 12),
         ((505, 470), (720, 330), '**Fissura inter-hemisférica** na linha média, sem desvio.', -12),
         ((607, 868), (820, 1000), '**Plexo coroide calcificado** no átrio do ventrículo '
          'lateral, achado habitual e sem significado clínico.', 12),
        ],
        ['Sem lesão expansiva, sangramento, hipodensidade ou hidrocefalia. '
         'Ventrículos de tamanho normal. Calcificações fisiológicas do plexo '
         'coroide.',
         'A tomografia afasta o que muda a conduta na hora. É pouco sensível para '
         'doenças que alteram a função do cérebro sem mudar sua forma.']),

    pg('plano', 'O que a equipe registra',
       'O psiquiatra de plantão avalia Camila às 22 horas e escreve: "Primeiro '
       'episódio psicótico agudo, com agitação e insônia, em contexto de estresse '
       'acadêmico. Rastreio orgânico sem alterações. Hipóteses: transtorno '
       'psicótico agudo e transitório; episódio maníaco com sintomas psicóticos."',
       'O raciocínio da evolução: tomografia, exames de sangue e triagem vieram '
       'normais, fora o benzodiazepínico receitado na UPA. A desorientação foi '
       'atribuída a dez noites quase sem sono e ao clonazepam; as pausas no meio '
       'da frase, ao bloqueio do pensamento, comum na psicose. O quadro febril '
       'de semanas antes ficou registrado como "virose, sem relação aparente". '
       'A psicose por substância fica de lado, com triagem negativa para '
       'estimulantes e maconha.',
       'Prescrição: haloperidol 5 mg com prometazina 50 mg intramusculares para '
       'a agitação, depois haloperidol 5 mg por via oral de 12 em 12 horas. O '
       'clonazepam é suspenso. Camila vai para o leito de saúde mental do '
       'hospital geral, com acompanhante.'),

    pagina('dia2', 'Segundo dia, 9 horas', '',
           p('Na primeira noite dormiu quatro horas. No primeiro dia ficou mais '
             'quieta e passou a responder com monossílabos; à noite parou de falar. '
             'Às 9 horas do segundo dia a enfermagem chama: Camila está febril, '
             'suada e rígida no leito, e não responde ao chamado.'),
           vitais(('Temperatura', '39,2 °C', True),
                  ('Pressão em duas horas', '168/100 a 96/58', True),
                  ('Frequência cardíaca', '132', True),
                  ('Frequência respiratória', '24', True),
                  ('SpO₂ em ar ambiente', '96%', False)),
           topicos(('Neurológico', 'Olhos abertos, não fixa o olhar nem obedece a '
                    'comandos. Rigidez em cano de chumbo nos quatro membros, igual em '
                    'toda a amplitude do movimento. Reflexos simétricos, sem clônus. '
                    'Pupilas de 3 mm, fotorreagentes.'),
                   ('Pele', 'Sudorese intensa, sem exantema.'),
                   ('Exames da manhã', 'Creatinoquinase 4.800 U/L (210 na chegada). '
                    'Leucócitos 14.200/mm³. Creatinina 0,9 mg/dL. Urina escura, com '
                    'sangue ++ na fita e 2 hemácias por campo.')),
           so_kicker=True),

    Q('p2', 2,
      'Rigidez em cano de chumbo, febre de 39,2 °C, pressão oscilante, '
      'sudorese, mutismo e CK de 4.800 U/L no segundo dia de internação. A que '
      'mecanismo o quadro corresponde?', [
      ('Bloqueio dopaminérgico central', True),
      ('Excesso de serotonina', False),
      ('Bloqueio colinérgico', False),
      ('Abstinência de benzodiazepínico', False),
      ('Excesso simpático por estimulante', False),
      ('Infecção sistêmica com sepse', False),
     ], [
      ('A leitura', 'Rigidez difusa que não muda com a velocidade do movimento, '
       'febre, instabilidade autonômica, alteração da consciência e CK alta, '
       'instalados em horas a poucos dias depois de um antagonista da dopamina, '
       'como o haloperidol da véspera, formam a síndrome por bloqueio '
       'dopaminérgico. O bloqueio no hipotálamo desregula a temperatura; no '
       'estriado, produz a rigidez, e a contração mantida libera CK e '
       'mioglobina, que explica a fita com sangue e poucas hemácias.'),
      ('Por que não as outras', 'O excesso de serotonina se instala em horas e '
       'dá clônus, hiper-reflexia e diarreia, ausentes aqui. O bloqueio '
       'colinérgico seca a pele e dilata as pupilas; Camila está suada, com '
       'pupilas de 3 mm. A abstinência do clonazepam suspenso dá tremor, '
       'agitação e crises, não rigidez com CK alta. A triagem não mostrou '
       'estimulante. Infecção precisa ser afastada, mas não explica a rigidez.'),
      ('Uma ressalva', 'Quadro igual aparece na catatonia maligna, e um cérebro '
       'já doente é fator de risco conhecido para a reação ao antipsicótico. O '
       'mecanismo responde à pergunta do momento, sem dizer por que a reação '
       'aconteceu.'),
     ]),

    pagina('nms', 'Discussão', 'A reação ao antipsicótico',
      p('A equipe registra a segunda hipótese: síndrome neuroléptica maligna. '
        'Pelo consenso internacional de 2011, ela se apoia em exposição a '
        'antagonista dopaminérgico nas 72 horas anteriores, febre acima de 38 °C '
        'em duas medidas, rigidez, alteração da consciência, CK de pelo menos '
        'quatro vezes o limite, instabilidade autonômica e ausência de outra '
        'causa. Camila preenche todos os itens, menos o último, que ainda não foi '
        'testado.'),
      p('A síndrome é rara, em torno de 0,01% a 0,02% dos expostos nas séries '
        'recentes. Pesam a dose alta ou o aumento rápido, a via intramuscular, a '
        'desidratação, a agitação e a doença cerebral prévia. A mortalidade, que '
        'já passou de 20%, hoje fica abaixo de 10% com reconhecimento precoce e '
        'suporte.'),
      p('Hemoculturas e urocultura são colhidas. A pergunta imediata é o que '
        'fazer com o antipsicótico e com a agitação, que vai voltar.')),

    bifurcacao('b1', 'Decisão', 'O antipsicótico',
      'Febre de 39,2 °C, rigidez, pressão oscilante e CK de 4.800 U/L no segundo '
      'dia de haloperidol. Como você conduz?', [
      caminho('Suspender todo antipsicótico; UTI, hidratação, resfriamento e '
              'benzodiazepínico venoso', 'uti',
              'Retirar o agente e dar suporte é o centro do tratamento; o '
              'benzodiazepínico trata a rigidez e a agitação sem bloquear '
              'dopamina.'),
      caminho('Trocar o haloperidol por olanzapina, para não perder o controle '
              'da psicose', 'atipico',
              'Antipsicótico atípico também causa a síndrome, e ela ainda está '
              'em curso.'),
      caminho('Manter o haloperidol e associar biperideno, como impregnação',
              'impregnacao',
              'Anticolinérgico trata distonia e parkinsonismo, não a síndrome; '
              'manter o agente que a causou a agrava.'),
    ]),

    pg('atipico', 'Quarto dia',
       'Com olanzapina 10 mg à noite, a febre sobe a 40,1 °C e a CK a 21.000 U/L. '
       'A creatinina vai de 0,9 a 2,8 mg/dL, com urina cor de refrigerante de '
       'cola. A olanzapina é suspensa; Camila vai para a UTI com hidratação '
       'vigorosa, resfriamento, benzodiazepínico e dantroleno, e a função renal '
       'leva duas semanas para voltar.',
       segue='uti'),

    pg('impregnacao', 'Terceiro dia',
       'Com haloperidol e biperideno, a temperatura chega a 40,6 °C, a CK passa de '
       '38.000 U/L e a creatinina sobe a 3,4 mg/dL. Camila é intubada pela rigidez '
       'e pela acidose e precisa de três sessões de hemodiálise. O antipsicótico é '
       'suspenso na UTI.',
       segue='uti'),

    pg('uti', 'Na terapia intensiva',
       'Sem antipsicótico, com cristaloide, resfriamento e diazepam venoso quando '
       'agitada, a febre cede e a CK começa a cair. Hemoculturas e urocultura são '
       'negativas.',
       'A rigidez diminui, mas Camila não volta: segue sem falar, de olhos '
       'abertos, sem seguir comandos, e a pressão e a frequência cardíaca oscilam '
       'várias vezes por hora.'),

    pg('movimentos', 'Quinto dia',
       'Aparecem movimentos que não param: Camila mastiga sem nada na boca, '
       'projeta a língua e contrai os lábios, de forma repetida, por horas, mesmo '
       'sob sedação leve. Os dedos da mão direita se mexem como se tocassem '
       'piano. À tarde tem uma crise tônico-clônica generalizada de dois minutos, '
       'tratada com diazepam e levetiracetam; depois dela, não abre mais os olhos '
       'ao chamado.',
       'A neurologia anota: "A reação ao antipsicótico não explica movimentos '
       'orofaciais contínuos, crise convulsiva e piora da consciência depois de '
       'retirado o agente. O problema está no próprio cérebro." Pede líquor, '
       'ressonância e eletroencefalograma, e inicia aciclovir 10 mg/kg de 8 em 8 '
       'horas até o resultado da pesquisa de herpes-vírus.'),

    painel('lcr', 'Quinto dia', 'Líquor', [
        ex('Aspecto / pressão de abertura', 'Límpido · 18 cmH₂O', 'límpido · até 20'),
        ex('Células', '38/mm³ · linfócitos 92%', 'até 5/mm³', True),
        ex('Hemácias', '2/mm³', '—'),
        ex('Proteína', '54 mg/dL', '15–45 mg/dL', True),
        ex('Glicose', '64 mg/dL {{(glicemia 108)}}', 'cerca de 2/3 da glicemia'),
        ex('Lactato', '2,1 mmol/L', 'até 2,8 mmol/L'),
        ex('Gram e cultura', 'Sem bactérias · cultura negativa em 48 horas', '—'),
        ex('PCR para herpes-vírus simples 1 e 2', 'Não detectado', 'não detectado'),
        ex('Bandas oligoclonais', 'Presentes no líquor, ausentes no soro', 'ausentes', True),
    ]),

    estudo('rm', 'Ressonância de encéfalo',
           'Feita no sexto dia, sob sedação. Sequência FLAIR axial na altura dos '
           'lobos temporais e do mesencéfalo, onde as infecções virais do cérebro '
           'costumam deixar marca.',
           IMG / 'rm_flair.jpg',
           'Ressonância de outro paciente · comparação didática · recortada na cabeça.',
           credito_meta(IMG / 'rm_flair.jpg.json'),
        [
         ((660, 790), (870, 640), '**Lobo temporal medial** esquerdo com sinal normal, '
          'sem o hipersinal que o herpes costuma deixar.', 12),
         ((328, 727), (170, 560), '**Corno temporal** do ventrículo lateral direito, de '
          'tamanho normal.', -12),
         ((497, 915), (280, 1100), '**Mesencéfalo** de sinal normal.', 12),
        ],
        ['Encéfalo sem alterações de sinal em FLAIR, T2 e difusão, sem realce '
         'anormal pelo contraste. Lobos temporais mediais, núcleos da base e '
         'tronco normais.',
         'Com crise, movimentos anormais e líquor inflamatório, a ressonância '
         'normal não tranquiliza: diz só que a doença ainda não deixou marca '
         'visível na estrutura.']),

    estudo('eeg', 'Eletroencefalograma',
           'Registro de 40 minutos no sexto dia, com Camila sob sedação leve, '
           'durante os movimentos da boca. Repare no ritmo de base e no que se '
           'sobrepõe a ele.',
           IMG / 'eeg_uti.jpg',
           'Traçado de outro paciente · comparação didática · quadros e ampliação do original.',
           credito_meta(IMG / 'eeg_uti.jpg.json'),
        [
         ((309, 16), (200, 120), '**Onda delta** lenta e ampla em Fp1: o ritmo de base '
          'está entre 1 e 3 ciclos por segundo, onde deveria haver alfa.', 12),
         ((523, 533), (380, 600), 'O mesmo ritmo lento nas **derivações occipitais**: a '
          'lentificação é difusa, não focal.', -12),
         ((889, 436), (720, 600), '**Atividade rápida** sobreposta a cada onda delta, '
          'como uma escova sobre a onda lenta (ampliada no quadro).', 12),
        ],
        ['Atividade delta rítmica e generalizada, de 1 a 3 Hz, com atividade beta '
         'sobreposta e sincronizada a cada onda delta. Sem descargas '
         'epileptiformes durante os movimentos orofaciais.',
         'Os movimentos da boca não têm correlato epiléptico no traçado: são um '
         'distúrbio do movimento, e não crises.']),

    Q('p3', 3,
      'Alteração da consciência há dias, uma crise convulsiva, movimentos '
      'orofaciais contínuos, líquor com 38 células por mm³, quase todas '
      'linfócitos, e eletroencefalograma com lentificação delta difusa. Onde '
      'está a doença?', [
      ('Parênquima cerebral, de forma difusa', True),
      ('Meninges, sem acometer o cérebro', False),
      ('Lesão estrutural focal', False),
      ('Músculo esquelético', False),
      ('Distúrbio metabólico sistêmico', False),
      ('Medula espinal', False),
     ], [
      ('A localização', 'Consciência alterada, crise e movimento anormal são '
       'sinais do próprio tecido cerebral, e a lentificação difusa diz que ele '
       'está acometido como um todo. Pelos critérios do Consórcio Internacional '
       'de Encefalite (2013), alteração do estado mental por mais de 24 horas '
       'sem outra causa, somada a dois critérios menores, define encefalite '
       'possível; três, provável. Os menores são febre, crises, achado focal '
       'novo, 5 ou mais células no líquor e imagem ou eletroencefalograma '
       'compatíveis. Camila tem quatro.'),
      ('Por que não as outras', 'Meningite isolada dá cefaleia e rigidez de nuca '
       'com consciência relativamente preservada, sem crises nem movimentos. '
       'Uma lesão focal apareceria na ressonância. A lesão muscular da reação ao '
       'antipsicótico explica a CK, mas não a crise nem o líquor. Glicose, '
       'sódio e funções renal e hepática normais afastam a encefalopatia '
       'metabólica.'),
      ('O que a categoria abre', 'Encefalite tem duas grandes famílias, a '
       'infecciosa, quase sempre viral, e a imunomediada. Com a pesquisa de '
       'herpes negativa e a ressonância normal, a lista continua aberta.'),
     ]),

    pg('hipovent', 'Sétimo dia',
       'A respiração fica lenta e superficial, com pausas, sem obstrução e sem '
       'fraqueza dos membros: pCO₂ de 62 mmHg e pH de 7,26. Camila é intubada. '
       'Os movimentos da boca continuam, e a frequência cardíaca alterna entre 48 '
       'e 140 sem causa aparente.',
       'A neurologia escreve: "Encefalite com PCR para herpes negativa e '
       'ressonância normal. Aciclovir mantido até a segunda PCR. Pesquisa de '
       'anticorpos contra antígenos de superfície neuronal enviada, em líquor e '
       'soro, por ensaio em células, a laboratório de referência." A mãe pergunta '
       'se a filha vai voltar a ser quem era. A equipe responde que depende da '
       'causa, que ainda não tem.'),

    pg('virada', 'Nono dia',
       'O laboratório de referência liga: anticorpos IgG contra a subunidade '
       'GluN1 do receptor NMDA (N-metil-D-aspartato) detectados no líquor, título '
       '1:32, por ensaio em células transfectadas; no soro, 1:100. A segunda PCR '
       'para herpes, colhida no sétimo dia, é negativa, e o aciclovir é suspenso.',
       'A neurologia relê a ficha da admissão e para na ultrassonografia de dois '
       'anos antes: cisto de 3 cm no ovário direito, sem controle.'),

    pg('diagnostico', 'O diagnóstico',
       'É **encefalite contra o receptor NMDA** (anti-NMDAR), definida pelos '
       'critérios de Graus e colaboradores de 2016: quadro clínico compatível, '
       'anticorpo IgG anti-GluN1 no líquor e exclusão razoável de outras causas.',
       'O receptor NMDA é um canal de glutamato essencial para memória, '
       'comportamento e controle autonômico. O anticorpo se liga à subunidade '
       'GluN1 e faz o neurônio internalizar o receptor; a perda é reversível e '
       'quase não mata neurônios, o que explica a ressonância normal e a chance '
       'real de recuperação. A doença segue fases: pródromo de virose, fase '
       'psiquiátrica, depois mutismo, discinesias orofaciais, crises, '
       'disautonomia e hipoventilação central. O traçado de Camila tem nome, '
       'delta brush extremo, visto em cerca de um terço dos adultos e ligado a '
       'doença mais grave.',
       'Na série de 577 pacientes de Titulaer (2013), 81% eram mulheres e 38% '
       'tinham tumor, quase sempre teratoma de ovário. Numa série francesa de '
       '2016, quase metade dos que receberam antipsicótico teve intolerância '
       'grave, com rigidez, febre, CK alta e piora da consciência: a reação do '
       'segundo dia fazia parte da doença.'),

    pareamento('p4', 'Pergunta 4',
      'Pelos critérios de Graus (2016) para encefalite anti-NMDAR provável, '
      'associe cada dado de Camila ao grupo em que ele entra.', [
      par('Insônia e ideias de perseguição', 'Comportamento ou cognição',
          'Sintomas psiquiátricos e queda da memória contam juntos, num grupo só.'),
      par('Mutismo depois da fala acelerada', 'Disfunção da fala',
          'Fala acelerada, redução da fala e mutismo formam o segundo grupo.'),
      par('Mastigação e protrusão da língua contínuas', 'Distúrbio do movimento',
          'Discinesias, rigidez e posturas anormais; as orofaciais são as mais '
          'típicas.'),
      par('Crise tônico-clônica de dois minutos', 'Crise epiléptica',
          'Qualquer tipo de crise conta.'),
      par('Respiração lenta com pCO₂ de 62 mmHg', 'Disautonomia ou hipoventilação central',
          'Hipoventilação de origem central e oscilação de pulso e pressão entram '
          'no mesmo grupo.'),
      par('Febre baixa duas semanas antes', 'Não entra nos critérios',
          'O pródromo de virose é comum, mas não pontua.'),
    ], opcoes=['Comportamento ou cognição', 'Disfunção da fala',
               'Distúrbio do movimento', 'Crise epiléptica',
               'Rebaixamento da consciência',
               'Disautonomia ou hipoventilação central',
               'Não entra nos critérios'],
    titulo_resposta='Seis grupos, e ela tem todos',
    nota='O rebaixamento da consciência, que ficou sem par, é o sexto grupo, e '
         'Camila também o tem. Quatro grupos com líquor ou eletroencefalograma '
         'alterados fazem o diagnóstico provável, que já autoriza tratar; três '
         'bastam se houver teratoma. O anticorpo no líquor torna o diagnóstico '
         'definido.'),

    pagina('tumor', 'Discussão', 'Onde procurar',
      p('Nas mulheres jovens com a doença, o tumor associado é quase sempre um '
        'teratoma de ovário, muitas vezes pequeno e de aspecto benigno. O '
        'teratoma contém tecidos das três camadas embrionárias, entre eles '
        'tecido nervoso que expressa o receptor NMDA; a resposta imune contra '
        'esse tecido alcança o cérebro.'),
      p('Retirar o tumor encurta a doença: na série de Titulaer, quem teve o '
        'tumor retirado junto com a imunoterapia evoluiu melhor e recaiu menos. A '
        'procura começa pela pelve, com ultrassonografia transvaginal ou '
        'ressonância; a tomografia serve quando as outras não estão à mão.'),
      p('Camila está intubada, com disautonomia, e o cisto de dois anos antes '
        'está na ficha.')),

    bifurcacao('b2', 'Decisão', 'Tratar e procurar',
      'Anticorpo anti-NMDAR no líquor, Camila intubada no nono dia, com '
      'discinesias e disautonomia. Qual o próximo passo?', [
      caminho('Metilprednisolona e imunoglobulina agora, e imagem da pelve hoje',
              'pelve',
              'A primeira linha começa já, e o tumor, se existir, precisa sair '
              'cedo.'),
      caminho('Imunoterapia agora; procurar tumor só se não houver resposta',
              'sem_busca',
              'O tumor mantém o estímulo imune; esperar a falha para procurá-lo '
              'custa semanas.'),
      caminho('Confirmar no soro por outro método e repetir o líquor antes de '
              'tratar', 'espera',
              'O IgG no líquor por ensaio em células já define o diagnóstico, e '
              'cada semana sem tratamento piora o desfecho.'),
    ]),

    pg('sem_busca', 'Terceira semana',
       'Com cinco dias de metilprednisolona e imunoglobulina, os movimentos '
       'diminuem, mas Camila continua intubada e sem contato. Sem melhora na '
       'terceira semana, a equipe pede a tomografia da pelve.',
       segue='pelve'),

    pg('espera', 'Décimo sexto dia',
       'Enquanto os exames são repetidos, Camila entra em estado de mal '
       'epiléptico no 12.º dia, controlado com midazolam contínuo e três drogas '
       'anticrise. A imunoterapia começa no 16.º dia, junto com a tomografia da '
       'pelve.',
       segue='pelve'),

    estudo('pelve', 'Tomografia da pelve com contraste',
           'Feita na UTI, com Camila intubada, no lugar da ultrassonografia '
           'transvaginal. Corte axial na altura das asas do ilíaco. Compare a '
           'densidade do conteúdo da lesão com a da gordura do subcutâneo.',
           IMG / 'tc_pelve.jpg',
           'Tomografia de outro paciente · comparação didática.',
           credito_meta(IMG / 'tc_pelve.jpg.json'),
        [
         ((544, 209), (700, 90), '**Conteúdo com densidade de gordura**, igual à do '
          'subcutâneo, ocupando quase toda a lesão.', 12),
         ((394, 274), (230, 170), '**Calcificação** grosseira na borda da lesão.', -12),
         ((530, 360), (690, 440), '**Nódulo heterogêneo** de partes moles na parte '
          'pendente, projetando-se para dentro do cisto.', 12),
        ],
        ['Massa cística pélvica de 7 cm, de origem anexial, com conteúdo de '
         'gordura, calcificação e nódulo de partes moles na parede: teratoma '
         'maduro (cisto dermoide). Na cirurgia, a lesão vinha do ovário direito.',
         'Gordura dentro de um cisto de ovário é praticamente diagnóstica de '
         'teratoma maduro. O cisto de 3 cm de dois anos antes cresceu.']),

    estudo('peca', 'A peça',
           'No dia seguinte à tomografia, a ginecologia retira a lesão por '
           'videolaparoscopia, com ooforectomia direita, porque o cisto ocupava '
           'quase todo o ovário. Lâmina da parede do cisto em hematoxilina-eosina, '
           'pequeno aumento. Procure tecidos que não deveriam estar num ovário.',
           IMG / 'peca.jpg',
           'Lâmina de outro paciente · comparação didática.',
           credito_meta(IMG / 'peca.jpg.json'),
        [
         ((464, 187), (560, 70), '**Epitélio escamoso** queratinizado, como a pele, '
          'revestindo a parede do cisto.', 12),
         ((72, 205), (170, 80), '**Anexo cutâneo** cortado de través, folículo e '
          'glândula, logo abaixo do epitélio.', -12),
         ((230, 370), (330, 560), '**Tecido glial** maduro, róseo e fibrilar, com '
          'núcleos esparsos: tecido nervoso dentro do tumor.', 12),
        ],
        ['Teratoma cístico maduro do ovário: pele com anexos, derme e tecido glial '
         'maduro na parede. Sem componente imaturo. Margens livres.',
         'O tecido nervoso do tumor expressa o receptor NMDA e é o alvo inicial da '
         'resposta imune.']),

    Q('p5', 5,
      'Sobre a imunoterapia de primeira linha que Camila recebe, **quais '
      'quatro** afirmações estão corretas?', [
      ('Metilprednisolona 1 g ao dia, cinco dias', True),
      ('Imunoglobulina 0,4 g/kg ao dia, cinco dias', True),
      ('Plasmaférese pode substituir a imunoglobulina', True),
      ('A melhora costuma levar semanas', True),
      ('Esperar o título sérico para começar', False),
      ('Suspender se não melhorar em 72 horas', False),
      ('Haloperidol para a agitação do despertar', False),
     ], [
      ('O esquema', 'A primeira linha é metilprednisolona 1 g por dia por cinco '
       'dias, com imunoglobulina humana 0,4 g/kg por dia por cinco dias, 2 g/kg '
       'no total, ou plasmaférese, cinco a sete trocas em dias alternados. O '
       'consenso brasileiro de 2024 recomenda começar nas primeiras quatro '
       'semanas de sintomas. Pelos critérios de Graus, o tratamento pode começar '
       'antes do anticorpo quando o quadro é compatível e as infecções foram '
       'razoavelmente afastadas.'),
      ('O tempo', 'Na série de Titulaer, pouco mais da metade melhorou nas '
       'primeiras quatro semanas de primeira linha com retirada do tumor. A '
       'melhora vem em semanas a meses e não se julga em dias. Na disautonomia, '
       'a plasmaférese pede cuidado com a pressão.'),
      ('O que não entra', 'O título no soro acompanha mal a doença e não decide '
       'nada; o líquor é o material que conta. Antipsicóticos típicos se evitam, '
       'pela intolerância grave que Camila já teve; agitação e insônia se tratam '
       'com benzodiazepínicos e outros sedativos, sob vigilância.'),
     ]),

    pg('semana2', 'Terceira semana',
       'Duas semanas depois do pulso, da imunoglobulina e da retirada do tumor, '
       'Camila segue intubada. As discinesias diminuíram sem sumir, ela não abre '
       'os olhos ao chamado e a pressão ainda oscila. O novo eletroencefalograma '
       'mantém a lentificação delta.'),

    bifurcacao('b3', 'Decisão', 'Sem resposta',
      'Duas semanas depois da primeira linha completa e da retirada do tumor, '
      'sem melhora clínica relevante. O que você faz?', [
      caminho('Rituximabe, como segunda linha', 'rituximabe',
              'Sem resposta à primeira linha, a segunda linha melhora o desfecho '
              'e reduz recaídas.'),
      caminho('Novo ciclo de imunoglobulina e reavaliar em um mês', 'mais_igiv',
              'Repetir a primeira linha sem escalar adia a segunda num quadro que '
              'não respondeu.'),
      caminho('Haloperidol para controlar as discinesias e a agitação',
              'halo_de_novo',
              'O antipsicótico típico já provocou a reação grave do segundo dia.'),
    ]),

    pg('mais_igiv', 'Sexta semana',
       'Com o segundo ciclo de imunoglobulina, Camila melhora pouco. O rituximabe '
       'só começa na oitava semana; ela passa 11 semanas intubada, com '
       'traqueostomia e uma pneumonia associada à ventilação no caminho.',
       segue='f2'),

    pg('halo_de_novo', 'Quarto dia de haloperidol',
       'A febre volta a 40,4 °C, com CK de 46.000 U/L, lesão renal que exige '
       'diálise e taquicardia ventricular revertida com choque. O haloperidol é '
       'suspenso, e o rituximabe só começa na sétima semana.',
       segue='f3'),

    pg('rituximabe', 'Da quarta semana em diante',
       'Rituximabe 375 mg/m² por semana, quatro doses. Na sexta semana Camila '
       'começa a acompanhar com os olhos; na oitava é extubada e as discinesias '
       'param. Na décima fala frases curtas e não lembra de nada desde a UPA.',
       'A agitação da fase de despertar é tratada com benzodiazepínico, sem '
       'antipsicótico.'),

    Q('p6', 6,
      'Camila vai para a enfermaria na 12.ª semana. **Quais três** afirmações '
      'sobre a recuperação e o seguimento estão corretas?', [
      ('A recuperação leva meses, até dois anos', True),
      ('A segunda linha reduz o risco de recaída', True),
      ('Sintomas novos pedem procurar outro teratoma', True),
      ('Antipsicótico de manutenção por dois anos', False),
      ('Anticorpo sérico negativo antes da alta', False),
      ('Imunossupressor oral contínuo, como azatioprina', False),
      ('Eletroencefalograma mensal por um ano', False),
     ], [
      ('A recuperação', 'Ela acontece na ordem inversa da instalação: voltam '
       'primeiro a respiração e a consciência, por último o comportamento, a '
       'memória e as funções executivas. Na série de Titulaer, cerca de 80% '
       'tinham boa recuperação em 24 meses, com escala de Rankin modificada de 0 '
       'a 2, e muitos seguiram melhorando depois disso. Reabilitação cognitiva e '
       'volta gradual aos estudos fazem parte do tratamento.'),
      ('As recaídas', 'Cerca de 12% recaem nos dois primeiros anos; recaem menos '
       'os que tiveram o tumor retirado e os que receberam segunda linha. Numa '
       'recaída, procura-se teratoma no outro ovário ou em outro sítio e '
       'repete-se o líquor.'),
      ('O que não entra', 'Antipsicótico de manutenção não trata a causa e expõe '
       'à mesma intolerância. O anticorpo pode persistir no soro por anos em '
       'quem está bem e não serve de critério de alta. O consenso brasileiro '
       'desaconselha imunossupressores orais na doença anti-NMDAR. '
       'Eletroencefalograma se repete por sintoma, não por calendário.'),
     ]),

    pg('alta', 'Preparando a alta',
       'Na 14.ª semana Camila caminha sozinha, conversa e começa a reabilitação '
       'cognitiva. Não lembra de quase nada dos dois meses de UTI.',
       conforme=('b2', ['alta_cedo', 'f2', 'f2'])),

    pg('alta_cedo', 'Última semana',
       'Ela pede o notebook para rever o projeto de conclusão e reconhece os '
       'próprios desenhos, embora ainda canse depois de meia hora de leitura.',
       conforme=('b1', ['f1', 'f2', 'f2'])),

    fim('f1', 'Alta para casa na 15.ª semana',
        'Camila sai andando, com reabilitação cognitiva duas vezes por semana. '
        'Retoma o curso seis meses depois; com um ano, a escala de Rankin é 1 e '
        'a ultrassonografia do ovário esquerdo é normal.',
        'Suspender o antipsicótico na primeira reação, tratar e procurar o tumor '
        'no mesmo dia do anticorpo e escalar para a segunda linha quando a '
        'primeira não bastou: cada decisão encurtou a fase grave.', 'melhor'),

    fim('f2', 'Alta depois de um percurso mais longo',
        'Camila sai viva, depois de semanas a mais de internação, e um ano depois '
        'ainda tem falhas de memória e de atenção que a impedem de voltar ao '
        'curso (Rankin 2 a 3).',
        'Um antipsicótico mantido, a imunoterapia adiada, o tumor procurado tarde '
        'ou a segunda linha atrasada prolongaram a fase grave. O tempo até o '
        'tratamento é um dos principais preditores do desfecho nessa doença.',
        'medio'),

    fim('f3', 'Sequela grave',
        'Depois de quatro meses de UTI, Camila vai para casa dependente para as '
        'atividades do dia (Rankin 4), com déficit cognitivo importante e '
        'epilepsia.',
        'Repetir o antipsicótico típico numa paciente que já tinha tido a reação '
        'grave provocou nova crise de rigidez, febre e lesão muscular e atrasou a '
        'segunda linha. Nessa doença, agitação e movimentos se tratam com '
        'benzodiazepínicos e imunoterapia.', 'pior'),

    pagina('retrospectiva', 'Pontos de ensino', '',
        pontos(
            'Num primeiro episódio psicótico, desorientação, atenção flutuante, '
            'crises, movimentos anormais ou pródromo febril pedem avaliação '
            'neurológica antes de fechar o diagnóstico psiquiátrico; tomografia e '
            'exames de sangue normais não encerram a busca.',
            'Rigidez, febre, disautonomia e CK alta depois de um antipsicótico '
            'pedem a suspensão do agente. Numa mulher jovem com psicose recente, '
            'a reação grave deve lembrar a encefalite anti-NMDAR.',
            'Discinesias orofaciais contínuas, crises e hipoventilação central '
            'depois de uma fase psiquiátrica são a sequência típica da doença; '
            'líquor com pleocitose leve e ressonância normal não a afastam.',
            'O anticorpo IgG anti-GluN1 no líquor, por ensaio em células, define '
            'o diagnóstico. Com quatro grupos clínicos e líquor ou '
            'eletroencefalograma alterados, o tratamento começa antes dele.',
            'Toda mulher com a doença precisa de imagem da pelve à procura de '
            'teratoma de ovário; retirar o tumor cedo melhora o desfecho e reduz '
            'recaídas.',
            'Primeira linha: metilprednisolona em pulso com imunoglobulina ou '
            'plasmaférese. Sem resposta clínica em cerca de duas semanas, '
            'rituximabe. Antipsicóticos típicos se evitam.'),
        so_kicker=True),

    pg('referencias', 'Fontes e limites',
       'Paciente, valores e percursos são ficcionais. A foto de abertura é uma '
       'prancheta de desenho técnico (Gaf.arq, Wikimedia Commons, CC BY-SA 2.0, '
       'commons.wikimedia.org/wiki/File:Drafting_table.jpg).',
       'Graus e cols. A clinical approach to diagnosis of autoimmune '
       'encephalitis, Lancet Neurol 2016. Titulaer e cols. Treatment and '
       'prognostic factors for long-term outcome in patients with anti-NMDA '
       'receptor encephalitis, Lancet Neurol 2013. Dutra e cols. Brazilian '
       'consensus recommendations on the diagnosis and treatment of autoimmune '
       'encephalitis in the adult and pediatric populations, Arq '
       'Neuropsiquiatr 2024. Dalmau e cols. An update on anti-NMDA receptor '
       'encephalitis for neurologists and psychiatrists, Lancet Neurol 2019. '
       'Lejuste e cols. Neuroleptic intolerance in patients with anti-NMDAR '
       'encephalitis, Neurol Neuroimmunol Neuroinflamm 2016. Schmitt e cols. '
       'Extreme delta brush, Neurology 2012. Venkatesan e cols. Case definitions '
       'of encephalitis (International Encephalitis Consortium), Clin Infect '
       'Dis 2013. Gurrera e cols. International consensus on neuroleptic '
       'malignant syndrome diagnostic criteria, J Clin Psychiatry 2011.',
       'Imagens, todas de outros pacientes, com setas adicionadas: tomografia de '
       'crânio, Mikael Häggström, CC0, recortada '
       '(commons.wikimedia.org/wiki/File:CT_of_a_normal_brain,_axial_21.png); '
       'ressonância FLAIR, 511KeV, CC BY-SA 4.0, recortada '
       '(commons.wikimedia.org/wiki/File:Mri_Brain_Flair_Axial_(7).jpg); '
       'eletroencefalograma, Mizoguchi, Hara, Hirose e Nakajima, CC BY 4.0 '
       '(commons.wikimedia.org/wiki/File:Extreme_delta_brush_in_anti-NMDAr_encephalitis.png); '
       'tomografia da pelve, Hellerhoff, CC BY-SA 4.0 '
       '(commons.wikimedia.org/wiki/File:Reifes_zystisches_Teratom_des_Ovars_Dermoidzyste_46W_-_CT_axial_KM_-_001.jpg); '
       'lâmina, Librepath, CC BY-SA 3.0 '
       '(commons.wikimedia.org/wiki/File:Mature_ovarian_teratoma_with_mature_neural_elements_--_low_mag.jpg). '
       'Todas pelo Wikimedia Commons.'),
]

REVISAO = []

"""Febre baixa, confusão que vai e volta, petéquias e urina escura numa técnica
de enfermagem de Quixadá, no sertão central do Ceará.

Escrito em 01/10/2026 no molde do //New England// (piloto: leptospirose; ver
Artifacts/nejm-casos-classicos/GRAMATICA_LIDA_2026-09-26.md). Apresentação
curta, ficha com a pista enterrada (uma "síndrome HELLP" que nunca fechou, sete
anos antes; anticoncepcional com estrogênio; tireoidite), exame com os vitais
em cima, foto da pele e primeiros exames entregues prontos. As três perguntas
antes da virada só classificam: o mecanismo da plaquetopenia (produção,
consumo, sequestro), o tipo de hemólise (intra ou extravascular, com ou sem
anticorpo) e se a coagulação está consumida.

Âncora registrada pela equipe: sepse com coagulação intravascular, de foco
meníngeo (ela trabalha na emergência e o setor atendeu uma meningite) ou
urinário, com AVC e encefalite como alternativas. A primeira decisão traz as
tentações do ramo: transfundir plaquetas para puncionar o líquor. A virada é a
lâmina revista pela hematologia (esquizócitos) e o escore PLASMIC; o nome
aparece depois da metade do percurso, e a atividade da enzima com o inibidor
chega só na evolução. Tratamento: troca plasmática urgente, corticoide,
rituximabe; caplacizumabe registrado pela Anvisa (2021) e fora do SUS.

Paciente ficcional. Fontes: Zheng e cols., ISTH 2020 (diagnóstico e
tratamento) e atualização focada de 2025; Scully e cols., BSH 2023; Cuker e
cols., critérios de resposta do IWG, Blood 2021; Bendapudi e cols., PLASMIC,
Lancet Haematol 2017; Zini e cols., ICSH 2021; filtração pelo CKD-EPI 2021.
"""
import json
from pathlib import Path

from motor.estudo_imagem import estudo
from motor.etapas import (alt, bifurcacao, caminho, capa, desfecho, op, p,
                          pagina, painel, par, pareamento, pergunta, pontos,
                          topicos, vitais)

TITULO = 'Do outro lado do plantão'
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


def disc(k, titulo, *textos, segue=''):
    return pagina(k, 'Discussão', titulo, *(p(t) for t in textos), segue=segue)


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
       'Sandra, técnica de enfermagem de 36 anos, moradora de Quixadá, no '
       'sertão central do Ceará, é trazida à emergência do hospital regional '
       'pelo marido no quarto dia de dor de cabeça, cansaço e febre baixa, '
       'entre 37,6 e 38 °C. Há três dias apareceram pintas vermelhas nas '
       'pernas e a gengiva sangra ao escovar os dentes. Desde ontem a urina '
       'está "cor de café".',
       'O marido conta que duas vezes, ontem e hoje, ela "trocou as palavras" '
       'e repetiu a mesma pergunta por alguns minutos, e depois voltou ao '
       'normal. No segundo dia, numa unidade de pronto atendimento, o teste '
       'NS1 para dengue foi negativo e as plaquetas eram 38.000/mm³; saiu com '
       'soro oral e orientação de voltar se piorasse.',
       'Nega diarreia, vômitos, tosse, rigidez no pescoço, convulsão, viagem '
       'recente, picada de carrapato, contato com água de enchente e uso de '
       'anti-inflamatório. Tem dor lombar leve desde ontem.'),

    pagina('ficha', 'Ficha do paciente', '',
           topicos(('Antecedentes', 'Hipotireoidismo por tireoidite de Hashimoto '
                    'há cinco anos. Duas gestações: a primeira sem intercorrências; '
                    'na segunda, aos 29 anos, cesárea de urgência com 34 semanas '
                    'por "pré-eclâmpsia grave com síndrome HELLP", nove dias de '
                    'UTI, transfusão de plaquetas e de plasma. O bebê nasceu bem.'),
                   ('Medicações', 'Levotiroxina 75 µg ao dia. Anticoncepcional '
                    'oral combinado, etinilestradiol e levonorgestrel, há um '
                    'ano. Dipirona para a dor de cabeça nestes quatro dias.'),
                   ('Hábitos', 'Não fuma. Cerveja em festas. Nega drogas.'),
                   ('Trabalho', 'Plantões noturnos na emergência do hospital '
                    'municipal. Na semana passada o setor atendeu um rapaz com '
                    'meningite; ela não participou da intubação e não recebeu '
                    'profilaxia. Acidente com agulha há dois anos, com '
                    'seguimento sorológico negativo.'),
                   ('Família', 'Mãe hipertensa, viva. Uma irmã com hipotireoidismo. '
                    'Sem doença do sangue conhecida na família.')),
           so_kicker=True),

    pagina('exame', 'Exame físico', '',
           vitais(('Temperatura', '37,9 °C', True),
                  ('Pressão arterial', '148/92', True),
                  ('Frequência cardíaca', '104', True),
                  ('Frequência respiratória', '20', False),
                  ('SpO₂ em ar ambiente', '97%', False),
                  ('Glasgow', '14', True)),
           topicos(('Estado geral', 'Descorada, com icterícia leve nas escleras. '
                    'Sonolenta, desorientada no tempo, obedece a comandos.'),
                   ('Pele e mucosas', 'Petéquias nas pernas e nos antebraços, '
                    'algumas confluentes. Sangramento discreto na gengiva.'),
                   ('Neurológico', 'Sem rigidez de nuca, sem déficit motor, '
                    'pupilas simétricas. Fala fluente no momento do exame.'),
                   ('Coração e pulmões', 'Taquicárdica, sem sopros. Pulmões '
                    'limpos.'),
                   ('Abdome', 'Doloroso à palpação profunda no flanco esquerdo. '
                    'Fígado e baço não palpáveis.'),
                   ('Linfonodos', 'Sem adenomegalias.')),
           so_kicker=True),

    estudo('pele', 'As pintas das pernas',
           'Fotografia de outro paciente com plaquetas muito baixas, com o mesmo '
           'tipo de lesão que Sandra tem nas pernas. Observe o tamanho, o relevo '
           'e o que acontece onde as lesões se juntam.',
           IMG / 'pele_perna.jpg',
           'Fotografia de outro paciente · comparação didática.',
           credito_meta(IMG / 'pele_perna.jpg.json'),
        [
         ((361, 474), (205, 560), '**Petéquia**: ponto vermelho-escuro de 1 a 2 mm, plano, '
          'que não some à pressão.', 12),
         ((389, 392), (250, 330), '**Lesão maior**, de vários milímetros, onde petéquias '
          'confluíram: púrpura.', -12),
         ((529, 478), (660, 560), 'Outra **petéquia**, isolada, na pele de cor normal: as '
          'lesões se espalham sem relevo.', 12),
        ],
        ['No exame de Sandra: petéquias nas pernas e nos antebraços, algumas '
         'confluentes, e sangramento discreto da gengiva.',
         'Púrpura plana, que não se palpa, é sangramento de capilar por falta '
         'de plaqueta. A púrpura que se palpa sugere inflamação da parede do '
         'vaso, e a que vem com necrose central, embolia ou infecção do vaso.']),

    painel('res1', 'Primeiros exames', 'Sangue', [
        ex('Hemoglobina / hematócrito', '7,8 g/dL / 23%', 'Hb 12–16 g/dL', True),
        ex('VCM / RDW', '88 fL / 18,6%', '80–100 fL / 11,5–14,5%', True),
        ex('Leucócitos', '9.800/mm³ · neutrófilos 72%', '4.000–11.000/mm³'),
        ex('Plaquetas', '14.000/mm³ {{(38.000 na UPA, dois dias antes)}}', '150.000–450.000/mm³', True),
        ex('Volume plaquetário médio', '12,4 fL', '7–11 fL', True),
        ex('Reticulócitos', '7,8%', '0,5–2,5%', True),
        ex('Lâmina revista pelo laboratório', 'Plaquetopenia confirmada, sem agregados · anisocitose e policromasia', '—', True),
        ex('Ureia / creatinina', '62 / 1,4 mg/dL {{(TFG 50, CKD-EPI 2021)}}', 'até 42 / 0,6–1,1', True),
        ex('Proteína C reativa', '24 mg/L', 'até 5 mg/L', True),
    ], introducao='Colhidos na chegada. Dois pares de hemoculturas foram colhidos '
                  'antes de qualquer antibiótico.'),

    Q('p1', 1,
      'Anemia, plaquetopenia rapidamente progressiva e urina escura: quais **três exames** mais distinguem perda sanguínea, hemólise imune e hemólise intravascular agora?', [
      ('DHL, bilirrubinas e haptoglobina', True),
      ('Teste de antiglobulina direto', True),
      ('Urina com fita e microscopia', True),
      ('Mielograma', False),
      ('Pesquisa de sangue oculto nas fezes', False),
      ('Ultrassonografia do baço', False),
     ], [
      ('Rendimento imediato', '**DHL, bilirrubinas e haptoglobina** procuram destruição eritrocitária. **Antiglobulina direta** testa um mecanismo imune. **Fita e microscopia da urina** distinguem hemácias de pigmento heme; a CK ajuda a comparar hemoglobina e mioglobina.'),
      ('Prioridade menor', '**Mielograma** não é a primeira etapa com reticulocitose e queda rápida de plaquetas. **Sangue oculto fecal** não explicaria por si icterícia e pigmentúria. **Ultrassom do baço** pode avaliar sequestro, mas discrimina menos o mecanismo urgente de anemia e lesão de órgãos.'),
     ]),

    painel('res1b', 'Primeiros exames', 'Hemólise e urina', [
        ex('Bilirrubina total / indireta', '3,2 / 2,7 mg/dL', 'até 1,2 / 0,9 mg/dL', True),
        ex('Desidrogenase lática (DHL)', '1.480 U/L', '120–246 U/L', True),
        ex('Haptoglobina', 'menor que 10 mg/dL', '30–200 mg/dL', True),
        ex('Teste de antiglobulina direto', 'Negativo', 'negativo'),
        ex('AST / ALT', '58 / 31 U/L', 'até 32 / 33 U/L', True),
        ex('Creatinoquinase', '110 U/L', 'até 170 U/L'),
        ex('Urina', 'Marrom-escura · sangue +++ · 0 a 2 hemácias por campo · 8 leucócitos por campo · nitrito negativo · proteína +', '—', True),
        ex('Beta-hCG sérico', 'Negativo', 'negativo'),
    ]),

    disc('urina',
       'A urina cor de café',
       'A urina permanece escura. A fita marca sangue +++, mas o microscópio encontra até duas hemácias por campo; a creatinoquinase é de 110 U/L.',
       'A haptoglobina veio menor que 10 mg/dL. A equipe precisa explicar a discrepância entre a fita e a microscopia em conjunto com os marcadores sanguíneos.',
       'Os oito leucócitos por campo, sem nitrito, são anotados junto da dor lombar e da febre. A urocultura está em andamento.'),

    Q('p2', 2,
      'Sangue +++ na fita, 0–2 hemácias/campo, CK normal e antiglobulina negativa: qual interpretação melhor explica a anemia e a urina?', [
      ('Hemólise com componente intravascular; mecanismo imune menos provável', True),
      ('Hematúria glomerular como causa principal da anemia', False),
      ('Mioglobinúria por lesão muscular como causa da urina escura', False),
      ('Hemólise imune comprovada pela bilirrubina indireta', False),
      ('Sangramento gengival como explicação suficiente da anemia', False),
     ], [
      ('Integração', 'Pigmento heme sem hemácias proporcionais, associado a haptoglobina muito baixa e DHL alta, favorece hemoglobinúria. CK normal torna mioglobinúria menos provável; a perda gengival não produz esse perfil bioquímico.'),
      ('O que ainda não se sabe', 'Antiglobulina negativa reduz, mas não zera, a possibilidade de hemólise imune. Bilirrubina indireta não identifica anticorpos. É preciso investigar fragmentação eritrocitária e outras causas não imunes, sem definir a etiologia só por esses dados.'),
     ]),

    painel('res1c', 'Primeiros exames', 'Coagulação e outros', [
        ex('Tempo de protrombina / INR', '13,1 s / 1,08', 'INR até 1,2'),
        ex('TTPa (relação)', '29 s (1,0)', 'até 1,25'),
        ex('Fibrinogênio', '340 mg/dL', '200–400 mg/dL'),
        ex('D-dímero', '1.200 ng/mL', 'até 500 ng/mL', True),
        ex('Lactato arterial', '1,6 mmol/L', 'até 2,0 mmol/L'),
        ex('Troponina I', '0,09 ng/mL', 'até 0,04 ng/mL', True),
        ex('Eletrocardiograma', 'Taquicardia sinusal, 104 bpm · sem alterações de ST', '—'),
    ]),

    estudo('tc', 'Tomografia de crânio sem contraste',
           'Feita na primeira hora, pela confusão que vai e volta, antes de '
           'decidir se é seguro puncionar o líquor. Corte axial na altura dos '
           'ventrículos laterais.',
           IMG / 'tc_cranio.jpg',
           'Tomografia de outro paciente · comparação didática.',
           credito_meta(IMG / 'tc_cranio.jpg.json'),
        [
         ((508, 522), (120, 300), '**Corno frontal** do ventrículo lateral, de tamanho normal '
          'e simétrico ao do outro lado.', 12),
         ((430, 780), (120, 980), '**Corno occipital**: sem sangue no ventrículo e sem '
          'desvio da linha média.', -12),
         ((632, 375), (880, 180), '**Substância branca frontal** sem hipodensidade: '
          'nenhum sinal de infarto estabelecido.', -12),
        ],
        ['Sem hemorragia, sem hipodensidade, sem efeito de massa. Ventrículos '
         'e sulcos normais para a idade.',
         'Uma tomografia normal nas primeiras horas não afasta isquemia '
         'pequena, transitória ou recente, nem encefalite.']),

    pg('plano', 'O que a equipe registra',
       'Na evolução da admissão, a equipe escreve: "Sepse de foco a esclarecer, '
       'com plaquetopenia grave, hemólise e possível coagulação intravascular '
       'disseminada. Hipóteses: doença meningocócica, pielonefrite. '
       'Diferenciais: encefalite viral, AVC isquêmico."',
       'O raciocínio: febre, petéquias e confusão numa profissional que atende '
       'emergências, numa semana em que o setor recebeu uma meningite, exigem '
       'tratar como doença meningocócica até prova em contrário. A dor lombar '
       'e os leucócitos na urina sustentam um foco urinário. A troponina de '
       '0,09 entra na conta da taquicardia e da sepse. A dengue grave fica '
       'menos provável com o NS1 negativo no segundo dia, e não houve '
       'extravasamento de plasma.',
       'O plano é antibiótico, punção lombar "assim que as plaquetas '
       'permitirem" e reavaliação da coagulação.'),

    Q('p3', 3,
      'Com hemólise, plaquetas de 14.000 e INR/fibrinogênio preservados, quais **dois exames** priorizar para discriminar o mecanismo da microangiopatia suspeita?', [
      ('Revisão do esfregaço com quantificação de esquizócitos', True),
      ('Atividade de ADAMTS13 e pesquisa de inibidor antes do plasma', True),
      ('C3 e C4 séricos', False),
      ('Pesquisa de toxina Shiga nas fezes', False),
      ('Vitamina B12 e homocisteína', False),
     ], [
      ('Prioridade diagnóstica', '**Esfregaço revisto** procura fragmentação eritrocitária e conecta a hemólise à plaquetopenia. **ADAMTS13/inibidor**, antes do plasma, discrimina deficiência grave; a espera pelo resultado não deve atrasar tratamento se a probabilidade clínica for alta.'),
      ('Outras microangiopatias', '**C3/C4** podem complementar a investigação, mas valores normais não afastam mecanismo por complemento e valores baixos não o confirmam. **Toxina Shiga** ganha prioridade com pródromo diarreico, ausente aqui. **B12/homocisteína** investigam pseudomicroangiopatia; reticulocitose e VCM de 88 tornam essa hipótese menos provável neste momento.'),
     ]),

    disc('coag',
       'Hemólise e coagulação',
       'INR, TTPa e fibrinogênio preservados pesam contra CIVD franca, sem excluir uma fase inicial. O D-dímero elevado é inespecífico.',
       'A queda das plaquetas acompanha hemólise, alterações transitórias da fala, creatinina de 1,4 mg/dL e troponina discretamente elevada. A equipe mantém a investigação de infecção e amplia as hipóteses.'),

    bifurcacao('b1', 'Decisão', 'A punção e as plaquetas',
      'Febre, confusão e petéquias numa profissional da emergência: a equipe não '
      'quer deixar uma meningite sem tratamento. Plaquetas de 14.000/mm³, '
      'hemoculturas colhidas. Como você conduz as próximas horas?', [
      caminho('Ceftriaxona agora, adiar a punção, sem transfundir plaquetas, '
              'e pedir à hematologia que reveja a lâmina',
              'noite',
              'O antibiótico cobre a hipótese grave sem esperar o líquor. A '
              'hemólise sem explicação pede um olho treinado na lâmina, e '
              'plaqueta transfundida num consumo sem causa definida pode piorar '
              'o que consome.'),
      caminho('Transfundir plaquetas para puncionar o líquor e iniciar '
              'ceftriaxona', 'transfusao',
              'Puncionar pede plaquetas acima de 40.000 a 50.000, mas a '
              'transfusão num consumo que ainda não tem nome é o passo que '
              'mais pode piorar a doença.'),
      caminho('Ceftriaxona e aguardar as hemoculturas antes de investigar mais',
              'espera',
              'O antibiótico está certo, mas a hemólise sem anticorpo e sem '
              'coagulação intravascular fica sem explicação por mais um dia.'),
    ]),

    pg('transfusao', 'Primeira noite',
       'Ela recebe uma dose de plaquetas por aférese. Uma hora depois a contagem '
       'é de 21.000/mm³, e a punção é feita: líquor com 2 células, proteína de '
       '38 mg/dL, glicose normal e Gram sem bactérias.',
       'Às 3 horas, a enfermeira encontra Sandra sem conseguir falar e com a mão '
       'direita fraca. Desta vez o déficit não passa. A ressonância da manhã '
       'mostra um infarto pequeno no território da artéria cerebral média '
       'esquerda. As plaquetas voltaram para 9.000/mm³.',
       segue='manha'),

    pg('espera', 'Primeira noite e segundo dia',
       'Com ceftriaxona, a febre cede pouco. A lâmina fica para a rotina do '
       'laboratório. No fim da tarde do segundo dia, as plaquetas estão em '
       '8.000/mm³, a creatinina sobe para 1,9 mg/dL e Sandra tem um episódio de '
       'quarenta minutos sem conseguir falar. A hematologia é chamada.',
       segue='manha'),

    pg('noite', 'Primeira noite',
       'Ceftriaxona 2 g a cada 12 horas, dose de meningite, desde a primeira '
       'hora. A punção fica adiada. Às 3 horas, Sandra passa quinze minutos sem '
       'achar as palavras; quando a neurologista chega, o exame já é normal.',
       'Às 6 horas: plaquetas 11.000/mm³, hemoglobina 7,1 g/dL, DHL 1.720 U/L, '
       'creatinina 1,5 mg/dL. As hemoculturas seguem sem crescimento.'),

    pg('manha', 'A lâmina',
       'A hematologista de plantão pega a lâmina da admissão e a de hoje e '
       'conta as hemácias ao microscópio, campo por campo. O laudo automatizado '
       'falava só em anisocitose e policromasia. Ela encontra 4,2% de hemácias '
       'fragmentadas, com plaquetas raras e reticulócitos abundantes.'),

    estudo('esfregaco', 'Esfregaço de sangue periférico',
           'Lâmina de outro paciente, com o mesmo achado que a hematologista '
           'contou na de Sandra. Compare o contorno das células marcadas com o '
           'de uma hemácia íntegra.',
           IMG / 'esfregaco.jpg',
           'Lâmina de outro paciente · comparação didática · região recortada.',
           credito_meta(IMG / 'esfregaco.jpg.json'),
        [
         ((336, 653), (175, 760), '**Hemácia em capacete**: perdeu um pedaço e ficou com '
          'uma borda reta e duas pontas.', 12),
         ((354, 731), (470, 805), '**Fragmento irregular**, menor que uma hemácia, sem '
          'halo central.', -12),
         ((361, 354), (285, 450), '**Hemácia íntegra**, redonda, com o halo central claro: '
          'a referência.', 12),
        ],
        ['No esfregaço de Sandra: 4,2% de esquizócitos (hemácias em capacete, '
         'triângulos e fragmentos), policromasia e plaquetas raras, sem '
         'agregados.',
         'Acima de 1%, num adulto com hemólise e plaquetopenia, a contagem apoia a suspeita de microangiopatia pela recomendação do ICSH de 2021.']),

    disc('fragmentos', 'O que parte a hemácia',
       'Esquizócito é a hemácia cortada ao passar por um vaso pequeno cheio de '
       'fios de plaqueta ou de fibrina, ou por uma prótese valvar. Com teste de '
       'antiglobulina negativo, hemólise dentro do vaso e plaquetas consumidas, '
       'os achados de Sandra formam uma anemia hemolítica microangiopática com '
       'plaquetopenia: a síndrome de microangiopatia trombótica.',
       'A confusão que vai e volta, a creatinina de 1,5 mg/dL e a troponina de 0,09 sugerem isquemia de órgão por trombos nos vasos pequenos do cérebro, do rim e do coração.',
       'A coagulação preservada pesa contra CIVD franca, sem excluir sua fase inicial. Ela não tem prótese, câncer conhecido, transplante, diarreia nem pressão em nível de emergência hipertensiva, e o beta-hCG é negativo. A hematologista calcula um escore à beira do leito.'),

    pagina('plasmic', 'Discussão', 'O escore PLASMIC',
        p('O escore PLASMIC estima, em quem tem microangiopatia trombótica, a '
          'chance de atividade da ADAMTS13 abaixo de 10%. Cada item vale um '
          'ponto. Na conta de Sandra, todos pontuam:'),
        topicos(('Plaquetas abaixo de 30.000/mm³', '14.000, e 11.000 na manhã seguinte.'),
                ('Hemólise', 'Reticulócitos de 7,8%, haptoglobina indetectável, '
                 'bilirrubina indireta de 2,7 mg/dL.'),
                ('Sem câncer ativo e sem transplante', 'Nenhum dos dois.'),
                ('VCM abaixo de 90 fL', '88 fL.'),
                ('INR abaixo de 1,5', '1,08.'),
                ('Creatinina abaixo de 2,0 mg/dL', '1,4 mg/dL.')),
        p('Sete pontos. Com 6 ou 7, a maioria dos pacientes tem a enzima '
          'gravemente deficiente. A amostra para a ADAMTS13 é colhida agora, '
          'antes de qualquer plasma; o resultado vem de um laboratório de '
          'referência e leva dias.')),

    pg('diagnostico', 'O diagnóstico',
       'É **púrpura trombocitopênica trombótica**, quase certamente imune, a '
       'confirmar pela atividade da ADAMTS13 e pelo inibidor.',
       'A ADAMTS13 corta os multímeros muito grandes do fator de von '
       'Willebrand que o endotélio libera. Quando um autoanticorpo bloqueia ou '
       'retira a enzima, esses multímeros ficam esticados nos vasos pequenos, '
       'onde o sangue corre rápido, e capturam plaquetas. Formam-se trombos de '
       'plaqueta e fator de von Willebrand, quase sem fibrina: por isso as '
       'plaquetas somem e a coagulação fica normal. As hemácias se cortam '
       'nesses trombos, e os órgãos sofrem isquemia em episódios, sobretudo '
       'cérebro, coração e rim.',
       'A pêntade clássica, com febre, alteração neurológica e lesão renal, aparece completa em poucos pacientes; microangiopatia com alta suspeita clínica justifica tratamento antes da confirmação enzimática. Sem tratamento, a mortalidade passa de 90%. É mais comum em mulheres de 30 a 50 anos, e gestação, estrogênio e doença autoimune estão entre os gatilhos e as associações descritas.'),

    Q('p4', 4,
      'Ao recuperar o prontuário da internação obstétrica de Sandra, qual informação ajudaria mais a distinguir HELLP de um episódio anterior da microangiopatia atual?', [
      ('Persistência de hemólise e plaquetopenia após o parto e sua evolução com o plasma', True),
      ('Intensidade da hipertensão no dia em que foi indicada a cesárea', False),
      ('Relação entre AST e ALT na admissão à maternidade', False),
      ('Necessidade de transfusão de plaquetas durante a cesárea', False),
      ('Idade gestacional e peso do recém-nascido', False),
     ], [
      ('O evento que separa as hipóteses', 'O parto remove o fator desencadeante da HELLP, embora a recuperação possa demorar e haja piora transitória inicial. Hemólise e plaquetopenia persistentes, com recuperação associada a plasma, tornam importante reconsiderar outra microangiopatia. O prontuário recuperado adiante permitirá essa comparação.'),
      ('Achados que se sobrepõem', 'Hipertensão, alteração de transaminases, prematuridade e transfusões podem ocorrer em ambas as apresentações. A magnitude e a cronologia ajudam, mas nenhum desses dados isolados identifica o mecanismo; ADAMTS13 e inibidor caracterizam o episódio atual.'),
     ]),
    pg('transferencia', 'Fim da tarde do segundo dia',
       'O hospital regional não tem serviço de aférese. O centro de referência '
       'em Fortaleza, a cerca de 170 km, aceita Sandra e pode começar a troca '
       'plasmática na mesma noite. A ADAMTS13 foi colhida às 9 horas; o '
       'resultado deve sair em cinco a sete dias.',
       'Sandra está orientada, com plaquetas de 10.000/mm³ e DHL de 1.810 U/L. '
       'O marido pergunta se não seria melhor esperar o exame para ter certeza.'),

    bifurcacao('b2', 'Decisão', 'Sem esperar o exame',
      'PLASMIC de 7, com isquemia cerebral transitória e troponina elevada. O '
      'que você faz?', [
      caminho('Corticoide agora e transferência para troca plasmática ainda '
              'hoje, com plasma na espera', 'troca',
              'Com probabilidade alta, a troca começa antes da confirmação. A '
              'BSH pede o início em até 4 a 8 horas, e o plasma infundido é '
              'ponte enquanto a transferência não chega.'),
      caminho('Corticoide e aguardar o resultado da ADAMTS13 para confirmar '
              'antes da troca', 'aguarda',
              'O resultado leva dias, e a mortalidade se concentra nos '
              'primeiros dias sem troca plasmática.'),
      caminho('Corticoide e plasma fresco em infusão, sem transferir; troca só '
              'se piorar', 'plasma',
              'Infusão repõe a enzima, mas não retira o anticorpo, e o volume '
              'necessário quase nunca é tolerado.'),
    ]),

    pg('aguarda', 'Quarto dia',
       'Com metilprednisolona, Sandra passa dois dias estável. Na madrugada do '
       'quarto dia tem uma convulsão tônico-clônica e não recupera a fala. '
       'Plaquetas 6.000/mm³, troponina 1,8 ng/mL, creatinina 2,3 mg/dL. O '
       'resultado da ADAMTS13 ainda não chegou.',
       segue='b3'),

    bifurcacao('b3', 'Decisão', 'A convulsão',
      'Microangiopatia em progressão, com lesão cerebral e cardíaca. Qual a '
      'conduta?', [
      caminho('Transferência imediata para troca plasmática de emergência e UTI',
              'troca_tardia',
              'A troca é o que interrompe a formação dos trombos, mesmo atrasada.'),
      caminho('Transfundir plaquetas pela contagem de 6.000 e aguardar o resultado',
              'obito_pagina',
              'Sem sangramento grave, plaqueta transfundida alimenta os trombos.'),
    ]),

    pg('obito_pagina', 'Quinto dia',
       'Depois da transfusão, Sandra tem dor no peito e arritmia ventricular. '
       'É intubada e recebe noradrenalina. A transferência é organizada quando '
       'ela já está em choque.',
       segue='f_obito'),

    pg('troca_tardia', 'Em Fortaleza',
       'A primeira troca plasmática começa no quinto dia, na UTI. A ressonância '
       'mostra infartos pequenos nos dois hemisférios. As plaquetas sobem a '
       'partir do terceiro dia de troca, mas a afasia e a fraqueza da mão '
       'direita melhoram só em parte.',
       segue='p5'),

    pg('plasma', 'Terceiro dia',
       'Ela recebe 15 mL/kg de plasma fresco e metilprednisolona. Na manhã '
       'seguinte, as plaquetas estão em 9.000/mm³, a pressão sobe e os pulmões '
       'têm crepitações pelo volume. Um novo episódio de afasia dura uma hora. '
       'A transferência sai com um dia de atraso.',
       segue='troca'),

    pg('troca', 'Primeiras 48 horas no centro de referência',
       'Metilprednisolona 1 g endovenosa ao dia por três dias. Cateter de '
       'diálise na veia jugular interna, guiado por ultrassom, sem transfusão '
       'de plaquetas. Troca plasmática diária com 1,5 volume plasmático nas '
       'primeiras sessões e plasma como reposição.',
       'O caplacizumabe tem registro na Anvisa desde 2021, mas não está '
       'incorporado ao SUS nem disponível no hospital; o pedido é feito e não '
       'chega na fase aguda. A equipe prescreve rituximabe 375 mg/m² por '
       'semana, quatro doses, a partir do terceiro dia.'),

    Q('p5', 5,
      'Durante a troca diária, qual critério deve orientar seu encerramento?', [
      ('Recuperação sustentada das plaquetas, resolução da hemólise e ausência de nova isquemia', True),
      ('Recuperação das plaquetas acompanhada de negativação do inibidor de ADAMTS13', False),
      ('Normalização da DHL acompanhada de recuperação renal e cardíaca', False),
      ('Atividade de ADAMTS13 acima de 20% acompanhada de melhora neurológica', False),
      ('Conclusão do pulso de corticoide acompanhada de aumento progressivo das plaquetas', False),
     ], [
      ('Resposta clínica composta', 'A decisão combina plaquetas sustentadamente recuperadas, hemólise resolvida ou próxima da resolução conforme o protocolo e ausência de isquemia nova ou progressiva. Uma primeira contagem normal ou uma DHL em queda ainda precisam de tendência confirmada.'),
      ('Tempos biológicos diferentes', 'Inibidor e ADAMTS13 podem recuperar depois da resposta clínica; exigir esses marcos prolongaria a troca por um alvo que depende da imunossupressão. DHL e função de órgãos sem recuperação plaquetária podem dar falsa segurança. Terminar o pulso tampouco equivale a interromper a microangiopatia.'),
     ]),

    pg('evolucao', 'Primeira semana de tratamento',
       'A confusão não volta depois da primeira troca. As plaquetas sobem de '
       '10.000 para 48.000, 96.000 e 162.000/mm³ no quinto dia, e a DHL cai '
       'para 290 U/L. A creatinina volta a 0,9 mg/dL e a troponina se '
       'normaliza. As hemoculturas e a urocultura são negativas, e a '
       'ceftriaxona é suspensa.'),

    pg('resultado', 'Sexto dia',
       'Chega o resultado colhido antes do primeiro plasma: atividade da '
       'ADAMTS13 menor que 5%, com anticorpo IgG anti-ADAMTS13 presente e '
       'inibidor de 1,8 unidade Bethesda. HIV, hepatites B e C e fator '
       'antinuclear são negativos.',
       'A equipe busca o prontuário da maternidade de sete anos antes: '
       'plaquetas de 9.000/mm³, DHL de 2.100 U/L, esquizócitos "frequentes" e '
       'AST de 90 U/L, que é pouco para uma síndrome HELLP. A pressão '
       'normalizou, mas as plaquetas só se recuperaram depois de vários dias '
       'de plasma. O primeiro episódio provavelmente foi aquele.'),

    disc('remissao', 'Resposta e remissão',
       'Pelos critérios do grupo internacional de trabalho (2021), resposta '
       'clínica é plaquetas acima de 150.000/mm³ e DHL abaixo de 1,5 vez o '
       'limite, sem nova isquemia. Remissão clínica é essa resposta mantida '
       'por 30 dias depois da última troca.',
       'A enzima tem os seus próprios critérios: remissão parcial com '
       'atividade de 20% ou mais, e completa quando volta ao normal. Plaquetas '
       'normais com ADAMTS13 abaixo de 20% são remissão clínica sem remissão '
       'da enzima, e esse é o grupo que mais recai.',
       'Sandra faz a última troca no oitavo dia. Com 30 dias, as plaquetas '
       'estão em 245.000/mm³ e a ADAMTS13, em 34%.'),

    Q('p6', 6,
      'Com plaquetas de 245.000 e ADAMTS13 de 34% após 30 dias, quais **duas decisões** são sustentadas?', [
      ('Manter vigilância da ADAMTS13 mesmo com hemograma normal', True),
      ('Planejar contracepção sem estrogênio e eventual gestação com a hematologia', True),
      ('Indicar nova troca plasmática pela atividade abaixo do normal', False),
      ('Iniciar anticoagulação plena para prevenir recaída hematológica', False),
      ('Classificar a deficiência como congênita pelo episódio obstétrico', False),
     ], [
      ('Remissão e risco', 'Plaquetas recuperadas com ADAMTS13 de 34% não exigem nova troca; a atividade merece acompanhamento porque pode cair antes da recaída. Estrogênio e uma futura gestação pedem planejamento individualizado.'),
      ('Mecanismos diferentes', 'Anticoagulação plena não previne a recaída por autoanticorpo. A presença de IgG e inibidor na amostra pré-plasma sustenta doença imune, apesar do episódio obstétrico anterior. Uma queda importante futura da enzima pede reavaliação para tratamento preventivo, sem esperar a plaquetopenia.'),
     ]),

    pg('alta', 'Preparando a alta',
       'Sandra completa as quatro doses de rituximabe e recebe as orientações '
       'por escrito: sinais de alerta, datas da ADAMTS13 e a troca do '
       'anticoncepcional por um dispositivo intrauterino de levonorgestrel.',
       conforme=('b1', ['alta_b2', 'f_avc', 'alta_atraso'])),

    pg('alta_b2', 'Última semana',
       'Ela já caminha pelo corredor e conversa sem perder as palavras. O '
       'marido trouxe a farda do hospital municipal, "para ela lembrar que vai '
       'voltar".',
       conforme=('b2', ['f1', 'f_avc', 'f2'])),

    pg('alta_atraso', 'Última semana',
       'A internação foi mais longa do que precisava. Ela caminha sozinha, mas '
       'ainda se cansa no corredor.',
       conforme=('b2', ['f2', 'f_avc', 'f2'])),

    fim('f1', 'Alta em remissão, sem sequela',
        'Sandra sai no 12.º dia, sem déficit neurológico e com função renal '
        'normal. Com três meses, a ADAMTS13 está em 68%, e ela volta aos '
        'plantões.',
        'Antibiótico sem transfusão de plaquetas, a lâmina revista a tempo e a '
        'troca plasmática sem esperar a confirmação foram as decisões que '
        'contaram.', 'melhor'),

    fim('f2', 'Alta depois de um percurso mais longo',
        'Sandra sai viva e sem déficit, depois de mais episódios de isquemia, '
        'mais dias de internação e mais sessões de troca do que o necessário.',
        'O dia perdido antes da lâmina ou a troca plasmática substituída por '
        'infusão de plasma deixaram os trombos se formando por mais tempo.',
        'medio'),

    fim('f_avc', 'Alta com sequela de AVC',
        'Sandra entra em remissão, mas sai com afasia e fraqueza da mão '
        'direita, em reabilitação. Não volta à enfermagem no primeiro ano.',
        'Plaquetas transfundidas sem sangramento grave, ou a troca adiada à '
        'espera da confirmação, deram tempo e matéria-prima aos trombos '
        'cerebrais.', 'pior'),

    fim('f_obito', 'Óbito no quinto dia',
        'Sandra morre em choque cardiogênico, com infarto do miocárdio por '
        'microtrombos, antes da primeira troca plasmática.',
        'Esperar o exame confirmatório e transfundir plaquetas sem sangramento '
        'grave deram tempo e matéria-prima aos trombos; a maior '
        'parte dos óbitos acontece nos primeiros dias, muitos por isquemia do '
        'coração.', 'pior'),

    pagina('retrospectiva', 'Pontos de ensino', '',
        pontos(
            'Plaquetopenia com reticulócitos altos, volume plaquetário grande e '
            'leucócitos normais é consumo ou destruição periférica.',
            'Hemoglobina livre na urina, haptoglobina indetectável e DHL alta são hemólise intravascular; antiglobulina direta negativa reduz, sem eliminar, a possibilidade de mecanismo imune.',
            'Hemólise e plaquetopenia com coagulação preservada pedem revisão da lâmina. Esquizócitos acima de 1% apoiam microangiopatia no contexto adequado, sem definir sua etiologia ou excluir CIVD inicial.',
            'PLASMIC de 6 ou 7 basta para começar troca plasmática e '
            'corticoide; a ADAMTS13 é colhida antes do plasma e não se espera '
            'por ela.',
            'Plaqueta não se transfunde sem sangramento grave, nem para passar '
            'cateter guiado por ultrassom.',
            'Rituximabe reduz a recaída; o caplacizumabe é sugerido pela ISTH e '
            'tem registro no Brasil, mas não está no SUS.',
            'Na remissão, a ADAMTS13 é seguida por toda a vida, e estrogênio e '
            'gestação exigem planejamento.'),
        so_kicker=True),

    pg('referencias', 'Fontes e limites',
       'Paciente, valores e percursos são ficcionais. A foto de abertura é da '
       'estrada de chegada a Quixadá, Otávio Nogueira, Wikimedia Commons, CC BY '
       '2.0 (commons.wikimedia.org/wiki/File:Monólitos_em_Quixadá_(1).jpg).',
       'Zheng e cols. ISTH guidelines for the diagnosis e for the treatment of '
       'thrombotic thrombocytopenic purpura, J Thromb Haemost 2020; Zheng e '
       'cols. 2025 focused update of the 2020 ISTH guidelines, J Thromb Haemost '
       '2025. Scully e cols. A British Society for Haematology guideline: '
       'diagnosis and management of TTP and thrombotic microangiopathies, Br J '
       'Haematol 2023. Cuker e cols. Redefining outcomes in iTTP, Blood 2021. '
       'Bendapudi e cols. PLASMIC score, Lancet Haematol 2017. Zini e cols. '
       'ICSH recommendations for schistocyte counting, Int J Lab Hematol 2021. '
       'Taylor e cols. ISTH overt DIC score, Thromb Haemost 2001. Anvisa, '
       'registro do Cablivi (caplacizumabe), 2021. Registro Brasileiro de PTT, '
       'Hematol Transfus Cell Ther 2023.',
       'Imagens, todas de outros pacientes, com setas adicionadas: petéquias '
       'na perna, James Heilman, CC BY-SA 4.0 '
       '(commons.wikimedia.org/wiki/File:Petechia_lower_leg.jpg); tomografia de '
       'crânio normal, Mikael Häggström, CC0, recortada '
       '(commons.wikimedia.org/wiki/File:CT_of_a_normal_brain,_axial_17.png); '
       'esfregaço com esquizócitos, Osaro Erhabor, CC0, recortado '
       '(commons.wikimedia.org/wiki/File:Schistocytes.jpg).'),
]

REVISAO = []

# Revisão de questões: fontes clínicas consultadas em 22/10/2026.
# https://pmc.ncbi.nlm.nih.gov/articles/PMC8146131/
# https://www.isth.org/page/ttpguidelines
# Redação: https://www.nbme.org/sites/default/files/2021-02/NBME_Item%20Writing%20Guide_R_6.pdf

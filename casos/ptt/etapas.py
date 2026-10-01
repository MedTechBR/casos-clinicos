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
      'Plaquetas de 14.000/mm³, que eram 38.000 dois dias antes. Qual o '
      'mecanismo mais provável da plaquetopenia?', [
      ('Falta de produção na medula', False),
      ('Consumo ou destruição periférica', True),
      ('Sequestro no baço', False),
      ('Diluição por volume infundido', False),
      ('Artefato de coleta', False),
     ], [
      ('A leitura', 'A medula está trabalhando: os leucócitos são normais, os '
       'reticulócitos estão em 7,8% e o volume plaquetário médio de 12,4 fL '
       'indica plaquetas jovens, grandes, liberadas às pressas. Uma contagem '
       'que cai de 38.000 para 14.000 em dois dias, com produção ativa, está '
       'sendo gasta na periferia.'),
      ('Por que não as outras', 'Falta de produção costuma baixar mais de uma '
       'linhagem e vem com reticulócitos baixos. O baço não é palpável, e o '
       'sequestro raramente leva as plaquetas abaixo de 40.000. Ela não '
       'recebeu volume endovenoso. O laboratório conferiu a lâmina e não '
       'encontrou agregados, o que afasta o artefato do anticoagulante do '
       'tubo.'),
      ('O que a categoria abre', 'Plaqueta gasta na periferia é destruída por '
       'anticorpo ou consumida em trombos, pela coagulação ativada ou pela '
       'adesão às paredes de vasos lesados. A anemia, com reticulócitos '
       'altos, também parece ser de destruição: a pergunta seguinte é como.'),
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

    disc('urina', 'A urina cor de café',
       'A fita marca sangue +++, mas o microscópio encontra até duas hemácias '
       'por campo. O que reage na fita é pigmento heme livre na urina: '
       'hemoglobina, que vem da hemácia destruída dentro do '
       'vaso, ou mioglobina, que vem do músculo.',
       'Com creatinoquinase de 110 U/L, o músculo está fora. A bilirrubina '
       'escurece a urina, mas não reage como sangue na fita. Sobra a '
       'hemoglobina livre, que só chega à urina quando a haptoglobina que a '
       'carregaria já se esgotou, como mostra o resultado menor que 10 mg/dL.',
       'A AST acima da ALT, com DHL de 1.480 U/L, vem das próprias hemácias e '
       'não do fígado. Os oito leucócitos por campo, sem nitrito, pesam pouco '
       'numa mulher com dor lombar e febre, mas a equipe os anota.'),

    Q('p2', 2,
      'Hemoglobina de 7,8 g/dL com reticulócitos de 7,8%, DHL de 1.480 U/L, '
      'haptoglobina indetectável e teste de antiglobulina direto negativo. '
      '**Quais duas** leituras estão corretas?', [
      ('Hemólise intravascular', True),
      ('Hemólise extravascular predominante', False),
      ('Destruição mediada por anticorpo', False),
      ('Destruição sem anticorpo na hemácia', True),
      ('Perda de sangue oculta', False),
      ('Medula que não responde', False),
     ], [
      ('Onde a hemácia se rompe', 'Hemoglobina livre na urina, haptoglobina '
       'esgotada e DHL quase seis vezes o limite dizem que a hemácia se rompe '
       'dentro do vaso. Na hemólise extravascular, em que o baço e o fígado '
       'retiram as hemácias, a bilirrubina indireta sobe, mas a hemoglobinúria '
       'é rara e o baço costuma crescer.'),
      ('Com ou sem anticorpo', 'O teste de antiglobulina direto negativo torna '
       'improvável a destruição por anticorpo quente ou por complemento fixado '
       'na hemácia. Sobram as causas não imunes: trauma mecânico dentro dos '
       'vasos ou em próteses, toxinas, parasitas, oxidação e defeitos da '
       'membrana ou da enzima da hemácia.'),
      ('Por que não as outras', 'Reticulócitos de 7,8% mostram uma medula que '
       'responde. Perda oculta não explica DHL alta nem haptoglobina zerada.'),
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
      'INR de 1,08, TTPa com relação de 1,0, fibrinogênio de 340 mg/dL e '
      'D-dímero de 1.200 ng/mL, com plaquetas de 14.000/mm³. Como está a '
      'coagulação?', [
      ('Consumo de fatores e de fibrinogênio', False),
      ('Preservada, sem consumo de fatores', True),
      ('Falta de vitamina K', False),
      ('Falha de síntese hepática', False),
      ('Inibidor circulante de fator', False),
     ], [
      ('A leitura', 'Tempo de protrombina, TTPa e fibrinogênio normais dizem '
       'que os fatores e o fibrinogênio não estão sendo gastos. O D-dímero de '
       '1.200 ng/mL é inespecífico: sobe com inflamação, infecção e trombos '
       'pequenos de qualquer natureza.'),
      ('Contra a coagulação intravascular', 'No escore da ISTH para coagulação '
       'intravascular disseminada franca, ela soma 2 pontos pelas plaquetas '
       'abaixo de 50.000, 2 pelo D-dímero moderadamente alto, zero pelo tempo '
       'de protrombina e zero pelo fibrinogênio acima de 100 mg/dL: 4 pontos, '
       'abaixo dos 5 que definem o quadro. Na sepse grave que consome '
       'plaquetas a esse ponto, o tempo de protrombina costuma se alongar e o '
       'fibrinogênio, cair.'),
      ('Por que não as outras', 'Falta de vitamina K, falha hepática e inibidor '
       'alongariam o tempo de protrombina, o TTPa ou os dois, e nenhum deles '
       'explicaria a plaquetopenia.'),
     ]),

    disc('coag', 'Plaquetas que somem sem trombina',
       'A coagulação intravascular consome plaquetas e fatores ao mesmo tempo, '
       'porque a trombina formada ativa as duas coisas. Em Sandra só as '
       'plaquetas somem. Elas estão sendo gastas por um caminho que não passa '
       'pela cascata, e é esse caminho que a lâmina pode mostrar.',
       'Somados, os dados são três consumos que andam juntos: plaquetas gastas '
       'na periferia, hemácias destruídas dentro do vaso sem anticorpo, e '
       'órgãos que falham por episódios curtos, como a fala que vai e volta, a '
       'creatinina de 1,4 mg/dL e a troponina discretamente elevada.',
       'A equipe mantém a sepse como hipótese principal, mas risca a '
       'coagulação intravascular da evolução.'),

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
         'Acima de 1%, num adulto com hemólise e plaquetopenia, a contagem tem '
         'valor diagnóstico pela recomendação do ICSH de 2021.']),

    disc('fragmentos', 'O que parte a hemácia',
       'Esquizócito é a hemácia cortada ao passar por um vaso pequeno cheio de '
       'fios de plaqueta ou de fibrina, ou por uma prótese valvar. Com teste de '
       'antiglobulina negativo, hemólise dentro do vaso e plaquetas consumidas, '
       'os achados de Sandra formam uma anemia hemolítica microangiopática com '
       'plaquetopenia: a síndrome de microangiopatia trombótica.',
       'A febre, a confusão que vai e volta, a creatinina de 1,5 mg/dL e a '
       'troponina de 0,09 são isquemia de órgão por trombos nos vasos pequenos '
       'do cérebro, do rim e do coração.',
       'A coagulação preservada já tinha afastado a coagulação intravascular '
       'como causa. Ela não tem prótese, câncer conhecido, transplante, '
       'diarreia nem pressão em nível de emergência hipertensiva, e o beta-hCG '
       'é negativo. A hematologista calcula um escore à beira do leito.'),

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
       'A pêntade clássica, com febre, alteração neurológica e lesão renal, '
       'aparece completa em poucos pacientes; plaquetopenia e esquizócitos '
       'bastam para tratar. Sem tratamento, a mortalidade passa de 90%. É mais '
       'comum em mulheres de 30 a 50 anos, e gestação, estrogênio e doença '
       'autoimune estão entre os gatilhos e as associações descritas.'),

    pareamento('p4', 'Pergunta 4',
      'Esquizócitos com plaquetas baixas aparecem em várias doenças. Associe '
      'cada quadro à causa mais provável.', [
      par('Criança com diarreia com sangue há seis dias e diurese mínima',
          'SHU por toxina Shiga',
          'A diarreia vem antes, e o rim é o órgão que mais sofre.'),
      par('Lesão renal grave, plaquetas de 60.000 e ADAMTS13 em 55%',
          'SHU atípica, por complemento',
          'Enzima preservada com rim muito acometido: desregulação do complemento.'),
      par('Gestante de 34 semanas, PA de 170/110 e AST de 400',
          'Síndrome HELLP',
          'Hipertensão e lesão hepática no fim da gestação; resolve com o parto.'),
      par('Sepse com INR de 2,8 e fibrinogênio de 80 mg/dL',
          'Coagulação intravascular disseminada',
          'Fatores e fibrinogênio consumidos com as plaquetas.'),
      par('PA de 240/140, papiledema e creatinina subindo',
          'Emergência hipertensiva',
          'A lesão do endotélio é pela pressão; melhora quando ela cai.'),
      par('Lesão renal e hipertensão meses após gencitabina',
          'Microangiopatia por fármaco',
          'Toxicidade direta no endotélio, dependente da dose acumulada.'),
    ], opcoes=['SHU por toxina Shiga', 'SHU atípica, por complemento',
               'Síndrome HELLP', 'Coagulação intravascular disseminada',
               'Emergência hipertensiva', 'Microangiopatia por fármaco',
               'Púrpura trombocitopênica imune'],
    titulo_resposta='A causa muda o tratamento',
    nota='A opção que sobrou, púrpura trombocitopênica imune, destrói plaquetas '
         'por anticorpo, sem hemólise e sem esquizócitos.'),

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
      'Na fase aguda, **quais quatro** condutas estão corretas?', [
      ('Troca plasmática diária de 1 a 1,5 volume', True),
      ('Corticoide em dose alta com a troca', True),
      ('Rituximabe já na fase aguda', True),
      ('Profilaxia de trombose com plaquetas acima de 50.000', True),
      ('Transfundir plaquetas para passar o cateter', False),
      ('Anticoagulação plena pelos microtrombos', False),
      ('Suspender a troca quando a DHL normalizar', False),
     ], [
      ('A base', 'A troca plasmática retira o autoanticorpo e os multímeros '
       'gigantes e repõe a enzima; é diária até as plaquetas passarem de '
       '150.000/mm³ por dois dias. A ISTH, em 2020, recomenda somar '
       'corticoide e sugere rituximabe já no primeiro episódio, o que reduz a '
       'recaída. A atualização de 2025 manteve essas recomendações.'),
      ('O caplacizumabe', 'Bloqueia a ligação entre o fator de von Willebrand '
       'e a plaqueta e acelera a recuperação; a ISTH sugere usá-lo. A dose é '
       '10 mg endovenoso antes da primeira troca e 10 mg subcutâneo ao dia até '
       '30 dias depois da última, prolongado se a atividade da enzima não '
       'subir. Aumenta o sangramento de mucosas. No Brasil, o acesso costuma '
       'depender de plano de saúde ou de via judicial.'),
      ('O que não entra', 'Plaqueta só se transfunde em sangramento grave; '
       'cateter passado com ultrassom não exige. Anticoagulação plena não '
       'desfaz trombos de plaqueta e aumenta o risco de sangrar. A troca '
       'segue até a contagem de plaquetas se sustentar; parar antes disso '
       'favorece a exacerbação. Ácido fólico e heparina profilática '
       'entram quando as plaquetas passam de 50.000/mm³.'),
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
      'No seguimento de Sandra, **quais quatro** condutas estão corretas?', [
      ('Dosar ADAMTS13 a cada um a três meses', True),
      ('Rituximabe preventivo se atividade abaixo de 20%', True),
      ('Trocar o anticoncepcional por método sem estrogênio', True),
      ('Planejar gestação futura com a hematologia', True),
      ('Aspirina e anticoagulação por seis meses', False),
      ('Esplenectomia para prevenir recaída', False),
      ('Alta do seguimento após um ano normal', False),
     ], [
      ('A enzima antes da plaqueta', 'A recaída é comum nos anos seguintes, e '
       'a atividade da ADAMTS13 cai semanas antes das plaquetas. Por isso ela '
       'é dosada com regularidade, mensal nos primeiros meses e depois a cada '
       'três meses. Se cair abaixo de 20%, a ISTH sugere rituximabe '
       'preventivo, mesmo com plaquetas normais.'),
      ('Os gatilhos', 'Estrogênio e gestação estão associados a episódios. A '
       'BSH orienta contracepção sem estrogênio, como dispositivo '
       'intrauterino ou progestagênio isolado. Uma gestação futura é de risco '
       'alto e precisa de planejamento, com a enzima acompanhada mês a mês. A '
       'tireoidite lembra que a autoimunidade costuma vir acompanhada.'),
      ('O que não entra', 'Antiagregante e anticoagulação não previnem '
       'recaída. A esplenectomia fica para casos refratários ao rituximabe. O '
       'seguimento é por toda a vida, inclusive pelo risco maior de AVC, '
       'depressão e queixas cognitivas descrito em quem teve a doença.'),
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
            'Hemoglobina livre na urina, haptoglobina indetectável e DHL alta '
            'são hemólise intravascular; com antiglobulina direta negativa, não '
            'é mediada por anticorpo.',
            'Plaquetas consumidas com tempo de protrombina, TTPa e fibrinogênio '
            'normais afastam a coagulação intravascular e mandam olhar a '
            'lâmina. Esquizócitos acima de 1% definem a microangiopatia.',
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

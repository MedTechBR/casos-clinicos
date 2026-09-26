"""Febre prolongada numa valvopata reumática: Streptococcus gallolyticus.

Alíquota → pergunta, no molde dos casos interativos do //New England//. O
caso começa como febre prolongada a esclarecer: diferencial amplo, primeira
rodada sindrômica, um sedimento urinário que acusa imunocomplexo e um segundo
exame à beira do leito que encontra o que o primeiro não viu. O nome só chega
com a identificação do agente e o ecocardiograma; o pareamento dos critérios
vem depois disso. Oito perguntas, dois painéis e três decisões de conduta,
uma delas com óbito. O agente manda olhar o cólon.
Paciente ficcional.
"""
from pathlib import Path

from motor.etapas import (alt, bifurcacao, caminho, capa, desfecho, op, p,
                          pagina, painel, par, pareamento, pergunta, tabela,
                          topicos, vitais, lamina)

TITULO = 'Pequenos sinais'
RODAPE = 'Paciente ficcional · evoluções simuladas para ensino'
COR = '#db2777'
IMG = Path(__file__).parent / 'img'
BANCO = []


def pg(k, titulo, *textos, segue='', conforme=None):
    return pagina(k, titulo, '', *(p(t) for t in textos), so_kicker=True,
                  segue=segue, conforme=conforme)


def Q(k, n, enunciado, itens, titulo, segue=''):
    return pergunta(k, f'Pergunta {n}', enunciado,
                    [alt(t, c, certa=ok) for t, c, ok in itens],
                    titulo_resposta=titulo, segue=segue)


def ex(nome, valor, ref='—', alt_=False):
    return op(nome, resultado=valor, referencia=ref, alterado=alt_)


def fim(k, titulo, texto, porque, qualidade):
    return desfecho(k, titulo, p(texto), qualidade=qualidade, porque=porque,
                    fecho='retrospectiva')


ETAPAS = [
    capa(TITULO, fundo='cena.png', kicker='Caso interativo',
         selo='Paciente ficcional · procedência e créditos na última tela'),

    pg('historia', 'Apresentação',
       'Lúcia, 59 anos, costureira em Sobral, procura o ambulatório de clínica '
       'médica por cinco semanas de febre no fim do dia, cansaço e suor '
       'noturno. Perdeu 5 kg. "Não tenho mais força nem para a máquina de '
       'costura."',
       'Na terceira semana, a unidade básica tratou como infecção urinária, '
       'com ciprofloxacino por sete dias. A febre sumiu e voltou quatro dias '
       'depois. Na quarta semana recebeu amoxicilina por cinco dias por '
       '"sinusite", sem mudança.'),

    pg('hda', 'História da doença atual',
       'A febre fica entre 37,8 e 38,3 °C, quase sempre à tarde. Há dor '
       'lombar e nos joelhos, sem inchaço, e o apetite caiu. Nega tosse, '
       'disúria, diarreia, dor de garganta e manchas na pele.',
       'Mede a temperatura em casa com termômetro digital e trouxe as '
       'anotações das últimas três semanas: nenhum dia sem febre.'),

    pg('antecedentes', 'Antecedentes',
       'Teve febre reumática na infância e acompanha um sopro no posto. Um '
       'ecocardiograma de três anos atrás descreveu insuficiência mitral '
       'moderada. É hipertensa e usa losartana.',
       'Anemia ferropriva tratada com sulfato ferroso há seis meses, sem '
       'investigação da causa. Não viajou, não tem contato conhecido com '
       'tuberculose e nega uso de drogas. Mora com a filha e um gato.'),

    pagina('exame', 'Exame físico', '',
           vitais(('Temperatura', '38,1 °C', True), ('Pressão arterial', '132/70', False),
                  ('Frequência cardíaca', '98', False), ('Frequência respiratória', '18', False),
                  ('SpO₂ em ar ambiente', '96%', False)),
           topicos(('Estado geral', 'Emagrecida, mucosas descoradas.'),
                   ('Linfonodos', 'Sem adenomegalias cervicais, axilares ou inguinais.'),
                   ('Cardiovascular', 'Sopro holossistólico 3+/6 no foco mitral, irradiado '
                    'para a axila. Sem terceira bulha.'),
                   ('Abdome', 'Baço palpável a 2 cm do rebordo costal, indolor.'),
                   ('Articulações', 'Dor à mobilização dos joelhos, sem calor nem derrame.'),
                   ('Neurológico', 'Sem déficit focal. Rigidez de nuca ausente.')),
           so_kicker=True),

    Q('p1', 1,
      'Febre há cinco semanas, emagrecimento, baço palpável e anemia numa '
      'mulher com valvopatia reumática, depois de dois antibióticos curtos. '
      '**Quais cinco** diagnósticos precisam ser considerados?', [
      ('Endocardite infecciosa', 'Valvopatia prévia e febre que recua com '
       'antibiótico curto e depois volta mantêm a hipótese na lista.', True),
      ('Linfoma', 'Febre, suor noturno, perda de peso e baço palpável. Não se '
       'fecha febre prolongada sem pensar nele.', True),
      ('Tuberculose extrapulmonar ou disseminada', 'Febre vespertina e '
       'emagrecimento no Brasil. Pode cursar com radiografia de tórax '
       'normal.', True),
      ('Doença autoimune sistêmica, como lúpus ou vasculite', 'Febre, '
       'artralgia e anemia numa mulher. Menos comum depois dos 50, mas '
       'cabe na primeira lista.', True),
      ('Mixoma atrial', 'Tumor cardíaco dá febre, emagrecimento e sopro. O '
       'sopro dela pode não ser só reumático.', True),
      ('Febre reumática aguda recorrente', 'Rara depois dos 40, e ela não '
       'tem artrite migratória, coreia nem nódulos subcutâneos.', False),
      ('Doença de Still do adulto', 'Picos acima de 39 °C, exantema que '
       'acompanha a febre e artrite franca. Não é o padrão dela.', False),
      ('Pielonefrite crônica', 'Sem sintomas urinários, e não explicaria o '
       'baço palpável.', False),
      ('Hipertireoidismo', 'Explica perda de peso e taquicardia, não cinco '
       'semanas de febre com baço palpável.', False),
      ('Sinusite bacteriana', 'O diagnóstico da unidade básica não explica '
       'cinco semanas de febre nem o baço.', False),
     ], 'Febre que cede com antibiótico e volta'),

    Q('ex1', 2,
      'Lúcia está estável e sem antibiótico há seis dias. **Quais cinco** '
      'exames são os mais apropriados agora?', [
      ('Três pares de hemoculturas de punções separadas, antes de qualquer '
       'antibiótico', 'Antibióticos curtos podem ter escondido bacteremia. '
       'Seis dias sem eles é a janela para colher.', True),
      ('Hemograma com esfregaço de sangue periférico', 'Citopenias, blastos '
       'ou linfócitos atípicos separam infecção de doença hematológica.',
       True),
      ('Urina com sedimento e creatinina', 'Hematúria, cilindros ou lesão '
       'renal mudam o território da investigação.', True),
      ('Radiografia de tórax', 'Infiltrado, cavidade ou mediastino alargado '
       'separam tuberculose e linfoma cedo e barato.', True),
      ('Fator antinuclear, fator reumatoide e complemento', 'A triagem '
       'autoimune entra na primeira rodada de febre prolongada.', True),
      ('PET-CT com FDG como primeiro exame', 'Útil quando a primeira rodada '
       'não esclarece. Não substitui culturas nem exames básicos.', False),
      ('Biópsia de medula óssea', 'Entra com citopenias ou esfregaço '
       'alterado, que ainda não foram vistos.', False),
      ('Antibiótico empírico de amplo espectro e reavaliação em 72 horas',
       'Ela está estável. Um terceiro antibiótico às cegas negativaria de '
       'novo as culturas.', False),
      ('Procalcitonina para decidir se é infecção', 'Não separa as causas '
       'de febre prolongada nem autoriza encerrar a busca.', False),
      ('Antiestreptolisina O', 'Mostra estreptococcia recente, não '
       'recorrência reumática sem critérios de Jones.', False),
     ], 'Primeira rodada de febre prolongada'),

    painel('res1', 'Resultados', 'O que a equipe pediu', [
        ex('Hemoculturas', 'Três pares colhidos com uma hora de intervalo · '
           'em incubação, sem leitura ainda', '—'),
        ex('Hemoglobina', '9,8 g/dL · VCM 76 fL · hipocromia no esfregaço, '
           'sem blastos', '12–16 g/dL', True),
        ex('Leucócitos / plaquetas', '11.200 (78% neutrófilos) / 180.000 por mm³',
           '4.000–11.000 / 150.000–450.000'),
        ex('Ferritina', '18 ng/mL', '15–150 ng/mL'),
        ex('VHS / proteína C reativa', '86 mm/h / 74 mg/L', 'até 20 / até 5', True),
        ex('Creatinina', '1,3 mg/dL · TFG estimada 47 mL/min/1,73 m² (CKD-EPI 2021)',
           '0,6–1,1 mg/dL', True),
        ex('Urina', 'Hematúria de 15 por campo, 40% de hemácias dismórficas · '
           'proteinúria 1+', 'normal', True),
        ex('FAN / fator reumatoide', 'Não reagente / reagente, 64 UI/mL',
           'não reagente / até 14', True),
        ex('Complemento C3 / C4', '58 / 22 mg/dL', '90–180 / 10–40', True),
        ex('Radiografia de tórax', 'Sem infiltrado, sem cavidade, mediastino '
           'normal · área cardíaca no limite superior', '—'),
    ], introducao='Exames colhidos na primeira consulta. A equipe acrescentou '
                  'ferritina, anti-HIV e VDRL, estes dois não reagentes.'),

    Q('p3', 3,
      'Hematúria dismórfica, proteinúria, C3 baixo e fator reumatoide '
      'reagente, com FAN negativo. **Quais três** afirmações sobre esse '
      'conjunto estão corretas?', [
      ('Aponta glomerulonefrite por imunocomplexo, e não lesão tubular',
       'Dismorfismo e proteinúria localizam no glomérulo. C3 baixo indica '
       'consumo por imunocomplexo.', True),
      ('Fator reumatoide pode surgir em infecção prolongada, sem artrite '
       'reumatoide', 'Antígeno persistente estimula sua produção, e o título '
       'cai quando a fonte é controlada.', True),
      ('FAN negativo torna lúpus improvável como explicação do conjunto',
       'Nefrite lúpica com FAN negativo é raríssima. A fonte de '
       'imunocomplexo deve ser outra.', True),
      ('C3 baixo com C4 normal é o padrão típico da crioglobulinemia mista',
       'A crioglobulinemia consome sobretudo C4. C3 isolado baixo sugere '
       'via alternativa.', False),
      ('Fator reumatoide de 64 UI/mL confirma artrite reumatoide',
       'Sem sinovite nem anti-CCP, o fator reumatoide isolado é '
       'inespecífico.', False),
      ('Com creatinina de 1,3, a função renal está preservada',
       'Pelo CKD-EPI 2021, 1,3 mg/dL nessa mulher equivale a TFG de 47. '
       'Já há perda.', False),
      ('O padrão indica nefrite intersticial pelo ciprofloxacino',
       'Nefrite intersticial dá leucocitúria e cilindros leucocitários, não '
       'dismorfismo com C3 baixo.', False),
     ], 'O glomérulo acusa imunocomplexo'),

    pg('segundo_dia', 'Segundo dia',
       'A febre de 38,4 °C volta às 16 horas. Perguntada de novo sobre o '
       'intestino, Lúcia conta que há três meses as fezes às vezes vêm "mais '
       'escuras". Atribuiu ao sulfato ferroso e não comentou antes.',
       'Às 20 horas, a microbiologia liga: os três pares positivaram com '
       'cocos gram-positivos em cadeia, todos entre 14 e 18 horas de '
       'incubação. A identificação e o antibiograma estão em curso.'),

    pagina('beira_leito', 'À beira do leito', '',
           p('O residente volta ao leito e examina as mãos, os pés e os olhos '
             'com calma, sob luz boa. Lúcia lembra de "dois caroços doloridos" '
             'na ponta dos dedos na semana anterior, que sumiram em dois dias.'),
           topicos(('Unhas', 'Três hemorragias lineares, finas e avermelhadas, sob as '
                    'unhas do segundo e do terceiro dedos da mão direita.'),
                   ('Dedos', 'Nódulo de 4 mm, doloroso, na polpa do quarto dedo direito.'),
                   ('Plantas', 'Duas máculas eritematosas de 3 mm na planta esquerda, '
                    'indolores à pressão.'),
                   ('Olhos', 'Duas petéquias na conjuntiva palpebral inferior esquerda, '
                    'vistas só com a pálpebra evertida.')),
           so_kicker=True),

    Q('p4', 4,
      'Três pares positivos com cocos gram-positivos em cadeia, e os achados '
      'da reavaliação. **Quais três** afirmações estão corretas?', [
      ('Três pares de punções separadas indicam bacteremia contínua, de '
       'fonte intravascular', 'Contaminante costuma positivar um frasco. '
       'Três punções positivas ao longo de horas são bacteremia contínua.',
       True),
      ('Cocos em cadeia apontam estreptococo ou enterococo, e não '
       'estafilococo', 'Estafilococos se agrupam em cachos. Cadeias são de '
       'estreptococos e enterococos.', True),
      ('O ecocardiograma deve ser feito agora, sem esperar a identificação',
       'Bacteremia contínua em valva doente, com lesões cutâneas novas, '
       'exige ver a valva já.', True),
      ('Positividade com menos de 24 horas sugere contaminação da coleta',
       'Crescimento rápido sugere inóculo alto. Contaminantes demoram mais e '
       'positivam um frasco.', False),
      ('As hemorragias sob as unhas são específicas e fecham a causa',
       'São inespecíficas: aparecem em trauma e em trabalho manual, '
       'como o de costureira.', False),
      ('O mixoma atrial passa a explicar melhor o quadro que uma infecção',
       'Mixoma não positiva hemoculturas. Três pares com cocos puxam para '
       'infecção.', False),
      ('Os antibióticos curtos esterilizaram a fonte, basta repetir as '
       'culturas', 'A febre voltou depois de cada ciclo. A fonte sobreviveu '
       'aos dois.', False),
     ], 'Bacteremia contínua pede olhar a valva'),

    painel('res2', 'A virada', 'Identificação e ecocardiograma', [
        ex('Hemoculturas', '**3 de 3 pares** com //Streptococcus gallolyticus// '
           '(antigo //S. bovis// biotipo I) · sensível à penicilina, CIM '
           '0,06 µg/mL', 'negativas', True),
        ex('Ecocardiograma transtorácico', '**Vegetação móvel de 12 mm** no '
           'folheto anterior mitral · insuficiência mitral importante · '
           'fração de ejeção 62%', '—', True),
        ex('Eletrocardiograma', 'Ritmo sinusal, 96 bpm · PR 180 ms', '—'),
    ], introducao='Com 44 horas de incubação sai a identificação. O '
                  'ecocardiograma é feito na mesma manhã.',
       nota='Endocardite infecciosa de valva mitral nativa, sobre cardiopatia '
            'reumática.'),

    pareamento('p5', 'Pergunta 5',
      'Pelos critérios de Duke-ISCVID de 2023, associe cada dado de Lúcia ao '
      'critério em que ele entra.', [
      par('Três de três pares com //S. gallolyticus//',
          'Critério maior microbiológico',
          'Agente típico em duas ou mais hemoculturas separadas.'),
      par('Vegetação móvel de 12 mm no folheto anterior mitral',
          'Critério maior de imagem',
          'Evidência direta de lesão endocárdica no ecocardiograma.'),
      par('Máculas indolores na planta e petéquias conjuntivais',
          'Critério menor vascular',
          'Lesões de Janeway e hemorragia conjuntival: êmbolos em pequenos '
          'vasos.'),
      par('Nódulo doloroso na polpa digital e fator reumatoide reagente',
          'Critério menor imunológico',
          'Nódulo de Osler e fator reumatoide são fenômenos de '
          'imunocomplexo.'),
      par('Insuficiência mitral moderada de origem reumática',
          'Critério menor de predisposição',
          'Regurgitação mais que discreta, de qualquer causa, predispõe.'),
      par('Baço palpável a 2 cm do rebordo',
          'Não entra nos critérios',
          'Esplenomegalia é comum, mas não pontua. Infarto ou abscesso '
          'esplênico em imagem, sim.'),
    ], opcoes=['Critério maior microbiológico', 'Critério maior de imagem',
               'Critério menor vascular', 'Critério menor imunológico',
               'Critério menor de predisposição', 'Critério menor de febre',
               'Não entra nos critérios'],
    titulo_resposta='Dois maiores fecham o diagnóstico',
    nota='Dois critérios maiores bastam para endocardite definida. A febre '
         'também soma como menor, mas nenhum item da lista era ela.'),

    Q('p6', 6,
      'O agente é //Streptococcus gallolyticus//. **Qual** investigação '
      'adicional é obrigatória?', [
      ('Colonoscopia', 'O agente se associa a adenoma e câncer colorretal. '
       'Ferritina de 18 e fezes escuras reforçam.', True),
      ('Endoscopia digestiva alta, e só ela', 'Pode entrar pelas fezes '
       'escuras, mas a associação do agente é com o cólon.', False),
      ('Sangue oculto nas fezes, e colonoscopia só se positivo',
       'Um resultado negativo não afasta adenoma. O agente já é a '
       'indicação.', False),
      ('Tomografia de abdome no lugar da colonoscopia', 'Perde adenomas '
       'pequenos e não permite biopsiar nem ressecar.', False),
      ('Tomografia de crânio', 'Sem sintoma neurológico, não é a '
       'investigação que o agente pede.', False),
      ('Biópsia de medula óssea', 'A anemia é ferropriva, com ferritina de '
       '18 e esfregaço sem blastos.', False),
     ], 'O agente manda olhar o cólon'),

    bifurcacao('b1', 'Decisão', 'O antibiótico',
      'Endocardite definida por estreptococo sensível à penicilina, em valva '
      'nativa. Como tratar?', [
      caminho('Penicilina cristalina ou ceftriaxona endovenosa por quatro '
              'semanas, com transesofágico e avaliação da cirurgia cardíaca',
              'tratamento',
              'É o esquema da valva nativa por estreptococo sensível, com a '
              'equipe de endocardite desde o início.'),
      caminho('Amoxicilina oral por duas semanas, em casa', 'oral',
              'Duas semanas de oral não é esquema de endocardite, e a '
              'vegetação é grande.'),
      caminho('Vancomicina e gentamicina empíricas até o transesofágico',
              'vanco',
              'O agente e a sensibilidade já são conhecidos. Vancomicina é '
              'inferior aos betalactâmicos para estreptococo sensível, e a '
              'gentamicina lesa o rim.'),
    ]),

    pg('oral', 'Dez dias depois',
       'Lúcia volta com febre de 38,6 °C e falta de ar ao deitar. As '
       'hemoculturas voltam a crescer //S. gallolyticus//. É internada para '
       'antibiótico endovenoso, com dez dias perdidos.',
       segue='tratamento'),

    pg('vanco', 'Quatro dias depois',
       'A febre cede devagar, mas a creatinina sobe de 1,3 para 2,4 mg/dL. A '
       'infectologia troca para ceftriaxona e suspende a gentamicina.',
       segue='tratamento'),

    pg('tratamento', 'Primeira semana de antibiótico',
       'Ceftriaxona 2 g ao dia. A febre some no quarto dia, e as hemoculturas '
       'de controle do terceiro dia são negativas.',
       'O transesofágico confirma a vegetação de 12 mm, móvel, e mostra '
       'perfuração do folheto anterior com regurgitação importante. Sem '
       'abscesso perivalvar.'),

    pg('piora', 'Sexto dia',
       'Na madrugada, Lúcia acorda sufocada. Crepitações até o terço médio, '
       'saturação de 88%, pressão de 100/60, frequência cardíaca de 124. A '
       'radiografia mostra congestão pulmonar. O eletrocardiograma segue com '
       'PR de 180 ms.'),

    Q('p7', 7,
      'Na endocardite de valva nativa esquerda, **quais quatro** situações '
      'indicam cirurgia precoce?', [
      ('Insuficiência cardíaca por regurgitação valvar grave',
       'É a indicação mais frequente e a mais urgente. A valva perfurada não '
       'se refaz com antibiótico.', True),
      ('Febre ainda presente no segundo dia de antibiótico',
       'A febre leva alguns dias para ceder. Não é indicação por si.', False),
      ('Abscesso perivalvar ou bloqueio atrioventricular novo',
       'Infecção que saiu da valva não se controla só com antibiótico.',
       True),
      ('Vegetação de 10 mm ou mais com evento embólico',
       'Vegetação grande que já embolizou tem alto risco de novo êmbolo.',
       True),
      ('Proteína C reativa ainda elevada no terceiro dia',
       'Cai devagar. Não indica cirurgia.', False),
      ('Hemoculturas positivas depois de uma semana de antibiótico '
       'adequado',
       'Infecção não controlada: foco que o antibiótico não alcança.', True),
      ('Sopro audível na alta',
       'A valva doente continua soprando. Não é indicação.', False),
      ('Hematúria da glomerulonefrite',
       'Melhora com o tratamento da infecção.', False),
     ], 'Coração que falha, infecção que escapa, êmbolo que se repete'),

    bifurcacao('b2', 'Decisão', 'A valva perfurada',
      'Edema pulmonar por insuficiência mitral aguda, no sexto dia de '
      'antibiótico. O que você faz?', [
      caminho('Cirurgia cardíaca nesta internação, em caráter de urgência',
              'cirurgia',
              'Insuficiência cardíaca por destruição valvar é a indicação '
              'clássica de cirurgia precoce.'),
      caminho('Diurético e vasodilatador, e cirurgia só depois de completar as '
              'quatro semanas', 'espera',
              'A valva não vai se refazer com antibiótico. O coração não '
              'aguenta quatro semanas de regurgitação aguda.'),
    ]),

    pg('espera', 'Nona noite',
       'Com furosemida e nitroglicerina, Lúcia melhora por dois dias. Na '
       'nona noite, entra em edema pulmonar de novo, agora com pressão de '
       '78/46 e lactato de 4,2. Vai para a UTI com noradrenalina.',
       segue='b3'),

    bifurcacao('b3', 'Decisão', 'Choque cardiogênico',
      'Qual a conduta?', [
      caminho('Cirurgia de emergência', 'cirurgia_tardia',
              'O risco cirúrgico subiu muito, mas sem cirurgia não há saída.'),
      caminho('Manter suporte clínico e esperar estabilizar para operar',
              'obito_pagina',
              'A estabilização não vem enquanto a valva estiver aberta.'),
    ]),

    pg('obito_pagina', 'Décimo dia',
       'Com duas drogas vasoativas e ventilação mecânica, a pressão não se '
       'sustenta. Lúcia evolui com disfunção de múltiplos órgãos.',
       segue='f_obito'),

    pg('cirurgia_tardia', 'Cirurgia de emergência',
       'A troca valvar mitral por prótese biológica é feita no décimo dia, '
       'sob choque. O pós-operatório tem lesão renal com três sessões de '
       'diálise e onze dias de UTI.',
       segue='colono'),

    pg('cirurgia', 'Cirurgia no sétimo dia',
       'A cirurgia encontra perfuração de 6 mm no folheto anterior, sem '
       'abscesso. A equipe faz **plástica mitral** com remendo de pericárdio, '
       'preservando a valva nativa. A cultura da vegetação é negativa, e o '
       'antibiótico segue contando a partir da primeira hemocultura '
       'negativa.',
       segue='colono'),

    pg('colono', 'A colonoscopia',
       'Na terceira semana de antibiótico, a colonoscopia encontra um '
       '**adenoma tubuloviloso de 25 mm no cólon sigmoide**, com displasia '
       'de alto grau, ressecado por inteiro. Margens livres.',
       'A anemia ferropriva de seis meses antes e as fezes escuras vinham '
       'dele. A anemia, sozinha, não tinha levado a nenhuma '
       'investigação; o agente levou.'),

    Q('p8', 8,
      'Sobre o tratamento e o seguimento de Lúcia, **quais quatro** '
      'afirmações estão corretas?', [
      ('A duração conta a partir da primeira hemocultura negativa',
       'Se a cultura da valva operada fosse positiva, a contagem recomeçaria '
       'da cirurgia.', True),
      ('A gentamicina deve ser associada em todo esquema de estreptococo',
       'Estreptococo sensível em valva nativa trata-se com betalactâmico '
       'isolado por quatro semanas.', False),
      ('Estável e com culturas negativas, pode completar com antibiótico '
       'oral ou em casa',
       'No ensaio POET, a passagem para via oral em pacientes estáveis não '
       'foi inferior.', True),
      ('Anticoagulação plena reduz a embolia da vegetação',
       'Não reduz, e aumenta o sangramento, inclusive cerebral.', False),
      ('Hemoculturas diárias até o fim do tratamento',
       'Colhe-se até a primeira negativa, e de novo se a febre voltar.',
       False),
      ('Avaliação odontológica completa antes da alta',
       'Tratar focos dentários reduz o risco de nova endocardite.', True),
      ('Passa a ter indicação de profilaxia antes de procedimento dentário '
       'que manipula a gengiva',
       'Endocardite prévia basta pela AHA de 2021, com ou sem '
       'material protético.', True),
      ('Ácido acetilsalicílico para prevenir embolia',
       'Sem benefício e com mais sangramento.', False),
     ], 'Contar certo, completar em casa quando der, e cuidar dos dentes'),

    pg('alta', 'Preparando a alta',
       'Lúcia completa o antibiótico com culturas negativas. O '
       'ecocardiograma de controle mostra a valva funcionando.',
       conforme=('b2', ['alta_cedo', 'f2'])),

    pg('alta_cedo', 'Última semana',
       'Ela já sobe um lance de escada sem parar e voltou a costurar no '
       'quarto do hospital.',
       conforme=('b1', ['f1', 'f2', 'f2'])),

    fim('f1', 'Alta com a valva preservada',
        'Plástica mitral funcionando, sem regurgitação significativa, '
        'fração de ejeção preservada. Seguimento da cardiologia e '
        'colonoscopia de vigilância em um ano.',
        'O antibiótico certo desde o início, a cirurgia no primeiro sinal de '
        'insuficiência cardíaca e o cólon investigado pelo agente: as três '
        'decisões contaram.', 'melhor'),

    fim('f2', 'Alta depois de um percurso mais longo',
        'Lúcia sai viva, com a infecção controlada, mas com mais dias de '
        'internação, função renal pior que a basal ou uma prótese no lugar '
        'da valva que poderia ter sido reparada.',
        'Esquema inadequado ou cirurgia adiada acrescentaram dano. A valva '
        'perfurada não se refaz enquanto o antibiótico corre.', 'medio'),

    fim('f_obito', 'Óbito no décimo primeiro dia',
        'Lúcia morre em choque cardiogênico refratário, com a infecção já '
        'controlada pelo antibiótico.',
        'A insuficiência mitral aguda por perfuração valvar é indicação de '
        'cirurgia de urgência. Esperar estabilizar um choque que só a '
        'cirurgia corrige levou ao óbito.', 'pior'),

    pagina('retrospectiva', 'Retrospectiva', '',
        tabela(['Momento', 'O dado', 'O que decidiu'], [
            ['Unidade básica', 'Febre que voltava depois de cada antibiótico curto',
             'Valvopata com febre prolongada colhe hemocultura antes de tratar'],
            ['Primeira rodada', 'Hematúria dismórfica, C3 baixo, fator reumatoide',
             'Imunocomplexo circulante antes de qualquer cultura'],
            ['Beira do leito', 'Estilhas, máculas plantares, nódulo digital, petéquia conjuntival',
             'Os pequenos sinais do título, que o primeiro exame não procurou'],
            ['Hemoculturas', '//S. gallolyticus//', 'O agente manda olhar o cólon'],
            ['Sexto dia', 'Edema pulmonar com folheto perfurado',
             'Cirurgia precoce, sem esperar o fim do antibiótico'],
            ['Alta', 'Endocardite prévia e material protético', 'Agora ela tem indicação de profilaxia'],
        ]),
        so_kicker=True),

    pg('referencias', 'Fontes e limites',
       'Paciente, valores e percursos são ficcionais. A cena de abertura é uma ilustração autoral gerada por inteligência artificial para este caso; não é fotografia nem documentação clínica.',
       'Fowler e cols. The 2023 Duke-ISCVID Criteria for Infective '
       'Endocarditis, Clin Infect Dis 2023. Delgado e cols. ESC Guidelines for '
       'the management of endocarditis, 2023. Iversen e cols. POET, N Engl J '
       'Med 2019. Wilson e cols. Prevention of Viridans Group Streptococcal '
       'Infective Endocarditis, AHA 2021. Haidar e Singh. Fever of Unknown '
       'Origin, N Engl J Med 2022.'),
]

REVISAO = []

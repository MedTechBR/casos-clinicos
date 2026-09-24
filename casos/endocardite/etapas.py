"""Endocardite infecciosa em valva mitral reumática por Streptococcus gallolyticus.

Alíquota → pergunta, no molde dos casos interativos do //New England//. Oito
perguntas, uma rodada de exames com gabarito e painel, um pareamento dos
sinais periféricos pelos critérios de Duke, e três decisões de conduta, uma
delas com óbito. A virada é o agente: ele manda olhar o cólon.
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
    capa(TITULO, fundo='', kicker='Caso interativo',
         selo='Paciente ficcional · procedência e créditos na última tela'),

    pg('historia', 'Apresentação',
       'Lúcia, 59 anos, costureira em Sobral, procura o ambulatório de clínica '
       'médica por cinco semanas de febre baixa no fim do dia, cansaço e '
       'sudorese à noite. Perdeu 5 kg. "Não tenho mais força nem para a '
       'máquina de costura."',
       'Na terceira semana, a unidade básica tratou como infecção urinária '
       'com ciprofloxacino por sete dias: a febre sumiu e voltou quatro dias '
       'depois. Na quarta semana recebeu amoxicilina por cinco dias por '
       '"sinusite". Nada mudou.'),

    pg('hda', 'História da doença atual',
       'A febre fica entre 37,8 e 38,3 °C. Há dores nas costas e nos joelhos, '
       'sem inchaço. Nos últimos dias notou "umas manchinhas vermelhas" nas '
       'plantas dos pés, que não doem, e dois caroços doloridos na ponta dos '
       'dedos, que sumiram em dois dias.',
       'Nega tosse, disúria e diarreia. Nos últimos três meses, as fezes às '
       'vezes vêm "mais escuras", e ela atribuiu ao sulfato ferroso que '
       'tomou por anemia.'),

    pg('antecedentes', 'Antecedentes',
       'Teve **febre reumática na infância**, com "sopro no coração" '
       'acompanhado no posto. Um ecocardiograma de três anos atrás mostrou '
       'insuficiência mitral moderada. Hipertensa, usa losartana.',
       'Não fez procedimentos dentários recentes. Não usa drogas injetáveis, '
       'não tem cateter nem prótese. Anemia ferropriva tratada há seis meses, '
       'sem investigação da causa.'),

    pagina('exame', 'Exame físico', '',
           vitais(('Temperatura', '38,1 °C', True), ('Pressão arterial', '132/70', False),
                  ('Frequência cardíaca', '98', False), ('Frequência respiratória', '18', False),
                  ('SpO₂ em ar ambiente', '96%', False)),
           topicos(('Estado geral', '**Palidez** moderada, emagrecida.'),
                   ('Cardiovascular', '**Sopro holossistólico mitral 3+/6** irradiado para a axila. '
                    'Sem terceira bulha.'),
                   ('Olhos', 'Duas **petéquias na conjuntiva** palpebral inferior esquerda.'),
                   ('Mãos e pés', '**Hemorragias em estilha** em três unhas. Máculas eritematosas '
                    'indolores nas plantas. Um nódulo doloroso na polpa do quarto dedo direito.'),
                   ('Abdome', '**Baço palpável** a 2 cm do rebordo.'),
                   ('Neurológico', 'Sem déficit focal.')),
           so_kicker=True),

    Q('p1', 1,
      'Febre baixa por cinco semanas, perda de peso e sopro mitral numa mulher '
      'com cardiopatia reumática, depois de dois antibióticos curtos. **Quais '
      'quatro** diagnósticos precisam ser considerados?', [
      ('Endocardite infecciosa', 'Valvopatia prévia, febre prolongada que '
       'cede e volta com antibiótico curto, esplenomegalia: é a hipótese '
       'principal.', True),
      ('Febre reumática aguda recorrente', 'Rara depois dos 40, sem artrite '
       'migratória verdadeira, sem coreia, sem cardite nova.', False),
      ('Linfoma', 'Febre, sudorese, perda de peso e baço palpável: não se '
       'fecha febre prolongada sem pensar nele.', True),
      ('Tuberculose extrapulmonar', 'Febre vespertina e emagrecimento no '
       'Brasil. Hemocultura e imagem ajudam a separar.', True),
      ('Doença de Still do adulto', 'Febre em picos acima de 39 °C, exantema '
       'que acompanha a febre e artrite: não é o padrão dela.', False),
      ('Mixoma atrial', 'Febre, sopro e fenômenos embólicos também são '
       'mixoma. O ecocardiograma separa.', True),
      ('Pielonefrite crônica', 'Explicaria febre, não o sopro, o baço e as '
       'lesões de pele.', False),
      ('Sinusite bacteriana', 'Não faz cinco semanas de febre com '
       'esplenomegalia.', False),
      ('Hipertireoidismo', 'Perda de peso e taquicardia, sim; febre '
       'persistente e petéquias, não.', False),
     ], 'Febre que volta sempre que o antibiótico acaba'),

    pareamento('p2', 'Pergunta 2',
      'Os sinais periféricos da endocardite entram como critérios menores de '
      'Duke. Associe cada achado ao tipo de fenômeno.', [
      par('Nódulo de Osler: doloroso, na polpa digital',
          'Fenômeno imunológico',
          'Vasculite por imunocomplexo. Dói porque é inflamação, não '
          'microabscesso.'),
      par('Lesão de Janeway: mácula indolor, na palma ou na planta',
          'Fenômeno vascular',
          'Microêmbolo séptico com microabscesso na derme. Não dói.'),
      par('Mancha de Roth: hemorragia retiniana com centro pálido',
          'Fenômeno imunológico',
          'Vasculite retiniana por imunocomplexo, no mesmo grupo de Osler.'),
      par('Hemorragia conjuntival em paciente com vegetação',
          'Fenômeno vascular',
          'Êmbolo em capilar conjuntival. Soma com Janeway e infartos.'),
      par('Glomerulonefrite com hematúria e fator reumatoide positivo',
          'Fenômeno imunológico',
          'Imunocomplexo circulante: o rim e o fator reumatoide contam como '
          'critério imunológico.'),
      par('Regurgitação nova por perfuração de folheto no ecocardiograma',
          'Destruição valvar (critério maior de imagem)',
          'Não é critério menor: é evidência direta de lesão endocárdica.'),
    ], opcoes=['Fenômeno imunológico', 'Fenômeno vascular',
               'Destruição valvar (critério maior de imagem)',
               'Reação ao antibiótico'],
    titulo_resposta='Dói é imunológico; não dói é embólico',
    nota='A opção que sobrou, reação ao antibiótico, não explica nenhum '
         'desses achados.'),

    Q('ex1', 3,
      'Suspeita de endocardite. **Quais quatro** condutas diagnósticas são as '
      'mais apropriadas agora?', [
      ('Três pares de hemoculturas de punções diferentes, antes do antibiótico',
       'Bacteremia contínua é a marca da endocardite. Três pares separados, '
       'antes de qualquer dose, dão o agente e a persistência.', True),
      ('Iniciar antibiótico empírico antes de colher, pela febre',
       'Ela está estável. Na endocardite subaguda, colher antes vale mais '
       'que ganhar horas.', False),
      ('Ecocardiograma transtorácico, seguido de transesofágico',
       'O transtorácico vê vegetações grandes; o transesofágico vê as '
       'pequenas e as complicações perivalvares.', True),
      ('PET-CT como exame inicial',
       'Tem papel na endocardite de prótese e em focos a distância. Não '
       'substitui o ecocardiograma na valva nativa.', False),
      ('Hemograma, função renal e urina com sedimento',
       'Anemia, lesão renal e hematúria de glomerulonefrite entram na '
       'gravidade e nos critérios.', True),
      ('Eletrocardiograma', 'Um PR que se alarga no seguimento é abscesso '
       'perivalvar até prova em contrário. O basal é a referência.', True),
      ('Sorologias para Bartonella e Coxiella já na chegada',
       'Entram na endocardite com cultura negativa, que ainda não é o caso.',
       False),
      ('Procalcitonina para decidir se trata',
       'Não confirma nem exclui endocardite.', False),
      ('Tomografia de crânio sem sintoma neurológico',
       'Rastreio de êmbolo cerebral assintomático não é rotina antes do '
       'diagnóstico.', False),
     ], 'Colher antes, olhar a valva, medir o estrago'),

    painel('res1', 'Resultados', 'O que a equipe pediu', [
        ex('Hemoculturas', '**3 de 3 pares positivos** para //Streptococcus '
           'gallolyticus// (antigo //S. bovis// biotipo I) · sensível à '
           'penicilina, CIM 0,06 µg/mL', 'negativas', True),
        ex('Hemoglobina', '9,8 g/dL · VCM 76 fL', '12–16 g/dL', True),
        ex('Ferritina', '18 ng/mL', '15–150 ng/mL', True),
        ex('Leucócitos / plaquetas', '11.200 / 180.000 por mm³', '—'),
        ex('VHS / proteína C reativa', '86 mm/h / 74 mg/L', 'até 20 / 5', True),
        ex('Creatinina', '1,3 mg/dL', '0,6–1,1 mg/dL', True),
        ex('Urina', 'Hematúria de 15 por campo, proteinúria 1+', 'normal', True),
        ex('Fator reumatoide', 'Reagente, 64 UI/mL', 'até 14 UI/mL', True),
        ex('Eletrocardiograma', 'Ritmo sinusal, 98 bpm · PR 180 ms', '—'),
        ex('Ecocardiograma transtorácico', '**Vegetação de 12 mm** no folheto '
           'anterior mitral · insuficiência mitral importante · fração de '
           'ejeção 62%', '—', True),
    ], introducao='Hemoculturas colhidas em três punções, com uma hora de intervalo, antes de qualquer antibiótico.'),

    pergunta('p4', 'Pergunta 4',
      'Três hemoculturas com //S. gallolyticus// e vegetação de 12 mm na '
      'mitral. Pelos critérios de Duke-ISCVID de 2023, qual a classificação?', [
      alt('Endocardite definida',
          'Dois critérios maiores: microrganismo típico em hemoculturas '
          'repetidas e evidência de imagem de vegetação. Os menores só '
          'reforçam.', certa=True),
      alt('Endocardite possível, até o ecocardiograma transesofágico',
          'O transesofágico vai detalhar complicações, mas o diagnóstico já '
          'está fechado pelo transtorácico.'),
      alt('Endocardite rejeitada, porque ela recebeu antibiótico antes',
          'O antibiótico prévio reduz a positividade das culturas; aqui elas '
          'vieram positivas assim mesmo.'),
      alt('Endocardite possível, porque falta o critério patológico',
          'Patologia só existe quando se opera ou na necropsia. A '
          'classificação clínica não depende dela.'),
      alt('Bacteremia sem endocardite, por ser um estreptococo',
          'O //S. gallolyticus// está entre os agentes típicos de endocardite '
          'nos critérios.'),
    ], titulo_resposta='Dois maiores fecham'),

    pergunta('p5', 'Pergunta 5',
      'O agente é //Streptococcus gallolyticus//. Que investigação adicional '
      'é **obrigatória**?', [
      alt('Colonoscopia',
          'O //S. gallolyticus// tem associação forte com adenoma e '
          'adenocarcinoma colorretal. A anemia ferropriva não investigada e '
          'as fezes escuras dela ganham outro sentido.', certa=True),
      alt('Endoscopia digestiva alta, e só ela',
          'Pode entrar, mas a associação do agente é com o cólon.'),
      alt('Tomografia de crânio',
          'Sem sintoma neurológico, não é a investigação que o agente pede.'),
      alt('Biópsia de medula óssea',
          'A anemia é ferropriva, com ferritina de 18.'),
      alt('Pesquisa de sangue oculto nas fezes, e colonoscopia só se positiva',
          'Um resultado negativo não afasta a lesão. O agente já é a '
          'indicação.'),
    ], titulo_resposta='O agente manda olhar o cólon'),

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
       '**perfuração do folheto anterior** com regurgitação importante. Sem '
       'abscesso perivalvar.'),

    pg('piora', 'Sexto dia',
       'Na madrugada, Lúcia acorda sufocada. Crepitações até o terço médio, '
       'saturação de 88%, pressão de 100/60, frequência cardíaca de 124. A '
       'radiografia mostra congestão pulmonar. O eletrocardiograma segue com '
       'PR de 180 ms.'),

    Q('p6', 6,
      'Na endocardite de valva nativa esquerda, **quais quatro** situações '
      'indicam cirurgia precoce?', [
      ('Insuficiência cardíaca por regurgitação valvar grave',
       'É a indicação mais frequente e a mais urgente. Esperar o fim do '
       'antibiótico com a valva perfurada mata.', True),
      ('Febre ainda presente no segundo dia de antibiótico',
       'A febre leva alguns dias para ceder. Não é indicação por si.', False),
      ('Abscesso perivalvar ou bloqueio atrioventricular novo',
       'Infecção que saiu da valva não se controla só com antibiótico.',
       True),
      ('Vegetação acima de 10 mm com evento embólico',
       'Vegetação grande que já embolizou tem alto risco de novo êmbolo. A '
       'cirurgia precoce reduz a embolia.', True),
      ('Proteína C reativa ainda elevada no terceiro dia',
       'Cai devagar. Não indica cirurgia.', False),
      ('Hemoculturas persistentemente positivas depois de uma semana de '
       'antibiótico adequado',
       'Infecção não controlada: foco que o antibiótico não alcança.', True),
      ('Sopro audível na alta',
       'A valva doente continua soprando. Não é indicação.', False),
      ('Hematúria de glomerulonefrite',
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
       'A anemia ferropriva de seis meses atrás e as fezes escuras tinham '
       'um endereço. Encontrá-lo foi mérito do agente, não da anemia.'),

    Q('p7', 7,
      'Pelas recomendações da AHA, **quais três** pacientes têm indicação de '
      'profilaxia antibiótica antes de procedimento dentário que manipula a '
      'gengiva?', [
      ('Portador de prótese valvar ou de material protético em reparo valvar',
       'Maior risco de endocardite e de desfecho grave. Lúcia, agora com '
       'remendo ou prótese, entra aqui.', True),
      ('Portador de prolapso da valva mitral sem regurgitação',
       'Risco baixo; a profilaxia não é indicada.', False),
      ('Paciente com endocardite infecciosa prévia',
       'Quem já teve, tem risco alto de ter de novo.', True),
      ('Paciente com stent coronário',
       'Não há indicação.', False),
      ('Cardiopatia congênita cianótica não corrigida',
       'Está entre as condições de risco mais alto.', True),
      ('Portador de marca-passo definitivo',
       'Não há indicação para procedimento dentário.', False),
      ('Valvopatia reumática sem prótese nem endocardite prévia',
       'Pelas recomendações atuais, não. Antes do episódio, Lúcia não '
       'tinha indicação.', False),
     ], 'Prótese, endocardite prévia e congênita cianótica'),

    Q('p8', 8,
      'Sobre o tratamento de Lúcia, **quais três** afirmações estão '
      'corretas?', [
      ('A duração conta a partir da primeira hemocultura negativa',
       'E, se a cultura da valva operada for positiva, recomeça da cirurgia.',
       True),
      ('A gentamicina deve ser associada em todo esquema de estreptococo',
       'Estreptococo sensível em valva nativa trata-se com betalactâmico '
       'isolado por quatro semanas.', False),
      ('Paciente estável, com culturas negativas, pode completar com '
       'antibiótico oral ou em casa',
       'O ensaio POET mostrou que a passagem para via oral, em pacientes '
       'estáveis, não foi inferior.', True),
      ('Anticoagulação plena reduz a embolia da vegetação',
       'Não reduz, e aumenta o sangramento, inclusive cerebral.', False),
      ('Hemoculturas diárias até o fim do tratamento',
       'Colhe-se até a primeira negativa, e de novo se voltar a febre.',
       False),
      ('Avaliação odontológica completa antes da alta',
       'Tratar focos dentários reduz o risco de nova endocardite.', True),
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
        'perfurada não espera o fim do antibiótico.', 'medio'),

    fim('f_obito', 'Óbito no décimo primeiro dia',
        'Lúcia morre em choque cardiogênico refratário, com a infecção já '
        'controlada pelo antibiótico.',
        'A insuficiência mitral aguda por perfuração valvar é indicação de '
        'cirurgia de urgência. Esperar estabilizar um choque que só a '
        'cirurgia corrige foi a decisão fatal.', 'pior'),

    pagina('retrospectiva', 'Retrospectiva', '',
        tabela(['Momento', 'O dado', 'O que decidiu'], [
            ['Unidade básica', 'Febre que voltava depois de cada antibiótico curto',
             'Valvopata com febre prolongada colhe hemocultura antes de tratar'],
            ['Exame', 'Estilhas, Janeway, Osler, baço', 'Os pequenos sinais do título'],
            ['Hemoculturas', '//S. gallolyticus//', 'O agente manda olhar o cólon'],
            ['Sexto dia', 'Edema pulmonar com folheto perfurado',
             'Cirurgia precoce, sem esperar o fim do antibiótico'],
            ['Alta', 'Endocardite prévia e material protético', 'Agora ela tem indicação de profilaxia'],
        ]),
        so_kicker=True),

    pg('referencias', 'Fontes e limites',
       'Paciente, valores e percursos são ficcionais.',
       'Fowler e cols. The 2023 Duke-ISCVID Criteria for Infective '
       'Endocarditis, Clin Infect Dis 2023. Delgado e cols. ESC Guidelines for '
       'the management of endocarditis, 2023. Iversen e cols. POET, N Engl J '
       'Med 2019. Wilson e cols. Prevention of Viridans Group Streptococcal '
       'Infective Endocarditis, AHA 2021.'),
]

REVISAO = []

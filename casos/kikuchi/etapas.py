"""Abordagem sindrômica da linfonodomegalia, revisada em 21/10/2026.

Apresentação regional, hipóteses amplas, investigação dirigida, reavaliação
e tecido antes de nomear a doença rara. Paciente e trajetórias ficcionais.
Layout e motor de apresentação preservados.
"""
from pathlib import Path

from motor.estudo_imagem import estudo
from motor.etapas import (alt, bifurcacao, caminho, capa, desfecho, op, p,
                          pagina, painel, par, pareamento, pergunta, pontos,
                          topicos, vitais, tabela)

TITULO = 'O que ficou no pescoço'
RODAPE = 'Paciente ficcional · evoluções simuladas para ensino'
COR = '#ea580c'
IMG = Path(__file__).parent / 'img'
BANCO = []
MOLDE = 'nejm'
CENA = 'cena.png'


def credito_meta(meta):
    import json
    m = json.loads(Path(meta).read_text())
    return m['autor'] + ' · Wikimedia Commons · ' + m['licenca'] + ' · setas adicionadas'


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


def fim(k, titulo, texto, porque, qualidade, fecho='retrospectiva'):
    return desfecho(k, titulo, p(texto), qualidade=qualidade, porque=porque,
                    fecho=fecho)


ETAPAS = [
    capa(TITULO, fundo=CENA, kicker='Caso interativo',
         selo='Paciente ficcional · procedência e créditos na última tela'),

    pg('historia', 'Apresentação',
       'Bianca, 27 anos, professora do ensino fundamental, procura o '
       'ambulatório por febre no fim da tarde há 12 dias e um caroço doloroso '
       'no lado esquerdo do pescoço. Tudo começou com dor de garganta, que '
       'passou; o caroço ficou.',
       'No quarto dia foi a uma unidade de pronto atendimento e saiu com '
       'amoxicilina por sete dias, já concluída, sem efeito sobre a febre. '
       'Nas últimas três noites acordou com a camiseta molhada de suor e '
       'perdeu 2 kg no mês, por falta de apetite.',
       'Nega tosse, falta de ar, dor de dente, lesões na pele, dor nas '
       'articulações, feridas na boca, disúria e diarreia.'),

    pagina('ficha', 'Ficha do paciente', '',
           topicos(('Antecedentes', 'Nenhuma doença crônica, nenhuma internação. '
                    'BCG na infância. Último teste de HIV há três anos, não '
                    'reagente.'),
                   ('Medicações', 'Anticoncepcional oral combinado há quatro anos. '
                    'Paracetamol 750 mg quando tem febre. Amoxicilina 500 mg de '
                    '8 em 8 horas, sete dias, terminada há dois dias.'),
                   ('Hábitos', 'Não fuma. Bebe vinho em encontros, raramente. '
                    'Nega drogas. Corre duas vezes por semana, parou há dez dias.'),
                   ('Vida social', 'Mora em São Paulo com o companheiro, parceiro '
                    'único há cinco anos, e um gato adulto; não lembra de '
                    'arranhadura. Não viajou nos últimos seis meses. Duas '
                    'crianças da turma dela faltaram com febre no mês passado.'),
                   ('Família', 'Mãe com hipotireoidismo. Pai hipertenso. Sem câncer, tuberculose ou doença '
                    'reumatológica conhecida na família.')),
           so_kicker=True),

    pagina('exame', 'Exame físico', '',
           vitais(('Temperatura', '38,1 °C', True),
                  ('Pressão arterial', '112/70', False),
                  ('Frequência cardíaca', '98', False),
                  ('Frequência respiratória', '16', False),
                  ('SpO₂ em ar ambiente', '98%', False),
                  ('Peso', '58 kg', False)),
           topicos(('Estado geral', 'Alerta, hidratada, corada, sem desconforto '
                    'respiratório.'),
                   ('Cabeça e pescoço', 'Orofaringe sem exsudato, dentes sem cárie '
                    'visível, couro cabeludo sem lesões. Três linfonodos na cadeia '
                    'cervical posterior esquerda, móveis, elásticos e dolorosos, o '
                    'maior com cerca de 2 cm, sem rubor e sem flutuação. Tireoide e '
                    'parótidas normais. Fossas supraclaviculares livres.'),
                   ('Outras cadeias', 'Sem linfonodos axilares, epitrocleares ou '
                    'inguinais palpáveis.'),
                   ('Tórax e abdome', 'Ausculta cardíaca e pulmonar normais. Fígado '
                    'no rebordo, baço não palpável.'),
                   ('Pele e articulações', 'Sem exantema, sem úlceras orais, sem '
                    'sinovite.')),
           so_kicker=True),

    Q('p1', 1,
      'Bianca tem linfonodos aumentados no pescoço há 12 dias, com febre e perda de peso. Está estável, e o exame não encontrou infecção na garganta, nos dentes ou no couro cabeludo que explique esse aumento. Qual plano inicial é mais adequado?', [
      ('Observar por quatro semanas, com exames apenas se o linfonodo persistir', False),
      ('Colher hemograma e selecionar outros exames conforme as hipóteses, avaliar o pescoço e marcar retorno próximo', True),
      ('Trocar a amoxicilina por cobertura mais ampla e usar a resposta para decidir os exames', False),
      ('Solicitar PET-CT para selecionar as hipóteses que merecem investigação', False),
      ], [
      ('O problema inicial', 'É uma linfonodomegalia localizada com sintomas sistêmicos. A estabilidade permite investigar ambulatorialmente, mas febre, perda ponderal e ausência de uma infecção local identificável tornam inadequada a observação sem plano.'),
      ('O que procurar', 'Examinar os linfonodos de outras regiões e procurar infecções na garganta, boca, dentes, pele e couro cabeludo. Perguntar sobre contatos, animais, viagens e medicamentos. Hemograma e testes selecionados pela história ajudam a decidir o próximo passo; ultrassom avalia estrutura e coleção, sem substituir seguimento.'),
      ('Reavaliar', 'Marcar retorno em uma semana, antecipado diante de piora, crescimento rápido, dificuldade para engolir ou respirar. O intervalo muda conforme gravidade; não existe tamanho ou prazo isolado que resolva todos os casos.'),
      ]),

    painel('res1', 'Primeiros exames', 'Sangue', [
        ex('Hemoglobina / VCM', '11,7 g/dL / 86 fL', 'Hb 12–16 g/dL · VCM 80–100 fL', True),
        ex('Leucócitos', '2.900/mm³', '4.000–11.000/mm³', True),
        ex('Neutrófilos / linfócitos / monócitos', '1.450 / 1.100 / 260 por mm³',
           'N 1.800–7.500 · L 1.000–4.000', True),
        ex('Esfregaço', 'Linfócitos reativos ocasionais, 4% · sem blastos',
           '—'),
        ex('Plaquetas', '188.000/mm³', '150.000–450.000/mm³'),
        ex('VHS / proteína C reativa', '46 mm/h / 24 mg/L', 'até 20 mm/h · até 5 mg/L', True),
        ex('Desidrogenase láctica', '330 U/L', '120–250 U/L', True),
    ], introducao='Colhidos na primeira consulta, no mesmo dia da '
                  'ultrassonografia do pescoço e da radiografia de tórax.'),

    painel('res1b', 'Primeiros exames', 'Bioquímica e urina', [
        ex('AST / ALT', '42 / 47 U/L', 'até 32 / 33 U/L', True),
        ex('Fosfatase alcalina / GGT', '88 / 30 U/L', 'até 104 / 40 U/L'),
        ex('Creatinina', '0,7 mg/dL', '0,5–1,1 mg/dL'),
        ex('Urina tipo 1', 'Densidade 1.018 · sem proteína, hemácias ou leucócitos', 'normal'),
    ]),

    Q('p2', 2,
      'A faringite inicial, a adenopatia cervical e a leucopenia permitem hipóteses diferentes. Bianca está estável, sem blastos, sem outras cadeias palpáveis e sem foco bacteriano. Qual investigação tem maior rendimento inicial?', [
      ('Tomografia de tórax e abdome e avaliação medular para pesquisar doença hematológica', False),
      ('FAN, anti-DNA e complemento para priorizar uma causa autoimune', False),
      ('Sorologias dirigidas à síndrome mononucleose-símile e teste para HIV, com reavaliação próxima', True),
      ('Hemoculturas e novo antibiótico oral para uma infecção cervical parcialmente tratada', False),
      ], [
      ('Prioridade', 'A cronologia e a faringite tornam razoável investigar primeiro infecções sistêmicas compatíveis. A seleção dos testes depende das exposições, e a avaliação não termina na coleta.'),
      ('Alternativas', 'Doença hematológica e autoimune permanecem possíveis, mas não há dados que justifiquem priorizar medula ou um painel autoimune amplo agora. Não se demonstrou foco para outro antibiótico.'),
      ('Reavaliação', 'Se os testes não sustentarem a hipótese e houver crescimento, a estratégia muda. Leucopenia e LDH isoladas não escolhem uma causa, e ausência de blastos não exclui linfoma.'),
      ]),

    estudo('us_cervical', 'Ultrassonografia do pescoço',
           'Pedida na primeira consulta para avaliar os linfonodos palpados. '
           'Neste corte, observe um linfonodo. Descreva a '
           'forma do linfonodo e o que há no centro dele antes de abrir os '
           'achados.',
           IMG / 'us_linfonodo_cervical.jpg',
           'Ultrassonografia com Doppler colorido de outro paciente · comparação didática.',
           credito_meta(IMG / 'us_linfonodo_cervical.jpg.json'),
        [
         ((442, 215), (330, 150), '**Córtex** hipoecoico, regular, em volta de todo o linfonodo.', 12),
         ((386, 312), (140, 250), '**Hilo** central ecogênico, com o vaso hilar se ramificando a partir dele.', -12),
         ((643, 529), (850, 650), '**Vaso** adjacente, fora do linfonodo, com fluxo ao Doppler.', 12),
        ],
        ['No corte apresentado, observa-se um linfonodo ovalado, com córtex '
         'hipoecoico, hilo central ecogênico preservado e vascularização hilar '
         'ao Doppler. Não há área de liquefação visível neste linfonodo. '
         'A imagem não apresenta medidas assinaladas.',
         'Forma oval, hilo preservado e fluxo hilar são o aspecto de um '
         'linfonodo reacional. O ultrassom tranquiliza, mas não afasta linfoma '
         'nem tuberculose no início.']),

    estudo('rx_torax', 'Radiografia de tórax',
           'Pedida na mesma consulta pela febre com sudorese e perda de peso: '
           'procurar linfonodos no mediastino e lesão no pulmão.',
           IMG / 'rx_torax_normal.jpg',
           'Radiografia de outra pessoa · comparação didática.',
           credito_meta(IMG / 'rx_torax_normal.jpg.json'),
        [
         ((350, 500), (170, 450), '**Hilo direito** de tamanho e densidade normais.', 12),
         ((575, 385), (720, 290), '**Botão aórtico** e mediastino superior de largura normal.', -12),
         ((665, 500), (850, 560), '**Hilo esquerdo** sem massa.', 12),
        ],
        ['Pulmões sem opacidades, mediastino e hilos normais, seios '
         'costofrênicos livres.',
         'Não há adenomegalia mediastinal visível nem lesão pulmonar que '
         'aponte tuberculose ou linfoma. A radiografia simples não vê '
         'linfonodos pequenos.']),

    pg('hipotese', 'Investigação dirigida',
       'Faringite no início, febre e linfonodos cervicais posteriores tornam infecções mononucleose-símile uma linha inicial plausível. O exame não mostrou foco dentário, otológico ou cutâneo nem coleção. Não há indicação de repetir antibiótico apenas porque o primeiro falhou.',
       'A equipe solicita sorologia para EBV, CMV e toxoplasmose e teste de quarta geração para HIV. Revê exposição sexual recente, contato com gatos e viagens; não há um achado epidemiológico que defina sozinho a investigação.',
       'Bianca mantém sintomáticos e retorna em uma semana. Infecção local, infecção sistêmica, doença inflamatória e neoplasia permanecem no diferencial.'),

    painel('res2', 'Retorno', 'Sorologias', [
        ex('EBV IgM (anti-VCA)', 'Não reagente', 'não reagente'),
        ex('EBV IgG (anti-VCA)', 'Reagente', '—', True),
        ex('EBV: marcador complementar (EBNA IgG)', 'Reagente', '—', True),
        ex('CMV: IgM / IgG', 'Não reagente / reagente', '—', True),
        ex('Toxoplasmose: IgM / IgG', 'Não reagente / não reagente', 'não reagente'),
        ex('HIV, teste de quarta geração', 'Não reagente', 'não reagente'),
        ex('VDRL', 'Não reagente', 'não reagente'),
    ], introducao='Colhidas na primeira consulta, no 12.º dia de febre.'),

    Q('sorologias_leitura', 3,
      'EBV IgG e o marcador complementar EBNA IgG são reagentes; EBV IgM é não reagente. A febre persiste. Qual conclusão é mais bem sustentada?', [
      ('O padrão favorece infecção passada por EBV e não explica o episódio atual', True),
      ('O VCA IgG reagente confirma que a febre atual é mononucleose', False),
      ('A presença de EBNA indica reativação sintomática que requer antiviral', False),
      ('As sorologias negativas excluem todas as causas infecciosas da adenopatia', False),
      ], [
      ('O que os testes medem', 'EBV é o vírus Epstein–Barr. Anti-VCA mede anticorpos contra o capsídeo, a estrutura que envolve o material genético viral. A IgM costuma surgir cedo e desaparecer em 4–6 semanas; a IgG aparece na fase aguda e geralmente persiste por toda a vida.'),
      ('Marcador complementar', 'EBNA é um antígeno nuclear do vírus. O EBNA IgG costuma aparecer 2–4 meses após o início dos sintomas e persistir. Por isso, IgG positiva isolada não data a infecção.'),
      ('Neste caso', 'IgM não reagente, com VCA IgG e EBNA IgG reagentes, favorece infecção passada. Esse padrão não sustenta mononucleose aguda como explicação da febre atual; a leitura depende da cronologia e do método. Fonte: CDC, Laboratory Testing for EBV.'),
      ('Outras infecções', 'CMV IgG isolada não demonstra doença aguda. Resultados negativos para HIV e toxoplasmose reduzem a probabilidade, mas precisam ser interpretados com a janela e a suspeita clínica; nova exposição pode justificar repetição ou outro método.'),
      ('Consequência', 'A hipótese inicial perdeu sustentação. O próximo passo depende do novo exame físico e da evolução, não de pedir indiscriminadamente mais sorologias.'),
      ]),

    pg('evolucao1', 'Terceira semana',
       'No retorno, no 19.º dia, a febre chega a 38,8 °C. O maior linfonodo mede 2,8 cm, e surgiram dois menores na cadeia cervical posterior direita. Perdeu mais 1 kg. Leucócitos: 2.500/mm³; neutrófilos: 1.300/mm³; LDH: 360 U/L.',
       'Continuam sem linfonodos palpáveis em outras regiões, lesões cutâneas ou sinovite. O comprometimento cervical bilateral continua regional; não equivale, por si, a adenopatia generalizada.',
       'A prova tuberculínica solicitada na avaliação dirigida mede 14 mm. Bianca recebeu BCG na infância e não refere contato conhecido com tuberculose. A equipe considera tuberculose ganglionar, mas mantém doença linfoproliferativa e causas inflamatórias.'),

    bifurcacao('b1', 'Decisão', 'O linfonodo de 2,8 cm',
      'Três semanas de febre, prova tuberculínica de 14 mm e linfonodos '
      'crescendo. Bianca está estável e quer uma resposta. O que você faz?', [
      caminho('Biópsia excisional nesta semana, com parte a fresco', 'tecido',
              'Uma amostra responde às duas hipóteses: arquitetura para '
              'linfoma, cultura e teste molecular rápido para tuberculose (TRM-TB).'),
      caminho('Iniciar o esquema básico para tuberculose sem tecido', 'ripe',
              'A prova tuberculínica mede infecção, não doença. Seis meses de '
              'tratamento sem confirmação expõem a hepatotoxicidade e podem '
              'mascarar outra causa.'),
      caminho('Prednisona 40 mg ao dia pela febre persistente', 'corticoide',
              'Alivia a febre, e o alívio parece resposta. Trata sem '
              'diagnóstico e pode dificultar a interpretação da amostra.'),
    ]),

    pg('ripe', 'Três semanas de esquema básico',
       'Rifampicina, isoniazida, pirazinamida e etambutol em comprimidos '
       'combinados. A febre cede na segunda semana, e a equipe anota boa '
       'resposta. Na terceira, Bianca tem náuseas e vômitos, com ALT de 310 '
       'U/L e bilirrubina normal.',
       'ALT acima de três vezes o limite com sintomas manda suspender o '
       'esquema, e ele é suspenso. O maior linfonodo não mudou de tamanho. Sem '
       'tecido, ninguém sabe se a febre cedeu pelo remédio ou sozinha. A '
       'equipe marca a biópsia e avisa o patologista das três semanas de '
       'tratamento, que reduzem a chance de a cultura crescer.',
       segue='tecido'),

    pg('corticoide', 'Duas semanas de prednisona',
       'A febre cede em quatro dias e o linfonodo dói menos. Na redução da '
       'dose, a febre volta e o linfonodo cresce de novo. Bianca pergunta se '
       'a melhora confirma uma doença inflamatória.',
       'Ainda não há diagnóstico. Se for tuberculose, o corticoide sem '
       'tratamento a agrava; se for linfoma, pode reduzir a celularidade a '
       'ponto de deixar a biópsia inconclusiva.'),

    bifurcacao('resgate', 'Decisão', 'A febre voltou',
      'O alívio sob prednisona foi transitório. Qual é o próximo passo?', [
      caminho('Reduzir o corticoide e marcar a biópsia, avisando o '
              'patologista', 'tecido',
              'A resposta foi inespecífica. O patologista precisa saber do '
              'corticoide para ler a lâmina.'),
      caminho('Repetir o ciclo que havia aliviado a febre', 'novo_ciclo',
              'Mais um ciclo empurra o diagnóstico sem tratar nenhuma causa '
              'demonstrada.'),
    ]),

    pg('novo_ciclo', 'Mais duas semanas',
       'A febre melhora de novo e volta na redução. Bianca está afastada do '
       'trabalho há um mês, dorme mal e ganhou 4 kg. O linfonodo mede 3 cm. '
       'A equipe abandona os ciclos, reduz a prednisona e marca a biópsia.',
       segue='tecido'),

    pg('tecido', 'A biópsia',
       'Bianca é encaminhada ao cirurgião de cabeça e pescoço. Antes de '
       'marcar a cirurgia, ele combina com a equipe como colher e enviar o '
       'material, porque as hipóteses em aberto pedem coisas diferentes da '
       'mesma amostra.'),

    Q('p4', 5,
      'O ultrassom descreveu linfonodos ovalados com hilo preservado. Mesmo assim, a equipe indicou biópsia. Qual dado tem maior peso para essa decisão?', [
      ('A persistência da febre com perda de peso e crescimento dos linfonodos, sem causa esclarecida', True),
      ('A dor nos linfonodos, que favorece acometimento neoplásico em relação ao infeccioso', False),
      ('A prova tuberculínica de 14 mm, que define a causa da adenopatia e exige confirmação histológica', False),
      ('A leucopenia associada à LDH elevada, combinação que permite priorizar linfoma como diagnóstico', False),
      ], [
      ('Evolução clínica', 'O que muda a conduta é a combinação de progressão, sintomas sistêmicos e investigação inicial sem explicação suficiente. Esses dados justificam obter tecido, mas ainda não escolhem uma doença.'),
      ('Limites dos exames', 'Aspecto reacional ao ultrassom não encerra a investigação. Dor, leucopenia e LDH elevada são inespecíficas; prova tuberculínica positiva não confirma tuberculose ganglionar.'),
      ('Objetivo da biópsia', 'A análise do linfonodo permite comparar causas infecciosas, inflamatórias e neoplásicas. O clínico comunica essas hipóteses à equipe que realizará o procedimento e ao patologista.'),
      ]),

    pg('tecido2', 'Amostra do linfonodo',
       'O cirurgião retira o linfonodo cervical mais representativo. A amostra é distribuída conforme o plano acordado: histologia e imuno-histoquímica, citometria de fluxo e investigação microbiológica.',
       'A citometria não identifica população clonal no material analisado; o TRM-TB não detecta micobactéria. Esses resultados, isoladamente, não excluem linfoma nem tuberculose ganglionar. O patologista pede correlação com a arquitetura e a microbiologia.'),

    estudo('arquitetura', 'Biópsia: pequeno aumento',
           'Lâmina de referência de outro paciente, com o padrão que o '
           'patologista mostra na de Bianca. Descreva a distribuição das áreas '
           'claras e das áreas celulares antes de abrir os achados.',
           IMG / 'linfonodo_baixo.jpg',
           'Hematoxilina-eosina, pequeno aumento · outro paciente.',
           credito_meta(IMG / 'linfonodo_baixo.jpg.json'),
        [
         ((560, 560), (820, 430), '**Área pálida e eosinofílica**, ampla e mal delimitada, que substitui o tecido linfoide.', 12),
         ((200, 520), (90, 390), '**Ilha de linfócitos** residuais, azul-escura, entre as áreas pálidas.', 12),
         ((450, 185), (330, 70), '**Cápsula** com gordura perinodal: o contorno do linfonodo está preservado.', -12),
        ],
        ['Arquitetura parcialmente apagada por áreas confluentes e pálidas, com '
         'cápsula preservada, sem granulomas e sem população linfoide '
         'monomórfica.',
         'O que ocupa as áreas pálidas só se define no grande aumento.']),

    estudo('celulas', 'Biópsia: grande aumento',
           'A mesma lâmina de referência em grande aumento. Que células povoam '
           'a área pálida, e que célula chama a atenção pela ausência?',
           IMG / 'linfonodo_alto.jpg',
           'Hematoxilina-eosina, grande aumento · outro paciente.',
           credito_meta(IMG / 'linfonodo_alto.jpg.json'),
        [
         ((325, 452), (150, 330), '**Cariorrexe**: fragmentos nucleares escuros, pequenos e irregulares, espalhados pela área pálida.', 12),
         ((655, 518), (860, 430), '**Histiócito** de núcleo claro, ovalado ou reniforme, com citoplasma pálido.', -12),
         ((845, 345), (760, 250), 'Fundo **eosinofílico e granular** de necrose, sem neutrófilos.', -12),
        ],
        ['Necrose paracortical com abundante cariorrexe e histiócitos, sem '
         'neutrófilos e sem granulomas.',
         'Não apresenta o padrão granulomatoso caseoso típico. Isso enfraquece, mas não exclui tuberculose; a conclusão depende da amostra completa e da microbiologia.']),

    pareamento('p5', 'Pergunta 4',
      'Necrose com cariorrexe, sem neutrófilos e sem granulomas. Associe cada '
      'achado histológico ao diagnóstico que ele sugere.', [
      par('Necrose paracortical com cariorrexe, histiócitos em crescente e '
          'ausência de neutrófilos',
          'Doença de Kikuchi–Fujimoto',
          'É o padrão de Bianca. Histiócitos em crescente sem neutrófilos o '
          'separam da linfadenite supurativa.'),
      par('Granulomas com necrose caseosa e bacilos álcool-ácido resistentes',
          'Linfadenite tuberculosa',
          'Histiócitos epitelioides e células gigantes em volta do caseo. A '
          'cultura confirma e dá o antibiograma.'),
      par('Granulomas com microabscessos estrelados, cheios de neutrófilos',
          'Doença da arranhadura do gato',
          'O abscesso estrelado é neutrofílico. O gato da casa estava na '
          'ficha.'),
      par('Corpos hematoxilínicos e depósito de DNA nas paredes dos vasos, '
          'com plasmócitos',
          'Linfadenite lúpica',
          'Pode haver sobreposição; corpos hematoxilínicos e '
          'plasmócitos favorecem lúpus. Por isso, a equipe solicita o fator antinuclear (FAN).'),
      par('Células de Reed-Sternberg em fundo inflamatório misto',
          'Linfoma de Hodgkin clássico',
          'Morfologia e imunofenótipo precisam ser interpretados em conjunto; uma citometria negativa não exclui esse diagnóstico.'),
    ], opcoes=['Doença de Kikuchi–Fujimoto', 'Linfadenite tuberculosa',
               'Doença da arranhadura do gato', 'Linfadenite lúpica',
               'Linfoma de Hodgkin clássico', 'Sarcoidose'],
    titulo_resposta='Neutrófilos, granulomas e corpos hematoxilínicos separam os padrões',
    nota='A opção que sobrou, sarcoidose, teria granulomas não necrosantes, '
         'compactos, sem cariorrexe.'),

    painel('res3', 'Complemento da biópsia', 'Tecido e autoanticorpos', [
        ex('Imuno-histoquímica', 'Histiócitos CD68 e mieloperoxidase positivos · '
           'células dendríticas plasmocitoides CD123 positivas · predomínio de '
           'linfócitos T CD8', '—', True),
        ex('Células de Reed-Sternberg (CD15 / CD30)', 'Ausentes', 'ausentes'),
        ex('Pesquisa de bacilos da tuberculose no tecido (BAAR)', 'Negativa', 'negativa'),
        ex('Cultura de micobactérias e fungos', 'Em andamento', '—'),
        ex('FAN', 'Não reagente', 'não reagente'),
        ex('Anti-DNA nativo', 'Não reagente', 'não reagente'),
        ex('C3 / C4', '112 / 25 mg/dL', '90–180 / 10–40 mg/dL'),
    ], introducao='Com a lâmina, a equipe fecha as alternativas que ela '
                  'deixou abertas.'),

    pg('diagnostico', 'Integração diagnóstica',
       'A revisão da amostra demonstra linfadenite necrosante histiocítica, compatível com doença de Kikuchi–Fujimoto. A morfologia, a imuno-histoquímica e a apresentação clínica sustentam o diagnóstico; ele não foi estabelecido apenas porque outros testes vieram negativos.',
       'A investigação não sustenta infecção supurativa, linfoma ou linfadenite tuberculosa. As culturas ainda serão acompanhadas. FAN e anti-DNA não reagentes, complemento normal e ausência de manifestações sistêmicas tornam lúpus menos provável neste momento, sem representar exclusão definitiva.',
       'O achado raro passa a ser a melhor explicação porque integra o padrão de tecido à doença observada. Persistência, novas manifestações ou evolução discordante reabririam o diagnóstico.'),

    painel('res3b', 'No dia do laudo', 'Sangue', [
        ex('Hemoglobina', '11,4 g/dL', '12–16 g/dL', True),
        ex('Leucócitos / neutrófilos', '2.600 / 1.350 por mm³', 'L 4.000–11.000 · N 1.800–7.500', True),
        ex('Plaquetas', '176.000/mm³', '150.000–450.000/mm³'),
        ex('Ferritina', '480 ng/mL', '15–150 ng/mL', True),
        ex('Triglicerídeos, em jejum', '126 mg/dL', 'até 150 mg/dL'),
        ex('Fibrinogênio', '390 mg/dL', '200–400 mg/dL'),
    ], introducao='Febre de semanas com leucopenia persistente: a equipe '
                  'procura uma complicação rara dessa doença.'),

    Q('p6', 6,
      'Ainda há febre intermitente. Ferritina é 480 ng/mL, plaquetas 176.000/mm³, neutrófilos 1.350/mm³, triglicerídeos 126 mg/dL e fibrinogênio 390 mg/dL. Como conduzir a possibilidade de síndrome hemofagocítica?', [
      ('Iniciar tratamento específico porque febre e leucopenia bastam para o diagnóstico', False),
      ('Manter avaliação clínica e seriada: os dados disponíveis não sustentam a síndrome neste momento', True),
      ('Excluir definitivamente a síndrome porque a ferritina está abaixo de 500', False),
      ('Solicitar medula e considerar qualquer hemofagocitose encontrada como confirmação isolada', False),
      ], [
      ('Dados atuais', 'Não há combinação de achados que sustente síndrome hemofagocítica agora. Os limiares e a contagem de critérios não substituem a avaliação da evolução; critérios não medidos não devem ser tratados como negativos.'),
      ('Quando reabrir', 'Febre persistente com piora sistêmica, esplenomegalia, queda progressiva de linhagens, aumento importante da ferritina ou coagulopatia justificaria investigação urgente e discussão especializada.'),
      ('Limites', 'HLH-2004 é uma referência, originalmente desenvolvida em pediatria. Em adultos, exige interpretação clínica; hemofagocitose isolada não confirma nem sua ausência exclui a síndrome.'),
      ]),

    pg('conduta', 'Conduta após o diagnóstico',
       'Bianca está estável, sem disfunção orgânica e com sintomas em redução. A equipe propõe analgesia conforme necessidade, hidratação e seguimento. Não há evidência suficiente de infecção bacteriana a justificar novo antibiótico.',
       'Sintomas intensos ou persistentes, doença extranodal ou complicações mudariam a avaliação e poderiam justificar tratamento imunomodulador após revisão das alternativas. O diagnóstico não autoriza ignorar deterioração posterior.',
       'A resposta aos sintomáticos será acompanhada junto ao tamanho dos linfonodos, estado geral e hemograma. A cultura final também precisa ser conferida.'),

    pg('tratamento', 'Tratamento e seguimento',
       'Bianca recebe ibuprofeno por dez dias, sem antibiótico, e sai sabendo '
       'que o linfonodo diminui mais devagar que a febre e que o corticoide '
       'fica guardado para doença grave ou arrastada.',
       'Quatro semanas depois está afebril há oito dias. O maior linfonodo '
       'mede 1 cm e não dói. Hemoglobina 12,1 g/dL, leucócitos 4.300/mm³, PCR '
       '4 mg/L. A cultura do linfonodo termina sem crescimento em seis '
       'semanas. Voltou a trabalhar meio período.'),

    Q('p8', 7,
      'Bianca está afebril, o hemograma recuperou e o linfonodo diminuiu para 1 cm. Qual plano de seguimento é mais adequado?', [
      ('Repetir a biópsia agora, pois qualquer linfonodo residual é discordante', False),
      ('Dosar FAN e anti-DNA mensalmente, mesmo sem sintomas novos', False),
      ('Acompanhar clinicamente e reinvestigar crescimento, persistência discordante ou novas manifestações', True),
      ('Encerrar o seguimento porque a primeira avaliação autoimune foi negativa', False),
      ], [
      ('Regressão', 'O linfonodo pode demorar mais a regredir que a febre. Sua trajetória e o estado geral importam mais que a palpabilidade isolada.'),
      ('Mudança de problema', 'Artrite, erupção fotossensível, edema, alteração urinária ou nova adenopatia justificam avaliação dirigida. Não se deve atribuir automaticamente todo sintoma posterior ao diagnóstico inicial.'),
      ('Reinvestigar', 'Persistência além do esperado ou novo crescimento pede reexaminar o diagnóstico e discutir exames ou nova amostragem conforme o contexto, sem um calendário universal de biópsias.'),
      ]),

    pg('alta', 'Oito semanas depois',
       'Bianca está sem febre, com linfonodos de menos de 1 cm, e voltou à '
       'sala de aula. A equipe revê com ela o que aconteceu, o que esperar e '
       'quando voltar antes do retorno marcado.',
       conforme=('b1', ['f0', 'f_ripe', 'alta_cort'])),

    fim('f0', 'Recuperação sem desvios',
        'Depois do retorno inicial em meio período, Bianca retoma o trabalho integral na avaliação seguinte, já sem febre ou dor. Não precisou de tratamento específico adicional.',
        'Tecido no momento em que a linfadenopatia passou a crescer, com parte '
        'a fresco, respondeu às hipóteses de uma vez e poupou tratamento '
        'empírico.', 'melhor', fecho='extensao'),

    pg('alta_cort', 'Oito semanas depois',
       'Bianca está sem febre, mas o corticoide deixou marcas: insônia, '
       'inchaço no rosto e glicemia de jejum de 112 mg/dL, que a equipe vai '
       'reavaliar depois da retirada.',
       conforme=('resgate', ['f_cort', 'f_pior'])),

    fim('f_ripe', 'Recuperação depois de uma hepatite medicamentosa',
        'A ALT volta ao normal três semanas depois da suspensão. Bianca fica '
        'sete semanas afastada e sai com uma notificação de tuberculose que '
        'precisou ser encerrada como erro diagnóstico.',
        'A prova tuberculínica não demonstrou doença ativa. A melhora durante o esquema não confirmou tuberculose; a trajetória incluiu toxicidade e atraso até a definição histológica.', 'medio', fecho='extensao'),

    fim('f_cort', 'Recuperação com diagnóstico atrasado',
        'A biópsia, com o patologista avisado, é conclusiva. A prednisona é '
        'retirada em três semanas, e Bianca fica seis semanas afastada.',
        'O corticoide aliviou a febre sem dizer o que ela era. Parar a tempo '
        'e contar ao patologista preservou a leitura da lâmina.', 'medio',
        fecho='extensao'),

    fim('f_pior', 'Dois ciclos de corticoide e dez semanas afastada',
        'Bianca fica dez semanas longe da escola, com 4 kg a mais e a febre '
        'voltando a cada redução. A lâmina, colhida sob corticoide, precisa de '
        'revisão por um segundo patologista antes do laudo.',
        'Ciclos empíricos podem dificultar a interpretação histológica e atrasar o reconhecimento de uma infecção ou neoplasia.', 'pior',
        fecho='extensao'),

    bifurcacao('extensao', 'Extensão opcional', 'Seis meses depois',
      'O caso principal terminou. Quer encerrar ou explorar um cenário de '
      'seguimento?', [
      caminho('Encerrar e ver os pontos de ensino', 'retrospectiva',
              'Retoma o que o caso quis ensinar.'),
      caminho('Explorar um retorno seis meses depois', 'novo_quadro',
              'Cenário independente: não é consequência de nenhuma escolha '
              'anterior nem a evolução de toda paciente com essa doença.'),
    ]),

    pg('novo_quadro', 'Seis meses depois',
       'Bianca volta por dor e rigidez matinal nas mãos há três semanas, e '
       'por manchas vermelhas no rosto depois de uma tarde na praia. Os '
       'linfonodos não voltaram. Sente-se cansada de novo.',
       'Ao exame, sinovite nas metacarpofalângicas e interfalângicas '
       'proximais, e eritema malar poupando os sulcos nasolabiais. Pressão '
       '124/80 mmHg, sem edema.'),

    estudo('eritema_face', 'Fotografia: o rosto',
           'Fotografia de outra paciente com o mesmo tipo de lesão que Bianca '
           'tem no rosto, com os olhos cobertos. Descreva onde fica o eritema '
           'e o que acontece com a pele dos sulcos nasolabiais antes de abrir '
           'os achados.',
           IMG / 'eritema_facial.jpg',
           'Fotografia de outra paciente · olhos cobertos · comparação didática.',
           credito_meta(IMG / 'eritema_facial.jpg.json').replace(
               'setas adicionadas', 'olhos cobertos, recorte e setas adicionadas'),
        [
         ((190, 300), (55, 440), '**Eritema** confluente na região malar direita, plano, sem pápulas nem pústulas.', 12),
         ((700, 360), (905, 470), '**Eritema** na região malar esquerda, com a mesma cor e a mesma textura: a lesão é simétrica.', -12),
         ((242, 470), (120, 615), '**Sulco nasolabial poupado**: a pele da dobra, do lado do nariz até o canto da boca, tem a cor normal.', 12),
        ],
        ['Eritema malar poupando os sulcos nasolabiais, surgido depois de uma '
         'tarde de sol.',
         'Eritema das duas bochechas que respeita os sulcos nasolabiais separa '
         'esse desenho da dermatite seborreica, que ocupa as dobras, e da '
         'rosácea, que traz pápulas e pústulas.']),

    bifurcacao('b2', 'Decisão', 'Os sintomas novos',
      'Como você conduz esse retorno?', [
      caminho('Investigar doença sistêmica agora, incluindo urina e função '
              'renal', 'seguimento',
              'Os sintomas são novos e cabem no lúpus que o seguimento '
              'procurava.'),
      caminho('Atribuir tudo a uma recorrência e observar', 'encerramento',
              'A recorrência faz febre e linfonodo, não sinovite com eritema '
              'malar.'),
    ]),

    painel('seguimento', 'Reavaliação', 'O que a equipe pediu', [
        ex('FAN', '1:640, padrão homogêneo', 'não reagente', True),
        ex('Anti-DNA nativo', 'Reagente', 'não reagente', True),
        ex('C3 / C4', '54 / 7 mg/dL', '90–180 / 10–40 mg/dL', True),
        ex('Hemograma', 'Hb 11,2 g/dL · leucócitos 3.100/mm³ · plaquetas 142.000/mm³', '—', True),
        ex('Creatinina', '0,9 mg/dL', '0,5–1,1 mg/dL'),
        ex('Sedimento urinário', '18 hemácias por campo, 30% dismórficas · sem cilindros', 'sem hemácias', True),
        ex('Relação proteína/creatinina urinária', '0,8 g/g', 'abaixo de 0,2 g/g', True),
    ], introducao='A creatinina é normal. O resto não é.'),

    pg('nova_doenca', 'O diagnóstico longitudinal',
       'É lúpus eritematoso sistêmico com nefrite: FAN em título alto, '
       'anti-DNA reagente, complemento consumido, hematúria dismórfica e '
       'proteinúria de 0,8 g/g. Proteinúria de 0,5 g/g ou mais com sedimento '
       'ativo indica biópsia renal mesmo com creatinina normal, porque a '
       'classe histológica decide o tratamento.',
       'A biópsia mostra nefrite lúpica classe III. Ela inicia '
       'hidroxicloroquina, salvo contraindicações, bloqueio do '
       'sistema renina-angiotensina pela proteinúria e indução com a '
       'nefrologia e a reumatologia. O primeiro diagnóstico continua válido: '
       'a associação não prova que o episódio anterior já fosse lúpus; a relação exige revisão longitudinal.',
       segue='f1'),

    fim('f1', 'Lúpus reconhecido cedo',
        'Bianca inicia o tratamento da nefrite com creatinina normal, e a '
        'proteinúria cai nos meses seguintes.',
        'Reconhecer manifestações novas evitou que o diagnóstico anterior '
        'explicasse tudo.', 'melhor'),

    pg('encerramento', 'Dois meses depois',
       'Bianca volta com edema de membros inferiores e urina espumosa. A '
       'pressão é 150/96 mmHg. Proteinúria de 2,4 g/g e creatinina de 1,5 '
       'mg/dL.',
       segue='resgate_renal'),

    bifurcacao('resgate_renal', 'Decisão', 'Edema e creatinina subindo',
      'O que acompanha a avaliação do edema?', [
      caminho('Investigação renal e reumatológica imediata, com biópsia',
              'f2', 'Ainda há rim a salvar; o atraso não é, sozinho, '
                    'irreversibilidade.'),
      caminho('Diurético e nova consulta em um mês', 'atraso_renal',
              'Aliviar o edema não trata a nefrite que o produz.'),
    ]),

    pg('atraso_renal', 'Um mês depois',
       'Bianca é internada com creatinina de 2,8 mg/dL e pressão de 170/104 '
       'mmHg. A biópsia mostra nefrite lúpica classe IV com crescentes em 30% '
       'dos glomérulos e algum grau de fibrose.',
       segue='f3'),

    fim('f2', 'Diagnóstico tardio, ainda a tempo',
        'A nefrite lúpica é tratada com a creatinina em 1,5 mg/dL. A função '
        'renal volta perto do basal, com proteinúria residual.',
        'O atraso custou dois meses de proteinúria, não o rim.', 'medio'),

    fim('f3', 'Nefrite com dano crônico',
        'A indução controla a atividade, mas a creatinina estabiliza em 1,9 '
        'mg/dL, com fibrose documentada na biópsia.',
        'Sinovite com eritema malar foi atribuída a uma recorrência que não '
        'fazia aquilo. A lesão renal progrediu no intervalo.', 'pior'),

    pagina('retrospectiva', 'Pontos de ensino', '',
      pontos(
        'Começar pela linfonodomegalia: distribuição, duração, drenagem, exposições e sinais de alarme. Sintomas sistêmicos podem acompanhar adenopatia localizada.',
        'Dor, ultrassom de aspecto reacional e ausência de blastos não excluem neoplasia. Nenhum deles encerra o diferencial.',
        'Selecionar exames para uma pergunta. Sorologia de contato passado não explica automaticamente febre atual; prova tuberculínica não confirma doença ativa.',
        'Crescimento com sintomas persistentes mudou o limiar para biópsia. Planejar a amostra permite investigar infecção e neoplasia sem perder material.',
        'O diagnóstico raro exige evidência positiva e integração. Negativos reduzem probabilidades em graus diferentes; não são uma lista de exclusões absolutas.',
        'Uma evolução discordante reabre o raciocínio. O diagnóstico anterior não deve impedir reconhecer uma doença nova.'),so_kicker=True),

    pg('referencias', 'Fontes e limites',
       'Paciente, valores e percursos são ficcionais. A extensão de seguimento '
       'é um cenário separado, não a evolução necessária da doença. A cena de '
       'abertura é uma ilustração gerada por inteligência artificial, sem '
       'valor diagnóstico.',
       'Gaddey HL, Riegel AM. Unexplained lymphadenopathy: evaluation and '
       'differential diagnosis. Am Fam Physician, 2016. Dumas e cols., '
       'Medicine, 2014: 91 casos de Kikuchi–Fujimoto. Yoo e cols., J '
       'Ultrasound Med, 2011 (ultrassonografia). Ministério da Saúde, Manual de '
       'Recomendações para o Controle da Tuberculose no Brasil, 2.ª ed., 2019 '
       '(prova tuberculínica e hepatotoxicidade). Henter e cols., Pediatr '
       'Blood Cancer, 2007 (HLH-2004). CDC, Epstein-Barr Virus: Laboratory '
       'Testing. KDIGO 2024 Clinical Practice Guideline for the Management of '
       'Lupus Nephritis.',
       'Imagens de outros pacientes, com setas adicionadas: ultrassonografia, '
       'Nevit Dilmen, Wikimedia Commons, CC BY-SA 3.0; radiografia, Mikael '
       'Häggström, Wikimedia Commons, CC0; lâminas, Nephron, Wikimedia '
       'Commons, CC BY-SA 3.0; fotografia do rosto, Doktorinternet, Wikimedia '
       'Commons, CC BY-SA 4.0, com olhos cobertos e recorte '
       '(commons.wikimedia.org/wiki/File:Lupusfoto.jpg).'),
]

REVISAO = []


# Revisão sindrômica de 21/10/2026. A doença permanece oculta até o tecido.
def _inserir_antes(destino, nova):
    pos = next(i for i, e in enumerate(ETAPAS) if e['k'] == destino)
    ETAPAS.insert(pos, nova)

_inserir_antes('res1', pagina('diferencial_inicial', 'Discussão', 'Linfonodomegalia cervical',
    tabela(['Grupo', 'O que procurar nesta paciente', 'O que mudaria a conduta'], [
      ['Infecção local', 'Dentes, orofaringe, ouvido e couro cabeludo; coleção', 'Foco tratável ou necessidade de drenagem'],
      ['Infecção sistêmica', 'Faringite, exposições e janela dos testes', 'Evidência de infecção recente compatível'],
      ['Neoplasia', 'Progressão, outras cadeias, baço e repercussão', 'Persistência ou crescimento que justifique tecido'],
      ['Inflamação / medicamentos', 'Pele, articulações, urina e cronologia de fármacos', 'Achados associados que direcionem exames'],
    ])))

_inserir_antes('b1', Q('p_probabilidade', 4,
    'Bianca mantém febre, perda de peso e linfonodos em crescimento. A prova tuberculínica (PPD) mede 14 mm. Como esse resultado deve influenciar o raciocínio?', [
      ('Manter tuberculose entre as hipóteses e buscar evidência no linfonodo, sem abandonar as outras causas', True),
      ('Iniciar tratamento para tuberculose, pois o PPD positivo com sintomas confirma a causa dos linfonodos', False),
      ('Desconsiderar o resultado, pois a vacinação BCG na infância explica qualquer PPD positivo', False),
      ('Tratar como infecção latente, pois a radiografia de tórax normal afasta doença ativa', False),
    ], [
      ('O que o PPD informa', 'Uma reação positiva pode indicar infecção pela bactéria da tuberculose. Sozinha, não distingue infecção latente de doença ativa nem demonstra a causa dos linfonodos. A BCG prévia não permite descartar automaticamente o resultado.'),
      ('O que investigar', 'A radiografia de tórax normal não exclui tuberculose nos linfonodos. A evolução clínica justifica obter tecido para análise e pesquisa da bactéria, mantendo também causas neoplásicas e inflamatórias.'),
    ]))

_inserir_antes('diagnostico', pagina('diferencial_final', 'Discussão', 'Revisão das hipóteses',
    tabela(['Hipótese', 'Dados que a enfraquecem', 'Limite da conclusão'], [
      ['Infecção viral aguda', 'Sorologias sem padrão recente e progressão', 'Janela e exposição sempre importam'],
      ['Tuberculose ganglionar', 'Sem granulomas; teste molecular e pesquisa de bacilos negativos', 'Negativos isolados não excluem; acompanhar cultura'],
      ['Linfoma', 'Revisão morfológica e imuno-histoquímica sem suporte', 'Citometria isolada não basta'],
      ['Linfadenite associada a lúpus', 'Sem manifestações associadas, autoanticorpos ou consumo de complemento', 'Seguimento permanece aberto'],
    ])))

for _n, _e in enumerate((x for x in ETAPAS if x['t'] in ('pergunta','pareamento')), 1):
    _e['kicker'] = f'Pergunta {_n}'
ETAPAS[-1]['corpo'] += p('Referências da revisão sindrômica: <a href="https://www.cdc.gov/epstein-barr/php/laboratories/index.html">CDC — sorologia para EBV</a>; <a href="https://www.cdc.gov/tb/hcp/testing-diagnosis/index.html">CDC — investigação de tuberculose</a>; <a href="https://www.nice.org.uk/guidance/ng52/chapter/Recommendations">NICE NG52 — amostragem em suspeita de linfoma</a>.')


_inserir_antes('conduta', pg('relacao_lupus', 'Relação com o lúpus',
    'A doença de Kikuchi–Fujimoto tem associação descrita com lúpus eritematoso sistêmico (LES). Pode ocorrer antes, ao mesmo tempo ou depois do diagnóstico de LES. Essa associação não significa que toda paciente desenvolverá lúpus nem que o episódio atual já seja uma manifestação dele.',
    'O lúpus também pode causar linfadenite com necrose e se parecer com Kikuchi na biópsia. Por isso, o laudo precisa ser integrado à história, ao exame físico e aos exames laboratoriais. Em Bianca, a avaliação atual não sustenta LES; FAN e anti-DNA negativos e complemento normal devem ser interpretados nesse contexto.',
    'No seguimento, artrite persistente, lesões relacionadas ao sol, úlceras orais, dor pleurítica, edema ou alterações na urina justificam nova avaliação. Conforme os achados, reavaliam-se hemograma, creatinina, urina/proteinúria e autoanticorpos/complemento. O objetivo é reconhecer um novo quadro clínico, sem repetir mensalmente um painel autoimune em quem está bem.'))
for _e in ETAPAS:
    if _e.get('segue') == 'conduta':
        _e['segue'] = 'relacao_lupus'

_inserir_antes('p1', Q('hipoteses_apresentacao', 1,
    'Na primeira avaliação, quais três grupos de hipóteses devem organizar a investigação da adenopatia cervical com febre, sudorese e perda de peso?', [
    ('Infecções sistêmicas com acometimento linfonodal', True),
    ('Doença linfoproliferativa', True),
    ('Doença inflamatória ou autoimune', True),
    ('Infecção bacteriana na garganta, nos dentes ou na pele próxima', False),
    ('Metástase de carcinoma de cabeça e pescoço', False),
    ('Reação medicamentosa à amoxicilina', False),
    ], [
    ('Priorizar', 'Infecção sistêmica é favorecida pela apresentação febril após faringite. Sintomas constitucionais exigem manter doença linfoproliferativa no diferencial. Causas inflamatórias e autoimunes permanecem como terceiro eixo, ainda sem manifestação que permita nomear uma doença.'),
    ('Menor sustentação', 'Não há foco bacteriano, rubor ou flutuação. Carcinoma metastático tem menor probabilidade nesta jovem, sem lesão primária ou linfonodo endurecido e fixo. A febre e a adenopatia começaram antes da amoxicilina, desfavorecendo reação a esse fármaco.'),
    ('Probabilidade', 'Menor prioridade não equivale a exclusão. A lista será revista conforme evolução, exame físico e resultados; ainda não há base para procurar exclusivamente uma doença rara.'),
    ]))
_inserir_antes('res3', Q('hipoteses_tecido', 1,
    'A biópsia mostra linfadenite necrosante com cariorrexe, histiócitos e escassez de neutrófilos, sem granulomas caseosos ou população neoplásica identificada. Quais duas hipóteses precisam ser comparadas agora?', [
    ('Doença de Kikuchi–Fujimoto', True),
    ('Linfadenite associada a lúpus', True),
    ('Linfadenite bacteriana supurativa', False),
    ('Tuberculose ganglionar', False),
    ('Doença da arranhadura do gato', False),
    ('Linfoma de Hodgkin', False),
    ], [
    ('Mais compatíveis', 'Kikuchi e linfadenite lúpica podem compartilhar necrose e restos nucleares. A distinção depende do conjunto da histologia, das manifestações clínicas e da investigação autoimune, e não de um achado isolado.'),
    ('Menos compatíveis', 'Supuração bacteriana e doença da arranhadura do gato costumam ter componente neutrofílico. A ausência de granulomas caseosos reduz o apoio à tuberculose, mas não a exclui: a microbiologia continua sendo acompanhada. O tecido não mostrou evidência de linfoma; persistência discordante exigiria revisão.'),
    ]))
for _n, _e in enumerate((x for x in ETAPAS if x['t'] in ('pergunta', 'pareamento')), 1):
    _e['kicker'] = f'Pergunta {_n}'

_inserir_antes('diferencial_final', pagina('leitura_imuno', 'Discussão', 'Como interpretar a imuno-histoquímica',
    p('O patologista usa anticorpos para marcar proteínas nas células do tecido. Isso ajuda a reconhecer quais células participam da lesão. “Positivo” significa que a proteína foi identificada; não significa, por si só, câncer.'),
    tabela(['Marcador', 'O que ajuda a identificar', 'Significado nesta biópsia'], [
        ['CD68 e mieloperoxidase (MPO)', 'Histiócitos: macrófagos presentes no tecido', 'Destacam os histiócitos junto às áreas de necrose'],
        ['CD123', 'Células dendríticas plasmocitoides, que participam da resposta imune', 'Sua presença compõe o padrão inflamatório observado'],
        ['CD8', 'Uma população de linfócitos T', 'Mostra o predomínio de linfócitos T citotóxicos na lesão'],
    ]),
    p('O conjunto é compatível com Kikuchi quando acompanha a morfologia já discutida. Nenhum desses marcadores, isoladamente, confirma o diagnóstico ou exclui linfoma; pode haver sobreposição com linfadenite do lúpus. Para o clínico, o essencial é integrar o laudo à evolução, sem decorar os marcadores.'),
    p('MPO aqui é uma proteína marcada no tecido: não é o exame de sangue anti-MPO/ANCA. Referências: <a href="https://pubmed.ncbi.nlm.nih.gov/11549584/">estudo dos histiócitos CD68/MPO</a>; <a href="https://meridian.allenpress.com/aplm/article/147/7/767/488040/Clinicopathologic-Analysis-of-Kikuchi-Fujimoto">série clinicopatológica de 170 casos</a>.'), so_kicker=True))

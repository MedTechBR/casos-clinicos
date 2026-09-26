"""Linfadenite necrosante histiocítica (doença de Kikuchi–Fujimoto).

Alíquota → pergunta, na gramática dos casos interativos do //New England//:
oito perguntas no percurso principal, uma rodada de exames com gabarito e
painel, um pareamento de histologia e uma extensão opcional de seguimento.
Paciente e valores são ficcionais.
"""
from pathlib import Path

from motor.estudo_imagem import estudo

from motor.etapas import (alt, bifurcacao, caminho, capa, desfecho, op, p,
                          pagina, painel, par, pareamento, pergunta, tabela,
                          topicos, vitais, lamina)
from casos.novos import imagem, referencia_imagem

TITULO = 'O que ficou no pescoço'
RODAPE = 'Paciente ficcional · evoluções simuladas para ensino'
COR = '#ea580c'
IMG = Path(__file__).parent / 'img'
BANCO = []
CENA = 'cena.png'


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
    capa(TITULO, fundo=CENA, kicker='Caso interativo',
         selo='Paciente ficcional · procedência e créditos na última tela'),

    pg('historia', 'Apresentação',
       'Bianca, 27 anos, professora do ensino fundamental, procura o '
       'ambulatório por febre no fim da tarde há doze dias. Começou com dor de '
       'garganta e desconforto ao virar o pescoço. Continuou trabalhando na '
       'primeira semana; agora precisa sentar-se no meio da aula.',
       'Notou um caroço doloroso abaixo e atrás da orelha esquerda. A dor de '
       'garganta passou; o caroço ficou. Tomou amoxicilina por sete dias, '
       'prescrita numa unidade de pronto atendimento, e a febre não cedeu.'),

    pg('hda', 'História da doença atual',
       'A temperatura medida em casa variou entre 37,8 e 38,6 °C. Nas últimas '
       'três noites trocou a camiseta por suor. Perdeu 2 kg por falta de '
       'apetite, sem disfagia, diarreia ou vômitos. A dor no pescoço é '
       'contínua e piora ao toque; ela não percebeu o caroço amolecer.',
       'Nega tosse, dispneia, disúria, dor de dente, artralgia e lesões de '
       'pele. Uma colega de escola teve uma síndrome febril na semana '
       'anterior.'),

    pg('antecedentes', 'Antecedentes e exposições',
       'Sem doenças crônicas nem internações. Usa anticoncepcional oral há '
       'quatro anos; durante a febre, só paracetamol e a amoxicilina já '
       'concluída. Não fuma e nega drogas. Mora em área urbana e não viajou '
       'nos últimos seis meses.',
       'Convive com um gato adulto e não lembra de arranhadura. Tem parceiro '
       'fixo; o último teste de HIV foi há três anos. Não conhece contato com '
       'tuberculose. A mãe tem hipotireoidismo; não há linfoma ou doença '
       'reumatológica na família.'),

    pagina('exame', 'Exame físico', '',
           vitais(('Temperatura', '38,1 °C', True), ('Pressão arterial', '112/70', False),
                  ('Frequência cardíaca', '98', False), ('Frequência respiratória', '16', False),
                  ('SpO₂ em ar ambiente', '98%', False)),
           topicos(('Estado geral', 'Alerta, hidratada, sem desconforto respiratório.'),
                   ('Cabeça e pescoço', 'Orofaringe sem exsudato. Três linfonodos '
                    'cervicais posteriores à esquerda, móveis e dolorosos, o maior '
                    'de 2 cm, sem rubor nem flutuação. Parótidas e tireoide normais.'),
                   ('Cardiopulmonar', 'Ritmo regular, sem sopros. Ausculta pulmonar normal.'),
                   ('Abdome', 'Indolor, sem hepatomegalia ou esplenomegalia.'),
                   ('Pele e articulações', 'Sem exantema, sem sinovite. Sem linfonodos '
                    'axilares ou inguinais palpáveis.')),
           so_kicker=True),

    Q('p1', 1,
      'Febre há doze dias e linfonodos cervicais posteriores dolorosos numa '
      'mulher de 27 anos, sem resposta à amoxicilina. **Quais cinco** '
      'diagnósticos precisam ser considerados?', [
      ('Síndrome mononucleose-símile por EBV ou CMV',
       'Faringite, febre e linfonodo cervical posterior em adulto jovem abrem '
       'a lista.', True),
      ('Faringite estreptocócica não tratada',
       'A dor de garganta passou com amoxicilina. Febre persistente seria '
       'complicação supurativa, que o exame não mostra.', False),
      ('Linfadenite tuberculosa',
       'Febre, sudorese noturna e linfonodo que não cede justificam a '
       'hipótese no Brasil.', True),
      ('Tireoidite subaguda',
       'Dói sobre a tireoide, na face anterior, e a tireoide dela é normal.',
       False),
      ('Linfoma',
       'Sudorese noturna, perda de peso e linfonodo persistente: não pode '
       'ficar de fora.', True),
      ('Parotidite',
       'As parótidas estão normais; o exame localiza linfonodos cervicais '
       'posteriores.', False),
      ('Lúpus eritematoso sistêmico',
       'Febre e linfadenopatia em mulher jovem cabem no lúpus, mesmo sem '
       'artrite ou lesão de pele.', True),
      ('Infecção aguda pelo HIV',
       'A síndrome retroviral aguda dá febre, faringite e linfadenopatia; um '
       'teste de três anos não a exclui.', True),
      ('Tromboflebite séptica da jugular após faringite',
       'Segue uma faringite, mas ela está estável, sem toxemia e sem dor ao '
       'longo da jugular.', False),
      ('Cisto branquial infectado',
       'Seria massa única, anterior ao esternocleidomastóideo e flutuante. '
       'Ela tem três linfonodos posteriores móveis.', False),
     ], 'Infecção viral, micobactéria, linfoma e autoimunidade seguem na lista'),

    Q('ex1', 2,
      'Nesta primeira consulta, **quais quatro** exames são os mais '
      'apropriados?', [
      ('Hemograma completo com esfregaço',
       'Linfocitose atípica, citopenia ou blastos mudam a direção e a pressa.',
       True),
      ('PET-CT',
       'Estadia linfoma já diagnosticado; não substitui tecido e irradia sem '
       'pergunta definida.', False),
      ('Sorologias para EBV e CMV',
       'VCA IgM, VCA IgG e EBNA datam a infecção por EBV; a IgM de CMV '
       'completa.', True),
      ('Punção aspirativa por agulha fina do maior linfonodo',
       'Citologia não mostra arquitetura, que é o que separa linfoma de '
       'linfadenite reativa.', False),
      ('Teste de quarta geração para HIV',
       'Antígeno p24 e anticorpo encurtam a janela da infecção aguda.', True),
      ('FAN e anti-DNA nativo',
       'Sem artrite, lesão de pele ou alteração urinária, o FAN isolado agora '
       'confunde mais do que esclarece.', False),
      ('Ultrassonografia cervical',
       'Número, tamanho, hilo e coleção; orienta a espera e, se preciso, qual '
       'linfonodo tirar.', True),
      ('Tomografia de tórax com contraste',
       'Sem sintoma respiratório, a radiografia simples vem antes.', False),
      ('Antiestreptolisina O',
       'Mede exposição passada ao estreptococo e não explica febre '
       'persistente.', False),
      ('Ferritina e triglicerídeos',
       'Rastreiam hemofagocitose, e nada na primeira consulta a sugere.',
       False),
     ], 'A equipe pede os quatro, e mais a radiografia de tórax'),

    painel('res1', 'Primeiros resultados', 'O que a equipe pediu', [
        ex('Hemoglobina', '11,7 g/dL', '12–16 g/dL', True),
        ex('Leucócitos', '2.900/mm³ · linfócitos atípicos 6% · sem blastos', '4.000–11.000/mm³', True),
        ex('Plaquetas', '188.000/mm³', '150.000–400.000/mm³'),
        ex('Proteína C reativa', '24 mg/L', 'até 5 mg/L', True),
        ex('Desidrogenase láctica', '330 U/L', '120–250 U/L', True),
        ex('AST / ALT', '42 / 47 U/L', 'até 35 / 35 U/L', True),
        ex('EBV', 'VCA IgG reagente · VCA IgM não reagente · EBNA reagente', 'VCA IgM não reagente'),
        ex('CMV', 'IgG reagente · IgM não reagente', 'IgM não reagente'),
        ex('HIV, teste de quarta geração', 'Não reagente', 'Não reagente'),
        ex('Ultrassonografia cervical', 'Múltiplos linfonodos cervicais posteriores à '
           'esquerda, o maior de 2,4 × 1,3 cm, com hilo preservado e área '
           'hipoecoica cortical · sem coleção', '—', True),
        ex('Radiografia de tórax', 'Sem alterações', 'normal'),
    ], introducao='Clique na imagem para ampliar; o laudo abre no botão.',
       laminas={'Radiografia de tórax': lamina('rx_torax_normal.jpg',
                'Radiografia de tórax', 'Imagem ilustrativa de outro adulto; não '
                'pertence a esta paciente.', 'Mikael Häggström · Wikimedia Commons · CC0')}),

    Q('p2', 3,
      'EBV com VCA IgG reagente, VCA IgM não reagente e EBNA reagente; CMV com '
      'IgG reagente e IgM não reagente. Leucócitos 2.900/mm³, linfócitos '
      'atípicos 6%. **Quais duas** conclusões estão corretas?', [
      ('Houve infecção por EBV no passado',
       'O EBNA só surge dois a quatro meses após o início; IgM negativa '
       'completa o perfil antigo.', True),
      ('O CMV também é contato antigo',
       'IgG sem IgM indica infecção passada; a síndrome mononucleose-símile '
       'perde a causa habitual.', True),
      ('É mononucleose aguda por EBV',
       'Na fase aguda, o VCA IgM é positivo e o EBNA ainda negativo; aqui é o '
       'oposto.', False),
      ('Uma reativação do EBV explica a febre',
       'Reativação não tem assinatura sorológica confiável no imunocompetente '
       'e não se lê neste perfil.', False),
      ('A coleta foi precoce demais para a IgM',
       'Com doze dias de febre, o VCA IgM já seria positivo, e o EBNA não se '
       'explica por janela.', False),
      ('Linfócitos atípicos em 6% confirmam infecção viral aguda',
       'Até 10% é inespecífico; mononucleose costuma dar linfocitose, não '
       'leucopenia.', False),
      ('A leucopenia torna linfoma improvável',
       'Linfoma pode cursar com citopenia, por infiltração medular ou por '
       'citocinas.', False),
     ], 'EBV e CMV antigos: a febre continua sem causa'),

    pg('evolucao1', 'Terceira semana',
       'A febre persiste. Um segundo grupo de linfonodos surge à direita, e o '
       'maior à esquerda chega a 2,8 cm. Bianca continua estável, mas falta ao '
       'trabalho. Os leucócitos caem para 2.500/mm³.',
       'A hemocultura não cresceu. As sorologias para toxoplasmose e para '
       '//Bartonella// não mostram infecção recente. O esfregaço não tem '
       'blastos.'),

    Q('p3', 4,
      'O linfonodo cresce há três semanas, com febre, perda de peso e '
      'leucopenia progressiva. Se a investigação seguir para tecido, **quais '
      'três** medidas tornam a amostra mais útil?', [
      ('Retirar o linfonodo inteiro, por excisão',
       'A arquitetura separa linfoma de reação; fragmento e agulha podem não '
       'mostrá-la.', True),
      ('Escolher o linfonodo maior e mais alterado ao ultrassom',
       'O mais alterado tem mais chance de conter a lesão; o mais fácil pode '
       'ser só reativo.', True),
      ('Enviar parte do tecido a fresco',
       'Citometria de fluxo e cultura de micobactéria exigem tecido sem '
       'formol.', True),
      ('Fixar todo o material em formol',
       'Preserva a morfologia, mas elimina citometria de fluxo e cultura.',
       False),
      ('Fazer punção aspirativa antes, para evitar cirurgia',
       'Um laudo de "linfócitos reativos" não exclui linfoma e atrasa o '
       'tecido.', False),
      ('Dar corticoide antes, para reduzir o linfonodo',
       'Corticoide reduz a celularidade e pode tornar a lâmina inconclusiva.',
       False),
      ('Confiar na congelação intraoperatória para o diagnóstico',
       'A congelação diz se a amostra é adequada; o diagnóstico sai da '
       'parafina e da imuno-histoquímica.', False),
      ('Preferir o linfonodo menor, mais simples de retirar',
       'O menor e mais acessível tende a ser reativo e pode não conter a '
       'lesão.', False),
     ], 'Linfonodo inteiro, o mais alterado, e parte a fresco'),

    bifurcacao('b1', 'Decisão', 'O linfonodo de 2,8 cm',
      'Bianca está estável, mas cansada de esperar. O que você faz?', [
      caminho('Encaminhar para biópsia excisional nesta semana', 'tecido',
              'Preserva a arquitetura e investiga as hipóteses de uma vez. '
              'Reserva material para micobactéria e fungo.'),
      caminho('Iniciar prednisona 40 mg/dia pela persistência dos sintomas',
              'corticoide',
              'Alivia a febre, e o alívio parece resposta. Mas trata sem '
              'diagnóstico e pode esconder um linfoma na lâmina.'),
      caminho('Observar mais uma semana, com critérios de alarme', 'observacao',
              'A estabilidade permite um retorno curto; o crescimento e a '
              'citopenia já tinham mudado o risco da espera.'),
    ]),

    pg('corticoide', 'Duas semanas de prednisona',
       'A febre cede em quatro dias e o linfonodo fica menos doloroso. Na '
       'redução, a febre volta e o linfonodo cresce de novo. Bianca pergunta '
       'se a melhora confirma uma doença inflamatória.',
       'Ainda não há diagnóstico. E o corticoide pode reduzir a celularidade '
       'de um linfoma a ponto de tornar a biópsia inconclusiva.'),

    bifurcacao('resgate', 'Decisão', 'A febre voltou',
      'O alívio sob prednisona foi transitório. Qual é o próximo passo?', [
      caminho('Reduzir o corticoide e organizar a biópsia, informando o '
              'patologista', 'tecido',
              'A resposta foi inespecífica. O patologista precisa saber do '
              'corticoide para interpretar a lâmina.'),
      caminho('Repetir o ciclo que havia aliviado a febre', 'novo_ciclo',
              'Mais um ciclo empurra o diagnóstico para frente sem tratar '
              'nenhuma causa demonstrada.'),
    ]),

    pg('novo_ciclo', 'Mais duas semanas',
       'A febre melhora de novo e volta na redução. Bianca está afastada do '
       'trabalho há um mês e tem insônia pelo corticoide. O linfonodo mede 3 '
       'cm. A equipe abandona os ciclos empíricos e obtém tecido; o laudo '
       'demora mais porque a primeira amostra vem pouco celular, e é preciso '
       'um segundo linfonodo.',
       segue='tecido'),

    pg('observacao', 'Três dias depois',
       'A temperatura chega a 39 °C, e a dor limita a alimentação. Os '
       'leucócitos caem para 2.300/mm³. A equipe encaminha para biópsia '
       'excisional em regime de prioridade.',
       segue='tecido'),

    pg('tecido', 'A biópsia',
       'O cirurgião de cabeça e pescoço retira inteiro o maior linfonodo '
       'cervical posterior esquerdo, de 2,6 cm. Uma parte vai fresca para '
       'citometria de fluxo, outra para cultura de micobactérias e fungos.',
       'A citometria não encontra população clonal de linfócitos B ou T. O '
       'patologista chama a equipe ao microscópio antes de liberar o laudo.'),

    estudo('arquitetura', 'Biópsia: pequeno aumento',
           'Esta lâmina é de outro paciente com o mesmo diagnóstico que a '
           'patologia vai propor. Descreva a distribuição das áreas claras e '
           'das áreas celulares antes de ler a interpretação.',
           IMG / 'linfonodo_baixo.jpg',
           'Hematoxilina-eosina, pequeno aumento · outro paciente.',
           referencia_imagem(IMG / 'linfonodo_baixo.jpg.json'),
        [
         ((560, 560), (820, 430), '**Área pálida e eosinofílica**, ampla e mal delimitada, que substitui o tecido linfoide.', 12),
         ((200, 520), (90, 390), '**Ilha de linfócitos** residuais, azul-escura, entre as áreas pálidas.', 12),
         ((450, 185), (330, 70), '**Cápsula** com gordura perinodal: o contorno do linfonodo está preservado.', -12),
        ],
        ['Arquitetura parcialmente apagada por áreas confluentes e pálidas, com cápsula preservada, sem granulomas e sem população linfoide monomórfica.', 'O que ocupa as áreas pálidas só se define no grande aumento.']),

    estudo('celulas', 'Biópsia: grande aumento',
           'A mesma lâmina de referência em grande aumento. Que células povoam '
           'a área pálida, e que célula chama a atenção pela ausência?',
           IMG / 'linfonodo_alto.jpg',
           'Hematoxilina-eosina, grande aumento · outro paciente.',
           referencia_imagem(IMG / 'linfonodo_alto.jpg.json'),
        [
         ((325, 452), (150, 330), '**Cariorrexe**: fragmentos nucleares escuros, pequenos e irregulares, espalhados pela área pálida.', 12),
         ((655, 518), (860, 430), '**Histiócito** de núcleo claro, ovalado ou reniforme, com citoplasma pálido.', -12),
         ((560, 330), (760, 250), 'Fundo **eosinofílico e granular** de necrose, sem neutrófilos.', -12),
        ],
        ['Necrose paracortical com abundante cariorrexe e histiócitos, sem neutrófilos e sem granulomas.', 'Mais de uma doença produz esse padrão; a imuno-histoquímica e a sorologia ajudam a separá-las.']),

    pareamento('p4', 'Pergunta 5',
      'A lâmina de Bianca mostra necrose com cariorrexe, sem neutrófilos e sem '
      'granulomas. Associe cada achado histológico ao diagnóstico que ele '
      'sugere.', [
      par('Necrose paracortical com cariorrexe, histiócitos em crescente e '
          'ausência de neutrófilos',
          'Doença de Kikuchi–Fujimoto',
          'É o padrão de Bianca. Histiócitos em crescente sem neutrófilos o '
          'afastam da linfadenite supurativa.'),
      par('Granulomas com necrose caseosa e bacilos álcool-ácido resistentes',
          'Linfadenite tuberculosa',
          'Histiócitos epitelioides e células gigantes em volta do caseo. A '
          'cultura confirma e dá o antibiograma.'),
      par('Granulomas com microabscessos estrelados, cheios de neutrófilos',
          'Doença da arranhadura do gato',
          'O abscesso estrelado é neutrofílico. O gato da casa estava na '
          'história.'),
      par('Corpos hematoxilínicos e depósito de DNA nas paredes dos vasos, '
          'com plasmócitos',
          'Linfadenite lúpica',
          'Lâmina quase idêntica à de Bianca; corpos hematoxilínicos e '
          'plasmócitos puxam para lúpus. Daí o FAN agora.'),
      par('Células de Reed-Sternberg em fundo inflamatório misto',
          'Linfoma de Hodgkin clássico',
          'CD15 e CD30 positivos. Pode haver necrose, e só o linfonodo inteiro '
          'resolve.'),
    ], opcoes=['Doença de Kikuchi–Fujimoto', 'Linfadenite tuberculosa',
               'Doença da arranhadura do gato', 'Linfadenite lúpica',
               'Linfoma de Hodgkin clássico', 'Sarcoidose'],
    titulo_resposta='Neutrófilos, granulomas e corpos hematoxilínicos separam os padrões',
    nota='A opção que sobrou, sarcoidose, teria granulomas não necrosantes, '
         'compactos, sem cariorrexe.'),

    painel('res2', 'Investigação complementar', 'O que a equipe pediu', [
        ex('FAN', 'Não reagente', 'não reagente'),
        ex('Anti-DNA nativo', 'Não reagente', 'não reagente'),
        ex('C3 / C4', '112 / 25 mg/dL', '90–180 / 10–40 mg/dL'),
        ex('Urina tipo 1', 'Sem hematúria e sem proteinúria', 'normal'),
        ex('Ferritina', '480 ng/mL', '15–150 ng/mL', True),
        ex('Triglicerídeos', '126 mg/dL', 'até 150 mg/dL'),
        ex('Fibrinogênio', '390 mg/dL', '200–400 mg/dL'),
        ex('Cultura do linfonodo', 'Sem crescimento de micobactérias ou fungos em 6 semanas', 'negativa'),
        ex('Imuno-histoquímica', 'Histiócitos CD68 e mieloperoxidase positivos · '
           'células dendríticas plasmocitoides CD123 positivas · sem células de Reed-Sternberg', '—', True),
    ], introducao='Com a lâmina, a equipe fecha as alternativas que ela '
                  'deixou abertas.'),

    pg('patologia', 'O diagnóstico',
       'A revisão com imuno-histoquímica confirma **linfadenite necrosante '
       'histiocítica, a doença de Kikuchi–Fujimoto**: necrose paracortical com '
       'cariorrexe, histiócitos mieloperoxidase-positivos com núcleo em '
       'crescente, células dendríticas plasmocitoides e ausência de '
       'neutrófilos.',
       'Não há corpos hematoxilínicos, e o FAN é negativo. Isso não dispensa o '
       'seguimento: o lúpus pode preceder, acompanhar ou suceder o quadro.'),

    Q('p5', 6,
      'Sobre a doença de Kikuchi–Fujimoto, **quais três** afirmações estão '
      'corretas?', [
      ('Regride sozinha em semanas a poucos meses',
       'Febre e linfonodos regridem sem tratamento específico, em geral em um '
       'a quatro meses.', True),
      ('Pode se associar a lúpus, antes, junto ou depois',
       'Uma minoria desenvolve lúpus, às vezes anos depois; é o motivo do '
       'seguimento.', True),
      ('Recorre numa minoria dos pacientes',
       'A recorrência é incomum e costuma repetir o quadro autolimitado.',
       True),
      ('Leucopenia fala contra o diagnóstico',
       'Leucopenia é achado frequente nessa doença, como em Bianca.', False),
      ('Linfonodo doloroso sugere outro diagnóstico',
       'Dor e sensibilidade no linfonodo são comuns, como no caso dela.',
       False),
      ('Histiócitos mieloperoxidase-positivos sugerem infiltração por '
       'leucemia mieloide',
       'São típicos do Kikuchi; sarcoma mieloide mostraria blastos, não '
       'histiócitos em crescente.', False),
      ('Antibiótico encurta a duração',
       'Nenhum agente bacteriano foi demonstrado; antibiótico só acrescenta '
       'efeito adverso.', False),
      ('Evolui para linfoma com frequência',
       'Não é doença pré-linfomatosa; o risco é confundi-la com linfoma na '
       'lâmina.', False),
      ('Corticoide é obrigatório para todos',
       'Fica para doença grave, arrastada ou complicada.', False),
     ], 'Autolimitada, recorre pouco e pede vigilância para lúpus'),

    Q('p6', 7,
      'Febre por semanas, leucopenia e ferritina de 480 ng/mL levantam a '
      'dúvida de síndrome hemofagocítica, complicação rara dessa doença. Pelos '
      'critérios HLH-2004, **quais duas** afirmações estão corretas?', [
      ('Dos critérios medidos, ela preenche só a febre',
       'Febre de 38,6 °C conta; ferritina, citopenias, baço e lipídios não '
       'atingem os cortes.', True),
      ('Sem teste molecular, exigem-se cinco dos oito',
       'Sem mutação que o confirme, o HLH-2004 pede cinco dos oito.', True),
      ('A ferritina de 480 ng/mL já conta como critério',
       'O corte é 500 ng/mL; a dela fica abaixo.', False),
      ('A leucopenia isolada, sem anemia nem plaquetopenia, já conta como citopenia',
       'O critério exige duas linhagens: Hb abaixo de 9, plaquetas abaixo de '
       '100.000 ou neutrófilos abaixo de 1.000.', False),
      ('Transaminases elevadas são critério',
       'São comuns na hemofagocitose, mas ficam fora do HLH-2004.', False),
      ('Desidrogenase láctica elevada é critério',
       'Acompanha a inflamação, sem entrar nos critérios.', False),
      ('Hemofagocitose no aspirado de medula é obrigatória para o diagnóstico',
       'É um dos oito critérios, nem necessária nem suficiente.', False),
      ('O CD25 solúvel não faz parte dos critérios',
       'CD25 solúvel de 2.400 U/mL ou mais é um dos oito critérios.', False),
     ], 'Ela preenche um dos oito critérios'),

    pg('tratamento', 'Tratamento e seguimento',
       'Bianca recebe analgésico e anti-inflamatório por curto prazo, sem '
       'antibiótico. A equipe explica que os linfonodos regridem mais devagar '
       'que a febre, e que corticoide fica guardado para doença grave ou '
       'arrastada.',
       'Quatro semanas depois está afebril há oito dias. O maior linfonodo '
       'mede 1 cm e não dói. Hemoglobina 12,1 g/dL, leucócitos 4.300/mm³, PCR '
       '4 mg/L. Voltou a trabalhar meio período.'),

    Q('p7', 8,
      'Na alta do acompanhamento agudo, **quais três** orientações estão '
      'corretas?', [
      ('Voltar se surgir artrite, fotossensibilidade ou edema',
       'São os sinais de lúpus que o seguimento procura, e ela precisa '
       'conhecê-los.', True),
      ('Seguimento clínico por alguns anos',
       'A associação com lúpus pode surgir anos depois; o acompanhamento é '
       'clínico.', True),
      ('Reavaliar linfonodo que não regride, até com nova biópsia',
       'Linfonodo que persiste além do esperado reabre o diferencial, '
       'inclusive linfoma.', True),
      ('PET-CT a cada seis meses por dois anos, para vigiar linfoma',
       'O diagnóstico é histológico e a doença é benigna; não há o que '
       'estadiar.', False),
      ('Antibiótico profilático contra recorrência',
       'Não há infecção demonstrada a prevenir.', False),
      ('FAN e anti-DNA todo mês, por tempo indeterminado',
       'Exame sem sintoma, repetido, gera falso-positivo e ansiedade sem '
       'mudar conduta.', False),
      ('Hidroxicloroquina contínua para prevenir o lúpus',
       'Não previne lúpus em quem não o tem; fica para casos recorrentes ou '
       'com lúpus.', False),
      ('Alta definitiva, já que o FAN negativo afasta lúpus futuro',
       'FAN negativo hoje não prevê o futuro; o lúpus pode vir depois.',
       False),
     ], 'Seguimento clínico, atento a lúpus e a linfonodo que persiste'),

    fim('f0', 'Recuperação clínica',
        'Bianca retoma o trabalho em tempo integral e segue sem sintomas no '
        'acompanhamento. A doença regrediu sem dano de órgão.',
        'A biópsia no momento certo respondeu à pergunta que o linfonodo '
        'fazia, e o seguimento ficou aberto ao que ainda pode vir.',
        'melhor') | {'fecho': 'extensao'},

    bifurcacao('extensao', 'Extensão opcional', 'Seis meses depois',
      'O caso principal terminou. Quer encerrar ou explorar um cenário de '
      'seguimento?', [
      caminho('Encerrar e revisar o caso', 'retrospectiva',
              'Retoma os pontos de decisão da investigação.'),
      caminho('Explorar um retorno seis meses depois', 'novo_quadro',
              'Cenário independente: não é consequência de nenhuma escolha '
              'anterior nem a evolução de toda paciente com Kikuchi.'),
    ]),

    pg('novo_quadro', 'Seis meses depois',
       'Bianca volta por dor e rigidez matinal nas mãos há três semanas, e '
       'por manchas vermelhas no rosto depois de uma tarde na praia. Os '
       'linfonodos não voltaram. Sente-se cansada de novo.',
       'Ao exame, sinovite nas metacarpofalângicas e interfalângicas '
       'proximais, e eritema malar poupando os sulcos nasolabiais.'),

    bifurcacao('b2', 'Decisão', 'Os sintomas novos',
      'Como você conduz esse retorno?', [
      caminho('Investigar doença sistêmica agora, incluindo urina e função '
              'renal', 'seguimento',
              'Os sintomas são novos e cabem no lúpus que o seguimento '
              'procurava.'),
      caminho('Atribuir tudo a uma recorrência do Kikuchi e observar',
              'encerramento',
              'Kikuchi recorrente faz febre e linfonodo, não sinovite com '
              'eritema malar.'),
    ]),

    painel('seguimento', 'Reavaliação', 'O que a equipe pediu', [
        ex('FAN', '1:640, padrão homogêneo', 'não reagente', True),
        ex('Anti-DNA nativo', 'Reagente', 'não reagente', True),
        ex('C3 / C4', '54 / 7 mg/dL', '90–180 / 10–40 mg/dL', True),
        ex('Hemograma', 'Hb 11,2 g/dL · leucócitos 3.100/mm³ · plaquetas 142.000/mm³', '—', True),
        ex('Creatinina', '0,9 mg/dL', '0,6–1,1 mg/dL'),
        ex('Sedimento urinário', '18 hemácias por campo, 30% dismórficas · sem cilindros', 'sem hemácias', True),
        ex('Relação proteína/creatinina urinária', '0,8 g/g', 'abaixo de 0,2 g/g', True),
    ], introducao='A creatinina é normal. O resto não é.'),

    Q('p_renal', 9,
      'Lúpus com FAN 1:640, anti-DNA reagente, complemento consumido, '
      'hematúria dismórfica e proteinúria de 0,8 g/g, com creatinina normal. '
      '**Quais três** condutas estão corretas?', [
      ('Biópsia renal',
       'Proteinúria de 0,5 g/g ou mais com sedimento ativo indica biópsia: a '
       'classe decide o tratamento.', True),
      ('Aguardar a creatinina subir para indicar biópsia',
       'Creatinina normal não exclui nefrite proliferativa. Esperar é perder '
       'néfron.', False),
      ('Hidroxicloroquina',
       'Indicada para todo paciente com lúpus: reduz surtos, trombose e '
       'mortalidade.', True),
      ('Anti-inflamatório diário pela artrite',
       'Com nefrite ativa, anti-inflamatório agrava a lesão renal.', False),
      ('Repetir a biópsia do linfonodo cervical',
       'Os linfonodos regrediram. A pergunta agora é o rim.', False),
      ('Bloqueio do sistema renina-angiotensina pela proteinúria',
       'Reduz a proteinúria e protege o rim, junto com a imunossupressão.',
       True),
      ('Atribuir a proteinúria ao episódio de febre de seis meses atrás',
       'A urina era normal naquela época.', False),
     ], 'Proteinúria de lúpus pede tecido, antimalárico e proteção renal'),

    pg('nova_doenca', 'O diagnóstico longitudinal',
       'A biópsia renal mostra nefrite lúpica classe III, e o tratamento de '
       'indução começa com a nefrologia e a reumatologia. O primeiro episódio '
       'foi Kikuchi, e o diagnóstico continua válido: a doença de Kikuchi '
       'pode ser a primeira manifestação de uma doença que só se declara '
       'depois.',
       segue='f1'),

    fim('f1', 'Lúpus reconhecido cedo',
        'Bianca inicia tratamento da nefrite com creatinina normal, e a '
        'proteinúria cai nos meses seguintes.',
        'Reconhecer manifestações novas evitou que o diagnóstico anterior '
        'explicasse tudo.',
        'melhor'),

    pg('encerramento', 'Dois meses depois',
       'Bianca volta com edema de membros inferiores e urina espumosa. A '
       'pressão é 150/96. Proteinúria de 2,4 g/g e creatinina de 1,5 mg/dL.',
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
       'Bianca é internada com creatinina de 2,8 mg/dL e pressão de 170/104. '
       'A biópsia mostra nefrite lúpica classe IV com crescentes em 30% dos '
       'glomérulos e algum grau de fibrose.',
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

    pagina('retrospectiva', 'Retrospectiva', '',
        tabela(['Momento', 'O que estava à mão', 'O que decidiu'], [
            ['Primeira consulta', 'Febre, linfonodo posterior doloroso, amoxicilina '
             'sem efeito', 'Não repetir antibiótico: o diferencial é infecção viral, '
             'micobactéria, linfoma e autoimunidade'],
            ['Sorologias', 'VCA IgG e EBNA reagentes, IgM não reagente; CMV antigo',
             'EBV e CMV passados não explicam a febre de hoje'],
            ['Terceira semana', 'Linfonodo crescendo, leucopenia, LDH alta',
             'Linfonodo inteiro, o mais alterado, parte a fresco, antes de qualquer corticoide'],
            ['Lâmina', 'Necrose com cariorrexe, sem neutrófilos e sem granulomas',
             'Kikuchi, com lúpus e linfoma excluídos por FAN e imuno-histoquímica'],
            ['Seguimento', 'Artrite e eritema malar meses depois',
             'Sintoma novo é doença nova até prova em contrário'],
        ]),
        so_kicker=True),

    pg('referencias', 'Fontes e limites',
       'Paciente, valores e percursos são ficcionais. A extensão de seguimento '
       'é um cenário separado, não a evolução necessária da doença.',
       'Dumas e cols. Medicine, 2014: 91 casos de Kikuchi–Fujimoto. Critérios '
       'HLH-2004: Henter e cols., Pediatric Blood & Cancer, 2007. Sorologia do '
       'EBV: CDC, Laboratory Testing for Epstein-Barr Virus. Nefrite lúpica: '
       'KDIGO 2024 Clinical Practice Guideline for the Management of Lupus '
       'Nephritis, Kidney International, 2024. Lâminas: Nephron, Wikimedia '
       'Commons, CC BY-SA 3.0. Radiografia: Mikael Häggström, CC0. Cena: '
       'ilustração gerada por IA, sem valor diagnóstico.'),
]

REVISAO = []

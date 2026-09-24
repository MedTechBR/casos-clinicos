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
       'Nega tosse, dispneia, disúria e dor de dente. Nega prurido, artrite, '
       'úlceras orais e manchas que surgem com o sol. Uma colega de escola '
       'teve uma síndrome febril na semana anterior.'),

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
                   ('Cabeça e pescoço', 'Orofaringe sem exsudato. **Três linfonodos '
                    'cervicais posteriores à esquerda**, móveis e dolorosos, o maior '
                    'de 2 cm, sem rubor nem flutuação. Parótidas normais.'),
                   ('Cardiopulmonar', 'Ritmo regular, sem sopros. Ausculta pulmonar normal.'),
                   ('Abdome', 'Indolor, **sem hepatomegalia ou esplenomegalia**.'),
                   ('Pele e articulações', 'Sem exantema, sem sinovite. Sem linfonodos '
                    'axilares ou inguinais palpáveis.')),
           so_kicker=True),

    Q('p1', 1,
      'Febre há doze dias e linfonodos cervicais posteriores dolorosos numa '
      'mulher de 27 anos, sem resposta à amoxicilina. **Quais cinco** '
      'diagnósticos precisam ser considerados?', [
      ('Síndrome mononucleose-símile por EBV ou CMV',
       'Febre, linfonodo cervical posterior e cansaço em adulto jovem: é a '
       'causa mais comum, e a amoxicilina não muda nada nela.', True),
      ('Faringite estreptocócica não tratada',
       'A dor de garganta passou e ela recebeu sete dias de amoxicilina — '
       'o tratamento dela. Febre persistente por causa estreptocócica '
       'sugeriria abscesso, que o exame não mostra.', False),
      ('Linfadenite tuberculosa',
       'Escrófula costuma ser pouco dolorosa, mas febre e sudorese noturna '
       'com linfonodo cervical que não cede entram na lista no Brasil.', True),
      ('Tireoidite subaguda',
       'Dói na região anterior do pescoço, sobre a tireoide, e não produz '
       'linfonodo posterior palpável.', False),
      ('Linfoma',
       'Sudorese noturna, perda de peso e linfonodo que persiste: é o '
       'diagnóstico que não pode ser perdido e o que obriga a pensar em '
       'tecido.', True),
      ('Parotidite',
       'O caroço é "abaixo da orelha", mas o exame localiza linfonodos '
       'cervicais posteriores e parótidas normais.', False),
      ('Lúpus eritematoso sistêmico',
       'Febre, linfadenopatia e, adiante, leucopenia: o lúpus abre com '
       'linfonodo em até um terço dos casos.', True),
      ('Infecção aguda pelo HIV',
       'A síndrome retroviral aguda faz febre, faringite e linfadenopatia. '
       'Um teste de três anos atrás não a exclui.', True),
      ('Doença de Kawasaki',
       'Doença da infância, com conjuntivite, alterações de mucosa e '
       'extremidades. Não aos 27 anos.', False),
      ('Cisto branquial infectado',
       'Massa única, lateral, anterior ao esternocleidomastóideo, que '
       'flutua. Ela tem três linfonodos posteriores móveis.', False),
     ], 'Infecção, linfoma e autoimunidade — os três endereços do linfonodo que não cede'),

    Q('ex1', 2,
      'Nesta primeira consulta, **quais quatro** exames são os mais '
      'apropriados?', [
      ('Hemograma completo com esfregaço',
       'Linfocitose atípica, citopenia ou blastos mudam a pressa e a '
       'direção. É o primeiro exame.', True),
      ('PET-CT',
       'Estadia linfoma já diagnosticado. Não diagnostica, e expõe a '
       'radiação uma paciente sem tecido.', False),
      ('Sorologias para EBV e CMV',
       'VCA IgM, VCA IgG e EBNA separam infecção aguda de passada; IgM de '
       'CMV completa a síndrome mononucleose-símile.', True),
      ('Punção aspirativa por agulha fina do maior linfonodo',
       'Citologia não mostra arquitetura, e é a arquitetura que separa '
       'linfoma de linfadenite. Se chegar a tecido, é linfonodo inteiro.',
       False),
      ('Teste de quarta geração para HIV',
       'Antígeno p24 e anticorpo: fecha a janela da infecção aguda melhor '
       'que os testes antigos.', True),
      ('FAN e anti-DNA nativo',
       'Sem artrite, sem lesão de pele e sem alteração urinária, o FAN '
       'isolado mais confunde do que esclarece. Entra se aparecerem dados '
       'de doença sistêmica.', False),
      ('Ultrassonografia cervical',
       'Tamanho, número, hilo, necrose e coleção: orienta a espera e, '
       'depois, qual linfonodo tirar.', True),
      ('Tomografia de tórax com contraste',
       'Sem sintoma respiratório e com radiografia simples ainda por fazer, '
       'não é o primeiro passo.', False),
      ('Antiestreptolisina O',
       'Mede exposição passada ao estreptococo. Não explica a febre '
       'persistente.', False),
      ('Novo curso de antibiótico de espectro mais largo',
       'Não é exame, e é o erro mais comum: trata-se uma linfadenite '
       'bacteriana que o exame não sustenta.', False),
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

    pergunta('p2', 'Pergunta 3',
      'EBV: **VCA IgG reagente, VCA IgM não reagente, EBNA reagente.** Qual a '
      'interpretação?', [
      alt('Infecção aguda por EBV',
          'Mononucleose aguda tem VCA IgM positivo e, nas primeiras semanas, '
          'EBNA negativo — o oposto do que ela tem.'),
      alt('Infecção passada por EBV',
          'O anticorpo contra o antígeno nuclear (EBNA) só aparece de seis a '
          'oito semanas depois da infecção. EBNA positivo com IgM negativo é '
          'infecção antiga.', certa=True),
      alt('Reativação do EBV como causa da febre',
          'Reativação sorológica não tem assinatura confiável em '
          'imunocompetente, e não se diagnostica por este perfil.'),
      alt('Falso-negativo por coleta precoce',
          'Doze dias de febre é justamente quando o VCA IgM já está '
          'positivo. E o EBNA positivo não se explica por janela.'),
      alt('Infecção crônica ativa por EBV',
          'Doença rara, com carga viral alta no sangue e títulos '
          'anormalmente altos. Não se lê numa sorologia comum.'),
    ], titulo_resposta='O EBNA chega por último — e não chega em duas semanas'),

    pg('evolucao1', 'Terceira semana',
       'A febre persiste. Um segundo grupo de linfonodos surge à direita, e o '
       'maior à esquerda chega a **2,8 cm**. Bianca continua estável, mas '
       'falta ao trabalho. Os leucócitos caem para 2.500/mm³.',
       'A hemocultura não cresceu. As sorologias para toxoplasmose e para '
       '//Bartonella// não mostram infecção recente. O esfregaço não tem '
       'blastos.'),

    pergunta('p3', 'Pergunta 4',
      'Linfadenopatia que cresce há três semanas, com febre, perda de peso e '
      'leucopenia. Qual o próximo passo diagnóstico **mais apropriado**?', [
      alt('Biópsia excisional de linfonodo',
          'Só o linfonodo inteiro mostra a arquitetura que separa linfoma, '
          'tuberculose e linfadenite necrosante. Parte para histologia, '
          'parte para cultura, fresco para citometria.', certa=True),
      alt('Punção aspirativa por agulha fina',
          'Pode achar granuloma ou células atípicas, mas um resultado '
          'negativo não exclui linfoma — e o laudo "linfócitos reativos" '
          'atrasa semanas.'),
      alt('PET-CT para escolher o alvo',
          'Útil para escolher o linfonodo em doença profunda. Aqui o alvo é '
          'palpável, e o PET não diagnostica.'),
      alt('Repetir as sorologias em duas semanas',
          'As sorologias já responderam. Esperar mais duas semanas com '
          'citopenia progressiva não traz informação nova.'),
      alt('Prova terapêutica com corticoide',
          'O corticoide trata a febre de três doenças diferentes e pode '
          'apagar, na lâmina, o linfoma que se procura.'),
    ], titulo_resposta='Arquitetura exige linfonodo inteiro'),

    bifurcacao('b1', 'Decisão', 'O linfonodo de 2,8 cm',
      'Bianca está estável, mas cansada de esperar. O que você faz?', [
      caminho('Encaminhar para biópsia excisional nesta semana', 'tecido',
              'Preserva a arquitetura e investiga as três hipóteses de uma '
              'vez. Reserva material para micobactéria e fungo.'),
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
       'demora mais porque a primeira amostra tem necrose extensa e pouca '
       'celularidade, e é preciso um segundo linfonodo.',
       segue='tecido'),

    pg('observacao', 'Três dias depois',
       'A temperatura chega a 39 °C, e a dor limita a alimentação. Os '
       'leucócitos caem para 2.300/mm³. A equipe encaminha para biópsia '
       'excisional em regime de prioridade.',
       segue='tecido'),

    pg('tecido', 'A biópsia',
       'O cirurgião de cabeça e pescoço retira um linfonodo cervical '
       'posterior esquerdo inteiro, de 2,6 cm. Uma parte vai fresca para '
       'citometria de fluxo, outra para cultura de micobactérias e fungos.',
       'O laudo preliminar descreve **áreas de necrose com abundantes '
       'fragmentos nucleares e histiócitos**, sem granulomas e sem população '
       'linfoide monomórfica. A citometria não encontra clone.'),

    estudo('arquitetura', 'Biópsia: pequeno aumento',
           'Esta lâmina é de outro paciente com o mesmo diagnóstico que a '
           'patologia vai propor. Descreva a distribuição das áreas claras e '
           'das áreas celulares antes de ler a interpretação.',
           IMG / 'linfonodo_baixo.jpg',
           'Hematoxilina-eosina, pequeno aumento · outro paciente.',
           referencia_imagem(IMG / 'linfonodo_baixo.jpg.json'),
        [
         ((560, 560), (820, 430), '**Área pálida e eosinofílica**, ampla e mal delimitada, que substitui o tecido linfoide: a necrose com histiócitos.', 12),
         ((200, 520), (90, 390), '**Ilha de linfócitos** residuais, azul-escura, entre as áreas pálidas.', 12),
         ((450, 185), (330, 70), '**Cápsula** com gordura perinodal: o contorno do linfonodo está preservado.', -12),
        ],
        ['Linfonodo com arquitetura parcialmente preservada, substituída por áreas confluentes de necrose pálida, sem granulomas e sem população linfoide monomórfica.', 'O pequeno aumento mostra onde está o processo. Quem ele é, só o grande aumento diz.']),

    estudo('celulas', 'Biópsia: grande aumento',
           'O mesmo diagnóstico em grande aumento. Que células povoam a área '
           'de necrose — e qual célula chama a atenção pela ausência?',
           IMG / 'linfonodo_alto.jpg',
           'Hematoxilina-eosina, grande aumento · outro paciente.',
           referencia_imagem(IMG / 'linfonodo_alto.jpg.json'),
        [
         ((325, 452), (150, 330), '**Cariorrexe**: fragmentos nucleares escuros, pequenos e irregulares, espalhados pela necrose.', 12),
         ((655, 518), (860, 430), '**Histiócito** de núcleo claro, ovalado ou reniforme, com citoplasma pálido.', -12),
         ((560, 330), (760, 250), 'Fundo **eosinofílico e granular** de necrose, sem neutrófilos.', -12),
        ],
        ['Necrose com abundante cariorrexe e histiócitos, sem neutrófilos e sem granulomas: linfadenite necrosante histiocítica.', 'A falta de neutrófilos a separa da linfadenite supurativa, e a de granulomas, da tuberculose. O lúpus pode dar lâmina idêntica, e por isso o FAN.']),

    pareamento('p4', 'Pergunta 5',
      'Linfadenite necrosante tem mais de um endereço. Associe cada achado '
      'histológico ao diagnóstico que ele sugere.', [
      par('Necrose paracortical com cariorrexe, histiócitos em crescente e '
          'ausência de neutrófilos',
          'Doença de Kikuchi–Fujimoto',
          'É o laudo de Bianca. Os histiócitos com núcleo em crescente e a '
          'falta de neutrófilos separam Kikuchi da linfadenite supurativa.'),
      par('Granulomas com necrose caseosa e bacilos álcool-ácido resistentes',
          'Linfadenite tuberculosa',
          'Necrose caseosa cercada de histiócitos epitelioides e células '
          'gigantes. A cultura confirma e dá o antibiograma.'),
      par('Granulomas com microabscessos estrelados, cheios de neutrófilos',
          'Doença da arranhadura do gato',
          'O abscesso estrelado é neutrofílico, o oposto do Kikuchi. O gato '
          'da casa estava na história.'),
      par('Corpos hematoxilínicos e depósito de DNA nas paredes dos vasos, '
          'com plasmócitos',
          'Linfadenite lúpica',
          'A lâmina pode ser quase idêntica ao Kikuchi; os corpos '
          'hematoxilínicos e os plasmócitos puxam para lúpus. É por isso que '
          'o FAN entra agora.'),
      par('Células de Reed-Sternberg em fundo inflamatório misto',
          'Linfoma de Hodgkin clássico',
          'CD15 e CD30 positivos. A necrose pode existir no Hodgkin, e é por '
          'isso que só o linfonodo inteiro resolve.'),
    ], opcoes=['Doença de Kikuchi–Fujimoto', 'Linfadenite tuberculosa',
               'Doença da arranhadura do gato', 'Linfadenite lúpica',
               'Linfoma de Hodgkin clássico', 'Sarcoidose'],
    titulo_resposta='Neutrófilo presente é abscesso; ausente, Kikuchi ou lúpus',
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
    ], introducao='Com o laudo, a equipe fecha as alternativas que a lâmina '
                  'deixou abertas.'),

    pg('patologia', 'O diagnóstico',
       'A revisão confirma **linfadenite necrosante histiocítica — doença de '
       'Kikuchi–Fujimoto**: necrose paracortical com cariorrexe, histiócitos '
       'mieloperoxidase-positivos com núcleo em crescente, células '
       'dendríticas plasmocitoides e ausência de neutrófilos.',
       'Não há corpos hematoxilínicos, e o FAN é negativo. A ausência de lúpus '
       'hoje não dispensa o seguimento — a associação pode vir antes, junto '
       'ou depois.'),

    Q('p5', 6,
      'Sobre a doença de Kikuchi–Fujimoto, **quais três** afirmações estão '
      'corretas?', [
      ('Costuma regredir sozinha em até quatro meses',
       'Febre e linfonodos regridem sozinhos; o tratamento é de sintomas.',
       True),
      ('Antibiótico encurta a duração da doença',
       'Não há agente bacteriano demonstrado. Antibiótico só acrescenta '
       'efeitos adversos.', False),
      ('Pode se associar a lúpus, antes ou depois',
       'Em séries, uma minoria desenvolve lúpus, às vezes anos depois. É o '
       'motivo do seguimento.', True),
      ('Predomina em homens acima dos 60 anos',
       'Predomina em adultos jovens, sobretudo mulheres abaixo dos 40.',
       False),
      ('Pode recorrer, em poucos pacientes',
       'Recorrência em torno de 3 a 4%. Quadro idêntico e autolimitado não '
       'exige outra excisão; quadro diferente, sim.', True),
      ('Evolui para linfoma na maioria dos casos',
       'Não é doença pré-linfomatosa. O risco é confundi-la com linfoma na '
       'lâmina, não se transformar nele.', False),
      ('Corticoide é obrigatório para todos',
       'Reservado para doença grave ou arrastada, com sintomas '
       'incapacitantes ou complicação.', False),
     ], 'Autolimitada, ligada ao lúpus, e às vezes volta'),

    Q('p6', 7,
      'Ela teve febre por semanas, leucopenia e ferritina de 480 ng/mL. A '
      'síndrome hemofagocítica é uma complicação rara do Kikuchi. **Quais '
      'quatro** achados fazem parte dos critérios diagnósticos dela?', [
      ('Ferritina de 500 ng/mL ou mais',
       'É critério do HLH-2004. A dela, 480, fica abaixo — e valores acima '
       'de 10.000 são os que realmente preocupam.', True),
      ('Linfonodo doloroso',
       'Dor no linfonodo é do Kikuchi, não da hemofagocitose.', False),
      ('Esplenomegalia',
       'Critério do HLH-2004. O baço dela não é palpável.', True),
      ('Citopenia em pelo menos duas linhagens',
       'Hemoglobina abaixo de 9, plaquetas abaixo de 100.000, neutrófilos '
       'abaixo de 1.000. Ela tem leucopenia leve, sem as outras.', True),
      ('Proteína C reativa acima de 20 mg/L',
       'Não é critério. Inflamação qualquer eleva a PCR.', False),
      ('Triglicerídeos de 265 mg/dL ou mais, ou fibrinogênio de 150 mg/dL ou '
       'menos',
       'O fígado inflamado pela tempestade de citocinas eleva triglicerídeo '
       'e consome fibrinogênio. Os dela estão normais.', True),
      ('Transaminases acima de três vezes o normal',
       'Frequente na hemofagocitose, mas não é critério do HLH-2004.',
       False),
      ('Desidrogenase láctica elevada',
       'Acompanha, sem definir. Não é critério.', False),
     ], 'Ferritina, baço, citopenias e lipídios — ela não fecha nenhum com folga'),

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
      ('Voltar se surgirem artrite, fotossensibilidade ou edema',
       'São os sinais de lúpus que o seguimento procura. A paciente precisa '
       'conhecê-los.', True),
      ('Repetir PET-CT a cada seis meses por dois anos',
       'Não há indicação: o diagnóstico é histológico e a doença, benigna.',
       False),
      ('Seguimento clínico, com FAN e urina se houver sintomas',
       'Seguimento clínico por alguns anos, guiado por sintomas, é o que as '
       'séries recomendam.', True),
      ('Antibiótico profilático para evitar recorrência',
       'Não há infecção a prevenir.', False),
      ('Recorrência igual pode dispensar nova excisão',
       'Recorrência igual e autolimitada tem o mesmo tratamento. Mudança do '
       'padrão pede nova investigação.', True),
      ('Dosar FAN todo mês, por tempo indeterminado',
       'Exame sem sintoma, repetido à exaustão, produz falso-positivo e '
       'ansiedade.', False),
      ('Hidroxicloroquina para todos, para prevenir lúpus',
       'Não previne lúpus em quem não o tem. Usa-se em Kikuchi recorrente ou '
       'com lúpus estabelecido.', False),
     ], 'O seguimento procura o lúpus, não o linfoma'),

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
       'Proteinúria acima de 0,5 g/g com sedimento ativo é indicação: a '
       'classe da nefrite decide o tratamento.', True),
      ('Aguardar a creatinina subir para indicar biópsia',
       'Creatinina normal não exclui nefrite proliferativa. Esperar é '
       'perder néfron.', False),
      ('Hidroxicloroquina',
       'Indicada para todo paciente com lúpus: reduz surtos, trombose e '
       'mortalidade.', True),
      ('Anti-inflamatório diário pela artrite',
       'Com nefrite ativa, anti-inflamatório agrava a lesão renal.', False),
      ('Repetir a biópsia do linfonodo cervical',
       'Os linfonodos regrediram. A pergunta agora é o rim.', False),
      ('Bloqueio do sistema renina-angiotensina pela proteinúria',
       'Reduz a proteinúria e protege o rim, junto com o tratamento '
       'imunossupressor.', True),
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
             'linfoma e autoimunidade'],
            ['Sorologias', 'VCA IgG e EBNA reagentes, IgM não reagente',
             'EBV passado não explica a febre de hoje'],
            ['Terceira semana', 'Linfonodo crescendo, leucopenia, LDH alta',
             'Linfonodo inteiro, antes de qualquer corticoide'],
            ['Lâmina', 'Necrose com cariorrexe e sem neutrófilos',
             'Kikuchi, com lúpus e linfoma excluídos por FAN e imuno-histoquímica'],
            ['Seguimento', 'Artrite e eritema malar meses depois',
             'Sintoma novo é doença nova até prova em contrário'],
        ]),
        so_kicker=True),

    pg('referencias', 'Fontes e limites',
       'Paciente, valores e percursos são ficcionais. A extensão de seguimento '
       'é um cenário separado, não a evolução necessária da doença.',
       'Dumas e cols. Medicine, 2014: 91 casos de Kikuchi–Fujimoto. Critérios '
       'HLH-2004: Henter e cols., Pediatric Blood & Cancer, 2007. Lâminas: '
       'Nephron, Wikimedia Commons, CC BY-SA 3.0. Radiografia: Mikael '
       'Häggström, CC0. Cena: ilustração gerada por IA, sem valor '
       'diagnóstico.'),
]

REVISAO = []

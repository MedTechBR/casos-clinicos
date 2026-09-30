"""Febre com linfonodos cervicais dolorosos numa professora de 27 anos.

Reescrito em 26/09/2026 no molde do //New England// aprovado no piloto da
leptospirose (ver Artifacts/nejm-casos-classicos/GRAMATICA_LIDA_2026-09-26.md):
apresentação curta, ficha do paciente, exame por sistema e primeiros exames
entregues prontos. Só duas perguntas antes da virada, e as duas
classificam sem nomear doença (linfadenopatia localizada ou generalizada,
leitura do hemograma); as sorologias viram uma página lida pela equipe.
Revisão de ritmo de 30/09: seis perguntas no caminho padrão, nunca duas
telas interativas seguidas. O caso segue duas âncoras que a equipe
registra e que eram razoáveis no momento: síndrome mononucleose-símile e,
depois, tuberculose ganglionar. A biópsia vira o caso depois da metade, e o
nome do diagnóstico aparece pela primeira vez no pareamento da histologia.
Uma extensão opcional acompanha o seguimento e o aparecimento de lúpus.

Paciente ficcional. Critérios e condutas: Gaddey e Riegel, Am Fam Physician
2016 (linfadenopatia); Manual de Recomendações para o Controle da
Tuberculose no Brasil, 2.ª ed., 2019; HLH-2004; KDIGO 2024 (nefrite lúpica).
"""
from pathlib import Path

from motor.estudo_imagem import estudo
from motor.etapas import (alt, bifurcacao, caminho, capa, desfecho, op, p,
                          pagina, painel, par, pareamento, pergunta, pontos,
                          topicos, vitais)

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
                   ('Família', 'Mãe com hipotireoidismo. Pai hipertenso, filho de '
                    'imigrantes japoneses. Sem câncer, tuberculose ou doença '
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
      'Antes dos exames, a equipe classifica a linfadenopatia. **Quais três** '
      'afirmações sobre a de Bianca estão corretas?', [
      ('É localizada: uma só região acometida', True),
      ('Sintomas constitucionais aumentam a preocupação', True),
      ('Dor à palpação não afasta neoplasia', True),
      ('É generalizada, pelo número de linfonodos', False),
      ('A cadeia posterior é sítio de alto risco', False),
      ('A idade dela é fator de risco', False),
      ('Por ser dolorosa, dispensa seguimento', False),
     ], [
      ('A classificação', 'Linfadenopatia generalizada é a que acomete duas ou '
       'mais regiões não contíguas, e aponta para doença sistêmica. Três '
       'linfonodos na mesma cadeia cervical, com axilas, virilhas e baço '
       'normais, são uma linfadenopatia localizada: o primeiro passo é olhar a '
       'área que aquela cadeia drena, e aqui orofaringe, dentes e couro '
       'cabeludo estão limpos.'),
      ('Os sinais que pedem tecido', 'Idade acima de 40 anos, localização '
       'supraclavicular, tamanho acima de 2 cm, consistência endurecida, '
       'fixação aos planos, duração acima de quatro semanas ou crescimento, e '
       'sintomas constitucionais: febre, sudorese noturna e perda de peso. '
       'Bianca tem o último e um tamanho no limite. A cadeia supraclavicular é '
       'a de maior risco; a posterior, não.'),
      ('O que muda', 'Dor sugere distensão rápida da cápsula, mais comum na '
       'inflamação, mas necrose ou hemorragia dentro de uma neoplasia também doem. '
       'Com 12 dias e um sinal de alarme, cabem exames de sangue, ultrassom e '
       'reavaliação curta. Linfadenopatia localizada sem explicação que não '
       'regride em três a quatro semanas, ou que cresce, pede tecido.'),
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
      '**Quais três** leituras do hemograma de Bianca estão corretas?', [
      ('Leucopenia com neutropenia leve', True),
      ('Anemia leve e normocítica', True),
      ('Duas linhagens baixas, plaquetas normais', True),
      ('Pancitopenia', False),
      ('Neutropenia grave, com risco infeccioso', False),
      ('Padrão de infecção bacteriana', False),
      ('Linfocitose com muitos linfócitos atípicos', False),
     ], [
      ('O padrão', 'Leucócitos de 2.900 com 1.450 neutrófilos: neutropenia '
       'leve, que vai de 1.000 a 1.500. Hemoglobina de 11,7 com VCM de 86 é '
       'anemia leve normocítica. As plaquetas estão normais, então são duas '
       'linhagens discretamente baixas, e não pancitopenia.'),
      ('Por que não as outras', 'Neutropenia grave é abaixo de 500. Infecção '
       'bacteriana daria neutrofilia com desvio, e a amoxicilina não mudou '
       'nada. Os linfócitos, 1.100, estão no limite inferior, e só 4% são '
       'reativos: não há linfocitose. Sem blastos e com plaquetas normais, '
       'nada aponta doença primária da medula.'),
      ('O que o padrão abre', 'Febre, linfonodo e leucopenia leve num adulto '
       'jovem abrem quatro grupos: infecção viral, infecção granulomatosa, '
       'doença autoimune e neoplasia linfoide. A desidrogenase láctica alta e '
       'a PCR modesta não escolhem entre eles.'),
     ]),

    estudo('us_cervical', 'Ultrassonografia do pescoço',
           'Pedida na primeira consulta, com os exames de sangue, para contar e '
           'medir os linfonodos, ver o hilo e procurar coleção. Descreva a '
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
        ['Três linfonodos na cadeia cervical posterior esquerda, o maior de 2,2 '
         '× 0,9 cm, ovalados, com hilo ecogênico preservado e fluxo de padrão '
         'hilar. Sem coleção, sem calcificação e sem necrose liquefeita.',
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

    pg('hipotese', 'A primeira hipótese',
       'Com febre, faringite no início, linfonodos cervicais posteriores e '
       'linfócitos reativos, a equipe registra síndrome mononucleose-símile. '
       'Pede sorologias para vírus Epstein-Barr (EBV), citomegalovírus (CMV) '
       'e toxoplasmose, teste de quarta geração para HIV e VDRL.',
       'Mantém paracetamol, não repete antibiótico e marca retorno em uma '
       'semana, com orientação de voltar antes se a febre subir ou surgir '
       'falta de ar.'),

    painel('res2', 'Retorno', 'Sorologias', [
        ex('EBV: VCA IgM', 'Não reagente', 'não reagente'),
        ex('EBV: VCA IgG', 'Reagente', '—', True),
        ex('EBV: EBNA IgG', 'Reagente', '—', True),
        ex('CMV: IgM / IgG', 'Não reagente / reagente', '—', True),
        ex('Toxoplasmose: IgM / IgG', 'Não reagente / não reagente', 'não reagente'),
        ex('HIV, teste de quarta geração', 'Não reagente', 'não reagente'),
        ex('VDRL', 'Não reagente', 'não reagente'),
    ], introducao='Colhidas na primeira consulta, no 12.º dia de febre.'),

    pagina('sorologias_leitura', 'Discussão', 'Como ler as sorologias',
           p('A equipe lê o painel do EBV pela ordem em que os anticorpos '
             'aparecem. A IgM contra o capsídeo viral (VCA) surge com os '
             'sintomas e some em semanas; o EBNA só aparece dois a quatro meses '
             'depois e fica para sempre. VCA IgG e EBNA reagentes com IgM '
             'negativa, no 12.º dia de febre, é infecção antiga. Na '
             'mononucleose aguda o desenho é o inverso, e a reativação não tem '
             'assinatura sorológica confiável em quem não é imunossuprimido.'),
           p('No CMV, IgG reagente sem IgM é contato passado. No toxoplasma, '
             'as duas negativas no 12.º dia afastam infecção aguda, porque a '
             'IgM surge na primeira semana.'),
           p('O teste de quarta geração para HIV detecta o antígeno p24 cerca '
             'de duas semanas depois da infecção, e a janela pode passar disso. '
             'Com parceiro único e teste não reagente, a hipótese perde força; '
             'se a suspeita subir, repete-se o teste ou pede-se carga viral.'),
           p('As causas habituais da síndrome mononucleose-símile ficaram sem '
             'sustentação, e a febre continua sem explicação.')),

    pg('evolucao1', 'Terceira semana',
       'No retorno, no 19.º dia, a febre chega a 38,8 °C e a sudorese é quase '
       'diária. O maior linfonodo cresceu para 2,8 cm, e dois menores '
       'apareceram na cadeia cervical posterior direita. Perdeu mais 1 kg. '
       'Leucócitos 2.500/mm³, neutrófilos 1.300/mm³, desidrogenase láctica '
       '360 U/L.',
       'Febre arrastada, sudorese, emagrecimento e linfonodo cervical que '
       'cresce, numa cidade com muita tuberculose: a equipe passa a registrar '
       'linfadenite tuberculosa como hipótese principal. A prova '
       'tuberculínica, lida em 72 horas, mede 14 mm. Ela não tem tosse nem '
       'escarro para pesquisa de bacilo.'),

    bifurcacao('b1', 'Decisão', 'O linfonodo de 2,8 cm',
      'Três semanas de febre, prova tuberculínica de 14 mm e linfonodos '
      'crescendo. Bianca está estável e quer uma resposta. O que você faz?', [
      caminho('Biópsia excisional nesta semana, com parte a fresco', 'tecido',
              'Uma amostra responde às duas hipóteses: arquitetura para '
              'linfoma, cultura e TRM-TB para tuberculose.'),
      caminho('Iniciar o esquema básico para tuberculose sem tecido', 'ripe',
              'A prova tuberculínica mede infecção, não doença. Seis meses de '
              'tratamento sem confirmação expõem a hepatotoxicidade e podem '
              'mascarar outra causa.'),
      caminho('Prednisona 40 mg ao dia pela febre persistente', 'corticoide',
              'Alivia a febre, e o alívio parece resposta. Trata sem '
              'diagnóstico e pode apagar um linfoma na lâmina.'),
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

    Q('p4', 3,
      '**Quais três** medidas tornam a amostra mais útil?', [
      ('Retirar o linfonodo inteiro', True),
      ('Escolher o mais alterado ao exame', True),
      ('Enviar parte do tecido a fresco', True),
      ('Fixar todo o material em formol', False),
      ('Punção aspirativa em vez da excisão', False),
      ('Corticoide antes, para reduzir o linfonodo', False),
      ('Preferir o menor, mais fácil de tirar', False),
     ], [
      ('A excisão', 'O que separa linfoma de linfadenite reativa é a '
       'arquitetura, e só o linfonodo inteiro a mostra. A biópsia por agulha '
       'grossa guiada por ultrassom é a alternativa quando a excisão não é '
       'possível. A punção aspirativa, com teste rápido molecular e cultura, '
       'pode confirmar tuberculose, mas um resultado negativo ou "linfócitos '
       'reativos" não afasta linfoma.'),
      ('O que vai a fresco', 'Citometria de fluxo, teste rápido molecular '
       'para tuberculose (TRM-TB) e cultura de micobactérias e fungos precisam '
       'de tecido em soro fisiológico, sem formol. O formol preserva a '
       'morfologia e mata o resto.'),
      ('O que atrapalha', 'Corticoide reduz a celularidade e pode deixar a '
       'lâmina inconclusiva. O linfonodo menor e mais acessível tende a ser o '
       'menos alterado.'),
     ]),

    pg('tecido2', 'A cirurgia',
       'O cirurgião de cabeça e pescoço retira inteiro o maior linfonodo '
       'cervical posterior esquerdo, de 2,6 cm. Uma parte vai a fresco para '
       'citometria de fluxo, TRM-TB e cultura de micobactérias e fungos; o '
       'resto, para formol.',
       'A citometria não encontra população clonal de linfócitos B ou T. O '
       'TRM-TB não detecta //Mycobacterium tuberculosis//. O patologista chama '
       'a equipe ao microscópio antes de liberar o laudo.'),

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
         ((560, 330), (760, 250), 'Fundo **eosinofílico e granular** de necrose, sem neutrófilos.', -12),
        ],
        ['Necrose paracortical com abundante cariorrexe e histiócitos, sem '
         'neutrófilos e sem granulomas.',
         'Não é a necrose caseosa da tuberculose, que viria cercada de '
         'granulomas. Mais de uma doença produz esse padrão.']),

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

    painel('res3', 'Complemento da biópsia', 'Tecido e autoanticorpos', [
        ex('Imuno-histoquímica', 'Histiócitos CD68 e mieloperoxidase positivos · '
           'células dendríticas plasmocitoides CD123 positivas · predomínio de '
           'linfócitos T CD8', '—', True),
        ex('Células de Reed-Sternberg (CD15 / CD30)', 'Ausentes', 'ausentes'),
        ex('Pesquisa de BAAR no tecido', 'Negativa', 'negativa'),
        ex('Cultura de micobactérias e fungos', 'Em andamento', '—'),
        ex('FAN', 'Não reagente', 'não reagente'),
        ex('Anti-DNA nativo', 'Não reagente', 'não reagente'),
        ex('C3 / C4', '112 / 25 mg/dL', '90–180 / 10–40 mg/dL'),
    ], introducao='Com a lâmina, a equipe fecha as alternativas que ela '
                  'deixou abertas.'),

    pg('diagnostico', 'O diagnóstico',
       'O laudo é de **linfadenite necrosante histiocítica, a doença de '
       'Kikuchi–Fujimoto**: necrose paracortical com cariorrexe, histiócitos '
       'mieloperoxidase-positivos, células dendríticas plasmocitoides e '
       'ausência de neutrófilos e de granulomas.',
       'Descrita no Japão em 1972, é mais frequente em adultos jovens e em '
       'pessoas de ascendência asiática, como o pai de Bianca. A causa é '
       'desconhecida; a hipótese mais aceita é uma resposta imune exagerada, '
       'mediada por linfócitos T, a um gatilho que não se identifica. O quadro '
       'típico é o dela: linfonodos cervicais posteriores dolorosos, febre e, '
       'em boa parte dos casos, leucopenia; alguns têm exantema.',
       'O risco está na confusão. A lâmina lembra linfoma, e a febre com '
       'emagrecimento lembra tuberculose. Por isso o diagnóstico é '
       'histológico, e o FAN negativo afasta hoje a linfadenite lúpica, que '
       'tem a mesma aparência.'),

    painel('res3b', 'No dia do laudo', 'Sangue', [
        ex('Hemoglobina', '11,4 g/dL', '12–16 g/dL', True),
        ex('Leucócitos / neutrófilos', '2.600 / 1.350 por mm³', 'L 4.000–11.000 · N 1.800–7.500', True),
        ex('Plaquetas', '176.000/mm³', '150.000–450.000/mm³'),
        ex('Ferritina', '480 ng/mL', '15–150 ng/mL', True),
        ex('Triglicerídeos, em jejum', '126 mg/dL', 'até 150 mg/dL'),
        ex('Fibrinogênio', '390 mg/dL', '200–400 mg/dL'),
    ], introducao='Febre de semanas com leucopenia persistente: a equipe '
                  'procura uma complicação rara dessa doença.'),

    Q('p6', 5,
      'A dúvida é síndrome hemofagocítica. Pelos critérios HLH-2004, **quais '
      'duas** afirmações estão corretas?', [
      ('Ela preenche um critério: a febre', True),
      ('Sem diagnóstico molecular, exigem-se cinco de oito', True),
      ('A ferritina de 480 já conta', False),
      ('A leucopenia isolada conta como citopenia', False),
      ('Transaminases elevadas são critério', False),
      ('Hemofagocitose na medula é obrigatória', False),
      ('CD25 solúvel não entra nos critérios', False),
     ], [
      ('Os oito critérios', 'Febre de 38,5 °C ou mais; esplenomegalia; '
       'citopenia em duas ou três linhagens (hemoglobina abaixo de 9 g/dL, '
       'plaquetas abaixo de 100.000, neutrófilos abaixo de 1.000); '
       'triglicerídeos em jejum de 265 mg/dL ou mais ou fibrinogênio de 150 '
       'mg/dL ou menos; hemofagocitose em medula, baço ou linfonodo; atividade '
       'de células NK baixa ou ausente; ferritina de 500 ng/mL ou mais; CD25 '
       'solúvel de 2.400 U/mL ou mais. Sem mutação que confirme, são '
       'necessários cinco.'),
      ('Contando com cuidado', 'A febre de 38,8 °C conta. O baço não é '
       'palpável. Hemoglobina de 11,4, plaquetas de 176.000 e neutrófilos de '
       '1.350 não atingem nenhum corte. Triglicerídeos de 126 e fibrinogênio '
       'de 390 estão normais, e a ferritina de 480 fica abaixo de 500. É um '
       'critério de oito.'),
      ('Por que não as outras', 'Transaminases e desidrogenase láctica sobem '
       'na hemofagocitose, mas não são critério. A hemofagocitose na medula é '
       'um critério entre oito, nem necessária nem suficiente.'),
     ]),

    pagina('conduta', 'Discussão', 'Sem hemofagocitose, o que tratar',
           p('A doença é autolimitada: febre e linfonodos regridem em um a '
             'quatro meses, em geral sem tratamento específico. '
             'Anti-inflamatório não esteroide e analgésico aliviam febre e dor.'),
           p('O corticoide entra com febre alta que não cede, sintomas '
             'incapacitantes, acometimento fora do linfonodo, como meningite '
             'asséptica ou hepatite, e hemofagocitose. A hidroxicloroquina fica '
             'para doença recorrente, dependente de corticoide ou com traços de '
             'lúpus; a imunoglobulina, para casos graves e refratários.'),
           p('Não há agente infeccioso a tratar: sem granulomas, com BAAR '
             'negativo e TRM-TB não detectado, o esquema para tuberculose não se '
             'sustenta, e a cultura final será conferida. Também não há linfoma '
             'a estadiar, e o PET-CT capta nos linfonodos dessa doença, o que só '
             'confunde.')),

    pg('tratamento', 'Tratamento e seguimento',
       'Bianca recebe ibuprofeno por dez dias, sem antibiótico, e sai sabendo '
       'que o linfonodo diminui mais devagar que a febre e que o corticoide '
       'fica guardado para doença grave ou arrastada.',
       'Quatro semanas depois está afebril há oito dias. O maior linfonodo '
       'mede 1 cm e não dói. Hemoglobina 12,1 g/dL, leucócitos 4.300/mm³, PCR '
       '4 mg/L. A cultura do linfonodo termina sem crescimento em seis '
       'semanas. Voltou a trabalhar meio período.'),

    Q('p8', 6,
      'Na alta do acompanhamento agudo, **quais três** orientações estão '
      'corretas?', [
      ('Voltar se surgir artrite, fotossensibilidade ou edema', True),
      ('Seguimento clínico por alguns anos', True),
      ('Rebiopsiar linfonodo que não regride', True),
      ('PET-CT a cada seis meses', False),
      ('FAN e anti-DNA todo mês', False),
      ('Hidroxicloroquina para prevenir lúpus', False),
      ('Alta definitiva: FAN negativo afasta lúpus', False),
     ], [
      ('O lúpus', 'Uma minoria dos pacientes tem lúpus antes, junto ou anos '
       'depois do episódio, e a associação é mais comum em mulheres jovens. '
       'FAN negativo hoje não prevê o futuro. O seguimento é clínico, e ela '
       'precisa conhecer os sinais que o motivam: artrite, lesão de pele ao '
       'sol, úlceras orais, edema e urina espumosa.'),
      ('A recorrência e o linfonodo', 'A doença recorre em cerca de 3 a 4% '
       'dos casos, em geral com o mesmo quadro autolimitado. Um linfonodo que '
       'não regride no tempo esperado reabre o diferencial, inclusive linfoma, '
       'e pode pedir nova biópsia.'),
      ('O que não entra', 'Exame sem sintoma, repetido todo mês, gera '
       'falso-positivo sem mudar conduta. Hidroxicloroquina não previne lúpus '
       'em quem não o tem, e PET-CT não tem o que vigiar numa doença benigna.'),
     ]),

    pg('alta', 'Oito semanas depois',
       'Bianca está sem febre, com linfonodos de menos de 1 cm, e voltou à '
       'sala de aula. A equipe revê com ela o que aconteceu, o que esperar e '
       'quando voltar antes do retorno marcado.',
       conforme=('b1', ['f0', 'f_ripe', 'alta_cort'])),

    fim('f0', 'Recuperação sem desvios',
        'Bianca volta ao trabalho em tempo integral na sexta semana de doença, '
        'depois de dez dias de ibuprofeno e nenhum outro remédio.',
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
        'A prova tuberculínica mediu infecção, e a febre que cedeu sob o '
        'esquema cederia sozinha. Tratar sem tecido trouxe o dano do remédio e '
        'atrasou o diagnóstico.', 'medio', fecho='extensao'),

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
        'Ciclos empíricos sem diagnóstico apagam a lâmina e, se a causa fosse '
        'tuberculose ou linfoma, a teriam agravado ou escondido.', 'pior',
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
       'hidroxicloroquina, indicada para todo paciente com lúpus, bloqueio do '
       'sistema renina-angiotensina pela proteinúria e indução com a '
       'nefrologia e a reumatologia. O primeiro diagnóstico continua válido: '
       'o episódio de seis meses atrás foi a primeira manifestação de uma '
       'doença que só se declarou depois.',
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
            'Linfadenopatia localizada manda examinar a área de drenagem; '
            'generalizada, duas ou mais regiões não contíguas, aponta doença '
            'sistêmica. Idade acima de 40, sítio supraclavicular, mais de 2 '
            'cm, consistência dura, fixação, sintomas constitucionais e '
            'persistência além de quatro semanas pedem tecido.',
            'Dor no linfonodo sugere inflamação, mas não afasta neoplasia.',
            'VCA IgG e EBNA reagentes com IgM negativa é EBV antigo: a '
            'síndrome mononucleose-símile precisa de outra causa.',
            'Prova tuberculínica reagente mede infecção, não doença. Febre '
            'que cede sob tratamento empírico não confirma o diagnóstico '
            'quando a doença pode ceder sozinha.',
            'Linfonodo inteiro, o mais alterado, com parte a fresco para '
            'citometria, TRM-TB e cultura, antes de qualquer corticoide.',
            'Necrose com cariorrexe, histiócitos e nenhum neutrófilo ou '
            'granuloma, num adulto jovem com leucopenia, é doença de '
            'Kikuchi–Fujimoto: autolimitada, tratada com sintomáticos, com '
            'seguimento clínico atento ao lúpus.'),
        so_kicker=True),

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

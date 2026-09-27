"""Febre prolongada numa valvopata reumática, com baço palpável, em Sobral.

Reescrito em 26/09/2026 no molde do //New England// (piloto: leptospirose;
ver Artifacts/nejm-casos-classicos/GRAMATICA_LIDA_2026-09-26.md). Apresentação
curta, ficha, exame com os vitais em primeiro, primeiros exames entregues
prontos. As primeiras perguntas interpretam números (a anemia, a urina com o
complemento) e a equipe registra a âncora correta para aquele momento: febre
prolongada com esplenomegalia e hiperglobulinemia numa moradora de área de
calazar, com linfoma e tuberculose na mesma linha. A virada é a hemocultura
colhida antes de mais um antibiótico; o agente manda olhar o cólon antes de
se nomear a doença, e o nome só aparece no ecocardiograma, depois da metade
do percurso. As decisões de conduta continuam mudando o desfecho.

Paciente ficcional. Critérios de Duke-ISCVID 2023 (Fowler, Clin Infect Dis
2023); conduta pela diretriz da ESC de 2023; filtração pelo CKD-EPI 2021.
"""
import json
from pathlib import Path

from motor.estudo_imagem import estudo
from motor.etapas import (alt, bifurcacao, caminho, capa, desfecho, op, p,
                          pagina, painel, par, pareamento, pergunta, pontos,
                          topicos)

TITULO = 'Pequenos sinais'
RODAPE = 'Paciente ficcional · evoluções simuladas para ensino'
COR = '#db2777'
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
    capa(TITULO, fundo='cena.png', kicker='Caso interativo',
         selo='Paciente ficcional · procedência e créditos na última tela'),

    pg('historia', 'Apresentação',
       'Lúcia, costureira de 59 anos, moradora de Sobral, no Ceará, é encaminhada '
       'ao ambulatório de clínica médica por cinco semanas de febre no fim da '
       'tarde, suor à noite e cansaço. Perdeu 5 kg. "Não tenho mais força nem '
       'para a máquina de costura."',
       'Na terceira semana, a unidade básica tratou como infecção urinária, com '
       'ciprofloxacino por sete dias; a febre sumiu e voltou quatro dias depois. '
       'Na quarta semana recebeu amoxicilina por cinco dias por sinusite, sem '
       'mudança. Está sem antibiótico há seis dias e trouxe as anotações do '
       'termômetro: entre 37,8 e 38,4 °C, quase sempre depois das 16 horas.',
       'Tem dor nos joelhos e na lombar, sem inchaço. Nega tosse, disúria, '
       'diarreia, dor de garganta, manchas na pele, viagens e contato recente '
       'com tuberculose.'),

    pagina('ficha', 'Ficha do paciente', '',
           topicos(('Antecedentes', 'Hipertensão há oito anos. Febre reumática aos 11 '
                    'anos; o posto acompanha um sopro, e um ecocardiograma de três '
                    'anos atrás descreveu insuficiência mitral moderada. Anemia '
                    'ferropriva há seis meses, tratada com sulfato ferroso, sem outra '
                    'investigação. Duas cesáreas.'),
                   ('Medicações', 'Losartana 50 mg ao dia. O sulfato ferroso foi '
                    'suspenso há dois meses, por "estômago ruim". Paracetamol quando a '
                    'febre incomoda.'),
                   ('Hábitos', 'Nunca fumou, não bebe. Usa prótese dentária superior '
                    'e vai pouco ao dentista.'),
                   ('Vida social', 'Mora com a filha numa casa com quintal, num bairro '
                    'da periferia de Sobral, e costura em casa. Tem um gato; os '
                    'vizinhos criam cães e galinhas.'),
                   ('Família', 'Mãe morreu aos 70 anos de acidente vascular cerebral. '
                    'Um irmão tratou tuberculose pulmonar há dez anos. Sem câncer '
                    'conhecido na família.')),
           so_kicker=True),

    pagina('exame', 'Exame físico', '',
           topicos(('Sinais vitais', 'Temperatura 38,1 °C · pressão 132/70 mmHg · '
                    'frequência cardíaca 98 · frequência respiratória 18 · SpO₂ 96% '
                    'em ar ambiente · peso 54 kg.'),
                   ('Estado geral', 'Emagrecida, mucosas descoradas, anictérica.'),
                   ('Linfonodos', 'Sem adenomegalias cervicais, supraclaviculares, '
                    'axilares ou inguinais.'),
                   ('Coração', 'Ritmo regular. Sopro holossistólico 3+/6 no foco '
                    'mitral, irradiado para a axila. Sem terceira bulha.'),
                   ('Pulmões', 'Murmúrio presente, sem ruídos adventícios.'),
                   ('Abdome', 'Baço palpável a 2 cm do rebordo costal esquerdo, '
                    'indolor. Fígado no rebordo.'),
                   ('Membros e pele', 'Dor à mobilização dos joelhos, sem calor nem '
                    'derrame. Sem exantema.')),
           so_kicker=True),

    painel('res1', 'Primeiros exames', 'Sangue', [
        ex('Hemoglobina / hematócrito', '9,8 g/dL / 30%', 'Hb 12–16 g/dL', True),
        ex('VCM / RDW', '76 fL / 17,8%', '80–100 fL / 11,5–14,5%', True),
        ex('Leucócitos', '11.200/mm³ · neutrófilos 78%', '4.000–11.000/mm³', True),
        ex('Plaquetas', '180.000/mm³', '150.000–450.000/mm³'),
        ex('Ferritina / saturação da transferrina', '18 ng/mL / 7%', '15–150 ng/mL / 20–45%', True),
        ex('VHS / proteína C reativa', '86 mm/h / 74 mg/L', 'até 20 / até 5', True),
        ex('Ureia / creatinina', '48 / 1,3 mg/dL {{(TFG 47, CKD-EPI 2021)}}', 'até 42 / 0,6–1,1', True),
        ex('Proteínas totais / albumina', '7,8 / 3,0 g/dL {{(globulinas 4,8)}}', '6,0–8,0 / 3,5–5,0', True),
        ex('AST / ALT / bilirrubina total', '28 / 24 U/L / 0,6 mg/dL', 'até 40 / 41 / 1,2'),
    ], introducao='Colhidos na primeira consulta. Três pares de hemoculturas foram '
                  'colhidos por punções separadas, antes de qualquer antibiótico.'),

    painel('res1b', 'Primeiros exames', 'Urina e outros', [
        ex('Urina', 'Densidade 1.018 · 15 hemácias por campo, 40% dismórficas · proteína 1+ · sem leucocitúria', '—', True),
        ex('Proteína / creatinina na urina', '0,8 g/g', 'até 0,2 g/g', True),
        ex('Fator antinuclear', 'Não reagente', 'não reagente'),
        ex('Fator reumatoide', '64 UI/mL', 'até 14 UI/mL', True),
        ex('Complemento C3 / C4', '58 / 22 mg/dL', '90–180 / 10–40', True),
        ex('TSH', '1,8 mUI/L', '0,4–4,0 mUI/L'),
        ex('Eletrocardiograma', 'Ritmo sinusal, 96 bpm · PR 180 ms · sem outras alterações', '—'),
    ]),

    estudo('rx_adm', 'Radiografia de tórax',
           'Radiografia da primeira consulta, parte da rodada inicial de febre '
           'prolongada: procura infiltrado, cavidade e linfonodos no mediastino.',
           IMG / 'rx_torax_normal.jpg',
           'Radiografia de outro paciente · comparação didática.',
           credito_meta(IMG / 'rx_torax_normal.jpg.json'),
        [
         ((300, 180), (130, 105), '**Ápice direito** sem opacidade nem cavidade.', 12),
         ((370, 462), (140, 560), '**Hilo direito** de tamanho e densidade normais.', -12),
         ((455, 300), (620, 150), '**Traqueia** central, sem desvio; mediastino superior sem alargamento.', 12),
        ],
        ['Pulmões sem infiltrado, cavidade ou nódulo. Hilos e mediastino sem '
         'alargamento. Sem derrame pleural.',
         'Uma radiografia normal não afasta tuberculose extrapulmonar ou '
         'disseminada, nem linfoma restrito ao abdome.']),

    Q('p1', 1,
      'Hemoglobina de 9,8 g/dL, VCM de 76 fL, ferritina de 18 ng/mL e saturação '
      'da transferrina de 7%, com proteína C reativa de 74 mg/L. Como '
      'interpretar a anemia?', [
      ('Deficiência absoluta de ferro', True),
      ('Anemia da inflamação isolada', False),
      ('Traço talassêmico', False),
      ('Hiperesplenismo', False),
      ('Anemia sideroblástica', False),
      ('Hemólise crônica', False),
     ], [
      ('A leitura', 'A ferritina sobe com a inflamação. Com PCR de 74 mg/L, uma '
       'ferritina normal não afastaria a falta de ferro; uma ferritina de 18 '
       'ng/mL, abaixo de 30, a confirma. A saturação de 7% e o RDW de 17,8% '
       'completam o quadro de ferro que falta, e não de ferro retido.'),
      ('Por que não as outras', 'Na anemia da inflamação a ferritina fica normal '
       'ou alta. O traço talassêmico dá microcitose com RDW normal e ferritina '
       'preservada. Hiperesplenismo derruba também leucócitos e plaquetas, que '
       'estão normais. Na sideroblástica sobra ferro, e hemólise não é '
       'microcítica.'),
      ('O que muda', 'Numa mulher de 59 anos, depois da menopausa, falta de ferro '
       'é perda de sangue pelo tubo digestivo até prova em contrário. A diretriz '
       'da Sociedade Britânica de Gastroenterologia de 2021 indica endoscopia '
       'alta e colonoscopia nessa situação, com ou sem febre. Seis meses de '
       'sulfato ferroso sem essa investigação deixaram a pergunta aberta.'),
     ]),

    Q('p2', 2,
      'Hematúria com 40% de hemácias dismórficas, proteinúria de 0,8 g/g, C3 de '
      '58 mg/dL e C4 normal. Onde está a lesão renal, e por qual mecanismo?', [
      ('Glomerulonefrite por imunocomplexo', True),
      ('Nefrite intersticial pelo ciprofloxacino', False),
      ('Necrose tubular aguda', False),
      ('Sangramento da via urinária', False),
      ('Doença antimembrana basal glomerular', False),
      ('Nefropatia por IgA', False),
     ], [
      ('A localização', 'Hemácias dismórficas em 40% e proteinúria dizem que o '
       'sangue atravessou o glomérulo. Sem leucocitúria, a urina não tem o '
       'padrão da nefrite intersticial; sangramento de bexiga ou de cálculo dá '
       'hemácias de forma normal.'),
      ('O mecanismo', 'C3 baixo com C4 normal é consumo pela via alternativa, o '
       'que acontece quando imunocomplexos se depositam no glomérulo. Doença '
       'antimembrana basal e nefropatia por IgA não consomem complemento. A '
       'creatinina de 1,3 mg/dL, que parece pouco, já corresponde a uma '
       'filtração de 47 mL/min/1,73 m² pelo CKD-EPI 2021.'),
      ('De onde vem o imunocomplexo', 'Com FAN não reagente, lúpus fica '
       'improvável, e a crioglobulinemia costuma derrubar o C4. Sobram as '
       'infecções de curso longo, que produzem antígeno todos os dias: bactérias '
       'que persistem em algum lugar do corpo e também a leishmaniose visceral, '
       'que ainda eleva as globulinas e o fator reumatoide.'),
     ]),

    Q('p3', 3,
      'Febre há cinco semanas, baço palpável, globulinas de 4,8 g/dL e '
      'glomerulonefrite por imunocomplexo, numa moradora de Sobral. **Quais '
      'três** hipóteses a equipe precisa perseguir primeiro?', [
      ('Leishmaniose visceral', True),
      ('Linfoma', True),
      ('Tuberculose disseminada', True),
      ('Malária por Plasmodium vivax', False),
      ('Hipertireoidismo', False),
      ('Doença de Still do adulto', False),
     ], [
      ('As prováveis', 'Sobral é área de leishmaniose visceral, com cães na '
       'vizinhança: febre longa, baço grande, anemia e hiperglobulinemia são o '
       'quadro clássico. Linfoma dá febre, suor noturno e baço palpável, mesmo '
       'sem linfonodo periférico. Tuberculose disseminada dá febre vespertina e '
       'emagrecimento, com radiografia normal.'),
      ('As improváveis', 'No Ceará, malária é quase sempre importada da '
       'Amazônia, e ela não viajou. O TSH de 1,8 afasta hipertireoidismo. Still '
       'dá picos acima de 39 °C e ferritina muito alta; a dela é 18.'),
      ('Em paralelo', 'As hemoculturas incubam, colhidas seis dias depois do '
       'último antibiótico: dois cursos curtos que baixaram a febre e a deixaram '
       'voltar podem ter escondido uma bacteremia.'),
     ]),

    pg('plano', 'O que a equipe registra',
       'Lúcia é internada na enfermaria de clínica médica. Na evolução do '
       'primeiro dia, a equipe escreve: "Febre prolongada a esclarecer, com '
       'esplenomegalia, hiperglobulinemia e glomerulonefrite por imunocomplexo. '
       'Hipóteses: leishmaniose visceral, linfoma, tuberculose disseminada."',
       'Pede o teste rápido rK39, mielograma com pesquisa de formas amastigotas '
       'e cultura do aspirado para micobactérias. Mantém sem antibiótico. A '
       'endoscopia e a colonoscopia da anemia ficam "para depois de esclarecida '
       'a febre".'),

    pg('investiga', 'Primeiro dia, à tarde',
       'Teste rápido rK39: não reagente. Mielograma: medula normocelular, sem '
       'formas amastigotas, sem infiltração linfoide e sem granulomas; ferro '
       'medular ausente. A cultura para micobactérias leva semanas.',
       'A equipe mantém as três hipóteses: nem o rK39 nem o mielograma afastam '
       'o calazar com segurança, e uma punção de baço é discutida para os '
       'próximos dias.'),

    pg('segundo_dia', 'Segundo dia, 7 horas',
       'A febre de 38,4 °C voltou às 16 horas da véspera, como todos os dias. '
       'Às 7 horas, a microbiologia liga: os três pares positivaram durante a '
       'madrugada, entre 16 e 22 horas de incubação, todos com cocos '
       'gram-positivos em cadeia. A identificação e o antibiograma estão em '
       'curso.'),

    Q('p4', 4,
      'Três de três pares positivos, com cocos gram-positivos em cadeia, entre '
      '16 e 22 horas de incubação. **Quais três** afirmações estão corretas?', [
      ('Bacteremia contínua, de fonte intravascular', True),
      ('Estreptococo ou enterococo, não estafilococo', True),
      ('Positividade rápida indica inóculo alto', True),
      ('Provável contaminação da coleta', False),
      ('Os antibióticos curtos esterilizaram a fonte', False),
      ('Repetir as culturas antes de valorizar', False),
     ], [
      ('A leitura', 'Três punções separadas, com horas entre elas, todas '
       'positivas com o mesmo morfotipo: é bacteremia contínua. A bacteremia de '
       'um foco fora do vaso, como uma pielonefrite ou um abscesso, costuma ser '
       'intermitente; a contínua é a assinatura de uma fonte dentro do vaso ou '
       'do coração. Positividade em menos de 24 horas reflete muitas bactérias '
       'por mililitro de sangue.'),
      ('O gram', 'Cocos gram-positivos em cadeia são estreptococos ou '
       'enterococos. Estafilococos se agrupam em cachos.'),
      ('Por que não as outras', 'Contaminante da pele positiva um frasco de um '
       'par, e mais tarde. Os dois tratamentos curtos baixaram a febre sem '
       'apagar a fonte, como a febre que voltou mostrou. Repetir culturas não '
       'muda a leitura: três de três já são o dado.'),
     ]),

    pg('identificacao', 'Terceiro dia',
       'Com 44 horas de incubação sai a identificação: três de três pares com '
       '//Streptococcus gallolyticus// (antigo //S. bovis// biotipo I), sensível '
       'à penicilina, concentração inibitória mínima de 0,06 µg/mL.',
       'Perguntada de novo sobre o intestino, Lúcia conta que há três meses as '
       'fezes às vezes vêm mais escuras. Atribuía ao sulfato ferroso, mas o '
       'ferro foi suspenso há dois meses e as fezes escuras continuaram.'),

    Q('p5', 5,
      '//Streptococcus gallolyticus// na corrente sanguínea. **Qual** '
      'investigação ele torna obrigatória?', [
      ('Colonoscopia', True),
      ('Endoscopia digestiva alta isolada', False),
      ('Pesquisa de sangue oculto nas fezes', False),
      ('Tomografia de abdome no lugar da colonoscopia', False),
      ('Biópsia de medula óssea', False),
      ('Tomografia de crânio', False),
     ], [
      ('A associação', 'O //S. gallolyticus// vive no cólon e chega ao sangue '
       'por uma mucosa doente. Entre os pacientes com bacteremia por ele, '
       'adenomas avançados e câncer colorretal aparecem muito mais que na '
       'população geral, e a associação justifica colonoscopia em todos, mesmo '
       'sem sintoma intestinal.'),
      ('Aqui, três pistas somadas', 'A falta de ferro com ferritina de 18, o '
       'ferro medular ausente e as fezes escuras que continuaram sem o sulfato '
       'ferroso apontavam para o tubo digestivo meses antes. A anemia sozinha já '
       'pedia colonoscopia; o agente a torna inadiável.'),
      ('Por que não as outras', 'A endoscopia alta pode entrar pelas fezes '
       'escuras, mas não substitui o cólon. Sangue oculto negativo não afasta '
       'adenoma. A tomografia perde lesões pequenas e não permite biopsiar nem '
       'ressecar. Medula e crânio não respondem à pergunta que o agente faz.'),
     ]),

    pagina('beira_leito', 'À beira do leito', '',
           p('Com o agente em mãos, o residente volta ao leito e examina mãos, pés '
             'e olhos com calma, sob luz boa. Lúcia lembra de "dois caroços '
             'doloridos" na ponta dos dedos na semana anterior, que sumiram em '
             'dois dias.'),
           topicos(('Unhas', 'Três hemorragias lineares, finas e avermelhadas, sob as '
                    'unhas do segundo e do terceiro dedos da mão direita.'),
                   ('Dedos', 'Nódulo de 4 mm, doloroso, na polpa do quarto dedo direito.'),
                   ('Plantas', 'Duas máculas eritematosas de 3 mm na planta esquerda, '
                    'indolores à pressão.'),
                   ('Olhos', 'Duas petéquias na conjuntiva palpebral inferior esquerda, '
                    'vistas só com a pálpebra evertida. Fundo de olho sem '
                    'hemorragias.')),
           so_kicker=True),

    estudo('eco', 'Ecocardiograma transtorácico',
           'Bacteremia contínua por um estreptococo de origem intestinal, numa '
           'valva reumática, com lesões novas nas mãos, nos pés e na conjuntiva: '
           'o ecocardiograma é feito na mesma manhã. Corte apical de quatro '
           'câmaras.',
           IMG / 'eco_4c.jpg',
           'Quadro de vídeo de outro paciente · comparação didática.',
           credito_meta(IMG / 'eco_4c.jpg.json'),
        [
         ((743, 655), (900, 520), '**Massa ecogênica** presa à valva mitral, que no vídeo se move com os folhetos.', 12),
         ((690, 785), (880, 890), '**Átrio esquerdo**, que recebe o jato da regurgitação.', -12),
         ((535, 470), (300, 370), '**Septo interventricular**: à direita dele, o ventrículo esquerdo.', 12),
        ],
        ['Vegetação móvel de 12 mm no folheto anterior mitral. Insuficiência '
         'mitral importante ao Doppler, com jato excêntrico. Ventrículo esquerdo '
         'de tamanho normal, fração de ejeção de 62%. Sem derrame pericárdico.']),

    pg('virada', 'O diagnóstico',
       'É **endocardite infecciosa** de valva mitral nativa, sobre cardiopatia '
       'reumática, por //Streptococcus gallolyticus//.',
       'A valva deformada pela febre reumática tem endotélio irregular, onde '
       'plaquetas e fibrina formam um trombo estéril. Uma bacteremia coloniza '
       'esse trombo, e a vegetação cresce protegida dos neutrófilos, soltando '
       'bactérias no sangue o tempo todo: daí a bacteremia contínua. Os '
       'imunocomplexos explicam o fator reumatoide, o consumo de C3, a '
       'glomerulonefrite e o nódulo doloroso da polpa digital (nódulo de '
       'Osler); os microêmbolos explicam as máculas plantares (lesões de '
       'Janeway) e as petéquias conjuntivais.',
       'O curso subagudo, de semanas, é o dos estreptococos. Os dois '
       'antibióticos curtos baixaram a carga bacteriana a ponto de a febre '
       'ceder, sem esterilizar a vegetação. Calazar, linfoma e tuberculose eram '
       'as hipóteses certas para febre com baço grande em Sobral; o que as '
       'desfez foi a hemocultura colhida antes de mais um antibiótico.'),

    pareamento('p6', 'Pergunta 6',
      'Pelos critérios de Duke-ISCVID de 2023, associe cada dado de Lúcia ao '
      'critério em que ele entra.', [
      par('Três de três pares com //S. gallolyticus//',
          'Critério maior microbiológico',
          'Agente típico em duas ou mais hemoculturas separadas.'),
      par('Vegetação móvel de 12 mm na valva mitral',
          'Critério maior de imagem',
          'Evidência direta de lesão endocárdica no ecocardiograma.'),
      par('Máculas plantares indolores e petéquias conjuntivais',
          'Critério menor vascular',
          'Lesões de Janeway e hemorragia conjuntival: êmbolos em pequenos vasos.'),
      par('Fator reumatoide, nódulo de Osler e glomerulonefrite',
          'Critério menor imunológico',
          'Os três são fenômenos de imunocomplexo, e a versão de 2023 incluiu a '
          'glomerulonefrite.'),
      par('Insuficiência mitral reumática moderada',
          'Critério menor de predisposição',
          'Regurgitação mais que discreta, de qualquer causa, predispõe.'),
      par('Baço palpável a 2 cm do rebordo',
          'Não entra nos critérios',
          'Esplenomegalia é comum, mas não pontua. Infarto ou abscesso esplênico '
          'em imagem, sim.'),
    ], opcoes=['Critério maior microbiológico', 'Critério maior de imagem',
               'Critério menor vascular', 'Critério menor imunológico',
               'Critério menor de predisposição', 'Critério menor de febre',
               'Não entra nos critérios'],
    titulo_resposta='Dois maiores fecham o diagnóstico',
    nota='Dois critérios maiores bastam para endocardite definida. A febre acima '
         'de 38 °C soma como menor, e as hemorragias sob as unhas não pontuam.'),

    bifurcacao('b1', 'Decisão', 'O antibiótico',
      'Endocardite definida por estreptococo sensível à penicilina, em valva '
      'nativa, com filtração de 47 mL/min. Como tratar?', [
      caminho('Penicilina cristalina ou ceftriaxona endovenosa por quatro '
              'semanas, com transesofágico e avaliação da cirurgia cardíaca',
              'tratamento',
              'É o esquema da valva nativa por estreptococo sensível, com a '
              'equipe de endocardite desde o início.'),
      caminho('Amoxicilina oral por duas semanas, em casa', 'oral',
              'Duas semanas de oral desde o início não é esquema de '
              'endocardite, e a vegetação é grande.'),
      caminho('Vancomicina e gentamicina empíricas até o transesofágico',
              'vanco',
              'O agente e a sensibilidade já são conhecidos. Vancomicina é '
              'inferior aos betalactâmicos para estreptococo sensível, e a '
              'gentamicina lesa um rim que já filtra 47 mL/min.'),
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
       'Ceftriaxona 2 g endovenosa uma vez ao dia, que não exige ajuste para a '
       'filtração dela. A febre some no quarto dia, e as hemoculturas de '
       'controle do terceiro dia são negativas.',
       'O ecocardiograma transesofágico, pedido para procurar abscesso '
       'perivalvar e medir a lesão do folheto, fica marcado para o oitavo dia. '
       'A cirurgia cardíaca de referência já acompanha o caso.'),

    pg('piora', 'Sexto dia, madrugada',
       'Lúcia acorda sufocada e não consegue deitar. Crepitações até o terço '
       'médio dos dois pulmões, saturação de 88% em ar ambiente, pressão de '
       '100/60 mmHg, frequência cardíaca de 124. O sopro mitral ficou mais curto '
       'e surgiu uma terceira bulha. O eletrocardiograma segue com PR de 180 ms. '
       'A radiografia é feita no leito.'),

    estudo('rx_piora', 'Radiografia de tórax no leito',
           'Incidência anteroposterior, feita no leito na madrugada do sexto dia. '
           'Compare com a radiografia da admissão, que não tinha opacidades.',
           IMG / 'rx_edema.jpg',
           'Radiografia de outro paciente · comparação didática.',
           credito_meta(IMG / 'rx_edema.jpg.json'),
        [
         ((290, 540), (95, 440), '**Opacidades alveolares** confluentes no pulmão direito, a partir do hilo.', 12),
         ((740, 440), (905, 330), 'O mesmo padrão no **pulmão esquerdo**: a doença é bilateral.', -12),
         ((290, 210), (120, 120), '**Terço superior** relativamente poupado: o predomínio é central e inferior.', 12),
        ],
        ['Opacidades alveolares bilaterais, peri-hilares, que não existiam na '
         'admissão. Com a queda da saturação e as crepitações, é edema pulmonar.',
         'A instalação é aguda: a valva que passa a regurgitar de repente joga '
         'pressão num átrio esquerdo que não teve tempo de se dilatar.']),

    Q('p7', 7,
      'Na endocardite de valva nativa esquerda, **quais quatro** situações '
      'indicam cirurgia precoce?', [
      ('Insuficiência cardíaca por regurgitação grave', True),
      ('Abscesso perivalvar ou bloqueio AV novo', True),
      ('Vegetação de 10 mm ou mais após embolia', True),
      ('Hemoculturas persistentes apesar do antibiótico', True),
      ('Febre no segundo dia de antibiótico', False),
      ('PCR ainda elevada no terceiro dia', False),
      ('Hematúria da glomerulonefrite', False),
     ], [
      ('As três razões para operar', 'Pela diretriz da ESC de 2023: '
       'insuficiência cardíaca por disfunção valvar; infecção que o antibiótico '
       'não controla, como abscesso, fístula ou bacteremia persistente; e '
       'prevenção de embolia, quando a vegetação de 10 mm ou mais já embolizou '
       'ou quando se soma a outra indicação. Edema refratário ou choque pedem '
       'cirurgia de emergência, em 24 horas; regurgitação grave com sintomas '
       'de insuficiência cardíaca, cirurgia urgente, em três a cinco dias.'),
      ('Para Lúcia', 'Edema pulmonar no sexto dia, com a regurgitação '
       'importante do laudo, é a indicação mais frequente e a mais urgente: a '
       'valva perfurada não se refaz com antibiótico. A vegetação de 12 mm soma '
       'uma segunda razão. O PR de 180 ms, igual ao da admissão, é o que se '
       'vigia: um bloqueio novo sugere abscesso no anel.'),
      ('Por que não as outras', 'A febre leva de cinco a sete dias para ceder e '
       'a PCR cai devagar; nenhuma das duas indica cirurgia por si. A '
       'glomerulonefrite melhora com o controle da infecção.'),
     ]),

    bifurcacao('b2', 'Decisão', 'A valva perfurada',
      'Edema pulmonar por insuficiência mitral aguda, no sexto dia de '
      'antibiótico. O que você faz?', [
      caminho('Cirurgia cardíaca nesta internação, em caráter de urgência',
              'cirurgia',
              'Insuficiência cardíaca por destruição valvar é a indicação '
              'clássica de cirurgia precoce.'),
      caminho('Diurético e vasodilatador, e cirurgia só depois de completar as '
              'quatro semanas', 'espera',
              'A valva não vai se refazer com antibiótico, e o coração não '
              'aguenta quatro semanas de regurgitação aguda.'),
    ]),

    pg('espera', 'Nona noite',
       'Com furosemida e nitroglicerina, Lúcia melhora por dois dias. Na '
       'nona noite, entra em edema pulmonar de novo, agora com pressão de '
       '78/46 e lactato de 4,2 mmol/L. Vai para a UTI com noradrenalina.',
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
       'abscesso. A equipe faz plástica mitral com remendo de pericárdio, '
       'preservando a valva nativa. A cultura da vegetação é negativa, e o '
       'antibiótico segue contando a partir da primeira hemocultura negativa.',
       segue='colono'),

    pg('colono', 'Terceira semana de antibiótico',
       'A colonoscopia encontra uma lesão séssil de 25 mm no cólon sigmoide, '
       'ressecada em peça única por mucosectomia. Não há outras lesões até o '
       'ceco.',
       'A peça vai para a anatomia patológica.'),

    estudo('histo', 'Anatomia patológica da lesão do sigmoide',
           'Peça da mucosectomia em hematoxilina-eosina, pequeno aumento. A '
           'pergunta é o tipo de lesão e o grau de displasia.',
           IMG / 'adenoma_histo.jpg',
           'Lâmina de outro paciente · comparação didática.',
           credito_meta(IMG / 'adenoma_histo.jpg.json'),
        [
         ((445, 75), (250, 30), '**Superfície com displasia de alto grau**: núcleos que perdem a polaridade.', 12),
         ((572, 305), (700, 250), '**Projeção vilosa**, em dedo de luva, revestida por epitélio displásico.', -12),
         ((755, 525), (880, 640), '**Glândulas tubulares** cortadas de través: o componente tubular.', 12),
        ],
        ['Adenoma tubuloviloso com displasia de alto grau na superfície e de '
         'baixo grau no restante, sem invasão da submucosa. Margens livres.',
         'Adenoma avançado pelos três critérios: 10 mm ou mais, componente '
         'viloso e displasia de alto grau. A anemia de seis meses antes e as '
         'fezes escuras vinham dele.']),

    Q('p8', 8,
      'Sobre o tratamento e o seguimento de Lúcia, **quais quatro** afirmações '
      'estão corretas?', [
      ('Contar a partir da primeira hemocultura negativa', True),
      ('Completar por via oral, se estável', True),
      ('Avaliação odontológica antes da alta', True),
      ('Profilaxia antes de procedimento dentário', True),
      ('Gentamicina associada em todo esquema', False),
      ('Anticoagulação plena contra a embolia', False),
      ('Hemoculturas diárias até o fim', False),
     ], [
      ('A duração', 'São quatro semanas de betalactâmico para estreptococo '
       'sensível em valva nativa, contadas da primeira hemocultura negativa. '
       'Como a cultura da valva operada foi negativa, a cirurgia não reinicia a '
       'contagem; se fosse positiva, um curso inteiro recomeçaria.'),
      ('A via oral', 'No ensaio POET, passar para antibiótico oral depois de '
       'pelo menos dez dias endovenosos, ou sete depois da cirurgia, em '
       'pacientes estáveis e sem abscesso, não foi inferior. A ESC de 2023 '
       'incorporou essa possibilidade.'),
      ('Os dentes', 'Ela usa prótese e vai pouco ao dentista. Focos dentários '
       'tratados antes da alta reduzem o risco de nova infecção, e a '
       'endocardite prévia, com ou sem anel ou remendo, indica profilaxia com '
       'amoxicilina 2 g antes de procedimentos que manipulam a gengiva, pela '
       'AHA de 2021 e pela ESC de 2023.'),
      ('O que não entra', 'Gentamicina não acrescenta nada ao estreptococo '
       'sensível e lesa o rim. Anticoagulação não reduz a embolia e aumenta o '
       'sangramento cerebral. Hemoculturas se repetem até a primeira negativa, '
       'e de novo se a febre voltar.'),
     ]),

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
        'fração de ejeção preservada. Seguimento com a cardiologia, reposição '
        'de ferro e colonoscopia de vigilância em três anos.',
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

    pagina('retrospectiva', 'Pontos de ensino', '',
        pontos(
            'Febre que cede com antibiótico curto e volta pede hemoculturas '
            'colhidas sem antibiótico, antes do próximo; numa valvopata, antes '
            'de qualquer outro passo.',
            'Ferritina abaixo de 30 ng/mL confirma falta de ferro mesmo com '
            'inflamação. Depois da menopausa, falta de ferro é perda digestiva '
            'até prova em contrário e pede endoscopia alta e colonoscopia.',
            'Hematúria dismórfica com C3 baixo é glomerulonefrite por '
            'imunocomplexo; com FAN negativo e febre há semanas, a fonte mais '
            'comum é uma infecção persistente.',
            'Três de três hemoculturas positivas são bacteremia contínua, a '
            'marca de uma fonte intravascular. Cocos em cadeia são estreptococos '
            'ou enterococos.',
            '//Streptococcus gallolyticus// no sangue obriga a colonoscopia, '
            'mesmo sem sintoma intestinal.',
            'Insuficiência cardíaca por regurgitação valvar é a principal '
            'indicação de cirurgia precoce, sem esperar o fim do antibiótico.',
            'Depois do primeiro episódio, a paciente passa a ter indicação de '
            'profilaxia antes de procedimentos dentários que manipulam a '
            'gengiva.'),
        so_kicker=True),

    pg('referencias', 'Fontes e limites',
       'Paciente, valores e percursos são ficcionais. A cena de abertura é uma '
       'ilustração autoral gerada por inteligência artificial para este caso; '
       'não é fotografia nem documentação clínica.',
       'Fowler e cols. The 2023 Duke-ISCVID Criteria for Infective '
       'Endocarditis, Clin Infect Dis 2023. Delgado e cols. 2023 ESC Guidelines '
       'for the management of endocarditis, Eur Heart J 2023. Iversen e cols. '
       'POET, N Engl J Med 2019. Wilson e cols. Prevention of Viridans Group '
       'Streptococcal Infective Endocarditis, Circulation 2021. Snook e cols. '
       'British Society of Gastroenterology guidelines for the management of '
       'iron deficiency anaemia in adults, Gut 2021. Haidar e Singh. Fever of '
       'Unknown Origin, N Engl J Med 2022. Ministério da Saúde, Manual de '
       'Vigilância e Controle da Leishmaniose Visceral.',
       'Imagens, todas de outros pacientes, com setas adicionadas: radiografia '
       'de tórax normal, Mikael Häggström, Wikimedia Commons, CC0; '
       'ecocardiograma apical de quatro câmaras, CardioNetworks ECHOpedia (AMC '
       'Echolab), Wikimedia Commons, CC BY-SA 3.0, quadro extraído do vídeo '
       'E00405; radiografia de tórax no leito, Jeremy Jones (Radiopaedia), '
       'Wikimedia Commons, CC BY-SA 3.0; micrografia de adenoma tubuloviloso, '
       'Mikael Häggström, Wikimedia Commons, CC0.'),
]

REVISAO = []

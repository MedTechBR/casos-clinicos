"""Febre, diarreia e citopenias no quarto mês de um transplante renal.

Reescrito no molde do //New England// lido em 26/09/2026 (ver
Artifacts/nejm-casos-classicos/GRAMATICA_LIDA_2026-09-26.md), com o piloto da
leptospirose como modelo: apresentação curta, ficha com a pista enterrada (a
profilaxia antiviral encerrada há quatro semanas), exame com os sinais vitais
primeiro, primeiros exames em dois painéis sem pergunta antes. As primeiras
perguntas classificam a diarreia, a lesão do enxerto, a tomografia e as
citopenias. A âncora, registrada pela equipe, é colite pelo micofenolato com
desidratação e tacrolimo acima do alvo; a lâmina da colonoscopia vira o caso,
e o nome do agente só aparece na página "O diagnóstico", perto de 57% do
percurso. As decisões de conduta continuam mudando o desfecho.

Paciente ficcional; sem doses numéricas de antiviral, porque a prescrição
depende da função renal e do protocolo do serviço. Condutas conferidas no
Fourth International Consensus Guidelines on the Management of
Cytomegalovirus in Solid Organ Transplantation (Kotton e cols.,
Transplantation 2025).
"""
from pathlib import Path

from motor.estudo_imagem import estudo
from motor.etapas import (alt, bifurcacao, caminho, capa, desfecho, op, p,
                          pagina, painel, par, pareamento, pergunta, pontos,
                          topicos, vitais)

TITULO = 'Depois da travessia'
RODAPE = 'Paciente ficcional · evoluções simuladas para ensino'
COR = '#ca8a04'
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


def fim(k, titulo, texto, porque, qualidade):
    return desfecho(k, titulo, p(texto), qualidade=qualidade, porque=porque,
                    fecho='retrospectiva')


ETAPAS = [
    capa(TITULO, fundo=CENA, kicker='Caso interativo',
         selo='Paciente ficcional · procedência e créditos na última tela'),

    pg('historia', 'Apresentação',
       'Helena, 58 anos, costureira aposentada, volta ao hospital do '
       'transplante por seis dias de diarreia e cansaço. Recebeu um rim há '
       'quatro meses. Há dois dias tem febre de até 38,4 °C e não termina as '
       'refeições.',
       'São seis a oito evacuações aquosas por dia, com cólica. No começo '
       'vinham depois das refeições; agora continuam em jejum e a acordam à '
       'noite. Na unidade básica recebeu soro oral e foi orientada a procurar '
       'a equipe do transplante. Perdeu 2 kg na semana e acha que urina menos.',
       'Nega sangue nas fezes, vômitos, dor sobre o enxerto, disúria, tosse, '
       'falta de ar, manchas na pele, viagem e comida fora de casa.'),

    pagina('ficha', 'Ficha do paciente', '',
           topicos(('Antecedentes', 'Doença renal do diabetes e da hipertensão, '
                    'três anos de hemodiálise. Transplante de doador falecido há '
                    'quatro meses, indução com timoglobulina, sem rejeição. '
                    'Creatinina basal depois do transplante: 1,2 mg/dL.'),
                   ('Medicações', 'Tacrolimo, micofenolato mofetil 1 g de 12 em 12 '
                    'horas, prednisona 5 mg, insulina glargina e regular, '
                    'anlodipino, omeprazol e sulfametoxazol-trimetoprima em dias '
                    'alternados. Valganciclovir nos três primeiros meses, '
                    'suspenso há quatro semanas, no prazo do protocolo. '
                    'Amoxicilina-clavulanato por sete dias, há cinco semanas, '
                    'por sinusite.'),
                   ('Hábitos', 'Não fuma nem bebe. Água filtrada em casa.'),
                   ('Vida social', 'Mora com o marido em Fortaleza. Cuida à tarde '
                    'da neta de quatro anos, que vai à creche e teve três dias '
                    'de diarreia no mês passado.'),
                   ('Família', 'Mãe diabética, morta de infarto aos 70 anos. Dois '
                    'irmãos hipertensos. Sem doença intestinal na família.')),
           so_kicker=True),

    pagina('exame', 'Exame físico', '',
           vitais(('Temperatura', '38,2 °C', True),
                  ('Pressão arterial', '100/62', False),
                  ('Frequência cardíaca', '108', True),
                  ('Frequência respiratória', '18', False),
                  ('SpO₂ em ar ambiente', '97%', False)),
           topicos(('Estado geral', 'Alerta, orientada, mucosas secas, sem '
                    'icterícia.'),
                   ('Cardiopulmonar', 'Taquicardia regular, sem sopros. Pulmões '
                    'limpos.'),
                   ('Abdome', 'Dor difusa leve à palpação, maior no flanco '
                    'esquerdo, sem defesa. Ruídos aumentados. Fígado e baço não '
                    'palpáveis. Enxerto na fossa ilíaca direita indolor, sem '
                    'sopro.'),
                   ('Pele e membros', 'Sem exantema, sem edema. Fístula '
                    'arteriovenosa no braço esquerdo, com frêmito.'),
                   ('Neurológico', 'Sem déficit focal, sem tremor.')),
           so_kicker=True),

    painel('res1', 'Primeiros exames', 'Sangue', [
        ex('Hemoglobina', '10,1 g/dL', '12–16 g/dL', True),
        ex('Leucócitos', '2.100/mm³ · neutrófilos 1.200 · linfócitos 400', '4.000–11.000/mm³', True),
        ex('Plaquetas', '112.000/mm³', '150.000–400.000/mm³', True),
        ex('Ureia / creatinina', '96 / 2,1 mg/dL {{(basal 1,2)}}', 'até 42 / 1,1 mg/dL', True),
        ex('Sódio / potássio / cloro', '134 / 3,4 / 108 mmol/L', 'Na 135–145 · K 3,5–5,0 · Cl 98–107', True),
        ex('Bicarbonato', '18 mmol/L', '22–28 mmol/L', True),
        ex('AST / ALT', '62 / 71 U/L', 'até 35 / 35 U/L', True),
        ex('Albumina', '3,2 g/dL', '3,5–5,0 g/dL', True),
        ex('Proteína C-reativa', '8,6 mg/dL', 'até 0,5 mg/dL', True),
    ], introducao='Duas hemoculturas são colhidas na chegada.'),

    painel('res1b', 'Primeiros exames', 'Fezes, urina e nível do tacrolimo', [
        ex('Tacrolimo, nível de vale', '14 ng/mL', 'alvo da equipe 5–8 ng/mL', True),
        ex('Urina', 'Densidade 1.024 · sem proteína, sangue ou leucócitos · sedimento sem cilindros', '—'),
        ex('Sódio / creatinina urinários', '18 mmol/L / 90 mg/dL · FENa 0,3%', '—', True),
        ex('Sódio / potássio fecais', '90 / 35 mmol/L', '—', True),
        ex('Calprotectina fecal', '640 µg/g', 'até 50 µg/g', True),
        ex('//Clostridioides difficile//: GDH e toxina', 'Negativos', 'negativos'),
        ex('Painel molecular gastrointestinal', 'Nenhum agente detectado', 'negativo'),
    ]),

    Q('p1', 1,
      'Com a história e os exames de fezes, **quais duas** características '
      'definem esta diarreia?', [
      ('Secretora', True),
      ('Inflamatória', True),
      ('Osmótica', False),
      ('Disabsortiva, com esteatorreia', False),
      ('Por trânsito acelerado', False),
      ('Funcional', False),
     ], [
      ('O hiato osmótico', 'O hiato osmótico fecal é 290 menos duas vezes a '
       'soma de sódio e potássio fecais: 290 − 2 × (90 + 35) = 40 mOsm/kg. '
       'Abaixo de 50 a água sai puxada por eletrólitos, o que define a '
       'diarreia secretora; acima de 125, por um soluto não absorvido, na '
       'osmótica. Continuar em jejum e acordar à noite confirmam.'),
      ('A inflamação', 'Calprotectina de 640 µg/g, febre e proteína C-reativa '
       'de 8,6 mg/dL indicam mucosa inflamada, com neutrófilos na parede. A '
       'diarreia é secretora e inflamatória ao mesmo tempo, o padrão das '
       'colites.'),
      ('Por que não as outras', 'Osmótica pararia em jejum e teria hiato alto. '
       'Esteatorreia não dá febre nem calprotectina alta. Trânsito acelerado '
       'e diarreia funcional não acordam a paciente nem inflamam a mucosa.'),
      ('O que esse padrão pede', 'No transplantado, colite quer dizer infecção '
       'ou fármaco. Com //C. difficile// e painel negativos, o micofenolato, '
       'que lesa a mucosa do cólon, passa ao primeiro plano.'),
     ]),

    Q('p2', 2,
      'Creatinina de 2,1 mg/dL (basal 1,2), FENa de 0,3% e tacrolimo de 14 '
      'ng/mL. **Quais dois** mecanismos explicam melhor a piora do enxerto?', [
      ('Hipovolemia pela perda intestinal', True),
      ('Vasoconstrição aferente pelo tacrolimo', True),
      ('Lesão tubular aguda', False),
      ('Rejeição aguda celular', False),
      ('Trimetoprima bloqueando a secreção de creatinina', False),
      ('Nefrite intersticial pela amoxicilina', False),
      ('Obstrução do ureter do enxerto', False),
     ], [
      ('A classificação', 'FENa de 0,3%, urina concentrada e sedimento sem '
       'cilindros mostram um túbulo que ainda reabsorve sódio: a lesão é '
       'pré-renal. Mucosas secas, frequência de 108 e pressão de 100/62 com '
       'oito evacuações por dia explicam a perda de volume.'),
      ('O tacrolimo', 'A diarreia reduz o metabolismo do tacrolimo na parede '
       'do intestino, e o nível sobe sem mudança de dose. Acima do alvo, ele '
       'contrai a arteríola aferente e também baixa a FENa. Os dois mecanismos '
       'somam.'),
      ('Por que não as outras', 'Lesão tubular teria FENa acima de 2% e '
       'cilindros granulosos. Rejeição só se investiga se a creatinina não '
       'voltar depois de volume e nível corrigidos. A trimetoprima já era usada '
       'com creatinina de 1,2. Sem exantema nem leucócitos na urina, nefrite '
       'intersticial é pouco provável; obstrução se afasta com ultrassom.'),
     ]),

    pg('ancora', 'O que a equipe registra',
       'Hipótese do plantão: colite pelo micofenolato, com lesão pré-renal do '
       'enxerto e tacrolimo acima do alvo. //C. difficile// e painel de fezes '
       'negativos.',
       'Cristaloide, dose do tacrolimo reduzida pelo nível e micofenolato '
       'cortado à metade. O ultrassom com Doppler do enxerto não mostra '
       'obstrução nem alteração vascular.',
       'No terceiro dia a creatinina está em 1,6 mg/dL. A febre continua, com '
       'picos de 38,6 °C, e a dor no flanco esquerdo aumenta.'),

    estudo('tc_abdome', 'Tomografia de abdome',
           'Terceiro dia. Tomografia com contraste venoso, depois da '
           'hidratação, para procurar complicação da colite. A imagem é de '
           'outro paciente, com o padrão descrito no laudo de Helena. Onde '
           'está a doença?',
           IMG / 'tc_colite.jpg',
           'Tomografia de outro paciente, corte axial · comparação didática.',
           credito_meta(IMG / 'tc_colite.jpg.json'),
        [
         ((430, 150), (400, 32), '**Cólon transverso** com parede espessada e mucosa '
          'edemaciada, que faz saliências para a luz.', 12),
         ((250, 320), (62, 205), '**Cólon ascendente**: o mesmo espessamento.', -12),
         ((775, 300), (945, 215), '**Cólon descendente**: o mesmo espessamento, do '
          'lado da dor.', 12),
        ],
        ['Espessamento parietal difuso do cólon, nos segmentos ascendente, '
         'transverso e descendente, com edema da mucosa. Intestino delgado sem '
         'alterações. Sem pneumatose, sem ar fora das alças, sem coleção.',
         'É uma pancolite sem complicação. A tomografia localiza a doença no '
         'cólon, mas não diz a causa.']),

    Q('p3', 3,
      'Nessa colite, **quais três** achados, se aparecessem na tomografia, '
      'levariam a cirurgia?', [
      ('Ar livre na cavidade', True),
      ('Pneumatose com gás na veia porta', True),
      ('Cólon transverso acima de 6 cm', True),
      ('Parede do cólon acima de 1 cm', False),
      ('Densificação da gordura pericólica', False),
      ('Pequena quantidade de líquido livre', False),
      ('Linfonodos mesentéricos aumentados', False),
     ], [
      ('Sinais cirúrgicos', 'Ar livre é perfuração. Pneumatose com gás no '
       'sistema porta, num paciente com dor e acidose, indica necrose da '
       'parede. Cólon transverso acima de 6 cm, com toxemia, é megacólon '
       'tóxico. Os três pedem cirurgião na hora, qualquer que seja a causa '
       'da colite.'),
      ('O que acompanha qualquer colite', 'Espessamento parietal, mesmo acima '
       'de 1 cm, densificação da gordura, pouco líquido livre e linfonodos '
       'reativos medem a inflamação. Não definem causa nem indicação '
       'cirúrgica.'),
      ('No imunossuprimido', 'A prednisona e os antiproliferativos embotam a '
       'dor e a defesa abdominal. Perfuração pode chegar com pouca clínica, e '
       'a tomografia é repetida quando a dor muda ou o lactato sobe.'),
     ]),

    pg('antibiotico', 'Sem sinal cirúrgico',
       'Pela febre numa imunossuprimida com pancolite, a equipe colhe novas '
       'hemoculturas e inicia ceftriaxona e metronidazol. A hipótese '
       'registrada continua a mesma: colite pelo micofenolato, agora com '
       'infecção bacteriana a afastar.'),

    pg('quinto_dia', 'Quinto dia',
       'Depois de 48 horas de antibiótico, a febre segue com picos de 38,6 °C '
       'e sete evacuações líquidas por dia, ainda sem sangue. As hemoculturas '
       'estão negativas em 72 horas. Creatinina 1,5 mg/dL.',
       'Hemoglobina 9,6 g/dL, leucócitos 1.800/mm³ com neutrófilos 950/mm³, '
       'plaquetas 98.000/mm³, AST 88 e ALT 94 U/L. Não há esplenomegalia nem '
       'linfonodos palpáveis.'),

    Q('p4', 4,
      'Três linhagens em queda no quinto dia, com febre. **Quais três** causas '
      'podem estar contribuindo?', [
      ('Micofenolato mofetil', True),
      ('Sulfametoxazol-trimetoprima', True),
      ('Infecção viral sistêmica', True),
      ('Tacrolimo acima do alvo', False),
      ('Prednisona de manutenção', False),
      ('Hiperesplenismo', False),
      ('Deficiência de folato ou de B12', False),
     ], [
      ('As drogas', 'O micofenolato é antiproliferativo e tóxico para a medula '
       'conforme a dose, e a redução à metade leva dias para aparecer no '
       'hemograma. O sulfametoxazol-trimetoprima é antifolato e soma a sua '
       'mielotoxicidade.'),
      ('O que as drogas não explicam', 'Febre que não cede com 48 horas de '
       'antibiótico e hemoculturas negativas, transaminases subindo de 62/71 '
       'para 88/94 e queda de neutrófilos de 1.200 para 950 com o micofenolato '
       'já reduzido: uma infecção viral sistêmica precisa entrar na lista.'),
      ('Por que não as outras', 'A toxicidade do tacrolimo é renal, '
       'neurológica e metabólica; citopenia é rara. Corticoide eleva os '
       'leucócitos por desmarginação. Sem baço palpável não há hiperesplenismo, '
       'e carência vitamínica não derruba três linhagens em cinco dias.'),
     ]),

    pg('colonoscopia', 'Sexto dia',
       'Para confirmar a colite pelo micofenolato e afastar outra causa, a '
       'equipe pede colonoscopia. Helena está estável, sem sinais peritoneais.',
       'No transverso e no descendente há úlceras rasas, bem delimitadas, de '
       'bordas nítidas, separadas por mucosa quase normal. O reto está '
       'poupado. São feitas biópsias da borda e do fundo das úlceras.'),

    estudo('histologia_baixo', 'Biópsia do cólon: aumento intermediário',
           'A lâmina do fundo de uma úlcera. A imagem é de outro paciente com '
           'o mesmo laudo. Descreva a mucosa antes de procurar a célula que '
           'decide.',
           IMG / 'colon_baixo.jpg',
           'Mucosa colônica em hematoxilina-eosina · outro paciente.',
           credito_meta(IMG / 'colon_baixo.jpg.json'),
        [
         ((300, 229), (230, 90), '**Lâmina própria** tomada por infiltrado inflamatório denso, sem criptas nessa região.', 12),
         ((854, 457), (965, 143), '**Criptas** remanescentes, distorcidas e afastadas umas das outras.', -12),
         ((500, 150), (560, 55), '**Superfície** irregular, com perda do epitélio de revestimento.', 12),
        ],
        ['Colite ativa com distorção e perda de criptas. Nesse aumento, '
         'procuram-se células grandes no estroma e no endotélio.',
         'O micofenolato também distorce criptas: o que separa as causas está '
         'no grande aumento.']),

    estudo('histologia_alto', 'Biópsia do cólon: grande aumento',
           'A mesma úlcera em grande aumento. Que alteração celular aparece?',
           IMG / 'colon_alto.jpg',
           'Hematoxilina-eosina, grande aumento · outro paciente.',
           credito_meta(IMG / 'colon_alto.jpg.json'),
        [
         ((743, 551), (930, 640), '**Inclusão intranuclear** grande e densa, que ocupa quase todo o núcleo.', 12),
         ((765, 420), (910, 300), '**Citomegalia**: célula várias vezes maior que as vizinhas, junto ao vaso.', -12),
         ((300, 795), (130, 900), '**Infiltrado inflamatório** misto na lâmina própria.', 12),
        ],
        ['Efeito citopático viral: células aumentadas, com inclusão '
         'intranuclear cercada de halo, no estroma e no endotélio.',
         'A imuno-histoquímica foi pedida no mesmo bloco.']),

    pg('diagnostico', 'O diagnóstico',
       'Laudo de Helena: colite ulcerada com efeito citopático e '
       '**imuno-histoquímica positiva para citomegalovírus**. Lâmina e clínica '
       'fecham doença gastrointestinal por CMV comprovada.',
       'O citomegalovírus fica latente depois da primeira infecção, e a grande '
       'maioria dos adultos brasileiros o carrega. A imunidade de linfócitos T '
       'o mantém quieto; timoglobulina, micofenolato e corticoide a derrubam. '
       'Chega também no rim de um doador soropositivo. O vírus infecta '
       'endotélio e estroma e produz úlceras; no sangue, dá febre, leucopenia, '
       'plaquetopenia e hepatite leve.',
       'O trato gastrointestinal é o órgão mais acometido no transplantado. A '
       'doença costuma surgir nos primeiros meses depois do fim da profilaxia, '
       'e o valganciclovir de Helena acabou quatro semanas antes da diarreia. '
       'A redução do micofenolato, feita pela hipótese anterior, já era parte '
       'do tratamento.'),

    pareamento('p5', 'Pergunta 5',
      'Na colite do transplantado, a lâmina decide. Associe cada achado '
      'histológico ao diagnóstico.', [
      par('Pseudomembranas com exsudato em jato saindo das criptas',
          '//Clostridioides difficile//',
          'Fibrina, neutrófilos e muco em "vulcão". O teste de fezes de Helena '
          'foi negativo.'),
      par('Apoptose de criptas sem inclusões virais, sob micofenolato',
          'Colite pelo micofenolato',
          'Lembra a doença do enxerto contra o hospedeiro e pode coexistir com a '
          'infecção. Era a hipótese do plantão.'),
      par('Células multinucleadas, núcleos em vidro fosco e moldagem',
          'Herpes-simples',
          'Multinucleação e marginação da cromatina. Mais no esôfago e no reto '
          'que no cólon.'),
      par('Infiltrado linfoide atípico com EBER positivo',
          'Doença linfoproliferativa pós-transplante',
          'Linfócitos B transformados pelo vírus Epstein-Barr. A conduta muda: '
          'redução da imunossupressão e rituximabe.'),
      par('Atrofia de criptas e lâmina própria hialinizada',
          'Colite isquêmica',
          'Criptas "fantasmas" e hialinização, sem inclusões. Poupa o reto e '
          'prefere as flexuras.'),
    ], opcoes=['Citomegalovírus', '//Clostridioides difficile//',
               'Colite pelo micofenolato', 'Herpes-simples',
               'Doença linfoproliferativa pós-transplante', 'Colite isquêmica'],
    titulo_resposta='Cada agente assina a lâmina de um jeito',
    nota='A opção que sobrou é a de Helena: citomegalia com inclusão '
         'intranuclear em "olho de coruja", no endotélio e no estroma, e '
         'imuno-histoquímica positiva.'),

    painel('res2', 'Sétimo dia', 'Plasma e prontuário', [
        ex('PCR quantitativa de CMV no plasma', '18.600 UI/mL', 'limite de quantificação 137 UI/mL', True),
        ex('IgG anti-CMV antes do transplante', 'Doador positivo · receptora positiva', '—'),
        ex('Tacrolimo, nível de vale', '7,2 ng/mL', 'alvo da equipe 5–8 ng/mL'),
        ex('Creatinina', '1,9 mg/dL {{(1,5 no quinto dia)}}', 'basal 1,2 mg/dL', True),
        ex('Neutrófilos', '900/mm³', '1.500–7.500/mm³', True),
        ex('Evacuações', 'Sete por dia, febre de 38,5 °C', '—', True),
    ], introducao='Com o laudo, a equipe pede a carga viral no plasma e resgata as '
                  'sorologias do pré-transplante.'),

    Q('p6', 6,
      'Doença comprovada no tecido e PCR de 18.600 UI/mL no plasma. **Quais '
      'duas** afirmações sobre a carga estão corretas?', [
      ('Será a linha de base da resposta', True),
      ('Na doença intestinal, pode vir baixa', True),
      ('Dispensaria a biópsia neste caso', False),
      ('Abaixo de 50.000, excluiria doença invasiva', False),
      ('Deve ser conferida em outro laboratório', False),
      ('Sugere resistência ao valganciclovir', False),
     ], [
      ('Para que serve agora', 'A carga guia o tratamento: é medida toda semana, '
       'no mesmo ensaio e no mesmo tipo de amostra, e o tratamento só termina '
       'quando ela cai abaixo do limiar do laboratório. Plasma e sangue total, '
       'ou dois ensaios diferentes, não se comparam.'),
      ('O intestino e o sangue', 'A doença gastrointestinal pode ter carga '
       'baixa ou indetectável, sobretudo em receptores soropositivos como '
       'Helena. Carga alta sugere, mas não localiza a doença nem exclui outra '
       'colite; nenhum limiar exclui doença invasiva. Por isso o tecido '
       'decide.'),
      ('Por que não resistência', 'Doença que aparece semanas depois do fim da '
       'profilaxia é o padrão esperado. Resistência se suspeita durante o '
       'tratamento, depois de exposição prolongada e resposta ruim.'),
     ]),

    bifurcacao('b1', 'Decisão', 'Tratar a doença comprovada',
      'Sete evacuações por dia, febre, neutrófilos de 900 e creatinina de '
      'novo em alta, 1,9 mg/dL, com a imunossupressão reduzida. A nefrologia '
      'lembra que rejeição é possível. Como você conduz?', [
      caminho('Ganciclovir endovenoso já, dose pela função renal', 'inicio_antiviral',
              'Doença intestinal grave com diarreia: a absorção oral é incerta, e '
              'a creatinina sobe com a perda de volume.'),
      caminho('Valganciclovir oral em dose de tratamento', 'oral',
              'Serve para doença leve a moderada; com sete evacuações, a '
              'absorção não é garantida.'),
      caminho('Pulso de metilprednisolona pela creatinina; antiviral depois',
              'imunossupressao',
              'Rejeição não foi demonstrada, e mais imunossupressão cai sobre '
              'uma infecção invasiva ativa.'),
    ]),

    pg('oral', 'Cinco dias de valganciclovir',
       'Sete evacuações por dia, febre de 38 °C à tarde. A PCR repetida no '
       'mesmo ensaio não caiu. Albumina 2,8 g/dL; creatinina 1,8 mg/dL.',
       segue='resgate_oral'),

    bifurcacao('resgate_oral', 'Decisão', 'A carga que não cai',
      'Qual a conduta?', [
      caminho('Trocar para ganciclovir endovenoso', 'inicio_antiviral',
              'Garante a exposição ao fármaco enquanto o intestino não absorve.'),
      caminho('Pedir genotipagem e manter o oral até o resultado', 'piora_oral',
              'Cinco dias de tratamento não bastam para suspeitar de resistência, '
              'e a exposição continua incerta.'),
    ]),

    pg('piora_oral', 'Mais uma semana',
       'Aparece sangue nas fezes e a hemoglobina cai para 8,4 g/dL. A '
       'genotipagem não mostra mutações de resistência. A equipe do '
       'transplante troca para ganciclovir endovenoso.',
       segue='inicio_antiviral'),

    pg('imunossupressao', '48 horas de pulso',
       'A febre chega a 39 °C, a diarreia aumenta e aparece sangue. A '
       'creatinina não cai. A tomografia repetida mostra o mesmo espessamento, '
       'sem ar fora das alças.',
       segue='resgate_corticoide'),

    bifurcacao('resgate_corticoide', 'Decisão', 'A piora sob corticoide',
      'Como prosseguir?', [
      caminho('Parar o pulso, iniciar ganciclovir e reavaliar o enxerto',
              'inicio_antiviral',
              'Tira a prioridade de uma rejeição não demonstrada sem suspender a '
              'imunossupressão de base.'),
      caminho('Completar o pulso e deixar o antiviral para depois',
              'insistencia',
              'Mais imunossupressão sobre uma infecção invasiva em curso.'),
    ]),

    pg('insistencia', '72 horas depois',
       'Dor intensa no flanco esquerdo, defesa abdominal, pressão de 82/50 e '
       'lactato de 3,8 mmol/L. A tomografia mostra ar extraluminal junto ao '
       'cólon descendente.',
       'Ressuscitação, antibiótico para sepse abdominal, ganciclovir e '
       'cirurgia de urgência. A peça mostra colite ulcerada com perfuração e '
       'imuno-histoquímica positiva para CMV.',
       segue='f3'),

    pg('inicio_antiviral', 'Tratar a doença',
       'Ganciclovir endovenoso, com dose ajustada à função renal e revista a '
       'cada nova creatinina. A data da primeira dose endovenosa passa a ser o '
       'D0. O micofenolato segue na metade e o tacrolimo, no alvo.',
       'Com hidratação, a creatinina volta a 1,5 mg/dL em dois dias, o que '
       'tira a rejeição da frente.'),

    painel('semana1', 'D7', 'A primeira semana de ganciclovir', [
        ex('PCR de CMV no plasma, D0', '18.600 UI/mL', 'mesmo ensaio', True),
        ex('PCR de CMV no plasma, D7', '3.200 UI/mL', 'limite de quantificação 137 UI/mL', True),
        ex('Neutrófilos', '700/mm³', '1.500–7.500/mm³', True),
        ex('Hemoglobina / plaquetas', '9,4 g/dL / 104.000/mm³', '12–16 g/dL / 150.000–400.000/mm³', True),
        ex('Creatinina', '1,4 mg/dL', 'basal 1,2 mg/dL', True),
        ex('Evacuações', 'Quatro por dia, sem sangue · febre em resolução', '—'),
    ], introducao='A carga caiu quase seis vezes em uma semana.'),

    Q('p7', 7,
      'Neutrófilos de 700/mm³ no D7, com febre em resolução e carga em queda. '
      'Qual o próximo passo?', [
      ('Reduzir a dose do ganciclovir', False),
      ('Trocar para foscarnet', False),
      ('Suspender micofenolato e trocar sulfametoxazol-trimetoprima', True),
      ('Pausar o antiviral até recuperar', False),
      ('Letermovir em dose de tratamento', False),
     ], [
      ('Poupar a medula sem enfraquecer o antiviral', 'O consenso de 2025 '
       'recomenda retirar os outros mielotóxicos antes de mexer no antiviral. '
       'O micofenolato é suspenso por ora e a profilaxia de pneumocistose '
       'passa a atovaquona. Fator estimulador de colônias é seguro e pode ser '
       'usado se a contagem cair mais.'),
      ('A dose do ganciclovir', 'Segue a função renal, não o hemograma. '
       'Subdose ou pausa no meio do tratamento de doença invasiva prolongam a '
       'replicação e favorecem a seleção de resistência.'),
      ('Por que não as outras', 'Foscarnet é nefrotóxico e causa distúrbios '
       'de cálcio, magnésio e potássio; fica para intolerância grave ou '
       'resistência, assim como o maribavir, onde disponível. O letermovir '
       'não trata doença estabelecida: tem barreira baixa à resistência e é '
       'usado em profilaxia.'),
     ]),

    pg('evolucao2', 'D14',
       'Sem o micofenolato e com a profilaxia trocada, os neutrófilos sobem '
       'para 1.400/mm³. Creatinina 1,3 mg/dL. Afebril, uma a duas evacuações '
       'formadas por dia, comendo bem.',
       'A PCR de CMV do D14 é **620 UI/mL**, ainda quantificável. O residente '
       'pergunta se já é hora de genotipar o vírus.'),

    Q('p8', 8,
      '**Quais três** achados, juntos, indicariam genotipagem de resistência '
      'ao ganciclovir?', [
      ('Quatro semanas ou mais de antiviral', True),
      ('Carga sem queda após duas semanas', True),
      ('Carga acima de 1.000 UI/mL', True),
      ('Carga de 620 após queda contínua', False),
      ('Neutropenia durante o tratamento', False),
      ('Carga que sobe na primeira semana', False),
      ('Carga inicial acima de 10.000 UI/mL', False),
     ], [
      ('O critério', 'O consenso de 2025 indica genotipagem depois de '
       'exposição prolongada ao antiviral, de pelo menos quatro semanas, com '
       'resposta ruim depois de duas semanas de dose plena. O teste é feito com '
       'carga acima de 1.000 UI/mL, porque abaixo disso a leitura das mutações '
       'é pouco confiável.'),
      ('O caso de Helena', 'Duas semanas de tratamento, carga de 18.600 para '
       '3.200 e depois 620 UI/mL: queda de 30 vezes. É resposta, e 620 está '
       'abaixo do limite para genotipar.'),
      ('Por que não as outras', 'Carga estável ou em alta na primeira semana '
       'acontece pela cinética do vírus e não prediz resistência. Neutropenia '
       'é toxicidade. Carga inicial alta pede tratamento, não genotipagem.'),
     ]),

    bifurcacao('b2', 'Decisão', 'O fim do tratamento',
      'D14, sintomas resolvidos, absorção confiável e carga de 620 UI/mL. '
      'Como seguir?', [
      caminho('Valganciclovir oral em dose de tratamento, com nova carga em '
              'uma semana', 'resposta',
              'Cumpre as duas semanas mínimas e espera o limiar virológico.'),
      caminho('Encerrar agora e manter só vigilância', 'recaida',
              'O mínimo de duração não basta com a carga acima do limiar.'),
    ]),

    pg('resposta', 'D21',
       'Série semanal: 18.600 → 3.200 → 620 → **abaixo de 137 UI/mL**. '
       'Assintomática, comendo, hemograma em recuperação.',
       'O tratamento termina com clínica resolvida, mais de duas semanas de '
       'terapia e uma amostra abaixo do limite de quantificação de um ensaio '
       'sensível. A carga segue semanal por oito a doze semanas.',
       conforme=('b1', ['f1', 'f2', 'f2'])),

    fim('f1', 'Retorno ao ambulatório',
        'Helena mantém alimentação, enxerto com creatinina de 1,3 mg/dL e '
        'hemograma em recuperação. O micofenolato volta em dose menor, com a '
        'carga viral semanal.',
        'Antiviral endovenoso logo depois do tecido, medula protegida sem '
        'subdose e término só abaixo do limiar foram as três decisões que '
        'contaram.', 'melhor'),

    pg('recaida', 'D28',
       'Duas semanas depois de parar, voltam a febre e seis evacuações '
       'líquidas por dia. Carga de CMV **9.800 UI/mL**, creatinina 1,8 mg/dL.',
       'O tratamento foi interrompido com 620 UI/mL, e a queda foi contínua '
       'enquanto ele durou. O padrão é de interrupção precoce.',
       segue='resgate_recaida'),

    bifurcacao('resgate_recaida', 'Decisão', 'A recorrência',
      'Como abordar?', [
      caminho('Reiniciar ganciclovir e revisar dose, absorção e outras causas',
              'retratamento', 'A interrupção precoce explica a volta.'),
      caminho('Trocar para foscarnet e pedir genotipagem', 'revisao_resistencia',
              'Resistência é hipótese, mas a curva durante o tratamento não '
              'a sustenta.'),
    ]),

    pg('revisao_resistencia', 'Antes da troca',
       'A infectologia revê a série: queda contínua sob tratamento, '
       'interrupção acima do limiar e duas semanas de exposição. A troca '
       'reflexa para foscarnet é suspensa pelo risco renal.',
       segue='retratamento'),

    pg('retratamento', 'Novo curso',
       'Ganciclovir endovenoso, depois valganciclovir em dose de tratamento. '
       'Carga semanal: 9.800 → 1.700 → 280 → abaixo de 137 UI/mL. Termina no '
       'D21 do novo curso.',
       segue='f2'),

    fim('f2', 'Recuperação mais longa',
        'A infecção é controlada e a creatinina volta a 1,4 mg/dL, com mais '
        'duas a três semanas de internação ou de tratamento.',
        'Tratamento por via incerta, corticoide para uma rejeição não '
        'demonstrada ou término com a carga ainda quantificável prolongaram a '
        'doença.', 'medio'),

    fim('f3', 'Perfuração e diálise',
        'Depois da colectomia parcial e do controle da sepse, Helena segue '
        'internada, dependente de diálise por lesão renal aguda. A '
        'recuperação do enxerto é incerta.',
        'O corticoide dado para uma rejeição não demonstrada, sobre uma '
        'colite viral sem tratamento, contribuiu para um desfecho que o '
        'antiviral precoce provavelmente teria evitado.', 'pior'),

    pagina('retrospectiva', 'Pontos de ensino', '',
        pontos(
            'Diarreia que continua em jejum, com hiato osmótico fecal abaixo de '
            '50 e calprotectina alta, é secretora e inflamatória: no '
            'transplantado, colite por infecção ou por fármaco.',
            'Na piora do enxerto durante diarreia, FENa baixa e tacrolimo acima '
            'do alvo apontam para volume e droga; rejeição se investiga depois '
            'de corrigi-los.',
            'Febre que não cede com antibiótico e citopenias que avançam com o '
            'micofenolato já reduzido pedem uma causa além das drogas.',
            'O fim da profilaxia com valganciclovir abre a janela da doença por '
            'citomegalovírus, e o intestino é o órgão mais acometido.',
            'A carga no plasma mede replicação e guia o tratamento; a doença '
            'intestinal se comprova no tecido, e pode ter carga baixa.',
            'No tratamento: ganciclovir endovenoso na doença grave, retirar '
            'mielotóxicos em vez de reduzir o antiviral, e terminar só com '
            'clínica resolvida e carga abaixo do limiar.'),
        so_kicker=True),

    pg('referencias', 'Fontes e limites',
       'Paciente, séries laboratoriais e percursos são ficcionais. Não há '
       'doses numéricas de antiviral: a prescrição depende da função renal e '
       'do protocolo do serviço. A cena de abertura é uma ilustração autoral '
       'gerada por inteligência artificial; não é fotografia nem documentação '
       'clínica.',
       'Kotton CN e cols. The Fourth International Consensus Guidelines on the '
       'Management of Cytomegalovirus in Solid Organ Transplantation. '
       'Transplantation 2025;109(7):1066–1110 (diagnóstico, duração do '
       'tratamento, neutropenia e critérios de genotipagem).',
       'Tomografia: Hellerhoff, Wikimedia Commons, CC BY-SA 4.0, painel axial '
       'recortado de "Clostridien Colitis 68M - CT KM pv - 001". Histologia: '
       'Nephron, Wikimedia Commons, CC BY-SA 3.0 ("CMV colitis - intermed '
       'mag" e "CMV colitis - high mag - cropped"). Todas de outros pacientes, '
       'com setas adicionadas.'),
]

REVISAO = []

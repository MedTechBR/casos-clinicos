"""Caso ficcional para raciocínio clínico em residência de clínica médica.

Revisão editorial: integração de dados, seleção limitada de exames e
explicações após a resposta. Fontes clínicas ao final deste arquivo.
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
    """Alternativas curtas e explicação única após a seleção limitada."""
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
      'Diarreia noturna que persiste em jejum, Na/K fecais 90/35 e calprotectina 640. Quais duas hipóteses de mecanismo permanecem prioritárias?', [
      ('Colite infecciosa não inteiramente coberta pelo painel de fezes', True),
      ('Lesão intestinal relacionada ao micofenolato', True),
      ('Diarreia osmótica isolada por carboidrato não absorvido', False),
      ('Síndrome funcional como explicação principal', False),
      ('Insuficiência pancreática exócrina como mecanismo dominante', False),
     ], [
      ('Integração', 'Hiato fecal = 290 − 2 × (90 + 35) = 40, com persistência em jejum: predomina secreção. Febre e calprotectina elevada sustentam inflamação, compatível com infecção ou lesão medicamentosa; calprotectina não as separa.'),
      ('Concorrentes', 'Painel negativo não pesquisa toda infecção nem substitui tecido. Diarreia osmótica isolada deveria diminuir em jejum e ter hiato maior. Sintomas noturnos, febre e inflamação pesam contra causa funcional. Não há esteatorreia ou contexto que priorize insuficiência pancreática.'),
     ]),

    pagina('colite_tx', 'Discussão', 'Colite no transplantado',
           p('No receptor de órgão sólido, as causas de colite se dividem em dois '
             'grupos: infecção e fármaco. A imunossupressão amplia o primeiro e '
             'muda a apresentação do segundo.'),
           p('Entre as infecções, os testes de fezes de Helena afastaram '
             '//C. difficile// e os agentes do painel molecular. Isso reduz a '
             'lista, mas não a esgota: o painel não cobre todos os agentes, e '
             'alguns só se mostram na mucosa.'),
           p('Entre os fármacos, o micofenolato é o mais frequente. Lesa o '
             'epitélio do cólon de modo dependente da dose e pode surgir em '
             'qualquer fase do transplante. O diagnóstico é de exclusão, ou vem '
             'da biópsia.')),

    Q('p2', 2,
      'Oito evacuações/dia, creatinina 2,1, FENa 0,3%, sedimento inativo e tacrolimo 14 ng/mL. Qual combinação explica melhor a disfunção inicial do enxerto?', [
      ('Depleção de volume somada à vasoconstrição pelo tacrolimo', True),
      ('Rejeição celular somada à nefrite por amoxicilina', False),
      ('Toxicidade tubular comprovada pelo sedimento inativo', False),
      ('Elevação isolada da creatinina pela trimetoprima crônica', False),
      ('Glomerulonefrite com retenção tubular de sódio', False),
     ], [
      ('Dois mecanismos convergentes', 'Perdas digestivas, mucosas secas e taquicardia favorecem depleção. Tacrolimo acima do alvo pode somar vasoconstrição renal, mesmo sem alteração da dose; a diarreia muda sua exposição. FENa baixa apoia retenção de sódio, mas não comprova causa pré-renal.'),
      ('O que falta às concorrentes', 'Rejeição não está excluída e merece avaliação se a disfunção persistir após correção. Sedimento inativo não comprova nem exclui toxicidade tubular. Trimetoprima já era usada com creatinina basal normal; não integra a mudança aguda. Ausência de hematúria/proteinúria torna glomerulonefrite menos provável.'),
     ]),

    pagina('enxerto', 'Discussão', 'A creatinina do enxerto',
           p('A equipe revê os dois mecanismos pré-renais. O volume se explica '
             'pelas oito evacuações por dia. O segundo está na ficha: o '
             'tacrolimo de 14 ng/mL, acima do alvo de 5 a 8, sem mudança de '
             'dose.'),
           p('A diarreia reduz o metabolismo do tacrolimo na parede do '
             'intestino, e o nível sobe. Acima do alvo, ele contrai a arteríola '
             'aferente e também baixa a FENa.'),
           p('Rejeição só se investiga se a creatinina não voltar depois de '
             'volume e nível corrigidos. A trimetoprima, que bloqueia a secreção '
             'de creatinina, já era usada com creatinina de 1,2. A amoxicilina '
             'de cinco semanas atrás pouco sugere nefrite intersticial sem '
             'exantema nem leucócitos na urina.')),

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

    pagina('sinais_cirurgicos', 'Discussão', 'Quando a colite é cirúrgica',
           topicos(('Sinais que pedem cirurgião', 'Ar livre na cavidade é '
                    'perfuração. Pneumatose com gás no sistema porta, com dor e '
                    'acidose, indica necrose da parede. Cólon transverso acima '
                    'de 6 cm, com toxemia, é megacólon tóxico. Valem para '
                    'qualquer causa de colite.'),
                   ('O que só mede a inflamação', 'Espessamento parietal, mesmo '
                    'acima de 1 cm, densificação da gordura, pouco líquido livre '
                    'e linfonodos reativos. Não definem causa nem indicação '
                    'cirúrgica.'),
                   ('No imunossuprimido', 'Prednisona e antiproliferativos embotam '
                    'a dor e a defesa abdominal. Perfuração pode chegar com pouca '
                    'clínica, e a tomografia é repetida quando a dor muda ou o '
                    'lactato sobe.')),
           p('O laudo de Helena não mostra nenhum dos três: é uma pancolite '
             'sem complicação.')),

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

    pagina('citopenias', 'Discussão', 'Três linhagens em queda',
           p('Hemoglobina, neutrófilos e plaquetas caem juntos. Sem baço '
             'palpável, perda por sequestro fica improvável, e a pergunta passa '
             'a ser o que está suprimindo a medula.'),
           p('Duas drogas da prescrição fazem isso. O micofenolato é '
             'antiproliferativo e tóxico para a medula conforme a dose; a redução '
             'à metade leva dias para aparecer no hemograma. O '
             'sulfametoxazol-trimetoprima é antifolato e soma a sua '
             'mielotoxicidade. Tacrolimo raramente causa citopenia, corticoide '
             'eleva os leucócitos, e carência vitamínica não derruba três '
             'linhagens em cinco dias.'),
           p('O que a hipótese medicamentosa não explica bem: febre que não cede com 48 horas de '
             'antibiótico e hemoculturas negativas, transaminases subindo de '
             '62/71 para 88/94 e neutrófilos caindo de 1.200 para 950 com o '
             'micofenolato já reduzido. Uma infecção viral sistêmica entra na '
             'lista.')),

    Q('p5', 3,
      'No D5, febre e diarreia persistem, com citopenias e transaminases em alta, apesar da redução do micofenolato. Quais dois exames priorizar para definir a causa da colite?', [
      ('Colonoscopia com biópsias para histologia e imuno-histoquímica', True),
      ('PCR quantitativa de CMV no plasma', True),
      ('Repetir o mesmo painel molecular gastrointestinal sem nova exposição', False),
      ('IgM anti-CMV para comprovar invasão intestinal', False),
      ('Biópsia do enxerto antes de investigar a mucosa', False),
      ('Nova tomografia abdominal para definir o agente', False),
     ], [
      ('Doença local e replicação', 'Colonoscopia com tecido: após testes fecais negativos e persistência clínica, distingue lesão medicamentosa e infecção invasiva; histologia e IHQ procuram o agente na mucosa. PCR plasmática: pesquisa replicação sistêmica e oferece linha de base se houver doença por CMV; não substitui biópsia e pode ser baixa na doença intestinal.'),
      ('Por que não os demais', 'Mesmo painel de fezes: sem nova pista, repete as limitações do primeiro. IgM anti-CMV: não comprova invasão tecidual, sobretudo no transplantado. Biópsia do enxerto: creatinina melhorou para 1,5 e ela não esclarece primeiro a colite. Nova TC: indicada se houver suspeita de complicação, mas não determina o agente nesta pancolite estável.'),
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
         ((400, 930), (130, 900), '**Infiltrado inflamatório** misto na lâmina própria.', 12),
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




    painel('res2', 'Sétimo dia', 'Plasma e prontuário', [
        ex('PCR quantitativa de CMV no plasma', '18.600 UI/mL', 'limite de quantificação 137 UI/mL', True),
        ex('IgG anti-CMV antes do transplante', 'Doador positivo · receptora positiva', '—'),
        ex('Tacrolimo, nível de vale', '7,2 ng/mL', 'alvo da equipe 5–8 ng/mL'),
        ex('Creatinina', '1,9 mg/dL {{(1,5 no quinto dia)}}', 'basal 1,2 mg/dL', True),
        ex('Neutrófilos', '900/mm³', '1.500–7.500/mm³', True),
        ex('Evacuações', 'Sete por dia, febre de 38,5 °C', '—', True),
    ], introducao='Após a investigação da mucosa, chega a carga viral plasmática. '
                  'A equipe também resgata as sorologias do pré-transplante.'),

    Q('p6', 4,
      'IHQ positiva no cólon, PCR plasmática 18.600 e doadora/receptora soropositivas. Quais duas interpretações melhor orientam a avaliação inicial?', [
      ('A imunossupressão permite doença intestinal por CMV em receptora previamente soropositiva', True),
      ('A PCR seriada no mesmo ensaio ajuda a medir resposta ao tratamento', True),
      ('A DNAemia favorece atribuir as citopenias ao vírus e manter os mielotóxicos na dose atual', False),
      ('A soropositividade do doador favorece transmissão pelo enxerto em relação à reativação da receptora', False),
      ('A profilaxia prévia e a carga atual favorecem resistência como explicação principal da doença', False),
     ], [
      ('Doença e seguimento', 'Clínica e IHQ na lesão comprovam doença intestinal, possível por reativação ou reinfecção em receptora soropositiva sob imunossupressão. A PCR no mesmo ensaio e tipo de amostra oferece linha de base e permite seguir a resposta.'),
      ('Inferências concorrentes', 'Vírus e fármacos podem somar mielotoxicidade; a DNAemia não discrimina suas contribuições nem justifica manter doses sem revisão. D+/R+ não permite priorizar transmissão pelo enxerto sobre reativação. Exposição prévia ao antiviral entra na avaliação de resistência, mas doença após o fim da profilaxia, antes de observar a resposta terapêutica, favorece inicialmente doença pós-profilaxia, não resistência como causa principal.'),
     ]),

    pg('visita7', 'Sétimo dia, na visita',
       'A creatinina voltou a subir, 1,9 mg/dL, com o tacrolimo no alvo. A '
       'nefrologia lembra que no quarto mês a rejeição é possível e que ela '
       'ainda não foi afastada por biópsia.',
       'A diarreia segue com sete evacuações por dia e a febre com 38,5 °C. Os '
       'neutrófilos estão em 900/mm³, com o micofenolato já na metade. Helena '
       'come pouco.'),

    bifurcacao('b1', 'Decisão', 'Tratar a doença comprovada',
      'Doença por CMV comprovada no cólon, diarreia intensa e creatinina em '
      'alta com a imunossupressão reduzida. Como você conduz?', [
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

    Q('p7', 5,
      'No D7 de ganciclovir, carga 18.600 → 3.200 e neutrófilos 900 → 700/mm³, com melhora clínica. Quais duas medidas são mais adequadas agora?', [
      ('Rever micofenolato e sulfametoxazol-trimetoprima como mielotóxicos associados', True),
      ('Manter dose antiviral de tratamento revista pela função renal atual', True),
      ('Reduzir ganciclovir pela metade apenas pela contagem de neutrófilos', False),
      ('Trocar para foscarnet por presumida resistência virológica', False),
      ('Encerrar o antiviral após a primeira queda de carga', False),
     ], [
      ('Resposta e toxicidade', 'Queda virológica com melhora clínica favorece eficácia, enquanto a neutropenia pode ter contribuições do vírus e de várias drogas. Revisar os mielotóxicos com a equipe do transplante, considerar G-CSF e manter vigilância permite preservar tratamento efetivo.'),
      ('Alternativas próximas', 'A dose de ganciclovir deve acompanhar a função renal, que melhorou, e não ser reduzida apenas pela leucopenia. Foscarnet traz nefrotoxicidade sem evidência atual de resistência; reserva-se para situações apropriadas de intolerância ou resistência. Carga ainda quantificável e doença recente não sustentam término.'),
     ]),

    pg('evolucao2', 'D14',
       'A PCR de CMV do D14 é **620 UI/mL**, ainda quantificável. A série '
       'semanal, no mesmo ensaio: 18.600 → 3.200 → 620 UI/mL.',
       'O residente pergunta se já é hora de genotipar o vírus.'),

    Q('p8', 6,
      'D14: PCR 18.600 → 3.200 → 620 UI/mL no mesmo ensaio. Quais três exames priorizar no seguimento para decidir dose, segurança e término?', [
      ('PCR quantitativa semanal no mesmo ensaio', True),
      ('Hemograma com diferencial', True),
      ('Creatinina seriada para rever a função renal', True),
      ('Genotipagem de resistência agora', False),
      ('Nova colonoscopia para comprovar cura antes da avaliação clínica', False),
      ('IgM anti-CMV seriada', False),
     ], [
      ('O que cada exame decide', 'PCR semanal: verifica supressão até o limiar do serviço, além da resolução clínica; a curva atual é de resposta. Hemograma: acompanha neutropenia e efeito da revisão de mielotóxicos. Creatinina: função renal em recuperação exige revisar a dose, evitando subexposição ou toxicidade.'),
      ('Por que não agora', 'Genotipagem: queda contínua não sugere refratariedade e 620 UI/mL reduz a confiabilidade técnica; a profilaxia conta como exposição prévia, mas não muda essa interpretação da resposta. Colonoscopia: não é controle rotineiro de cura se houver boa evolução clínica/virológica; entra se sintomas persistirem ou voltarem. IgM: não mede resposta nem orienta término.'),
     ]),

    pg('visita14', 'D14, na visita',
       'Sem o micofenolato e com a profilaxia trocada, os neutrófilos sobem '
       'para 1.400/mm³. Creatinina 1,3 mg/dL. Afebril, uma a duas evacuações '
       'formadas por dia, comendo bem.',
       'Faz duas semanas de ganciclovir endovenoso. A equipe discute o que '
       'falta para terminar o tratamento.'),

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

# Fontes conferidas na revisão das questões (22/10/2026):
# https://pmc.ncbi.nlm.nih.gov/articles/PMC12180710/

# Referência de construção dos itens (aplicação e opções plausíveis):
# https://www.nbme.org/sites/default/files/2021-02/NBME_Item%20Writing%20Guide_R_6.pdf

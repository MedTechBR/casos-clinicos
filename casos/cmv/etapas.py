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
                    'suspenso há quatro semanas conforme plano individual de três meses de profilaxia; a equipe revê esse prazo à luz da indução com timoglobulina. '
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

    painel('res1b', 'Primeiros exames', 'Urina', [
        ex('Urina', 'Densidade 1.024 · sem proteína, sangue ou leucócitos · sedimento sem cilindros', '—'),
    ], introducao='Urina avaliada diante da menor diurese e disfunção do enxerto.'),

    pg('reavaliacao_perdas', 'Reavaliação durante a hidratação',
       'Após a reposição inicial, a pressão sobe e a tontura diminui, mas Helena volta a evacuar e tem cólica. Mantém mucosas secas e não consegue compensar todas as perdas por boca. A creatinina acima da basal torna necessária a revisão da exposição ao tacrolimo.',
       'Solicitam-se nível de vale do tacrolimo e investigação de fezes, pela diarreia febril sob imunossupressão e exposição recente a antibiótico. A febre e as citopenias também justificam investigação viral dirigida desde o primeiro atendimento; esses pedidos são feitos em paralelo, sem esperar os exames fecais.'),

    painel('diarreia_dirigida', 'Investigação dirigida', 'Fezes e exposição ao tacrolimo', [
        ex('Tacrolimo, nível de vale', '14 ng/mL', 'alvo da equipe 5–8 ng/mL', True),
        ex('//Clostridioides difficile//: GDH e toxina', 'Negativos', 'negativos'),
        ex('Painel molecular gastrointestinal', 'Nenhum agente detectado', 'negativo'),
    ], introducao='A interpretação considera quais agentes o painel local efetivamente pesquisa. Os resultados chegam ao longo do primeiro dia, com hidratação e vigilância do enxerto em curso.'),

    Q('p1', 1,
      'Quais duas causas você prioriza na investigação inicial?', [
      ('Colite infecciosa não inteiramente coberta pelo painel de fezes', True),
      ('Lesão intestinal relacionada ao micofenolato', True),
      ('Diarreia osmótica por má absorção de carboidratos', False),
      ('Síndrome funcional', False),
      ('Insuficiência pancreática exócrina', False),
     ], [('Integração', 'Febre, sintomas noturnos, perda de peso e imunossupressão sustentam doença orgânica. Infecção e lesão por micofenolato continuam prioritárias; esses dados não distinguem as duas nem definem sozinhos um mecanismo secretor puro.'), ('Concorrentes', 'Painel negativo não pesquisa toda infecção nem substitui tecido. Diarreia causada apenas por carboidrato não absorvido costuma diminuir com o jejum. Sintomas noturnos, febre e inflamação pesam contra causa funcional. Não há esteatorreia ou contexto que priorize insuficiência pancreática.'), ('Como organizar a diarreia', 'No transplantado, infecção e toxicidade de medicamentos podem coexistir. O painel de fezes não cobre todas as causas e resultado negativo não prova efeito do micofenolato. Duração, febre, citopenias e endoscopia mudam a investigação.')]),

    pagina('colite_tx', 'Discussão', 'Colite no transplantado',
           p('No receptor de órgão sólido, as causas de colite se dividem em dois '
             'grupos: infecção e fármaco. A imunossupressão amplia o primeiro e '
             'muda a apresentação do segundo.'),
           p('Entre as infecções, os testes de fezes de Helena reduziram a probabilidade de '
             '//C. difficile// e os agentes do painel molecular. Isso reduz a '
             'lista, mas não a esgota: o painel não cobre todos os agentes, e '
             'alguns só se mostram na mucosa.'),
           p('Entre os fármacos, o micofenolato é o mais frequente. Lesa o '
             'epitélio do cólon de modo dependente da dose e pode surgir em '
             'qualquer fase do transplante. O diagnóstico é de exclusão, ou vem '
             'da biópsia.')),

    Q('p2', 2,
      'Qual mecanismo melhor explica a alteração da função do enxerto?', [
      ('Depleção de volume somada à vasoconstrição pelo tacrolimo', True),
      ('Rejeição celular somada à nefrite por amoxicilina', False),
      ('Toxicidade tubular comprovada pelo sedimento inativo', False),
      ('Inibição da secreção de creatinina pela trimetoprima', False),
      ('Glomerulonefrite com retenção tubular de sódio', False),
     ], [
      ('Dois mecanismos convergentes', 'Perdas digestivas, mucosas secas e taquicardia favorecem depleção. Tacrolimo acima do alvo pode somar vasoconstrição renal, mesmo sem alteração da dose; a diarreia muda sua exposição.'),
      ('O que falta às concorrentes', 'Rejeição não está excluída e merece avaliação se a disfunção persistir após correção. Sedimento inativo não comprova nem exclui toxicidade tubular. Trimetoprima já era usada com creatinina basal normal; não integra a mudança aguda. Ausência de hematúria/proteinúria torna glomerulonefrite menos provável.'),
     ]),

    pagina('enxerto', 'Discussão', 'A creatinina do enxerto',
           p('A equipe revê os mecanismos hemodinâmicos. O volume se explica '
             'pelas oito evacuações por dia. O segundo está na ficha: o '
             'tacrolimo de 14 ng/mL, acima do alvo de 5 a 8, sem mudança de '
             'dose.'),
           p('A diarreia reduz o metabolismo do tacrolimo na parede do '
             'intestino, e o nível sobe. Acima do alvo, ele contrai a arteríola '
             'aferente, podendo agravar a disfunção hemodinâmica.'),
           p('O enxerto é avaliado desde a admissão; disfunção persistente após corrigir volume e exposição ao tacrolimo reforça a indicação de biópsia. Não é preciso esperar se houver suspeita independente de rejeição. A trimetoprima, que bloqueia a secreção '
             'de creatinina, já era usada com creatinina de 1,2. A exposição à amoxicilina '
             'de cinco semanas atrás é menos convincente como causa principal, mas ausência de exantema ou leucocitúria não exclui nefrite intersticial.')),

    Q('p5', 3,
      'Após a avaliação inicial, quais dois exames você solicita?', [
      ('Biópsia de mucosa colônica', True),
      ('PCR quantitativa de CMV no plasma', True),
      ('Repetir o mesmo painel molecular gastrointestinal sem nova exposição', False),
      ('IgM anti-CMV', False),
      ('Biópsia do enxerto antes de investigar a mucosa', False),
      ('Tomografia de abdome', False),
     ], [('Doença local e replicação', 'Colonoscopia com tecido: após testes fecais negativos e persistência clínica, distingue lesão medicamentosa e infecção invasiva; o estudo do tecido e a imuno-histoquímica (coloração que procura proteínas do agente na amostra) ajudam a demonstrar infecção na mucosa. PCR plasmática: pesquisa replicação sistêmica e oferece linha de base se houver doença por CMV; não substitui biópsia e pode ser baixa na doença intestinal.'), ('Por que não os demais', 'Mesmo painel de fezes: sem nova pista, repete as limitações do primeiro. IgM anti-CMV: não comprova invasão tecidual, sobretudo no transplantado. Biópsia do enxerto: pode ser necessária conforme a evolução renal, mas não esclarece a causa da colite; a avaliação renal corre em paralelo. Nova TC: indicada se houver suspeita de complicação, mas não determina o agente nesta pancolite estável.'), ('Sangue e tecido respondem a perguntas diferentes', 'Detectar DNA viral no sangue demonstra replicação, mas não comprova que ele explique a lesão intestinal. Histologia e imuno-histoquímica procuram o vírus no órgão afetado. Essa distinção evita tratar uma carga detectável como explicação automática para toda diarreia.')]),

    pg('ancora', 'Primeiras 24 horas: melhora incompleta',
       'Cristaloide e reposição de potássio melhoram sede, tontura ao levantar e diurese. Pressão 118/70, frequência 88 e creatinina 1,6 mg/dL. A ultrassonografia com Doppler não mostra obstrução ou alteração vascular. A equipe ajusta tacrolimo e reduz micofenolato, considerando toxicidade associada.',
       'Durante o dia são quatro evacuações, mas à noite voltam as cólicas, a urgência e seis evacuações que a despertam. O apetite continua ruim. Corrigir a depleção melhorou o enxerto e o estado circulatório, sem resolver a doença intestinal.'),

    pg('evolucao_local', 'Segundo dia: muda o padrão da dor',
       'Helena passa a sentir dor também entre as evacuações, localizada no lado esquerdo. Há sensibilidade mais nítida nesse local, sem defesa ou distensão; mantém eliminação de gases e lactato normal. A mudança exige procurar complicação, embora ainda não indique cirurgia.',
       'A PCR plasmática de CMV colhida na admissão retorna em 18.600 UI/mL. O registro pré-transplante já mostra D+/R+. A presença de DNA do vírus no sangue aumenta a suspeita, mas não separa colite invasiva de outra causa coexistente. A endoscopia com biópsia foi solicitada desde o primeiro dia. A medida da quantidade de vírus no sangue depende da rede do transplante; o envio da amostra não substitui a avaliação do intestino.'),

    estudo('tc_abdome', 'Tomografia de abdome',
           'Segundo dia. Tomografia com contraste venoso, depois da hidratação, para procurar complicação da colite. Onde está a doença?',
           IMG / 'tc_colite.jpg',
           'Tomografia, corte axial.',
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
         'Espessamento envolvendo múltiplos segmentos colônicos, sem os sinais de complicação descritos acima.']),

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

    pg('quinto_dia', 'Terceiro dia: manifestação intestinal nova',
       'Surge pequena quantidade de sangue misturada às fezes e sensação de evacuação incompleta. Helena precisa ir ao banheiro oito vezes, dorme mal e não consegue terminar a refeição. Continua hemodinamicamente estável, sem queda aguda de hemoglobina nem sinais peritoneais.',
       'Leucócitos 1.800/mm³, neutrófilos 950/mm³ e plaquetas 98.000/mm³; AST/ALT 88/94 U/L. A piora local, apesar de melhor hidratação e menor micofenolato, torna inadequado apenas aguardar a resposta à redução do fármaco. Infecção e toxicidade podem coexistir.'),

    bifurcacao('b_amostra', 'Decisão', 'Como obter o tecido',
      'Com pancolite sem complicação na TC, DNA do vírus no sangue e piora intestinal, qual procedimento priorizar para a amostragem?', [
      caminho('Colonoscopia com biópsias dirigidas', 'amostra_completa',
              'Permite mapear segmentos e colher tecido das úlceras, ponderando preparo e risco com a endoscopia.'),
      caminho('Retossigmoidoscopia com biópsias dirigidas', 'amostra_distal',
              'Pode reduzir o preparo e fornecer diagnóstico se houver lesão acessível; amostra distal negativa pode não representar todo o cólon.'),
    ]),

    pg('amostra_completa', 'Preparar sem agravar a depleção',
       'A endoscopia considera o procedimento completo seguro após hidratação e correção eletrolítica, com preparo supervisionado e monitorização da função renal. Não há peritonismo, dilatação importante ou suspeita de perfuração.',
       segue='colonoscopia'),

    pg('amostra_distal', 'Amostra de menor extensão',
       'O exame de menor extensão alcança úlceras no descendente distal e permite biópsia dirigida. Se apenas mucosa normal tivesse sido amostrada, a persistência da suspeita exigiria ampliar a investigação; uma amostra negativa não excluiria doença proximal.',
       segue='colonoscopia'),

    pg('colonoscopia', 'Terceiro dia: endoscopia e amostra',
       'A endoscopia colônica encontra úlceras rasas bem delimitadas, separadas por mucosa quase normal, no descendente examinado. O reto está poupado. São feitas biópsias dirigidas, com histologia e imuno-histoquímica solicitadas no mesmo material.',
       'A estabilidade permite colher tecido antes do antiviral com laudo prioritário. Se surgisse instabilidade ou atraso relevante na amostragem, o tratamento seria iniciado diante da forte suspeita. No exame completo, avaliam-se também os outros segmentos; a amostra deve representar a lesão.'),

    estudo('histologia_baixo', 'Biópsia do cólon: aumento intermediário',
           'A lâmina do fundo de uma úlcera. Descreva a mucosa antes de procurar a célula que decide.',
           IMG / 'colon_baixo.jpg',
           'Mucosa colônica em hematoxilina-eosina.',
           credito_meta(IMG / 'colon_baixo.jpg.json'),
        [
         ((300, 229), (230, 90), '**Lâmina própria** tomada por infiltrado inflamatório denso, sem criptas nessa região.', 12),
         ((854, 457), (965, 143), '**Criptas** remanescentes, distorcidas e afastadas umas das outras.', -12),
         ((500, 150), (560, 55), '**Superfície** irregular, com perda do epitélio de revestimento.', 12),
        ],
        ['Colite ativa com distorção e perda de criptas. Nesse aumento, '
         'procuram-se células grandes no estroma e no endotélio.',
         'O micofenolato também distorce criptas: o que separa as causas está '
         'na integração do tecido com a pesquisa do agente e a clínica.']),

    estudo('histologia_alto', 'Biópsia do cólon: grande aumento',
           'A mesma úlcera em grande aumento. Que alteração celular aparece?',
           IMG / 'colon_alto.jpg',
           'Hematoxilina-eosina, grande aumento.',
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
       'O trato gastrointestinal é um sítio importante de doença invasiva no transplantado. A '
       'doença costuma surgir nos primeiros meses depois do fim da profilaxia, '
       'e o valganciclovir de Helena acabou quatro semanas antes da diarreia. '
       'A redução do micofenolato, feita pela hipótese anterior, já era parte '
       'do tratamento.'),




    painel('res2', 'Quarto dia', 'Plasma e prontuário', [
        ex('PCR quantitativa de CMV no plasma', '18.600 UI/mL', 'limite de quantificação 137 UI/mL', True),
        ex('IgG anti-CMV antes do transplante', 'Doador positivo · receptora positiva', '—'),
        ex('Tacrolimo, nível de vale', '7,2 ng/mL', 'alvo da equipe 5–8 ng/mL'),
        ex('Creatinina', '1,9 mg/dL {{(1,6 após hidratação)}}', 'basal 1,2 mg/dL', True),
        ex('Neutrófilos', '900/mm³', '1.500–7.500/mm³', True),
        ex('Evacuações', 'Oito por dia, com urgência e estrias de sangue', '—', True),
    ], introducao='A equipe revê a PCR e a sorologia já disponíveis junto ao tecido. A perda intestinal continua e a creatinina voltou a subir.'),

    Q('p6', 4,
      'Quais duas conclusões os resultados permitem?', [
      ('A imunossupressão permite doença intestinal por CMV em receptora previamente soropositiva', True),
      ('A PCR seriada no mesmo ensaio ajuda a medir resposta ao tratamento', True),
      ('A presença de DNA do vírus no sangue favorece atribuir as citopenias ao vírus e manter os mielotóxicos na dose atual', False),
      ('A soropositividade do doador favorece transmissão pelo enxerto em relação à reativação da receptora', False),
      ('A profilaxia prévia e a carga atual favorecem resistência ao antiviral', False),
     ], [
      ('Integração do tecido', 'A TC localiza alterações, mas não determina a causa. Distorção de criptas também pode ocorrer por fármacos; a integração de efeito citopático, IHQ e clínica sustenta doença invasiva.'),
      ('Doença e seguimento', 'Clínica e IHQ na lesão comprovam doença intestinal, possível por reativação ou reinfecção em receptora soropositiva sob imunossupressão. A PCR no mesmo ensaio e tipo de amostra oferece linha de base e permite seguir a resposta.'),
      ('Conclusões concorrentes', 'Vírus e fármacos podem somar supressão da produção de células do sangue; a presença de DNA do vírus no sangue não discrimina suas contribuições nem justifica manter doses sem revisão. D+/R+ não permite priorizar transmissão pelo enxerto sobre reativação. Exposição prévia ao antiviral entra na avaliação de resistência, mas doença após o fim da profilaxia, antes de observar a resposta terapêutica, favorece inicialmente doença pós-profilaxia, não resistência como causa principal.'),
     ]),

    pg('visita7', 'Quarto dia: repercussão da colite',
       'Ao levantar para o banheiro, Helena volta a sentir tontura e a diurese diminui. Creatinina 1,9 mg/dL, apesar do tacrolimo no alvo. Não há dor no enxerto nem sinais de obstrução; perdas persistentes continuam relevantes, sem excluir rejeição se a disfunção não se resolver.',
       'O tecido confirma colite por CMV. A pequena hematoquezia e a incapacidade de manter ingestão adequada tornam a via do antiviral uma decisão clínica, não apenas uma escolha baseada no número da carga.'),

    bifurcacao('b1', 'Decisão', 'Via inicial do antiviral',
      'Doença intestinal comprovada, oito evacuações diárias, ingestão baixa e nova depleção. Qual via priorizar?', [
      caminho('Ganciclovir intravenoso', 'inicio_antiviral',
              'É preferível quando a gravidade e a possibilidade de absorção oral insuficiente exigem exposição mais previsível.'),
      caminho('Valganciclovir oral', 'oral',
              'É opção na doença leve a moderada com absorção confiável. A diarreia sozinha não prova má absorção, mas o conjunto atual favorece iniciar pela via intravenosa.'),
    ]),

    pg('oral', 'Revisão da via ainda no mesmo dia',
       'A equipe revê a tolerância oral: Helena não vomita, mas come pouco, mantém perdas elevadas e precisa de hidratação intravenosa. Decide começar por ganciclovir intravenoso. Não se declara resistência por um controle precoce de PCR nem se assume que todo comprimido seria ineficaz.',
       segue='inicio_antiviral'),

    pg('inicio_antiviral', 'Tratar a doença',
       'Ganciclovir endovenoso, com dose ajustada à função renal e revista a '
       'cada nova creatinina. A amostra de 18.600 UI/mL é a basal colhida na admissão, antes do antiviral. A data da primeira dose endovenosa passa a ser o '
       'D0. A equipe registra peso, depuração de creatinina para dose e alvo do tacrolimo; reavalia micofenolato e outros mielotóxicos sem suspender toda a imunossupressão.',
       'Com hidratação, a creatinina volta a 1,5 mg/dL em dois dias, o que '
       'reduz a prioridade de biópsia renal imediata; disfunção persistente ou recorrente reabrirá essa avaliação.'),

    painel('semana1', 'D7', 'A primeira semana de ganciclovir', [
        ex('PCR de CMV no plasma, pré-tratamento', '18.600 UI/mL', 'mesmo ensaio', True),
        ex('PCR de CMV no plasma, D7', '3.200 UI/mL', 'limite de quantificação 137 UI/mL', True),
        ex('Neutrófilos', '700/mm³', '1.500–7.500/mm³', True),
        ex('Hemoglobina / plaquetas', '9,4 g/dL / 104.000/mm³', '12–16 g/dL / 150.000–400.000/mm³', True),
        ex('Creatinina', '1,4 mg/dL', 'basal 1,2 mg/dL', True),
        ex('Evacuações', 'Quatro por dia, sem sangue · febre em resolução', '—'),
    ], introducao='A carga caiu quase seis vezes. Helena já dorme a noite inteira, a urgência e o sangue desapareceram, mas ainda tem quatro evacuações amolecidas e apetite parcial. Há resposta clínica em curso, com nova limitação hematológica.'),

    Q('p7', 5,
      'No sétimo dia, quais duas medidas você adota?', [
      ('Reavaliar o micofenolato', True),
      ('Manter dose antiviral de tratamento revista pela função renal atual', True),
      ('Reduzir ganciclovir pela metade diante da neutropenia', False),
      ('Trocar para foscarnet por presumida resistência virológica', False),
      ('Encerrar o antiviral após a primeira queda de carga', False),
     ], [
      ('Resposta e toxicidade', 'Queda virológica com melhora clínica favorece eficácia, enquanto a neutropenia pode ter contribuições do vírus e de várias drogas. Revisar os mielotóxicos com a equipe do transplante, considerar G-CSF e manter vigilância permite preservar tratamento efetivo.'),
      ('Alternativas próximas', 'A dose de ganciclovir deve acompanhar a função renal, que melhorou, e não ser reduzida apenas pela leucopenia. Foscarnet traz nefrotoxicidade sem evidência atual de resistência; reserva-se para situações apropriadas de intolerância ou resistência. Carga ainda quantificável e doença recente não sustentam término.'),
     ]),

    pg('evolucao2', 'D14: recuperação em ritmos diferentes',
       'Após rever os mielotóxicos com a equipe, o micofenolato fica temporariamente suspenso e a profilaxia de pneumocistose é substituída. Os neutrófilos sobem para 1.400/mm³. A reintrodução da imunossupressão será guiada pelo enxerto, infecção e hemograma.',
       'Agora afebril, sem dor ou urgência, Helena volta a comer normalmente e tem uma a duas evacuações formadas por dia. Creatinina 1,3 mg/dL. A PCR semanal ainda é 620 UI/mL: o intestino melhorou antes de atingir a meta virológica.'),

    Q('p8', 6,
      'Quais três exames você solicita na reavaliação do 14.º dia?', [
      ('PCR quantitativa semanal no mesmo ensaio', True),
      ('Hemograma com diferencial', True),
      ('Creatinina seriada para rever a função renal', True),
      ('Genotipagem de resistência agora', False),
      ('Colonoscopia de controle', False),
      ('IgM anti-CMV seriada', False),
     ], [
      ('O que cada exame decide', 'PCR semanal: verifica supressão até o limiar do serviço, além da resolução clínica; a curva atual é de resposta. Hemograma: acompanha neutropenia e efeito da revisão de mielotóxicos. Creatinina: função renal em recuperação exige revisar a dose, evitando subexposição ou toxicidade.'),
      ('Por que não agora', 'Genotipagem: queda contínua não sugere refratariedade e 620 UI/mL reduz a confiabilidade técnica; a profilaxia conta como exposição prévia, mas não muda essa interpretação da resposta. Colonoscopia: não é controle rotineiro de cura se houver boa evolução clínica/virológica; entra se sintomas persistirem ou voltarem. IgM: não mede resposta nem orienta término.'),
     ]),

    pg('visita14', 'Transição para casa',
       'Com absorção clinicamente confiável e recuperação renal, a equipe passa para valganciclovir oral em dose de tratamento, ajustada à depuração atual. A mudança da via não é o término da terapia.',
       'Helena e o marido recebem o plano de coleta semanal, revisão do hemograma e dose, e orientação para avisar se voltarem febre, diarreia ou redução da diurese.'),

    pg('resposta', 'D21',
       'A série de PCR no mesmo ensaio é 18.600 → 3.200 → 620 → abaixo de 137 UI/mL. Helena está assintomática, comendo e com hemograma em recuperação. A equipe encerra após mais de duas semanas, resolução clínica e queda abaixo do limiar do laboratório, em ensaio sensível.',
       'Pelo risco de recorrência e pela revisão recente da imunossupressão, mantém vigilância semanal por período individualizado, inicialmente oito a doze semanas. Profilaxia secundária não é automática.',
       segue='f1'),

    fim('f1', 'Retorno ao ambulatório',
        'Helena mantém alimentação e atividade em casa, sem recorrência da diarreia nas primeiras consultas. Creatinina 1,3 mg/dL e hemograma em recuperação. A equipe reintroduz micofenolato em dose menor com monitorização.',
        'A resposta à hidratação esclareceu parte da disfunção do enxerto, mas não a colite. Tecido representativo, tratamento com exposição adequada e revisão conjunta de toxicidade permitiram recuperar intestino e função renal sem atribuir tudo a um único mecanismo.', 'melhor'),

    pagina('retrospectiva', 'Pontos de ensino', '',
        pontos(
            'Diarreia noturna com febre e perda de peso justifica investigação orgânica no transplantado; testes fecais negativos não separam toda infecção de lesão medicamentosa.',
            'Na piora do enxerto durante diarreia, perdas de volume e tacrolimo acima '
            'do alvo apontam para volume e droga; a avaliação do enxerto ocorre em paralelo e disfunção persistente reforça investigar rejeição.',
            'Resposta circulatória à hidratação com progressão de dor, urgência e sangue exige rever a colite; PCR para CMV e avaliação de mucosa já têm indicação na apresentação.',
            'O fim da profilaxia com valganciclovir abre a janela da doença por '
            'citomegalovírus; sintomas e tecido distinguem DNA do vírus no sangue de doença intestinal.',
            'A presença de DNA do vírus no plasma acompanha a infecção e guia o tratamento; a doença '
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
       'Revisão em 23/10/2026: https://pubmed.ncbi.nlm.nih.gov/40200403/. Kotton CN e cols. The Fourth International Consensus Guidelines on the '
       'Management of Cytomegalovirus in Solid Organ Transplantation. '
       'Transplantation 2025;109(7):1066–1110 (diagnóstico, duração do '
       'tratamento, neutropenia e critérios de genotipagem).',
       'Tomografia: Hellerhoff, Wikimedia Commons, CC BY-SA 4.0, painel axial recortado de "Clostridien Colitis 68M - CT KM pv - 001". Histologia: Nephron, Wikimedia Commons, CC BY-SA 3.0 ("CMV colitis - intermed mag" e "CMV colitis - high mag - cropped"). Setas adicionadas.'),
]

REVISAO = []

# Fontes conferidas na revisão das questões (22/10/2026):
# https://pmc.ncbi.nlm.nih.gov/articles/PMC12180710/

# Referência de construção dos itens (aplicação e opções plausíveis):
# https://www.nbme.org/sites/default/files/2021-02/NBME_Item%20Writing%20Guide_R_6.pdf

# Revisão de evolução 23/10/2026: Kotton et al. 2025, PMID 40200403.
# https://pubmed.ncbi.nlm.nih.gov/40200403/

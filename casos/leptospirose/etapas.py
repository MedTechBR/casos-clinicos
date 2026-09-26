"""Febre ictérica grave com lesão renal e hemorragia pulmonar.

Alíquota → pergunta, no molde dos casos interativos do //New England//. Oito
perguntas, uma rodada de exames sindrômica com gabarito e painel, um
pareamento das febres ictéricas e hemorrágicas do Nordeste e três decisões de
conduta, uma delas com óbito. A exposição só aparece quando o irmão volta, e o
nome do diagnóstico só na página do laboratório de referência, perto do meio
do percurso. Paciente ficcional; doses e critérios segundo o Guia de
Vigilância em Saúde do Ministério da Saúde, 6.ª edição revisada, 2024.
"""
from pathlib import Path

from motor.estudo_imagem import estudo

from motor.etapas import (alt, bifurcacao, caminho, capa, desfecho, op, p,
                          pagina, painel, par, pareamento, pergunta, tabela,
                          topicos, vitais, lamina)
from casos.novos import imagem

TITULO = 'Febre de abril'
RODAPE = 'Paciente ficcional · evoluções simuladas para ensino'
COR = '#0891b2'
IMG = Path(__file__).parent / 'img'
BANCO = []
CREDITO_RX = 'Samir · Wikimedia Commons · CC BY-SA 3.0'


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
       'Joaquim, 38 anos, morador de Fortaleza, chega à emergência trazido '
       'pelo irmão no sexto dia de uma febre que começou de repente, com '
       'calafrios, dor de cabeça e dor no corpo todo, forte a ponto de '
       'atrapalhar a marcha.',
       'No segundo dia foi a uma unidade de pronto atendimento, onde '
       'disseram que era dengue: soro oral, paracetamol e repouso. Há dois '
       'dias está amarelo, e desde a noite passada tosse com raias de sangue '
       'e fica sem ar para ir ao banheiro.'),

    pg('hda', 'História da doença atual',
       'A febre chegou a 39,8 °C nos três primeiros dias, cedeu um pouco no '
       'quarto e voltou. A urina está "cor de guaraná", e hoje ele urinou '
       'pouco. Teve dois episódios de vômito, sem sangue. Nega dor abdominal '
       'forte, diarreia e manchas no corpo antes da febre.',
       'O irmão acha que ele está mais sonolento desde a tarde.'),

    pg('antecedentes', 'Antecedentes',
       'Sem doenças conhecidas, sem medicações de uso contínuo. Bebe cerveja '
       'nos fins de semana, sem excesso diário. Não fuma. Nega drogas '
       'injetáveis e transfusões. Vacinado contra febre amarela há seis anos. '
       'Não saiu do Ceará no último ano.',
       'Joaquim responde pouco, e o irmão, que mora em outro bairro, não '
       'sabe detalhar a rotina de trabalho dele nas últimas semanas.'),

    pagina('exame', 'Exame físico', '',
           vitais(('Temperatura', '38,4 °C', True), ('Pressão arterial', '94/56', True),
                  ('Frequência cardíaca', '116', True), ('Frequência respiratória', '28', True),
                  ('SpO₂ em ar ambiente', '90%', True)),
           topicos(('Estado geral', 'Prostrado, sonolento mas orientado. Icterícia '
                    'intensa.'),
                   ('Olhos', 'Escleras ictéricas. Conjuntivas hiperemiadas dos dois '
                    'lados, sem secreção.'),
                   ('Respiratório', 'Crepitações nas bases dos dois pulmões.'),
                   ('Abdome', 'Fígado a 2 cm do rebordo, doloroso. Baço não palpável. '
                    'Sem sinal de Murphy.'),
                   ('Membros', 'Petéquias nas pernas. Massas musculares dolorosas à '
                    'palpação.'),
                   ('Neurológico', 'Sem rigidez de nuca, sem déficit focal.')),
           so_kicker=True),

    Q('p1', 1,
      'Febre aguda, icterícia intensa, pouca urina, hemoptise e hipotensão '
      'num homem previamente saudável de Fortaleza. **Quais quatro** '
      'diagnósticos precisam ser considerados já?', [
      ('Dengue grave', 'Foi o diagnóstico da UPA. Plaquetopenia, sangramento '
       'e choque cabem nela.', True),
      ('Hepatite viral aguda', 'Febre com icterícia obriga a pensar em A e B, '
       'mesmo com rim e pulmão acometidos.', True),
      ('Sepse bacteriana de foco biliar ou pulmonar', 'Febre, icterícia e '
       'hipotensão são sepse até prova em contrário.', True),
      ('Leptospirose', 'Doença febril aguda que pode reunir icterícia, lesão '
       'renal e sangramento pulmonar.', True),
      ('Febre amarela', 'Vacinado há seis anos e sem entrada conhecida em '
       'área de mata.', False),
      ('Malária grave', 'Sem viagem. Fora da região amazônica, a malária é '
       'quase sempre importada.', False),
      ('Hantavirose', 'Cardiopulmonar, com hemoconcentração e sem icterícia '
       'intensa. O fígado não combina.', False),
      ('Hepatite alcoólica', 'Exige anos de consumo pesado diário; cerveja de '
       'fim de semana não chega lá.', False),
      ('Mononucleose infecciosa', 'Faz febre e hepatite leve, raramente lesão '
       'renal com hemoptise.', False),
     ], 'Febre ictérica com rim e pulmão: o diferencial ainda é largo'),

    Q('ex1', 2,
      'Na emergência, **quais cinco** exames são os mais apropriados?', [
      ('Hemograma com plaquetas', 'Plaquetas e hematócrito ajudam a separar '
       'dengue, sepse e outras febres com sangramento.', True),
      ('Creatinina, ureia, sódio e potássio', 'Urina escura e escassa. '
       'Esses números decidem reposição e diálise.', True),
      ('Bilirrubinas, transaminases e creatinoquinase', 'A proporção entre '
       'bilirrubina e transaminases, e a CK na mialgia, orientam o diferencial.',
       True),
      ('Radiografia de tórax', 'Hemoptise com SpO₂ de 90%: é preciso ver o que '
       'ocupa os alvéolos.', True),
      ('Hemoculturas antes do antibiótico', 'Sepse está na lista, e a coleta '
       'agora não atrasa o tratamento.', True),
      ('Gota espessa', 'Sem viagem à região amazônica, o rendimento esperado '
       'é mínimo.', False),
      ('Tomografia de crânio', 'Sonolência sem déficit focal nem rigidez de '
       'nuca sugere causa metabólica.', False),
      ('Colangiorressonância', 'Antes dela vem o ultrassom, que mostra se há '
       'via biliar dilatada.', False),
      ('Sorologia para hantavírus', 'Sem exposição rural conhecida e com '
       'icterícia intensa, não entra na primeira rodada.', False),
      ('Biópsia hepática', 'Não tem lugar na avaliação inicial da icterícia '
       'febril aguda.', False),
     ], 'A equipe pede os cinco, mais gasometria, ultrassom e sorologias de '
        'dengue e hepatites'),

    painel('res1', 'Na emergência', 'O que a equipe pediu', [
        ex('Hemoglobina / hematócrito', '11,6 g/dL / 34%', 'Hb 13,5–17,5 g/dL', True),
        ex('Leucócitos', '14.800/mm³ · neutrófilos 88%', '4.000–11.000/mm³', True),
        ex('Plaquetas', '52.000/mm³ {{(145.000 na UPA)}}', '150.000–450.000/mm³', True),
        ex('Creatinina / ureia', '3,9 / 148 mg/dL {{(creatinina 1,0 na UPA)}}', 'até 1,3 / 45 mg/dL', True),
        ex('Sódio / potássio / cloro', '133 / 3,1 / 100 mmol/L', 'Na 135–145 · K 3,5–5,0 · Cl 98–107', True),
        ex('Bilirrubina total / direta', '17,8 / 15,2 mg/dL', 'até 1,2 / 0,3 mg/dL', True),
        ex('AST / ALT', '112 / 84 U/L', 'até 40 / 41 U/L', True),
        ex('Creatinoquinase', '4.260 U/L', 'até 190 U/L', True),
        ex('INR', '1,3', 'até 1,2', True),
        ex('Gasometria arterial em ar ambiente', 'pH 7,32 · pCO₂ 30 · HCO₃ 15 · pO₂ 58 mmHg · lactato 3,6 mmol/L', '—', True),
        ex('Dengue: NS1 e IgM', 'Não reagentes', 'não reagentes'),
        ex('Hepatites: anti-HAV IgM, HBsAg, anti-HBc IgM', 'Não reagentes', 'não reagentes'),
        ex('Ultrassonografia de abdome', 'Fígado discretamente aumentado, vias biliares sem dilatação, rins de tamanho normal', '—', True),
        ex('Radiografia de tórax', 'Infiltrado alveolar bilateral, predominando em bases e periferia', '—', True),
    ], introducao='Duas hemoculturas foram colhidas antes de qualquer antibiótico, e '
                  'uma alíquota de sangue da admissão ficou guardada no laboratório.',
       laminas={'Radiografia de tórax': lamina('rx_torax_alveolar.jpg', 'Radiografia de tórax',
                'Imagem ilustrativa de outro paciente; o padrão alveolar não '
                'distingue sangue de água ou de pus.', CREDITO_RX)}),

    Q('p3', 3,
      'Bilirrubina de 17,8 (direta 15,2) com AST de 112, CK de 4.260, '
      'potássio de 3,1 e creatinina de 3,9. **Quais três** afirmações estão '
      'corretas?', [
      ('A desproporção entre bilirrubina e transaminases fala contra hepatite viral',
       'Hepatite viral com essa icterícia teria transaminases na casa dos '
       'milhares.', True),
      ('A CK alta indica lesão muscular que pode somar-se à lesão renal',
       'Miosite com rabdomiólise agrava a lesão tubular e escurece a urina.',
       True),
      ('Potássio baixo com creatinina de 3,9 sugere perda tubular de potássio',
       'Na lesão renal habitual o potássio sobe. Aqui o túbulo perde potássio.',
       True),
      ('A icterícia é sobretudo hemolítica, de bilirrubina indireta',
       'A fração direta é 85% do total: o defeito é de excreção.', False),
      ('Os dois vômitos explicam a hipocalemia',
       'Perda gástrica daria alcalose, e o bicarbonato está baixo.', False),
      ('Bilirrubina direta alta exige colangiorressonância antes de tratar',
       'Vias biliares finas no ultrassom apontam colestase intra-hepática, sem '
       'obstrução.', False),
      ('O INR de 1,3 com sonolência define insuficiência hepática aguda',
       'O critério pede INR de 1,5 ou mais com encefalopatia.', False),
      ('A plaquetopenia, com essas provas negativas, ainda confirma dengue',
       'Plaquetopenia é comum a sepse e a várias febres ictéricas.', False),
     ], 'Colestase sem necrose, músculo lesado e túbulo que perde potássio'),

    Q('p4', 4,
      'Gasometria em ar ambiente: pH 7,32, pCO₂ 30, HCO₃ 15, pO₂ 58; sódio '
      '133, cloro 100, lactato 3,6. **Quais três** afirmações estão '
      'corretas?', [
      ('Há acidose metabólica com ânion gap elevado',
       '133 menos 115 dá 18. Lactato e uremia somam ácidos não medidos.',
       True),
      ('A pCO₂ de 30 é a compensação esperada',
       'Pela fórmula de Winter, 1,5 × 15 + 8 dá cerca de 30.', True),
      ('A relação PaO₂/FiO₂ perto de 280 indica lesão pulmonar relevante',
       '58 dividido por 0,21 dá 276, já com infiltrado bilateral.', True),
      ('A pCO₂ baixa indica alcalose respiratória primária dominante',
       'O pH é ácido, e a pCO₂ está no previsto para a compensação.', False),
      ('A acidose se explica pelos vômitos',
       'Perda de suco gástrico produz alcalose metabólica, não acidose.',
       False),
      ('Bicarbonato intravenoso está indicado com pH de 7,32',
       'Acima de 7,2, o bicarbonato não traz benefício e soma sódio e volume.',
       False),
      ('SpO₂ de 90% em ar ambiente dispensa oxigênio suplementar',
       'Com taquipneia e infiltrado bilateral, o alvo é de 92 a 96%.', False),
     ], 'Acidose de ânion gap elevado, compensada, e troca gasosa já comprometida'),

    bifurcacao('b1', 'Decisão', 'As primeiras horas',
      'Joaquim está hipotenso, ictérico e hipoxêmico. As hemoculturas já '
      'foram colhidas. Como você conduz?', [
      caminho('Oxigênio, leito monitorizado e ceftriaxona 2 g endovenosa agora',
              'tratado',
              'Ceftriaxona em dose plena cobre as causas bacterianas tratáveis '
              'deste diferencial, sem esperar sorologias.'),
      caminho('Oxigênio e hidratação; escolher o antibiótico quando saírem as '
              'sorologias', 'espera',
              'Sorologias e culturas levam dias. Com sepse possível, o '
              'antibiótico vem no primeiro atendimento.'),
      caminho('Conduzir como dengue grave: cristaloide 20 mL/kg em bolus '
              'repetidos, sem antibiótico', 'volume',
              'NS1 e IgM negativos, hemoptise e crepitações pedem cautela com '
              'volume e cobertura antibiótica.'),
    ]),

    pg('volume', 'Quatro horas depois',
       'Depois de três litros de cristaloide, a pressão sobe para 102/60, mas '
       'a saturação cai para 84% com cateter nasal e as crepitações chegam '
       'aos terços médios. A plantonista suspende o volume e inicia '
       'ceftriaxona com quatro horas de atraso.',
       segue='tratado'),

    pg('espera', 'Dezoito horas depois',
       'Sob soro e oxigênio, a saturação cai para 85% e a urina para 20 mL '
       'por hora. As sorologias ainda não saíram. A plantonista inicia '
       'ceftriaxona com dezoito horas de atraso.',
       segue='tratado'),

    pg('tratado', 'Primeiras horas de antibiótico',
       'Duas horas depois da primeira dose, Joaquim tem calafrios, febre de '
       '40 °C e queda da pressão para 84/50. Com 500 mL de cristaloide e '
       'antitérmico, melhora em quatro horas. A equipe mantém a ceftriaxona.',
       'Na madrugada, a tosse fica úmida. Ele expectora sangue vivo.'),

    pg('irmao', 'Na manhã seguinte',
       'O irmão volta com os documentos, depois de conversar com os colegas de '
       'Joaquim. '
       'Ele é agente de limpeza urbana. Doze dias antes da febre, depois de '
       'três dias de chuva forte, passou um turno dentro de um canal alagado, '
       'desobstruindo a passagem da água, com uma bota furada.',
       'Revisto, o exame mostra que a dor à compressão é muito maior nas '
       'panturrilhas, e há um corte cicatrizado na planta do pé direito. Os '
       'colegas dizem que o depósito da equipe tem ratos.'),

    pg('virada', 'Laboratório de referência',
       'Com essa história, a equipe envia a alíquota guardada da admissão, '
       'colhida no sexto dia de doença e antes da ceftriaxona, ao laboratório '
       'de referência.',
       '**PCR para Leptospira no sangue: DNA detectado.** ELISA IgM para '
       'leptospira na mesma amostra: não reagente. As hemoculturas seguem '
       'sem crescimento em 48 horas.',
       'Joaquim tem leptospirose na forma grave, com icterícia, lesão renal e '
       'sangramento pulmonar: a síndrome de Weil.'),

    Q('p5', 5,
      'PCR detectado e ELISA IgM não reagente, ambos na amostra do sexto dia. '
      '**Quais três** afirmações estão corretas?', [
      ('PCR detectado em sangue colhido até o sétimo dia confirma o caso',
       'É critério de confirmação laboratorial do Guia de Vigilância em '
       'Saúde.', True),
      ('Nova sorologia deve ser colhida a partir do sétimo dia',
       'Antes disso é comum não haver anticorpo; a MAT pareada pede '
       'amostra entre 14 e 60 dias.', True),
      ('A cultura para leptospira só termina em semanas',
       'Serve ao diagnóstico retrospectivo e à tipagem, não à decisão de '
       'hoje.', True),
      ('O ELISA não reagente no sexto dia descarta a infecção',
       'Amostra antes do sétimo dia não descarta: o IgM ainda pode não ter '
       'aparecido.', False),
      ('Na primeira semana, a urina é a melhor amostra para PCR',
       'Na fase precoce a leptospira está no sangue; na urina, mais tarde.',
       False),
      ('Com a confirmação, a ceftriaxona deve dar lugar à doxiciclina oral',
       'Doxiciclina oral é esquema da forma leve. Joaquim tem forma grave.',
       False),
      ('O tempo de antibiótico depende do resultado da MAT',
       'O esquema endovenoso dura pelo menos sete dias, independentemente '
       'da MAT.', False),
     ], 'O DNA confirma cedo; o anticorpo chega depois'),

    pg('hemorragia', 'Segundo dia de internação',
       'Saturação de 83% com máscara com reservatório, frequência '
       'respiratória de 36, hemoptise de 150 mL em seis horas. Diurese de 280 '
       'mL em 24 horas. Creatinina 5,8 mg/dL, potássio 3,4. A hemoglobina '
       'caiu de 11,6 para 9,1 g/dL.',
       'A nova radiografia mostra opacidades alveolares confluentes nos dois '
       'pulmões.'),

    estudo('rx_hemorragia', 'Radiografia de tórax',
           'Radiografia ilustrativa de outro paciente, com o padrão descrito '
           'no laudo de Joaquim. Descreva a distribuição antes de propor o '
           'mecanismo.',
           IMG / 'rx_torax_alveolar.jpg',
           'Radiografia de outro paciente · comparação didática.',
           CREDITO_RX,
        [
         ((308, 427), (110, 345), '**Opacidades alveolares** no pulmão direito, em mancha e confluentes.', 12),
         ((704, 430), (912, 320), 'O mesmo padrão no **pulmão esquerdo**: a doença é bilateral.', -12),
         ((620, 160), (760, 60), '**Ápices relativamente poupados**: o predomínio é central e inferior.', 12),
        ],
        ['Opacidades alveolares bilaterais, confluentes, com predomínio central e inferior.',
         'Com hemoptise, hipoxemia e queda de hemoglobina, é hemorragia pulmonar, '
         'a complicação que mais mata na leptospirose grave.']),

    bifurcacao('b2', 'Decisão', 'O pulmão que sangra',
      'Saturação de 83% com máscara, hemoptise e oligúria. O que você faz?', [
      caminho('UTI: intubação precoce com ventilação protetora e diálise '
              'precoce e diária', 'uti',
              'Proteger o pulmão com volumes baixos e dialisar cedo reduz a '
              'mortalidade.'),
      caminho('Ventilação não invasiva e furosemida em dose alta', 'vni',
              'A máscara não protege uma via aérea que sangra, e o diurético '
              'não muda o curso da lesão renal.'),
      caminho('Pulso de metilprednisolona e observação na enfermaria', 'pulso',
              'O corticoide na hemorragia pulmonar é controverso e não '
              'substitui suporte intensivo.'),
    ]),

    pg('pulso', 'Seis horas depois',
       'Na enfermaria, sob corticoide, a saturação cai para 78%. O time de '
       'resposta rápida é chamado.',
       segue='vni'),

    pg('vni', 'Na sala de emergência',
       'Com ventilação não invasiva, Joaquim enche a máscara de sangue e não '
       'consegue manter a saturação acima de 80%. Está agitado e confuso.',
       segue='b3'),

    bifurcacao('b3', 'Decisão', 'A máscara falhou',
      'Qual a próxima conduta?', [
      caminho('Intubar agora, ventilação protetora e UTI com diálise',
              'uti_tardia', 'A falha da ventilação não invasiva é a indicação.'),
      caminho('Manter a máscara e aumentar a fração inspirada de oxigênio',
              'parada', 'Insistir num suporte que já falhou.'),
    ]),

    pg('parada', 'Vinte minutos depois',
       'Joaquim para em atividade elétrica sem pulso, hipoxêmico. É '
       'intubado durante a reanimação, com sangue saindo pelo tubo. O '
       'retorno da circulação acontece depois de 18 minutos.',
       segue='f_obito'),

    pg('uti_tardia', 'Na UTI',
       'Intubado em emergência, com ventilação protetora, pressão expiratória '
       'alta e sedação profunda. A hemodiálise começa no mesmo dia. A '
       'hipoxemia grave dura quatro dias.',
       segue='f2'),

    pg('uti', 'Na UTI',
       'Intubação planejada, ventilação com volume corrente de 6 mL/kg de '
       'peso predito e pressão expiratória elevada. Hemodiálise no mesmo dia, '
       'depois diária. Potássio reposto conforme os controles.',
       'A hemoptise para no terceiro dia. Joaquim é extubado no sexto.'),

    pareamento('p6', 'Pergunta 6',
      'As febres ictéricas e hemorrágicas do Nordeste se sobrepõem. Associe '
      'cada quadro à doença que ele sugere.', [
      par('Sufusão conjuntival, dor na panturrilha e contato com enchente',
          'Leptospirose',
          'A combinação de Joaquim. A sufusão é congestão sem secreção.'),
      par('Dor abdominal, vômitos e hematócrito subindo na defervescência',
          'Dengue grave',
          'O extravasamento plasmático começa quando a febre cai.'),
      par('Febre, icterícia e pulso lento para a febre, sem vacina, após mata',
          'Febre amarela',
          'Sinal de Faget e transaminases na casa dos milhares.'),
      par('Febre em picos, anemia e esplenomegalia depois de viagem ao Pará',
          'Malária por Plasmodium vivax',
          'A gota espessa decide. No Ceará, quase sempre importada.'),
      par('Icterícia com transaminases acima de 1.000 e pouca febre',
          'Hepatite A aguda',
          'Hepatite hepatocelular pura, sem rim nem pulmão.'),
    ], opcoes=['Leptospirose', 'Dengue grave', 'Febre amarela',
               'Malária por Plasmodium vivax', 'Hepatite A aguda', 'Hantavirose'],
    titulo_resposta='O detalhe da história decide mais que o laboratório',
    nota='A opção que sobrou, hantavirose, é cardiopulmonar, de exposição '
         'rural, com hemoconcentração e sem icterícia importante.'),

    Q('p7', 7,
      'Sobre o tratamento de Joaquim, **quais três** afirmações estão '
      'corretas?', [
      ('Ceftriaxona ou penicilina cristalina endovenosa, por pelo menos sete dias',
       'Esquemas equivalentes na forma grave; a doxiciclina oral fica para a '
       'forma leve.', True),
      ('Diálise precoce e diária reduz a mortalidade',
       'Comparada à diálise em dias alternados, reduziu a mortalidade num '
       'ensaio brasileiro.', True),
      ('O potássio deve ser reposto conforme os controles',
       'A perda tubular de potássio continua, sobretudo na fase poliúrica.',
       True),
      ('A piora febril após a primeira dose pedia suspender a ceftriaxona',
       'Foi uma reação de Jarisch-Herxheimer: trata-se o sintoma e mantém-se '
       'o antibiótico.', False),
      ('Furosemida converte a oligúria e evita a diálise',
       'Não muda a necessidade de diálise nem a mortalidade.', False),
      ('O antibiótico só traz benefício na primeira semana de doença',
       'Está indicado em qualquer fase, embora renda mais na primeira semana.',
       False),
      ('Corticoide é tratamento de rotina da forma grave',
       'Não há evidência que sustente o uso rotineiro.', False),
     ], 'Antibiótico mantido, diálise cedo, potássio sempre'),

    pg('recuperacao', 'Segunda semana',
       'A diurese volta com poliúria de 4 litros por dia, e o potássio '
       'precisa de reposição. A icterícia regride devagar. A segunda '
       'amostra, no 14.º dia, tem ELISA IgM reagente e microaglutinação com '
       'título de 1:1.600 para o sorogrupo Icterohaemorrhagiae.'),

    Q('p8', 8,
      'Na alta, **quais três** medidas estão corretas?', [
      ('Notificar o caso à vigilância epidemiológica',
       'Leptospirose é de notificação compulsória, e a vigilância investiga os '
       'colegas expostos.', True),
      ('Investigar o local de trabalho e orientar equipamento de proteção',
       'Botas íntegras e luvas na limpeza de canais, e controle de roedores no '
       'depósito.', True),
      ('Acompanhar creatinina e potássio nas semanas seguintes',
       'A função renal costuma recuperar em semanas, e a fase poliúrica perde '
       'potássio.', True),
      ('Isolamento de contato em casa',
       'Não há transmissão entre pessoas; o risco está na água e nos roedores.',
       False),
      ('Antibiótico profilático por três meses',
       'Não há indicação depois de tratada a infecção.', False),
      ('Vacina humana para os colegas',
       'Não há vacina humana disponível no Brasil.', False),
      ('Repetir a microaglutinação todo mês',
       'O caso já está confirmado, e repetir não muda a conduta.', False),
     ], 'Notificar, proteger quem trabalha na água e acompanhar o rim'),

    pg('alta', 'Preparando a alta',
       'A equipe revê com Joaquim e o irmão o que aconteceu: a exposição, a '
       'doença, as sessões de diálise e o que esperar do rim e dos músculos '
       'nas próximas semanas.',
       conforme=('b2', ['alta_cedo', 'f2', 'f2'])),

    pg('alta_cedo', 'Última visita',
       'A diálise foi suspensa no nono dia e a creatinina cai todos os dias. '
       'Ele já caminha pelo corredor sem oxigênio.',
       conforme=('b1', ['f1', 'f2', 'f2'])),

    fim('f1', 'Alta sem diálise',
        'Joaquim sai no 16.º dia, sem diálise desde o 9.º, com creatinina de '
        '1,6 mg/dL e bilirrubina em queda. Retoma o trabalho em seis semanas.',
        'Antibiótico no primeiro contato, UTI antes da falência e diálise '
        'precoce: as três decisões que mudam a mortalidade da síndrome de '
        'Weil.', 'melhor'),

    fim('f2', 'Alta depois de internação prolongada',
        'Joaquim sai no 27.º dia, com creatinina de 2,1 mg/dL e fraqueza '
        'muscular que leva dois meses para passar.',
        'O atraso do antibiótico ou do suporte intensivo acrescentou dias de '
        'hipoxemia e de diálise. Ele sobreviveu a uma forma de letalidade alta.',
        'medio'),

    fim('f_obito', 'Óbito no terceiro dia',
        'Depois da parada, Joaquim evolui com choque refratário e hemorragia '
        'pulmonar maciça. Morre no terceiro dia de internação.',
        'A ventilação não invasiva numa via aérea que sangra, mantida depois '
        'de falhar, levou à parada hipóxica. A hemorragia pulmonar da '
        'leptospirose pede intubação precoce.', 'pior'),

    pagina('retrospectiva', 'Retrospectiva', '',
        tabela(['Momento', 'O dado', 'O que decidiu'], [
            ['Na UPA, segundo dia', 'Febre súbita e mialgia intensa, sem pergunta '
             'sobre trabalho e água', 'Perguntar pela exposição teria mudado o '
             'diagnóstico de dengue'],
            ['Na emergência', 'Bilirrubina 17,8 com AST 112, CK alta, potássio baixo',
             'Colestase, miosite e perda tubular: o padrão da síndrome de Weil'],
            ['Primeiras horas', 'Ceftriaxona antes do diagnóstico', 'O antibiótico '
             'empírico já cobria a leptospirose'],
            ['Manhã seguinte', 'O canal alagado, a bota furada, as panturrilhas',
             'A história que faltava levou ao teste certo'],
            ['Laboratório', 'PCR detectado, IgM ainda negativo no sexto dia',
             'O DNA confirma antes do anticorpo'],
            ['Segundo dia', 'Hemoptise, hipoxemia, oligúria', 'UTI, intubação protetora '
             'e diálise precoce'],
        ]),
        so_kicker=True),

    pg('referencias', 'Fontes e limites',
       'Paciente, valores e percursos são ficcionais. A cena de abertura é uma ilustração autoral gerada por inteligência artificial para este caso; não é fotografia nem documentação clínica.',
       'Ministério da Saúde. Guia de Vigilância em Saúde, 6.ª edição '
       'revisada, 2024, volume 3, capítulo de leptospirose (critérios de '
       'confirmação e antibioticoterapia), e Leptospirose: diagnóstico e '
       'manejo clínico, 2014. Andrade e cols., Clin J Am Soc Nephrol 2007 '
       '(diálise diária). Spichler e cols., Am J Trop Med Hyg 2008 '
       '(preditores de mortalidade). Radiografia: Samir, Wikimedia Commons, '
       'CC BY-SA 3.0, de outro paciente.'),
]

REVISAO = []

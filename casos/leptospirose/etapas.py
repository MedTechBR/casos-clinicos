"""Febre ictérica grave com lesão renal e hemorragia pulmonar.

PILOTO do molde do //New England// lido em 26/09/2026 (ver
Artifacts/nejm-casos-classicos/GRAMATICA_LIDA_2026-09-26.md), no desenho de
"An Unusual Case of Abdominal Pain": apresentação curta, ficha do paciente,
exame por sistema e primeiros exames entregues prontos; as primeiras
perguntas classificam os dados (padrão hepático, tipo de lesão renal,
gasometria, mecanismo da hipoxemia) sem nomear doença; a exposição chega
depois, com o irmão; o nome do diagnóstico aparece pela primeira vez na
pergunta do exame confirmatório, perto de 60% do caso. Cada pergunta tem uma
explicação só, em seções com subtítulo. As decisões de conduta continuam
mudando o desfecho, a pedido do Matheus.

Paciente ficcional; doses e critérios segundo o Guia de Vigilância em Saúde
do Ministério da Saúde, 6.ª edição revisada, 2024.
"""
from pathlib import Path

from motor.estudo_imagem import estudo
from motor.etapas import (alt, bifurcacao, caminho, capa, desfecho, op, p,
                          pagina, painel, par, pareamento, pergunta, pontos,
                          topicos, vitais, lamina)

TITULO = 'Febre de abril'
RODAPE = 'Paciente ficcional · evoluções simuladas para ensino'
COR = '#0891b2'
IMG = Path(__file__).parent / 'img'
BANCO = []
MOLDE = 'nejm'
CREDITO_RX = 'Samir · Wikimedia Commons · CC BY-SA 3.0'


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
    capa(TITULO, fundo='cena.png', kicker='Caso interativo',
         selo='Paciente ficcional · procedência e créditos na última tela'),

    pg('historia', 'Apresentação',
       'Um homem de 38 anos, morador de Fortaleza, chega à emergência trazido '
       'pelo irmão no sexto dia de uma febre que começou de repente, com '
       'calafrios, dor de cabeça e dor no corpo todo, forte a ponto de '
       'atrapalhar a marcha.',
       'No segundo dia foi a uma unidade de pronto atendimento, onde '
       'disseram que era dengue: soro oral, paracetamol e repouso. A febre '
       'cedeu no quarto dia e voltou. Há dois dias está amarelo, a urina ficou '
       'escura e escassa, e desde a noite passada tosse com raias de sangue e '
       'fica sem ar para ir ao banheiro.',
       'Nega dor abdominal forte, diarreia, manchas na pele antes da febre, '
       'viagem, transfusão e uso de remédios além do paracetamol.'),

    pagina('ficha', 'Ficha do paciente', '',
           topicos(('Antecedentes', 'Nenhuma doença conhecida. Nunca internou.'),
                   ('Medicações', 'Paracetamol 750 mg até quatro vezes ao dia '
                    'desde o segundo dia. Nenhuma outra, nem chás.'),
                   ('Vacinas', 'Febre amarela há seis anos. Não sabe informar '
                    'as outras.'),
                   ('Hábitos', 'Três a quatro latas de cerveja nos fins de '
                    'semana. Não fuma. Nega drogas injetáveis.'),
                   ('Vida social', 'Mora sozinho. Servidor da prefeitura, em '
                    'trabalho de rua. O irmão mora em outro bairro e não sabe '
                    'detalhar a rotina dele.'),
                   ('Família', 'Pais vivos, hipertensos. Sem doença hepática ou '
                    'renal na família.')),
           so_kicker=True),

    pagina('exame', 'Exame físico', '',
           vitais(('Temperatura', '38,4 °C', True), ('Pressão arterial', '94/56', True),
                  ('Frequência cardíaca', '116', True), ('Frequência respiratória', '28', True),
                  ('SpO₂ em ar ambiente', '90%', True)),
           topicos(('Estado geral', 'Prostrado, sonolento mas orientado. Icterícia '
                    'intensa.'),
                   ('Olhos', 'Escleras ictéricas. Conjuntivas hiperemiadas dos dois '
                    'lados, sem secreção.'),
                   ('Respiratório', 'Crepitações nas bases dos dois pulmões.'),
                   ('Coração', 'Rítmico, taquicárdico, sem sopros.'),
                   ('Abdome', 'Fígado a 2 cm do rebordo, doloroso. Baço não palpável. '
                    'Sem sinal de Murphy.'),
                   ('Membros', 'Petéquias nas pernas. Massas musculares dolorosas à '
                    'palpação.'),
                   ('Neurológico', 'Sem rigidez de nuca, sem déficit focal.')),
           so_kicker=True),

    painel('res1', 'Primeiros exames', 'Na emergência', [
        ex('Hemoglobina / hematócrito', '11,6 g/dL / 34%', 'Hb 13,5–17,5 g/dL', True),
        ex('Leucócitos', '14.800/mm³ · neutrófilos 88%', '4.000–11.000/mm³', True),
        ex('Plaquetas', '52.000/mm³ {{(145.000 na UPA)}}', '150.000–450.000/mm³', True),
        ex('Creatinina / ureia', '3,9 / 148 mg/dL {{(creatinina 1,0 na UPA)}}', 'até 1,3 / 45 mg/dL', True),
        ex('Sódio / potássio / cloro', '133 / 3,1 / 100 mmol/L', 'Na 135–145 · K 3,5–5,0 · Cl 98–107', True),
        ex('Bilirrubina total / direta', '17,8 / 15,2 mg/dL', 'até 1,2 / 0,3 mg/dL', True),
        ex('AST / ALT', '112 / 84 U/L', 'até 40 / 41 U/L', True),
        ex('Fosfatase alcalina / GGT', '210 / 185 U/L', 'até 129 / 60 U/L', True),
        ex('Creatinoquinase', '4.260 U/L', 'até 190 U/L', True),
        ex('INR', '1,3', 'até 1,2', True),
        ex('Urina', 'Densidade 1.012 · sangue ++ · proteína + · 3 a 5 hemácias e cilindros granulosos por campo · sem cilindros hemáticos', '—', True),
        ex('Sódio / creatinina / potássio urinários', '52 mmol/L / 62 mg/dL / 38 mmol/L · FENa 2,5%', '—', True),
        ex('Gasometria arterial em ar ambiente', 'pH 7,32 · pCO₂ 30 · HCO₃ 15 · pO₂ 58 mmHg · lactato 3,6 mmol/L', '—', True),
        ex('Ultrassonografia de abdome', 'Fígado discretamente aumentado, vias biliares sem dilatação, rins de tamanho normal, sem hidronefrose', '—', True),
        ex('Radiografia de tórax', 'Infiltrado alveolar bilateral, predominando em bases e periferia', '—', True),
        ex('Dengue (NS1, IgM) e hepatites (anti-HAV IgM, HBsAg, anti-HBc IgM)', 'Enviadas ao laboratório central · pendentes', '—'),
    ], introducao='Duas hemoculturas foram colhidas antes de qualquer antibiótico, e '
                  'uma alíquota de sangue da admissão ficou guardada no laboratório.',
       laminas={'Radiografia de tórax': lamina('rx_torax_alveolar.jpg', 'Radiografia de tórax',
                'Imagem ilustrativa de outro paciente; o padrão alveolar não '
                'distingue sangue de água ou de pus.', CREDITO_RX)}),

    Q('p1', 1,
      'Qual padrão descreve melhor as alterações das provas hepáticas?', [
      ('Hepatocelular', False),
      ('Colestase intra-hepática', True),
      ('Obstrução biliar extra-hepática', False),
      ('Hemólise', False),
      ('Infiltração hepática', False),
     ], [
      ('O padrão', 'A bilirrubina é de 17,8 mg/dL, 85% dela direta, com '
       'fosfatase alcalina e GGT elevadas e transaminases abaixo de três vezes '
       'o limite. A icterícia é desproporcional à lesão do hepatócito: é '
       'colestase, e o ultrassom sem dilatação das vias biliares a coloca '
       'dentro do fígado.'),
      ('Por que não as outras', 'Hepatite viral, isquêmica ou tóxica com essa '
       'icterícia teria transaminases na casa dos milhares. Obstrução '
       'extra-hepática dilataria as vias biliares. Hemólise eleva a fração '
       'indireta, e aqui a direta domina. Infiltração costuma subir a '
       'fosfatase alcalina muito mais que a bilirrubina.'),
      ('O que esse padrão pede', 'Colestase intra-hepática em doença febril '
       'aguda aparece na sepse, em infecções sistêmicas e em lesão por '
       'fármacos. O paracetamol em dose usual não produz esse quadro. A '
       'pergunta passa a ser qual infecção sistêmica faz isso junto com rim e '
       'pulmão.'),
     ]),

    Q('p2', 2,
      'Creatinina de 3,9 mg/dL, que era 1,0 há quatro dias. Qual a '
      'interpretação mais adequada da lesão renal?', [
      ('Pré-renal por hipovolemia', False),
      ('Lesão tubular aguda', True),
      ('Glomerulonefrite aguda', False),
      ('Obstrução urinária', False),
      ('Doença renal crônica agudizada', False),
     ], [
      ('A classificação', 'A lesão renal aguda se divide primeiro em '
       'pré-renal, intrínseca e pós-renal. Com densidade urinária de 1.012, '
       'sódio urinário de 52 mmol/L, fração de excreção de sódio de 2,5% e '
       'cilindros granulosos, o túbulo já não reabsorve sódio: é lesão '
       'intrínseca tubular. Na pré-renal, a FENa fica abaixo de 1% e a urina '
       'vem concentrada.'),
      ('Por que não as outras', 'Sem cilindros hemáticos nem proteinúria '
       'importante, glomerulonefrite é pouco provável. O ultrassom sem '
       'hidronefrose afasta obstrução, e a creatinina normal quatro dias antes '
       'afasta doença crônica.'),
      ('Dois achados que chamam atenção', 'O potássio está baixo, 3,1, com '
       'potássio urinário de 38 mmol/L: o rim está perdendo potássio, quando '
       'na lesão renal habitual ele o retém. E a fita mostra sangue ++ com '
       'poucas hemácias, o que, com CK de 4.260, indica pigmento muscular na '
       'urina.'),
     ]),

    Q('p3', 3,
      'Gasometria em ar ambiente: pH 7,32, pCO₂ 30, HCO₃ 15, pO₂ 58; sódio '
      '133, cloro 100, lactato 3,6. **Quais três** afirmações estão '
      'corretas?', [
      ('Acidose metabólica com ânion gap elevado', True),
      ('Compensação respiratória adequada', True),
      ('PaO₂/FiO₂ de lesão pulmonar relevante', True),
      ('Alcalose respiratória primária dominante', False),
      ('Acidose explicada pelos vômitos', False),
      ('Indicação de bicarbonato endovenoso', False),
      ('Dispensa de oxigênio suplementar', False),
     ], [
      ('O distúrbio', 'Ânion gap de 133 menos 115, igual a 18: há ácidos não '
       'medidos, que aqui são o lactato e a uremia. Pela fórmula de Winter, '
       '1,5 × 15 + 8 dá cerca de 30, a pCO₂ encontrada: a compensação é a '
       'esperada, sem distúrbio respiratório somado.'),
      ('A troca gasosa', 'PaO₂ de 58 dividida por 0,21 dá 276. Com infiltrado '
       'bilateral, é lesão pulmonar já relevante, num paciente com '
       'frequência respiratória de 28. O alvo de saturação é de 92 a 96%.'),
      ('Por que não as outras', 'Vômito causa alcalose metabólica, não '
       'acidose. Com pH acima de 7,2, bicarbonato endovenoso não traz '
       'benefício e soma sódio e volume a um pulmão que já não troca bem.'),
     ]),

    bifurcacao('b1', 'Decisão', 'As primeiras horas',
      'Ele está hipotenso, ictérico e hipoxêmico, com lesão tubular e '
      'colestase. As hemoculturas já foram colhidas e as sorologias estão '
      'pendentes. Como você conduz?', [
      caminho('Oxigênio, leito monitorizado e ceftriaxona 2 g endovenosa agora',
              'tratado',
              'Numa infecção sistêmica grave ainda sem agente, o antibiótico '
              'empírico de amplo espectro vem no primeiro atendimento.'),
      caminho('Oxigênio e hidratação; escolher o antibiótico quando saírem as '
              'sorologias', 'espera',
              'Sorologias e culturas levam dias, e a mortalidade da sepse sobe '
              'a cada hora sem antibiótico.'),
      caminho('Conduzir como dengue grave: cristaloide 20 mL/kg em bolus '
              'repetidos, sem antibiótico', 'volume',
              'Crepitações e hipoxemia pedem cautela com volume, e a colestase '
              'com lesão tubular não é o padrão da dengue.'),
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
       'Duas horas depois da primeira dose, ele tem calafrios, febre de 40 °C '
       'e queda da pressão para 84/50. Com 500 mL de cristaloide e '
       'antitérmico, melhora em quatro horas. A equipe mantém a ceftriaxona.',
       'Na madrugada, a tosse fica úmida e ele expectora sangue vivo.'),

    pg('hemorragia', 'Segundo dia de internação',
       'Saturação de 83% com máscara com reservatório, frequência '
       'respiratória de 36, hemoptise de 150 mL em seis horas. Diurese de 280 '
       'mL em 24 horas. Creatinina 5,8 mg/dL, potássio 3,4. A hemoglobina '
       'caiu de 11,6 para 9,1 g/dL, sem outro sangramento visível.',
       'A nova radiografia mostra opacidades alveolares confluentes nos dois '
       'pulmões.'),

    estudo('rx_hemorragia', 'Radiografia de tórax',
           'Radiografia ilustrativa de outro paciente, com o padrão descrito '
           'no laudo dele. Descreva a distribuição antes de propor o '
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
         'O padrão alveolar não distingue sangue, água e pus; quem decide é a clínica.']),

    Q('p4', 4,
      'Hemoptise, queda de 2,5 g/dL na hemoglobina e opacidades alveolares '
      'bilaterais. Qual o mecanismo mais provável da piora da hipoxemia?', [
      ('Hemorragia alveolar difusa', True),
      ('Edema pulmonar cardiogênico', False),
      ('Pneumonia bacteriana sobreposta', False),
      ('Tromboembolismo pulmonar', False),
      ('Sobrecarga de volume', False),
     ], [
      ('A tríade', 'Hemoptise, queda de hemoglobina sem outra perda e '
       'infiltrado alveolar difuso formam a tríade da hemorragia alveolar. Nem '
       'toda hemorragia alveolar tem hemoptise volumosa; a queda da '
       'hemoglobina costuma ser o sinal mais confiável.'),
      ('Por que não as outras', 'Edema cardiogênico e sobrecarga não explicam '
       'a queda da hemoglobina, e ele recebeu pouco volume. Pneumonia não '
       'anda com 2,5 g/dL de hemoglobina a menos em um dia. TEP não produz '
       'opacidade alveolar bilateral difusa.'),
      ('O que muda', 'Hemorragia alveolar com lesão renal aguda é uma síndrome '
       'pulmão-rim, e na febre aguda ela é a complicação que mais mata. O '
       'suporte vem antes do diagnóstico etiológico.'),
     ]),

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
       'Com ventilação não invasiva, ele enche a máscara de sangue e não '
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
       'Ele para em atividade elétrica sem pulso, hipoxêmico. É intubado '
       'durante a reanimação, com sangue saindo pelo tubo. O retorno da '
       'circulação acontece depois de 18 minutos.',
       segue='f_obito'),

    pg('uti_tardia', 'Na UTI',
       'Intubado em emergência, com ventilação protetora, pressão expiratória '
       'alta e sedação profunda. A hemodiálise começa no mesmo dia. A '
       'hipoxemia grave dura quatro dias.',
       segue='irmao'),

    pg('uti', 'Na UTI',
       'Intubação planejada, ventilação com volume corrente de 6 mL/kg de '
       'peso predito e pressão expiratória elevada. Hemodiálise no mesmo dia, '
       'depois diária, com reposição de potássio.',
       'A hemoptise diminui no terceiro dia.'),

    pg('irmao', 'O irmão volta',
       'O irmão volta com os documentos, depois de conversar com os colegas de '
       'trabalho. Ele é agente de limpeza urbana. Doze dias antes da febre, '
       'depois de três dias de chuva forte, passou um turno dentro de um canal '
       'alagado, desobstruindo a passagem da água, com uma bota furada.',
       'Revisto com calma, o exame mostra que a dor à compressão é muito '
       'maior nas panturrilhas, e há um corte cicatrizado na planta do pé '
       'direito. Os colegas dizem que o depósito da equipe tem ratos.',
       'As hemoculturas seguem sem crescimento em 48 horas, e as sorologias '
       'de dengue e hepatites voltam não reagentes.'),

    Q('p5', 5,
      'Com essa exposição, a equipe quer confirmar a hipótese a partir da '
      'alíquota guardada da admissão, colhida no sexto dia e antes do '
      'antibiótico. Qual exame confirma o diagnóstico nessa amostra?', [
      ('PCR para Leptospira no sangue', True),
      ('ELISA IgM para leptospira', False),
      ('Microaglutinação em amostra única', False),
      ('Cultura de urina para leptospira', False),
      ('Hemocultura em meio convencional', False),
     ], [
      ('O tempo da doença', 'Na primeira semana a leptospira circula no '
       'sangue, e o anticorpo ainda pode não ter aparecido. Pelo Guia de '
       'Vigilância em Saúde, PCR detectável em sangue colhido até o sétimo '
       'dia confirma o caso.'),
      ('Por que não as outras', 'ELISA IgM antes do sétimo dia pode vir '
       'negativo e não descarta; só a partir do sétimo dia um resultado '
       'negativo pesa contra. A microaglutinação precisa de amostras pareadas, '
       'a segunda entre 14 e 60 dias. A leptospira aparece na urina mais '
       'tarde e cresce devagar, em semanas. Hemocultura convencional não '
       'isola o agente.'),
     ]),

    pg('virada', 'O diagnóstico',
       'Laboratório de referência: **PCR para Leptospira no sangue, DNA '
       'detectado.** ELISA IgM na mesma amostra: não reagente.',
       'É leptospirose na forma grave, a síndrome de Weil: icterícia, lesão '
       'renal e hemorragia pulmonar. A leptospira entra por pele lesada ou '
       'mucosa em contato com água ou lama contaminada pela urina de roedores. '
       'A vasculite capilar difusa explica o que se viu: colestase sem '
       'necrose, lesão tubular com perda de potássio, miosite e sangramento '
       'alveolar. A hemorragia pulmonar é a complicação que mais mata, com '
       'letalidade acima de 50% em várias séries.',
       'A ceftriaxona do primeiro atendimento já tratava a doença, e a febre '
       'com hipotensão duas horas depois da primeira dose ganha agora outro '
       'sentido.'),

    pareamento('p6', 'Pergunta 6',
      'As febres ictéricas e hemorrágicas do Nordeste se sobrepõem. Associe '
      'cada quadro à doença que ele sugere.', [
      par('Sufusão conjuntival, dor na panturrilha e contato com enchente',
          'Leptospirose',
          'A combinação dele. A sufusão é congestão sem secreção.'),
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
      'Sobre o tratamento, **quais três** afirmações estão corretas?', [
      ('Antibiótico endovenoso por pelo menos 7 dias', True),
      ('Diálise precoce e diária', True),
      ('Reposição de potássio pelos controles', True),
      ('Suspender a ceftriaxona pela reação febril', False),
      ('Furosemida para evitar a diálise', False),
      ('Antibiótico só na primeira semana', False),
      ('Corticoide de rotina na forma grave', False),
     ], [
      ('O antibiótico', 'Na forma grave, ceftriaxona ou penicilina cristalina '
       'endovenosa, por pelo menos sete dias; doxiciclina oral fica para a '
       'forma leve. O benefício é maior na primeira semana, mas o antibiótico '
       'está indicado em qualquer fase.'),
      ('A reação da primeira dose', 'Calafrios, febre alta e hipotensão '
       'poucas horas após a primeira dose são a reação de Jarisch-Herxheimer, '
       'descrita nas infecções por espiroquetas. Trata-se o sintoma e o '
       'antibiótico continua.'),
      ('O rim', 'Diálise precoce e diária reduziu a mortalidade frente à '
       'diálise em dias alternados num ensaio brasileiro. Furosemida não muda '
       'a necessidade de diálise. A perda tubular de potássio continua, '
       'sobretudo na fase poliúrica.'),
      ('O que não entra', 'Não há evidência que sustente corticoide de rotina '
       'na forma grave.'),
     ]),

    pg('recuperacao', 'Segunda semana',
       'A diurese volta com poliúria de 4 litros por dia, e o potássio '
       'precisa de reposição. A icterícia regride devagar. A segunda '
       'amostra, no 14.º dia, tem ELISA IgM reagente e microaglutinação com '
       'título de 1:1.600 para o sorogrupo Icterohaemorrhagiae.'),

    Q('p8', 8,
      'Na alta, **quais três** medidas estão corretas?', [
      ('Notificar à vigilância epidemiológica', True),
      ('Investigar o local de trabalho', True),
      ('Acompanhar creatinina e potássio', True),
      ('Isolamento de contato em casa', False),
      ('Antibiótico profilático por três meses', False),
      ('Vacinar os colegas de trabalho', False),
      ('Repetir a microaglutinação todo mês', False),
     ], [
      ('Vigilância e trabalho', 'Leptospirose é de notificação compulsória. '
       'A vigilância investiga os colegas expostos e o depósito, e a '
       'prevenção está em botas íntegras, luvas e controle de roedores.'),
      ('O seguimento', 'A função renal costuma se recuperar em semanas, e a '
       'fase poliúrica perde potássio; creatinina e potássio guiam as '
       'consultas seguintes.'),
      ('O que não entra', 'Não há transmissão entre pessoas, nem vacina humana '
       'disponível no Brasil. Antibiótico profilático depois da infecção '
       'tratada não tem indicação, e repetir a microaglutinação não muda a '
       'conduta num caso confirmado.'),
     ]),

    pg('alta', 'Preparando a alta',
       'A equipe revê com ele e o irmão o que aconteceu: a exposição, a '
       'doença, as sessões de diálise e o que esperar do rim e dos músculos '
       'nas próximas semanas.',
       conforme=('b2', ['alta_cedo', 'f2', 'f2'])),

    pg('alta_cedo', 'Última visita',
       'A diálise foi suspensa no nono dia e a creatinina cai todos os dias. '
       'Ele já caminha pelo corredor sem oxigênio.',
       conforme=('b1', ['f1', 'f2', 'f2'])),

    fim('f1', 'Alta sem diálise',
        'Ele sai no 16.º dia, sem diálise desde o 9.º, com creatinina de 1,6 '
        'mg/dL e bilirrubina em queda. Retoma o trabalho em seis semanas.',
        'Antibiótico no primeiro contato, UTI antes da falência e diálise '
        'precoce foram as três decisões que mudam a mortalidade da síndrome '
        'de Weil.', 'melhor'),

    fim('f2', 'Alta depois de internação prolongada',
        'Ele sai no 27.º dia, com creatinina de 2,1 mg/dL e fraqueza muscular '
        'que leva dois meses para passar.',
        'O atraso do antibiótico ou do suporte intensivo acrescentou dias de '
        'hipoxemia e de diálise, numa forma de letalidade alta.',
        'medio'),

    fim('f_obito', 'Óbito no terceiro dia',
        'Depois da parada, ele evolui com choque refratário e hemorragia '
        'pulmonar maciça, e morre no terceiro dia de internação.',
        'A ventilação não invasiva numa via aérea que sangra, mantida depois '
        'de falhar, levou à parada hipóxica. A hemorragia pulmonar pede '
        'intubação precoce.', 'pior'),

    pagina('retrospectiva', 'Pontos de ensino', '',
        pontos(
            'Na icterícia febril, a primeira leitura é o padrão: bilirrubina '
            'direta muito alta com transaminases abaixo de três vezes o limite '
            'é colestase, e afasta as hepatites virais agudas.',
            'Na lesão renal aguda, FENa acima de 2% com cilindros granulosos '
            'indica lesão tubular. Potássio baixo com potássio urinário alto '
            'é perda tubular, incomum e útil para o diagnóstico.',
            'Hemoptise, queda de hemoglobina e infiltrado alveolar difuso são '
            'hemorragia alveolar até prova em contrário, e pedem suporte '
            'intensivo antes do nome da causa.',
            'A exposição à água e à lama muda a hipótese; ela precisa ser '
            'perguntada, porque o paciente grave raramente a conta.',
            'Na primeira semana, PCR no sangue confirma a leptospirose; o '
            'ELISA IgM negativo antes do sétimo dia não descarta.',
            'Na forma grave: antibiótico endovenoso sem esperar a '
            'confirmação, intubação precoce com ventilação protetora na '
            'hemorragia pulmonar e diálise precoce e diária.'),
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

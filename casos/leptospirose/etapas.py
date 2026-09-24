"""Leptospirose grave (síndrome de Weil) com hemorragia pulmonar.

Alíquota → pergunta, no molde dos casos interativos do //New England//. Oito
perguntas, uma rodada de exames com gabarito e painel, um pareamento das
febres ictéricas e hemorrágicas do Nordeste e três decisões de conduta, uma
delas com óbito. Paciente ficcional; doses segundo o Guia de Vigilância em
Saúde do Ministério da Saúde.
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
       'Joaquim, 38 anos, agente de limpeza urbana em Fortaleza, chega à '
       'emergência trazido pelo irmão no sexto dia de uma febre que começou '
       'de repente, com calafrios, dor de cabeça e uma dor muscular que ele '
       'descreve como "a pior da vida", sobretudo nas batatas das pernas.',
       'No segundo dia foi a uma unidade de pronto atendimento, onde '
       'disseram que era dengue: soro oral, paracetamol e repouso. Há dois '
       'dias está amarelo, e desde a noite passada tosse com raias de sangue '
       'e fica sem ar para ir ao banheiro.'),

    pg('hda', 'História da doença atual',
       'A febre chegou a 39,8 °C nos três primeiros dias, cedeu um pouco no '
       'quarto e voltou. A urina está "cor de guaraná". Urinou pouco hoje. '
       'Teve dois episódios de vômito, sem sangue. Nega dor abdominal forte, '
       'diarreia e manchas no corpo antes da febre.',
       'Os olhos ficaram vermelhos no terceiro dia, "sem remela". O irmão '
       'acha que ele está mais sonolento desde a tarde.'),

    pg('antecedentes', 'Antecedentes e exposições',
       'Sem doenças conhecidas, sem medicações de uso contínuo. Bebe cerveja '
       'nos fins de semana, sem excesso diário. Não fuma. Vacinado contra '
       'febre amarela há seis anos. Não saiu do Ceará no último ano.',
       'Doze dias antes da febre, depois de três dias de chuva forte, '
       'trabalhou na desobstrução de um canal alagado no bairro. A bota '
       'estava furada e ele tinha um corte no pé. Os colegas comentaram que '
       'havia muitos ratos no depósito da equipe.'),

    pagina('exame', 'Exame físico', '',
           vitais(('Temperatura', '38,4 °C', True), ('Pressão arterial', '94/56', True),
                  ('Frequência cardíaca', '116', True), ('Frequência respiratória', '28', True),
                  ('SpO₂ em ar ambiente', '90%', True)),
           topicos(('Estado geral', 'Prostrado, sonolento mas orientado. **Icterícia '
                    'intensa, de tom alaranjado.**'),
                   ('Olhos', '**Sufusão conjuntival bilateral**, sem secreção.'),
                   ('Respiratório', 'Crepitações nas bases dos dois pulmões.'),
                   ('Abdome', 'Fígado a 2 cm do rebordo, doloroso. Baço não palpável.'),
                   ('Membros', '**Dor intensa à compressão das panturrilhas.** Petéquias '
                    'nas pernas. Corte cicatrizado na planta do pé direito.'),
                   ('Neurológico', 'Sem rigidez de nuca, sem déficit focal.')),
           so_kicker=True),

    Q('p1', 1,
      'Febre aguda com icterícia, sufusão conjuntival, mialgia intensa e '
      'hemoptise, em abril, em Fortaleza. **Quais quatro** diagnósticos '
      'precisam ser considerados?', [
      ('Leptospirose', 'Exposição a água de enchente com ferida no pé, '
       'sufusão conjuntival e dor na panturrilha: é a hipótese principal.',
       True),
      ('Malária', 'Ele nunca saiu do Ceará. Malária autóctone no Nordeste é '
       'excepcional; sem viagem à Amazônia, sai da lista.', False),
      ('Dengue grave', 'O diagnóstico que a UPA fez. Plaquetopenia, '
       'sangramento e choque cabem nela — e ela coexiste com leptospirose '
       'na mesma estação.', True),
      ('Febre amarela', 'Ele é vacinado e não entrou em área de mata.',
       False),
      ('Hepatite viral aguda', 'Icterícia com febre obriga a pensar em A e '
       'E, ainda que a mialgia e o rim falem contra.', True),
      ('Hepatite alcoólica', 'Exigiria consumo pesado e diário por anos. '
       'Cerveja de fim de semana não chega lá.', False),
      ('Sepse bacteriana com colangite ou pneumonia', 'Febre, icterícia e '
       'hipotensão também são sepse de foco biliar ou pulmonar. Hemocultura '
       'e ultrassom a separam.', True),
      ('Síndrome de Gilbert', 'Bilirrubina indireta que sobe no jejum, sem '
       'febre, sem doença.', False),
      ('Mononucleose infecciosa', 'Faz febre e hepatite leve, mas não '
       'insuficiência renal com hemoptise.', False),
     ], 'Água de enchente, olho vermelho e panturrilha dolorosa'),

    Q('ex1', 2,
      'Na emergência, **quais cinco** exames são os mais apropriados?', [
      ('Hemograma com plaquetas', 'Plaquetopenia e neutrofilia são comuns na '
       'leptospirose; hemoconcentração puxa para dengue.', True),
      ('Creatinina, ureia e potássio', 'A lesão renal da leptospirose é '
       'frequentemente não oligúrica e com hipocalemia. Os três números '
       'decidem diálise e reposição.', True),
      ('Gota espessa', 'Sem viagem à região amazônica, o exame não tem lugar.',
       False),
      ('Bilirrubinas, transaminases e creatinoquinase', 'Bilirrubina muito '
       'alta com transaminases modestas e CK elevada é o padrão que separa '
       'leptospirose de hepatite.', True),
      ('Tomografia de crânio', 'Sem déficit focal, a sonolência é '
       'metabólica. Não é prioridade.', False),
      ('Radiografia de tórax', 'Hemoptise e hipoxemia: o pulmão é o órgão que '
       'mata na leptospirose grave.', True),
      ('ELISA IgM para leptospira, com hemocultura em meio específico',
       'Sorologia no sexto dia e cultura antes do antibiótico. Nenhum dos '
       'dois deve atrasar o tratamento.', True),
      ('Sorologia para hantavírus', 'A hantavirose das Américas é '
       'cardiopulmonar e de área rural do Sul e Centro-Oeste.', False),
      ('Biópsia hepática', 'Não tem indicação na icterícia febril aguda.',
       False),
      ('Antiestreptolisina O', 'Não explica nada do quadro.', False),
     ], 'A equipe pede os cinco, mais dengue, hepatites e gasometria'),

    painel('res1', 'Na emergência', 'O que a equipe pediu', [
        ex('Hemoglobina / hematócrito', '11,6 g/dL / 34%', 'Hb 13,5–17,5 g/dL', True),
        ex('Leucócitos', '14.800/mm³ · neutrófilos 88%', '4.000–11.000/mm³', True),
        ex('Plaquetas', '52.000/mm³ {{(145.000 na UPA)}}', '150.000–450.000/mm³', True),
        ex('Creatinina / ureia', '3,9 / 148 mg/dL {{(creatinina 1,0 na UPA)}}', 'até 1,3 / 45 mg/dL', True),
        ex('Potássio / sódio', '3,1 / 133 mmol/L', 'K 3,5–5,0 · Na 135–145', True),
        ex('Bilirrubina total / direta', '17,8 / 15,2 mg/dL', 'até 1,2 / 0,3 mg/dL', True),
        ex('AST / ALT', '112 / 84 U/L', 'até 40 / 41 U/L', True),
        ex('Creatinoquinase', '4.260 U/L', 'até 190 U/L', True),
        ex('INR', '1,3', 'até 1,2', True),
        ex('Gasometria arterial', 'pH 7,33 · pCO₂ 30 · HCO₃ 16 · pO₂ 58 mmHg', '—', True),
        ex('Dengue: NS1 e IgM', 'Não reagentes', 'não reagentes'),
        ex('Hepatites: anti-HAV IgM, HBsAg, anti-HEV IgM', 'Não reagentes', 'não reagentes'),
        ex('ELISA IgM para leptospira', 'Não reagente', 'não reagente'),
        ex('Radiografia de tórax', 'Infiltrado alveolar bilateral, predominando em bases e periferia', '—', True),
    ], introducao='Hemoculturas e cultura para leptospira foram colhidas antes de qualquer antibiótico.',
       laminas={'Radiografia de tórax': lamina('rx_torax_alveolar.jpg', 'Radiografia de tórax',
                'Imagem ilustrativa de outro paciente; o padrão alveolar não '
                'distingue sangue de água ou de pus.', CREDITO_RX)}),

    Q('p3', 3,
      'Bilirrubina de 17,8 com AST de 112, CK de 4.260, potássio de 3,1 e '
      'creatinina de 3,9. **Quais três** afirmações estão corretas?', [
      ('A desproporção entre bilirrubina e transaminases fala contra hepatite viral',
       'Na hepatite aguda as transaminases passam de mil. Na leptospirose a '
       'icterícia é de colestase com lesão hepatocelular discreta.', True),
      ('Transaminases acima de 1.000 são esperadas na leptospirose',
       'É o contrário: raramente passam de 200 a 300.', False),
      ('A CK alta traduz a miosite que dói na panturrilha',
       'A rabdomiólise contribui para a lesão renal e é um dado a favor do '
       'diagnóstico.', True),
      ('A hipocalemia exclui lesão renal aguda grave',
       'A leptospirose lesa o túbulo proximal e perde potássio: lesão renal '
       'com hipocalemia é a assinatura dela.', False),
      ('A lesão renal costuma ser não oligúrica e hipocalêmica no início',
       'Nefrite tubulointersticial com defeito de reabsorção de sódio e '
       'potássio. A oligúria é sinal de gravidade.', True),
      ('A icterícia é hemolítica, de bilirrubina indireta',
       'A bilirrubina é quase toda direta: colestase, não hemólise.', False),
      ('A plaquetopenia exclui leptospirose e confirma dengue',
       'Plaquetopenia é comum na leptospirose grave e associa-se a pior '
       'prognóstico.', False),
     ], 'Bilirrubina alta, transaminase baixa, CK alta e potássio baixo'),

    pergunta('p4', 'Pergunta 4',
      'ELISA IgM para leptospira **não reagente no sexto dia**. Qual a conduta?', [
      alt('Afastar leptospirose e tratar como dengue grave',
          'NS1 e IgM de dengue foram negativos, e o IgM da leptospira só se '
          'torna positivo depois do quinto ao sétimo dia.'),
      alt('Tratar presuntivamente e repetir a sorologia em uma a duas semanas',
          'Na suspeita clínico-epidemiológica, a forma grave é tratada sem '
          'confirmação. A segunda amostra e a microaglutinação pareada '
          'confirmam depois.', certa=True),
      alt('Esperar a microaglutinação antes de qualquer antibiótico',
          'O resultado leva dias. Na síndrome de Weil, cada dia sem '
          'antibiótico pesa na mortalidade.'),
      alt('Solicitar biópsia renal para confirmar nefrite',
          'A clínica e a epidemiologia bastam para tratar. Biópsia não '
          'tem papel aqui.'),
      alt('Repetir o mesmo ELISA amanhã e decidir pelo resultado',
          'Um dia não muda a cinética dos anticorpos, e a conduta já está '
          'indicada.'),
    ], titulo_resposta='Sorologia negativa cedo não afasta, e a forma grave não espera'),

    bifurcacao('b1', 'Decisão', 'O antibiótico',
      'Joaquim está hipotenso, ictérico e hipoxêmico. Como você trata?', [
      caminho('Internar em leito monitorizado e iniciar penicilina cristalina '
              'endovenosa agora', 'tratado',
              'Penicilina cristalina 1,5 milhão de UI de 6/6 horas (ou '
              'ceftriaxona 1 a 2 g/dia) é o esquema da forma grave.'),
      caminho('Doxiciclina oral e retorno em 48 horas', 'doxi',
              'É o esquema da forma leve, ambulatorial. Joaquim não tem forma '
              'leve.'),
      caminho('Hidratar e aguardar a segunda sorologia para iniciar antibiótico',
              'espera',
              'A confirmação é importante para a vigilância, não para a '
              'decisão de tratar.'),
    ]),

    pg('doxi', 'Na manhã seguinte',
       'Joaquim volta à emergência carregado pelo irmão, doze horas depois: '
       'saturação de 84%, hemoptise de 100 mL e urina "quase nada". É '
       'internado, e a penicilina cristalina começa com um dia de atraso.',
       segue='tratado'),

    pg('espera', 'Dezoito horas depois',
       'Sob soro e oxigênio, a saturação cai para 85% e a urina para 20 mL '
       'por hora. A plantonista inicia penicilina cristalina com dezoito '
       'horas de atraso.',
       segue='tratado'),

    pg('tratado', 'Primeiras horas de antibiótico',
       'Duas horas depois da primeira dose, Joaquim tem calafrios, febre de '
       '40 °C e piora da pressão por algumas horas. A equipe reconhece uma '
       '**reação de Jarisch-Herxheimer**, trata com volume e antitérmico e '
       'mantém a penicilina.',
       'Na madrugada, a tosse fica úmida. Ele expectora sangue vivo.'),

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
        ['Opacidades alveolares bilaterais, confluentes, com predomínio central e inferior.', 'Na leptospirose, hipoxemia com hemoptise e queda de hemoglobina é hemorragia pulmonar: a vasculite capilar difusa que faz a mortalidade da forma grave passar de 50%.']),

    Q('p5', 5,
      'Hemorragia pulmonar, oligúria e sonolência. **Quais três** fatores '
      'associam-se a maior mortalidade na leptospirose grave?', [
      ('Acometimento pulmonar com hemorragia', 'O preditor mais forte de '
       'morte nas séries brasileiras.', True),
      ('Icterícia intensa', 'É frequente e dramática, mas não prediz morte '
       'de forma independente.', False),
      ('Oligúria', 'A lesão renal oligúrica pesa mais que a não oligúrica.',
       True),
      ('Creatinoquinase acima de 1.000 U/L', 'Ajuda o diagnóstico; não é '
       'preditor independente.', False),
      ('Alteração do nível de consciência', 'Sonolência ou confusão na '
       'admissão multiplica o risco.', True),
      ('Febre acima de 39 °C', 'Comum a quase todos, sem valor '
       'prognóstico.', False),
      ('Sufusão conjuntival', 'Sinal diagnóstico, não prognóstico.', False),
     ], 'Pulmão, rim e cérebro'),

    bifurcacao('b2', 'Decisão', 'O pulmão que sangra',
      'Saturação de 83% com máscara, hemoptise e oligúria. O que você faz?', [
      caminho('UTI: intubação precoce com ventilação protetora e diálise '
              'precoce e diária', 'uti',
              'Proteger o pulmão com volumes baixos e tirar o excesso de '
              'volume e as toxinas urêmicas cedo reduz a mortalidade.'),
      caminho('Ventilação não invasiva e furosemida em dose alta', 'vni',
              'A máscara não protege uma via aérea que sangra, e diurético não '
              'converte a lesão renal nem reduz a mortalidade.'),
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
          'A tríade epidemiológica e clínica de Joaquim. A sufusão é '
          'congestão sem secreção.'),
      par('Dor abdominal, vômitos e hematócrito subindo na defervescência',
          'Dengue grave',
          'O extravasamento plasmático começa quando a febre cai: são os '
          'sinais de alarme.'),
      par('Febre, icterícia e pulso lento para a febre, sem vacina, após mata',
          'Febre amarela',
          'O sinal de Faget e a hepatite com transaminases de milhares. '
          'A vacina previne.'),
      par('Febre em picos, anemia e esplenomegalia depois de viagem ao Pará',
          'Malária por Plasmodium vivax',
          'A gota espessa decide. No Nordeste, quase sempre importada.'),
      par('Icterícia com transaminases acima de 1.000 e pouca febre',
          'Hepatite A aguda',
          'Hepatite hepatocelular pura, sem rim nem pulmão.'),
    ], opcoes=['Leptospirose', 'Dengue grave', 'Febre amarela',
               'Malária por Plasmodium vivax', 'Hepatite A aguda', 'Hantavirose'],
    titulo_resposta='O detalhe da história decide mais que o laboratório',
    nota='A opção que sobrou, hantavirose, é cardiopulmonar, rural, do Sul e '
         'do Centro-Oeste, e sem icterícia.'),

    Q('p7', 7,
      'Sobre o tratamento da leptospirose grave, **quais três** afirmações '
      'estão corretas?', [
      ('Penicilina cristalina ou ceftriaxona endovenosa por sete dias',
       'Os dois esquemas têm eficácia semelhante; a doxiciclina oral é da '
       'forma leve.', True),
      ('Furosemida converte a oligúria e evita diálise',
       'Não muda a necessidade de diálise nem a mortalidade.', False),
      ('Diálise precoce e diária reduz a mortalidade',
       'Comparada à diálise em dias alternados, reduziu a mortalidade num '
       'ensaio brasileiro.', True),
      ('O potássio deve ser reposto conforme os controles',
       'A perda tubular de potássio continua na fase poliúrica.', True),
      ('O antibiótico só tem benefício nos primeiros quatro dias',
       'Recomenda-se tratar em qualquer fase da doença.', False),
      ('A reação de Jarisch-Herxheimer obriga a suspender a penicilina',
       'É liberação de toxinas das espiroquetas mortas: trata-se o sintoma '
       'e mantém-se o antibiótico.', False),
      ('Corticoide é tratamento de rotina da forma grave',
       'Não há evidência para uso rotineiro.', False),
     ], 'Antibiótico em qualquer fase, diálise cedo, potássio sempre'),

    pg('recuperacao', 'Segunda semana',
       'A diurese volta com poliúria de 4 litros por dia, e o potássio '
       'precisa de reposição. A icterícia regride devagar. A segunda '
       'sorologia, no 14.º dia, é **ELISA IgM reagente**, e a '
       'microaglutinação mostra soroconversão para o sorovar '
       'Icterohaemorrhagiae.'),

    Q('p8', 8,
      'Na alta, **quais três** medidas estão corretas?', [
      ('Notificar o caso à vigilância epidemiológica',
       'Leptospirose é de notificação compulsória. A vigilância investiga o '
       'local e os colegas expostos.', True),
      ('Isolamento de contato em casa',
       'Não há transmissão entre pessoas. O risco está na água e nos '
       'roedores.', False),
      ('Investigar o local de trabalho e orientar equipamento de proteção',
       'Botas íntegras e luvas na limpeza de canais. Controle de roedores no '
       'depósito.', True),
      ('Antibiótico profilático por três meses',
       'Não há indicação depois de tratada a infecção.', False),
      ('Acompanhar creatinina e potássio nas semanas seguintes',
       'A função renal costuma recuperar, mas em semanas, e a fase poliúrica '
       'perde potássio.', True),
      ('Vacina humana para os colegas',
       'Não há vacina humana disponível no Brasil.', False),
      ('Repetir a microaglutinação todo mês',
       'A soroconversão já confirmou. Repetir não muda nada.', False),
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
        'hipoxemia e de diálise. Ele sobreviveu à forma que mata metade.',
        'medio'),

    fim('f_obito', 'Óbito no terceiro dia',
        'Depois da parada, Joaquim evolui com choque refratário e hemorragia '
        'pulmonar maciça. Morre no terceiro dia de internação.',
        'A ventilação não invasiva numa via aérea que sangra, mantida depois '
        'de falhar, levou à parada hipóxica. A hemorragia pulmonar da '
        'leptospirose pede intubação precoce.', 'pior'),

    pagina('retrospectiva', 'Retrospectiva', '',
        tabela(['Momento', 'O dado', 'O que decidiu'], [
            ['Na UPA, segundo dia', 'Febre súbita, mialgia de panturrilha, enchente '
             'dez dias antes', 'Perguntar pela água muda o diagnóstico de dengue '
             'para leptospirose'],
            ['Na emergência', 'Bilirrubina 17,8 com AST 112, CK alta, potássio baixo',
             'O padrão laboratorial da síndrome de Weil'],
            ['Sorologia', 'IgM não reagente no sexto dia', 'Tratar sem esperar: o '
             'anticorpo vem depois'],
            ['Segundo dia', 'Hemoptise, hipoxemia, oligúria', 'UTI, intubação protetora '
             'e diálise precoce'],
            ['Alta', 'Soroconversão na microaglutinação', 'Notificar e proteger quem '
             'trabalha na água'],
        ]),
        so_kicker=True),

    pg('referencias', 'Fontes e limites',
       'Paciente, valores e percursos são ficcionais. A cena de abertura é uma ilustração autoral gerada por inteligência artificial para este caso; não é fotografia nem documentação clínica.',
       'Ministério da Saúde. Guia de Vigilância em Saúde, capítulo de '
       'leptospirose, e Leptospirose: diagnóstico e manejo clínico. Andrade e '
       'cols., Clin J Am Soc Nephrol 2007 (diálise diária). Spichler e cols., '
       'Am J Trop Med Hyg 2008 (preditores de mortalidade). Radiografia: '
       'Samir, Wikimedia Commons, CC BY-SA 3.0 — outro paciente.'),
]

REVISAO = []

"""Camila: evolução psiquiátrica, motora e autonômica de encefalite anti-NMDAR.
Revisão de 23/10/2026. Paciente e percursos ficcionais; fontes ao final.
Investigação e tratamento não aguardam o anticorpo quando há indicação clínica.
"""
import json
from pathlib import Path

from motor.estudo_imagem import estudo
from motor.etapas import (alt, bifurcacao, caminho, capa, desfecho, op, p,
                          pagina, painel, par, pareamento, pergunta, pontos,
                          topicos, vitais)

TITULO = 'Dez noites'
RODAPE = 'Paciente ficcional · evoluções simuladas para ensino'
COR = '#7c3aed'
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
    capa(TITULO, fundo='cena-paciente.png', kicker='Caso interativo',
         selo='Paciente ficcional · procedência e créditos na última tela'),

    pg('historia', 'Apresentação',
       'Camila, de 24 anos, estudante do último ano de arquitetura em Teresina, '
       'é trazida à emergência pela mãe e pelo irmão. Há dez dias dorme duas ou '
       'três horas por noite, anda pela casa de madrugada e diz que os vizinhos '
       'instalaram câmeras para filmá-la. Nos últimos três dias a fala ficou '
       'rápida e difícil de acompanhar. "Ela não é assim", diz a mãe.',
       'Há cinco dias a família a levou a uma unidade de pronto atendimento, '
       'onde o quadro foi atribuído à ansiedade com o trabalho de conclusão de '
       'curso; recebeu clonazepam 0,5 mg à noite, sem melhora do sono. Ontem '
       'saiu de casa descalça, às 3 horas, e foi trazida de volta por um vizinho.',
       'A mãe lembra que, cerca de duas semanas antes de tudo começar, Camila '
       'passou quatro dias com dor de cabeça, febre baixa e dor no corpo, '
       'tratados em casa como virose. A família nega uso de drogas, trauma na '
       'cabeça e remédios novos além do clonazepam.'),

    pagina('ficha', 'Ficha do paciente', '',
           topicos(('Antecedentes', 'Rinite alérgica. Nunca consultou psiquiatra. Aos '
                    '22 anos, uma ultrassonografia transvaginal pedida por cólica '
                    'menstrual descreveu um cisto de 3 cm no ovário direito, "de '
                    'aspecto benigno"; o controle sugerido não foi feito.'),
                   ('Medicações', 'Anticoncepcional oral combinado há quatro anos. '
                    'Clonazepam 0,5 mg à noite há cinco dias. Loratadina nas crises de '
                    'rinite.'),
                   ('Hábitos', 'Duas a três latas de cerveja nos fins de semana. Fumou '
                    'maconha algumas vezes aos 19 anos; a família e as amigas dizem que '
                    'não usa há anos. Não fuma tabaco.'),
                   ('Vida social', 'Mora com a mãe e o irmão. Entrega o trabalho de '
                    'conclusão em três semanas; a orientadora achou a última versão '
                    '"desconexa". Não viajou nos últimos meses.'),
                   ('Família', 'Tia materna em tratamento para depressão. Pai '
                    'hipertenso. Sem epilepsia, esquizofrenia ou transtorno bipolar '
                    'conhecidos.')),
           so_kicker=True),

    pagina('exame', 'Exame físico', '',
           vitais(('Temperatura', '37,4 °C', False),
                  ('Pressão arterial', '132/84', False),
                  ('Frequência cardíaca', '108', True),
                  ('Frequência respiratória', '18', False),
                  ('SpO₂ em ar ambiente', '98%', False),
                  ('Glicemia capilar', '94 mg/dL', False)),
           topicos(('Estado geral', 'Inquieta, levanta da maca várias vezes. Corada e '
                    'hidratada.'),
                   ('Exame mental', 'Vígil. Diz o próprio nome e reconhece a mãe; diz '
                    'que estamos em março, quando é agosto, e não sabe o nome do '
                    'hospital. A atenção se perde no meio das perguntas. Fala '
                    'acelerada, com saltos de assunto, e ideias de perseguição pelos '
                    'vizinhos. Nega ouvir vozes, mas olha várias vezes para o canto da '
                    'sala.'),
                   ('Neurológico', 'Pupilas isocóricas e fotorreagentes, sem rigidez de '
                    'nuca, força e reflexos simétricos, marcha normal. Em dois '
                    'momentos para no meio da frase por cerca de dez segundos, com o '
                    'olhar parado, e retoma sem lembrar do que dizia.'),
                   ('Coração e pulmões', 'Taquicardia regular, sem sopros. Murmúrio '
                    'presente, sem ruídos adventícios.'),
                   ('Pele', 'Sem lesões e sem marcas de agulha.')),
           so_kicker=True),

    pg('rastreio', 'Avaliação inicial',
       'A equipe verifica glicemia, sinais vitais e exame neurológico e colhe hemograma, eletrólitos e funções renal e hepática. Pela possibilidade de encefalite, a avaliação neurológica e o aciclovir empírico são organizados desde a admissão, em paralelo aos exames básicos.',
       'A sequência das telas organiza a leitura dos resultados; não significa esperar o rastreio metabólico terminar para investigar as pausas com amnésia e a desorientação.'),

    painel('res1', 'Primeiros exames', 'Sangue', [
        ex('Hemoglobina / leucócitos', '13,4 g/dL / 9.800/mm³ · neutrófilos 72%', 'Hb 12–16 · 4.000–11.000'),
        ex('Plaquetas', '254.000/mm³', '150.000–450.000/mm³'),
        ex('Proteína C reativa', '4 mg/L', 'até 5 mg/L'),
        ex('Sódio / potássio / cálcio', '138 / 4,1 mmol/L / 9,4 mg/dL', 'Na 135–145 · K 3,5–5,0 · Ca 8,5–10,5'),
        ex('Glicose', '96 mg/dL', '70–99 mg/dL'),
        ex('Ureia / creatinina', '24 / 0,7 mg/dL {{(TFG 124, CKD-EPI 2021)}}', 'até 42 / 0,6–1,1'),
        ex('AST / ALT', '22 / 18 U/L', 'até 32 / 33 U/L'),
    ], introducao='Colhidos na chegada à emergência.'),

    painel('res1b', 'Primeiros exames', 'Urina e avaliação reprodutiva', [
        ex('Urina tipo 1', 'Sem alterações', '—'),
        ex('Beta-hCG sérico', 'Negativo', 'negativo'),
    ], introducao='Teste de gravidez pela idade reprodutiva e planejamento de exames e tratamento.'),

    pg('reavaliacao_inicial', 'Reexame ainda na emergência',
       'Com glicemia e eletrólitos sem alterações explicativas, Camila continua confundindo a data. Durante nova conversa, interrompe a frase, fixa o olhar e depois não lembra do intervalo. A mãe confirma que isso também ocorreu em casa. A ausência de déficit motor não torna o episódio apenas psiquiátrico.',
       'A equipe acrescenta exames dirigidos para causas tóxicas, endócrinas e infecciosas tratáveis. O ECG orienta a segurança do manejo da agitação; CK basal é colhida pela agitação persistente antes de eventual antipsicótico. A investigação neurológica corre em paralelo.'),

    Q('p1', 1,
      'Após a avaliação inicial, quais três exames você prioriza?', [
      ('Eletroencefalograma', True),
      ('Punção lombar diagnóstica', True),
      ('Ressonância de encéfalo', True),
      ('FAN sérico', False),
      ('Vitamina B12 sérica', False),
     ], [('Investigar função, inflamação e estrutura', '**EEG** procura atividade epiléptica nas pausas estereotipadas. **Líquor** investiga inflamação e infecção após avaliação de segurança. **RM** pesquisa lesões não identificadas pela TC e pode apoiar uma causa; seu resultado normal não encerra a investigação.'), ('Outros exames possíveis', '**FAN/complemento** ganham prioridade com manifestações sistêmicas de autoimunidade, não descritas. **B12/folato** entram na avaliação de causas reversíveis, mas a evolução em dez dias, o pródromo e os episódios breves tornam a investigação direta do cérebro mais urgente.'), ('Como organizar a alteração de comportamento', 'Quadro psiquiátrico primário, intoxicação, distúrbio metabólico e doença cerebral entram na comparação. Desorientação, episódios estereotipados e progressão rápida justificam investigação neurológica. Uma imagem normal não basta para atribuir os sintomas a uma causa psiquiátrica.')]),

    painel('rastreio_dirigido', 'Investigação dirigida', 'Contexto neuropsiquiátrico', [
        ex('TSH', '1,9 mUI/L', '0,4–4,0 mUI/L'),
        ex('Creatinoquinase', '210 U/L', 'até 170 U/L', True),
        ex('Triagem toxicológica na urina', 'Benzodiazepínicos positivos · cocaína, canabinoides e anfetaminas negativos', '—', True),
        ex('Etanol sérico', 'Não detectado', 'não detectado'),
        ex('Testes para HIV e sífilis', 'Não reagentes', 'não reagentes'),
        ex('Eletrocardiograma', 'Taquicardia sinusal, 106 bpm · QTc 428 ms · sem outras alterações', '—'),
    ], introducao='Resultados complementares do primeiro atendimento. A triagem toxicológica negativa não exclui todas as substâncias; não se aguardam esses testes para avaliar encefalite.'),

    estudo('tc_cranio', 'Tomografia de crânio sem contraste',
           'Feita na emergência, pela desorientação. Corte axial na altura dos '
           'átrios dos ventrículos laterais.',
           IMG / 'tc_cranio.jpg',
           'Tomografia · recortada no corte axial.',
           credito_meta(IMG / 'tc_cranio.jpg.json'),
        [
         ((335, 345), (130, 420), '**Parênquima frontal** com diferenciação normal entre '
          'substância cinzenta e branca, sem hipodensidade.', 12),
         ((505, 470), (720, 330), '**Fissura inter-hemisférica** na linha média, sem desvio.', -12),
         ((607, 868), (820, 1000), '**Plexo coroide calcificado** no átrio do ventrículo '
          'lateral, achado habitual e sem significado clínico.', 12),
        ],
        ['Sem lesão expansiva, sangramento, hipodensidade ou hidrocefalia. '
         'Ventrículos de tamanho normal. Calcificações fisiológicas do plexo '
         'coroide.',
         'Sem alteração estrutural aguda identificada.']),

    pg('plano', 'Primeira noite',
       'Camila permanece no hospital geral, com avaliação conjunta de neurologia e psiquiatria. A desorientação e as pausas com amnésia impedem encerrar a investigação como psicose primária. Inicia-se aciclovir empírico enquanto se investiga encefalite infecciosa.',
       'O EEG inicial mostra lentificação difusa, sem capturar uma pausa. O primeiro líquor tem 18 células/mm³, predomínio linfocítico, proteína 48 mg/dL e glicose preservada; Gram sem bactérias. A primeira PCR para HSV é negativa. A equipe mantém investigação infecciosa e envia líquor e soro para anticorpos neuronais, sem esperar a resposta às medidas de agitação.'),

    pg('noite1', 'Agitação e fala em mudança',
       'Na mesma noite, mesmo em ambiente calmo e com a mãe presente, Camila tenta sair e retirar o acesso. Recebe haloperidol intramuscular para agitação de risco e mais uma dose oral antes da revisão do plano. Não há uso programado prolongado.',
       'Dorme algumas horas, mas ao despertar a fala, antes acelerada, está escassa. Passa a repetir a última palavra da mãe e depois deixa de responder verbalmente. A redução da fala persiste quando está desperta, sem nova dose de sedativo.'),

    pagina('dia2', 'Segundo dia, 9 horas', '',
           p('Na primeira noite dormiu quatro horas. No primeiro dia ficou mais '
             'quieta e passou a responder com monossílabos; à noite parou de falar. '
             'Às 9 horas do segundo dia a enfermagem chama: Camila está febril, '
             'suada e rígida no leito, e não responde ao chamado.'),
           vitais(('Temperatura', '39,2 °C', True),
                  ('Pressão em duas horas', '168/100 a 96/58', True),
                  ('Frequência cardíaca', '132', True),
                  ('Frequência respiratória', '24', True),
                  ('SpO₂ em ar ambiente', '96%', False)),
           topicos(('Neurológico', 'Olhos abertos, não fixa o olhar nem obedece a '
                    'comandos. Rigidez em cano de chumbo nos quatro membros, igual em '
                    'toda a amplitude do movimento. Reflexos simétricos, sem clônus. '
                    'Pupilas de 3 mm, fotorreagentes.'),
                   ('Pele', 'Sudorese intensa, sem exantema.'),
                   ('Exames da manhã', 'Creatinoquinase 4.800 U/L (210 na chegada). '
                    'Leucócitos 14.200/mm³. Creatinina 0,9 mg/dL. Urina escura, com '
                    'sangue ++ na fita e 2 hemácias por campo.')),
           so_kicker=True),

    Q('p2', 2,
      'Qual interpretação melhor explica a mudança do quadro?', [
      ('Reação ao bloqueio dopaminérgico sobre quadro cerebral ainda não esclarecido', True),
      ('Síndrome serotoninérgica como explicação da piora', False),
      ('Abstinência de clonazepam como explicação do quadro inteiro', False),
      ('Catatonia maligna primária demonstrada pela elevação de CK', False),
      ('Sepse como explicação única da alteração mental e da rigidez', False),
     ], [('A cronologia discrimina', 'A exposição recente ao haloperidol, a rigidez difusa e a lesão muscular sustentam síndrome neuroléptica maligna. Ela explica a piora, mas não os dez dias anteriores de psicose, desorientação e pausas.'), ('O concorrente próximo', 'Catatonia maligna pode se sobrepor e CK não a distingue sozinha. Não há exposição serotoninérgica convincente nem clônus descrito; o uso breve de clonazepam e sua suspensão tampouco explicam a síndrome inteira. Infecção permanece investigável, sem apagar a associação temporal com o antipsicótico.'), ('Doença de base ou complicação', 'Uma reação ao antipsicótico pode explicar a piora sem explicar o início do caso. Sepse, catatonia e reações a medicamentos compartilham sinais. A relação temporal, a lista de medicamentos e o exame neurológico ajudam a separar processos que podem coexistir.')]),

    pg('nms', 'Duas hipóteses que podem se sobrepor',
       'A equipe considera reação neuroléptica grave e catatonia associada à doença cerebral. A temporalidade com haloperidol favorece síndrome neuroléptica maligna, mas não prova que toda a rigidez e disautonomia tenham uma única causa. CK elevada mede lesão muscular, não distingue sozinha essas síndromes.',
       'Camila é transferida à UTI para resfriamento, hidratação guiada e vigilância renal e autonômica. A investigação da encefalite continua; não se considera a reação ao fármaco uma explicação para os dez dias anteriores.'),

    pg('retirada', 'Retirada e suporte',
       'A equipe suspende haloperidol e evita outros bloqueadores dopaminérgicos. Mantém hidratação, resfriamento, prevenção de complicações e vigilância respiratória e renal. A presença de mutismo e posturas mantidas motiva avaliação de catatonia.'),

    bifurcacao('b1', 'Decisão', 'Avaliar a redução da fala',
      'Após retirar haloperidol e iniciar suporte, persistem mutismo e posturas mantidas. Qual estratégia acrescentar à avaliação especializada?', [
      caminho('Prova com lorazepam intravenoso monitorizada', 'prova_lorazepam',
              'Pode ajudar a avaliar componente catatônico, com observação de resposta e da ventilação; não define a causa da encefalite.'),
      caminho('Exame neurológico seriado sem sedativo adicional', 'exame_sem_sedativo',
              'Preserva a leitura do exame e evita depressão respiratória, mas ausência de prova não resolve a hipótese de catatonia.'),
    ]),

    pg('prova_lorazepam', 'Resposta parcial à prova',
       'Sob monitorização na UTI, a prova reduz transitoriamente as posturas e a resistência ao movimento. Camila continua sem contato consistente e não recupera a fala. A resposta parcial apoia um componente catatônico, mas não explica a inflamação liquórica nem exclui intolerância neuroléptica sobreposta.',
       segue='uti'),

    pg('exame_sem_sedativo', 'Exame com menor interferência farmacológica',
       'Nas horas seguintes, sem sedativo adicional, a temperatura e a resistência passiva diminuem com o suporte, mas Camila continua muda e sem seguir comandos. A persistência da alteração cognitiva fora do pico febril reforça o processo cerebral subjacente.',
       segue='uti'),

    pg('uti', 'Na terapia intensiva',
       'Sem antipsicótico, com suporte e sintomáticos titulados conforme a necessidade, a febre cede e a CK começa a cair. Hemoculturas e urocultura são '
       'negativas.',
       'A rigidez diminui, mas Camila não volta: segue sem falar, de olhos '
       'abertos, sem seguir comandos, e a pressão e a frequência cardíaca oscilam '
       'várias vezes por hora.'),

    pg('movimentos', 'Quinto dia',
       'Aparecem movimentos que não param: Camila mastiga sem nada na boca, '
       'projeta a língua e contrai os lábios, de forma repetida, por horas, mesmo '
       'sob sedação leve. Os dedos da mão direita se mexem como se tocassem '
       'piano. À tarde tem uma crise tônico-clônica generalizada de dois minutos, '
       'tratada com diazepam e levetiracetam; depois dela, não abre mais os olhos '
       'ao chamado.',
       'O aparecimento de discinesias e crise, apesar da queda da CK e da febre, amplia a síndrome cerebral. A neurologia repete o líquor e o teste molecular para herpes (PCR), mantém aciclovir com dose revista pela função renal e realiza RM e vídeo-EEG. Os anticorpos já foram enviados na primeira noite para um laboratório de referência. Se esse exame não for feito no hospital, a equipe organiza o envio da amostra e discute o tratamento pela suspeita clínica, sem aguardar sua confirmação.'),

    painel('lcr', 'Quinto dia', 'Líquor', [
        ex('Aspecto / pressão de abertura', 'Límpido · 18 cmH₂O', 'límpido · até 20'),
        ex('Células', '38/mm³ · linfócitos 92%', 'até 5/mm³', True),
        ex('Hemácias', '2/mm³', '—'),
        ex('Proteína', '54 mg/dL', '15–45 mg/dL', True),
        ex('Glicose', '64 mg/dL {{(glicemia 108)}}', 'cerca de 2/3 da glicemia'),
        ex('Lactato', '2,1 mmol/L', 'até 2,8 mmol/L'),
        ex('Gram e cultura', 'Sem bactérias · cultura negativa em 48 horas', '—'),
        ex('PCR para herpes-vírus simples 1 e 2', 'Não detectado', 'não detectado'),
    ]),

    estudo('rm', 'Ressonância de encéfalo',
           'Feita no sexto dia, sob sedação. Sequência FLAIR axial na altura dos '
           'lobos temporais e do mesencéfalo, onde as infecções virais do cérebro '
           'costumam deixar marca.',
           IMG / 'rm_flair.jpg',
           'Ressonância · recortada na cabeça.',
           credito_meta(IMG / 'rm_flair.jpg.json'),
        [
         ((660, 790), (870, 640), '**Lobo temporal medial** esquerdo com sinal normal, '
          'sem o hipersinal que o herpes costuma deixar.', 12),
         ((328, 727), (170, 560), '**Corno temporal** do ventrículo lateral direito, de '
          'tamanho normal.', -12),
         ((497, 915), (280, 1100), '**Mesencéfalo** de sinal normal.', 12),
        ],
        ['Encéfalo sem alterações de sinal em FLAIR, T2 e difusão, sem realce '
         'anormal pelo contraste. Lobos temporais mediais, núcleos da base e '
         'tronco normais.',
         'Sem lesão estrutural identificada nas sequências descritas.']),

    estudo('eeg', 'Eletroencefalograma',
           'Registro de 40 minutos no sexto dia, com Camila sob sedação leve, '
           'durante os movimentos da boca. Repare no ritmo de base e no que se '
           'sobrepõe a ele.',
           IMG / 'eeg_uti.jpg',
           'Traçado · quadros e ampliação do original.',
           credito_meta(IMG / 'eeg_uti.jpg.json'),
        [
         ((309, 16), (200, 120), '**Onda delta** lenta e ampla em Fp1: o ritmo de base '
          'está entre 1 e 3 ciclos por segundo, onde deveria haver alfa.', 12),
         ((523, 533), (380, 600), 'O mesmo ritmo lento nas **derivações occipitais**: a '
          'lentificação é difusa, não focal.', -12),
         ((889, 436), (720, 600), '**Atividade rápida** sobreposta a cada onda delta, '
          'como uma escova sobre a onda lenta (ampliada no quadro).', 12),
        ],
        ['Atividade delta rítmica e generalizada, de 1 a 3 Hz, com atividade beta '
         'sobreposta e sincronizada a cada onda delta. Sem descargas '
         'epileptiformes durante os movimentos orofaciais.',
         'Não foi registrado correlato eletrográfico ictal durante os movimentos orofaciais observados.']),

    Q('p3', 3,
      'Quais dois exames você prioriza após a nova avaliação neurológica?', [
      ('IgG anti-GluN1 no líquor', True),
      ('Ultrassonografia da pelve', True),
      ('PCR para enterovírus no líquor', False),
      ('Pesquisa de micobactérias no líquor', False),
      ('Sorologia para arboviroses no soro', False),
     ], [
      ('Limites de imagem e EEG', 'TC e RM normais não excluem encefalite ou disfunção sináptica. A falta de correlato ictal durante a mastigação favorece discinesia naquele episódio, sem excluir outras crises.'),
      ('Hipóteses prioritárias', 'A pesquisa de IgG anti-GluN1 no líquor já enviada tem prioridade neste conjunto de manifestações, com interpretação conjunta ao soro. A imagem da pelve procura tumor associado e revisita o cisto antigo antes de haver confirmação sorológica.'),
      ('Infecção em paralelo', 'A segunda PCR para HSV foi colhida no quinto dia, após a primeira negativa. Aciclovir permanece até reavaliação do resultado e das hipóteses. Outros agentes dependem de exposição e conjunto de manifestações; a investigação autoimune não substitui essa avaliação.'),
     ]),

    pg('hipovent', 'Sétimo dia',
       'Mesmo após reduzir os sedativos e sem novas crises no vídeo-EEG, a respiração fica lenta e superficial, com pausas: pCO₂ de 62 mmHg e pH de 7,26. Camila é intubada. Não há alteração pulmonar ou metabólica que explique o padrão; hipoventilação central ganha peso, sem ignorar contribuição farmacológica.',
       'Os movimentos da boca persistem e a frequência cardíaca oscila entre 48 e 140. A queda da CK não acompanhou a evolução neurológica. A equipe explica à mãe que agora é necessário sustentar ventilação e tratar uma doença cerebral provável, ainda sem confirmação da causa.'),

    pg('probabilidade', 'Antes do anticorpo',
       'Há alteração comportamental e cognitiva, redução da fala, crise, discinesias, redução da consciência e disfunção autonômica/respiratória, além de líquor e EEG alterados. A segunda PCR para HSV é negativa. Após exclusão razoável das infecções prioritárias, o conjunto preenche critérios clínicos de provável encefalite anti-NMDAR; o anticorpo ainda não retornou.',
       'O ultrassom pélvico solicitado foi tecnicamente limitado e não caracterizou o ovário direito. A equipe discute tratamento e complementação da imagem durante o suporte intensivo.'),

    pg('iniciar_imuno', 'Tratamento da síndrome provável',
       'Após revisar as infecções prioritárias, inicia-se metilprednisolona em pulso. Não se exige esperar anticorpos para tratar. Pela gravidade, a equipe indica associar outra modalidade de primeira linha e discute acesso vascular, estabilidade e riscos.'),

    bifurcacao('b2', 'Decisão', 'Completar a primeira linha',
      'Camila está intubada, sem trombose conhecida ou contraindicação maior a uma das modalidades. Que tratamento associar ao corticoide?', [
      caminho('Imunoglobulina intravenosa', 'primeira_linha',
              'É opção de primeira linha; avaliar risco trombótico, função renal e tolerância à infusão.'),
      caminho('Plasmaférese', 'plasmaferese',
              'Também é opção de primeira linha; exige acesso e ponderação das oscilações hemodinâmicas. Não há comparação robusta que imponha uma única escolha para toda paciente.'),
    ]),

    pg('primeira_linha', 'Primeira linha com imunoglobulina',
       'A equipe inicia um curso de cinco dias de imunoglobulina, com vigilância de infusão, função renal e trombose. Nas primeiras horas ainda não há recuperação da fala ou da ventilação; isso não basta para declarar falha. A imagem da pelve continua em paralelo.',
       segue='pelve'),

    pg('plasmaferese', 'Primeira linha com troca plasmática',
       'A equipe usa acesso apropriado e programa as sessões com monitorização hemodinâmica. As pausas para realizar o procedimento exigem coordenar sedação e exame neurológico. Após a primeira sessão, Camila segue sem contato consistente; a resposta não é julgada por horas.',
       segue='pelve'),

    estudo('pelve', 'Tomografia da pelve com contraste',
           'Feita na UTI, com Camila intubada, para complementar a ultrassonografia inconclusiva. Corte axial na altura das asas do ilíaco. Compare a '
           'densidade do conteúdo da lesão com a da gordura do subcutâneo.',
           IMG / 'tc_pelve.jpg',
           'Tomografia.',
           credito_meta(IMG / 'tc_pelve.jpg.json'),
        [
         ((544, 209), (700, 90), '**Conteúdo com densidade de gordura**, igual à do '
          'subcutâneo, ocupando quase toda a lesão.', 12),
         ((394, 274), (230, 170), '**Calcificação** grosseira na borda da lesão.', -12),
         ((530, 360), (690, 440), '**Nódulo heterogêneo** de partes moles na parte '
          'pendente, projetando-se para dentro do cisto.', 12),
        ],
        ['Massa cística pélvica de 7 cm, de origem anexial, com conteúdo de '
         'gordura, calcificação e nódulo de partes moles na parede: teratoma '
         'maduro (cisto dermoide). Na cirurgia, a lesão vinha do ovário direito.',
         'Gordura dentro de um cisto de ovário é praticamente diagnóstica de '
         'teratoma maduro. A descrição antiga não permite assegurar que fosse a mesma lesão nem medir sua evolução com precisão.']),

    estudo('peca', 'A peça',
           'No oitavo dia, após avaliação da estabilidade e discussão com a família, a ginecologia retira a lesão por '
           'videolaparoscopia, com ooforectomia direita, porque o cisto ocupava '
           'quase todo o ovário. Lâmina da parede do cisto em hematoxilina-eosina, '
           'pequeno aumento. Procure tecidos que não deveriam estar num ovário.',
           IMG / 'peca.jpg',
           'Lâmina.',
           credito_meta(IMG / 'peca.jpg.json'),
        [
         ((464, 187), (560, 70), '**Epitélio escamoso** queratinizado, como a pele, '
          'revestindo a parede do cisto.', 12),
         ((72, 205), (170, 80), '**Anexo cutâneo** cortado de través, folículo e '
          'glândula, logo abaixo do epitélio.', -12),
         ((230, 370), (330, 560), '**Tecido glial** maduro, róseo e fibrilar, com '
          'núcleos esparsos: tecido nervoso dentro do tumor.', 12),
        ],
        ['Teratoma cístico maduro do ovário: pele com anexos, derme e tecido glial '
         'maduro na parede. Sem componente imaturo. Margens livres.',
         'O tecido neural de teratomas pode expressar o receptor NMDA e participar da '
         'resposta imune.']),

    pg('virada', 'Nono dia',
       'O laboratório de referência informa IgG contra a subunidade GluN1 do receptor NMDA detectada no líquor por ensaio em células, título 1:32; no soro, 1:100. A segunda PCR para HSV, colhida no quinto dia, também foi negativa. Após revisão das alternativas infecciosas, o aciclovir é suspenso.',
       'O tratamento da síndrome provável e a retirada da lesão ovariana já ocorreram. O resultado confirma a causa; não foi uma autorização para só agora começar a assistência.'),

    pg('diagnostico', 'O diagnóstico',
       'É **encefalite contra o receptor NMDA** (anti-NMDAR): síndrome compatível, IgG anti-GluN1 no líquor e exclusão razoável de alternativas. O teratoma maduro com tecido neural é uma associação relevante, na integração da clínica, imagem e anatomopatológico.',
       'Os anticorpos alteram a disponibilidade de receptores sinápticos; a disfunção pode ser importante mesmo sem lesão na RM. Isso ajuda a compreender a possibilidade de recuperação, sem garantir reversibilidade completa. Pródromo, psicose, redução da fala, crises, discinesias e disautonomia podem se sobrepor; não são fases obrigatórias.',
       'O padrão delta brush extremo no EEG apoia o conjunto de manifestações, mas não é isoladamente diagnóstico nem prova que todo movimento seja crise. A reação após haloperidol permanece como provável intolerância neuroléptica sobreposta à encefalite.'),

    Q('p4', 4,
      'Quais duas conclusões melhor integram os resultados disponíveis?', [
      ('O resultado no líquor tem maior peso diagnóstico que o título sérico isolado', True),
      ('A RM normal é compatível com disfunção neuronal mediada por anticorpos', True),
      ('A ausência de descarga durante a mastigação exclui as crises já observadas', False),
      ('A descrição antiga do cisto estabelecia a natureza da lesão', False),
      ('O título no soro mede diretamente a gravidade e define a alta', False),
     ], [
      ('Peso dos achados', 'IgG anti-GluN1 no **líquor**, com síndrome compatível e exclusão razoável de alternativas, sustenta o diagnóstico definido. A RM pode permanecer normal porque disfunção sináptica não exige lesão estrutural visível.'),
      ('Limites', 'O EEG durante a mastigação favorece discinesia naquele episódio, sem negar a crise tônico-clônica prévia. A descrição do cisto antigo não definia sua natureza; a imagem atual e o tecido é que caracterizaram a lesão. Títulos séricos isolados não medem a evolução clínica de modo confiável.'),
     ]),

    Q('p5', 5,
      'Quais dois registros você prioriza para avaliar a resposta?', [
      ('Exame neurológico seriado sob sedação comparável', True),
      ('Vídeo-EEG durante eventos motores duvidosos', True),
      ('Título sérico de anti-GluN1', False),
      ('Contagem de movimentos sem registrar a sedação', False),
      ('Ressonância de encéfalo de controle', False),
     ], [
      ('Resposta observável', 'Contato, comandos, linguagem e autonomia respiratória precisam ser comparados com exposição conhecida a sedativos. Vídeo-EEG ajuda quando surge evento diferente ou há dúvida entre discinesia e crise; não implica monitorização indefinida de toda discinesia.'),
      ('Limites', 'Anticorpos podem persistir e a RM inicial já era normal. Menos movimentos sob mais sedação não demonstra, isoladamente, resposta imunológica.'),
     ]),

    pg('semana2', 'Reavaliação após a primeira linha',
       'Cerca de três semanas após completar a primeira linha e retirar o tumor, '
       'Camila segue intubada. As discinesias diminuíram sem sumir, ela não abre '
       'os olhos ao chamado e a pressão ainda oscila. O novo eletroencefalograma '
       'mantém a lentificação delta.'),

    bifurcacao('b3', 'Decisão', 'Resposta ainda insuficiente',
      'Após cerca de três semanas da primeira linha, Camila segue dependente de ventilação e sem contato consistente, sob menor sedação. Qual tratamento acrescentar?', [
      caminho('Rituximabe', 'rituximabe',
              'Persistência de doença grave após primeira linha adequada justifica segunda linha, após avaliação de segurança infecciosa.'),
      caminho('Repetição da modalidade de primeira linha', 'mais_igiv',
              'Pode ser individualizado, mas repetir primeira linha não deve postergar indefinidamente a escalada num quadro grave sem resposta relevante.'),
    ]),

    pg('mais_igiv', 'Reavaliação da resposta',
       'A proposta de repetir a primeira linha é discutida com a neuroimunologia. Discinesias menores sem recuperação de contato ou ventilação não bastam para declarar resposta. A equipe escolhe segunda linha após rastreio infeccioso e planejamento de prevenção de infecção.',
       segue='rituximabe'),

    pg('rituximabe', 'Semanas seguintes',
       'Após rastreio de hepatite B e outras infecções relevantes, usa-se rituximabe segundo protocolo especializado. Na sexta semana Camila '
       'começa a acompanhar com os olhos; na oitava é extubada e as discinesias '
       'param. Na décima fala frases curtas e não lembra de nada desde a UPA.',
       'A agitação da fase de despertar é tratada com benzodiazepínico, sem '
       'antipsicótico.'),

    Q('p6', 6,
      'Na 12.ª semana, como você interpreta a evolução?', [
      ('Recuperação incompleta em curso, a acompanhar com avaliação cognitiva e funcional seriada', True),
      ('Resposta insuficiente à segunda linha, a reavaliar para outro ciclo de imunoterapia', False),
      ('Recorrência da doença após a resposta, a investigar com nova punção lombar', False),
      ('Déficit predominantemente pós-crítico, a manejar intensificando o tratamento anticrise', False),
      ('Sequela cognitiva estabilizada, a usar como referência definitiva para o retorno ao curso', False),
     ], [
      ('Trajetória atual', 'Ela voltou a acompanhar com os olhos, foi extubada e passou a falar frases. Essa melhora progressiva favorece recuperação ainda em curso; o déficit cognitivo pode melhorar durante meses e exige reabilitação e avaliação seriada.'),
      ('O que mudaria a leitura', 'Falha terapêutica pede considerar estagnação ou agravamento relevantes, e recaída pressupõe nova piora após melhora. Não foram descritas novas crises que sustentem déficit pós-crítico predominante. A trajetória recente também não permite declarar que a sequela estabilizou.'),
     ]),

    pg('alta', 'Preparando a alta',
       'Na 14.ª semana Camila caminha sozinha e conversa, mas perde a sequência de tarefas e cansa depois de meia hora de leitura. Não há nova piora que indique recaída. A equipe combina reabilitação e retorno gradual aos estudos.',
       segue='f1'),

    fim('f1', 'Alta e recuperação em curso',
        'Camila sai na 15.ª semana com reabilitação cognitiva e seguimento neurológico e ginecológico. Retoma parte do curso seis meses depois; aos doze meses ainda precisa de pausas para estudar. O ovário remanescente não apresenta lesão na avaliação atual.',
        'A melhora levou meses apesar de tratamento indicado e retirada do tumor. O plano de vigilância tumoral é individualizado; piora nova exige distinguir recaída de crise, infecção, efeito medicamentoso ou flutuação da recuperação.', 'melhor'),

    pagina('retrospectiva', 'Pontos de ensino', '',
        pontos(
            'Num primeiro episódio psicótico, desorientação, atenção flutuante, '
            'crises, movimentos anormais ou pródromo febril pedem avaliação '
            'neurológica antes de fechar o diagnóstico psiquiátrico; tomografia e '
            'exames de sangue normais não encerram a busca.',
            'Rigidez, febre, disautonomia e CK alta depois de um antipsicótico '
            'pedem a suspensão do agente. Numa mulher jovem com psicose recente, '
            'a reação grave deve lembrar a encefalite anti-NMDAR.',
            'Discinesias orofaciais contínuas, crises e hipoventilação central '
            'depois de uma fase psiquiátrica são a sequência típica da doença; '
            'líquor com pleocitose leve e ressonância normal não a afastam.',
            'O anticorpo IgG anti-GluN1 no líquor, por ensaio em células, define '
            'o diagnóstico. Com quatro grupos clínicos e líquor ou '
            'eletroencefalograma alterados, o tratamento começa antes dele.',
            'Toda mulher com a doença precisa de imagem da pelve à procura de '
            'teratoma de ovário; retirar o tumor cedo melhora o desfecho e reduz '
            'recaídas.',
            'Primeira linha: metilprednisolona em pulso com imunoglobulina ou '
            'plasmaférese. Persistência de doença grave após cerca de 2–4 semanas justifica discutir segunda linha, frequentemente rituximabe; tempo e escolha são individualizados.'),
        so_kicker=True),

    pg('referencias', 'Fontes e limites',
       'Revisão clínica em 23/10/2026: consenso brasileiro 2024 e Abboud et al. 2021 (recomendações de prática; evidência limitada para comparar modalidades). Fontes: https://pubmed.ncbi.nlm.nih.gov/39089672/ e https://pubmed.ncbi.nlm.nih.gov/33649022/. Paciente, valores e percursos são ficcionais. A abertura mostra uma '
       'ilustração original da paciente ficcional, gerada com OpenAI imagegen '
       'para este projeto em 24/10/2026; não é fotografia clínica.',
       'Graus e cols. A clinical approach to diagnosis of autoimmune '
       'encephalitis, Lancet Neurol 2016. Titulaer e cols. Treatment and '
       'prognostic factors for long-term outcome in patients with anti-NMDA '
       'receptor encephalitis, Lancet Neurol 2013. Dutra e cols. Brazilian '
       'consensus recommendations on the diagnosis and treatment of autoimmune '
       'encephalitis in the adult and pediatric populations, Arq '
       'Neuropsiquiatr 2024. Dalmau e cols. An update on anti-NMDA receptor '
       'encephalitis for neurologists and psychiatrists, Lancet Neurol 2019. '
       'Lejuste e cols. Neuroleptic intolerance in patients with anti-NMDAR '
       'encephalitis, Neurol Neuroimmunol Neuroinflamm 2016. Schmitt e cols. '
       'Extreme delta brush, Neurology 2012. Venkatesan e cols. Case definitions '
       'of encephalitis (International Encephalitis Consortium), Clin Infect '
       'Dis 2013. Gurrera e cols. International consensus on neuroleptic '
       'malignant syndrome diagnostic criteria, J Clin Psychiatry 2011.',
       'Imagens, com setas adicionadas: tomografia de crânio, Mikael Häggström, CC0, recortada (commons.wikimedia.org/wiki/File:CT_of_a_normal_brain,_axial_21.png); ressonância FLAIR, 511KeV, CC BY-SA 4.0, recortada (commons.wikimedia.org/wiki/File:Mri_Brain_Flair_Axial_(7).jpg); eletroencefalograma, Mizoguchi, Hara, Hirose e Nakajima, CC BY 4.0 (commons.wikimedia.org/wiki/File:Extreme_delta_brush_in_anti-NMDAr_encephalitis.png); tomografia da pelve, Hellerhoff, CC BY-SA 4.0 (commons.wikimedia.org/wiki/File:Reifes_zystisches_Teratom_des_Ovars_Dermoidzyste_46W_-_CT_axial_KM_-_001.jpg); lâmina, Librepath, CC BY-SA 3.0 (commons.wikimedia.org/wiki/File:Mature_ovarian_teratoma_with_mature_neural_elements_--_low_mag.jpg). Todas pelo Wikimedia Commons.'),
]

REVISAO = []

# Revisão de questões: fontes clínicas consultadas em 22/10/2026.
# https://pmc.ncbi.nlm.nih.gov/articles/PMC5066574/
# https://pubmed.ncbi.nlm.nih.gov/23290630/
# https://www.idsociety.org/practice-guideline/encephalitis
# https://pubmed.ncbi.nlm.nih.gov/39089672/
# Redação: https://www.nbme.org/sites/default/files/2021-02/NBME_Item%20Writing%20Guide_R_6.pdf

# Revisão de evolução 23/10/2026: Dutra et al. 2024, PMID 39089672;
# Abboud et al. 2021, PMID 33649022; Graus 2016 (critérios diagnósticos).

# Catatonia e prova monitorizada: Rogers et al. 2023, PMID 37039129.
# https://pubmed.ncbi.nlm.nih.gov/37039129/

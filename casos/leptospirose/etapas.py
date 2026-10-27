"""Caso ficcional reformulado em 23/10/2026: evolução clínica antes da resolução.

Imagens, créditos e marcações preservados. Fontes e limites no fechamento.
"""
from pathlib import Path

from motor.estudo_imagem import estudo
from motor.etapas import (alt, bifurcacao, caminho, capa, desfecho, op, p,
                          pagina, painel, par, pareamento, pergunta, pontos,
                          topicos, vitais, lamina)

TITULO = 'O sexto dia'
RODAPE = 'Paciente ficcional · evoluções simuladas para ensino'
COR = '#0891b2'
IMG = Path(__file__).parent / 'img'
BANCO = []
MOLDE = 'nejm'
CREDITO_RX = 'Samir · Wikimedia Commons · CC BY-SA 3.0'
CREDITO_RX_ADM = 'Mikael Häggström · Wikimedia Commons · CC0'


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
    capa(TITULO, fundo='cena.png', kicker='Caso interativo',
         selo='Paciente ficcional · procedência e créditos na última tela'),

    pg('historia', 'Apresentação',
       'Um homem de 38 anos, morador de Fortaleza, chega à emergência trazido '
       'pelo irmão no sexto dia de febre, com calafrios, dor de cabeça e dor no '
       'corpo. Há dois dias a tosse, até então seca, passou a ter raias de '
       'sangue, e desde ontem ele fica sem ar para ir ao banheiro.',
       'No segundo dia foi a uma unidade de pronto atendimento, onde '
       'disseram que era virose: soro oral, paracetamol e repouso. A febre '
       'cedeu no quarto dia e voltou. O irmão acha que ele está com os olhos '
       'amarelados desde ontem e que urinou pouco hoje.',
       'Nega dor torácica, dor abdominal forte, diarreia, manchas na pele, '
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
           vitais(('Temperatura', '38,4 °C', True),
                  ('Pressão arterial', '94/56', True),
                  ('Frequência cardíaca', '116', True),
                  ('Frequência respiratória', '30', True),
                  ('SpO₂ em ar ambiente', '90%', True)),
           topicos(('Estado geral', 'Prostrado, sonolento, orientado no tempo e no '
                    'espaço. Escleras ictéricas.'),
                   ('Respiratório', 'Crepitações nas bases dos dois pulmões.'),
                   ('Coração', 'Rítmico, taquicárdico, sem sopros.'),
                   ('Abdome', 'Fígado a 2 cm do rebordo, doloroso. Baço não palpável. '
                    'Sem sinal de Murphy.'),
                   ('Pele e membros', 'Algumas petéquias nas pernas. Sem edema.'),
                   ('Neurológico', 'Sem rigidez de nuca, sem déficit focal.')),
           so_kicker=True),

    painel('res1', 'Primeiros exames', 'Sangue', [
        ex('Hemoglobina / hematócrito', '12,8 g/dL / 38%', 'Hb 13,5–17,5 g/dL', True),
        ex('Leucócitos', '15.600/mm³ · neutrófilos 90%', '4.000–11.000/mm³', True),
        ex('Plaquetas', '88.000/mm³ {{(145.000 na UPA)}}', '150.000–450.000/mm³', True),
        ex('Ureia / creatinina', '148 / 2,6 mg/dL {{(creatinina 1,0 na UPA)}}', 'até 42 / 1,3 mg/dL', True),
        ex('Sódio / potássio / cloro', '133 / 3,1 / 100 mmol/L', 'Na 135–145 · K 3,5–5,0 · Cl 98–107', True),
        ex('Glicemia capilar na chegada', '102 mg/dL', 'sem hipoglicemia'),
    ], introducao='Duas hemoculturas foram colhidas antes de qualquer antibiótico, e '
                  'uma alíquota de sangue da admissão ficou guardada no laboratório.'),

    painel('res1b', 'Primeiros exames', 'Gasometria e urina', [
        ex('Gasometria arterial em ar ambiente', 'pH 7,33 · pCO₂ 31 · HCO₃ 16 · pO₂ 58 mmHg · lactato 3,1 mmol/L', '—', True),
        ex('Urina', 'Densidade 1.012 · sangue ++ · proteína + · 3 a 5 hemácias e cilindros granulosos por campo · sem cilindros hemáticos', '—', True),
    ], introducao='Gasometria e lactato são precoces pela hipoxemia e hipotensão; a urina integra a avaliação da oligúria e da alteração renal.'),

    pg('suporte_inicial', 'Primeiros minutos',
 'Enquanto os exames chegam, ele recebe oxigênio, monitorização e cristaloide em alíquotas pequenas, com reavaliação de perfusão e ausculta. Após 500 mL, a pressão passa a 108/64, sem piora das crepitações; saturação 94% com oxigênio. Ceftriaxona 2 g IV a cada 24 horas e azitromicina são iniciadas após culturas pela suspeita inicial de infecção pulmonar grave.',
 'A internação em terapia intensiva é organizada pela disfunção respiratória e renal. Não se aguarda uma pergunta nem confirmação da causa para oferecer suporte e antibiótico. O volume adicional será individualizado; melhora da pressão não autoriza bolus repetidos independentemente do pulmão.',
 'Após a melhora da pressão, a icterícia, a pouca urina e a dor muscular continuam. A equipe acrescenta bilirrubinas e enzimas hepáticas pela icterícia, CK pela mialgia com sangue na fita e poucas hemácias, e potássio urinário pela alteração renal com potássio baixo. A complementação usa amostras precoces e não retarda o suporte.'),

    painel('investigacao_dirigida', 'Exames dirigidos', 'Icterícia, mialgia e alteração renal', [
        ex('Bilirrubina total / direta', '6,4 / 5,3 mg/dL', 'até 1,2 / 0,3 mg/dL', True),
        ex('AST / ALT', '96 / 70 U/L', 'até 40 / 41 U/L', True),
        ex('Fosfatase alcalina / GGT', '190 / 160 U/L', 'até 129 / 60 U/L', True),
        ex('Creatinoquinase', '2.380 U/L', 'até 190 U/L', True),
        ex('Potássio urinário', '38 mmol/L', 'interpretar com o potássio sanguíneo, a diurese e a reposição', True),
    ], introducao='Resultados da investigação orientada pelos achados iniciais, ainda nas primeiras horas da admissão.'),

    estudo('rx_adm', 'Radiografia de tórax na admissão',
           'Radiografia feita na chegada. Descreva a localização e o tipo da '
           'opacidade antes de ler os achados.',
           IMG / 'rx_consolidacao.jpg',
           'Radiografia.',
           CREDITO_RX_ADM,
        [
         ((190, 478), (70, 330), '**Consolidação alveolar** no terço inferior do pulmão direito.', 12),
         ((47, 700), (175, 745), '**Seio costofrênico** direito livre: sem derrame.', -12),
         ((690, 290), (900, 200), '**Pulmão esquerdo** sem opacidades.', 12),
        ],
        ['Consolidação alveolar em base direita, sem derrame pleural e sem '
         'aumento da área cardíaca.',
         'A opacidade está localizada no pulmão direito nesta imagem inicial.']),

    estudo('us_adm', 'Ultrassonografia de abdome',
           'Ultrassonografia feita na chegada, pela icterícia e pela dor no '
           'hipocôndrio direito.',
           IMG / 'us_vias_biliares.jpg',
           'Ultrassonografia.',
           credito_meta(IMG / 'us_vias_biliares.jpg.json'),
        [
         ((447, 150), (330, 60), '**Parênquima hepático** de ecotextura homogênea.', 12),
         ((600, 215), (790, 110), '**Vesícula** de parede fina, sem cálculos nem lama.', -12),
        ],
        ['Fígado discretamente aumentado e homogêneo. Vesícula normal, vias '
         'biliares intra e extra-hepáticas sem dilatação. Rins de tamanho '
         'normal, sem hidronefrose.',
         'Não se observam cálculos ou dilatação das vias biliares e dos sistemas coletores.']),

    pagina('figado', 'Discussão', 'Icterícia no quadro febril',
 p('Bilirrubina predominantemente direta, com elevação relativamente modesta de transaminases, favorece comprometimento colestático associado à doença sistêmica. Ultrassom sem dilatação reduz o suporte a obstrução evidente, mas não exclui toda obstrução inicial.'),
 p('Sepse, infecção sistêmica e lesão por fármacos podem produzir esse padrão. Transaminases abaixo de três vezes o limite não excluem absolutamente hepatite viral ou tóxica; o curso, exposições e exames dirigidos determinam a investigação. Não se deduz necrose ou sua ausência apenas desses valores.')),

    Q('p3', 1,
      'Qual mecanismo melhor explica a alteração renal?', [
      ('Lesão tubular com perda de eletrólitos, possivelmente somada à hipoperfusão', True),
      ('Hipoperfusão isolada com túbulos preservados', False),
      ('Nefropatia por pigmentos como explicação suficiente de todos os achados', False),
      ('Glomerulonefrite como mecanismo predominante', False),
      ('Obstrução urinária com diurese paradoxal', False),
    ], [('Integração', 'Cilindros granulosos e urina pouco concentrada favorecem lesão tubular. A hipotensão pode contribuir, mas não explica sozinha o padrão urinário. K urinário 38 durante hipocalemia sugere perda renal inadequada, interpretada com diurese e reposição.'), ('Concorrentes', 'CK 2.380 e sangue na fita com poucas hemácias sustentam contribuição de pigmento muscular, sem provar que seja o mecanismo dominante. Pouca proteína e ausência de cilindros hemáticos enfraquecem glomerulonefrite; ultrassom sem dilatação reduz obstrução.')]),

    pg('exposicao_precoce', 'A história é ampliada na emergência',
 'Após a melhora da pressão, o paciente consegue detalhar o trabalho: é agente de limpeza urbana. Doze dias antes da febre, entrou num canal alagado com uma bota furada, após chuvas fortes. O irmão confirma a presença de ratos no depósito da equipe.',
 'Ele mantém tosse, dor muscular e pouca urina. As hemoculturas ainda estão em processamento. A equipe mantém o suporte e a ceftriaxona com azitromicina enquanto amplia a investigação.'),

    Q('p_causas', 2, 'Quais três diagnósticos você prioriza nesta reavaliação?',
 [('Leptospirose', True), ('Pneumonia bacteriana com sepse', True), ('Dengue com comprometimento de órgãos', True), ('Hepatite A aguda', False), ('Colangite aguda', False), ('Pielonefrite aguda', False)],
 [('Três hipóteses em paralelo', 'Pneumonia permanece pelo início respiratório, pela consolidação e pela neutrofilia. Leptospirose entra pela exposição e pela combinação de alterações renais e hepáticas. Dengue também pode comprometer vários órgãos. A exposição não confirma a causa, e a investigação viral não deve atrasar o antibiótico.'), ('Como comparar as demais', 'Hepatite A explicaria febre e icterícia, mas integra pior a lesão tubular, as plaquetas e o pulmão com transaminases apenas moderadamente elevadas. Não há achado obstrutivo no ultrassom que favoreça colangite. A urina não mostra piúria ou bacteriúria que sustentem pielonefrite. Esses dados reduzem a prioridade, sem tornar cada hipótese impossível.')]),

    Q('p5', 3, 'Entre estes exames, quais dois você acrescenta primeiro à investigação?',
 [('PCR para Leptospira no sangue da admissão', True), ('Antígeno NS1 para dengue', True), ('IgM para hepatite A', False), ('ANCA', False), ('Anticorpo anti-membrana basal glomerular', False), ('Complemento C3', False)],
 [('Investigar causas concorrentes', 'A amostra sanguínea do sexto dia, colhida antes do antibiótico, permite pesquisar DNA de Leptospira. O NS1 investiga dengue na primeira semana e deve ser interpretado com IgM e tempo de doença. Nenhum desses pedidos equivale a confirmar sua hipótese. As hemoculturas já colhidas continuam investigando infecção bacteriana.'), ('O que mudaria a prioridade', 'IgM para hepatite A ganha peso se a evolução sustentar hepatite. ANCA, anti-MBG e C3 podem ser úteis se surgirem evidências de lesão glomerular ou sangramento alveolar. Até aqui, o padrão urinário é tubular e há uma consolidação focal; essas possibilidades serão revistas conforme o quadro mudar.'), ('Limites e acesso', 'NS1 ou sorologia inicial negativos não encerram a investigação de dengue. A equipe complementa a coleta com IgM para dengue e leptospirose e programa nova amostra se necessário. PCR depende da rede de referência; sua indisponibilidade não deve atrasar suporte, antibiótico ou acompanhamento sorológico.')]),

    pg('coletas', 'Coletas e prioridades',
 'O laboratório encaminha o sangue da admissão para PCR de Leptospira e realiza NS1 para dengue, com sorologias IgM complementares. As hemoculturas seguem em processamento. Não há resultado específico disponível neste momento; a função hepática, o hemograma e o coagulograma serão acompanhados.',
 'Na observação, a pressão permanece melhor e ele consegue conversar. Ainda necessita de oxigênio e tem pouca urina. A equipe mantém a reavaliação de perfusão, diurese e respiração.'),

    pg('reacao_inicial', 'Duas horas após o antibiótico',
 'Ele apresenta calafrios, temperatura de 40 °C e pressão de 84/50. Não há urticária, sibilância ou edema de língua. A equipe reavalia perfusão, sangramento, reação ao medicamento e progressão da infecção; administra suporte titulado e mantém vigilância intensiva.',
 'Em quatro horas, a pressão volta a 106/62 e os calafrios cedem. A equipe registra a relação temporal com a medicação, mas mantém em avaliação infecção, sangramento e outras causas de hipotensão. O episódio não permite concluir que houve alergia, falha do esquema ou confirmação de uma causa infecciosa específica.'),

    pg('pulmao_muda', 'Seis horas de internação',
 'Apesar da melhora da pressão e de estar mais desperto, ele precisa de mais oxigênio para manter saturação de 92%. A tosse fica úmida e aparecem novos episódios de sangue vivo. No reexame, há hiperemia conjuntival sem secreção; ele relata que a dor muscular é mais intensa nas panturrilhas. A diurese permanece baixa; o balanço de volume não explica sozinho a mudança pulmonar.',
 'A equipe repete hemograma e radiografia e acompanha gasometria e lactato. Prepara suporte de via aérea caso a troca gasosa piore. A suspeita deixa de ser apenas uma consolidação focal: hemorragia, edema e dano alveolar por infecção precisam ser comparados.'),

    pg('hemorragia', 'Doze horas: o quadro torna-se bilateral',
 'A saturação cai a 83% mesmo com máscara com reservatório; frequência respiratória 36, uso de musculatura acessória e cerca de 150 mL de hemoptise nas últimas seis horas. Hemoglobina 9,6 g/dL, plaquetas 38.000/mm³, INR 1,4 e fibrinogênio 390 mg/dL. Bilirrubina total 17,8, creatinina 4,6 e potássio 3,0; o esfregaço não mostra esquizócitos.',
 'A gasometria mostra pH 7,30, pCO₂ 32 mmHg e HCO₃ 15 mmol/L; lactato 2,0 mmol/L. Diante da hipoxemia persistente e do sangramento, realiza-se intubação na UTI, sem esperar broncoscopia ou resultado dos testes para identificar a causa. A deterioração faz parte deste percurso ficcional de doença grave apesar do tratamento; não é consequência obrigatória de uma escolha.'),

    estudo('rx_hemorragia', 'Radiografia de tórax',
           'Radiografia após a mudança respiratória. Compare com a da admissão, que mostrava consolidação só na base direita.',
           IMG / 'rx_torax_alveolar.jpg',
           'Radiografia.',
           CREDITO_RX,
        [
         ((308, 427), (110, 345), '**Opacidades alveolares** no pulmão direito, em mancha e confluentes.', 12),
         ((704, 430), (912, 320), 'O mesmo padrão no **pulmão esquerdo**: a doença é bilateral.', -12),
         ((620, 160), (760, 60), '**Ápices relativamente poupados**: o predomínio é central e inferior.', 12),
        ],
        ['Opacidades alveolares bilaterais e confluentes, que '
         'passaram da base direita para os dois pulmões em poucas horas.',
         'Com hemoptise e queda da hemoglobina, há forte suspeita de hemorragia alveolar. A radiografia isolada não distingue sangue, edema e outras causas de preenchimento alveolar.']),

    Q('p4', 2,
      'Quais duas interpretações melhor explicam a piora respiratória?', [
      ('Lesão da barreira alveolocapilar pode somar-se à trombocitopenia', True),
      ('CIVD permanece possível, mas não demonstrada por estes dados', True),
      ('Consumo sistêmico de fatores é o mecanismo comprovado do sangramento', False),
      ('Microangiopatia trombótica é a explicação mais forte para rim e pulmão', False),
      ('A contagem plaquetária permite atribuir a hemorragia apenas à hemostasia primária', False),
    ], [('Limite da inferência', 'A gravidade pulmonar não deve ser atribuída apenas às plaquetas: lesão capilar pode coexistir. Fibrinogênio preservado, reagente de fase aguda, não exclui CIVD; faltam tendência do coagulograma e marcadores de fibrina para caracterizar consumo.'), ('Comparação', 'Sem esquizócitos nem demonstração de hemólise microangiopática, a microangiopatia perde força, sem ser impossibilidade. A hemorragia exige suporte e pode justificar plaquetas; INR 1,4 isolado não fundamenta plasma.')]),

    pg('suporte', 'Suporte e investigação do sangramento',
 'A ventilação usa volume corrente em torno de 6 mL/kg de peso predito e pressões ajustadas à mecânica e à oxigenação. Plaquetas são transfundidas diante do sangramento ativo e da contagem de 38.000; o controle é 61.000/mm³. Plasma não é indicado apenas pelo INR de 1,4.',
 'A hemoglobina de 9,6 não determina, isoladamente, transfusão de hemácias: a equipe acompanha perda, perfusão e tendência. São solicitados ANCA e anti-membrana basal glomerular pela síndrome pulmonar-renal, além de revisão do sedimento e marcadores de hemólise. A hipótese infecciosa permanece forte, mas não exclui capilarite por princípio.'),

    bifurcacao('b1', 'Decisão', 'O que acrescentar à investigação agora?',
 'Após intubação e estabilização, há dúvida sobre o mecanismo das opacidades. Qual avaliação você prioriza?', [
 caminho('Ecocardiografia à beira do leito', 'eco', 'Ajuda a avaliar função cardíaca e congestão sem transporte; não confirma nem exclui sozinha hemorragia alveolar.'),
 caminho('Broncoscopia com lavado sequencial', 'lavado', 'Pode documentar sangramento alveolar e colher agentes, se a oxigenação e o risco do procedimento permitirem. Não deve atrasar ventilação ou suporte.')]),

    pg('eco', 'Avaliação hemodinâmica',
 'Não há disfunção ventricular importante ou valvopatia que explique a mudança. Isso enfraquece edema cardiogênico como causa principal, sem excluir aumento de permeabilidade ou algum componente de volume. Sangue pelo tubo e queda de hemoglobina mantêm forte suspeita de hemorragia alveolar.',
 'A equipe decide não acrescentar broncoscopia de imediato, pois a informação disponível já orienta suporte e a hipoxemia aumenta o risco. A avaliação microbiológica inicial continua em andamento.', segue='rim'),

    pg('lavado', 'Depois de melhorar a oxigenação',
 'Com ventilação estabilizada e plaquetas acima de 50.000 após reposição, a equipe pondera benefício e risco e faz broncoscopia sem biópsia. Não há fonte endobrônquica focal; alíquotas sequenciais do lavado tornam-se progressivamente mais hemorrágicas, apoiando hemorragia alveolar.',
 'O material é encaminhado à microbiologia. A documentação do mecanismo não identifica a causa: infecção sistêmica e capilarite continuam na discussão até integrar os demais exames.', segue='rim'),

    pg('rim', 'O suporte renal acompanha a evolução',
 'A oligúria persiste, com balanço positivo crescente e dificuldade de controlar o volume num pulmão gravemente comprometido. A nefrologia inicia terapia renal substitutiva pela situação clínica, com modalidade e frequência ajustadas à estabilidade, depuração e balanço.',
 'Não se indica diálise apenas pela creatinina de 4,6 nem um calendário diário universal. O potássio baixo exige reposição e ajuste da solução utilizada; insuficiência renal grave não significa obrigatoriamente retenção de potássio.'),

    pg('virada', 'Integração da causa',
 'O laboratório de referência detecta DNA de Leptospira no sangue pré-antibiótico do sexto dia. IgM na mesma amostra é não reagente; isso não contradiz a PCR positiva nesta fase. A exposição e o conjunto clínico estabelecem leptospirose grave, com comprometimento hepatorrenal e hemorragia pulmonar.',
 'NS1 para dengue é negativo; a sorologia de convalescença ainda será conferida. ANCA e anti-membrana basal glomerular são negativos. A revisão urinária mantém poucas hemácias, sem cilindros hemáticos; não há aumento de bilirrubina indireta, queda de haptoglobina ou esquizócitos que sustentem hemólise microangiopática. Esses negativos não excluem toda doença autoimune, mas a confirmação infecciosa oferece explicação coerente.',
 'A ceftriaxona é mantida para completar sete dias, com revisão do esquema conforme evolução. A azitromicina é suspensa quando a investigação não sustenta coinfecção bacteriana comunitária. Não se atribui uma porcentagem individual de morte ao paciente nem se promete que antibiótico elimina o risco de progressão já instalada.'),

    pg('discussao_confirmacao', 'Discussão após os resultados',
       'O resultado molecular positivo sustenta a confirmação. A IgM inicial negativa é compatível com coleta precoce; a amostra posterior permitirá acompanhar a resposta de anticorpos. Para dengue, NS1 negativo não basta para excluir a doença, e a sorologia de convalescença continua em acompanhamento.',
       'A febre e a hipotensão nas primeiras horas após o antibiótico podem corresponder a reação de Jarisch–Herxheimer, uma resposta inflamatória descrita no tratamento de infecções por espiroquetas. É uma interpretação retrospectiva possível, não uma prova diagnóstica nem uma razão para deixar de investigar e tratar choque.'),

    Q('p6', 4,
      'Como você interpreta a evolução da função renal e dos eletrólitos?', [
      ('Redução da filtração coexistindo com perda tubular de potássio', True),
      ('Perda digestiva de potássio com conservação renal apropriada', False),
      ('Liberação muscular de potássio como mecanismo predominante', False),
      ('Redistribuição intracelular isolada, sem perda corporal relevante', False),
      ('Recuperação da filtração já estabelecida pela queda do potássio', False),
    ], [('Integração', 'K urinário de 38 durante hipocalemia sugere excreção renal inadequada, embora a concentração isolada dependa do fluxo urinário. Lesão tubular pode produzir perda de K mesmo com filtração muito reduzida; creatinina alta não garante hipercalemia.'), ('Comparação', 'Perda digestiva e redistribuição podem contribuir, mas isoladamente explicam pior a excreção urinária descrita. Miosite com lise celular tende a liberar K, não explica a hipocalemia persistente. Potássio baixo não documenta recuperação da filtração: pode persistir perda tubular durante lesão renal grave.'), ('Filtração e função tubular', 'Creatinina estima perda de filtração; potássio depende também do transporte tubular, da ingestão e de perdas fora do rim. Por isso, lesão renal importante pode coexistir com hipocalemia. A interpretação pede evolução seriada e contexto das reposições.')]),

    pg('recuperacao', 'Segunda semana: o rim muda de fase',
 'A hemoptise diminui no terceiro dia e o suporte respiratório é reduzido progressivamente. No nono dia, a diálise pode ser suspensa pela recuperação conjunta de diurese, controle de volume e depuração. A decisão não depende de um número isolado.',
 'A diurese chega a 4 L/dia. Apesar de reposição de potássio, ele cai a 2,9 mmol/L e o magnésio a 1,4 mg/dL. A icterícia ainda é evidente, embora a bilirrubina comece a cair. A amostra colhida no 14.º dia de doença, oitavo dia de internação, retorna com IgM reagente e microaglutinação 1:1.600; o resultado apoia a infecção, sem identificar com certeza o sorovar infectante.'),

    Q('p7', 6, 'Qual medida você acrescenta à prescrição neste momento?',
 [('Reposição de magnésio', True), ('Furosemida para acelerar recuperação tubular', False), ('Suspensão da reposição de potássio', False), ('Diálise diária apenas pela poliúria', False)],
 [('Mecanismo', 'Hipomagnesemia favorece perda renal de potássio e dificulta sua correção. Repor magnésio é uma medida adicional; o potássio continua sendo titulado com controles frequentes conforme a função renal se modifica.'),
 ('Segurança', 'Poliúria exige acompanhar balanço e eletrólitos, não diurético automático nem diálise por calendário. A necessidade anterior de diálise não prova retenção atual de potássio.')]),

    pg('resultados_pendentes', 'Conferência dos resultados',
 'As hemoculturas convencionais terminam sem crescimento e a sorologia de convalescença não sustenta dengue. No percurso com lavado, a pesquisa microbiológica não identifica coinfecção adicional. A negatividade desses exames não é a base da confirmação: o resultado positivo da PCR e a evolução sorológica já responderam à investigação dirigida.',
 'Corrigidos magnésio e potássio, a força melhora e a reposição é reduzida conforme a poliúria cede. A bilirrubina cai mais devagar que a febre. Antes da alta, ele caminha sem oxigênio, mas ainda se cansa ao tomar banho.'),

    Q('p8', 6,
      'Qual interpretação orienta a avaliação dos colegas e do irmão?', [
      ('Os colegas podem compartilhar a exposição ambiental; cuidar do paciente raramente transmite a doença', True),
      ('A negatividade das hemoculturas indica baixo risco ocupacional para os colegas', False),
      ('O título de microaglutinação define quais colegas devem receber antibiótico', False),
      ('O contato domiciliar deve ser tratado como exposição equivalente à água do canal', False),
      ('A recuperação clínica dispensa investigação do ambiente de trabalho', False),
    ], [('Exposição', 'Canal alagado, bota furada e roedores sustentam risco compartilhado no trabalho e justificam notificação e investigação ambiental. Hemocultura convencional negativa não mede esse risco.'), ('Contato e seguimento', 'Transmissão entre pessoas é rara; cuidar dele não equivale à exposição ao canal. Título sorológico do paciente não define profilaxia de terceiros. A recuperação não elimina a fonte ambiental, e o paciente ainda precisa acompanhar função renal e eletrólitos.')]),

    desfecho('alta', 'Alta e recuperação funcional',
 p('Recebe alta após a recuperação respiratória, sem diálise, com creatinina 1,6 mg/dL e bilirrubina em queda. Reavaliação clínica e de função renal e eletrólitos é combinada em uma a duas semanas, antes de discutir retorno ao trabalho pesado.'),
 p('Notificação e investigação da exposição ocupacional são organizadas. O irmão recebe orientação de que o cuidado habitual não equivale ao contato com água contaminada; os colegas precisam de avaliação da exposição e de sintomas, sem profilaxia automática baseada no título sorológico do paciente.'),
 p('Em seis semanas a capacidade de esforço melhora e o retorno é discutido com a saúde do trabalhador. É uma evolução ficcional favorável após doença grave, sem afirmar recuperação obrigatória nesse prazo.'),
 qualidade='melhor', porque='O suporte acompanhou as mudanças de pulmão e rim; o seguimento e a avaliação ocupacional continuam após a alta.', fecho='retrospectiva'),

    pagina('retrospectiva', 'Pontos de ensino', '', pontos(
 'Na febre com icterícia, rim e pulmão, uma consolidação focal não deve encerrar o diferencial.',
 'A pressão pode melhorar enquanto a troca gasosa piora. Mudanças clínicas exigem reavaliar suporte e mecanismo.',
 'A história de enchente deve ser perguntada cedo. Não é uma pista que se guarda até o paciente sangrar.',
 'PCR sanguínea na primeira semana e sorologia interpretada por fase são complementares. IgM inicial negativa não afasta infecção.',
 'Hemorragia alveolar requer suporte imediato; a imagem isolada não define causa. Plaquetas baixas podem coexistir com lesão capilar.',
 'Diálise e reposições dependem da evolução de volume, depuração e eletrólitos. Poliúria de recuperação não significa equilíbrio restaurado.'), so_kicker=True),

    pg('referencias', 'Fontes e limites',
       'Paciente, valores e percursos são ficcionais. A cena de abertura é uma ilustração autoral gerada por inteligência artificial para este caso; não é fotografia nem documentação clínica.',
       'Ministério da Saúde. Guia de Vigilância em Saúde, 6.ª edição revisada, 2024, volume 3, capítulo de leptospirose (critérios de confirmação e antibioticoterapia), e Leptospirose: diagnóstico e manejo clínico, 2014. Andrade e cols., Clin J Am Soc Nephrol 2007 (diálise diária). Spichler e cols., Am J Trop Med Hyg 2008 (preditores de mortalidade). Radiografias: Mikael Häggström, Wikimedia Commons, CC0 (admissão), e Samir, Wikimedia Commons, CC BY-SA 3.0 (segundo dia). Ultrassonografia: Ptrump16, Wikimedia Commons, CC BY-SA 4.0. Setas adicionadas.',
 'Revisão de 27/10/2026: <a href="https://www.cdc.gov/dengue/hcp/diagnosis-testing/">CDC, investigação de dengue por fase</a>;  <a href="https://www.cdc.gov/yellow-book/hcp/travel-associated-infections-diseases/leptospirosis.html">CDC Yellow Book 2026, capítulo atualizado em 2025</a>; <a href="https://www.gov.br/saude/pt-br/assuntos/saude-de-a-a-z/l/leptospirose/notas-tecnicas/nota-tecnica-no-16-2024-cgzv-dedt-svsa-ms">Ministério da Saúde, Nota Técnica 16/2024</a>; <a href="https://pubmed.ncbi.nlm.nih.gov/17699490/">Andrade et al., 2007</a>, estudo histórico pequeno de períodos assistenciais, não regra universal de diálise; <a href="https://www.nice.org.uk/guidance/ng148/chapter/Recommendations">NICE NG148, indicações clínicas de terapia renal substitutiva</a>. A hemorragia grave já integrava o caso; não foi criada como consequência de respostas erradas.')
]

REVISAO = []

for _n, _e in enumerate((e for e in ETAPAS if e['t'] == 'pergunta'), 1):
    _e['kicker'] = f'Pergunta {_n}'

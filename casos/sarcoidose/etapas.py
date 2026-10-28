"""Caso ficcional reformulado em 23/10/2026: evolução clínica antes da resolução.

Imagens, créditos e marcações preservados. Fontes e limites no fechamento.
"""
from pathlib import Path

from motor.estudo_imagem import estudo
from motor.etapas import (alt, bifurcacao, caminho, capa, desfecho, op, p,
                          pagina, painel, par, pareamento, pergunta, pontos,
                          topicos, vitais)

TITULO = 'Entre a sede e o fôlego'
RODAPE = 'Paciente ficcional · evoluções simuladas para ensino'
COR = '#0d9488'
IMG = Path(__file__).parent / 'img'
BANCO = []
MOLDE = 'nejm'
CENA = 'cena.png'


def credito_meta(meta):
    """Autor e licença, sem o link: o nome do arquivo no Commons diz o
    diagnóstico. A fonte completa fica na última tela."""
    import json
    m = json.loads(Path(meta).read_text())
    return m['autor'] + ' · Wikimedia Commons · ' + m['licenca'] + ' · setas adicionadas'


def _fonte(meta, rotulo):
    import json
    m = json.loads(Path(meta).read_text())
    return '<a href="' + m['fonte'] + '" target="_blank" rel="noopener">' + rotulo + '</a>'


def pg(k, titulo, *textos, segue='', conforme=None):
    return pagina(k, titulo, '', *(p(t) for t in textos), so_kicker=True,
                  segue=segue, conforme=conforme)


def disc(k, titulo, *textos, segue=''):
    """Página didática sem pergunta, no estilo das do NEJM."""
    return pagina(k, 'Discussão', titulo, *(p(t) for t in textos), segue=segue)


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
       'Rafael, 41 anos, analista administrativo em Fortaleza, é trazido pela '
       'esposa ao pronto-socorro com náuseas, intestino preso há cinco dias e '
       'dificuldade para se concentrar no trabalho. Há uma semana tem sede o '
       'tempo todo e acorda três vezes à noite para urinar.',
       'Há dois meses tem tosse seca, que vai e volta, e se cansa nas '
       'caminhadas do fim de semana. Perdeu 4 kg. Há três semanas, numa '
       'unidade de pronto atendimento, recebeu xarope e o diagnóstico de tosse '
       'pós-viral.',
       'Nega febre, suor noturno, escarro com sangue, dor no peito, vômitos '
       'repetidos, diarreia, cólica renal e caroços no pescoço.'),

    pagina('ficha', 'Ficha do paciente', '',
           topicos(('Antecedentes', 'Hipertenso há cinco anos. Nunca teve '
                    'cálculo renal. Nunca internou.'),
                   ('Medicações', 'Hidroclorotiazida 25 mg/dia. Colecalciferol '
                    '5.000 UI/dia há três meses, por conta própria, porque ouviu '
                    'que dava disposição. Colírio lubrificante há um mês, pelos '
                    'olhos vermelhos e ardendo no fim do dia, que atribui ao '
                    'computador. Não usa carbonato de cálcio, lítio nem antiácidos.'),
                   ('Hábitos', 'Não fuma. Uma ou duas cervejas no fim de semana. '
                    'Caminhava 5 km aos sábados até dois meses atrás.'),
                   ('Vida social', 'Casado, dois filhos. Trabalha em escritório '
                    'e nunca lidou com pedra, areia, fundição ou metais. Há cinco '
                    'meses ajudou a limpar um galinheiro abandonado no sítio do '
                    'sogro, no sertão central. Nunca saiu do Nordeste. Não conhece '
                    'contato com tuberculose.'),
                   ('Família', 'Pai com câncer de próstata aos 70 anos. Mãe com '
                    'hipotireoidismo. Um irmão saudável.')),
           so_kicker=True),

    pagina('exame', 'Exame físico', '',
           vitais(('Pressão arterial', '104/66', False),
                  ('Frequência cardíaca', '102', True),
                  ('Frequência respiratória', '20', False),
                  ('Temperatura', '36,8 °C', False),
                  ('SpO₂ em ar ambiente', '95%', False),
                  ('Peso', '74 kg', False)),
           topicos(('Estado geral', 'Mucosas secas. Orientado, com atenção lenta; '
                    'sem déficit focal.'),
                   ('Pescoço e linfonodos', 'Tireoide normal. Sem adenomegalia '
                    'cervical, supraclavicular, axilar ou inguinal.'),
                   ('Respiratório', 'Murmúrio presente, raros estertores finos '
                    'nas bases.'),
                   ('Coração', 'Rítmico, sem sopros, sem turgência jugular.'),
                   ('Abdome', 'Ruídos diminuídos, indolor, sem massas nem '
                    'visceromegalias.'),
                   ('Pele e membros', 'Sem lesões de pele, sem edema, sem sinovite.')),
           so_kicker=True),

    painel('res1', 'Primeiros exames', 'Sangue', [
        ex('Hemoglobina', '12,8 g/dL', '13,5–17,5 g/dL', True),
        ex('Leucócitos / linfócitos', '5.200 / 780 por mm³', '4.000–11.000 / 1.000–4.800', True),
        ex('Cálcio total / albumina', '13,6 mg/dL / 4,0 g/dL', 'Ca 8,5–10,5 · albumina 3,5–5,0', True),
        ex('Ureia / creatinina', '72 / 2,0 mg/dL {{(creatinina 1,0 há um ano)}}', 'até 45 / 1,3 mg/dL', True),
        ex('Sódio / potássio / cloro', '146 / 3,5 / 106 mmol/L', 'Na 135–145 · K 3,5–5,0 · Cl 98–107', True),
        ex('Glicemia', '98 mg/dL', '70–99 mg/dL'),
    ]),

    pg('estabilizacao', 'Reavaliação após os primeiros resultados',
 'O laboratório comunica o cálcio de 13,6 mg/dL e a creatinina de 2,0. Rafael continua com náuseas e mucosas secas; a glicemia de 98 não explica a sede. A esposa conta que ele bebeu água várias vezes na sala de espera e voltou ao banheiro em menos de uma hora.',
 'Inicia-se solução salina isotônica, ajustada à ausculta, ao volume e à diurese. Hidroclorotiazida e colecalciferol são suspensos. A alteração do cálcio motiva confirmação com cálcio ionizado, dosagem de PTH e ECG. O tratamento não espera a investigação da causa.'),

    painel('res1b', 'Avaliação da hipercalcemia', 'Confirmação e repercussões', [
        ex('Urina', 'Densidade 1.004 · sem glicose · sem proteína · sedimento sem cilindros', '—', True),
        ex('Cálcio ionizado', '1,72 mmol/L', '1,12–1,32 mmol/L', True),
        ex('Fósforo', '4,1 mg/dL', '2,5–4,5 mg/dL'),
        ex('Eletrocardiograma', 'Ritmo sinusal, 102 bpm · QTc 340 ms · sem bloqueios', '—', True),
    ], introducao='O exame de urina pertence à coleta inicial. Os demais exames foram acrescentados após o resultado do cálcio; o PTH ainda está em processamento.'),

    Q('p1', 1,
      'Qual mecanismo explica melhor os dados da admissão?', [
      ('Diurese aquosa por defeito de concentração, com perda de volume', True),
      ('Diurese osmótica por solutos filtrados, com lesão renal secundária', False),
      ('Polidipsia primária, com hipercalcemia por hemoconcentração', False),
      ('Lesão glomerular, com perda urinária de proteínas e cálcio total elevado', False),
      ('Retenção de cálcio pela lesão renal como evento inicial', False),
    ], [('Integração', 'Urina muito diluída, Na 146 e sinais de desidratação sugerem dificuldade para conservar água. A densidade orienta a hipótese; não substitui uma avaliação dirigida se a poliúria persistir. A hipercalcemia pode reduzir a resposta renal ao ADH; desidratação e vasoconstrição renal contribuem para a creatinina.'), ('Comparação', 'A diurese osmótica costuma elevar a osmolalidade urinária; não há glicosúria. Polidipsia não explica bem a hipernatremia e a desidratação, e o ionizado alto afasta aumento apenas por hemoconcentração. Sedimento e proteinúria não sustentam lesão glomerular. Não é preciso esperar Ca 14 para tratar este paciente sintomático.')]),

    disc('urina', 'Rim e estado de hidratação',
 'A hipercalcemia pode reduzir a capacidade renal de concentrar a urina. A perda de água contribui para a desidratação, que por sua vez dificulta a excreção de cálcio. Sem glicosúria e com glicemia normal, diurese osmótica por glicose perde força.',
 'A diurese é acompanhada durante a reposição. A melhora do estado geral, da função renal e do cálcio será reavaliada antes de atribuir toda a lesão renal a um único mecanismo.'),

    pg('evolucao1', 'Primeiras 24 horas',
 'Rafael fica mais atento e consegue tomar o café da manhã sem náusea. A sede diminui e ele deixa de pedir água a cada poucos minutos. A tosse e a limitação ao caminhar pelo corredor continuam.',
 'Cálcio 12,4 mg/dL, creatinina 1,6 mg/dL e sódio 141 mmol/L. O PTH colhido na chegada é 6 pg/mL (15–65). A melhora com volume não demonstra que o suplemento fosse a causa única.'),

    Q('p3', 2, 'Quais dois exames você acrescenta à investigação inicial?',
 [('25-hidroxivitamina D', True), ('Eletroforese de proteínas séricas', True), ('Repetição imediata do PTH', False), ('Cintilografia de paratireoides', False), ('Enzima conversora de angiotensina', False)],
 [('Mecanismos', '25-OH-D avalia se o suplemento elevou o estoque de vitamina D. A eletroforese procura um padrão de proteínas que pode sugerir doença de células produtoras de anticorpos, diante da associação de cálcio alto, anemia e alteração renal. Exames mais específicos serão considerados conforme esses resultados e a imagem.'), ('Limites', 'O PTH já está baixo; repeti-lo imediatamente não responde à causa. Cintilografia de paratireoides localiza doença já caracterizada pelos exames de sangue; não explica este PTH suprimido. ECA tem sensibilidade e especificidade limitadas, não substitui a investigação da causa nem confirma doença granulomatosa.'), ('Como organizar a hipercalcemia', 'Primeiro separe causas dependentes de PTH das demais. Com PTH reduzido, medicamentos, excesso de vitamina D e neoplasias entram na comparação. Anemia e alteração renal justificam pesquisar proteína monoclonal; o resultado será integrado à imagem e à evolução.')]),

    pg('pedidos', 'Investigações em paralelo',
 'São pedidos os dois exames. A radiografia solicitada pela tosse e perda de peso é revista. A investigação pode avançar com esses dados enquanto exames que dependam de outro laboratório são organizados.'),

    painel('res2', 'Investigação', 'Segundo e terceiro dias', [
        ex('25-hidroxivitamina D', '38 ng/mL', '20–50 ng/mL'),
        ex('Eletroforese de proteínas', 'Sem componente monoclonal · gamaglobulina policlonal discretamente elevada', 'sem pico'),
    ]),

    estudo('rx_hilos', 'Radiografia de tórax',
           'Radiografia feita na chegada, pela tosse de dois meses e pela perda '
           'de peso. Olhe os hilos nas duas incidências antes de ler os achados.',
           IMG / 'rx_hilos.jpg',
           'Radiografia frontal e lateral.',
           credito_meta(IMG / 'rx_hilos.jpg.json'),
        [
         ((176, 280), (70, 180), '**Hilo direito** aumentado, de contorno lobulado.', 12),
         ((353, 273), (470, 180), '**Hilo esquerdo** também aumentado: o alargamento é bilateral e simétrico.', -12),
         ((735, 315), (900, 240), 'Na incidência lateral, a **massa hilar** se sobrepõe à sombra cardíaca.', 12),
        ],
        ['Adenopatia hilar bilateral e simétrica, com parênquima sem '
         'opacidades e sem derrame.',
         'Sem calcificações grosseiras visíveis nestas incidências.']),

    pg('calcio_dirigido', 'Complemento da investigação',
 'O cálcio continua alto, o PTH está baixo e a radiografia mostra linfonodos aumentados nos dois hilos. A equipe acrescenta a dosagem da forma ativa da vitamina D, o calcitriol, em laboratório de referência: 104 pg/mL (referência 18–72). A 25-OH-D é 38 ng/mL.',
 'Se a dosagem não estiver disponível, a investigação da alteração no tórax e a coleta de tecido não precisam esperar por ela. Neste caso, o resultado acrescenta informação sobre o mecanismo do cálcio alto.'),

    Q('p4', 3,
      'Quais duas hipóteses melhor integram os novos resultados?', [
      ('Doença granulomatosa com produção extrarrenal de calcitriol', True),
      ('Linfoma com produção aumentada de calcitriol', True),
      ('Intoxicação por colecalciferol como explicação unificadora', False),
      ('Uso do tiazídico como explicação de todos os achados', False),
      ('Hiperparatireoidismo primário agravado pelo tiazídico', False),
    ], [('O mecanismo não é a causa', 'Calcitriol alto com PTH suprimido favorece produção pouco regulada, possível tanto em granulomas quanto em linfomas. A simetria hilar favorece a primeira categoria, mas perda de peso e adenopatia justificam tecido.'), ('Alternativas próximas', '25-OH-D normal enfraquece intoxicação por colecalciferol; o suplemento ainda pode fornecer substrato. O PTH baixo pesa contra hiperparatireoidismo. O tiazídico pode agravar o cálcio alto, mas não explica os linfonodos do tórax. Ainda é necessário investigar doenças que causam esses achados.')]),

    pg('nova_sede', 'Terceiro dia: o alívio não se mantém',
 'Ao reduzir o soro porque já parecia hidratado, Rafael volta a sentir muita sede e urina mais durante a noite. O intestino segue preso. Cálcio 12,8 mg/dL e creatinina 1,5 mg/dL. A ausculta permanece sem congestão.',
 'A equipe reajusta a hidratação e os controles. A recorrência metabólica apesar da retirada dos medicamentos enfraquece a explicação exclusivamente medicamentosa e torna necessário esclarecer a adenopatia. Calcitonina ou outro tratamento de resgate seriam considerados se houvesse agravamento; a investigação não substitui a estabilização.'),

    estudo('tc', 'Tomografia de tórax',
           'Após a radiografia, a equipe pede tomografia para delimitar os linfonodos e escolher um local de coleta. No quarto dia, a creatinina está em 1,3 mg/dL; o exame é realizado após avaliação do risco do contraste.',
           IMG / 'tc_mediastino.jpg',
           'Tomografia com contraste, janela de mediastino.',
           credito_meta(IMG / 'tc_mediastino.jpg.json'),
        [
         ((357, 336), (250, 262), 'Linfonodos **hilares direitos** aumentados e confluentes, sem necrose central.', 12),
         ((668, 395), (742, 470), 'O mesmo no **hilo esquerdo**: a adenopatia é bilateral e simétrica.', -12),
         ((493, 392), (392, 482), 'Linfonodo **subcarinal** aumentado, entre os brônquios principais.', 12),
        ],
        ['Linfonodos hilares bilaterais, subcarinais e paratraqueais, simétricos, '
         'até 2,4 cm, sem necrose e sem calcificação. Na janela de pulmão, '
         'pequenos nódulos ao longo dos feixes broncovasculares e das fissuras. '
         'No abdome, fígado e baço normais, sem linfonodos retroperitoneais.',
         'Sem massa pulmonar dominante descrita na série completa.']),

    pg('olho_novo', 'Quarto dia: a luz passa a incomodar',
 'Enquanto aguarda a coleta, Rafael passa a fechar os olhos ao olhar pela janela. O ardor antigo agora vem com fotofobia e dor, sem secreção. A acuidade à beira do leito parece preservada. Não se trata apenas de revelar o colírio da ficha: a fotofobia começou nesta internação.',
 'A avaliação oftalmológica é organizada no mesmo dia, antes da conclusão do tecido. Não se espera confirmar uma doença sistêmica para examinar um olho doloroso.'),

    Q('p_olho', 4, 'Qual exame você solicita diante da nova queixa?',
 [('Exame à lâmpada de fenda', True), ('Dosagem de cálcio', False), ('Fundo de olho', False), ('Teste de Schirmer', False)],
 [('Novo compartimento', 'Fotofobia e dor exigem pesquisar inflamação intraocular. Lágrima artificial insuficiente não estabelece a causa; a lâmpada de fenda permite examinar a câmara anterior. Fundo, pressão e acuidade também serão avaliados pelo especialista.'),
 ('Limites', 'Cálcio normal não exclui doença ocular. Fundo ou teste de lágrima isolados não avaliam adequadamente uma possível uveíte anterior.')]),

    pg('avaliacao_ocular', 'Avaliação urgente',
 'Há células 2+ na câmara anterior e precipitados ceráticos grandes bilateralmente, sem sinéquias. Acuidade 20/25, pressão 16 e 17 mmHg, sem vitreíte ou edema macular. A oftalmologia caracteriza uveíte anterior granulomatosa e inicia prednisolona tópica e cicloplégico, com controle próximo.',
 'A dor e a fotofobia diminuem após o tratamento local. O cálcio permanece elevado e a tosse continua. A coleta de tecido é mantida, com o controle ocular em paralelo.'),

    bifurcacao('b1', 'Decisão', 'Amostra do mediastino',
 'A investigação permanece inconclusiva. Não há linfonodo periférico acessível. Qual procedimento você escolhe?', [
 caminho('Punção guiada por ecobroncoscopia', 'coleta_ebus', 'Via menos invasiva, feita por equipe com treinamento e equipamento próprios. Se não houver esse recurso, o paciente pode ser encaminhado a um centro ou avaliado para biópsia cirúrgica. A coleta permite estudar as células e pesquisar infecção. Nem toda punção fornece material representativo.'),
 caminho('Mediastinoscopia', 'avaliacao_cirurgica', 'Fornece fragmentos maiores e arquitetura do linfonodo, ao custo de procedimento cirúrgico e anestesia. A indicação é discutida com a equipe e o paciente.')]),

    pg('coleta_ebus', 'Ecobroncoscopia',
 'São puncionados linfonodos subcarinal e hilar direito. Não há intercorrência respiratória. No dia seguinte, a patologia informa que o material tem sangue, poucos linfócitos e raros histiócitos, sem bloco celular representativo. A citometria não pode ser interpretada pela baixa celularidade.',
 'Rafael continua com cálcio de 12,6 mg/dL sob hidratação ajustada. A fotofobia está menor com o colírio, mas a tosse persiste. O resultado da punção não esclareceu a causa da adenopatia.', segue='b_amostra'),

    bifurcacao('b_amostra', 'Decisão', 'Amostra insuficiente',
 'A primeira punção não foi diagnóstica. Qual próximo procedimento você indica?', [
 caminho('Mediastinoscopia', 'avaliacao_cirurgica', 'Permite avaliar arquitetura e obter material maior quando a primeira amostra não resolveu a dúvida, especialmente se neoplasia permanece possível.'),
 caminho('Nova punção guiada por ecobroncoscopia', 'repetir_ebus', 'Pode ser discutida com a equipe experiente se a insuficiência inicial for técnica e houver possibilidade de melhorar a coleta. Persistência de amostra inadequada exigirá outra via.')]),

    pg('repetir_ebus', 'Segunda ecobroncoscopia',
 'A coleta é repetida com avaliação da adequação durante o procedimento e material separado para bloco celular e microbiologia. Desta vez há tecido representativo: granulomas compactos não necrosantes. A citometria não identifica população clonal, sem excluir sozinha todos os tipos de linfoma.',
 'Nesse intervalo, Rafael voltou a alimentar-se e a creatinina chegou a 1,3 mg/dL. O cálcio oscila entre 12,2 e 12,6; a necessidade de hidratação continua. A melhora da náusea não encerrou a investigação.', segue='microbiologia_tecido'),

    pg('avaliacao_cirurgica', 'Mediastinoscopia',
 'Após avaliação anestésica e concordância do paciente, realiza-se mediastinoscopia com biópsia de linfonodo paratraqueal. No pós-operatório tem dor local controlada com analgésico e permanece em observação; não há complicação maior.',
 'A amostra preserva a arquitetura e mostra granulomas não necrosantes. Não foram identificadas células de Reed–Sternberg, infiltrado maligno ou população clonal nos estudos realizados. Fragmentos separados seguem para microbiologia. O cálcio continua acima de 12 mg/dL, apesar da melhora do volume e da creatinina.', segue='microbiologia_tecido'),

    pg('microbiologia_tecido', 'Complemento da investigação',
 'As pesquisas de bacilos álcool-ácido resistentes e de fungos e o teste molecular para tuberculose no tecido são negativos. As culturas permanecem em incubação. A imunodifusão para Histoplasma é negativa, a prova tuberculínica mede 0 mm e o anti-HIV não é reagente.',
 'Os resultados são integrados ao tipo e à qualidade da amostra obtida. A equipe mantém acompanhamento das culturas e reúne os dados do tórax, do olho e da alteração metabólica.'),

    estudo('granuloma', 'O granuloma',
           'Microfotografia do tecido. Observe a organização das células e a região central do agregado.',
           IMG / 'granuloma.jpg',
           'Tecido.',
           credito_meta(IMG / 'granuloma.jpg.json'),
        [
         ((420, 330), (330, 55), '**Histiócitos epitelioides**: citoplasma amplo e pálido, núcleo oval, agrupados de forma compacta.', -12),
         ((500, 628), (330, 700), '**Coroa de linfócitos**, pequenos e escuros, na periferia do granuloma.', 12),
         ((540, 470), (800, 670), '**Centro celular, sem necrose**: é o que define o granuloma como não necrosante.', 12),
        ],
        ['Granuloma não necrosante: agregado compacto de histiócitos '
         'epitelioides com coroa linfocitária, sem necrose central.',
         'Não se observa área central acelular de necrose nesta figura.']),

    Q('p5', 5, 'Quais duas conclusões a biópsia permite neste momento?',
 [('Há inflamação granulomatosa não necrosante', True), ('Ainda é necessário integrar a investigação microbiológica', True), ('A citometria negativa exclui linfoma', False), ('A melhora com hidratação confirma causa medicamentosa', False), ('Granuloma sem necrose exclui tuberculose', False)],
 [('Integração', 'O padrão torácico, a uveíte e o mecanismo do cálcio favorecem doença granulomatosa sistêmica. A histologia não nomeia a causa; microbiologia e evolução continuam necessárias.'), ('Incerteza', 'Granulomas podem ocorrer em infecção ou junto de neoplasia. Citometria tem limitações, especialmente para Hodgkin. Piora discordante exige revisão da amostra, não uma certeza construída de negativos.'), ('Granuloma não define a causa', 'Tuberculose, micoses, reações a substâncias e doenças inflamatórias podem formar granulomas. A ausência de necrose não exclui infecção. A citometria sem clone reduz algumas suspeitas, mas amostra pequena pode não representar todo o processo.')]),

    pg('virada', 'O diagnóstico',
       'O conjunto de manifestações clínicas, distribuição torácica e granulomas não necrosantes favorece sarcoidose. A investigação das alternativas não encontrou outra causa mais consistente até aqui; a equipe acompanhará as culturas e reavaliará o diagnóstico se houver evolução discordante.',
       'A sarcoidose é uma doença granulomatosa de causa desconhecida. Atinge '
       'pulmão e linfonodos do tórax em mais de 90% dos casos e, com frequência, '
       'olho, pele, fígado, rim e coração. Os macrófagos do granuloma expressam '
       'a 1-alfa-hidroxilase e convertem 25-hidroxivitamina D em calcitriol sem '
       'obedecer ao PTH: sobem a absorção intestinal de cálcio, a reabsorção '
       'óssea e a calciúria.',
       'É o que se viu: calcitriol alto com estoque normal, '
       'linfopenia compatível com inflamação sistêmica e adenopatia '
       'hilar simétrica com nódulos ao longo dos feixes. O colecalciferol deu '
       'substrato para essa via, e o tiazídico pode reduzir a excreção renal de cálcio. Ambos podem ter agravado a hipercalcemia, sem explicar sozinhos a doença do tórax.'),

    Q('p6', 6, 'Quais três exames você solicita para completar a avaliação inicial?',
 [('Espirometria', True), ('Difusão de monóxido de carbono', True), ('Fosfatase alcalina', True), ('PET-CT cardíaco', False), ('Holter de rotina', False), ('ECA seriada', False)],
 [('Referência', 'Tosse e falta de ar justificam medir função pulmonar. A difusão avalia a passagem de gás do pulmão para o sangue e pode exigir encaminhamento; não deve atrasar o tratamento do cálcio alto ou do olho. Fosfatase alcalina pode revelar acometimento hepático pouco sintomático. ECG, cálcio, creatinina e hemograma já estão disponíveis; o olho já foi examinado por indicação urgente.'),
 ('Seleção', 'Sem palpitação, síncope ou alteração eletrocardiográfica, exames cardíacos avançados não são rastreio universal inicial. ECA isolada não deve dirigir o tratamento.')]),

    pg('extensao', 'Referência e início de tratamento',
 'Na avaliação de função pulmonar, capacidade vital forçada (CVF) de 83% e capacidade de difusão (DLCO) de 64% do previsto. Fosfatase alcalina e transaminases normais, ECG sem bloqueios ou arritmia. O cálcio permanece acima de 12 mg/dL apesar do suporte, com repercussão renal recente.',
 'Após tecido adequado e revisão da probabilidade residual de infecção, inicia-se prednisona 40 mg/dia, com controles de cálcio, creatinina, eletrólitos e efeitos adversos em uma a duas semanas. A indicação sistêmica é metabólica/renal; a uveíte anterior continua com tratamento local. Culturas ainda pendentes serão conferidas. Não se prescrevem cálcio ou vitamina D automaticamente.'),

    pg('evolucao2', 'Respostas em ritmos diferentes',
 'Em duas semanas, sede e constipação desapareceram; cálcio 10,1 mg/dL, creatinina 1,2 mg/dL. A tosse diminuiu, mas subir escadas ainda cansa. A lâmpada de fenda mostra redução da inflamação, orientando o tratamento ocular.',
 'Em oito semanas, cálcio 9,8 e creatinina 1,1; culturas finais sem crescimento. Durante a redução individualizada, a dor ocular reaparece. A equipe antecipa a oftalmologia: células 2+ no olho direito, sem edema macular. O colírio havia acabado há uma semana; a reposição e o ajuste local controlam o episódio. Exames de sangue normais não garantem controle do olho.'),

    pg('controle', 'Seguimento por órgão',
 'Nos meses seguintes, novas recidivas documentadas apesar de adesão e dificuldade de reduzir a prednisona motivam discussão de poupador com as equipes. Metotrexato é iniciado com ácido fólico e monitorização de hemograma, função hepática e renal, após avaliação de contraindicações e infecções.',
 'Não se atribui automaticamente a recidiva a resistência nem se escala o tratamento por um episódio de falta de colírio. A necessidade e a dose do tratamento sistêmico são revistas ao longo do seguimento.'),

    estudo('rx_tc', 'Comparação: acometimento pulmonar mais extenso',
           'Acometimento pulmonar extenso: observe a radiografia e a tomografia coronal.',
           IMG / 'rx_tc.jpg',
           'Radiografia e TC coronal.',
           credito_meta(IMG / 'rx_tc.jpg.json'),
        [
         ((360, 110), (470, 35), '**Opacidades reticulonodulares** densas, que predominam nos campos superiores.', -12),
         ((638, 257), (575, 420), 'Na TC coronal, **conglomerado peri-hilar** com espessamento peribroncovascular.', 12),
         ((905, 170), (985, 60), '**Micronódulos** difusos, de distribuição perilinfática.', -12),
        ],
        ['Exemplo de acometimento pulmonar mais extenso: opacidades reticulonodulares de '
         'predomínio superior, conglomerados peri-hilares e micronódulos '
         'perilinfáticos.',
         'O padrão radiológico ajuda a mapear extensão, mas sozinho não mede atividade nem define necessidade de aumentar imunossupressão. Rafael será acompanhado por sintomas, função e exames próprios.'],
        segue='fecho'),

    desfecho('fecho', 'Seis meses depois',
 p('Rafael voltou às caminhadas, com visão 20/20, cálcio e creatinina normais e função pulmonar estável. A prednisona está em redução, apoiada pelo poupador. Segue com pneumologia e oftalmologia.'),
 p('A recuperação metabólica rápida, a melhora respiratória mais lenta e a recidiva ocular não foram respostas intercambiáveis. A hipótese permaneceu sujeita à revisão das culturas e da evolução, em vez de ser confirmada apenas pela resposta ao corticoide.'),
 qualidade='melhor', porque='O controle observado exige seguimento de cada órgão; não encerra a vigilância de recaídas ou de diagnósticos alternativos.', fecho='retrospectiva'),

    pagina('retrospectiva', 'Pontos de ensino', '', pontos(
 'Hipercalcemia sintomática exige suporte enquanto se investiga. Retirar tiazida e suplemento não dispensa procurar a causa.',
 'PTH suprimido orienta investigação; calcitriol elevado pode ocorrer em granulomas e em linfomas.',
 'Melhora da sede não explica tosse e adenopatia. Fotofobia nova exige exame urgente, antes do diagnóstico sistêmico.',
 'Granuloma é padrão; amostra adequada, alternativas infecciosas e evolução sustentam o diagnóstico.',
 'Cada órgão exige seguimento próprio; recidiva ocular não depende de hipercalcemia concomitante.'), so_kicker=True),

    pg('referencias', 'Fontes e limites',
       'Paciente, valores e percursos são ficcionais. A cena de abertura é uma '
       'ilustração autoral gerada por inteligência artificial para este caso; '
       'não é fotografia nem documentação clínica.',
       'Crouser e cols. Diagnosis and detection of sarcoidosis, official ATS '
       'clinical practice guideline, 2020. Baughman e cols. ERS clinical practice '
       'guidelines on treatment of sarcoidosis, 2021. Mochizuki e cols. Revised '
       'criteria of the International Workshop on Ocular Sarcoidosis, 2019. '
       'Walker e Shane. Hypercalcemia: a review, JAMA, 2022. Tebben e cols. '
       'Vitamin D-mediated hypercalcemia, Endocrine Reviews, 2016.',
       'Imagens do Wikimedia Commons e com setas adicionadas: radiografia dos hilos e radiografia com TC coronal, Hellerhoff, CC BY-SA 4.0 ('
       + _fonte(IMG / 'rx_hilos.jpg.json', 'hilos') + '; '
       + _fonte(IMG / 'rx_tc.jpg.json', 'radiografia e TC') + '); tomografia '
       'do mediastino e granuloma, Yale Rosen, CC BY-SA 2.0 ('
       + _fonte(IMG / 'tc_mediastino.jpg.json', 'tomografia') + '; '
       + _fonte(IMG / 'granuloma.jpg.json', 'granuloma') + ').',
 'Revisão de 23/10/2026: <a href="https://pubmed.ncbi.nlm.nih.gov/32293205/">ATS 2020, diagnóstico e rastreio</a>; <a href="https://doi.org/10.1183/13993003.04079-2020">ERS 2021, tratamento</a>. A evolução diária é ficcional; não representa uma sequência obrigatória.')
]

REVISAO = []

for _n, _e in enumerate((e for e in ETAPAS if e['t'] == 'pergunta'), 1):
    _e['kicker'] = f'Pergunta {_n}'

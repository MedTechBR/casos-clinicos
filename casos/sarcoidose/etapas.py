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
        ex('Cálcio ionizado', '1,72 mmol/L', '1,12–1,32 mmol/L', True),
        ex('Fósforo', '4,1 mg/dL', '2,5–4,5 mg/dL'),
        ex('Ureia / creatinina', '72 / 2,0 mg/dL {{(creatinina 1,0 há um ano)}}', 'até 45 / 1,3 mg/dL', True),
        ex('Sódio / potássio / cloro', '146 / 3,5 / 106 mmol/L', 'Na 135–145 · K 3,5–5,0 · Cl 98–107', True),
        ex('Glicemia', '98 mg/dL', '70–99 mg/dL'),
        ex('Desidrogenase láctica', '268 U/L', '135–225 U/L', True),
    ]),

    painel('res1b', 'Primeiros exames', 'Urina, gasometria e ECG', [
        ex('Débito urinário na emergência', '220 mL/h nas duas primeiras horas, antes do soro', '—', True),
        ex('Urina', 'Densidade 1.004 · sem glicose · sem proteína · sedimento sem cilindros', '—', True),
        ex('Osmolalidade urinária / sérica', '190 / 302 mOsm/kg', 'sérica 275–295', True),
        ex('Fração de excreção de ureia', '29%', 'abaixo de 35% sugere pré-renal', True),
        ex('Gasometria venosa', 'pH 7,40 · pCO₂ 41 mmHg · HCO₃ 25 mmol/L', '—'),
        ex('Eletrocardiograma', 'Ritmo sinusal, 102 bpm · QTc 340 ms · sem bloqueios', '—', True),
    ]),

    pg('estabilizacao', 'Tratar enquanto se investiga',
 'Na chegada, Rafael recebe solução salina isotônica, ajustada ao exame de volume, diurese e ausculta. Hidroclorotiazida e colecalciferol são suspensos. Cálcio, função renal e eletrólitos são acompanhados; não se espera o nome da causa para tratar a hipercalcemia sintomática.',
 'O PTH e as demais amostras iniciais são colhidos antes de qualquer tratamento etiológico. Não há congestão, arritmia ou piora neurológica progressiva.'),

    Q('p1', 1,
      'Diante da poliúria e da lesão renal, qual mecanismo integra melhor os primeiros exames?', [
      ('Diurese aquosa por defeito de concentração, com depleção de volume', True),
      ('Diurese osmótica por solutos filtrados, com lesão renal secundária', False),
      ('Polidipsia primária, com hipercalcemia por hemoconcentração', False),
      ('Lesão glomerular, com perda urinária de proteínas e cálcio total elevado', False),
      ('Retenção de cálcio pela lesão renal como evento inicial', False),
    ], [('Integração', 'Urina a 190 mOsm/kg diante de plasma a 302 e Na 146 indica perda de água apesar do estímulo para concentrar. A hipercalcemia pode reduzir a resposta renal ao ADH; desidratação e vasoconstrição renal contribuem para a creatinina.'), ('Comparação', 'A diurese osmótica costuma elevar a osmolalidade urinária; não há glicosúria. Polidipsia não explica bem a hiperosmolalidade, e o ionizado alto afasta aumento apenas por hemoconcentração. Sedimento e proteinúria não sustentam lesão glomerular. Não é preciso esperar Ca 14 para tratar este paciente sintomático.')]),

    disc('urina', 'Duas alterações que se reforçam',
 'Urina diluída apesar de plasma hiperosmolar e desidratação sugere defeito de concentração. A hipercalcemia pode reduzir a resposta renal ao ADH; a perda de água, por sua vez, piora a depuração do cálcio. Não há glicosúria que sustente diurese osmótica por glicose.',
 'Fração de excreção de ureia de 29% apoia, mas não comprova, componente hemodinâmico. Diurético, função renal prévia e contexto limitam os índices urinários. A resposta à hidratação será mais informativa que atribuir toda a lesão renal a um único número.'),

    pg('evolucao1', 'Primeiras 24 horas',
 'Rafael fica mais atento e consegue tomar o café da manhã sem náusea. A sede diminui e ele deixa de pedir água a cada poucos minutos. A tosse e a limitação ao caminhar pelo corredor continuam.',
 'Cálcio 12,4 mg/dL, creatinina 1,6 mg/dL e sódio 141 mmol/L. O PTH colhido na chegada é 6 pg/mL (15–65). A melhora com volume não demonstra que o suplemento fosse a causa única.'),

    Q('p3', 2, 'Com PTH suprimido, quais quatro exames mais ajudam a discriminar os mecanismos neste paciente?',
 [('PTHrP', True), ('25-hidroxivitamina D', True), ('1,25-di-hidroxivitamina D', True), ('Eletroforese de proteínas séricas', True), ('Cintilografia de paratireoides', False), ('Enzima conversora de angiotensina', False)],
 [('Mecanismos', 'PTHrP procura mecanismo humoral tumoral; 25-OH-D avalia excesso de estoque e calcitriol investiga produção pouco regulada. Eletroforese é pertinente diante de hipercalcemia, anemia e alteração renal; a equipe complementa com cadeias leves livres.'),
 ('Limites', 'Cintilografia de paratireoides localiza doença já caracterizada bioquimicamente; não explica este PTH suprimido. ECA tem sensibilidade e especificidade limitadas, não substitui a investigação etiológica nem confirma doença granulomatosa.')]),

    pg('pedidos', 'Investigações em paralelo',
 'As quatro dosagens são encaminhadas. Acrescentam-se cadeias leves livres e calciúria de 24 horas. A radiografia pedida pela tosse e perda de peso também é revista. Todos os resultados clinicamente indicados serão discutidos, independentemente da seleção na pergunta.'),

    painel('res2', 'Investigação', 'Segundo e terceiro dias', [
        ex('PTHrP', 'Não detectado', 'não detectado'),
        ex('25-hidroxivitamina D', '38 ng/mL', '20–50 ng/mL'),
        ex('1,25-di-hidroxivitamina D', '104 pg/mL', '18–72 pg/mL', True),
        ex('Eletroforese de proteínas', 'Sem componente monoclonal · gamaglobulina policlonal discretamente elevada', 'sem pico'),
        ex('Cadeias leves livres', 'Relação kappa/lambda 1,3', '0,26–1,65'),
        ex('Calciúria de 24 horas', '410 mg', 'abaixo de 300 mg', True),
    ]),

    estudo('rx_hilos', 'Radiografia de tórax',
           'Radiografia feita na chegada, pela tosse de dois meses e pela perda '
           'de peso. Olhe os hilos nas duas incidências antes de ler os achados.',
           IMG / 'rx_hilos.jpg',
           'Radiografia frontal e lateral de outro paciente · comparação didática.',
           credito_meta(IMG / 'rx_hilos.jpg.json'),
        [
         ((176, 280), (70, 180), '**Hilo direito** aumentado, de contorno lobulado.', 12),
         ((353, 273), (470, 180), '**Hilo esquerdo** também aumentado: o alargamento é bilateral e simétrico.', -12),
         ((735, 315), (900, 240), 'Na incidência lateral, a **massa hilar** se sobrepõe à sombra cardíaca.', 12),
        ],
        ['Adenopatia hilar bilateral e simétrica, com parênquima sem '
         'opacidades e sem derrame.',
         'A simetria sugere processo sistêmico. Doenças granulomatosas, '
         'incluindo tuberculose e histoplasmose, e linfoma ficam no '
         'diferencial.']),

    Q('p4', 3,
      'Calcitriol 104, 25-OH-D 38, PTHrP não detectado. Quais duas hipóteses ainda integram hipercalcemia e adenopatia?', [
      ('Doença granulomatosa com produção extrarrenal de calcitriol', True),
      ('Linfoma com produção aumentada de calcitriol', True),
      ('Intoxicação por colecalciferol como explicação unificadora', False),
      ('Hipercalcemia humoral por PTHrP', False),
      ('Hiperparatireoidismo primário agravado pelo tiazídico', False),
    ], [('O mecanismo não é a etiologia', 'Calcitriol alto com PTH suprimido favorece produção pouco regulada, possível tanto em granulomas quanto em linfomas. A simetria hilar favorece a primeira categoria, mas perda de peso e adenopatia justificam tecido.'), ('Alternativas próximas', '25-OH-D normal enfraquece intoxicação por colecalciferol; o suplemento ainda pode fornecer substrato. PTHrP não detectado e PTH suprimido tornam os outros dois mecanismos menos prováveis, sem excluir neoplasia por outra via.')]),

    pg('nova_sede', 'Terceiro dia: o alívio não se mantém',
 'Ao reduzir o soro porque já parecia hidratado, Rafael volta a sentir muita sede e urina mais durante a noite. O intestino segue preso. Cálcio 12,8 mg/dL e creatinina 1,5 mg/dL. A ausculta permanece sem congestão.',
 'A equipe reajusta a hidratação e os controles. A recorrência metabólica apesar da retirada dos medicamentos enfraquece a explicação exclusivamente medicamentosa e torna necessário esclarecer a adenopatia. Calcitonina ou outro tratamento de resgate seriam considerados se houvesse agravamento; a investigação não substitui a estabilização.'),

    estudo('tc', 'Tomografia de tórax',
           'No quarto dia, com creatinina de 1,3 mg/dL, a equipe faz tomografia '
           'de tórax e abdome com contraste para estadiar a adenopatia e '
           'escolher onde biopsiar. Com perda de peso, DHL alta e calcitriol '
           'possivelmente produzido fora do rim, a equipe mantém linfoma entre as hipóteses '
           'prioritárias, ao lado de doenças granulomatosas.',
           IMG / 'tc_mediastino.jpg',
           'Tomografia com contraste de outro paciente, janela de mediastino · comparação didática.',
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
         'Os linfonodos do mediastino são o alvo da biópsia. O diferencial '
         'registrado: doença granulomatosa não infecciosa, linfoma, tuberculose ganglionar e histoplasmose.']),

    pg('olho_novo', 'Quarto dia: a luz passa a incomodar',
 'Enquanto aguarda a coleta, Rafael passa a fechar os olhos ao olhar pela janela. O ardor antigo agora vem com fotofobia e dor, sem secreção. A acuidade à beira do leito parece preservada. Não se trata apenas de revelar o colírio da ficha: a fotofobia começou nesta internação.',
 'A avaliação oftalmológica é organizada no mesmo dia, antes da conclusão do tecido. Não se espera confirmar uma doença sistêmica para examinar um olho doloroso.'),

    Q('p_olho', 4, 'Qual avaliação responde melhor à mudança ocular?',
 [('Exame à lâmpada de fenda', True), ('Dosagem de cálcio', False), ('Fundo de olho isoladamente', False), ('Teste de Schirmer isoladamente', False)],
 [('Novo compartimento', 'Fotofobia e dor exigem pesquisar inflamação intraocular. Lágrima artificial insuficiente não estabelece a causa; a lâmpada de fenda permite examinar a câmara anterior. Fundo, pressão e acuidade também serão avaliados pelo especialista.'),
 ('Limites', 'Cálcio normal não exclui doença ocular. Fundo ou teste de lágrima isolados não avaliam adequadamente uma possível uveíte anterior.')]),

    pg('avaliacao_ocular', 'Avaliação urgente',
 'Há células 2+ na câmara anterior e precipitados ceráticos grandes bilateralmente, sem sinéquias. Acuidade 20/25, pressão 16 e 17 mmHg, sem vitreíte ou edema macular. A oftalmologia caracteriza uveíte anterior granulomatosa e inicia prednisolona tópica e cicloplégico, com controle próximo.',
 'O achado aproxima os problemas ocular e torácico, mas não distingue sozinho inflamação não infecciosa de infecção. Não se inicia prednisona sistêmica apenas pela aparência do olho; a coleta torácica é mantida.'),

    bifurcacao('b1', 'Decisão', 'Amostra do mediastino',
 'Sem linfonodo periférico acessível, a equipe precisa de tecido para distinguir inflamação, infecção e neoplasia. Qual via inicial você escolhe?', [
 caminho('Punção guiada por ecobroncoscopia', 'coleta_ebus', 'É menos invasiva e tem bom rendimento em adenopatia com suspeita granulomatosa; planejar bloco celular, citometria e microbiologia.'),
 caminho('Avaliação para mediastinoscopia', 'avaliacao_cirurgica', 'Pode fornecer arquitetura mais ampla, sobretudo se houver forte suspeita de linfoma ou amostra endoscópica insuficiente. O benefício precisa ser ponderado com o risco cirúrgico.')]),

    pg('coleta_ebus', 'Plano de coleta',
 'Patologia e microbiologia combinam a distribuição das punções para bloco celular, citometria e culturas. A equipe explica que citometria negativa não exclui todos os linfomas e que uma amostra insuficiente exigirá nova estratégia.', segue='tecido'),

    pg('avaliacao_cirurgica', 'Discussão entre as equipes',
 'A cirurgia revê o caso e os riscos. Com adenopatia simétrica e alvo endoscópico acessível, decide-se começar por EBUS; mediastinoscopia fica como alternativa se o material não responder à dúvida. A decisão antecipada muda o planejamento da amostra, sem atribuir uma complicação obrigatória à via cirúrgica.', segue='tecido'),

    pg('tecido', 'A ecobroncoscopia',
       'Punções dos linfonodos subcarinal e hilar direito: granulomas não '
       'necrosantes, compactos, sem células atípicas. A citometria de fluxo não '
       'mostra população clonal.',
       'Pesquisa de bacilo álcool-ácido resistente e de fungos, teste molecular '
       'rápido para tuberculose e imunodifusão para //Histoplasma// negativos. '
       'Prova tuberculínica de 0 mm. Anti-HIV não reagente. As culturas para '
       'micobactéria e fungo seguem em incubação por seis a oito semanas.'),

    estudo('granuloma', 'O granuloma',
           'Lâmina do bloco celular da punção. Para comparação, microfotografia '
           'de tecido de outro paciente com o mesmo padrão. Descreva o granuloma '
           'antes de ler a interpretação.',
           IMG / 'granuloma.jpg',
           'Tecido de outro paciente · comparação morfológica.',
           credito_meta(IMG / 'granuloma.jpg.json'),
        [
         ((420, 330), (330, 55), '**Histiócitos epitelioides**: citoplasma amplo e pálido, núcleo oval, agrupados de forma compacta.', -12),
         ((500, 628), (330, 700), '**Coroa de linfócitos**, pequenos e escuros, na periferia do granuloma.', 12),
         ((540, 470), (800, 670), '**Centro celular, sem necrose**: é o que define o granuloma como não necrosante.', 12),
        ],
        ['Granuloma não necrosante: agregado compacto de histiócitos '
         'epitelioides com coroa linfocitária, sem necrose central.',
         'A lâmina descreve uma forma de reação, não a causa. O diagnóstico '
         'junta a lâmina, as culturas e a história.']),

    Q('p5', 5, 'Quais duas conclusões são sustentadas pelo tecido e pela evolução?',
 [('Há inflamação granulomatosa não necrosante', True), ('Ainda é necessário integrar a investigação microbiológica', True), ('A citometria negativa exclui linfoma', False), ('A melhora com hidratação confirma causa medicamentosa', False), ('Granuloma sem necrose exclui tuberculose', False)],
 [('Integração', 'O padrão torácico, a uveíte e o mecanismo do cálcio favorecem doença granulomatosa sistêmica. A histologia não nomeia a etiologia; microbiologia e evolução continuam necessárias.'),
 ('Incerteza', 'Granulomas podem ocorrer em infecção ou junto de neoplasia. Citometria tem limitações, especialmente para Hodgkin. Piora discordante exige revisão da amostra, não uma certeza construída de negativos.')]),

    pg('virada', 'O diagnóstico',
       'O conjunto de manifestações clínicas, distribuição torácica e granulomas não necrosantes favorece sarcoidose. A investigação das alternativas não encontrou outra causa mais consistente até aqui; a equipe acompanhará as culturas e reavaliará o diagnóstico se houver evolução discordante.',
       'A sarcoidose é uma doença granulomatosa de causa desconhecida. Atinge '
       'pulmão e linfonodos do tórax em mais de 90% dos casos e, com frequência, '
       'olho, pele, fígado, rim e coração. Os macrófagos do granuloma expressam '
       'a 1-alfa-hidroxilase e convertem 25-hidroxivitamina D em calcitriol sem '
       'obedecer ao PTH: sobem a absorção intestinal de cálcio, a reabsorção '
       'óssea e a calciúria.',
       'É o que se viu: calcitriol alto com estoque normal, calciúria de 410 mg, '
       'linfopenia compatível com inflamação sistêmica e adenopatia '
       'hilar simétrica com nódulos ao longo dos feixes. O colecalciferol deu '
       'substrato para essa via, e o tiazídico pode reduzir a excreção renal de cálcio. Ambos podem ter agravado a hipercalcemia, sem explicar sozinhos a doença do tórax.'),

    Q('p6', 6, 'Quais três exames completam melhor a referência funcional e o rastreio ainda não documentados?',
 [('Espirometria', True), ('Difusão de monóxido de carbono', True), ('Fosfatase alcalina', True), ('PET-CT cardíaco', False), ('Holter de rotina', False), ('ECA seriada', False)],
 [('Referência', 'Tosse e dispneia justificam medir função pulmonar. Fosfatase alcalina pode revelar acometimento hepático pouco sintomático. ECG, cálcio, creatinina e hemograma já estão disponíveis; o olho já foi examinado por indicação urgente.'),
 ('Seleção', 'Sem palpitação, síncope ou alteração eletrocardiográfica, exames cardíacos avançados não são rastreio universal inicial. ECA isolada não deve dirigir o tratamento.')]),

    pg('extensao', 'Referência e início de tratamento',
 'CVF 83% e DLCO 64% do previsto. Fosfatase alcalina e transaminases normais, ECG sem bloqueios ou arritmia. O cálcio permanece acima de 12 mg/dL apesar do suporte, com repercussão renal recente.',
 'Após tecido adequado e revisão da probabilidade residual de infecção, inicia-se prednisona 40 mg/dia, com controles de cálcio, creatinina, eletrólitos e efeitos adversos em uma a duas semanas. A indicação sistêmica é metabólica/renal; a uveíte anterior continua com tratamento local. Culturas ainda pendentes serão conferidas. Não se prescrevem cálcio ou vitamina D automaticamente.'),

    pg('evolucao2', 'Respostas em ritmos diferentes',
 'Em duas semanas, sede e constipação desapareceram; cálcio 10,1 mg/dL, creatinina 1,2 mg/dL. A tosse diminuiu, mas subir escadas ainda cansa. A lâmpada de fenda mostra redução da inflamação, orientando o tratamento ocular.',
 'Em oito semanas, cálcio 9,8 e creatinina 1,1; culturas finais sem crescimento. Durante a redução individualizada, a dor ocular reaparece. A equipe antecipa a oftalmologia: células 2+ no olho direito, sem edema macular. O colírio havia acabado há uma semana; a reposição e o ajuste local controlam o episódio. Exames de sangue normais não garantem controle do olho.'),

    pg('controle', 'Seguimento por órgão',
 'Nos meses seguintes, novas recidivas documentadas apesar de adesão e dificuldade de reduzir a prednisona motivam discussão de poupador com as equipes. Metotrexato é iniciado com ácido fólico e monitorização de hemograma, função hepática e renal, após avaliação de contraindicações e infecções.',
 'Não se atribui automaticamente a recidiva a resistência nem se escala o tratamento por um episódio de falta de colírio. A necessidade e a dose do tratamento sistêmico são revistas ao longo do seguimento.'),

    estudo('rx_tc', 'Comparação: acometimento pulmonar mais extenso',
           'Comparação didática de outro paciente com acometimento pulmonar mais extenso. Não é um exame novo de Rafael nem documenta progressão no seu seguimento.',
           IMG / 'rx_tc.jpg',
           'Radiografia e TC coronal de outro paciente · comparação didática.',
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
       'Imagens de outros pacientes, todas do Wikimedia Commons e com setas '
       'adicionadas: radiografia dos hilos e radiografia com TC coronal, '
       'Hellerhoff, CC BY-SA 4.0 ('
       + _fonte(IMG / 'rx_hilos.jpg.json', 'hilos') + '; '
       + _fonte(IMG / 'rx_tc.jpg.json', 'radiografia e TC') + '); tomografia '
       'do mediastino e granuloma, Yale Rosen, CC BY-SA 2.0 ('
       + _fonte(IMG / 'tc_mediastino.jpg.json', 'tomografia') + '; '
       + _fonte(IMG / 'granuloma.jpg.json', 'granuloma') + ').',
 'Revisão de 23/10/2026: <a href="https://pubmed.ncbi.nlm.nih.gov/32293205/">ATS 2020, diagnóstico e rastreio</a>; <a href="https://doi.org/10.1183/13993003.04079-2020">ERS 2021, tratamento</a>. A evolução diária é ficcional; não representa uma sequência obrigatória. A prancha de acometimento pulmonar extenso é comparação didática, não um exame de Rafael.')
]

REVISAO = []

for _n, _e in enumerate((e for e in ETAPAS if e['t'] == 'pergunta'), 1):
    _e['kicker'] = f'Pergunta {_n}'

"""Hipercalcemia com PTH suprimido, calcitriol alto e adenopatia hilar.

Molde do //New England// lido em 26/09/2026 (ver
Artifacts/nejm-casos-classicos/GRAMATICA_LIDA_2026-09-26.md), no desenho do
piloto da leptospirose: apresentação curta, ficha do paciente com uma pista
enterrada (o colírio lubrificante), exame físico com os sinais vitais como
primeiro item e primeiros exames entregues prontos. As primeiras perguntas
leem números (o cálcio, a urina diluída) e depois o divisor do PTH. A âncora
é a da equipe naquele momento: adenopatia hilar, perda de peso, DHL alta e
calcitriol alto num homem de 41 anos são linfoma até a biópsia. O granuloma
não necrosante do EBUS vira o caso; o nome aparece pela primeira vez na
pergunta que interpreta o tecido, depois da metade. O olho, que estava na
ficha, só é examinado no rastreio de base.

Paciente ficcional. Critérios e condutas: ATS 2020 (diagnóstico e
rastreio), ERS 2021 (tratamento), Walker e Shane, JAMA 2022 (hipercalcemia).
"""
from pathlib import Path

from motor.estudo_imagem import estudo
from motor.etapas import (alt, bifurcacao, caminho, capa, desfecho, op, p,
                          pagina, painel, par, pareamento, pergunta, pontos,
                          topicos)

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
           topicos(('Sinais vitais', 'Pressão 104/66 mmHg · frequência cardíaca '
                    '102 · frequência respiratória 20 · temperatura 36,8 °C · '
                    'SpO₂ 95% em ar ambiente · peso 74 kg.'),
                   ('Estado geral', 'Mucosas secas. Orientado, com atenção lenta; '
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
         'Com perda de peso e tosse, a equipe pensa primeiro em linfoma; '
         'tuberculose ganglionar, histoplasmose e metástase ficam no '
         'diferencial.']),

    Q('p1', 1,
      'Cálcio total de 13,6 mg/dL, albumina de 4,0 g/dL, cálcio ionizado de '
      '1,72 mmol/L e QTc de 340 ms. **Quais três** leituras estão corretas?', [
      ('Hipercalcemia verdadeira, confirmada pelo ionizado', True),
      ('Faixa moderada, entre 12 e 14 mg/dL', True),
      ('QT curto como efeito do cálcio', True),
      ('Grave, por passar de 13 mg/dL', False),
      ('A correção pela albumina muda a leitura', False),
      ('Pseudo-hipercalcemia por paraproteína', False),
     ], [
      ('Os números', 'Com albumina de 4,0 g/dL, o cálcio corrigido é o próprio '
       'total, 13,6 mg/dL, e o ionizado de 1,72 mmol/L mostra que a fração '
       'livre, a que age, está alta. Uma paraproteína que liga cálcio subiria o '
       'total sem mexer no ionizado; aqui os dois sobem juntos.'),
      ('A gravidade', 'Na classificação usual (Walker e Shane, JAMA 2022), até '
       '12 mg/dL é leve, de 12 a 13,9 é moderada e de 14 em diante é grave. Ele '
       'está na faixa moderada, mas com sintomas: sede, poliúria, constipação, '
       'atenção lenta e creatinina que dobrou. O QTc de 340 ms é o encurtamento '
       'da repolarização que o cálcio alto produz.'),
      ('O que isso muda', 'Hipercalcemia moderada com sintomas se trata na '
       'emergência: soro fisiológico para repor o volume perdido na urina, '
       'suspensão do tiazídico, que reduz a excreção renal de cálcio, e do '
       'colecalciferol. Furosemida só entra depois de restaurado o volume, e '
       'apenas se houver sobrecarga.'),
     ]),

    Q('p2', 2,
      'Poliúria de 220 mL/h num paciente desidratado, com osmolalidade '
      'urinária de 190 mOsm/kg e sódio de 146 mmol/L. Qual a leitura mais '
      'adequada?', [
      ('Diabetes insípido nefrogênico pela hipercalcemia', True),
      ('Diabetes insípido central', False),
      ('Polidipsia primária', False),
      ('Diurese osmótica', False),
      ('Necrose tubular aguda', False),
      ('Efeito do tiazídico', False),
     ], [
      ('O padrão', 'Com mucosas secas e sódio de 146, o rim deveria concentrar '
       'a urina, e ela sai mais diluída que o plasma. Glicemia de 98 e urina '
       'sem glicose afastam diurese osmótica. É o defeito de concentração da '
       'hipercalcemia: o cálcio ativa o receptor sensor de cálcio na alça de '
       'Henle e no ducto coletor e reduz a resposta ao hormônio antidiurético.'),
      ('E a creatinina', 'A fração de excreção de ureia de 29% indica '
       'componente pré-renal; ela serve aqui porque o tiazídico distorce a '
       'fração de excreção de sódio. A perda de água pela urina e a '
       'vasoconstrição renal causada pelo cálcio somam. Sedimento sem cilindros '
       'não sugere necrose tubular.'),
      ('Por que não as outras', 'Na polidipsia primária o sódio fica normal ou '
       'baixo, não em 146. O diabetes insípido central também dilui a urina, '
       'mas o cálcio já explica o quadro, e a poliúria que some quando o cálcio '
       'cai resolve a dúvida. O tiazídico não dilui a urina; ele é usado, ao '
       'contrário, para reduzir a poliúria do diabetes insípido nefrogênico.'),
     ]),

    pg('evolucao1', 'Primeiras 24 horas',
       'Com soro fisiológico guiado pela diurese e sem hidroclorotiazida nem '
       'colecalciferol, Rafael fica mais atento. O cálcio cai para 12,4 mg/dL, '
       'a creatinina para 1,6 mg/dL e o sódio para 141 mmol/L.',
       'O PTH, colhido na chegada, é de 6 pg/mL (referência 15 a 65).'),

    Q('p3', 3,
      'Cálcio de 12,4 mg/dL com PTH de 6 pg/mL. **Quais quatro** exames são '
      'os mais apropriados agora?', [
      ('Peptídeo relacionado ao PTH (PTHrP)', True),
      ('25-hidroxi e 1,25-di-hidroxivitamina D', True),
      ('Eletroforese de proteínas e cadeias leves livres', True),
      ('Tomografia de tórax e abdome', True),
      ('Cintilografia das paratireoides com sestamibi', False),
      ('Cintilografia óssea', False),
      ('Calcitonina sérica', False),
     ], [
      ('PTH suprimido', 'Com cálcio alto, um PTH de 6 pg/mL está '
       'suprimido: a paratireoide não é a causa, e o sestamibi procuraria um '
       'adenoma que esse PTH já afasta.'),
      ('Os quatro', 'PTHrP para a hipercalcemia humoral dos tumores sólidos. '
       'As duas vitaminas D juntas separam excesso de suplemento (25-hidroxi '
       'alta) de calcitriol produzido sem controle (1,25 alta). Eletroforese e '
       'cadeias leves procuram mieloma. A tomografia estuda os hilos e escolhe '
       'onde biopsiar.'),
      ('O que não entra', 'Cintilografia óssea vê mal a lesão lítica do '
       'mieloma. Calcitonina marca carcinoma medular de tireoide e não explica '
       'hipercalcemia.'),
     ]),

    painel('res2', 'Investigação', 'Segundo e terceiro dias', [
        ex('PTHrP', 'Não detectado', 'não detectado'),
        ex('25-hidroxivitamina D', '38 ng/mL', '20–50 ng/mL'),
        ex('1,25-di-hidroxivitamina D', '104 pg/mL', '18–72 pg/mL', True),
        ex('Eletroforese de proteínas', 'Sem componente monoclonal · gamaglobulina policlonal discretamente elevada', 'sem pico'),
        ex('Cadeias leves livres', 'Relação kappa/lambda 1,3', '0,26–1,65'),
        ex('Calciúria de 24 horas', '410 mg', 'abaixo de 300 mg', True),
    ]),

    pareamento('p4', 'Pergunta 4',
      'O 1,25-di-hidroxivitamina D está alto e o 25-hidroxi, normal. Associe '
      'cada perfil de outro paciente ao mecanismo da hipercalcemia.', [
      par('PTH 95 pg/mL, fósforo 2,2 mg/dL, calciúria alta',
          'Hiperparatireoidismo primário',
          'O PTH reabsorve cálcio e espolia fósforo; é a causa mais comum no '
          'ambulatório.'),
      par('PTH 48 pg/mL, fração de excreção de cálcio abaixo de 0,01',
          'Hipercalcemia hipocalciúrica familiar',
          'O sensor de cálcio mal regulado mantém PTH normal e calciúria muito '
          'baixa.'),
      par('PTH suprimido, PTHrP alto, 1,25-(OH)₂D baixo',
          'Hipercalcemia humoral maligna',
          'O PTHrP imita o PTH no osso e no rim, mas não ativa a vitamina D.'),
      par('PTH suprimido, 1,25-(OH)₂D alto, 25-OH-D normal',
          'Produção extrarrenal de calcitriol',
          'É o perfil de Rafael: uma 1-alfa-hidroxilase fora do rim, que não '
          'obedece ao PTH.'),
      par('PTH suprimido, 25-OH-D de 180 ng/mL',
          'Intoxicação por vitamina D',
          'Exige doses muito altas por meses; o 25-OH de Rafael é 38.'),
      par('PTH suprimido, bicarbonato 34 mmol/L, carbonato de cálcio diário',
          'Síndrome leite-álcali',
          'Cálcio oral, alcalose e lesão renal se alimentam; o bicarbonato de '
          'Rafael é 25.'),
    ], opcoes=['Hiperparatireoidismo primário', 'Hipercalcemia hipocalciúrica familiar',
               'Hipercalcemia humoral maligna', 'Produção extrarrenal de calcitriol',
               'Intoxicação por vitamina D', 'Síndrome leite-álcali',
               'Mieloma múltiplo'],
    titulo_resposta='O calcitriol alto com estoque normal aponta para fora do rim',
    nota='A opção que sobrou, mieloma, teria paraproteína ou cadeias leves '
         'alteradas; as de Rafael são normais.'),

    estudo('tc', 'Tomografia de tórax',
           'No quarto dia, com creatinina de 1,3 mg/dL, a equipe faz tomografia '
           'de tórax e abdome com contraste para estadiar a adenopatia e '
           'escolher onde biopsiar. Com perda de peso, DHL alta e calcitriol '
           'produzido fora do rim, a hematologia registra linfoma como hipótese '
           'principal.',
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
         'registrado: linfoma, tuberculose ganglionar e histoplasmose.']),

    bifurcacao('b1', 'Decisão', 'Como chegar ao tecido',
      'Rafael está estável, com cálcio de 11,6 mg/dL e sem ameaça '
      'respiratória. Como conduzir a definição da causa?', [
      caminho('Ecobroncoscopia com punção dos linfonodos, citometria e '
              'culturas', 'tecido',
              'Chega aos linfonodos do mediastino sem cirurgia e colhe material '
              'para linfoma, micobactéria e fungo antes de qualquer '
              'imunossupressão.'),
      caminho('Prednisona agora; biópsia só se o cálcio não cair',
              'empirico',
              'Corticoide antes da biópsia pode deixar um linfoma irreconhecível '
              'na lâmina e piorar tuberculose ou histoplasmose.'),
      caminho('Atribuir ao suplemento, dar alta e reavaliar', 'suplemento',
              'O colecalciferol soma, mas não produz linfonodo nem calcitriol '
              'alto com 25-hidroxi normal.'),
    ]),

    pg('empirico', 'Dez dias de prednisona',
       'Com 40 mg/dia, o cálcio cai e a tosse melhora. A hematologia se recusa a '
       'manter o corticoide sem tecido, e ninguém excluiu linfoma, tuberculose '
       'nem histoplasmose. A ecobroncoscopia é feita com o paciente já sob '
       'prednisona, e o patologista é avisado de que o corticoide pode reduzir '
       'o rendimento da amostra.',
       segue='tecido'),

    pg('suplemento', 'Dez semanas depois',
       'Rafael saiu com hidratação oral, sem suplemento e sem tiazídico, e '
       'retorno marcado para dois meses. Volta antes, com cálcio de 13,1 mg/dL, '
       'creatinina de 1,9 mg/dL, falta de ar ao caminhar no plano e dor nos '
       'dois olhos com a luz. É readmitido e hidratado de novo; a radiografia e '
       'a tomografia são repetidas.'),

    estudo('rx_tc', 'Radiografia e tomografia na readmissão',
           'Exames repetidos pela falta de ar nova. Compare com a radiografia '
           'da chegada, que mostrava só os hilos, com o parênquima limpo.',
           IMG / 'rx_tc.jpg',
           'Radiografia e TC coronal de outro paciente · comparação didática.',
           credito_meta(IMG / 'rx_tc.jpg.json'),
        [
         ((360, 110), (470, 35), '**Opacidades reticulonodulares** densas, que predominam nos campos superiores.', -12),
         ((638, 257), (575, 420), 'Na TC coronal, **conglomerado peri-hilar** com espessamento peribroncovascular.', 12),
         ((905, 170), (985, 60), '**Micronódulos** difusos, de distribuição perilinfática.', -12),
        ],
        ['Doença parenquimatosa nova e extensa: opacidades reticulonodulares de '
         'predomínio superior, conglomerados peri-hilares e micronódulos '
         'perilinfáticos.',
         'Em dez semanas sem diagnóstico, a doença saiu dos linfonodos para o '
         'pulmão. A ecobroncoscopia é feita na mesma internação.'],
        segue='tecido'),

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

    Q('p5', 5,
      'Granulomas não necrosantes, citometria sem clone, pesquisas '
      'negativas e culturas pendentes. Qual a interpretação mais adequada?', [
      ('Sarcoidose provável, a confirmar pelas culturas', True),
      ('Tuberculose excluída pelo teste molecular', False),
      ('Sem necrose, infecção está excluída', False),
      ('Granuloma confirma e dispensa as culturas', False),
      ('Linfoma confirmado pela reação granulomatosa', False),
      ('Esquema para tuberculose até sair a cultura', False),
      ('Biópsia cirúrgica antes de qualquer conduta', False),
     ], [
      ('Os critérios', 'A ATS (2020) pede quadro compatível, granuloma não '
       'necrosante em tecido e exclusão razoável das outras causas de '
       'granuloma. Os dois primeiros estão aqui; a exclusão depende das '
       'culturas, que levam de seis a oito semanas.'),
      ('Por que não as outras', 'O teste molecular negativo reduz a chance de '
       'tuberculose sem zerá-la, e o galinheiro da ficha mantém a histoplasmose '
       'em mente; as duas podem dar granuloma sem necrose. O linfoma de Hodgkin '
       'pode vir cercado de granulomas e escapa à citometria, mas a lâmina não '
       'tem células atípicas. Biópsia cirúrgica fica para quando o quadro '
       'divergir, e tratar tuberculose sem evidência só soma toxicidade.'),
     ]),

    pg('virada', 'O diagnóstico',
       'Com quadro compatível, granuloma não necrosante e infecção e linfoma '
       'razoavelmente afastados, a equipe fecha o diagnóstico de sarcoidose, '
       'que as culturas finais ainda precisam sustentar.',
       'A sarcoidose é uma doença granulomatosa de causa desconhecida. Atinge '
       'pulmão e linfonodos do tórax em mais de 90% dos casos e, com frequência, '
       'olho, pele, fígado, rim e coração. Os macrófagos do granuloma expressam '
       'a 1-alfa-hidroxilase e convertem 25-hidroxivitamina D em calcitriol sem '
       'obedecer ao PTH: sobem a absorção intestinal de cálcio, a reabsorção '
       'óssea e a calciúria.',
       'É o que se viu: calcitriol alto com estoque normal, calciúria de 410 mg, '
       'linfopenia pelo sequestro de linfócitos nos granulomas e adenopatia '
       'hilar simétrica com nódulos ao longo dos feixes. O colecalciferol deu '
       'substrato, e o tiazídico impediu o rim de eliminar o excesso: os dois '
       'descompensaram uma produção de calcitriol que vinha de antes.'),

    Q('p6', 6,
      'Pela ATS, **quais três** avaliações se fazem em todo paciente ao '
      'diagnóstico, mesmo sem sintomas?', [
      ('Eletrocardiograma de 12 derivações', True),
      ('Exame oftalmológico com lâmpada de fenda', True),
      ('Creatinina e fosfatase alcalina', True),
      ('Ecocardiograma e Holter de rotina', False),
      ('PET-CT de corpo inteiro', False),
      ('Biópsia hepática', False),
      ('Enzima conversora seriada', False),
     ], [
      ('O rastreio de base', 'A ATS (2020) sugere, para todo paciente ao '
       'diagnóstico, mesmo sem sintomas: eletrocardiograma, exame oftalmológico, '
       'cálcio, creatinina e fosfatase alcalina. O cálcio de Rafael já é '
       'conhecido; os outros entram agora.'),
      ('Por quê', 'O acometimento cardíaco pode começar por bloqueio ou '
       'arritmia, e o ECG é a triagem; alterado, leva a ressonância ou PET. A '
       'uveíte pode ser silenciosa e deixar sinéquias, catarata e glaucoma. '
       'Creatinina e fosfatase alcalina rastreiam rim e fígado.'),
      ('O que não entra', 'Sem sintomas nem ECG alterado, a ATS sugere não '
       'fazer ecocardiograma nem Holter de rotina. PET-CT não é rastreio: serve '
       'para doença cardíaca ou para escolher onde biopsiar. Biópsia hepática '
       'não se faz para rastrear, e a enzima conversora oscila demais para guiar '
       'conduta.'),
     ]),

    pg('extensao', 'O rastreio',
       'ECG sem bloqueio nem arritmia. Fosfatase alcalina e transaminases '
       'normais. Creatinina de 1,2 mg/dL. Capacidade vital forçada de 83% e '
       'difusão de monóxido de carbono de 64% do previsto.',
       'Na consulta oftalmológica, Rafael conta que o colírio lubrificante não '
       'resolveu e que a luz do computador passou a incomodar. Na lâmpada de '
       'fenda, células 2+ na câmara anterior dos dois olhos e precipitados '
       'ceráticos grandes, sem sinéquias. Acuidade 20/25 em cada olho, pressão '
       'intraocular de 16 e 17 mmHg, fundo sem vitreíte e tomografia de '
       'coerência óptica sem edema macular.',
       'Uveíte anterior granulomatosa bilateral: colírio de prednisolona 1% e '
       'cicloplégico.'),

    Q('p7', 7,
      'A prednisona vai começar. **Quais quatro** afirmações estão corretas?', [
      ('A indicação é o cálcio com lesão renal', True),
      ('Dose inicial de 20 a 40 mg/dia', True),
      ('A uveíte segue com colírio e oftalmologia', True),
      ('Pode começar antes das culturas finais', True),
      ('Repor cálcio e vitamina D de rotina', False),
      ('Suspender quando a radiografia normalizar', False),
      ('Infliximabe como primeira linha', False),
     ], [
      ('A indicação', 'Adenopatia hilar sem sintomas muitas vezes só se '
       'acompanha. Hipercalcemia com lesão renal é indicação clara: o '
       'corticoide suprime a 1-alfa-hidroxilase do granuloma, e o cálcio '
       'costuma cair em dias.'),
      ('A dose', 'Dose moderada, em torno de 20 a 40 mg/dia de prednisona, com '
       'redução lenta. A ERS (2021) não viu benefício pulmonar acima de 20 '
       'mg/dia, e doses maiores só somam toxicidade. Infliximabe é terceira '
       'linha, depois do corticoide e do metotrexato. A meta é a função dos '
       'órgãos acometidos, não a imagem.'),
      ('O que acompanha', 'Cálcio e vitamina D de rotina, como se costuma dar '
       'com corticoide, pioram a hipercalcemia com calcitriol alto; a proteção '
       'óssea se decide caso a caso. A uveíte anterior segue com colírio e '
       'lâmpada de fenda. E o rim não espera oito semanas de cultura: começa-se '
       'agora, com alguém responsável por conferir o resultado final.'),
     ]),

    pg('evolucao2', 'Oito semanas depois',
       'Cálcio 9,8 mg/dL, creatinina 1,1 mg/dL. Culturas finais sem '
       'crescimento. A inflamação ocular está controlada e Rafael voltou a '
       'caminhar. Começa a redução da prednisona.',
       'Quatro semanas depois, durante a redução, a dor no olho direito '
       'volta. Os exames de sangue estão normais, e Rafael quer manter o '
       'esquema porque o resto melhorou.'),

    Q('p8', 8,
      'A dor ocular voltou durante a redução. Se for recidiva da uveíte, '
      '**quais duas** estratégias são as mais adequadas?', [
      ('Metotrexato como poupador de corticoide', True),
      ('Conferir adesão ao colírio e excluir infecção', True),
      ('Prednisona 40 mg/dia por tempo indefinido', False),
      ('Infliximabe antes do metotrexato', False),
      ('Suspender o sistêmico pela espirometria boa', False),
      ('Hidroxicloroquina para a uveíte', False),
     ], [
      ('A recidiva', 'Dor ocular durante a redução do corticoide é recidiva '
       'até prova em contrário. Antes de escalar, confere-se o colírio, que pode '
       'ter acabado ou sido suspenso, e se exclui infecção ocular, que imita '
       'inflamação.'),
      ('O poupador', 'Recidiva ou dependência de corticoide pede um poupador. '
       'Metotrexato é a segunda linha da ERS, com ácido fólico e controle de '
       'hemograma e função hepática. Anti-TNF vem depois dele.'),
      ('Por que não as outras', 'Prednisona alta por tempo indefinido é o que '
       'o poupador evita: osso, glicemia, catarata e glaucoma. Cada órgão tem a '
       'sua meta, e a espirometria boa não diz nada da câmara anterior. '
       'Hidroxicloroquina tem papel na pele e na hipercalcemia, não na uveíte.'),
     ]),

    bifurcacao('b2', 'Decisão', 'O olho durante a redução',
      'Como responder à volta da dor ocular?', [
      caminho('Reavaliar na oftalmologia no mesmo dia e ajustar pelo exame',
              'controle',
              'Cada órgão tem seu marcador; o do olho é a lâmpada de fenda.'),
      caminho('Manter a redução e antecipar só o cálcio e a espirometria',
              'visao',
              'Nenhum desses exames vê a câmara anterior.'),
    ]),

    pg('controle', 'No mesmo dia',
       'Células 2+ no olho direito, pressão de 18 mmHg, sem edema macular. O '
       'colírio tinha acabado havia uma semana. É recidiva anterior: o colírio '
       'é retomado e intensificado, a redução sistêmica desacelera e começa o '
       'metotrexato.',
       segue='f1'),

    pg('visao', 'Três semanas depois',
       'Rafael volta com visão turva no olho direito. Acuidade 20/80, células '
       '3+, sinéquias posteriores novas, pressão de 28 mmHg e edema macular na '
       'tomografia de coerência óptica.',
       segue='b_resgate'),

    bifurcacao('b_resgate', 'Decisão', 'Edema macular e pressão alta',
      'Qual resgate organizar?', [
      caminho('Oftalmologia urgente: controlar inflamação e pressão, com '
              'tratamento local e sistêmico', 'resgate',
              'Edema macular ameaça a visão central e pede tratamento '
              'dirigido.'),
      caminho('Só colírio hipotensor e aguardar', 'resgate_tardio',
              'A pressão é parte do problema; a inflamação e o edema '
              'continuam.'),
    ]),

    pg('resgate', 'Duas semanas depois',
       'Pressão de 18 mmHg e acuidade 20/40, com edema em regressão. A recidiva '
       'grave antecipa o metotrexato.',
       segue='f1b'),

    pg('resgate_tardio', 'Uma semana depois',
       'A pressão caiu, mas a dor e o borramento continuam: células e edema '
       'macular seguem ativos. O resgate integrado começa com uma semana de '
       'atraso.',
       segue='f2'),

    fim('f1', 'Controle com visão preservada',
        'Com metotrexato, a prednisona chega a 5 mg/dia em seis meses. Cálcio e '
        'creatinina normais, visão 20/20, espirometria estável.',
        'O tecido veio antes do corticoide, cada órgão foi examinado com o seu '
        'instrumento, e a recidiva ocular foi vista no dia em que apareceu.',
        'melhor'),

    fim('f1b', 'Controle após recidiva grave',
        'A visão do olho direito volta a 20/25 em três meses. Metotrexato '
        'mantido, prednisona em redução.',
        'O resgate imediato do edema macular preservou a visão, mas a '
        'recidiva grave poderia ter sido vista três semanas antes.', 'medio'),

    fim('f2', 'Perda visual residual',
        'A inflamação e a pressão estão controladas, mas a acuidade direita '
        'estabiliza em 20/50, com alterações maculares documentadas.',
        'Tratar só a pressão deixou o edema macular ativo por mais uma '
        'semana.', 'pior'),

    pagina('retrospectiva', 'Pontos de ensino', '',
        pontos(
            'Na hipercalcemia, o primeiro divisor é o PTH. Suprimido, manda '
            'procurar PTHrP, as duas formas da vitamina D, paraproteína e '
            'imagem; sestamibi não tem lugar.',
            'Urina diluída com sódio alto num paciente desidratado é defeito de '
            'concentração: a hipercalcemia causa diabetes insípido nefrogênico '
            'e lesão pré-renal, e o volume vem antes de qualquer diurético.',
            '1,25-di-hidroxivitamina D alta com 25-hidroxi normal indica '
            'calcitriol produzido fora do rim, por granuloma ou linfoma. '
            'Tiazídico e suplemento de vitamina D descompensam essa produção.',
            'Adenopatia mediastinal com suspeita de linfoma pede tecido antes do '
            'corticoide; a ecobroncoscopia colhe histologia, citometria e '
            'culturas de uma vez.',
            'Granuloma não necrosante é padrão, não diagnóstico: a sarcoidose '
            'exige quadro compatível, tecido e exclusão de micobactéria, fungo '
            'e linfoma.',
            'Ao diagnóstico, todos fazem ECG, exame oftalmológico, cálcio, '
            'creatinina e fosfatase alcalina. A uveíte pode estar lá sem queixa, '
            'ou escondida num colírio lubrificante.'),
        so_kicker=True),

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
       + _fonte(IMG / 'granuloma.jpg.json', 'granuloma') + ').'),
]

REVISAO = []

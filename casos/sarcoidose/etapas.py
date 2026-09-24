"""Sarcoidose com hipercalcemia por calcitriol, lesão renal e uveíte anterior.

Alíquota → pergunta, no molde dos casos interativos do //New England//. Oito
perguntas no percurso, uma rodada de exames com gabarito e painel, um
pareamento dos mecanismos de hipercalcemia e duas decisões de conduta com
consequência. Paciente ficcional.
"""
from pathlib import Path

from motor.estudo_imagem import estudo

from motor.etapas import (alt, bifurcacao, caminho, capa, desfecho, op, p,
                          pagina, painel, par, pareamento, pergunta, tabela,
                          topicos, vitais, lamina)
from casos.novos import imagem, referencia_imagem

TITULO = 'Entre a sede e o fôlego'
RODAPE = 'Paciente ficcional · evoluções simuladas para ensino'
COR = '#0d9488'
IMG = Path(__file__).parent / 'img'
BANCO = []
CENA = 'cena.png'


def pg(k, titulo, *textos, segue=''):
    return pagina(k, titulo, '', *(p(t) for t in textos), so_kicker=True, segue=segue)


def Q(k, n, enunciado, itens, titulo, segue=''):
    return pergunta(k, f'Pergunta {n}', enunciado,
                    [alt(t, c, certa=ok) for t, c, ok in itens],
                    titulo_resposta=titulo, segue=segue)


def ex(nome, valor, ref='—', alt_=False):
    return op(nome, resultado=valor, referencia=ref, alterado=alt_)


def fim(k, titulo, texto, porque, qualidade):
    return desfecho(k, titulo, p(texto), qualidade=qualidade, porque=porque,
                    fecho='retrospectiva')


def sem_setas(meta):
    return referencia_imagem(meta).replace(
        'Setas editoriais sob a mesma licença; arquivo sem recorte adicional.',
        'Sem setas ou recorte adicional.')


ETAPAS = [
    capa(TITULO, fundo=CENA, kicker='Caso interativo',
         selo='Paciente ficcional · procedência e créditos na última tela'),

    pg('historia', 'Apresentação',
       'Rafael, 41 anos, analista administrativo, é trazido pela esposa ao '
       'pronto-socorro por náuseas, intestino preso há cinco dias e '
       'dificuldade para se concentrar. Há uma semana bebe água o tempo todo e '
       'acorda três vezes à noite para urinar.',
       'Antes disso, vinha encurtando as caminhadas do fim de semana por '
       'cansaço. Atribuiu ao trabalho — e a uma tosse seca que começou há '
       'dois meses e vai e volta.'),

    pg('hda', 'História da doença atual',
       'A tosse não tem catarro nem sangue. Subir dois lances de escada deixa '
       'Rafael sem fôlego, sem ortopneia e sem dor no peito. Não mediu febre. '
       'Perdeu 4 kg em oito semanas. A sede veio antes das náuseas.',
       'Nega vômitos repetidos, diarreia e cólica renal. Não teve desmaio nem '
       'palpitação. Os olhos, diz, "às vezes ardem com a luz do computador".'),

    pg('antecedentes', 'Antecedentes e exposições',
       'Hipertenso há cinco anos, usa **hidroclorotiazida 25 mg/dia**. Há três '
       'meses, por conta própria, começou **colecalciferol 5.000 UI/dia** '
       'porque ouviu que "dava disposição". Não usa carbonato de cálcio, lítio '
       'ou antiácido.',
       'Nunca teve cálculo renal. Trabalha em escritório; nega corte de '
       'pedra, jateamento de areia, fundição e contato com berílio. Não fuma. '
       'Não conhece contato com tuberculose e nunca viajou para fora do '
       'Nordeste.'),

    pagina('exame', 'Exame físico', '',
           vitais(('Pressão arterial', '104/66', True), ('Frequência cardíaca', '102', True),
                  ('Frequência respiratória', '20', False), ('Temperatura', '36,8 °C', False),
                  ('SpO₂ em ar ambiente', '95%', False)),
           topicos(('Estado geral', 'Desidratado, orientado, com atenção lenta; sem déficit focal.'),
                   ('Cardiovascular', 'Ritmo regular, sem sopros, sem turgência jugular.'),
                   ('Respiratório', 'Murmúrio presente, **raros estertores finos** bilaterais.'),
                   ('Abdome', 'Ruídos diminuídos, indolor, sem massas.'),
                   ('Olhos', 'Hiperemia ciliar discreta nos dois olhos, pupilas reagentes.'),
                   ('Pele e membros', 'Sem edema, sem lesões cutâneas, sem sinovite.')),
           so_kicker=True),

    painel('res0', 'Na chegada', 'A bancada da emergência', [
        ex('Cálcio total', '13,6 mg/dL', '8,5–10,5 mg/dL', True),
        ex('Albumina', '4,0 g/dL', '3,5–5,0 g/dL'),
        ex('Cálcio ionizado', '1,72 mmol/L', '1,12–1,32 mmol/L', True),
        ex('Creatinina', '2,0 mg/dL {{(1,0 há um ano)}}', '0,7–1,3 mg/dL', True),
        ex('Ureia', '72 mg/dL', '15–45 mg/dL', True),
        ex('Sódio / potássio', '143 / 3,5 mmol/L', '135–145 / 3,5–5,0'),
        ex('Hemoglobina', '12,8 g/dL', '13,5–17,5 g/dL', True),
        ex('Eletrocardiograma', 'Ritmo sinusal, 102 bpm · QT corrigido curto (360 ms)', '—', True),
    ], introducao='A equipe colhe bioquímica, gasometria venosa e ECG antes de qualquer outra coisa.'),

    Q('p1', 1,
      'Cálcio de 13,6 mg/dL, sintomas neurológicos e creatinina que dobrou. '
      '**Quais três** medidas são prioritárias agora?', [
      ('Soro fisiológico com meta de diurese',
       'Hipercalcemia faz diabetes insípido nefrogênico, e o paciente '
       'desidratado não excreta cálcio. Volume é o primeiro tratamento.',
       True),
      ('Furosemida antes de repor volume',
       'Aumenta a calciúria só depois que o volume foi restaurado; antes '
       'disso, piora a desidratação e o rim.', False),
      ('Suspender tiazídico e colecalciferol',
       'O tiazídico reduz a excreção de cálcio; a vitamina D aumenta a '
       'absorção. Os dois contribuem, mesmo que não expliquem tudo.', True),
      ('Dosar o paratormônio com o cálcio',
       'É a bifurcação de toda hipercalcemia: PTH alto ou inapropriado de um '
       'lado, PTH suprimido do outro.', True),
      ('Hemodiálise de urgência pela creatinina',
       'Reservada para hipercalcemia grave refratária, com insuficiência '
       'renal que não permite volume. Não é o caso ainda.', False),
      ('Restrição hídrica pela poliúria',
       'A poliúria é consequência, não causa. Restringir água piora tudo.',
       False),
      ('Dieta rica em cálcio para "equilibrar"',
       'Não tem racional nenhum.', False),
      ('Gluconato de cálcio pelo QT curto',
       'O QT curto é do cálcio alto. Dar cálcio seria absurdo.', False),
     ], 'Volume, retirar o que soma, e a pergunta do PTH'),

    pg('evolucao1', 'Primeiras 24 horas',
       'Com soro e sem as duas medicações, Rafael fica mais atento. O cálcio '
       'cai para 12,4 mg/dL e a creatinina para 1,6 mg/dL. **O PTH é 6 '
       'pg/mL** (referência 15–65).',
       'A melhora parcial não explica a causa. A tosse, a perda de peso e o '
       'fôlego curto continuam sem dono.'),

    Q('ex2', 2,
      'Hipercalcemia com **PTH suprimido**. **Quais quatro** exames são os '
      'mais apropriados agora?', [
      ('Peptídeo relacionado ao PTH (PTHrP)',
       'É o mediador da hipercalcemia humoral maligna, a causa mais comum de '
       'hipercalcemia grave em internados.', True),
      ('Cintilografia com sestamibi das paratireoides',
       'Localiza adenoma em hiperparatireoidismo — que um PTH de 6 exclui.',
       False),
      ('25-hidroxivitamina D e 1,25-di-hidroxivitamina D',
       'A primeira mede estoque (intoxicação); a segunda, a forma ativa, que '
       'granuloma e linfoma produzem fora do rim.', True),
      ('Eletroforese de proteínas com cadeias leves livres',
       'Mieloma faz hipercalcemia por osteólise, com PTH baixo e lesão '
       'renal. Não se deixa de fora.', True),
      ('Radiografia de tórax',
       'A tosse, a perda de peso e os estertores pedem imagem — e o tórax é '
       'onde moram granulomas, linfomas e carcinomas.', True),
      ('Densitometria óssea',
       'Não investiga a causa da hipercalcemia.', False),
      ('Enzima conversora da angiotensina como teste diagnóstico',
       'Sensibilidade e especificidade baixas. Não confirma nem exclui '
       'sarcoidose.', False),
      ('Calcitonina sérica',
       'Marcador de carcinoma medular de tireoide; não explica hipercalcemia.',
       False),
      ('Ultrassonografia cervical das paratireoides',
       'Mesma lógica do sestamibi: sem PTH, não há o que procurar.', False),
     ], 'PTH baixo manda procurar PTHrP, vitamina D, paraproteína e o tórax'),

    painel('res2', 'Investigação', 'O que a equipe pediu', [
        ex('PTHrP', 'Não detectado', 'não detectado'),
        ex('25-hidroxivitamina D', '38 ng/mL', '20–50 ng/mL'),
        ex('1,25-di-hidroxivitamina D', '104 pg/mL', '18–72 pg/mL', True),
        ex('Eletroforese de proteínas', 'Sem componente monoclonal · gamaglobulina policlonal discretamente elevada', 'sem pico'),
        ex('Cadeias leves livres', 'Relação kappa/lambda 1,3', '0,26–1,65'),
        ex('Fósforo', '3,6 mg/dL', '2,5–4,5 mg/dL'),
        ex('Calciúria de 24 horas', '410 mg', 'abaixo de 300 mg', True),
        ex('Radiografia de tórax', 'Alargamento hilar bilateral e simétrico · parênquima sem consolidação', '—', True),
    ], introducao='Clique na imagem para ampliar; o laudo abre no botão.',
       laminas={'Radiografia de tórax': lamina('rx_hilos.jpg', 'Radiografia de tórax, PA e perfil',
                'Imagem de outro paciente, usada para ilustrar o achado; não pertence a Rafael.',
                'Hellerhoff · Wikimedia Commons · CC BY-SA 4.0')}),

    pareamento('p3', 'Pergunta 3',
      'O 1,25-di-hidroxivitamina D está alto e o 25-hidroxi normal. Associe '
      'cada perfil laboratorial ao mecanismo da hipercalcemia.', [
      par('PTH alto, fósforo baixo', 'Hiperparatireoidismo primário',
          'O PTH aumenta a reabsorção de cálcio e a perda de fósforo. É a '
          'causa mais comum no ambulatório.'),
      par('PTH baixo, PTHrP alto, 1,25-(OH)₂D baixo',
          'Hipercalcemia humoral maligna',
          'Carcinoma escamoso, renal ou de mama. O PTHrP imita o PTH no '
          'osso e no rim, mas não ativa a vitamina D.'),
      par('PTH baixo, 1,25-(OH)₂D alto, 25-OH-D normal',
          'Produção extrarrenal de calcitriol (granuloma, linfoma)',
          'É o de Rafael. O macrófago do granuloma tem 1-alfa-hidroxilase '
          'própria, que não obedece ao PTH nem ao cálcio.'),
      par('PTH baixo, 25-OH-D acima de 150 ng/mL',
          'Intoxicação por vitamina D',
          'Exige doses de dezenas de milhares de unidades por meses. Os '
          '5.000 UI/dia de Rafael não chegam lá — e o 25-OH dele é 38.'),
      par('PTH baixo, pico monoclonal, lesões líticas',
          'Mieloma múltiplo',
          'Osteólise local por citocinas. A eletroforese e as cadeias leves '
          'dele são normais.'),
    ], opcoes=['Hiperparatireoidismo primário', 'Hipercalcemia humoral maligna',
               'Produção extrarrenal de calcitriol (granuloma, linfoma)',
               'Intoxicação por vitamina D', 'Mieloma múltiplo',
               'Síndrome leite-álcali'],
    titulo_resposta='O calcitriol alto com estoque normal aponta para fora do rim',
    nota='A opção que sobrou, síndrome leite-álcali, teria alcalose e história '
         'de carbonato de cálcio.'),

    estudo('rx_hilos', 'Radiografia de tórax',
           'Com o calcitriol alto, a equipe volta à radiografia. Observe os '
           'hilos nas incidências frontal e lateral antes de ler a descrição.',
           IMG / 'rx_hilos.jpg',
           'Radiografia frontal e lateral de outro paciente · comparação didática.',
           referencia_imagem(IMG / 'rx_hilos.jpg.json'),
        [
         ((176, 280), (70, 180), '**Hilo direito** aumentado, de contorno lobulado.', 12),
         ((353, 273), (470, 180), '**Hilo esquerdo** também aumentado: a adenopatia é bilateral e simétrica.', -12),
         ((735, 315), (900, 240), 'Na incidência lateral, a **massa hilar** se sobrepõe à sombra cardíaca.', 12),
        ],
        ['Adenopatia hilar bilateral e simétrica, com parênquima pulmonar sem opacidades: estágio I de Scadding.', 'Linfoma e tuberculose voltam ao diferencial quando a adenopatia é assimétrica ou quando a tomografia mostra necrose.']),

    pg('tomografia', 'Tomografia de tórax',
       'O laudo descreve **linfonodos hilares e mediastinais bilaterais, '
       'simétricos**, sem necrose central, e **pequenos nódulos em '
       'distribuição perilinfática** — ao longo dos feixes '
       'broncovasculares, das fissuras e da pleura. Sem cavitação e sem '
       'derrame.'),

    Q('p4', 4,
      'Linfonodos hilares bilaterais simétricos e micronódulos '
      'perilinfáticos, com calcitriol alto. **Quais quatro** diagnósticos '
      'precisam ser considerados?', [
      ('Sarcoidose', 'O padrão radiológico mais típico, com o metabolismo do '
       'cálcio a favor.', True),
      ('Tuberculose', 'Faz granuloma, linfonodo mediastinal e, raramente, '
       'produz calcitriol. No Brasil não se imunossuprime sem excluí-la.',
       True),
      ('Pneumonia bacteriana', 'Não produz linfonodo bilateral simétrico nem '
       'micronódulo perilinfático, e não há febre.', False),
      ('Linfoma', 'Linfonodo mediastinal, perda de peso e calcitriol alto: o '
       'linfoma produz 1-alfa-hidroxilase como o granuloma.', True),
      ('Histoplasmose ou outra micose endêmica', 'Granulomatosa, com '
       'linfonodo mediastinal e, às vezes, hipercalcemia. Pergunta-se pela '
       'caverna e pelo galinheiro.', True),
      ('Silicose', 'Faz linfonodo hilar com calcificação em casca de ovo e '
       'nódulo nos lobos superiores — mas ele nunca trabalhou com sílica.',
       False),
      ('Edema pulmonar cardiogênico', 'Nem linfonodo nem nódulo '
       'perilinfático, e o coração dele é normal.', False),
      ('Beriliose crônica', 'É indistinguível da sarcoidose, na imagem e na '
       'lâmina — mas exige exposição ao berílio, que ele não tem.', False),
      ('Tromboembolismo pulmonar', 'Não produz linfonodo.', False),
     ], 'Granuloma, micobactéria, fungo e linfoma — e a história de exposição tira dois'),

    bifurcacao('b1', 'Decisão', 'Como chegar ao tecido',
      'Rafael está estável depois da hidratação, sem ameaça respiratória. '
      'Como conduzir a definição etiológica?', [
      caminho('Ecobroncoscopia com punção dos linfonodos (EBUS), com '
              'histologia e culturas', 'tecido',
              'Chega aos linfonodos mediastinais sem cirurgia e colhe material '
              'para micobactéria e fungo antes de imunossuprimir.'),
      caminho('Iniciar prednisona sem amostra e considerar a resposta como '
              'confirmação', 'empirico',
              'Sarcoidose, linfoma e até tuberculose podem melhorar por '
              'semanas com corticoide.'),
      caminho('Atribuir tudo ao suplemento e observar', 'suplemento',
              'O colecalciferol soma, mas não produz linfonodo nem '
              'calcitriol alto com 25-OH normal.'),
    ]),

    pg('empirico', 'Dez dias de prednisona',
       'O cálcio cai e a tosse melhora. Mas ninguém excluiu tuberculose nem '
       'linfoma, e a pneumologia recusa-se a manter o corticoide sem tecido. '
       'O EBUS é feito com o paciente já sob prednisona; o patologista é '
       'avisado.',
       segue='tecido'),

    pg('suplemento', 'Uma semana depois',
       'Sem suplemento e sem tiazídico, o cálcio volta a **13,1 mg/dL**. '
       'Rafael retorna com dor nos olhos e fotofobia. É readmitido, hidratado '
       'de novo e avaliado pela oftalmologia no mesmo dia; o EBUS é marcado '
       'para depois da estabilização.',
       segue='tecido'),

    pg('tecido', 'O EBUS',
       'Punções dos linfonodos subcarinal e hilar direito mostram '
       '**granulomas não necrosantes**, compactos, sem células malignas. '
       'Colorações para bacilo álcool-ácido resistente e fungos e o teste '
       'molecular para tuberculose são negativos; as culturas seguem em '
       'incubação por seis a oito semanas.'),

    estudo('granuloma', 'Granuloma pulmonar',
           'Compare com esta microfotografia de tecido pulmonar de outro '
           'paciente. Descreva o granuloma antes de ler a interpretação.',
           IMG / 'granuloma.jpg',
           'Tecido pulmonar de outro paciente · comparação morfológica.',
           referencia_imagem(IMG / 'granuloma.jpg.json'),
        [
         ((420, 330), (330, 55), '**Histiócitos epitelioides**: citoplasma amplo e pálido, núcleo oval, agrupados de forma compacta.', -12),
         ((500, 628), (330, 700), '**Coroa de linfócitos**, pequenos e escuros, na periferia do granuloma.', 12),
         ((540, 470), (800, 670), '**Centro celular, sem necrose**: é o que define o granuloma como não necrosante.', 12),
        ],
        ['Granuloma não necrosante: agregado compacto de histiócitos epitelioides com coroa linfocitária, sem necrose central.', 'Descreve morfologia, não causa. Não exclui micobactéria nem fungo: o diagnóstico junta lâmina, cultura e exposição.']),

    Q('p5', 5,
      'Granulomas não necrosantes no EBUS, com BAAR, fungos e teste '
      'molecular negativos e culturas pendentes. Qual a interpretação mais '
      'adequada?', [
      ('Tuberculose está excluída: o teste molecular é suficientemente sensível',
       'Em doença paucibacilar a sensibilidade cai muito. O negativo reduz, '
       'não zera.', False),
      ('Sarcoidose provável, até as culturas finais',
       'Apresentação compatível, granuloma não necrosante e exclusão '
       'razoável de alternativas: é a definição da ATS. As culturas fecham '
       'a exclusão.', True),
      ('A ausência de necrose exclui micobactéria e fungo',
       'Há sobreposição morfológica. Histoplasmose pode ter granuloma sem '
       'necrose.', False),
      ('O granuloma confirma sarcoidose e dispensa as culturas',
       'Granuloma é um padrão de resposta, não uma doença.', False),
      ('É preciso biópsia pulmonar cirúrgica antes de qualquer conduta',
       'O EBUS rendeu. Cirurgia só se o quadro divergir.', False),
     ], 'Granuloma é padrão; o diagnóstico é integração'),

    pg('ocular', 'Avaliação oftalmológica',
       'Na lâmpada de fenda: **células 2+ na câmara anterior dos dois olhos** '
       'e precipitados ceráticos, sem sinéquias. Acuidade 20/25 em cada olho. '
       'Pressão intraocular 16 e 17 mmHg. Fundo de olho sem vitreíte; '
       'tomografia de coerência óptica sem edema macular.',
       'Uveíte anterior bilateral, sem ameaça macular. O oftalmologista '
       'inicia colírio de corticoide e cicloplégico.'),

    Q('p6', 6,
      'Sarcoidose com pulmão, linfonodo, cálcio, rim e olho. **Quais três** '
      'avaliações de outros órgãos são recomendadas para todo paciente ao '
      'diagnóstico?', [
      ('Eletrocardiograma de 12 derivações',
       'O coração é o órgão que mata na sarcoidose. O ECG é a triagem; '
       'bloqueio ou arritmia levam à ressonância.', True),
      ('Ressonância cardíaca de rotina em todos',
       'Sem sintoma e com ECG normal, não é recomendada de rotina.', False),
      ('Exame oftalmológico com lâmpada de fenda',
       'Uveíte pode ser assintomática e cegar. Todos examinam, com ou sem '
       'queixa.', True),
      ('Cálcio, creatinina e fosfatase alcalina',
       'Rastreiam hipercalcemia, lesão renal e acometimento hepático.', True),
      ('PET-CT de corpo inteiro para todos',
       'Não é rastreio. Serve em situações específicas — doença cardíaca, '
       'escolher o sítio de biópsia.', False),
      ('Biópsia hepática',
       'Fosfatase alcalina normal não pede biópsia.', False),
      ('Holter de 24 horas em assintomáticos',
       'Guiado por sintomas ou ECG alterado, não de rotina.', False),
      ('Enzima conversora seriada para monitorar',
       'Oscila e não guia tratamento com confiança.', False),
     ], 'Coração, olho e o metabolismo — em todos'),

    pg('extensao', 'Outros órgãos',
       'ECG sem bloqueio nem arritmia. Fosfatase alcalina e transaminases '
       'normais. Creatinina 1,5 mg/dL, sedimento sem cilindros. Capacidade '
       'vital forçada 83% e difusão de monóxido de carbono 64% do previsto.'),

    estudo('rx_tc', 'Sarcoidose avançada',
           'Outro paciente, com sarcoidose pulmonar avançada. Não é a '
           'tomografia de Rafael — é o que a doença pode fazer quando '
           'progride no parênquima.',
           IMG / 'rx_tc.jpg',
           'Radiografia e TC coronal de outro paciente · doença parenquimatosa avançada.',
           referencia_imagem(IMG / 'rx_tc.jpg.json'),
        [
         ((360, 110), (470, 35), '**Opacidades reticulonodulares** densas, que predominam nos campos superiores.', -12),
         ((665, 240), (575, 420), 'Na TC coronal, **conglomerado peri-hilar** com espessamento peribroncovascular.', 12),
         ((905, 170), (985, 60), '**Micronódulos** difusos, de distribuição perilinfática.', -12),
        ],
        ['Doença parenquimatosa extensa, com predomínio superior e peri-hilar e conglomerados: o estágio IV de Scadding, a fibrose.', 'O que se trata é a inflamação antes dela; fibrose não volta.']),

    Q('p7', 7,
      'A prednisona vai começar. **Quais três** afirmações estão corretas?', [
      ('A indicação é o cálcio com lesão renal',
       'Adenopatia hilar isolada muitas vezes se observa. Cálcio e rim são '
       'indicação clara.', True),
      ('Cálcio e vitamina D devem ser repostos pelo corticoide, como de rotina',
       'Com calcitriol alto, reposição automática piora a hipercalcemia. A '
       'proteção óssea é individual.', False),
      ('A uveíte segue com colírio',
       'O corticoide sistêmico não substitui o colírio nem o seguimento '
       'ocular.', True),
      ('Dose inicial de 20 a 40 mg/dia',
       'A ERS sugere dose moderada: doses altas não são mais eficazes e '
       'cobram mais toxicidade.', True),
      ('Suspender quando a radiografia normalizar',
       'A meta é a função dos órgãos, não a imagem.', False),
      ('Infliximabe como primeira linha, pela gravidade',
       'É terceira linha, depois do corticoide e do metotrexato.', False),
      ('Pode começar antes das culturas finais',
       'O risco renal não espera oito semanas. Começa-se com um responsável '
       'por conferir as culturas.', True),
     ], 'Trata-se o órgão ameaçado, em dose moderada, olhando cada um'),

    pg('evolucao2', 'Oito semanas depois',
       'Cálcio 9,8 mg/dL, creatinina 1,1 mg/dL. Culturas finais sem '
       'crescimento. A inflamação ocular está controlada e Rafael voltou a '
       'caminhar. Começa a redução da prednisona.',
       'Quatro semanas depois, durante a redução, a dor no olho direito '
       'volta. Os exames de sangue estão normais, e Rafael quer manter o '
       'esquema porque "o resto melhorou".'),

    Q('p8', 8,
      'A dor ocular voltou durante a redução. Se for recidiva da uveíte, '
      '**quais duas** estratégias são as mais adequadas?', [
      ('Metotrexato como poupador de corticoide',
       'É a segunda linha da ERS na sarcoidose que recidiva ou exige dose '
       'alta prolongada — com ácido fólico, função hepática e renal.', True),
      ('Manter prednisona 40 mg/dia por tempo indeterminado',
       'A toxicidade cumulativa — osso, glicemia, catarata, glaucoma — é '
       'o preço que o poupador existe para evitar.', False),
      ('Revisar adesão aos colírios e excluir infecção antes de escalonar',
       'Recidiva também é colírio que acabou, ou uma infecção que imita a '
       'sarcoidose.', True),
      ('Iniciar infliximabe antes de tentar metotrexato',
       'Anti-TNF é terceira linha, depois de corticoide e metotrexato.',
       False),
      ('Suspender o sistêmico porque a espirometria melhorou',
       'Cada órgão tem a sua meta. O olho está ativo.', False),
      ('Hidroxicloroquina para a uveíte',
       'Tem papel em pele e hipercalcemia; não controla uveíte.', False),
     ], 'Poupar corticoide, mas primeiro conferir o colírio'),

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
       'Células 2+ no olho direito, pressão 18 mmHg, sem edema macular. '
       'Recidiva anterior. O colírio é intensificado, a redução sistêmica '
       'desacelera, e começa o metotrexato.',
       segue='f1'),

    pg('visao', 'Três semanas depois',
       'Rafael volta com visão turva no olho direito. Acuidade 20/80, células '
       '3+, **sinéquias posteriores novas**, pressão de 28 mmHg e **edema '
       'macular** na tomografia de coerência óptica.',
       segue='b_resgate'),

    bifurcacao('b_resgate', 'Decisão', 'Edema macular e pressão alta',
      'Qual resgate organizar?', [
      caminho('Oftalmologia urgente: controlar inflamação e pressão, com '
              'tratamento local e sistêmico', 'resgate',
              'Edema macular é ameaça à visão central e pede tratamento '
              'dirigido.'),
      caminho('Só colírio hipotensor e aguardar', 'resgate_tardio',
              'A pressão é parte do problema; a inflamação e o edema '
              'continuam.'),
    ]),

    pg('resgate', 'Duas semanas depois',
       'Pressão 18 mmHg e acuidade 20/40, com edema em regressão. A recidiva '
       'grave acelera o metotrexato.',
       segue='f1b'),

    pg('resgate_tardio', 'Uma semana depois',
       'A pressão caiu, mas a dor e o borramento continuam: células e edema '
       'macular seguem ativos. O resgate integrado começa com uma semana de '
       'atraso.',
       segue='f2'),

    fim('f1', 'Controle com visão preservada',
        'Com metotrexato, a redução da prednisona chega a 5 mg/dia em seis '
        'meses. Cálcio e creatinina normais, visão 20/20, espirometria '
        'estável.',
        'Cada órgão foi examinado com o seu instrumento, e a recidiva ocular '
        'foi vista no dia em que apareceu.', 'melhor'),

    fim('f1b', 'Controle após recidiva grave',
        'A visão do olho direito volta a 20/25 em três meses. Metotrexato '
        'mantido, prednisona em redução.',
        'O resgate imediato do edema macular preservou a visão, mas a '
        'recidiva grave poderia ter sido vista três semanas antes.', 'medio'),

    fim('f2', 'Perda visual residual',
        'A inflamação e a pressão estão controladas, mas a acuidade direita '
        'estabiliza em 20/50, com alterações maculares documentadas.',
        'Tratar só a pressão deixou o edema macular ativo por mais uma '
        'semana. A lesão foi documentada no seguimento, não presumida.', 'pior'),

    pagina('retrospectiva', 'Retrospectiva', '',
        tabela(['Momento', 'O dado', 'O que decidiu'], [
            ['Na emergência', 'Cálcio 13,6, creatinina dobrada, QT curto',
             'Volume antes de diurético; tirar tiazídico e vitamina D'],
            ['Primeiras 24 h', 'PTH 6 pg/mL', 'A pergunta passa a ser: PTHrP, vitamina D, paraproteína, tórax'],
            ['Investigação', '1,25-(OH)₂D alto, 25-OH normal, hilos bilaterais',
             'Calcitriol produzido fora do rim — granuloma ou linfoma'],
            ['EBUS', 'Granuloma não necrosante, culturas pendentes',
             'Sarcoidose provável, tratada pelo rim e pelo cálcio'],
            ['Redução', 'Dor ocular com exames de sangue normais',
             'O olho se examina com lâmpada de fenda, não com cálcio'],
        ]),
        so_kicker=True),

    pg('referencias', 'Fontes e limites',
       'Caso autoral e ficcional; valores, intervalos e desfechos simulados.',
       'Crouser e cols. Diagnosis and detection of sarcoidosis, ATS 2020. '
       'Baughman e cols. ERS clinical practice guidelines on treatment of '
       'sarcoidosis, 2021. Herbort e cols. IWOS 2021 — sarcoidose ocular. '
       'Imagens de outros pacientes: Hellerhoff (CC BY-SA 4.0) e Yale Rosen '
       '(CC BY-SA 2.0), Wikimedia Commons. Cena: ilustração gerada por IA.'),
]

REVISAO = []

"""O caso pulmão-rim, no molde do //New England// lido em 26/09/2026.

Reescrito no desenho do piloto da leptospirose (ver
Artifacts/nejm-casos-classicos/GRAMATICA_LIDA_2026-09-26.md): apresentação
curta, ficha do paciente com a pista enterrada (a urina e a creatinina do
ambulatório de seis semanas antes), exame físico por sistema e os primeiros
exames entregues prontos, sem pergunta antes. As primeiras perguntas
interpretam números (gasometria, tipo de lesão renal) e testam a âncora da
equipe: pneumonia multilobar com glomerulonefrite associada à infecção,
endocardite a afastar. A âncora é correta naquele momento. O caso vira no
quinto dia, com as culturas negativas e o reexame (púrpura, pé caído); o
mecanismo vem por categoria (pauci-imune) e o nome da doença só aparece com o
anticorpo, depois de 60% do percurso. Cada pergunta tem uma explicação só, em
seções com subtítulo. As três decisões de conduta e o balanço continuam.

Paciente ficcional. Os números fecham entre si: gasometria por
Henderson-Hasselbalch, filtração por CKD-EPI 2021, hiato aniônico corrigido
pela albumina, FENa pelos valores do painel. Condutas: KDIGO 2024 (vasculite
associada ao ANCA), EULAR 2022, PEXIVAS, CYCLOPS, RAVE, RITUXVAS.
"""

from pathlib import Path

from motor.estudo_imagem import estudo
from motor.etapas import (
    alt, balanco, bifurcacao, caminho, capa, consequencia, desfecho, grade,
    lamina, op, p, pagina, painel, par, pareamento, pergunta, pontos, quadro,
    tabela, topicos, vitais,
)

from .banco import BANCO  # noqa: F401  (a gaveta de exames é a mesma)

TITULO = "O sangue que não saiu"
RODAPE = "Caso interativo · curso simulado"
COR = '#e11d48'
IMG = Path(__file__).parent / "img"
MOLDE = 'nejm'

CENA = "cena_admissao.jpg"


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


# ═════════════════ o que é comum aos três esquemas de indução ═══════════════

def _esquema_comum():
    glicocorticoide = quadro("O glicocorticoide, igual nos três caminhos",
        p("Metilprednisolona 500 mg/dia por três dias, depois prednisona, "
          "**75 mg/dia** pela faixa de peso acima de 75 kg. No PEXIVAS (2020), "
          "o **desmame reduzido**, com pouco mais da metade da dose acumulada "
          "em seis meses, não foi inferior e reduziu as infecções graves no "
          "primeiro ano."),
        sistema="geral")
    plasma = quadro("Troca plasmática: uma decisão em disputa",
        p("O PEXIVAS não mostrou redução de morte ou de doença renal terminal "
          "em 704 pacientes. A KDIGO 2024 sugere considerá-la com creatinina "
          "acima de 3,4 mg/dL (300 µmol/L), e ele está em **4,6 mg/dL (407 "
          "µmol/L)**, ou na hemorragia alveolar com hipoxemia. Aqui ela é "
          "discutível, e não está descartada."),
        sistema="sangue")
    avacopan = quadro("Avacopan, e por que ele não entra aqui",
        p("O ADVOCATE (2021) mostrou **superioridade na remissão sustentada em "
          "52 semanas**, poupando glicocorticoide. É adjuvante da indução, não "
          "substituto, e o limite aqui é a disponibilidade."),
        sistema="geral")
    cerco = quadro("Antes da primeira dose, e depois dela",
        p("Antes: HBsAg e anti-HBc, anti-HCV e anti-HIV; ivermectina 200 "
          "µg/kg por dois dias. Depois: sulfametoxazol-trimetoprima **400/80 "
          "mg três vezes por semana**, meia dose pela filtração, com o potássio "
          "vigiado: ele chegou com 5,4. Cálcio, vitamina D e hemograma "
          "semanal."),
        sistema="pulmao")
    return glicocorticoide + plasma, avacopan + cerco


def fim(k, titulo, *textos, porque, qualidade):
    return desfecho(k, titulo, *(p(t) for t in textos), qualidade=qualidade,
                    porque=porque, fecho='retrospectiva')


ETAPAS = [

    capa(TITULO, fundo=CENA,
         kicker="Caso interativo · 8 perguntas · 3 decisões",
         selo="Paciente ficcional · procedência e créditos na última tela"),

    # ═══════════════════════════ a abertura ═══════════════════════════

    pg('historia', 'Apresentação',
       'Um homem de 63 anos é trazido pela esposa ao pronto-socorro com falta '
       'de ar em repouso e sangue vivo no escarro. Oito semanas antes '
       'surgiram obstrução nasal e secreção espessa, tratadas na unidade '
       'básica como rinossinusite: amoxicilina por dez dias e, quatro semanas '
       'depois, amoxicilina-clavulanato por catorze, sem melhora. Vieram '
       'depois dores articulares que mudavam de lugar, febre no fim da tarde, '
       'suor noturno e 6 kg a menos.',
       'Há duas semanas começou tosse com raias de sangue; numa emergência, a '
       'radiografia de tórax foi lida como normal e ele saiu com '
       'antitussígeno. Na última semana a urina ficou escura, cor de '
       'refrigerante de cola, e ele deixou de levantar à noite para urinar. A '
       'falta de ar piorou nos últimos três dias, e hoje ele expectorou cerca '
       'de 50 mL de sangue.',
       'Nega dor torácica, ortopneia, inchaço nas pernas, dor ao urinar, '
       'vômitos, diarreia e uso de anti-inflamatório.'),

    pagina('ficha', 'Ficha do paciente', '',
           topicos(('Antecedentes', 'Hipertenso há dez anos. Sem diabetes. '
                    'Exames de rotina de dois meses atrás: creatinina 1,0 '
                    'mg/dL, hemoglobina 13,9 g/dL, urina normal. No ambulatório '
                    'de clínica médica, há seis semanas, pela febre e pelo '
                    'emagrecimento: creatinina 1,4 mg/dL e 12 hemácias por '
                    'campo na urina, com retorno marcado para três meses.'),
                   ('Medicações', 'Losartana 50 mg por dia. Dipirona quando '
                    'tem febre. Xarope antitussígeno. O último antibiótico '
                    'terminou há quatro semanas. Nega anti-inflamatório, chás e '
                    'suplementos.'),
                   ('Hábitos', 'Ex-tabagista de 30 anos-maço, parou há oito '
                    'anos. Bebe pouco, nas festas. Nega cocaína e outras '
                    'drogas.'),
                   ('Vida social', 'Pedreiro dos 18 aos 58 anos; hoje cuida de '
                    'uma horta no quintal, quase sempre descalço. Mora com a '
                    'esposa em Quixadá, no sertão central do Ceará, em casa de '
                    'alvenaria com água encanada. Sem viagens e sem animais em '
                    'casa.'),
                   ('Família', 'Pai morreu de infarto aos 70 anos. Mãe '
                    'diabética. Dois filhos saudáveis.')),
           so_kicker=True),

    pagina('exame', 'Exame físico', '',
           vitais(('Temperatura', '37,8 °C', True),
                  ('Pressão arterial', '148/92', True),
                  ('Frequência cardíaca', '104', True),
                  ('Frequência respiratória', '28', True),
                  ('SpO₂ em ar ambiente', '88%', True),
                  ('Peso', '78 kg (84 kg há dois meses)', True)),
           topicos(('Estado geral', 'Dispneico, prefere ficar sentado, completa '
                    'só frases curtas. Palidez acentuada.'),
                   ('Nariz e orofaringe', 'Crostas hemáticas aderidas ao septo '
                    'nas duas narinas, mucosa friável que sangra ao toque. Septo '
                    'íntegro. Orofaringe sem lesões.'),
                   ('Pescoço', 'Sem estase jugular a 45°. Sem linfonodos '
                    'palpáveis.'),
                   ('Respiratório', 'Crepitações finas nos dois hemitórax, da '
                    'base ao terço médio. Sem sibilos.'),
                   ('Coração', 'Rítmico, taquicárdico, sem sopros.'),
                   ('Abdome', 'Flácido, indolor, sem visceromegalias.'),
                   ('Pele e membros', 'Sem edema. No dorso dos pés, algumas '
                    'pápulas avermelhadas de 1 a 2 mm, que ele atribui a '
                    'picadas de inseto na horta. Sem lesões nas polpas digitais '
                    'nem hemorragias subungueais.'),
                   ('Neurológico', 'Orientado. Força proximal preservada, '
                    'reflexos patelares presentes. Marcha não testada, pela '
                    'dispneia.')),
           so_kicker=True),

    painel('res1', 'Primeiros exames', 'Sangue', [
        ex('Hemoglobina / hematócrito', '7,8 g/dL / 23,6% {{(13,9 g/dL há dois meses)}}', 'Hb 13,5–17,5 g/dL', True),
        ex('VCM / reticulócitos', '88 fL / 2,1%', '80–100 fL · 0,5–2,5%'),
        ex('Leucócitos', '14.200/mm³ · neutrófilos 82%', '4.000–11.000/mm³', True),
        ex('Plaquetas', '468.000/mm³', '150.000–450.000/mm³', True),
        ex('Ureia / creatinina', '118 / 3,8 mg/dL {{(creatinina 1,4 há seis semanas)}}', 'até 42 / 1,3 mg/dL', True),
        ex('Sódio / potássio / cloro', '136 / 5,4 / 104 mmol/L', 'Na 135–145 · K 3,5–5,0 · Cl 98–107', True),
        ex('Albumina', '2,9 g/dL', '3,5–5,0 g/dL', True),
        ex('Proteína C reativa / procalcitonina', '186 mg/L / 0,4 ng/mL', 'até 5 mg/L / abaixo de 0,5 ng/mL', True),
        ex('DHL / bilirrubina total', '210 U/L / 0,6 mg/dL', 'até 250 U/L / até 1,2 mg/dL'),
    ], introducao='Três pares de hemoculturas foram colhidos antes de qualquer '
                  'antibiótico.'),

    painel('res1b', 'Primeiros exames', 'Gasometria, urina e outros', [
        ex('Gasometria arterial em ar ambiente', 'pH 7,29 · pCO₂ 32 · pO₂ 56 mmHg · HCO₃ 15 mmol/L · lactato 1,6 mmol/L', '—', True),
        ex('Urina, tira e sedimento automatizado', 'Densidade 1.018 · sangue +++ · proteína ++ · 60 hemácias e 6 leucócitos por campo · sem bacteriúria · sem cilindros na leitura automatizada', '—', True),
        ex('Relação proteína/creatinina urinária', '1,4 g/g', 'abaixo de 0,2 g/g', True),
        ex('Sódio / creatinina urinários', '28 mmol/L / 98 mg/dL · FENa 0,8%', '—'),
        ex('Esfregaço de sangue periférico', 'Hemácias normocíticas, sem esquizócitos', 'sem esquizócitos'),
        ex('Coombs direto', 'Negativo', 'negativo'),
    ]),

    estudo('rx_adm', 'Radiografia de tórax na admissão',
        'Radiografia feita na chegada, com ele sentado no leito. Descreva a '
        'distribuição das opacidades antes de ler os achados.',
        IMG / 'rx_torax_alveolar.jpg',
        'Radiografia de outro paciente · comparação didática.',
        'Samir · Wikimedia Commons · CC BY-SA 3.0 · recorte prévio e setas adicionadas',
        [
         ((308, 427), (110, 345), '**Opacidades alveolares** no pulmão direito, mais densas nos campos médio e inferior.', 12),
         ((704, 430), (912, 320), 'O mesmo padrão no **pulmão esquerdo**: a doença é bilateral.', -12),
         ((620, 160), (760, 60), '**Ápices relativamente poupados**: o predomínio é central e inferior.', 12),
        ],
        ['Opacidades alveolares bilaterais, em campos médios e inferiores, sem '
         'derrame pleural e sem aumento da área cardíaca.',
         'Com febre, leucocitose e proteína C reativa de 186 mg/L, a equipe lê '
         'como pneumonia multilobar.']),

    estudo('us_adm', 'Ultrassonografia renal',
        'Pedida na chegada, pela creatinina de 3,8 mg/dL. Antes de interpretar '
        'a urina, a pergunta é se há obstrução ou rim pequeno de doença antiga.',
        IMG / 'us_rim.jpg',
        'Rim de outro adulto. Asteriscos da fonte: um, coluna de Bertin; '
        'dois, pirâmide; três, córtex; quatro, seio renal. Os cálipers também '
        'são da fonte e não medem este paciente.',
        'Hansen, Nielsen e Ewertsen · Wikimedia Commons · CC BY 4.0 · recorte prévio e setas adicionadas',
        [
         ((495, 288), (620, 105), '**Córtex** renal (três asteriscos), de espessura preservada.', 12),
         ((462, 345), (330, 160), '**Pirâmide medular** (dois asteriscos), hipoecoica: a diferenciação entre córtex e medula está preservada.', 12),
         ((447, 400), (720, 550), '**Seio renal** (quatro asteriscos), ecogênico, sem dilatação do sistema coletor.', -12),
        ],
        ['Rins de 11,2 e 11,0 cm, córtex de espessura preservada, sem '
         'hidronefrose (laudo do caso).',
         'Sem obstrução e sem sinal de doença renal antiga: a lesão é do rim, '
         'e recente.']),

    Q('p1', 1,
      'Gasometria arterial em ar ambiente, com os eletrólitos da mesma coleta. '
      '**Quais três** afirmações estão corretas?', [
      ('Acidose metabólica com hiato aniônico aumentado', True),
      ('Compensação respiratória adequada', True),
      ('Gradiente alvéolo-arterial de oxigênio aumentado', True),
      ('Acidose respiratória associada', False),
      ('Acidose lática por hipoperfusão', False),
      ('Hiato aniônico normal depois de corrigir a albumina', False),
      ('Hipoxemia explicada por hipoventilação', False),
     ], [
      ('As contas', 'O hiato aniônico é 136 − (104 + 15) = 17 mmol/L. '
       'Corrigido pela albumina de 2,9 g/dL, soma 2,5 para cada grama abaixo '
       'de 4 e chega a cerca de 20. Pela fórmula de Winters, o pCO₂ esperado é '
       '1,5 × 15 + 8 = 30,5 ± 2; o medido, 32, cabe na faixa. A resposta '
       'respiratória é a esperada, sem distúrbio respiratório primário.'),
      ('O oxigênio', 'Em ar ambiente, a pressão alveolar de oxigênio é cerca '
       'de 0,21 × (760 − 47) − 32/0,8, perto de 110 mmHg. Com pO₂ de 56, o '
       'gradiente passa de 50 mmHg, quando o esperado aos 63 anos fica perto '
       'de 20. A hipoxemia vem do parênquima; a ventilação está aumentada, não '
       'reduzida.'),
      ('O que a acidose indica', 'Lactato de 1,6 mmol/L afasta hipoperfusão '
       'como causa. Com ureia de 118 e creatinina de 3,8, é a acidose da lesão '
       'renal, que retém sulfato, fosfato e outros ânions.'),
     ]),

    Q('p2', 2,
      'Creatinina de 1,0 há dois meses, 1,4 há seis semanas e 3,8 mg/dL hoje. '
      'Com a urina e o ultrassom da chegada, qual a interpretação mais '
      'adequada da lesão renal?', [
      ('Pré-renal por hipovolemia', False),
      ('Necrose tubular aguda da sepse', False),
      ('Nefrite intersticial pela amoxicilina', False),
      ('Glomerulonefrite rapidamente progressiva', True),
      ('Obstrução urinária', False),
      ('Doença renal crônica agudizada', False),
     ], [
      ('O padrão', 'Hematúria de 60 hemácias por campo, proteinúria de 1,4 '
       'g/g e perda de função em semanas descrevem síndrome nefrítica de '
       'evolução rápida. Por CKD-EPI 2021, aos 63 anos, a filtração caiu de '
       'cerca de 85 para 17 mL/min/1,73 m² em dois meses. Perder mais da metade '
       'da filtração em semanas a poucos meses, com sedimento nefrítico, é a '
       'definição de glomerulonefrite rapidamente progressiva.'),
      ('A armadilha da FENa', 'A fração de excreção de sódio de 0,8% parece '
       'pré-renal. Na glomerulonefrite, porém, o túbulo está íntegro e '
       'reabsorve sódio com avidez, porque recebe pouco filtrado. FENa baixa '
       'com hematúria e proteinúria não é hipovolemia.'),
      ('Por que não as outras', 'Necrose tubular daria FENa acima de 2% e '
       'cilindros granulosos. Nefrite intersticial por betalactâmico traria '
       'leucocitúria, e aqui há 6 leucócitos por campo. O ultrassom sem '
       'hidronefrose afasta obstrução, e rins de 11 cm com creatinina de 1,0 '
       'dois meses antes afastam doença crônica.'),
     ]),

    estudo('sedimento', 'Sedimento urinário, leitura manual',
        'A leitura automatizada não procura dismorfismo nem cilindro. A equipe '
        'pede a leitura manual do sedimento da admissão.',
        IMG / 'sedimento_cilindro.jpg',
        'Sedimento de outro paciente. A fonte identifica o cilindro como '
        'hemático; ampliada, a foto não resolve hemácias uma a uma.',
        'Rian Kabir · Wikimedia Commons · CC BY 2.0 · setas adicionadas',
        [
         ((457, 493), (200, 380), '**Borda** lisa e paralela: o cilindro é o molde do lúmen de um túbulo.', 12),
         ((500, 500), (720, 700), '**Conteúdo celular** denso e acastanhado, preso na matriz do cilindro.', -12),
         ((757, 243), (880, 110), '**Extremidade** arredondada, onde o molde se desprendeu do túbulo.', 12),
        ],
        ['Hemácias dismórficas em 40%, com acantócitos, e cilindros hemáticos '
         '(laudo do caso).',
         'A hemácia que se deforma ao atravessar o glomérulo e o cilindro '
         'formado dentro do túbulo localizam o sangramento no glomérulo.']),

    estudo('tc_seios', 'Tomografia dos seios da face',
        'Pela obstrução nasal de oito semanas que não cedeu a dois '
        'antibióticos, a equipe pede tomografia dos seios da face, à procura '
        'de um foco de infecção.',
        IMG / 'tc_seio_maxilar.jpg',
        'Corte axial de outro paciente, em janela óssea. O lado esquerdo do '
        'paciente está à direita da imagem.',
        credito_meta(IMG / 'tc_seio_maxilar.jpg.json'),
        [
         ((596, 176), (820, 90), '**Seio maxilar esquerdo** velado por conteúdo de partes moles, com pequena bolha de ar.', -12),
         ((429, 171), (250, 90), '**Seio maxilar direito** aerado, de paredes finas.', 12),
         ((504, 143), (560, 30), '**Septo nasal** íntegro, sem perfuração.', 12),
        ],
        ['Velamento do seio maxilar esquerdo, sem erosão das paredes ósseas. '
         'Septo nasal íntegro.',
         'A equipe lê como sinusite maxilar crônica, e ela reforça a hipótese '
         'de infecção.']),

    pg('hipotese', 'A hipótese da equipe',
       'Febre, infiltrado bilateral, leucocitose e proteína C reativa de 186 '
       'mg/L num homem com sinusite arrastada. No rim, glomerulonefrite com '
       'cilindros hemáticos. A equipe registra pneumonia grave multilobar com '
       'glomerulonefrite associada à infecção, e endocardite a afastar.',
       'Inicia ceftriaxona 2 g e azitromicina 500 mg ao dia, oxigênio por '
       'cateter nasal a 4 L/min, e pede ecocardiograma transtorácico, '
       'complemento e antígenos urinários de pneumococo e legionela.'),

    Q('p3', 3,
      'Sobre a glomerulonefrite associada à infecção no adulto, **quais três** '
      'afirmações estão corretas?', [
      ('O estafilococo é hoje o agente mais comum', True),
      ('Pode surgir com a infecção ainda ativa', True),
      ('O C3 costuma estar consumido', True),
      ('Exige latência de duas a três semanas', False),
      ('Complemento normal a exclui', False),
      ('Regride com poucos dias de antibiótico', False),
     ], [
      ('No adulto', 'Na criança, o modelo é a glomerulonefrite '
       'pós-estreptocócica, que aparece uma a três semanas depois da faringite '
       'ou da infecção de pele, quando a infecção já passou. No adulto, '
       'sobretudo acima dos 60 anos, com diabetes ou câncer, o estafilococo '
       'passou à frente, e a nefrite costuma surgir com a infecção em curso: '
       'pele, osso, pulmão, cateter ou endocardite.'),
      ('O complemento', 'O C3 está baixo na maioria dos casos e é a pista '
       'sorológica mais útil, mas um C3 normal não exclui, sobretudo nas '
       'formas estafilocócicas. Quem confirma é a biópsia, com depósitos '
       'granulares de C3, às vezes com IgA dominante.'),
      ('O que muda', 'O tratamento é o da infecção, e a recuperação renal leva '
       'semanas, às vezes incompleta no idoso. Complemento, antígenos '
       'urinários, hemoculturas e ecocardiograma testam, cada um, um pedaço da '
       'hipótese.'),
     ]),

    estudo('eco', 'Ecocardiograma transtorácico',
        'Feito no primeiro dia, à procura de vegetação. Localize o septo e as '
        'duas valvas atrioventriculares antes de ler o laudo.',
        IMG / 'eco_4camaras.jpg',
        'Corte apical de quatro câmaras de outra pessoa, na orientação da '
        'fonte: ápice para baixo, coração esquerdo à direita da imagem.',
        credito_meta(IMG / 'eco_4camaras.jpg.json'),
        [
         ((432, 430), (270, 560), '**Septo interventricular**, entre o ventrículo direito, à esquerda da imagem, e o esquerdo.', 12),
         ((522, 258), (700, 150), '**Valva mitral** fechada, de folhetos finos, sem massa aderida.', -12),
         ((370, 258), (230, 150), '**Valva tricúspide**, no mesmo plano, também sem massa.', 12),
        ],
        ['Valvas finas, sem vegetação e sem regurgitação significativa. '
         'Função sistólica preservada (laudo do caso).',
         'O transtorácico sem vegetação reduz a probabilidade de endocardite, '
         'mas não a afasta: a sensibilidade para vegetações pequenas é '
         'limitada.']),

    painel('res2', 'As primeiras 36 horas', 'O que a equipe pediu', [
        ex('Complemento C3 / C4', '112 / 28 mg/dL', 'C3 90–180 · C4 10–40 mg/dL'),
        ex('Antígeno urinário de pneumococo', 'Não reagente', 'não reagente'),
        ex('Antígeno urinário de legionela', 'Não reagente', 'não reagente'),
        ex('Hemoculturas, três pares', 'Sem crescimento em 36 horas', 'sem crescimento'),
        ex('Procalcitonina', '0,3 ng/mL', 'abaixo de 0,5 ng/mL'),
        ex('HBsAg, anti-HCV e anti-HIV', 'Não reagentes', 'não reagentes'),
    ]),

    pg('dia2', 'Segundo dia de internação',
       'Trinta e seis horas depois da primeira dose, a saturação caiu para 89% '
       'com cateter nasal a 4 L/min e foi preciso passar para máscara com '
       'reservatório a 10 L/min, sem ganho proporcional. A frequência '
       'respiratória subiu para 32. Ele expectorou mais duas vezes sangue '
       'vivo, cerca de 30 mL de cada vez.',
       'A hemoglobina está em 6,9 g/dL, sem melena, hematêmese ou epistaxe '
       'volumosa. A creatinina subiu para 4,1 mg/dL, e a diurese das últimas '
       '24 horas foi de 620 mL. A equipe pede tomografia de tórax sem '
       'contraste.'),

    estudo('tc_torax', 'Tomografia de tórax',
        'Tomografia do segundo dia, pela piora da oxigenação. Descreva o '
        'padrão e a distribuição antes de propor o que ocupa o alvéolo.',
        IMG / 'tc_torax_vidro_fosco.jpg',
        'Cortes axiais e reconstruções de outro paciente, em janela de '
        'pulmão · comparação didática.',
        'Hellerhoff · Wikimedia Commons · CC BY-SA 4.0 · setas adicionadas',
        [
         ((115, 165), (330, 40), '**Vidro fosco** no lobo superior direito, entremeado de pulmão aerado.', -12),
         ((93, 750), (300, 830), 'O mesmo padrão, mais denso, nas **bases**, com áreas de consolidação.', 12),
         ((533, 235), (640, 70), 'Na reconstrução coronal, o **pulmão direito** tomado do ápice à base.', -12),
        ],
        ['Opacidades em vidro fosco difusas e bilaterais, com áreas de '
         'consolidação. Sem nódulos escavados e sem derrame pleural.',
         'No vidro fosco cabem sangue, água, pus e células; quem escolhe é a '
         'clínica.']),

    Q('p4', 4,
      'Com a tomografia e a evolução do segundo dia, **quais quatro** achados '
      'deste paciente sustentam hemorragia alveolar difusa?', [
      ('Hemoglobina caindo sem sangramento externo', True),
      ('Hemoptise', True),
      ('Hipoxemia que responde mal ao oxigênio', True),
      ('Vidro fosco difuso e bilateral', True),
      ('Derrame pleural bilateral', False),
      ('Nódulos escavados', False),
      ('Capacidade de difusão reduzida', False),
     ], [
      ('O sangue que não saiu', 'Cerca de 110 mL expectorados em dois dias '
       'não explicam a hemoglobina de 13,9, dois meses antes, para 6,9 g/dL, sem melena, '
       'hematêmese nem epistaxe volumosa. O sangue ficou no espaço aéreo.'),
      ('O pulmão', 'Alvéolo cheio de sangue é perfundido e não ventilado: é '
       'shunt, que responde mal ao aumento do oxigênio ofertado, como na '
       'passagem para a máscara com reservatório. O vidro fosco difuso é '
       'compatível e inespecífico. A hemoptise sustenta, mas falta em até um '
       'terço das hemorragias alveolares.'),
      ('Por que não as outras', 'Não há derrame nem nódulos escavados na '
       'tomografia; nódulo escavado apontaria para êmbolo séptico, '
       'micobactéria ou fungo. Na hemorragia recente, a capacidade de difusão '
       'do monóxido de carbono sobe, porque a hemoglobina dentro do alvéolo '
       'capta o gás. Ninguém mede isso em quem está de máscara, mas a lógica '
       'ensina.'),
     ]),

    bifurcacao("b_dia2", "Decisão",
        "Ele piorou sob antibiótico. O que você faz agora?",
        "Trinta e seis horas de ceftriaxona e azitromicina, mais oxigênio, mais "
        "hemoptise e 0,9 g/dL a menos de hemoglobina. As culturas ainda não "
        "voltaram.",
        [
            caminho("Escalonar o antibiótico para carbapenêmico e vancomicina",
                    "r_escalona",
                    "É a leitura de que o espectro foi insuficiente, e germe "
                    "resistente existe. Mas trinta e seis horas é cedo para "
                    "declarar falha numa pneumonia comunitária, e antibiótico "
                    "mais largo não retém sangue no alvéolo."),
            caminho("Investigar a hemorragia alveolar antes de mudar o "
                    "tratamento", "r_investiga",
                    "A broncoscopia com lavado mostra de onde vem o sangue, e a "
                    "cultura do lavado responde ao que sobrou da hipótese de "
                    "infecção. O antibiótico continua correndo enquanto isso."),
            caminho("Iniciar corticoide em dose imunossupressora agora",
                    "r_corticoide",
                    "A hemorragia alveolar é uma emergência, e o corticoide "
                    "costuma contê-la. O preço é o momento: as culturas ainda "
                    "estão em curso, e nenhum material foi colhido antes."),
        ],
    ),

    pg("r_escalona", "Terceiro e quarto dias",
       "Meropeném e vancomicina correram por 48 horas. A saturação caiu para "
       "91% em máscara com reservatório a 12 L/min e a hemoglobina está em 6,3 "
       "g/dL, com nova hemoptise de cerca de 40 mL. A creatinina subiu para "
       "4,6 mg/dL e a diurese caiu para 380 mL.",
       "As hemoculturas da admissão seguem negativas. A urocultura, negativa.",
       segue="virada"),

    pg("r_investiga", "Terceiro dia",
       "Broncoscopia à beira do leito, sob oxigênio a 100%. Árvore brônquica "
       "sem lesão endobrônquica e sem ponto de sangramento: sangue difuso "
       "escorrendo dos óstios segmentares dos dois pulmões.",
       "Lavado em três alíquotas de 60 mL no mesmo segmento: a primeira "
       "rosada, a segunda vermelha, a terceira francamente hemorrágica. A "
       "citologia mostra macrófagos carregados de hemossiderina, e a "
       "bacterioscopia é negativa.",
       segue="virada"),

    pg("r_corticoide", "Terceiro e quarto dias",
       "Metilprednisolona 500 mg ao dia. Em 48 horas a hemoptise cessou e a "
       "saturação subiu para 95% em cateter a 4 L/min. A hemoglobina "
       "estabilizou em 6,9 g/dL e a creatinina parou de subir, em 4,6 mg/dL.",
       "A partir de agora, toda cultura negativa terá sido colhida sob "
       "imunossupressão, e o valor dela é menor.",
       segue="virada"),

    # ══════════════════════ a virada ══════════════════════

    pg("virada", "Quinto dia de internação",
       "As três hemoculturas colhidas antes do antibiótico vieram negativas em "
       "cinco dias. A urocultura e os antígenos urinários também são "
       "negativos, e o complemento é normal. A creatinina está em 4,6 mg/dL.",
       "Com cinco dias de antibiótico e nenhuma cultura positiva, a equipe "
       "volta ao paciente e o reexamina, dessa vez de pé."),

    pagina("reexame", "O reexame do quinto dia", "",
        topicos(
            ("Marcha",
             "Levado ao banheiro com apoio, arrasta a ponta do pé direito. Diz "
             "que tropeça há cerca de dez dias e achou que era fraqueza."),
            ("Neurológico",
             "Dorsiflexão do pé direito com força 2/5 e aquileu direito "
             "abolido. Hipoestesia no território ulnar esquerdo. Sem nível "
             "sensitivo e sem padrão de raiz única."),
            ("Pele",
             "As pápulas dos pés se multiplicaram e subiram para as pernas: "
             "lesões elevadas de 2 a 8 mm, algumas com centro escurecido, que "
             "não desaparecem à digitopressão."),
        ),
        so_kicker=True),

    estudo('purpura', 'A pele das pernas',
        'Fotografia de outro paciente, com lesões do mesmo tipo das dele. Antes '
        'de ler os achados, descreva o tamanho, o centro das lesões e onde '
        'elas se concentram.',
        IMG / 'purpura_perna.jpg',
        'Outro paciente, de outra causa. A foto não mostra o relevo nem o teste '
        'da pressão: a elevação se sente com a polpa do dedo, e a lesão que não '
        'empalidece sob uma lâmina de vidro é sangue fora do vaso.',
        credito_meta(IMG / 'purpura_perna.jpg.json'),
        [
         ((809, 207), (450, 200), 'Na perna, **pápulas isoladas** de poucos milímetros, com pele normal entre elas.', 12),
         ((471, 993), (200, 820), 'No dorso do pé, lesão com **centro escurecido** e halo vermelho.', -12),
         ((857, 657), (450, 560), 'Perto do tornozelo, lesões mais densas que **confluem**, com centro acinzentado de necrose.', 12),
        ],
        ['Pápulas purpúricas de 2 a 8 mm que começaram nos pés e subiram para '
         'as pernas, algumas com centro escurecido, que não desaparecem à '
         'digitopressão (exame do caso).',
         'Púrpura que se palpa é sangue fora de um vaso pequeno cuja parede '
         'está inflamada; a púrpura plana da plaquetopenia não tem relevo. A '
         'predileção pelas pernas acompanha a pressão hidrostática.']),

    Q('p5', 5,
      'Hemorragia alveolar e glomerulonefrite com cilindros hemáticos, no '
      'mesmo mês, com culturas negativas. **Quais três** mecanismos produzem '
      'esse par?', [
      ('Anticorpo contra a membrana basal', True),
      ('Deposição de imunocomplexos', True),
      ('Inflamação de pequenos vasos sem depósitos', True),
      ('Microangiopatia trombótica', False),
      ('Congestão cardiorrenal', False),
      ('Necrose tubular com lesão pulmonar da sepse', False),
      ('Nefrotoxicidade do betalactâmico', False),
     ], [
      ('Os três mecanismos', 'Anticorpo contra o colágeno tipo IV da membrana '
       'basal, presente no glomérulo e no alvéolo: é a doença anti-MBG, com '
       'depósito linear de IgG. Imunocomplexos que se depositam nos dois '
       'leitos: lúpus, crioglobulinemia, vasculite por IgA e a própria '
       'endocardite, com depósito granular e, em várias delas, complemento '
       'baixo. E a inflamação necrosante de pequenos vasos sem depósito na '
       'imunofluorescência, chamada pauci-imune, a mais comum depois dos 50 '
       'anos.'),
      ('O que o paciente já mostrou', 'A púrpura que não some à digitopressão '
       'e a mononeurite múltipla, com pé caído à direita e território ulnar à '
       'esquerda, dizem que o vaso pequeno está inflamado também na pele e no '
       'nervo. C3 e C4 normais tornam o imunocomplexo menos provável.'),
      ('Por que não os outros', 'Microangiopatia trombótica exigiria '
       'plaquetas baixas e esquizócitos, e ele tem 468.000 e esfregaço limpo. '
       'Congestão daria estase jugular e edema. Sepse e betalactâmico lesam o '
       'túbulo, não o glomérulo: cilindro granuloso, não hemático.'),
     ]),

    painel("res_mec", "O mecanismo", "Biópsia e sorologias", [
        ex('Anticorpo anti-membrana basal glomerular', 'Não reagente {{(resultado em horas)}}', 'não reagente'),
        ex('FAN / anti-DNA nativo', 'Não reagentes', 'não reagentes'),
        ex('Crioglobulinas', 'Não detectadas', 'não detectadas'),
        ex('Biópsia renal · microscopia óptica', '24 glomérulos · crescentes celulares em 15 (62%) · necrose fibrinoide segmentar · fibrose intersticial em 10% do córtex', 'sem proliferação extracapilar', True),
        ex('Biópsia renal · imunofluorescência', 'Sem depósitos significativos de IgG, IgA, IgM, C3 ou C1q · padrão pauci-imune · sem depósito linear', 'sem depósitos', True),
    ], introducao='Com o anti-MBG negativo em horas, a equipe transfundiu, '
                  'puncionou o rim no mesmo dia, e a metilprednisolona 500 mg ao '
                  'dia passou a correr sem esperar o laudo. A biópsia saiu em '
                  'três dias. Um último anticorpo, colhido junto, levou quatro.'),

    estudo("crescente", "Corpúsculo renal",
        "Antes de interpretar a microfotografia, localize a cápsula, o espaço "
        "urinário e o tufo capilar neste esquema. O que significa uma "
        "proliferação ocorrer fora do tufo?",
        IMG / "corpusculo_setas.jpg",
        "Esquema de um corpúsculo renal normal, com as estruturas da legenda "
        "original apontadas pelas setas.",
        "Michał Komorniczak · Wikimedia Commons · CC BY-SA 3.0 · números "
        "originais retirados, setas adicionadas",
        [((722, 178), (830, 70), "**Camada parietal da cápsula de Bowman**: "
          "epitélio achatado que forra a cápsula por dentro.", -14),
         ((566, 130), (330, 40), "**Espaço urinário (de Bowman)**: entre o "
          "tufo e a cápsula, recebe o filtrado.", 14),
         ((604, 571), (720, 690), "**Podócito**: a camada visceral da cápsula, "
          "que reveste as alças por fora.", 14),
         ((436, 214), (250, 130), "**Capilar glomerular**: uma alça do tufo, "
          "com endotélio e membrana basal.", 14),
         ((486, 370), (300, 690), "**Célula mesangial**: no eixo do tufo, "
          "entre as alças.", -14)],
        ["Tudo o que fica dentro da cápsula e fora das alças é espaço "
         "urinário. Uma proliferação de células nesse espaço, a partir do "
         "epitélio parietal e com macrófagos, é a crescente: lesão "
         "extracapilar, sinal de ruptura da parede capilar.",
         "O esquema normal orienta a leitura da microfotografia seguinte, mas "
         "não demonstra lesão nem a proporção de glomérulos afetados."],
        kicker="Discussão visual"),

    estudo("crescente_histologia", "Biópsia renal",
        "Microfotografia de outro paciente, com a mesma lesão descrita no "
        "laudo. Localize o tufo, a cápsula e o que ocupa o espaço entre eles.",
        IMG / "glomerulo_crescente.jpg",
        "PAS. Microfotografia ilustrativa de outro paciente; não permite contar "
        "os glomérulos do laudo do caso.",
        "Nephron · Wikimedia Commons · CC BY-SA 3.0 · setas adicionadas",
        [((795, 285), (750, 110), "**Tufo glomerular**: alças capilares, à direita da "
          "proliferação extracapilar.", 14),
         ((432, 292), (230, 210), "**Cápsula de Bowman**: o limite externo do "
          "corpúsculo renal.", 20),
         ((505, 362), (320, 490), "**Crescente**: proliferação extracapilar que ocupa "
          "o espaço de Bowman, na periferia do tufo.", -26)],
        ["Crescentes celulares em 15 dos 24 glomérulos (62%), necrose "
         "fibrinoide segmentar, sem depósitos (laudo do caso).",
         "Na classificação de Berden, 50% ou mais de glomérulos com crescente "
         "celular é a classe crescêntica: prognóstico renal intermediário, e a "
         "classe em que a pressa do tratamento mais preserva rim, porque a "
         "crescente celular ainda regride."],
        kicker="Discussão de imagem"),

    estudo('if_anca', 'O último anticorpo',
        'Chega no nono dia. Neutrófilos fixados em etanol recebem o soro do '
        'paciente e um anticorpo antiglobulina marcado: onde a fluorescência '
        'se acumula, está o alvo.',
        IMG / 'panca_imunofluorescencia.jpg',
        'Neutrófilos de outro paciente · imagem ilustrativa.',
        'Simon Caulton · Wikimedia Commons · CC BY-SA 3.0 · setas adicionadas',
        [
         ((468, 514), (330, 640), 'A fluorescência **contorna os lóbulos do núcleo** e deixa o citoplasma escuro.', 12),
         ((629, 236), (800, 120), 'Outro neutrófilo com o mesmo **contorno perinuclear**.', -12),
        ],
        ['ANCA por imunofluorescência indireta: padrão perinuclear, título '
         '1:640. ELISA: anti-MPO 148 U/mL; anti-PR3 não reagente (laudo do '
         'caso).',
         'O padrão perinuclear em etanol é artefato da fixação: a '
         'mieloperoxidase, catiônica, migra para perto do núcleo. Quem define o '
         'alvo é o ELISA.']),

    pareamento("p6", "Pergunta 6",
        "Associe cada perfil sorológico ao contexto em que ele é "
        "característico.",
        [
            par("c-ANCA com anti-PR3",
                "Granulomatose com poliangiite",
                "Padrão citoplasmático com anti-PR3; via aérea destrutiva, "
                "granuloma e nódulo escavado."),
            par("p-ANCA com anti-MPO",
                "Poliangiite microscópica",
                "O perfil dele: rim e capilarite pulmonar, em geral sem "
                "granuloma."),
            par("Anti-PR3 e anti-MPO simultâneos, com anti-elastase",
                "Vasculite por cocaína adulterada com levamisol",
                "Dupla positividade com anti-elastase é atípica das vasculites "
                "primárias e sugere levamisol."),
            par("Anti-MPO com anti-membrana basal, os dois positivos",
                "Doença anti-MBG com ANCA (dupla positividade)",
                "Rim com prognóstico de anti-MBG e recidiva de vasculite; a "
                "troca plasmática entra."),
            par("p-ANCA atípico, sem anti-MPO nem anti-PR3",
                "Colite ulcerativa e hepatopatia autoimune",
                "Fluorescência perinuclear sem alvo definido acompanha doença "
                "intestinal e hepatopatia autoimune."),
        ],
        opcoes=[
            "Granulomatose com poliangiite",
            "Poliangiite microscópica",
            "Vasculite por cocaína adulterada com levamisol",
            "Doença anti-MBG com ANCA (dupla positividade)",
            "Colite ulcerativa e hepatopatia autoimune",
            "Poliarterite nodosa",
        ],
        titulo_resposta="O alvo do anticorpo orienta o fenótipo",
        nota="A opção que sobrou é a armadilha: a poliarterite nodosa é ANCA "
             "negativa e de vaso médio."),

    pagina("diagnostico", "O diagnóstico", "",
        p("Glomerulonefrite crescêntica pauci-imune, anti-MPO de 148 U/mL e "
          "hemorragia alveolar: é **vasculite associada ao ANCA**, no fenótipo "
          "de **poliangiite microscópica**, com síndrome pulmão-rim. A púrpura "
          "das pernas e a mononeurite múltipla são a mesma inflamação na pele e "
          "nos vasos do nervo. O anticorpo ativa neutrófilos já estimulados, "
          "que liberam enzimas na parede do capilar sem depositar "
          "imunoglobulina; no glomérulo, a parede rota deixa passar fibrina e "
          "células para o espaço de Bowman, e a crescente se forma."),
        p("A equipe revê com a esposa os fármacos que induzem o mesmo quadro "
          "(hidralazina, propiltiouracila, minociclina) e volta a perguntar a "
          "ele, a sós, sobre cocaína, que pode vir adulterada com levamisol. "
          "Nada."),
        tabela(["", "Poliangiite microscópica", "Granulomatose com poliangiite"], [
            ["Sorologia típica", "Anti-MPO, perinuclear", "Anti-PR3, citoplasmático"],
            ["Via aérea superior", "Ausente ou leve, sem destruição",
             "Destrutiva: perfuração septal, nariz em sela"],
            ["Granuloma", "Ausente", "Na via aérea e no pulmão"],
            ["Neste paciente", "Anticorpo e ausência de lesão destrutiva",
             "Os sintomas nasais lembram, sem fechar"],
        ]),
        so_kicker=True),

    Q('p7', 7,
      'Antes e junto da primeira dose da indução, **quais três** medidas '
      'estão indicadas?', [
      ('Sorologia completa de hepatite B', True),
      ('Ivermectina por dois dias', True),
      ('Sulfametoxazol-trimetoprima profilático', True),
      ('Vacina de febre amarela', False),
      ('Fluconazol profilático', False),
      ('Imunoglobulina endovenosa de rotina', False),
     ], [
      ('Hepatite B', 'O anti-HBc isolado reativa sob rituximabe e sob '
       'glicocorticoide em dose alta, e a reativação pode ser fulminante. O '
       'HBsAg não basta: HBsAg e anti-HBc antes da primeira dose decidem se '
       'entra profilaxia antiviral.'),
      ('Estrongiloidíase', 'Ele trabalhou a vida inteira com terra e cuida da '
       'horta descalço, no sertão cearense. O glicocorticoide em dose alta '
       'pode transformar uma infecção silenciosa por //Strongyloides '
       'stercoralis// em hiperinfecção, de mortalidade alta. Ivermectina 200 '
       'µg/kg ao dia por dois dias, junto do pulso, é a conduta usual em quem '
       'tem exposição.'),
      ('Pneumocistose', 'A profilaxia com sulfametoxazol-trimetoprima '
       'acompanha a indução com rituximabe ou ciclofosfamida. Com creatinina '
       'de 4,6 mg/dL, filtração de 14 mL/min/1,73 m² por CKD-EPI 2021, usa-se '
       'meia dose, e o potássio, que chegou a 5,4 mmol/L, precisa ser '
       'vigiado.'),
      ('O que não entra', 'Vacina de vírus vivo é contraindicada sob '
       'imunossupressão. Fluconazol e imunoglobulina não têm indicação de '
       'rotina.'),
     ]),

    # ═══════════ o tratamento, e a segunda virada ═══════════

    bifurcacao("b1", "Decisão",
        "Com que esquema você induz a remissão?",
        "Creatinina de 4,6 mg/dL (407 µmol/L), filtração estimada de 14 "
        "mL/min/1,73 m² por CKD-EPI 2021, 78 kg, 63 anos, hemorragia alveolar "
        "em curso. O glicocorticoide é comum aos três caminhos; a segunda "
        "droga é a decisão.",
        [
            caminho("Rituximabe semanal com dois pulsos de ciclofosfamida",
                    "t_rituximabe",
                    "É o esquema do RITUXVAS, que incluiu doentes com "
                    "filtração mediana de 18 mL/min: rituximabe 375 mg/m² por "
                    "quatro semanas e **dois pulsos de ciclofosfamida**, nas "
                    "semanas 0 e 2. O rituximabe sozinho tem o apoio do RAVE, "
                    "que **excluiu creatinina acima de 4,0 mg/dL**; ele está "
                    "em 4,6. A KDIGO 2024 sugere, com função tão reduzida, "
                    "ciclofosfamida ou a combinação das duas."),
            caminho("Ciclofosfamida endovenosa com dose reduzida pela idade e "
                    "pela função renal", "t_cfx_ajustada",
                    "A redução vem do esquema do CYCLOPS, adotado pela EULAR: "
                    "parte de 15 mg/kg e subtrai **2,5 mg/kg entre 60 e 70 "
                    "anos** (5,0 acima de 70) e mais **2,5 mg/kg com "
                    "creatinina entre 300 e 500 µmol/L**. Aqui: 15 − 2,5 − 2,5 "
                    "= **10 mg/kg**, com teto de 1,2 g por pulso."),
            caminho("Ciclofosfamida endovenosa em dose plena, 15 mg/kg",
                    "t_cfx_plena",
                    "A dose de indução sem as duas subtrações. Com filtração "
                    "de 14 mL/min, a exposição fica bem acima da pretendida, "
                    "porque os metabólitos ativos da ciclofosfamida são "
                    "eliminados por via renal."),
        ],
    ),

    pagina("t_rituximabe", "A prescrição", "O que foi prescrito: caminho A",
        p("**Rituximabe 375 mg/m², uma vez por semana, quatro doses.** "
          "Superfície corporal de 1,93 m² por Mosteller, com 78 kg e "
          "1,72 m: cerca de **725 mg** por dose. Sem correção para a função "
          "renal: o anticorpo monoclonal não é depurado pelo rim.")
        + p("**Ciclofosfamida endovenosa, dois pulsos, nas semanas 0 e 2.** "
            "A dose segue a conta do CYCLOPS: 15 mg/kg de base, −2,5 pela "
            "idade entre 60 e 70 anos e −2,5 pela creatinina de 407 µmol/L, "
            "**10 mg/kg**, 780 mg por pulso. Depois do segundo pulso, só o "
            "rituximabe e o corticoide.")
        + quadro("O que este caminho pede de vigilância",
            p("Pré-medicação com anti-histamínico, paracetamol e o próprio "
              "glicocorticoide, pela reação infusional da primeira dose. "
              "Hepatite B rastreada **antes**. Imunoglobulinas séricas na "
              "linha de base, porque a hipogamaglobulinemia tardia é efeito "
              "dos ciclos seguintes."),
            sistema="sangue"),
        segue="esquema",
    ),

    pagina("t_cfx_ajustada", "A prescrição", "O que foi prescrito: caminho B",
        p("**Ciclofosfamida endovenosa em pulso, 10 mg/kg.** A conta do "
          "CYCLOPS por extenso: 15 mg/kg de base; −2,5 mg/kg por idade "
          "entre 60 e 70 anos; −2,5 mg/kg por creatinina entre 300 e 500 "
          "µmol/L, e os 4,6 mg/dL de hoje são **407 µmol/L**. Restam "
          "**10 mg/kg**. Com 78 kg, **780 mg** por pulso, abaixo do teto "
          "de 1,2 g. Pulsos nas semanas 0, 2 e 4, depois a cada três "
          "semanas.")
        + quadro("O que este caminho pede de vigilância",
            p("Mesna e hidratação em cada pulso, pela cistite hemorrágica da "
              "acroleína. Hemograma entre o 10º e o 14º dia de cada pulso, "
              "onde cai o nadir: leucócitos abaixo de 3.000/mm³ reduzem o "
              "pulso seguinte para 80% da dose, e abaixo de 2.000, para 60%. "
              "E a conversa sobre fertilidade antes da primeira dose, que aos "
              "63 anos pesa menos, mas não se pula."),
            sistema="sangue"),
        segue="esquema",
    ),

    pagina("t_cfx_plena", "A prescrição", "O que foi prescrito: caminho C",
        p("**Ciclofosfamida endovenosa em pulso, 15 mg/kg.** Com 78 kg, "
          "**1,17 g** por pulso. É a dose de indução dos ensaios sem as duas "
          "subtrações, nem a da idade entre 60 e 70 anos, nem a da "
          "creatinina entre 300 e 500 µmol/L. Os metabólitos ativos são "
          "eliminados por via renal, e com filtração de 14 mL/min a "
          "exposição a 1,17 g é maior que a dos ensaios."),
        segue="esquema",
    ),

    pagina("esquema", "A prescrição", "O que é igual nos três caminhos",
        grade(*_esquema_comum(), colunas=2),
        segue="dia3",
    ),

    pg("dia3", "Terceiro dia de indução",
       "Setenta e duas horas depois do primeiro pulso de metilprednisolona, a "
       "hemoptise cessou. O oxigênio caiu de máscara com reservatório para "
       "cateter nasal a 3 L/min, com saturação de 95%. A hemoglobina "
       "estabilizou em 6,8 g/dL depois de duas unidades de concentrado de "
       "hemácias no primeiro dia.",
       "A creatinina parou de subir, em 4,6 mg/dL, com diurese de 780 mL. Ele "
       "voltou a completar frases inteiras e pediu para comer. Ao caminhar "
       "com ajuda, ainda arrasta a ponta do pé direito."),

    pg("dia5", "Quinto dia de indução",
       "Na madrugada, temperatura de 38,9 °C, com calafrio. A pressão caiu "
       "para 92/54 mmHg e respondeu a 500 mL de cristaloide. Frequência "
       "cardíaca de 118, saturação de 94% no mesmo cateter a 3 L/min, sem nova "
       "hemoptise, e as crepitações seguem restritas às bases.",
       "Ele está com um cateter venoso central em jugular interna direita, "
       "puncionado no segundo dia de internação, e o sítio de inserção está "
       "hiperemiado e doloroso. A proteína C reativa, que havia caído para 88 "
       "mg/L com a indução, está em 204 mg/L, e a procalcitonina, que era 0,3, "
       "está em 3,1 ng/mL."),

    Q('p8', 8,
      'Febre de 38,9 °C no quinto dia de indução, hipotensão que respondeu a '
      'volume, sem nova hemoptise. **Quais quatro** causas devem entrar na '
      'lista?', [
      ('Infecção relacionada ao cateter', True),
      ('Atividade da vasculite', True),
      ('Tromboembolismo venoso', True),
      ('Reação hemolítica transfusional tardia', True),
      ('Pneumocistose', False),
      ('Nadir da ciclofosfamida', False),
      ('Reativação de citomegalovírus', False),
     ], [
      ('As quatro que entram', 'Cateter central de mais de uma semana, sítio '
       'inflamado, calafrio e procalcitonina de 0,3 para 3,1: a infecção do '
       'cateter é a primeira hipótese. A atividade da doença entra sempre, mas '
       'o órgão-alvo desmente: a hemoptise cessou e o pulmão não piorou. '
       'Vasculite ativa e imobilidade elevam o risco de trombose venosa, e '
       'febre com taquicardia é apresentação possível. E ele recebeu duas '
       'unidades de hemácias: a reação hemolítica tardia aparece de 3 a 14 '
       'dias depois e pede Coombs e bilirrubina.'),
      ('As que o tempo afasta', 'O nadir da ciclofosfamida cai entre o 10º e '
       'o 14º dia do pulso, e o rituximabe não o produz. Pneumocistose e '
       'citomegalovírus exigem semanas de imunossupressão, e a profilaxia da '
       'pneumocistose já corre.'),
     ]),

    bifurcacao("b_febre", "Decisão",
        "Febre no quinto dia de indução. O que você faz?",
        "38,9 °C com calafrio, hipotensão que respondeu a volume, "
        "procalcitonina de 0,3 para 3,1, cateter central com sítio inflamado. "
        "Sem nova hemoptise e sem piora pulmonar.",
        [
            caminho("Retirar o cateter, colher hemoculturas pareadas e "
                    "iniciar antibiótico com cobertura para "
                    "//Staphylococcus aureus//", "f_retira",
                    "Órgão-alvo estável, procalcitonina subindo e porta de "
                    "entrada visível. Retirar o cateter faz parte do "
                    "tratamento."),
            caminho("Intensificar a imunossupressão, por recidiva da vasculite",
                    "f_intensifica",
                    "Tem lógica se a leitura for de doença descontrolada. Mas a "
                    "hemoptise cessou, o pulmão não piorou e a "
                    "procalcitonina subiu, o marcador que mais separa "
                    "inflamação estéril de infecção bacteriana."),
            caminho("Suspender toda a imunossupressão até esclarecer a febre",
                    "f_suspende",
                    "Parece prudente. Mas a vasculite acabou de ser controlada "
                    "e a crescente ainda é celular: tratar a infecção e manter "
                    "a indução é possível."),
        ],
    ),

    pg("f_retira", "Sétimo dia",
       "Cateter retirado; a ponta cultivou o mesmo agente das hemoculturas "
       "pareadas, //Staphylococcus aureus// sensível a oxacilina, com tempo "
       "diferencial de positivação compatível com origem no cateter. O "
       "ecocardiograma transesofágico não mostrou vegetação.",
       "A febre cedeu em 48 horas, sem interromper a indução.",
       segue="dia10"),

    pg("f_suspende", "Sétimo ao nono dia",
       "A febre cedeu com a retirada tardia do cateter e a oxacilina, no "
       "sétimo dia. Mas no nono, com 48 horas sem corticoide, voltou a "
       "hemoptise, dois episódios de cerca de 40 mL, e a saturação caiu para "
       "90% em cateter a 4 L/min. A hemoglobina caiu de 8,6 para 7,4 g/dL e a "
       "creatinina voltou a subir, de 4,2 para 4,8.",
       "A indução foi reiniciada no décimo dia, em dose plena, sobre um "
       "paciente que passou 48 horas sangrando de novo no alvéolo.",
       segue="dia10"),

    pg("f_intensifica", "Sétimo dia",
       "Metilprednisolona voltou a 1 g ao dia por três dias, sobre a "
       "bacteremia não tratada. O cateter permaneceu. Em 24 horas a "
       "temperatura chegou a 39,6 °C, a pressão caiu para 78/44 mmHg e não "
       "respondeu a 2.000 mL de cristaloide. Lactato 4,8 mmol/L.",
       "As hemoculturas voltaram com //Staphylococcus aureus// em 2 de 2 "
       "pares. Ele foi transferido para a terapia intensiva em choque, com "
       "noradrenalina.",
       conforme=("b1", ["fi_grave", "fi_grave", "fi_obito"])),

    pg("fi_grave", "Do sétimo ao vigésimo dia",
       "Choque séptico por //S. aureus//, com foco em cateter mantido por 48 "
       "horas depois do primeiro pico febril. Noradrenalina por seis dias, "
       "oxacilina por 28 dias, a duração da bacteremia complicada, e três "
       "sessões de diálise durante o choque, por oligúria e acidose "
       "refratária.",
       "Sobreviveu. Saiu da terapia intensiva treze dias depois, com "
       "creatinina de 3,2 mg/dL e diurese recuperada, ainda dependente de "
       "oxigênio suplementar.",
       conforme=("b1", ["prealta_rituximabe", "prealta_cfx", "prealta_uti"])),

    fim("fi_obito", "Óbito na terceira semana de internação",
        "O choque séptico se instalou sobre uma medula que a ciclofosfamida "
        "em dose plena, sem correção para a filtração de 14 mL/min, havia "
        "levado a **210 neutrófilos**. A intensificação do corticoide no "
        "sétimo dia foi dada sobre uma bacteremia já em curso, com a porta "
        "de entrada ainda no pescoço.",
        "Evoluiu com disfunção de múltiplos órgãos e choque refratário a três "
        "drogas vasoativas. Faleceu no nono dia de bacteremia. A vasculite "
        "estava respondendo: a hemoptise havia cessado no terceiro dia de "
        "indução.",
        qualidade="pior",
        porque="Três decisões se somaram, e nenhuma delas era sobre o "
               "diagnóstico. A dose plena da ciclofosfamida com filtração de "
               "14 mL/min entregou uma neutropenia que o esquema corrigido não "
               "produziria. A febre do quinto dia foi lida como recidiva "
               "quando a procalcitonina, o órgão-alvo estável e o sítio de "
               "inserção indicavam infecção. E o cateter, a porta de entrada, "
               "permaneceu. No primeiro ano da vasculite ANCA tratada, a "
               "infecção mata mais do que a própria vasculite."),

    pg("dia10", "Décimo dia de indução",
       "O que vem a seguir depende do esquema de indução escolhido, e é aqui "
       "que os três caminhos deixam de ser o mesmo caso.",
       conforme=("b1", ["d10_rituximabe", "d10_cfx_ajustada", "d10_cfx_plena"])),

    pg("d10_rituximabe", "Décimo dia · caminho A",
       "O hemograma do décimo dia, no nadir do primeiro pulso, mostra 4.800 "
       "leucócitos com 3.000 neutrófilos. Com um pulso só de dose ajustada, a "
       "queda é pequena, e o rituximabe não produz nadir de neutrófilos: a "
       "bacteremia veio do cateter e do corticoide.",
       "Completou as quatro doses semanais e catorze dias de oxacilina. A "
       "creatinina caiu de forma sustentada.",
       segue="prealta_rituximabe"),

    pg("d10_cfx_ajustada", "Décimo dia · caminho B",
       "O hemograma do décimo dia, no nadir esperado do pulso, mostra 3.600 "
       "leucócitos com 1.900 neutrófilos. É citopenia leve, dentro do previsto "
       "para 10 mg/kg; com nadir acima de 3.000 leucócitos, o pulso seguinte "
       "fica na mesma dose, e o hemograma passa a duas vezes por semana "
       "durante a bacteremia.",
       "A febre cedeu, completou catorze dias de oxacilina, e o segundo pulso "
       "foi dado na semana 2, como programado.",
       segue="prealta_cfx"),

    pg("d10_cfx_plena", "Décimo dia · caminho C",
       "O hemograma do décimo dia mostra 900 leucócitos com 210 neutrófilos. "
       "A febre, que havia cedido com a oxacilina, voltou a 39,4 °C, agora com "
       "hipotensão que exigiu noradrenalina, e ele foi transferido para a "
       "terapia intensiva.",
       "A neutropenia é muito mais profunda que a esperada: o nadir de um "
       "pulso ajustado fica em torno de 1.900 neutrófilos. Entraram "
       "antibiótico de amplo espectro, antifúngico empírico no quinto dia de "
       "neutropenia febril e fator estimulador de colônias.",
       segue="prealta_uti"),

    pg("prealta_rituximabe", "Preparação do seguimento",
       "Passa a fazer os trajetos da enfermaria com apoio. A dispneia em "
       "repouso deixou de dominar a conversa; agora pergunta como retomará a "
       "horta. O pé caído exige órteses e orientação de marcha.",
       "Na reconciliação da prescrição, a equipe escreve as datas das "
       "próximas infusões e retornos, além do desmame do corticoide.",
       segue="d_rituximabe"),

    pg("prealta_cfx", "Planejamento dos próximos pulsos",
       "Está mais disposto e volta a comer fora do leito. Ainda precisa de "
       "ajuda em percursos longos, e a esposa pretende ficar com ele na "
       "primeira semana em casa.",
       "A equipe organiza a avaliação antes de cada pulso, com hemograma e "
       "revisão da tolerância. Ele recebe um calendário por escrito e a "
       "orientação de procurar atendimento diante de febre ou nova piora "
       "respiratória.",
       segue="d_cfx_ajustada"),

    pg("prealta_uti", "Recuperação na enfermaria",
       "Fora da terapia intensiva, está desperto e reconhece a família. "
       "Interrompe a caminhada até o banheiro e se apoia no acompanhante para "
       "levantar. Não se lembra de parte da internação e teme voltar a "
       "piorar.",
       "A equipe revê com a família o que aconteceu, organiza a reabilitação "
       "e reconcilia os medicamentos.",
       segue="d_cfx_plena"),

    fim("d_rituximabe", "Alta sem diálise",
        "A creatinina, que havia chegado a 4,6 mg/dL, caiu de forma sustentada "
        "e a diurese se recuperou; ele sai sem diálise e em ar ambiente, com "
        "saturação de 96%.",
        "Segue em manutenção programada com rituximabe e com o pé caído em "
        "reabilitação: a mononeurite é o achado que mais demora a melhorar, "
        "quando melhora.",
        qualidade="melhor",
        porque="O tratamento entrou enquanto a crescente ainda era celular, "
               "lesão ativa e capaz de responder. Com filtração de 14 "
               "mL/min/1,73 m², a combinação do RITUXVAS limita a "
               "ciclofosfamida a dois pulsos de dose ajustada, e a infecção de "
               "cateter não encontrou uma medula deprimida."),

    fim("d_cfx_ajustada", "Alta sem diálise, com vigilância semanal",
        "A creatinina estabilizou acima do valor do caminho A e a diurese se "
        "recuperou; ele sai sem diálise. O hemograma foi vigiado duas vezes "
        "por semana durante a bacteremia, e o nadir do segundo pulso foi de "
        "1.600 neutrófilos.",
        "Completou a oxacilina e os três primeiros pulsos de ciclofosfamida "
        "sem nova intercorrência infecciosa.",
        qualidade="melhor",
        porque="A ciclofosfamida com dose corrigida pela idade e pela "
               "filtração é tão eficaz quanto o esquema com rituximabe. Custa "
               "mais vigilância (hemograma seriado, mesna, ajuste a cada "
               "ciclo) e cobra uma dose acumulada maior que a dos dois pulsos do "
               "caminho A. Neste paciente, de 63 anos, a fertilidade pesa "
               "menos; a conta da dose, não."),

    fim("d_cfx_plena", "Alta após a terapia intensiva",
        "A vasculite respondeu como nos outros dois caminhos: a hemoptise "
        "cessou no terceiro dia e a creatinina caiu. O que mudou foi o resto: "
        "treze dias de terapia intensiva, noradrenalina por quatro deles, "
        "antibiótico de amplo espectro, antifúngico empírico e fator "
        "estimulador de colônias.",
        "Saiu andando, com mais dias de internação e menos função renal que "
        "nos outros caminhos.",
        qualidade="pior",
        porque="Com filtração glomerular de 14 mL/min/1,73 m², a dose plena "
               "produziu exposição bem acima da pretendida: os metabólitos "
               "ativos da ciclofosfamida saem por via renal, e a conta do "
               "CYCLOPS teria pedido 10 mg/kg. No primeiro ano da vasculite "
               "ANCA tratada, a infecção mata mais do que a vasculite. Aqui a "
               "infecção veio do cateter, que os três caminhos tinham; a "
               "profundidade dela veio da dose, que só este caminho escolheu."),

    # ═══════════════ o fecho, igual para os três ramos ═══════════════

    pagina('retrospectiva', 'Pontos de ensino', '',
        pontos(
            'Rinossinusite que não responde a dois antibióticos corretos, com '
            'febre, artralgia e perda de peso, pede urina e creatinina. Aqui, '
            'seis semanas antes, a urina já tinha 12 hemácias por campo.',
            'A creatinina se lê contra o basal do paciente: de 1,0 para 1,4 '
            'mg/dL é perder um terço da filtração (por CKD-EPI 2021, de 85 '
            'para 56 mL/min/1,73 m²), mesmo perto da referência.',
            'FENa baixa com hematúria, proteinúria e cilindros hemáticos não '
            'é pré-renal: na glomerulonefrite o túbulo ainda reabsorve sódio.',
            'Hemoglobina caindo sem sangramento externo, hipoxemia que '
            'responde mal ao oxigênio e vidro fosco difuso são hemorragia '
            'alveolar até prova em contrário; a hemoptise falta em um terço.',
            'Hemorragia alveolar com glomerulonefrite pede anti-MBG e ANCA no '
            'primeiro dia, junto das culturas: o resultado leva dias, e a '
            'crescente celular não espera. A âncora infecciosa foi razoável; '
            'o que faltou foi testar as outras ao mesmo tempo.',
            'Na indução, a ciclofosfamida se ajusta por idade e filtração '
            '(CYCLOPS); antes da primeira dose, hepatite B, ivermectina em '
            'quem tem exposição ao solo e profilaxia de pneumocistose.',
            'Febre durante a indução com o órgão-alvo estável é infecção até '
            'prova em contrário, e o cateter é a primeira porta. No primeiro '
            'ano, a infecção mata mais que a vasculite.'),
        so_kicker=True),

    balanco("balanco", "O balanço da sua condução",
        "O percurso e o preço",
        p("O que cada decisão custou, contra o melhor percurso que este caso "
          "permite. Os números são inferência autoral, coerente com a "
          "fisiologia do caso, e cada linha traz o motivo que a sustenta."),
        base_dias=21, base_tfg=39, base_creatinina="1,9 mg/dL",
        obito_se={"escolheu_todos": [["b_febre", 1], ["b1", 2]]},
        obito_texto="Ciclofosfamida em dose plena com filtração de 14 mL/min, "
                    "e a febre do quinto dia lida como recidiva da doença. A "
                    "vasculite estava respondendo: a hemoptise havia cessado "
                    "no terceiro dia e o pulmão nunca voltou a piorar. "
                    "Nenhuma das decisões que levaram ao óbito era sobre o "
                    "diagnóstico.",
        consequencias=[
            consequencia(
                chave="escalonou",
                titulo="Escalonou o antibiótico em vez de investigar o sangramento",
                quando={"escolheu": ["b_dia2", 0]}, dias=3, tfg=6,
                porque="Trinta e seis horas é cedo para declarar falha de "
                       "antibiótico numa pneumonia comunitária, e nenhum "
                       "espectro retém sangue no alvéolo. Foram 48 horas a "
                       "mais de sangramento e de creatinina subindo, com "
                       "crescentes celulares em formação."),
            consequencia(
                chave="corticoide_antes_das_provas",
                titulo="Imunossuprimiu antes de colher qualquer prova",
                quando={"escolheu": ["b_dia2", 2]}, dias=2, tfg=2,
                porque="Parou o sangramento, e isso conta. Mas toda cultura "
                       "colhida a partir dali foi colhida sob corticoide, e o "
                       "negativo delas vale menos justamente quando se "
                       "precisa dele para justificar o que já foi feito."),
            consequencia(
                chave="febre_intensificou",
                titulo="Leu a febre do quinto dia como recidiva da vasculite",
                quando={"escolheu": ["b_febre", 1]}, dias=14, tfg=14,
                porque="A hemoptise havia cessado, o pulmão não piorou e a "
                       "procalcitonina subiu de 0,3 para 3,1. Intensificar a "
                       "imunossupressão sobre uma bacteremia com a porta de "
                       "entrada ainda no pescoço levou a choque séptico e a "
                       "três sessões de diálise."),
            consequencia(
                chave="febre_suspendeu",
                titulo="Suspendeu toda a imunossupressão",
                quando={"escolheu": ["b_febre", 2]}, dias=6, tfg=9,
                porque="Quarenta e oito horas sem corticoide bastaram para o "
                       "alvéolo voltar a sangrar e a creatinina voltar a "
                       "subir. Tratar a infecção e manter a indução era "
                       "possível."),
            consequencia(
                chave="cfx_ajustada",
                titulo="Escolheu ciclofosfamida, com a conta feita",
                quando={"escolheu": ["b1", 1]}, dias=5, tfg=8,
                porque="Tão eficaz quanto o esquema com rituximabe, e o nadir de "
                       "1.900 neutrófilos ficou onde a dose corrigida prevê. "
                       "Custa mais vigilância e mais dias, e o preço é da "
                       "droga, não de um erro de conduta."),
            consequencia(
                chave="cfx_plena",
                titulo="Escolheu ciclofosfamida sem a correção de dose",
                quando={"escolheu": ["b1", 2]}, dias=13, tfg=12,
                porque="Os metabólitos ativos saem por via renal, e com "
                       "filtração de 14 mL/min a exposição de 15 mg/kg é bem "
                       "maior do que a pretendida. A vasculite respondeu igual "
                       "nos três caminhos; o que mudou foi a medula, e a "
                       "bacteremia encontrou 210 neutrófilos em vez de 1.900."),
        ],
    ),

    pg('referencias', 'Fontes e limites',
       'Paciente, valores e percursos são ficcionais. A cena de abertura é uma '
       'ilustração gerada por inteligência artificial para este caso; não é '
       'fotografia nem retrata pessoa real.',
       'KDIGO 2024 para vasculite associada ao ANCA (indução, troca '
       'plasmática, profilaxias) e EULAR 2022. PEXIVAS //(N Engl J Med. '
       '2020;382:622-31)//; CYCLOPS //(Ann Intern Med. 2009;150:670-80)//; '
       'RAVE e RITUXVAS //(N Engl J Med. 2010;363:221-32 e 211-20)//; ADVOCATE '
       '//(N Engl J Med. 2021;384:599-609)//; Berden //(J Am Soc Nephrol. '
       '2010;21:1628-36)//; Nasr e cols. //(Kidney Int. 2013;83:792-803)// '
       'para a glomerulonefrite associada à infecção no adulto; CDC, '
       'tratamento da estrongiloidíase (ivermectina 200 µg/kg por dois dias).',
       'Imagens de outros pacientes, de licença aberta, com setas '
       'adicionadas: radiografia, Samir, CC BY-SA 3.0; ultrassom renal, '
       'Hansen, Nielsen e Ewertsen, CC BY 4.0; sedimento, Rian Kabir, CC BY '
       '2.0; tomografia dos seios, 511KeV, CC BY-SA 4.0; ecocardiograma, '
       'Kjetil Lenes, domínio público; tomografia de tórax, Hellerhoff, CC '
       'BY-SA 4.0; glomérulo, Nephron, CC BY-SA 3.0; imunofluorescência, Simon '
       'Caulton, CC BY-SA 3.0; corpúsculo renal, Michał Komorniczak, CC BY-SA '
       '3.0, números originais retirados; pele das pernas, James Heilman, MD, '
       'CC BY-SA 3.0. Todas no Wikimedia Commons, com setas adicionadas; '
       'endereços completos em img/CREDITOS.md.'),
]


# ═══════════════ o que a revisão cobra, quando não há mais o que decidir ══════

REVISAO = []

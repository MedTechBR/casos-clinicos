"""Caso ficcional para raciocínio clínico em residência de clínica médica.

Revisão editorial: integração de dados, seleção limitada de exames e
explicações após a resposta. Fontes clínicas ao final deste arquivo.
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
    """Alternativas curtas e explicação única após a seleção limitada."""
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
    cerco = quadro("Proteção durante a indução",
        p("Colher HBsAg e anti-HBc, anti-HCV e anti-HIV em paralelo ao tratamento urgente, sem atrasá-lo para esperar resultados; ivermectina 200 "
          "µg/kg por dois dias iniciada prontamente pela exposição. Profilaxia com sulfametoxazol-trimetoprima **400/80 "
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
         kicker="Caso interativo · 6 perguntas · 3 decisões",
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
                   ('Neurológico', 'Orientado. Força proximal e dorsiflexão dos pés preservadas; '
                    'sensibilidade distal sem assimetria, reflexos patelares e aquileus presentes. Marcha não testada, pela '
                    'dispneia.')),
           so_kicker=True),

    painel('res1', 'Primeiros exames', 'Sangue', [
        ex('Hemoglobina / hematócrito', '7,8 g/dL / 23,6% {{(13,9 g/dL há dois meses)}}', 'Hb 13,5–17,5 g/dL', True),
        ex('VCM', '88 fL', '80–100 fL'),
        ex('Leucócitos', '14.200/mm³ · neutrófilos 82%', '4.000–11.000/mm³', True),
        ex('Plaquetas', '468.000/mm³', '150.000–450.000/mm³', True),
        ex('Ureia / creatinina', '118 / 3,8 mg/dL {{(creatinina 1,4 há seis semanas)}}', 'até 42 / 1,3 mg/dL', True),
        ex('Sódio / potássio / cloro', '136 / 5,4 / 104 mmol/L', 'Na 135–145 · K 3,5–5,0 · Cl 98–107', True),
        ex('Albumina', '2,9 g/dL', '3,5–5,0 g/dL', True),
        ex('Proteína C reativa', '186 mg/L', 'até 5 mg/L', True),
    ], introducao='Três pares de hemoculturas foram colhidos antes de qualquer '
                  'antibiótico.'),

    painel('res1b', 'Primeiros exames', 'Gasometria, urina e outros', [
        ex('Gasometria arterial em ar ambiente', 'pH 7,29 · pCO₂ 32 · pO₂ 56 mmHg · HCO₃ 15 mmol/L · lactato 1,6 mmol/L', '—', True),
        ex('Urina, tira e sedimento automatizado', 'Densidade 1.018 · sangue +++ · proteína ++ · 60 hemácias e 6 leucócitos por campo · sem bacteriúria · sem cilindros na leitura automatizada', '—', True),
    ]),

    pg('reavaliacao_rotina', 'Reavaliação na emergência',
       'A equipe revê o hemograma e os exames de dois meses antes: a hemoglobina caiu para 7,8 e a creatinina subiu para 3,8. A urina inicial mostra sangue e proteína. Ele permanece dispneico; oxigênio e monitorização já estão em curso, com avaliação seriada da via aérea, da perfusão e da necessidade de transfusão.',
       'A anemia e a lesão renal motivam reticulócitos, esfregaço, DHL, bilirrubina e Coombs, para avaliar produção e possíveis sinais de hemólise. A proteína na tira leva à quantificação urinária. Esses pedidos dirigidos são feitos nas primeiras horas, sem interromper o suporte ou aguardar resultados para tratar a suspeita infecciosa; a radiografia é realizada em paralelo.'),

    painel('dirigidos_anemia_rim', 'Investigação dirigida', 'Resultados nas primeiras horas', [
        ex('Reticulócitos', '2,1%', '0,5–2,5%'),
        ex('DHL / bilirrubina total', '210 U/L / 0,6 mg/dL', 'até 250 U/L / até 1,2 mg/dL'),
        ex('Relação proteína/creatinina urinária', '1,4 g/g', 'abaixo de 0,2 g/g', True),
        ex('Esfregaço de sangue periférico', 'Hemácias normocíticas, sem esquizócitos', 'sem esquizócitos'),
        ex('Coombs direto', 'Negativo', 'negativo'),
    ]),

    estudo('rx_adm', 'Radiografia de tórax na admissão',
        'Radiografia feita na chegada, com ele sentado no leito. Descreva a '
        'distribuição das opacidades antes de ler os achados.',
        IMG / 'rx_torax_alveolar.jpg',
        'Radiografia.',
        'Samir · Wikimedia Commons · CC BY-SA 3.0 · recorte prévio e setas adicionadas',
        [
         ((308, 427), (110, 345), '**Opacidades alveolares** no pulmão direito, mais densas nos campos médio e inferior.', 12),
         ((704, 430), (912, 320), 'O mesmo padrão no **pulmão esquerdo**: a doença é bilateral.', -12),
         ((620, 160), (760, 60), '**Ápices relativamente poupados**: o predomínio é central e inferior.', 12),
        ],
        ['Opacidades alveolares bilaterais, em campos médios e inferiores, sem '
         'derrame pleural e sem aumento da área cardíaca.']),

    Q('p1', 1,
      'Como você interpreta a gasometria da admissão? Selecione duas conclusões.', [
      ('Acidose metabólica com hiato aumentado e compensação esperada', True),
      ('Defeito de troca gasosa além do distúrbio ácido-básico', True),
      ('Acidose metabólica hiperclorêmica isolada', False),
      ('Acidose respiratória somada à metabólica', False),
      ('Acidose lática como principal origem do hiato', False),
      ('Hipoventilação como principal causa da hipoxemia', False),
     ], [
      ('Ácido-básico', 'Hiato = 136 − 104 − 15 = 17; corrigido pela albumina, cerca de 20 mmol/L. Winters prevê pCO₂ de 30,5 ± 2; 32 cabe na faixa, sem acidose respiratória adicional. Lactato 1,6 não sustenta acidose lática como causa principal, embora não exclua infecção.'),
      ('Oxigenação', 'Em ar ambiente e próximo ao nível do mar, PAO₂ ≈ 110 e PaO₂ = 56: gradiente de cerca de 54 mmHg. A pCO₂ baixa indica aumento da ventilação; o gradiente elevado exige alteração de troca gasosa, sem distinguir sozinho sangue, pus ou edema.'),
     ]),

    estudo('us_adm', 'Ultrassonografia renal',
        'Pedida na chegada, pela creatinina de 3,8 mg/dL. Antes de interpretar '
        'a urina, a pergunta é se há obstrução ou rim pequeno de doença antiga.',
        IMG / 'us_rim.jpg',
        'Rim. Asteriscos da fonte: um, coluna de Bertin; dois, pirâmide; três, córtex; quatro, seio renal. Cálipers da imagem original.',
        'Hansen, Nielsen e Ewertsen · Wikimedia Commons · CC BY 4.0 · recorte prévio e setas adicionadas',
        [
         ((495, 288), (620, 105), '**Córtex** renal (três asteriscos), de espessura preservada.', 12),
         ((472, 357), (330, 160), '**Pirâmide medular** (dois asteriscos), hipoecoica: a diferenciação entre córtex e medula está preservada.', 12),
         ((447, 400), (720, 550), '**Seio renal** (quatro asteriscos), ecogênico, sem dilatação do sistema coletor.', -12),
        ],
        ['Rins de 11,2 e 11,0 cm, córtex de espessura preservada, sem '
         'hidronefrose (laudo do caso).']),

    Q('p2', 2,
      'Na primeira reavaliação, quais dois exames você prioriza?', [
      ('Sedimento urinário com microscopia manual', True),
      ('Tomografia dos seios da face', True),
      ('Fração de excreção de sódio', False),
      ('Cintilografia renal', False),
      ('Eletroforese de proteínas séricas', False),
      ('Angiotomografia das artérias renais', False),
     ], [('Os dois pedidos', 'Sedimento manual: procura acantócitos e cilindros que a leitura automatizada pode perder, distinguindo sangramento glomerular de causas urológicas. TC dos seios: sintomas persistentes após dois antibióticos justificam avaliar extensão e complicação, sem atribuir causa apenas pelo velamento.'), ('Por que adiar os demais', 'FENa: isoladamente não localiza esta lesão; valores baixos também ocorrem na glomerulonefrite. Cintilografia: sem dilatação no ultrassom ou outra pista de obstrução, tem baixo rendimento agora. Eletroforese: não é a primeira resposta à hematúria de evolução rápida. Angio-TC renal: não há quadro de infarto ou doença renovascular, e o contraste acrescenta risco na lesão renal.'), ('Diagnósticos a comparar', 'Hematúria pode vir do glomérulo ou das vias urinárias. Cilindros hemáticos e acantócitos favorecem origem glomerular; sua ausência não a exclui. O sedimento orienta a investigação, mas ainda não separa infecção, autoimunidade e outras causas.')]),

    estudo('sedimento', 'Sedimento urinário, leitura manual',
        'A leitura automatizada não procura dismorfismo nem cilindro. A equipe '
        'pede a leitura manual do sedimento da admissão.',
        IMG / 'sedimento_cilindro.jpg',
        'Sedimento. A fonte identifica o cilindro como hemático; ampliada, a foto não resolve hemácias uma a uma.',
        'Rian Kabir · Wikimedia Commons · CC BY 2.0 · setas adicionadas',
        [
         ((457, 493), (200, 380), '**Borda** lisa e paralela: o cilindro é o molde do lúmen de um túbulo.', 12),
         ((500, 500), (720, 700), '**Conteúdo celular** denso e acastanhado, preso na matriz do cilindro.', -12),
         ((745, 262), (880, 110), '**Extremidade** arredondada, onde o molde se desprendeu do túbulo.', 12),
        ],
        ['Hemácias dismórficas em 40%, com acantócitos, e cilindros hemáticos '
         '(laudo do caso).']),

    estudo('tc_seios', 'Tomografia dos seios da face',
        'Pela obstrução nasal de oito semanas que não cedeu a dois '
        'antibióticos, a equipe pede tomografia dos seios da face, à procura '
        'de um foco de infecção.',
        IMG / 'tc_seio_maxilar.jpg',
        'Corte axial, em janela óssea. O lado esquerdo do paciente está à direita da imagem.',
        credito_meta(IMG / 'tc_seio_maxilar.jpg.json'),
        [
         ((596, 176), (820, 90), '**Seio maxilar esquerdo** velado por conteúdo de partes moles, com pequena bolha de ar.', -12),
         ((429, 171), (250, 90), '**Seio maxilar direito** aerado, de paredes finas.', 12),
         ((504, 143), (560, 30), '**Septo nasal** íntegro, sem perfuração.', 12),
        ],
        ['Velamento do seio maxilar esquerdo, sem erosão das paredes ósseas. '
         'Septo nasal íntegro.']),

    pg('hipotese', 'A hipótese da equipe',
       'Febre, infiltrado bilateral, leucocitose e proteína C reativa de 186 '
       'mg/L num homem com sinusite arrastada. No rim, glomerulonefrite com '
       'cilindros hemáticos. A equipe registra pneumonia grave multilobar com '
       'glomerulonefrite associada à infecção, e endocardite a afastar.',
       'Desde a chegada recebe oxigênio e monitorização, com avaliação imediata da necessidade de suporte ventilatório. Sem aguardar a rodada dirigida, inicia ceftriaxona 2 g e azitromicina 500 mg ao dia, oxigênio por '
       'cateter nasal a 4 L/min, e pede ecocardiograma transtorácico, '
       'complemento e antígenos urinários de pneumococo e legionela.'),

    pagina('gn_infeccao', 'Discussão', 'A glomerulonefrite associada à infecção',
        p('Na criança, o modelo é a glomerulonefrite pós-estreptocócica, que '
          'aparece uma a três semanas depois da faringite ou da infecção de '
          'pele, quando a infecção já passou. No adulto, sobretudo acima dos 60 '
          'anos, com diabetes ou câncer, o estafilococo passou à frente, e a '
          'nefrite costuma surgir com a infecção ainda em curso: pele, osso, '
          'pulmão, cateter ou endocardite. Por isso a equipe fala em '
          'glomerulonefrite associada à infecção, e não pós-infecciosa.'),
        p('O C3 está baixo na maioria dos casos e é a pista sorológica mais '
          'útil, mas um C3 normal não a exclui, sobretudo nas formas '
          'estafilocócicas. Quem confirma é a biópsia, com depósitos granulares '
          'de C3, às vezes com IgA dominante.'),
        p('O tratamento é o da infecção, e a recuperação renal leva semanas, às '
          'vezes incompleta no idoso. Cada exame pedido na chegada testa um '
          'pedaço da hipótese: o complemento, o rim; os antígenos urinários, o '
          'pulmão; as hemoculturas e o ecocardiograma, a endocardite.')),

    estudo('eco', 'Ecocardiograma transtorácico',
        'Feito no primeiro dia, à procura de vegetação. Localize o septo e as '
        'duas valvas atrioventriculares antes de ler o laudo.',
        IMG / 'eco_4camaras.jpg',
        'Corte apical de quatro câmaras, na orientação da fonte: ápice para baixo, coração esquerdo à direita da imagem.',
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
        ex('HBsAg, anti-HBc, anti-HCV e anti-HIV', 'Não reagentes', 'não reagentes'),
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
       'contraste. Pela hipoxemia e pelo sangramento ativo, é transferido para cuidado intensivo, com oxigênio titulado e avaliação de via aérea; intubação não será adiada se houver fadiga ou hipoxemia refratária. Recebe uma unidade de concentrado de hemácias, com reavaliação clínica e da hemoglobina após a transfusão.'),

    estudo('tc_torax', 'Tomografia de tórax',
        'Tomografia do segundo dia, pela piora da oxigenação. Descreva o '
        'padrão e a distribuição antes de propor o que ocupa o alvéolo.',
        IMG / 'tc_torax_vidro_fosco.jpg',
        'Cortes axiais e reconstruções, em janela de pulmão.',
        'Hellerhoff · Wikimedia Commons · CC BY-SA 4.0 · setas adicionadas',
        [
         ((100, 186), (330, 40), '**Vidro fosco** no lobo superior direito, entremeado de pulmão aerado.', -12),
         ((68, 771), (300, 830), 'O mesmo padrão, mais denso, nas **bases**, com áreas de consolidação.', 12),
         ((533, 235), (640, 70), 'Na reconstrução coronal, o **pulmão direito** tomado do ápice à base.', -12),
        ],
        ['Opacidades em vidro fosco difusas e bilaterais, com áreas de '
         'consolidação. Sem nódulos escavados e sem derrame pleural.']),

    pagina('alveolo', 'Discussão', 'O sangue que não saiu',
        p('A equipe junta a tomografia à evolução do segundo dia e registra '
          'hemorragia alveolar difusa. Cerca de 110 mL expectorados em dois dias '
          'não explicam a queda da hemoglobina de 13,9, dois meses antes, para '
          '6,9 g/dL, sem melena, hematêmese nem epistaxe volumosa. O sangue '
          'ficou no espaço aéreo.'),
        p('Alvéolo cheio de sangue é perfundido e não ventilado: é shunt, que '
          'responde mal ao aumento do oxigênio ofertado, como na passagem do '
          'cateter a 4 L/min para a máscara com reservatório. O vidro fosco '
          'difuso é compatível e inespecífico. A hemoptise sustenta, mas falta '
          'em até um terço das hemorragias alveolares.'),
        p('O que não está na tomografia também conta. Não há derrame, e não há '
          'nódulos escavados, que apontariam para êmbolo séptico, micobactéria '
          'ou fungo. Na hemorragia recente, a capacidade de difusão do monóxido '
          'de carbono sobe, porque a hemoglobina dentro do alvéolo capta o gás; '
          'ninguém mede isso em quem está de máscara, mas a lógica ajuda a '
          'separar sangue de água e de pus.')),

    bifurcacao("b_dia2", "Decisão",
        "Piora respiratória no segundo dia",
        "Trinta e seis horas de ceftriaxona e azitromicina, mais oxigênio, mais "
        "hemoptise e 0,9 g/dL a menos de hemoglobina. As culturas ainda não "
        "têm resultado final. O suporte respiratório e transfusional já está em curso. Qual investigação você prioriza?",
        [
            caminho("Ampliar a cobertura antibiótica",
                    "r_escalona",
                    "É a leitura de que o espectro foi insuficiente, e germe "
                    "resistente existe. Mas trinta e seis horas é cedo para "
                    "declarar falha numa pneumonia comunitária, e antibiótico "
                    "mais largo não retém sangue no alvéolo."),
            caminho("Realizar lavado broncoalveolar", "r_investiga",
                    "A broncoscopia com lavado mostra de onde vem o sangue, e a "
                    "microbiologia do lavado investiga infecção concomitante. A coleta depende da segurança respiratória e não deve atrasar tratamento urgente. O antibiótico continua enquanto se reavalia a hipótese."),
            caminho("Iniciar corticoide em dose imunossupressora agora",
                    "r_corticoide",
                    "Na hemorragia alveolar ameaçadora, o tratamento pode começar enquanto a causa é investigada. Hemoculturas pré-antibiótico já foram colhidas; revisar infecção e obter outras amostras quando seguro continua necessário."),
        ],
    ),

    pg("r_escalona", "Reavaliação nas horas seguintes",
       "A cobertura é ampliada, mas nas horas seguintes persiste hemoptise e a oxigenação exige máscara com reservatório. A hemoglobina é reavaliada após a primeira unidade; pelo sangramento persistente, recebe uma segunda unidade, com controle de volume e resposta. Creatinina 4,6 mg/dL, diurese de 380 mL nas últimas 24 horas.",
       "No cuidado intensivo, a equipe reconhece que ampliar antibióticos não trata a possível capilarite e retoma imediatamente a investigação e o tratamento da síndrome pulmão-rim, sem esperar cinco dias de culturas.",
       segue="virada"),

    pg("r_investiga", "Ainda no segundo dia",
       "Após estabilização respiratória e avaliação conjunta da equipe intensiva, realiza-se broncoscopia com suporte de via aérea apropriado. Não há lesão endobrônquica nem ponto focal de sangramento.",
       "As alíquotas sequenciais no mesmo segmento ficam progressivamente hemorrágicas. A bacterioscopia inicial é negativa; culturas do lavado permanecem pendentes e foram obtidas após antibiótico. Uma segunda unidade de hemácias é administrada pelo sangramento persistente, com reavaliação após a transfusão. A coleta não é condição para iniciar tratamento se houver nova deterioração.",
       segue="virada"),

    pg("r_corticoide", "Tratamento urgente e investigação paralela",
       "Metilprednisolona 500 mg/dia é iniciada pela hemorragia alveolar ameaçadora, após discussão conjunta. Mantêm-se suporte intensivo e avaliação infecciosa; recebe uma segunda unidade de hemácias pelo sangramento persistente, com controle da resposta e do volume.",
       "O corticoide não invalida as hemoculturas da admissão, colhidas antes do antibiótico. Amostras posteriores precisam ser interpretadas considerando sobretudo o antibiótico já recebido e a sensibilidade de cada teste. Resposta ao corticoide não confirma vasculite nem exclui infecção.",
       segue="virada"),

    # ══════════════════════ a virada ══════════════════════

    pg("virada", "Reavaliação no segundo dia",
       "As hemoculturas pré-antibiótico seguem sem crescimento preliminar; só terão resultado final ao completar a incubação. Antígenos urinários negativos e complemento normal não excluem infecção. A creatinina está em 4,6 mg/dL.",
       "Durante a internação surge dificuldade nova para mover o pé direito. Sem colocá-lo de pé enquanto está hipoxêmico, a equipe repete o exame neurológico e examina a pele."),

    pagina("reexame", "Novo exame à beira do leito", "",
        topicos(
            ("Evolução", "Na admissão, a dorsiflexão e a sensibilidade distal estavam preservadas. Agora ele relata dificuldade nova para elevar o pé direito, surgida nas últimas horas."),
            ("Neurológico", "Dorsiflexão direita 2/5, eversão 3/5 e reflexo aquileu direito reduzido. Há também hipoestesia nova no território ulnar esquerdo. Sem nível sensitivo; a distribuição multifocal exige investigação de neuropatia, sem atribuição automática a uma raiz única."),
            ("Pele", "As pápulas dos pés se multiplicaram e subiram para as pernas: lesões elevadas de 2 a 8 mm, algumas com centro escurecido, que não desaparecem à digitopressão."),
        ), so_kicker=True),

    estudo('purpura', 'A pele das pernas',
        'Antes de ler os achados, descreva o tamanho, o centro das lesões e onde elas se concentram.',
        IMG / 'purpura_perna.jpg',
        'Lesões cutâneas nas pernas e no dorso do pé.',
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

    Q('p5', 3,
      'Após a broncoscopia e a reavaliação clínica, quais quatro exames você solicita?', [
      ('Anti-membrana basal glomerular', True),
      ('Biópsia renal com imunofluorescência', True),
      ('Anti-MPO', True),
      ('Anti-PR3', True),
      ('Repetir C3', False),
      ('Biópsia de nervo periférico', False),
      ('Difusão pulmonar de monóxido de carbono', False),
     ], [
      ('Exames que mudam o caminho', 'Anti-MBG (anticorpo contra a membrana basal glomerular): identifica uma sobreposição em que a troca plasmática ganha prioridade. Biópsia renal com IF: separa depósitos lineares, granulares e padrão pauci-imune, além de medir atividade e cronicidade. MPO/PR3: anticorpos contra proteínas dos neutrófilos, que ajudam a interpretar o conjunto de manifestações; ANCA isolado não substitui contexto e tecido.'),
      ('Exames de menor rendimento agora', 'Repetir C3/C4: já normais, não diferencia com segurança os mecanismos nem exclui imunocomplexos. Biópsia de nervo: pode demonstrar vasculite, mas o rim oferece tecido do órgão ameaçado e classificação por IF. DLCO: pode subir com sangue alveolar, mas não identifica a causa e é pouco viável nesta insuficiência respiratória.'),
     ]),

    painel("res_mec", "O mecanismo", "Biópsia e sorologias", [
        ex('Anticorpo anti-membrana basal glomerular', 'Não reagente {{(resultado em horas)}}', 'não reagente'),
        ex('Anti-MPO', '148 U/mL (positivo)', 'negativo', True),
        ex('Anti-PR3', 'Não reagente', 'não reagente'),
        ex('FAN / anti-DNA nativo', 'Não reagentes', 'não reagentes'),
        ex('Crioglobulinas', 'Não detectadas', 'não detectadas'),
        ex('Biópsia renal · microscopia óptica', '24 glomérulos · crescentes celulares em 15 (62%) · necrose fibrinoide segmentar · fibrose intersticial em 10% do córtex', 'sem proliferação extracapilar', True),
        ex('Biópsia renal · imunofluorescência', 'Sem depósitos significativos de IgG, IgA, IgM, C3 ou C1q · padrão pauci-imune · sem depósito linear', 'sem depósitos', True),
    ], introducao='Anti-MBG, anti-MPO e anti-PR3 são enviados com urgência no segundo dia e retornam no dia seguinte. Diante da deterioração compatível, o corticoide começa ainda no segundo dia, caso não tenha sido iniciado no ramo escolhido. Com anti-MPO positivo, a indução com rituximabe e/ou ciclofosfamida é definida sem aguardar a biópsia, conforme KDIGO 2024. Após estabilização e avaliação do risco hemorrágico, o rim é biopsiado; o laudo sai três dias depois. O painel reúne os resultados obtidos em momentos distintos; as telas seguintes detalham essa decisão, sem acrescentar espera clínica.'),

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
        'Localize o tufo, a cápsula e o que ocupa o espaço entre eles.',
        IMG / "glomerulo_crescente.jpg",
        'Coloração PAS.',
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
        'Revisão ilustrativa do ANCA já disponível no terceiro dia; não se espera esta imagem para tratar. Neutrófilos fixados em etanol recebem o soro do '
        'paciente e um anticorpo antiglobulina marcado: onde a fluorescência '
        'se acumula, está o alvo.',
        IMG / 'panca_imunofluorescencia.jpg',
        'Neutrófilos · imagem ilustrativa.',
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

    Q('p6', 4,
      'Quais duas conclusões você tira da biópsia e dos resultados disponíveis?', [
      ('Vasculite associada ao ANCA integra rim, pulmão, pele e nervos', True),
      ('Crescentes celulares e pouca fibrose indicam componente potencialmente reversível', True),
      ('Glomerulonefrite associada à infecção permanece a explicação principal pela febre e PCR elevada', False),
      ('Doença anti-MBG soronegativa é a principal hipótese pela combinação de hemorragia e crescentes', False),
      ('A perda funcional decorre predominantemente de cicatriz renal, pelo percentual de crescentes', False),
      ('Vasculite restrita ao rim com pneumonia concomitante explica melhor o acometimento pulmonar', False),
     ], [
      ('Integração', 'IF pauci-imune, anti-MPO e envolvimento simultâneo de rim, alvéolo, pele e nervos favorecem vasculite sistêmica ANCA. Crescentes celulares e apenas 10% de fibrose apontam atividade potencialmente tratável; a creatinina elevada ainda implica risco renal importante.'),
      ('Hipóteses concorrentes', 'Febre e PCR alta também acompanham vasculite; culturas negativas e ausência de depósitos tornam glomerulonefrite infecciosa menos provável. Anti-MBG soronegativa é possível, mas esperaria depósito linear, ausente aqui. Crescentes celulares não equivalem a cicatriz. Separar rim e pulmão exige duas causas quando a hemorragia alveolar e as lesões extrarrenais integram o mesmo processo.'),
     ]),

    pagina("diagnostico", "O diagnóstico", "",
        p("Glomerulonefrite crescêntica pauci-imune, anti-MPO de 148 U/mL e "
          "hemorragia alveolar: é **vasculite associada ao ANCA**, no conjunto de manifestações "
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

    # ═══════════ o tratamento, e a segunda virada ═══════════

    bifurcacao("b1", "Decisão",
        "Com que esquema você induz a remissão?",
        "Creatinina de 4,6 mg/dL (407 µmol/L), filtração estimada de 14 "
        "mL/min/1,73 m² por CKD-EPI 2021, 78 kg, 63 anos, hemorragia alveolar "
        "recente e ameaçadora. Esta decisão é tomada assim que a sorologia retorna, sem aguardar o laudo renal. O glicocorticoide é comum aos três caminhos; a segunda "
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
        segue="p7",
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
        segue="p7",
    ),

    pagina("t_cfx_plena", "A prescrição", "O que foi prescrito: caminho C",
        p("**Ciclofosfamida endovenosa em pulso, 15 mg/kg.** Com 78 kg, "
          "**1,17 g** por pulso. É a dose de indução dos ensaios sem as duas "
          "subtrações, nem a da idade entre 60 e 70 anos, nem a da "
          "creatinina entre 300 e 500 µmol/L. Os metabólitos ativos são "
          "eliminados por via renal, e com filtração de 14 mL/min a "
          "exposição a 1,17 g é maior que a dos ensaios."),
        segue="p7",
    ),

    Q('p7', 5,
      'Quais duas medidas preventivas você inclui na prescrição?', [
      ('Tratar presuntivamente estrongiloidíase pela exposição ao solo e pelo corticoide urgente', True),
      ('Iniciar prevenção de pneumocistose considerando função renal e potássio', True),
      ('Reservar prevenção de pneumocistose para linfopenia após o primeiro ciclo', False),
      ('Completar HBsAg com anti-HBs para definir o risco de reativação antes do rituximabe', False),
      ('Iniciar sulfametoxazol-trimetoprima no esquema habitual e ajustar se a creatinina subir mais', False),
      ('Aguardar parasitológico de fezes antes de tratar estrongiloidíase na ausência de sintomas digestivos', False),
     ], [
      ('Prevenção desde a indução', 'Exposição ao solo em área endêmica e corticoide urgente favorecem ivermectina presuntiva conforme avaliação local. Rituximabe ou ciclofosfamida justificam prevenção de pneumocistose desde a indução, sem depender de linfopenia documentada.'),
      ('Escolha e rastreio', 'HBsAg e anti-HBs não substituem anti-HBc para pesquisar infecção passada e risco de reativação. A função renal já está muito reduzida e o potássio chegou a 5,4: escolher e ajustar o esquema agora é mais seguro que aguardar nova piora sob trimetoprima. Estrongiloidíase pode ser assintomática e o parasitológico tem sensibilidade limitada; esperar seu resultado pode deixar o pulso sem proteção.'),
     ], segue='esquema'),

    pagina("esquema", "A prescrição", "O que é igual nos três caminhos",
        grade(*_esquema_comum(), colunas=2),
        segue="dia3",
    ),

    pg("dia3", "Terceiro dia de indução",
       "Setenta e duas horas depois do primeiro pulso de metilprednisolona, a "
       "hemoptise cessou. O oxigênio caiu de máscara com reservatório para "
       "cateter nasal a 3 L/min, com saturação de 95%. A hemoglobina "
       "chegou a 8,6 g/dL após duas unidades de concentrado de "
       "hemácias durante a piora do segundo dia, sem nova queda.",
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

    Q('p8', 6,
      'Qual hipótese explica melhor a intercorrência do quinto dia?', [
      ('Infecção de corrente sanguínea relacionada ao cateter', True),
      ('Recidiva de capilarite pulmonar', False),
      ('Hemólise transfusional tardia', False),
      ('Tromboembolismo pulmonar', False),
      ('Toxicidade medular da ciclofosfamida como causa já demonstrada', False),
     ], [('O que discrimina', 'Calafrios, hipotensão e inflamação no sítio do cateter priorizam infecção relacionada ao dispositivo; a procalcitonina reforça, mas não comprova. Culturas periféricas e do cateter ajudam a confirmar sem atrasar tratamento.'), ('Concorrentes', 'Capilarite perde força com hemoptise cessada e oxigenação estável. Hemólise tardia é temporalmente possível após a transfusão, mas faltam nova anemia ou sinais de hemólise. TEP permanece possível pela imobilidade, sem explicar tão bem o foco local. O D5 não demonstra nadir por ciclofosfamida e essa exposição varia entre os caminhos; seria necessário hemograma.'), ('Como rever a hipótese', 'Febre durante imunossupressão exige comparar infecção, atividade da doença e reação ao tratamento. O exame do acesso, a evolução pulmonar e o hemograma mudam o peso dessas hipóteses; nenhuma se confirma apenas pelo dia em que a febre apareceu.')]),

    pagina('calendario', 'Discussão', 'O calendário da infecção na indução',
        p('Cada complicação infecciosa da imunossupressão tem a sua janela. Nas '
          'primeiras semanas, a infecção que aparece é a do hospital: cateter, '
          'pneumonia associada à assistência, urina, pele e diarreia por '
          '//Clostridioides difficile//. Os germes esperados são os que entram '
          'pela pele e pelos dispositivos, e os estafilococos vêm à frente.'),
        p('A ciclofosfamida derruba os neutrófilos entre o 10º e o 14º dia de '
          'cada pulso, e a contagem se recupera em cerca de uma semana. O '
          'rituximabe não produz esse nadir; a queda de imunoglobulinas que ele '
          'causa é tardia, de meses.'),
        p('O que depende da imunidade celular vem depois: pneumocistose e '
          'reativação de citomegalovírus se concentram entre o primeiro e o '
          'sexto mês, com o linfócito deprimido pelo glicocorticoide em dose '
          'alta. É a janela que a profilaxia com sulfametoxazol-trimetoprima '
          'cobre, e por isso ela segue por pelo menos seis meses.')),

    bifurcacao("b_febre", "Decisão",
        "Febre durante a indução",
        "38,9 °C com calafrio, hipotensão que respondeu a volume, "
        "procalcitonina de 0,3 para 3,1, cateter central com sítio inflamado. "
        "Sem nova hemoptise e sem piora pulmonar. Hemoculturas pareadas são colhidas antes do antibiótico empírico, sem atrasá-lo; essas medidas são comuns aos percursos. Qual decisão sobre o foco ou a imunossupressão você prioriza?",
        [
            caminho("Retirar o cateter suspeito", "f_retira",
                    "Órgão-alvo estável, procalcitonina subindo e porta de "
                    "entrada visível. A procalcitonina não confirma a causa. Após garantir outro acesso, retirar o cateter faz parte do "
                    "tratamento."),
            caminho("Intensificar a imunossupressão, por recidiva da vasculite",
                    "f_intensifica",
                    "Tem lógica se a leitura for de doença descontrolada. Mas a "
                    "hemoptise cessou, o pulmão não piorou e a "
                    "procalcitonina subiu. O conjunto prioriza infecção; o marcador isolado não confirma nem exclui bacteremia."),
            caminho("Suspender toda a imunossupressão até esclarecer a febre",
                    "f_suspende",
                    "Parece prudente. Mas a vasculite acabou de ser controlada "
                    "e a crescente ainda é celular. Controlar a infecção exige reavaliar a próxima dose de imunossupressor; não implica suspender abruptamente todo o corticoide."),
        ],
    ),

    pg("f_retira", "Sétimo dia",
       "Cateter retirado; a ponta cultivou o mesmo agente das hemoculturas "
       "pareadas, //Staphylococcus aureus// sensível a oxacilina, com tempo "
       "diferencial de positivação compatível com origem no cateter. O "
       "ecocardiograma transesofágico não mostrou vegetação.",
       "A febre cedeu em 48 horas. O corticoide é mantido na menor dose necessária; as próximas doses da indução são reavaliadas conforme o controle da bacteremia.",
       segue="dia10"),

    pg("f_suspende", "Sétimo ao nono dia",
       "A febre cedeu com a retirada tardia do cateter e a oxacilina, no "
       "sétimo dia. No nono, após a suspensão do corticoide, voltou a "
       "hemoptise, dois episódios de cerca de 40 mL, e a saturação caiu para "
       "90% em cateter a 4 L/min. A hemoglobina caiu de 8,6 para 7,4 g/dL e a "
       "creatinina voltou a subir, de 4,2 para 4,8.",
       "A indução foi reiniciada no décimo dia, em dose plena, sobre um "
       "paciente que passou 48 horas sangrando de novo no alvéolo.",
       segue="dia10"),

    pg("f_intensifica", "Sétimo dia",
       "Metilprednisolona voltou a 1 g ao dia por três dias, sobre a "
       "bacteremia com foco ainda não controlado, apesar do antibiótico empírico. O cateter permaneceu. Em 24 horas a "
       "temperatura chegou a 39,6 °C, a pressão caiu para 78/44 mmHg e não "
       "respondeu a 2.000 mL de cristaloide. Lactato 4,8 mmol/L.",
       "As hemoculturas voltaram com //Staphylococcus aureus// em 2 de 2 "
       "pares. Ele foi transferido para a terapia intensiva em choque, com "
       "noradrenalina.",
       conforme=("b1", ["fi_grave", "fi_grave", "fi_obito"])),

    pg("fi_grave", "Do sétimo ao vigésimo dia",
       "Choque séptico por //S. aureus//, com foco em cateter mantido por 48 "
       "horas depois do primeiro pico febril. Noradrenalina por seis dias, "
       "oxacilina por 28 dias neste curso, com duração individualizada após revisão da bacteremia complicada, e três "
       "sessões de diálise durante o choque, por oligúria e acidose "
       "refratária.",
       "Sobreviveu. Saiu da terapia intensiva treze dias depois, com "
       "creatinina de 3,2 mg/dL e diurese recuperada, ainda dependente de "
       "oxigênio suplementar.",
       conforme=("b1", ["prealta_rituximabe", "prealta_cfx", "prealta_uti"])),

    fim("fi_obito", "Óbito na terceira semana de internação",
        'Neste curso ficcional, o choque séptico ocorreu com neutropenia grave, de **210 neutrófilos/mm³**, após ciclofosfamida sem ajuste para idade e função renal. O corticoide foi intensificado durante bacteremia já coberta por antibiótico empírico, mas com atraso na retirada do cateter suspeito.',
        "Evoluiu com disfunção de múltiplos órgãos e choque refratário a três "
        "drogas vasoativas. Faleceu no nono dia de bacteremia. A vasculite "
        "estava respondendo: a hemoptise havia cessado no terceiro dia de "
        "indução.",
        qualidade="pior",
        porque='A dose não ajustada aumenta o risco de toxicidade, mas neutropenia grave também pode ocorrer com dose ajustada. Neste percurso, a intensificação da imunossupressão e o atraso no controle do foco acompanharam a piora infecciosa apesar do antibiótico empírico. O óbito é um desfecho simulado, não consequência inevitável dessas escolhas.'),

    pg("dia10", "Décimo dia de indução",
       "O que vem a seguir depende do esquema de indução escolhido, e é aqui "
       "que os três caminhos deixam de ser o mesmo caso.",
       conforme=("b1", ["d10_rituximabe", "d10_cfx_ajustada", "d10_cfx_plena"])),

    pg("d10_rituximabe", "Décimo dia · caminho A",
       'No décimo dia deste percurso, o hemograma mostra 4.800 leucócitos/mm³ e 3.000 neutrófilos/mm³, sem neutropenia. Essas contagens são valores simulados, não uma resposta garantida ao esquema. O cateter foi identificado como foco da bacteremia; a imunossupressão contribui para o risco infeccioso.',
       "Completou as quatro doses semanais e catorze dias de oxacilina. A "
       "creatinina caiu de forma sustentada.",
       segue="prealta_rituximabe"),

    pg("d10_cfx_ajustada", "Décimo dia · caminho B",
       'No décimo dia deste percurso, o hemograma mostra 3.600 leucócitos/mm³ e 1.900 neutrófilos/mm³. São valores observados na simulação, não um nadir universal para 10 mg/kg. O hemograma é repetido duas vezes por semana; dose e momento do próximo pulso dependem da evolução das contagens, da função renal e do controle da infecção.',
       'Na evolução subsequente, a febre cedeu e o tratamento da bacteremia foi completado. O segundo pulso foi reprogramado após controle da infecção e revisão clínica e laboratorial.',
       segue="prealta_cfx"),

    pg("d10_cfx_plena", "Décimo dia · caminho C",
       "O hemograma do décimo dia mostra 900 leucócitos com 210 neutrófilos. "
       "A febre, que havia cedido com a oxacilina, voltou a 39,4 °C, agora com "
       "hipotensão que exigiu noradrenalina, e ele foi transferido para a "
       "terapia intensiva.",
       'Neste percurso, houve neutropenia grave após a dose não ajustada; a contagem de 1.900 do outro ramo não prevê o nadir de outros pacientes. Entraram antibiótico de amplo espectro e fator estimulador de colônias. Pela persistência da febre e pelo risco de neutropenia prolongada, acrescentou-se antifúngico empírico no quinto dia de neutropenia febril.',
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
        porque='Havia lesão ativa potencialmente tratável. Neste curso ficcional, houve recuperação sem diálise e sem neutropenia grave. O esquema combina rituximabe com dois pulsos ajustados de ciclofosfamida; esse resultado individual não demonstra superioridade sobre os outros esquemas nem elimina o risco infeccioso.'),

    fim("d_cfx_ajustada", "Alta sem diálise, com vigilância semanal",
        'Neste percurso, a creatinina estabilizou e a diurese se recuperou; ele sai sem diálise. O hemograma foi vigiado duas vezes por semana durante a bacteremia. A menor contagem registrada após o segundo pulso foi de 1.600 neutrófilos/mm³, um valor deste curso ficcional.',
        "Completou a oxacilina e os três primeiros pulsos de ciclofosfamida "
        "sem nova intercorrência infecciosa.",
        qualidade="melhor",
        porque='A ciclofosfamida ajustada é uma opção de indução para doença grave, com hemograma, função renal e toxicidades revistos antes de cada pulso. A recuperação desta simulação não permite comparar causalmente eficácia ou duração da internação entre esquemas. Riscos cumulativos e preferências individuais também orientam a escolha.'),

    fim("d_cfx_plena", "Alta após a terapia intensiva",
        'Neste curso ficcional, a hemoptise cessou no terceiro dia e a creatinina caiu. Houve treze dias de terapia intensiva, noradrenalina por quatro deles, antibiótico de amplo espectro, antifúngico empírico e fator estimulador de colônias.',
        'Saiu andando, após internação prolongada, com disfunção renal residual. Os valores deste percurso não estimam a diferença esperada entre tratamentos.',
        qualidade="pior",
        porque='A dose sem ajuste para idade e disfunção renal aumenta o risco de toxicidade hematológica. Neste percurso houve neutropenia grave e complicação infecciosa; a gravidade não pode ser atribuída exclusivamente à dose. Ajustar a prescrição reduz risco, sem garantir ausência de complicações.'),

    # ═══════════════ o fecho, igual para os três ramos ═══════════════

    pagina('retrospectiva', 'Pontos de ensino', '',
        pontos(
            'Rinossinusite que não responde a dois antibióticos corretos, com '
            'febre, artralgia e perda de peso, pede urina e creatinina. Aqui, '
            'seis semanas antes, a urina já tinha 12 hemácias por campo.',
            'A creatinina se lê contra o basal do paciente: de 1,0 para 1,4 '
            'mg/dL é perder um terço da filtração (por CKD-EPI 2021, de 85 '
            'para 56 mL/min/1,73 m²), mesmo perto da referência.',
            'Hematúria, proteinúria e cilindros hemáticos exigem investigação glomerular. A FENa isolada não substitui o sedimento nem confirma mecanismo pré-renal.',
            'Hemoglobina caindo sem sangramento externo, hipoxemia que '
            'responde mal ao oxigênio e vidro fosco difuso são hemorragia '
            'alveolar até prova em contrário; a hemoptise falta em um terço.',
            'Hemorragia alveolar com glomerulonefrite pede anti-MBG e ANCA '
            'assim que a síndrome é reconhecida, junto da investigação infecciosa: o resultado pode levar dias, e a '
            'crescente celular não espera. Com quadro compatível e ANCA positivo, não se aguarda biópsia para tratar a deterioração. A âncora infecciosa foi razoável; '
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
        p('Comparação dos percursos ficcionais. Dias e valores de função renal foram definidos pelo autor para esta simulação; não são estimativas de efeito causal, previsões individuais ou prova de superioridade de um esquema.'),
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
                quando={"escolheu": ["b_dia2", 0]}, dias=1, tfg=2,
                porque="Trinta e seis horas é cedo para declarar falha de "
                       "antibiótico numa pneumonia comunitária, e nenhum "
                       "espectro trata a capilarite. A reavaliação ocorreu em horas, com "
                       "sangramento e creatinina ainda em ascensão, com "
                       "crescentes celulares em formação."),
            consequencia(
                chave="febre_intensificou",
                titulo="Leu a febre do quinto dia como recidiva da vasculite",
                quando={"escolheu": ["b_febre", 1]}, dias=14, tfg=14,
                porque='Pulmão estável e cateter inflamado priorizavam infecção; procalcitonina isolada não a confirma. Neste percurso, apesar do antibiótico empírico, o foco permaneceu e houve choque e três sessões de diálise após intensificação da imunossupressão. Esses números são próprios da simulação.'),
            consequencia(
                chave="febre_suspendeu",
                titulo="Suspendeu toda a imunossupressão",
                quando={"escolheu": ["b_febre", 2]}, dias=6, tfg=9,
                porque='Neste percurso, houve nova hemorragia e piora renal após a suspensão. Isso não estabelece um prazo universal de recidiva. O controle da infecção e a dose necessária de corticoide devem ser reavaliados juntos, com revisão das próximas doses da indução.'),
            consequencia(
                chave="cfx_ajustada",
                titulo="Escolheu ciclofosfamida, com a conta feita",
                quando={"escolheu": ["b1", 1]}, dias=5, tfg=8,
                porque='Neste ramo, a menor contagem registrada foi de 1.900 neutrófilos/mm³. Os dias e a função renal atribuídos à simulação não demonstram que ciclofosfamida ajustada prolongue internação ou prejudique recuperação em comparação com rituximabe.'),
            consequencia(
                chave="cfx_plena",
                titulo="Escolheu ciclofosfamida sem a correção de dose",
                quando={"escolheu": ["b1", 2]}, dias=13, tfg=12,
                porque='A dose não ajustada aumenta o risco de toxicidade. Neste ramo, registraram-se 210 neutrófilos/mm³ e complicação infecciosa grave. Os valores dos outros ramos não são previsões contrafactuais nem garantias de segurança.'),
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
       'para a glomerulonefrite associada à infecção no adulto; Surviving Sepsis Campaign 2026 (antibiótico imediato pela suspeita clínica, sem depender da procalcitonina); CDC, '
       'tratamento da estrongiloidíase (ivermectina 200 µg/kg por dois dias).',
       'Imagens, de licença aberta, com setas adicionadas: radiografia, Samir, CC BY-SA 3.0; ultrassom renal, Hansen, Nielsen e Ewertsen, CC BY 4.0; sedimento, Rian Kabir, CC BY 2.0; tomografia dos seios, 511KeV, CC BY-SA 4.0; ecocardiograma, Kjetil Lenes, domínio público; tomografia de tórax, Hellerhoff, CC BY-SA 4.0; glomérulo, Nephron, CC BY-SA 3.0; imunofluorescência, Simon Caulton, CC BY-SA 3.0; corpúsculo renal, Michał Komorniczak, CC BY-SA 3.0, números originais retirados; pele das pernas, James Heilman, MD, CC BY-SA 3.0. Todas no Wikimedia Commons, com setas adicionadas; endereços completos em img/CREDITOS.md.'),
]


# ═══════════════ o que a revisão cobra, quando não há mais o que decidir ══════

REVISAO = []

# Fontes conferidas na revisão das questões (22/10/2026):
# https://kdigo.org/wp-content/uploads/2024/05/KDIGO-2024-ANCA-Vasculitis-Guideline-Update.pdf
# https://www.who.int/news/item/17-12-2020-a-parasitic-infection-that-can-turn-fatal-with-administration-of-corticosteroids

# Referência de construção dos itens (aplicação e opções plausíveis):
# https://www.nbme.org/sites/default/files/2021-02/NBME_Item%20Writing%20Guide_R_6.pdf

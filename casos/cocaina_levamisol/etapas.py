"""Caso ficcional para raciocínio clínico em residência de clínica médica.

Revisão editorial: integração de dados, seleção limitada de exames e
explicações após a resposta. Fontes clínicas ao final deste arquivo.
"""
from pathlib import Path

from motor.estudo_imagem import ecg, estudo
from motor.etapas import (alt, bifurcacao, caminho, capa, desfecho, op, p,
                          pagina, painel, par, pareamento, pergunta, pontos,
                          topicos, vitais)

TITULO = 'À flor da pele'
RODAPE = 'Paciente ficcional · evoluções simuladas para ensino'
COR = '#7c3aed'
IMG = Path(__file__).parent / 'img'
BANCO = []
MOLDE = 'nejm'
CENA = 'cena.png'


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


def fim(k, titulo, texto, porque, qualidade):
    return desfecho(k, titulo, p(texto), qualidade=qualidade, porque=porque,
                    fecho='retrospectiva')


ETAPAS = [
    capa(TITULO, fundo=CENA, kicker='Caso interativo',
         selo='Paciente ficcional · procedência e créditos na última tela'),

    pg('historia', 'Apresentação',
       'Marina, 34 anos, vendedora numa loja de roupas, chega ao pronto-socorro '
       'com a irmã por manchas dolorosas nas coxas há três dias e febre desde '
       'ontem, com calafrios. Começaram como duas áreas avermelhadas na face '
       'externa das coxas, que ela atribuiu ao atrito da calça; outras '
       'surgiram ao lado, escureceram, e hoje doem em repouso.',
       'Há dor nos punhos e tornozelos, sem inchaço. Tomou paracetamol. Não '
       'usou antibiótico nem pomada.',
       'Nega queda, picada, exercício intenso, falta de ar, tosse, dor '
       'abdominal, diarreia, ardor ao urinar, sangramento de gengiva e aumento '
       'do fluxo menstrual.'),

    pagina('ficha', 'Ficha do paciente', '',
           topicos(('Antecedentes', 'Apendicectomia aos 16 anos. Uma gestação a '
                    'termo. Rinite desde o ano passado, com crostas e sangramento '
                    'discreto pelo nariz. Há quatro meses teve manchas pequenas '
                    'nas pernas, que sumiram em duas semanas sem consulta.'),
                   ('Medicações', 'Dipirona 1 g quando tem cólica ou dor de '
                    'cabeça, a última há cinco dias. Soro fisiológico nasal. Sem '
                    'anticoncepcional hormonal, fórmulas para emagrecer ou chás.'),
                   ('Hábitos', 'Fuma cinco cigarros por dia. Bebe nos fins de '
                    'semana. Nega drogas ilícitas; a entrevista é feita com a '
                    'irmã no quarto.'),
                   ('Vida social', 'Mora com a filha de 9 anos. Sai com amigas '
                    'aos sábados. Sem viagem nos últimos meses, sem animais em '
                    'casa.'),
                   ('Família', 'Mãe com hipotireoidismo. Pai hipertenso. Sem '
                    'trombose, doença autoimune ou renal na família.')),
           so_kicker=True),

    pagina('exame', 'Exame físico', '',
           vitais(('Temperatura', '38,6 °C', True),
                  ('Pressão arterial', '108/68', False),
                  ('Frequência cardíaca', '112', True),
                  ('Frequência respiratória', '18', False),
                  ('SpO₂ em ar ambiente', '98%', False)),
           topicos(('Estado geral', 'Lúcida, orientada, com dor ao movimentar as '
                    'pernas.'),
                   ('Cabeça e pescoço', 'Orofaringe sem aftas nem placas. Mucosa '
                    'nasal com crostas, septo íntegro. Sem linfonodos palpáveis.'),
                   ('Coração e pulmões', 'Ritmo regular, sem sopro. Murmúrio '
                    'vesicular sem ruídos adventícios.'),
                   ('Abdome', 'Indolor. Fígado e baço não palpáveis.'),
                   ('Pele', 'Nas faces laterais das coxas, cinco placas violáceas '
                    'de 2 a 6 cm, dolorosas, que não clareiam à digitopressão, com '
                    'bordas anguladas e ramificadas; duas têm centro enegrecido. '
                    'Sem bolhas nem crepitação. Pulsos distais presentes.'),
                   ('Articulações', 'Dor à mobilização dos punhos, sem sinovite.')),
           so_kicker=True),

    estudo('pele', 'Fotografia de pele',
           'A equipe fotografa as placas para acompanhar a evolução. Esta '
           'fotografia é de outro paciente, com o mesmo tipo de lesão, de outra '
           'causa e em outra região do corpo; a régua está em centímetros.',
           IMG / 'pele_placa.jpg',
           'Fotografia de outro paciente, com lesão do mesmo tipo · régua em centímetros.',
           'Niels Olson · Wikimedia Commons · CC BY-SA 3.0 · setas adicionadas',
        [
         ((336, 71), (215, 175), '**Desenho em rede** na periferia: traços violáceos finos e ramificados, que seguem a malha de vasos da derme.', 12),
         ((684, 345), (560, 560), '**Centro enegrecido**: a pele que dependia do vaso ocluído necrosou.', -12),
         ((714, 441), (860, 560), '**Borda angulada**, que termina em ponta, sem o contorno arredondado da púrpura comum.', 12),
        ],
        ['Placa violácea de cerca de 4 cm, de borda angulada e '
         'ramificada, com centro enegrecido e traços em rede na periferia.',
         'É o desenho descrito nas coxas de Marina: placas violáceas de 2 a '
         '6 cm, dolorosas, que não clareiam, com bordas anguladas e '
         'ramificadas, duas com centro enegrecido.']),

    Q('q1', 1, 'Quais três hipóteses você precisa diferenciar inicialmente?', [
 ('Vasculite cutânea', True), ('Ectima gangrenoso', True), ('Síndrome antifosfolípide', True),
 ('Púrpura trombocitopênica imune', False), ('Eritema nodoso', False), ('Calcifilaxia urêmica', False)],
 [('Mecanismos concorrentes', 'O desenho ramificado com necrose sugere comprometimento vascular. Inflamação do vaso, invasão infecciosa e trombose imune precisam ser diferenciadas; a pele sozinha não define qual delas está presente.'),
 ('Por que as outras pesam menos', 'Trombocitopenia costuma produzir petéquias e sangramento, sem explicar bem a necrose em rede. Eritema nodoso é uma paniculite nodular, de outra morfologia. Calcifilaxia urêmica integra pior a ausência de doença renal conhecida; uma forma não urêmica não é impossível, mas não é a prioridade entre estas opções.')]),

    painel('res1', 'Primeiros exames', 'Sangue', [
        ex('Hemoglobina / hematócrito', '12,1 g/dL / 36%', 'Hb 12–16 g/dL'),
        ex('Volume corpuscular médio', '88 fL', '80–100 fL'),
        ex('Leucócitos', '900/mm³ · neutrófilos 20% · linfócitos 70% · monócitos 10%',
           '4.000–11.000/mm³', True),
        ex('Plaquetas', '238.000/mm³', '150.000–450.000/mm³'),
        ex('Esfregaço de sangue periférico', 'Sem blastos, sem esquizócitos'),
        ex('INR / TTPa', '1,0 / 29 s', 'INR até 1,2 · TTPa 25–35 s'),
        ex('Fibrinogênio', '410 mg/dL', '200–400 mg/dL', True),
        ex('Ureia / creatinina', '28 / 0,9 mg/dL', 'até 42 / 1,1 mg/dL'),
        ex('Proteína C reativa / lactato', '96 mg/L / 1,7 mmol/L', 'PCR < 5 · lactato até 2,0', True),
    ], introducao='Dois pares de hemoculturas foram colhidos antes de qualquer '
                  'antibiótico.'),

    painel('res1b', 'Primeiros exames', 'Urina e bioquímica', [
        ex('Urina', 'Densidade 1.020 · sangue negativo · proteína negativa · 0 a 2 hemácias por campo · sem cilindros'),
        ex('Sódio / potássio', '137 / 4,1 mmol/L', 'Na 135–145 · K 3,5–5,0'),
        ex('AST / ALT', '31 / 26 U/L', 'até 40 / 41 U/L'),
        ex('Bilirrubina total', '0,6 mg/dL', 'até 1,2 mg/dL'),
        ex('Beta-hCG sérico', 'Negativo'),
    ]),

    estudo('rx_adm', 'Radiografia de tórax',
           'Radiografia feita na chegada, à procura de um foco para a febre '
           'numa paciente com poucos neutrófilos.',
           IMG / 'rx_torax_normal.jpg',
           'Radiografia de outro adulto · comparação didática.',
           'Mikael Häggström · Wikimedia Commons · CC0 · setas adicionadas',
        [
         ((250, 560), (90, 440), '**Pulmão direito** transparente, sem consolidação.', 12),
         ((110, 975), (250, 1080), '**Seio costofrênico** direito livre: sem derrame.', -12),
         ((745, 800), (900, 700), '**Contorno cardíaco** esquerdo nítido, de tamanho normal.', 12),
        ],
        ['Sem opacidade focal, sem derrame, área cardíaca normal.',
         'No neutropênico a radiografia pode vir limpa mesmo com pneumonia, '
         'porque falta a célula que forma o infiltrado. Sem tosse e com '
         'saturação normal, o pulmão não é o foco provável.']),

    *ecg('ecg_evolucao',
         'Uma hora depois do antitérmico, a frequência cardíaca continua acima '
         'de 110 e a equipe registra um eletrocardiograma. Qual é o ritmo?', IMG,
         'Febre e dor explicam o ritmo; o traçado não aponta outra causa para a '
         'taquicardia.'),

    Q('q2', 2, 'Quais três estudos da pele você solicita sem atrasar o antibiótico?', [
 ('Histologia de biópsia profunda', True), ('Cultura bacteriana do tecido', True), ('Pesquisa de fungos no tecido', True),
 ('Mielograma', False), ('Angiografia dos membros inferiores', False), ('Novo fibrinogênio', False)],
 [('Amostra da lesão', 'A histologia compara trombose, inflamação e possível invasão vascular. Cultura bacteriana e pesquisa micológica, com colorações e cultura conforme o laboratório, procuram uma infecção que mudaria o tratamento. Planejar fragmentos adequados antes de colocar todo o material em formol.'),
 ('Prioridade clínica', 'Febre com 180 neutrófilos/mm³ exige antibiótico empírico imediato, em paralelo à coleta. Angiografia tem menor rendimento com pulsos preservados e lesões de pequenos vasos; mielograma pode ser necessário se a neutropenia não se resolver ou surgirem outras alterações. Repetir fibrinogênio não substitui investigar a lesão.')]),

    pagina('coag', 'Discussão', 'O que a coagulação diz',
      p('Diante de púrpura que oclui vasos, a equipe relê o sangue da chegada '
        'à procura de consumo. Plaquetas de 238.000/mm³, INR de 1,0, TTPa de '
        '29 s e fibrinogênio de 410 mg/dL: não há gasto de plaquetas nem de '
        'fatores, e esses resultados não sustentam coagulação intravascular '
        'disseminada.'),
      p('O esfregaço sem esquizócitos, com plaquetas normais, reduz a probabilidade de '
        'hemólise mecânica das microangiopatias trombóticas. O fibrinogênio '
        'pouco acima do limite acompanha a PCR de 96 mg/L: é inflamação, não '
        'consumo.'),
      p('Sobram as oclusões que não gastam fatores: microrganismo que invade '
        'a parede, anticorpo que trombosa, crioproteína que precipita e '
        'inflamação da própria parede. No neutropênico febril, a primeira a '
        'excluir é a infecção que invade o vaso, e isso pede tecido: biópsia '
        'profunda da borda de uma placa, com colorações e cultura para '
        'bactérias e fungos, sem atrasar o antibiótico.')),

    bifurcacao('b1', 'Decisão', 'As primeiras horas',
      'Febril, com 180 neutrófilos e placas necróticas nas coxas. As '
      'hemoculturas já foram colhidas. Como você conduz?', [
      caminho('Iniciar cefepima endovenosa',
              'protecao',
              'Neutropenia febril pede betalactâmico antipseudomonas na primeira '
              'hora; infecção de pele e partes moles é critério para somar '
              'vancomicina.', rotulo_curto='Tratar agora'),
      caminho('Aguardar a cultura do tecido',
              'espera',
              'Cultura de tecido leva dias; aguardar o resultado deixa uma '
              'possível infecção grave sem tratamento.', rotulo_curto='Esperar'),
      caminho('Iniciar filgrastim como única intervenção', 'gcsf',
              'O fator estimulador pode encurtar a agranulocitose, mas não '
              'trata a infecção que já pode estar presente.',
              rotulo_curto='Só filgrastim'),
    ]),

    pg('espera', 'Doze horas depois',
       'Ainda sem antibiótico, Marina tem novo calafrio. A pressão cai para '
       '86/50 mmHg e o lactato sobe para 3,4 mmol/L. A plantonista faz '
       'cristaloide e inicia cefepima e vancomicina com doze horas de atraso.',
       segue='internacao'),

    pg('gcsf', 'Oito horas depois',
       'Depois do filgrastim, a febre chega a 39,5 °C e a pressão cai para '
       '88/52 mmHg. A equipe da noite inicia cefepima e vancomicina com oito '
       'horas de atraso, com expansão volêmica.',
       segue='internacao'),

    pg('protecao', 'Primeira hora',
       'Cefepima 2 g endovenosa de 8 em 8 horas começa 40 minutos depois da '
       'triagem, com vancomicina por peso e nível sérico. A dipirona é '
       'suspensa e anotada no prontuário como suspeita de reação.',
       'A dermatologia retira um fragmento profundo da borda de uma placa para '
       'histologia e cultura de bactérias e fungos.'),

    pg('internacao', 'Na enfermaria',
       'Marina é internada em quarto individual, com hemograma diário. A '
       'hipótese registrada é agranulocitose por dipirona com lesões necróticas '
       'de provável causa infecciosa.',
       'Confere-se a coleta de tecido da borda da lesão para histologia e '
       'microbiologia; nos caminhos em que ainda não foi feita, a dermatologia '
       'obtém a amostra durante a estabilização, sem atrasar o antibiótico.'),

    pg('dia3', 'Terceiro dia',
       'A febre cedeu no segundo dia. Os neutrófilos estão em 240/mm³ e as '
       'hemoculturas seguem sem crescimento em 48 horas. A biópsia mostra '
       'trombos de fibrina nos pequenos vasos da derme, necrose da epiderme e '
       'leucocitoclasia focal; as colorações para bactérias e fungos não '
       'mostram microrganismos, e a cultura do tecido não cresceu.',
       'No reexame da manhã há uma placa purpúrica nova, pequena e dolorosa, '
       'na hélice da orelha esquerda. Marina conta que a urina ficou cor de '
       'chá desde a noite anterior.'),

    painel('res2', 'Terceiro dia', 'Rim e urina', [
        ex('Ureia / creatinina', '52 / 1,6 mg/dL {{(0,9 na admissão)}}', 'até 42 / 1,1 mg/dL', True),
        ex('Urina', 'Sangue +++ · proteína ++', '—', True),
        ex('Sedimento urinário', '50 hemácias por campo, 60% dismórficas, com acantócitos · cilindros hemáticos', '—', True),
        ex('Leucócitos na urina', '4 por campo · sem cilindros leucocitários', 'até 5 por campo'),
        ex('Proteína / creatinina urinária', '1,1 g/g', '< 0,2 g/g', True),
        ex('Fração de excreção de sódio', '0,8%'),
        ex('Vancomicina, nível de vale', '12 mg/L', '10–20 mg/L'),
        ex('Creatinoquinase', '96 U/L', 'até 170 U/L'),
        ex('Neutrófilos absolutos', '240/mm³', '1.500–7.500/mm³', True),
    ]),

    estudo('us_evolucao', 'Ultrassonografia renal',
        'Com a creatinina em alta e a urina escura, a equipe pede '
        'ultrassonografia dos rins para afastar obstrução e medir o tamanho '
        'deles.',
        IMG / 'us_rim.jpg',
        'Rim de outro adulto. Asteriscos da fonte: um, coluna de Bertin; '
        'dois, pirâmide; três, córtex; quatro, seio renal. Os cálipers também '
        'são da fonte.',
        'Hansen, Nielsen e Ewertsen · Wikimedia Commons · CC BY 4.0 · setas adicionadas',
        [
         ((495, 288), (620, 105), '**Córtex** renal (três asteriscos), de espessura preservada.', 12),
         ((447, 400), (720, 550), '**Seio renal** (quatro asteriscos), ecogênico, sem dilatação do sistema coletor.', -12),
         ((472, 357), (330, 160), '**Pirâmide medular** (dois asteriscos), hipoecoica: a diferenciação entre córtex e medula está preservada.', 12),
        ],
        ['Rins de 11 cm, com córtex preservado e sem hidronefrose.',
         'Sem obstrução e sem rim pequeno de doença antiga: a lesão é aguda e '
         'está dentro do rim.']),

    Q('q4', 3, 'Quais quatro exames mais ajudam a distinguir os mecanismos possíveis?', [
 ('Anti-MPO', True), ('Anti-PR3', True), ('Anticorpo anti-membrana basal glomerular', True), ('Complemento C3', True),
 ('Novo nível sérico de vancomicina', False), ('Nova creatinoquinase', False), ('Novo ultrassom renal', False)],
 [('Mecanismos', 'MPO e PR3 avaliam duas especificidades do ANCA; positividade não estabelece sozinha uma vasculite primária. Anti-MBG pesquisa um mecanismo de glomerulonefrite com consequências terapêuticas importantes. C3 ajuda a avaliar a hipótese de imunocomplexos; a equipe complementa com C4 e crioglobulinas.'),
 ('Toxicidade e obstrução', 'A vigilância da vancomicina permanece necessária, mas o nível sérico não explica sozinho acantócitos e cilindros hemáticos. A CK inicial normal e hemácias verdadeiras tornam pigmentúria menos provável. Sem nova pista de obstrução, repetir o ultrassom acrescenta menos que esclarecer o mecanismo glomerular.')]),

    bifurcacao('b_investigacao_renal', 'Decisão', 'Nova alteração urinária',
 'A pele começa a doer menos, mas a creatinina continua subindo. Qual exame você prioriza?', [
 caminho('Biópsia renal', 'renal_precoce', 'A evolução e o sedimento sugerem lesão glomerular. A amostra pode distinguir mecanismos e medir atividade antes de atribuir a piora apenas aos medicamentos.'),
 caminho('Novo nível sérico de vancomicina', 'renal_vigilancia', 'É útil para segurança e ajuste, mas não responde à localização glomerular sugerida pelo sedimento. O resultado deve ser confrontado com a evolução, sem encerrar a investigação.')]),

    pg('renal_precoce', 'Avaliação da nefrologia',
 'Marina passa a urinar menos e nota a primeira urina do dia avermelhada. A febre não voltou e a dor das placas diminuiu. Não há edema importante nem dispneia. Creatinina de controle: 2,1 mg/dL.',
 'Com plaquetas e coagulação preservadas, a equipe programa a biópsia renal e mantém vigilância infecciosa. O contraste entre melhora da pele e piora do rim impede tratar os dois órgãos como se estivessem em remissão.', segue='res3'),

    pg('renal_vigilancia', 'Reavaliação no dia seguinte',
 'O novo nível de vancomicina é de 13 mg/L. A indicação e a dose são revistas; a cobertura empírica é ajustada à microbiologia e à função renal. Esse valor não exclui toxicidade, mas também não explica o sedimento.',
 'Marina continua afebril e as placas estão menos dolorosas. A urina permanece avermelhada, a creatinina chega a 2,1 mg/dL e os cilindros hemáticos persistem. A equipe solicita a biópsia renal, sem presumir que a melhora cutânea significa melhora renal.', segue='res3'),

    painel('res3', 'Terceiro dia', 'Anticorpos e complemento', [
        ex('ANCA por imunofluorescência', 'Padrão perinuclear (p-ANCA), título 1:1.280', 'Não reagente', True),
        ex('Anti-MPO', '128 U/mL', '< 20 U/mL', True),
        ex('Anti-PR3', '46 U/mL', '< 20 U/mL', True),
        ex('Anti-membrana basal glomerular', 'Não reagente', 'Não reagente'),
        ex('C3 / C4', '104 / 22 mg/dL', 'C3 90–180 · C4 10–40'),
        ex('Crioglobulinas (colheita a 37 °C)', 'Não detectadas', 'Não detectadas'),
        ex('Anticardiolipina e anti-β2-glicoproteína I', 'Não reagentes', 'Não reagentes'),
        ex('Anticoagulante lúpico', 'Não detectado', 'Não detectado'),
        ex('HIV, HBsAg e anti-HCV', 'Não reagentes', 'Não reagentes'),
    ]),

    Q('q5', 4,
      'MPO e PR3 positivos, agranulocitose, lesão auricular e sedimento nefrítico. Qual hipótese ganha mais peso para integrar o quadro?', [
      ('Doença vascular associada a exposição medicamentosa ou recreativa', True),
      ('Vasculite primária associada ao ANCA', False),
      ('Endocardite infecciosa', False),
      ('Síndrome antifosfolípide', False),
      ('Vasculite crioglobulinêmica', False),
     ], [
      ('A combinação', 'Dupla especificidade ANCA, neutropenia profunda e púrpura auricular favorecem exposição como mecanismo comum. Nenhum desses achados isoladamente comprova a substância; é necessário rever medicamentos e uso recreativo a sós.'),
      ('Concorrentes', 'Vasculite primária pode ter perfis atípicos, mas MPO não basta para classificá-la. Endocardite pode positivar ANCA; culturas pré-antibiótico negativas e ausência de outros sinais reduzem, sem zerar, essa possibilidade. Antifosfolípides negativos e sedimento glomerular inflamatório pesam contra SAF. Crioglobulinas não detectadas e C4 normal diminuem a probabilidade de crioglobulinemia.'),
     ]),

    pg('entrevista', 'Entrevista a sós',
       'A médica volta ao quarto no fim da tarde, quando a irmã saiu. Explica '
       'que o que for dito fica no prontuário e na equipe, e que a pergunta '
       'muda o tratamento.',
       'Marina conta que usa cocaína aspirada aos sábados há cerca de oito '
       'meses, a última vez dois dias antes de vir ao hospital, e que as '
       'manchas de quatro meses atrás vieram depois de um fim de semana de uso '
       'maior. Não sabe o que há no pó. Nunca injetou. A rinite com crostas '
       'começou na mesma época.'),

    Q('q6', 5,
      'A coleta toxicológica ocorrerá cinco dias após o último uso referido. Quais duas conclusões poderão ser sustentadas pelos testes?', [
      ('Benzoilecgonina confirmada documenta exposição à cocaína', True),
      ('Levamisol não detectado terá pouco poder para excluir a exposição', True),
      ('Benzoilecgonina confirmada identifica a composição do adulterante', False),
      ('A intensidade do ANCA permite datar a última exposição', False),
      ('A histologia cutânea distingue quimicamente cocaína de levamisol', False),
     ], [
      ('Janela e inferência', 'Benzoilecgonina é metabólito da cocaína, não do adulterante. Levamisol é eliminado rapidamente; coleta tardia tem baixa sensibilidade e resultado negativo não deve ser tratado como refutação.'),
      ('O limite dos marcadores', 'ANCA pode persistir além da exposição e não serve como relógio. Histologia mostra trombose e inflamação, não a molécula causal. Assim, toxicologia de cocaína, padrão clínico e cronologia sustentam associação provável, sem comprovação química do levamisol.'),
     ]),

    painel('res4', 'Quarto ao sexto dia', 'Toxicologia e biópsia renal', [
        ex('Benzoilecgonina urinária, confirmada por cromatografia', 'Detectada', 'Não detectada', True),
        ex('Levamisol urinário (LC-MS/MS)', 'Não detectado', 'Não detectado'),
        ex('Biópsia renal, microscopia', 'Glomerulonefrite necrosante com crescentes celulares em 5 de 18 glomérulos · fibrose intersticial mínima', '—', True),
        ex('Biópsia renal, imunofluorescência', 'Pauci-imune', '—', True),
        ex('Creatinina', '2,6 mg/dL', '0,6–1,1 mg/dL', True),
        ex('Neutrófilos absolutos', '1.100/mm³', '1.500–7.500/mm³', True),
    ], introducao='A biópsia renal foi feita após a reavaliação nefrológica, com plaquetas e '
                  'coagulação normais.'),

    Q('q7', 6,
      'Após toxicologia e biópsia renal, quais duas interpretações melhor ponderam causa e atividade da doença?', [
      ('A biópsia demonstra doença glomerular ativa apesar da melhora dos neutrófilos', True),
      ('A toxicologia confirma cocaína, mantendo levamisol como associação provável', True),
      ('A creatinina em alta reflete sobretudo recuperação renal tardia após a fase infecciosa', False),
      ('Vasculite ANCA primária com agranulocitose por dipirona é a explicação mais provável do conjunto', False),
      ('O componente trombótico da pele favorece microangiopatia trombótica como causa da perda renal', False),
     ], [
      ('Atividade e atribuição', 'Neutrófilos subiram a 1.100, mas creatinina chegou a 2,6 e há necrose com crescentes celulares em 5/18 glomérulos: predomina uma lesão glomerular ativa, não apenas recuperação lenta de injúria anterior. Benzoilecgonina confirma cocaína; coleta tardia negativa para levamisol deixa a associação provável.'),
      ('Explicações concorrentes', 'Vasculite primária e agranulocitose por dipirona podem coexistir, mas exigem causas separadas para uma combinação ligada à exposição recorrente, com púrpura auricular e ANCA duplo. Trombos cutâneos não demonstram microangiopatia renal: plaquetas preservadas, ausência de esquizócitos e biópsia necrosante pauci-imune favorecem outro mecanismo.'),
     ]),

    pg('diagnostico', 'Discussão clínica',
 'A integração da exposição recorrente, da agranulocitose, da púrpura retiforme com lesão auricular e da glomerulonefrite pauci-imune sustenta doença vascular associada à cocaína, com provável participação do levamisol. A toxicologia comprova cocaína; a coleta tardia negativa para levamisol não confirma nem exclui o adulterante.',
 'A melhora dos neutrófilos e da pele após a interrupção da exposição não resolveu a inflamação glomerular. Esse comportamento diferente entre órgãos é o motivo para discutir tratamento renal específico, e não apenas prolongar observação.',
 'A dipirona permanece suspensa e registrada como possível contribuinte da agranulocitose. Nenhum exame isolado permite atribuir com certeza toda a neutropenia a uma única substância.'),

    pagina('sobre_biopsia', 'Discussão', 'Sobre a biópsia renal',
      p('Crescente é a proliferação de células no espaço de Bowman, em torno '
        'de um tufo glomerular cuja parede se rompeu. Celular, é lesão recente '
        'e ainda pode regredir; fibrosa, é cicatriz. Em Marina, 5 de 18 '
        'glomérulos têm crescentes celulares, com fibrose intersticial mínima.'),
      p('Pauci-imune quer dizer imunofluorescência com pouco ou nenhum '
        'depósito de imunoglobulina ou complemento. É o padrão das vasculites '
        'ANCA e combina com o C3 e o C4 normais; a lesão por imunocomplexo ou '
        'por anticorpo antimembrana basal teria outro desenho.'),
      p('A creatinina foi de 0,9 na admissão a 1,6 no terceiro dia e a 2,6 '
        'agora. O ritmo da piora e a proporção de crescentes ativos são o que '
        'pesa na decisão sobre o rim.')),

    bifurcacao('b2', 'Decisão', 'O rim',
      'Glomerulonefrite crescêntica pauci-imune, creatinina de 2,6 mg/dL, '
      'neutrófilos em 1.100 e subindo, culturas negativas, sem cocaína há '
      'sete dias. O que você propõe?', [
      caminho('Iniciar rituximabe para a doença renal ativa',
              'renal',
              'Crescentes celulares são lesão ativa e reversível; tratar agora '
              'preserva néfrons, com a infecção coberta enquanto os neutrófilos '
              'sobem.', rotulo_curto='Tratar o rim'),
      caminho('Manter suporte sem imunossupressor', 'suporte',
              'A pele e a medula respondem à abstinência; o glomérulo com '
              'crescente ativo nem sempre.', rotulo_curto='Esperar'),
      caminho('Iniciar ciclofosfamida em dose plena',
              'infeccao',
              'Ciclofosfamida é mielotóxica e ela ainda está neutropênica; '
              'a dose e o momento exigem discussão especializada. A cobertura '
              'antimicrobiana é revista conforme a recuperação, as culturas e '
              'a evolução.', rotulo_curto='Ciclofosfamida plena'),
    ]),

    pg('renal', 'Tratamento dirigido',
       'Metilprednisolona 500 mg por dia por três dias, depois prednisona em '
       'esquema de redução, e rituximabe. A cefepima segue até os neutrófilos '
       'passarem de 500 e a febre ficar para trás; entra profilaxia para '
       '//Pneumocystis//.',
       'A equipe oferece acompanhamento para o uso de cocaína sem condicionar '
       'o cuidado à abstinência, e Marina autoriza a irmã a participar do '
       'plano.'),

    pagina('tratamento', 'Discussão', 'O que entra no tratamento',
      p('A exposição vem primeiro. Sem novo uso, a pele e a medula se '
        'recuperam na maioria dos casos publicados, sem imunossupressor, e '
        'uma nova exposição pode provocar recorrência; persistência ou piora também exige investigar outras causas.'),
      p('O rim não segue a pele. As séries de glomerulonefrite associada ao '
        'levamisol trataram os crescentes ativos com corticoide e rituximabe ou '
        'ciclofosfamida, como a KDIGO 2024 indica na vasculite ANCA. Numa '
        'mulher de 34 anos que acaba de sair da agranulocitose, o rituximabe '
        'poupa a fertilidade e a medula; a ciclofosfamida, quando usada, é '
        'ajustada pela contagem de leucócitos.'),
      topicos(('Troca plasmática', 'A KDIGO 2024 sugere considerar em situações como creatinina '
               'acima de 3,4 mg/dL, diálise, queda rápida da função ou '
               'hemorragia alveolar com hipoxemia.'),
              ('Anticoagulação', 'Sem antifosfolípide, trombo de pequeno vaso '
               'da pele não a indica, e a biópsia renal é recente.'),
              ('Seguimento', 'O ANCA persiste meses depois da remissão e não '
               'guia a duração. Quem guia é a creatinina, o sedimento e a '
               'proteinúria, com vigilância de infecção durante a '
               'imunossupressão.'))),

    pg('seguimento', 'Após o controle da inflamação renal',
       'Não surgem placas novas. As áreas necróticas das coxas delimitam e '
       'recebem curativo; a da orelha cicatriza. Os neutrófilos passam de '
       '2.000 no controle atual, e a creatinina começa a cair. O tempo de '
       'recuperação depende do percurso: o início tardio do tratamento renal '
       'prolongou a internação neste caso.',
       conforme=('b2', ['alta_cedo', 'f2', 'f2'])),

    pg('alta_cedo', 'Última visita',
       'A creatinina está em 1,4 mg/dL e o sedimento tem menos hemácias. Ela '
       'aprendeu a trocar os curativos e tem consultas marcadas com '
       'nefrologia, dermatologia e o serviço de álcool e drogas.',
       conforme=('b1', ['f1', 'f2', 'f2'])),

    pg('suporte', 'Cinco dias depois',
       'A pele melhora e os neutrófilos passam de 1.500, mas a creatinina sobe '
       'para 3,8 mg/dL e a diurese cai. O sedimento segue com cilindros '
       'hemáticos.', segue='b3'),

    bifurcacao('b3', 'Decisão', 'O rim não seguiu a pele',
      'Creatinina de 3,8 mg/dL e subindo, sem cocaína há doze dias. E agora?', [
      caminho('Iniciar rituximabe', 'tardio',
              'A equipe associa glicocorticoide ao tratamento da lesão renal '
              'ativa. O atraso aumenta o risco de recuperação incompleta, sem '
              'permitir prever individualmente quantos néfrons foram perdidos.',
              rotulo_curto='Tratar agora'),
      caminho('Manter a espera por mais uma semana', 'dialise',
              'Esperar a regressão espontânea com a função caindo transforma '
              'crescente celular em fibrose.', rotulo_curto='Esperar mais'),
    ]),

    pg('tardio', 'Tratamento tardio',
       'Metilprednisolona por três dias e rituximabe. A creatinina para de '
       'subir no quinto dia de tratamento, em 4,1 mg/dL, sem necessidade de '
       'diálise.', segue='tratamento'),

    pg('dialise', 'Uma semana depois',
       'A creatinina chega a 6,2 mg/dL, com potássio de 6,1 mmol/L e '
       'sobrecarga de volume. Ela começa hemodiálise. A nova biópsia mostra '
       'crescentes fibrosos na maior parte dos glomérulos.', segue='f_dialise'),

    pg('infeccao', 'Dez dias depois',
       'Os neutrófilos, que estavam em 1.100, caem para 300 depois da '
       'ciclofosfamida. Nesta trajetória simulada, Marina tem febre de 39,4 °C, pressão de 80/46 mmHg e '
       'hemocultura com bacilo gram-negativo. Vai para a terapia intensiva.',
       segue='f_infeccao'),

    fim('f1', 'Alta no 16.º dia',
        'Marina sai com creatinina de 1,4 mg/dL, neutrófilos normais e as '
        'feridas das coxas cicatrizando. Três meses depois, sem uso, não há '
        'lesões novas e a creatinina está em 1,1 mg/dL; o ANCA segue '
        'positivo, em título menor.',
        'Antibiótico na primeira hora, a história de exposição refeita a sós e '
        'o tratamento da glomerulonefrite enquanto os crescentes eram celulares '
        'foram as decisões que preservaram o rim.', 'melhor'),

    fim('f2', 'Alta depois de internação prolongada',
        'Marina sai no 27.º dia, com creatinina de 2,2 mg/dL e cicatrizes '
        'retráteis nas coxas. Segue com nefrologia, com filtração glomerular '
        'reduzida.',
        'O atraso do antibiótico ou do tratamento do rim acrescentou dias de '
        'internação e néfrons perdidos, numa doença que responde bem quando '
        'tratada cedo.', 'medio'),

    fim('f_dialise', 'Alta em hemodiálise',
        'Marina sai no 30.º dia em hemodiálise três vezes por semana. Três '
        'meses depois, a função renal não voltou.',
        'A pele e a medula melhoraram com a abstinência, e isso tranquilizou a '
        'equipe. O glomérulo seguiu inflamado, e em duas semanas os crescentes '
        'celulares viraram fibrosos.', 'pior'),

    fim('f_infeccao', 'Choque séptico na terapia intensiva',
        'Com meropeném, vasopressor e retirada da ciclofosfamida, ela sai do '
        'choque em cinco dias e deixa a UTI no décimo. A glomerulonefrite '
        'segue ativa, e o tratamento do rim recomeça do zero.',
        'Neste percurso simulado, a exposição mielotóxica foi seguida de nova '
        'neutropenia e infecção grave. Não se presume suspensão do antibiótico '
        'nem se apresenta a bacteremia como consequência inevitável da '
        'ciclofosfamida; a dose e o momento exigiam individualização.', 'pior'),

    pagina('retrospectiva', 'Pontos de ensino', '',
        pontos(
            'Púrpura dolorosa, angulada e ramificada, com centro necrótico, é '
            'púrpura retiforme: oclusão de vaso da derme até prova em '
            'contrário.',
            'Neutrófilos absolutos se calculam. Febre com menos de 500 é '
            'neutropenia febril e pede betalactâmico antipseudomonas na '
            'primeira hora; lesão de pele e partes moles justifica somar '
            'vancomicina.',
            'Coagulação e plaquetas normais afastam púrpura fulminante e '
            'microangiopatia; no neutropênico, a infecção angioinvasiva é a '
            'primeira a excluir, com biópsia e cultura do tecido.',
            'Hemácias dismórficas e cilindros hemáticos localizam a lesão no '
            'glomérulo, e o dano renal pode não seguir o curso da pele.',
            'ANCA contra MPO e PR3 ao mesmo tempo sugere vasculite induzida. A '
            'história de exposição precisa ser refeita a sós.',
            'O levamisol sai da urina em cerca de 48 horas: o negativo tardio '
            'não exclui. Abstinência trata a pele e a medula; crescentes '
            'ativos pedem imunossupressão com a infecção vigiada.'),
        so_kicker=True),

    pg('referencias', 'Fontes e limites',
       'Paciente, valores e percursos são ficcionais. A cena de abertura é uma '
       'ilustração autoral gerada por inteligência artificial para este caso; '
       'não é fotografia nem documentação clínica.',
       'Levamisol: '
       '<a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC2780984/" '
       'target="_blank" rel="noopener">Knowles e cols., 2009</a>; '
       '<a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC3255368/" '
       'target="_blank" rel="noopener">McGrath e cols., 2011</a> (dupla '
       'positividade MPO/PR3); '
       '<a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC4602417/" '
       'target="_blank" rel="noopener">Carlson e cols., 2014</a> '
       '(glomerulonefrite); '
       '<a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC5821816/" '
       'target="_blank" rel="noopener">revisão de vasculite induzida por '
       'levamisol</a> (meia-vida e janela urinária). Adulterantes no Brasil: '
       '<a href="https://pubmed.ncbi.nlm.nih.gov/25544694/" target="_blank" '
       'rel="noopener">Polícia Federal, Forensic Sci Int 2015</a> e estudo de '
       'fluido oral em festas, Drug Alcohol Depend 2021.',
       'Neutropenia febril: IDSA 2010 (Freifeld e cols.) e ASCO/IDSA 2018 '
       '(Taplitz e cols.). Vasculite ANCA: KDIGO 2024 e PEXIVAS (Walsh e '
       'cols., 2020). O manejo antimicrobiano é extrapolado da neutropenia '
       'febril oncológica; não há ensaio que compare imunossupressores nesta '
       'síndrome.',
       'Imagens de outros pacientes, com setas adicionadas: fotografia de '
       'pele, placa por calcifilaxia no abdome, Niels Olson, '
       '<a href="https://commons.wikimedia.org/wiki/File:Calciphylaxis.png" '
       'target="_blank" rel="noopener">Wikimedia Commons</a>, CC BY-SA 3.0; '
       'radiografia de tórax, Mikael '
       'Häggström, Wikimedia Commons, CC0; eletrocardiograma, Ewingdo, '
       'Wikimedia Commons, CC BY-SA 4.0; ultrassonografia renal, Hansen, '
       'Nielsen e Ewertsen, Wikimedia Commons, CC BY 4.0.'),
]

REVISAO = []

# Fontes conferidas na revisão das questões (22/10/2026):
# https://pubmed.ncbi.nlm.nih.gov/21980179/
# https://pubmed.ncbi.nlm.nih.gov/22152487/
# https://kdigo.org/wp-content/uploads/2024/05/KDIGO-2024-ANCA-Vasculitis-Guideline-Update.pdf

# https://www.idsociety.org/practice-guideline/skin-and-soft-tissue-infections/
# https://www.health.ny.gov/diseases/aids/consumers/prevention/opioidprevention/health_advisory_levamisole-contaminated_cocaine.htm

# Referência de construção dos itens (aplicação e opções plausíveis):
# https://www.nbme.org/sites/default/files/2021-02/NBME_Item%20Writing%20Guide_R_6.pdf

next(e for e in ETAPAS if e['k']=='referencias')['corpo'] += p('Revisão da evolução: melhora cutânea e hematológica não garante remissão renal. Conduta em doença glomerular ativa individualizada, com extrapolação das diretrizes de vasculite: <a href="https://kdigo.org/wp-content/uploads/2024/05/KDIGO-2024-ANCA-Vasculitis-Guideline-Update.pdf">KDIGO 2024</a>. Para a emergência infecciosa, <a href="https://www.idsociety.org/globalassets/idsa/practice-guidelines/outpatient-management-of-fever-and-neutropenia.pdf">ASCO/IDSA — antibiótico empírico precoce na neutropenia febril</a>; diretriz oncológica usada como referência de segurança, não prova específica de tratamento da agranulocitose por adulterantes.')

for _n,_e in enumerate((e for e in ETAPAS if e['t']=='pergunta'),1): _e['kicker']=f'Pergunta {_n}'

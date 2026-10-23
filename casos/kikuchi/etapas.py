"""Abordagem sindrômica da linfonodomegalia, revisada em 21/10/2026.

Apresentação regional, hipóteses amplas, investigação dirigida, reavaliação
e tecido antes de nomear a doença rara. Paciente e trajetórias ficcionais.
Layout e motor de apresentação preservados.
"""
from pathlib import Path

from motor.estudo_imagem import estudo
from motor.etapas import (alt, bifurcacao, caminho, capa, desfecho, op, p,
                          pagina, painel, par, pareamento, pergunta, pontos,
                          topicos, vitais, tabela)

TITULO = 'O que ficou no pescoço'
RODAPE = 'Paciente ficcional · evoluções simuladas para ensino'
COR = '#ea580c'
IMG = Path(__file__).parent / 'img'
BANCO = []
MOLDE = 'nejm'
CENA = 'cena.png'


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


def fim(k, titulo, texto, porque, qualidade, fecho='retrospectiva'):
    return desfecho(k, titulo, p(texto), qualidade=qualidade, porque=porque,
                    fecho=fecho)


ETAPAS = [
    capa(TITULO, fundo=CENA, kicker='Caso interativo',
         selo='Paciente ficcional · procedência e créditos na última tela'),

    pg('historia', 'Apresentação',
       'Bianca, 27 anos, professora do ensino fundamental, procura o '
       'ambulatório por febre no fim da tarde há 12 dias e um caroço doloroso '
       'no lado esquerdo do pescoço. Tudo começou com dor de garganta, que '
       'passou; o caroço ficou.',
       'No quarto dia foi a uma unidade de pronto atendimento e saiu com '
       'amoxicilina por sete dias, já concluída, sem efeito sobre a febre. '
       'Nas últimas três noites acordou com a camiseta molhada de suor e '
       'perdeu 2 kg no mês, por falta de apetite.',
       'Nega tosse, falta de ar, dor de dente, lesões na pele, dor nas '
       'articulações, feridas na boca, disúria e diarreia.'),

    pagina('ficha', 'Ficha do paciente', '',
           topicos(('Antecedentes', 'Nenhuma doença crônica, nenhuma internação. '
                    'BCG na infância. Último teste de HIV há três anos, não '
                    'reagente.'),
                   ('Medicações', 'Anticoncepcional oral combinado há quatro anos. '
                    'Paracetamol 750 mg quando tem febre. Amoxicilina 500 mg de '
                    '8 em 8 horas, sete dias, terminada há dois dias.'),
                   ('Hábitos', 'Não fuma. Bebe vinho em encontros, raramente. '
                    'Nega drogas. Corre duas vezes por semana, parou há dez dias.'),
                   ('Vida social', 'Mora em São Paulo com o companheiro, parceiro '
                    'único há cinco anos, e um gato adulto; não lembra de '
                    'arranhadura. Não viajou nos últimos seis meses. Duas '
                    'crianças da turma dela faltaram com febre no mês passado.'),
                   ('Família', 'Mãe com hipotireoidismo. Pai hipertenso. Sem câncer, tuberculose ou doença '
                    'reumatológica conhecida na família.')),
           so_kicker=True),

    pagina('exame', 'Exame físico', '',
           vitais(('Temperatura', '38,1 °C', True),
                  ('Pressão arterial', '112/70', False),
                  ('Frequência cardíaca', '98', False),
                  ('Frequência respiratória', '16', False),
                  ('SpO₂ em ar ambiente', '98%', False),
                  ('Peso', '58 kg', False)),
           topicos(('Estado geral', 'Alerta, hidratada, corada, sem desconforto '
                    'respiratório.'),
                   ('Cabeça e pescoço', 'Orofaringe sem exsudato, dentes sem cárie '
                    'visível, couro cabeludo sem lesões. Três linfonodos na cadeia '
                    'cervical posterior esquerda, móveis, elásticos e dolorosos, o '
                    'maior com cerca de 3 cm à palpação, sem rubor e sem flutuação. Tireoide e '
                    'parótidas normais. Fossas supraclaviculares livres.'),
                   ('Outras cadeias', 'Sem linfonodos axilares, epitrocleares ou '
                    'inguinais palpáveis.'),
                   ('Tórax e abdome', 'Ausculta cardíaca e pulmonar normais. Fígado '
                    'no rebordo, baço não palpável.'),
                   ('Pele e articulações', 'Sem exantema, sem úlceras orais, sem '
                    'sinovite.')),
           so_kicker=True),

    Q('p1', 1, 'Quais três conjuntos de exames você solicita nesta consulta?',
[('Hemograma com esfregaço e LDH', True),
 ('Tomografias de pescoço, tórax e abdome', False),
 ('Ultrassonografia cervical e radiografia de tórax', True),
 ('FAN, anti-DNA e dosagem de complemento', False),
 ('Proteína C reativa, transaminases e creatinina', True),
 ('Hemoculturas e ecocardiograma transtorácico', False)],
[('Hemograma, esfregaço e LDH',
  'Selecionados. Procuram citopenias e alterações celulares. LDH elevada pode acompanhar infecção, '
  'inflamação ou linfoma; não distingue essas causas sozinha.'),
 ('Tomografias de pescoço, tórax e abdome',
  'Podem ser necessárias para extensão ou lesões profundas. Nesta consulta há linfonodos superficiais '
  'acessíveis, sem sinais de compressão ou outras cadeias palpáveis: ultrassom e radiografia são um '
  'primeiro passo, sem assumir que exames normais excluam linfoma.'),
 ('Ultrassom e radiografia',
  'Selecionados. O ultrassom avalia estrutura sólida, coleção e morfologia. A radiografia procura '
  'alterações torácicas associadas à febre e à perda de peso.'),
 ('FAN, anti-DNA e complemento',
  'A idade e o sexo mantêm autoimunidade no diferencial, mas ainda faltam manifestações que deem '
  'rendimento a esse conjunto. Citopenia persistente ou novos achados podem mudar a prioridade.'),
 ('Inflamação e bioquímica',
  'Selecionadas. Registram inflamação e procuram comprometimento além do pescoço; o padrão encontrado '
  'orientará a próxima investigação, sem identificar sozinho uma doença.'),
 ('Hemoculturas e ecocardiograma',
  'Febre isolada não torna esse conjunto prioritário. Ganha valor com achados de bacteremia ou '
  'endocardite. A escolha é de prioridade neste quadro, não uma contraindicação absoluta.')]),

    painel('res1', 'Primeiros exames', 'Sangue', [
        ex('Hemoglobina / VCM', '11,7 g/dL / 86 fL', 'Hb 12–16 g/dL · VCM 80–100 fL', True),
        ex('Leucócitos', '2.900/mm³', '4.000–11.000/mm³', True),
        ex('Neutrófilos / linfócitos / monócitos', '1.450 / 1.100 / 260 por mm³',
           'N 1.800–7.500 · L 1.000–4.000', True),
        ex('Esfregaço', 'Linfócitos reativos ocasionais, 4% · sem blastos',
           '—'),
        ex('Plaquetas', '188.000/mm³', '150.000–450.000/mm³'),
        ex('VHS / proteína C reativa', '46 mm/h / 24 mg/L', 'até 20 mm/h · até 5 mg/L', True),
        ex('Desidrogenase láctica', '330 U/L', '120–250 U/L', True),
    ], introducao='Colhidos na primeira consulta, no mesmo dia da '
                  'ultrassonografia do pescoço e da radiografia de tórax.'),

    painel('res1b', 'Primeiros exames', 'Bioquímica e urina', [
        ex('AST / ALT', '42 / 47 U/L', 'até 32 / 33 U/L', True),
        ex('Fosfatase alcalina / GGT', '88 / 30 U/L', 'até 104 / 40 U/L'),
        ex('Creatinina', '0,7 mg/dL', '0,5–1,1 mg/dL'),
        ex('Urina tipo 1', 'Densidade 1.018 · sem proteína, hemácias ou leucócitos', 'normal'),
    ]),

    Q('p2', 1, 'Com esses resultados, quais três investigações você acrescenta?',
[('FAN, anti-DNA e complemento', False),
 ('Sorologias para EBV e CMV', True),
 ('Sorologia para Bartonella', False),
 ('Teste de HIV de quarta geração', True),
 ('Sorologia para toxoplasmose', True),
 ('Tomografias de tórax e abdome', False)],
[('EBV e CMV',
  'Prioritários. Faringite inicial, linfócitos reativos e discreta elevação de transaminases sustentam '
  'essa investigação. Linfócitos reativos ocasionais não confirmam infecção viral.'),
 ('HIV',
  'Prioritário. Pode causar febre, adenopatia e citopenias. A ausência de exposição relatada não '
  'dispensa o teste; o resultado deve ser interpretado com a janela de exposição.'),
 ('Toxoplasmose',
  'Prioritária. É compatível com adenopatia cervical subaguda e pode ocorrer sem arranhadura. '
  'A presença de um gato não prova a causa nem é necessária para essa infecção.'),
 ('Bartonella',
  'É uma concorrente pela convivência com gato, mas não há lesão de inoculação, exposição a filhote '
  'ou arranhadura lembrada. Tem menor prioridade relativa; uma história revista ou evolução sugestiva '
  'poderia justificar o teste mesmo sem arranhadura reconhecida.'),
 ('Autoimunidade',
  'Leucopenia merece seguimento, mas isoladamente não torna esse painel mais informativo que a '
  'investigação infecciosa inicial. Procurar manifestações cutâneas, articulares e urinárias continua '
  'sendo necessário.'),
 ('Tomografias',
  'Podem revelar doença profunda e serão consideradas se houver progressão ou investigação inicial '
  'inconclusiva. Não determinam a etiologia do linfonodo. A seleção não exclui linfoma do diferencial.')]),

    estudo('us_cervical', 'Ultrassonografia do pescoço',
           'Pedida na primeira consulta para avaliar os linfonodos palpados. '
           'Neste corte, observe um linfonodo. Descreva a '
           'forma do linfonodo e o que há no centro dele antes de abrir os '
           'achados.',
           IMG / 'us_linfonodo_cervical.jpg',
           'Ultrassonografia com Doppler colorido de outro paciente · comparação didática.',
           credito_meta(IMG / 'us_linfonodo_cervical.jpg.json'),
        [
         ((442, 215), (330, 150), '**Córtex** hipoecoico, regular, em volta de todo o linfonodo.', 12),
         ((386, 312), (140, 250), '**Hilo** central ecogênico, com o vaso hilar se ramificando a partir dele.', -12),
         ((643, 529), (850, 650), '**Vaso** adjacente, fora do linfonodo, com fluxo ao Doppler.', 12),
        ],
        ['No corte apresentado, observa-se um linfonodo ovalado, com córtex '
         'hipoecoico, hilo central ecogênico preservado e vascularização hilar '
         'ao Doppler. Não há área de liquefação visível neste linfonodo. '
         'A imagem não apresenta medidas assinaladas.',
         'Forma oval, hilo preservado e fluxo hilar são o aspecto de um '
         'linfonodo reacional. O ultrassom tranquiliza, mas não afasta linfoma '
         'nem tuberculose no início.']),

    estudo('rx_torax', 'Radiografia de tórax',
           'Pedida na mesma consulta pela febre com sudorese e perda de peso: '
           'procurar linfonodos no mediastino e lesão no pulmão.',
           IMG / 'rx_torax_normal.jpg',
           'Radiografia de outra pessoa · comparação didática.',
           credito_meta(IMG / 'rx_torax_normal.jpg.json'),
        [
         ((350, 500), (170, 450), '**Hilo direito** de tamanho e densidade normais.', 12),
         ((575, 385), (720, 290), '**Botão aórtico** e mediastino superior de largura normal.', -12),
         ((665, 500), (850, 560), '**Hilo esquerdo** sem massa.', 12),
        ],
        ['Pulmões sem opacidades, mediastino e hilos normais, seios '
         'costofrênicos livres.',
         'Não há adenomegalia mediastinal visível nem lesão pulmonar que '
         'aponte tuberculose ou linfoma. A radiografia simples não vê '
         'linfonodos pequenos.']),

    pg('hipotese', 'Investigação dirigida',
       'Faringite no início, febre e linfonodos cervicais posteriores tornam infecções mononucleose-símile uma linha inicial plausível. O exame não mostrou foco dentário, otológico ou cutâneo nem coleção. Não há indicação de repetir antibiótico apenas porque o primeiro falhou.',
       'A equipe solicita sorologia para EBV, CMV e toxoplasmose e teste de quarta geração para HIV. Revê exposição sexual recente, contato com gatos e viagens; não há um achado epidemiológico que defina sozinho a investigação.',
       'Bianca mantém sintomáticos e retorna em uma semana. Infecção local, infecção sistêmica, doença inflamatória e neoplasia permanecem no diferencial.'),

    painel('res2', 'Retorno', 'Sorologias', [
        ex('EBV IgM (anti-VCA)', 'Não reagente', 'não reagente'),
        ex('EBV IgG (anti-VCA)', 'Reagente', '—', True),
        ex('EBV: marcador complementar (EBNA IgG)', 'Reagente', '—', True),
        ex('CMV: IgM / IgG', 'Não reagente / reagente', '—', True),
        ex('Toxoplasmose: IgM / IgG', 'Não reagente / não reagente', 'não reagente'),
        ex('HIV, teste de quarta geração', 'Não reagente', 'não reagente'),
        ex('VDRL', 'Não reagente', 'não reagente'),
    ], introducao='Colhidas na primeira consulta, no 12.º dia de febre.'),

    Q('sorologias_leitura', 1, 'Qual interpretação integra melhor os resultados para EBV?',
[('Infecção passada, sem evidência sorológica de infecção primária recente', True),
 ('Infecção primária em fase tardia, com IgM já desaparecida', False),
 ('Reativação como explicação mais provável para a febre atual', False),
 ('Fase inicial de infecção primária, antes do aparecimento de IgM', False)],
[('Dado decisivo',
  'VCA IgG e EBNA IgG reagentes, com VCA IgM não reagente, favorecem infecção passada. Em apenas 12 '
  'dias de sintomas, não é coerente atribuir o EBNA já presente a essa nova infecção primária: ele '
  'costuma aparecer após meses.'),
 ('O que os marcadores significam',
  'VCA é o antígeno do capsídeo viral. A IgM costuma surgir cedo e desaparecer em 4–6 semanas; a IgG '
  'persiste. EBNA é um antígeno nuclear, cuja IgG geralmente aparece em 2–4 meses e persiste.'),
 ('Concorrentes',
  'Uma IgM já negativa pode ocorrer em fases tardias, mas a cronologia deste episódio não sustenta essa '
  'leitura. IgG e EBNA positivos não demonstram reativação sintomática. A fase inicial antes da IgM '
  'tampouco explica o EBNA desse episódio. As demais infecções continuam dependentes de seus testes e '
  'respectivas janelas.')]),

    pg('evolucao1', 'Terceira semana',
       'No retorno, no 19.º dia, a febre chega a 38,8 °C. O maior linfonodo mede cerca de 3,9 cm no ultrassom de controle, e surgiram dois menores na cadeia cervical posterior direita. Perdeu mais 1 kg. Leucócitos: 2.500/mm³; neutrófilos: 1.300/mm³; LDH: 360 U/L.',
       'Continuam sem linfonodos palpáveis em outras regiões, lesões cutâneas ou sinovite. O comprometimento cervical bilateral continua regional; não equivale, por si, a adenopatia generalizada.',
       'A prova tuberculínica solicitada na avaliação dirigida mede 14 mm. Bianca recebeu BCG na infância e não refere contato conhecido com tuberculose. A radiografia de tórax não mostrou alterações.'),

    bifurcacao('b1', 'Decisão', 'O linfonodo em crescimento',
      'Três semanas de febre, prova tuberculínica de 14 mm e linfonodos '
      'crescendo. Bianca está estável e quer uma resposta. O que você faz?', [
      caminho('Obter uma amostra do linfonodo nesta semana', 'tecido',
              'A análise do tecido e a pesquisa de infecção ajudam a investigar a causa, mantendo as alternativas não infecciosas.'),
      caminho('Iniciar o esquema básico para tuberculose sem tecido', 'ripe',
              'A prova tuberculínica mede infecção, não doença. Seis meses de '
              'tratamento sem confirmação expõem a hepatotoxicidade e podem '
              'mascarar outra causa.'),
      caminho('Prednisona 40 mg ao dia pela febre persistente', 'corticoide',
              'Alivia a febre, e o alívio parece resposta. Trata sem '
              'diagnóstico e pode dificultar a interpretação da amostra.'),
    ]),

    pg('ripe', 'Terceira semana de tratamento',
       'Após iniciar rifampicina, isoniazida, pirazinamida e etambutol, a febre diminui. Na terceira semana, surgem náuseas e vômitos. ALT: 310 U/L (referência até 40); bilirrubina: 0,8 mg/dL; INR: 1,0. O linfonodo permanece com cerca de 3,9 cm.',
       segue='b_toxicidade'),

    pg('corticoide', 'Duas semanas de prednisona',
       'A febre cede em quatro dias e o linfonodo dói menos. Na redução da '
       'dose, a febre volta e o linfonodo cresce de novo. Bianca pergunta se '
       'a melhora confirma uma doença inflamatória.',
       'Ainda não há diagnóstico. Se for tuberculose, o corticoide sem '
       'tratamento a agrava; se for linfoma, pode reduzir a celularidade a '
       'ponto de deixar a biópsia inconclusiva.'),

    bifurcacao('resgate', 'Decisão', 'A febre voltou',
      'O alívio sob prednisona foi transitório. Qual é o próximo passo?', [
      caminho('Reduzir o corticoide e marcar a biópsia, avisando o '
              'patologista', 'tecido',
              'A resposta foi inespecífica. O patologista precisa saber do '
              'corticoide para ler a lâmina.'),
      caminho('Repetir o ciclo que havia aliviado a febre', 'novo_ciclo',
              'Mais um ciclo empurra o diagnóstico sem tratar nenhuma causa '
              'demonstrada.'),
    ]),

    pg('novo_ciclo', 'Mais duas semanas',
       'A febre melhora de novo e volta na redução. Bianca está afastada do '
       'trabalho há um mês, dorme mal e ganhou 4 kg. O linfonodo mede cerca de 4,2 cm no controle. '
       'A equipe abandona os ciclos, reduz a prednisona e marca a biópsia.',
       segue='tecido'),

    pg('tecido', 'A biópsia',
       'Bianca é encaminhada para avaliação do linfonodo. Uma punção por agulha fina, realizada no encaminhamento, mostra população linfoide polimórfica, sem células malignas identificadas. A citometria não detecta população B clonal. O material não permite avaliar a arquitetura do linfonodo.',
       'A febre persiste e o linfonodo não diminuiu. Ele é superficial, acessível e não está aderido aos planos profundos. A causa permanece sem definição.'),

    Q('p4', 1, 'Após essa amostra, qual é o próximo passo?',
[('Retirada de um linfonodo para histologia e microbiologia', True),
 ('Repetir a punção com nova citologia e citometria', False),
 ('Biópsia por agulha grossa para histologia e microbiologia', False),
 ('PET-CT para escolher o linfonodo mais ativo', False)],
[('Melhor opção aqui',
  'A punção não encerrou a investigação: ausência de células malignas e de clone B não exclui todos os linfomas. O linfonodo é acessível e a retirada permite '
  'avaliar sua arquitetura e realizar estudos complementares. A escolha depende também do risco do '
  'procedimento e da disponibilidade local.'),
 ('Alternativas próximas',
  'A punção fina pode ajudar em metástases e infecções, mas avalia mal a arquitetura. A agulha grossa é '
  'uma alternativa quando o risco ou a localização desfavorecem a retirada; não é um exame errado em '
  'si. O PET-CT não distingue com segurança inflamação de neoplasia e, com um linfonodo já acessível, '
  'não resolve a pergunta principal.')]),

    pg('tecido2', 'Amostra do linfonodo',
       'O cirurgião retira o linfonodo cervical mais representativo. A amostra é distribuída conforme o plano acordado: histologia e imuno-histoquímica, citometria de fluxo e investigação microbiológica.',
       'A citometria não identifica população clonal no material analisado; o TRM-TB não detecta micobactéria. Esses resultados, isoladamente, não excluem linfoma nem tuberculose ganglionar. O patologista pede correlação com a arquitetura e a microbiologia.'),

    estudo('arquitetura', 'Biópsia: pequeno aumento',
           'Lâmina de referência de outro paciente, com o padrão que o '
           'patologista mostra na de Bianca. Descreva a distribuição das áreas '
           'claras e das áreas celulares antes de abrir os achados.',
           IMG / 'linfonodo_baixo.jpg',
           'Hematoxilina-eosina, pequeno aumento · outro paciente.',
           credito_meta(IMG / 'linfonodo_baixo.jpg.json'),
        [
         ((560, 560), (820, 430), '**Área pálida e eosinofílica**, ampla e mal delimitada, que substitui o tecido linfoide.', 12),
         ((200, 520), (90, 390), '**Ilha de linfócitos** residuais, azul-escura, entre as áreas pálidas.', 12),
         ((450, 185), (330, 70), '**Cápsula** com gordura perinodal: o contorno do linfonodo está preservado.', -12),
        ],
        ['Arquitetura parcialmente apagada por áreas confluentes e pálidas, com '
         'cápsula preservada, sem granulomas e sem população linfoide '
         'monomórfica.',
         'O que ocupa as áreas pálidas só se define no grande aumento.']),

    estudo('celulas', 'Biópsia: grande aumento',
           'A mesma lâmina de referência em grande aumento. Que células povoam '
           'a área pálida, e que célula chama a atenção pela ausência?',
           IMG / 'linfonodo_alto.jpg',
           'Hematoxilina-eosina, grande aumento · outro paciente.',
           credito_meta(IMG / 'linfonodo_alto.jpg.json'),
        [
         ((325, 452), (150, 330), '**Cariorrexe**: fragmentos nucleares escuros, pequenos e irregulares, espalhados pela área pálida.', 12),
         ((655, 518), (860, 430), '**Histiócito** de núcleo claro, ovalado ou reniforme, com citoplasma pálido.', -12),
         ((845, 345), (760, 250), 'Fundo **eosinofílico e granular** de necrose, sem neutrófilos.', -12),
        ],
        ['Necrose paracortical com abundante cariorrexe e histiócitos, sem '
         'neutrófilos e sem granulomas.',
         'Não apresenta o padrão granulomatoso caseoso típico. Isso enfraquece, mas não exclui tuberculose; a conclusão depende da amostra completa e da microbiologia.']),

    Q('p5', 1, 'Quais duas hipóteses melhor se ajustam ao padrão da biópsia?',
[('Doença de Kikuchi–Fujimoto', True),
 ('Linfadenite lúpica', True),
 ('Linfadenite tuberculosa', False),
 ('Doença da arranhadura do gato', False),
 ('Linfadenite supurativa', False),
 ('Linfoma de Hodgkin', False)],
[('Melhor ajuste',
  'Necrose, cariorrexe, histiócitos e escassez de neutrófilos compõem um padrão compatível com Kikuchi '
  'e também com linfadenite lúpica. A distinção exige correlação clínica, análise completa do tecido e '
  'investigação autoimune.'),
 ('Demais hipóteses',
  'Tuberculose é enfraquecida pela ausência do padrão granulomatoso típico, sem estar excluída. '
  'Arranhadura do gato costuma apresentar granulomas com microabscessos; a forma supurativa, '
  'neutrófilos abundantes. O tecido descrito não demonstra as células e o contexto morfológico '
  'esperados para Hodgkin; discordância clínica exigiria revisão.')]),

    painel('res3', 'Complemento da biópsia', 'Tecido e autoanticorpos', [
        ex('Imuno-histoquímica', 'Histiócitos CD68 e mieloperoxidase positivos · '
           'células dendríticas plasmocitoides CD123 positivas · predomínio de '
           'linfócitos T CD8', '—', True),
        ex('Células de Reed-Sternberg (CD15 / CD30)', 'Ausentes', 'ausentes'),
        ex('Pesquisa de bacilos da tuberculose no tecido (BAAR)', 'Negativa', 'negativa'),
        ex('Cultura de micobactérias e fungos', 'Em andamento', '—'),
        ex('FAN', 'Não reagente', 'não reagente'),
        ex('Anti-DNA nativo', 'Não reagente', 'não reagente'),
        ex('C3 / C4', '112 / 25 mg/dL', '90–180 / 10–40 mg/dL'),
    ], introducao='Com a lâmina, a equipe fecha as alternativas que ela '
                  'deixou abertas.'),

    pg('diagnostico', 'Integração diagnóstica',
       'A revisão da amostra demonstra linfadenite necrosante histiocítica, compatível com doença de Kikuchi–Fujimoto. A morfologia, a imuno-histoquímica e a apresentação clínica sustentam o diagnóstico; ele não foi estabelecido apenas porque outros testes vieram negativos.',
       'A investigação não sustenta infecção supurativa, linfoma ou linfadenite tuberculosa. As culturas ainda serão acompanhadas. FAN e anti-DNA não reagentes, complemento normal e ausência de manifestações sistêmicas tornam lúpus menos provável neste momento, sem representar exclusão definitiva.',
       'O achado raro passa a ser a melhor explicação porque integra o padrão de tecido à doença observada. Persistência, novas manifestações ou evolução discordante reabririam o diagnóstico.'),

    painel('res3b', 'No dia do laudo', 'Sangue', [
        ex('Hemoglobina', '11,4 g/dL', '12–16 g/dL', True),
        ex('Leucócitos / neutrófilos', '2.600 / 1.350 por mm³', 'L 4.000–11.000 · N 1.800–7.500', True),
        ex('Plaquetas', '176.000/mm³', '150.000–450.000/mm³'),
        ex('Ferritina', '480 ng/mL', '15–150 ng/mL', True),
        ex('Triglicerídeos, em jejum', '126 mg/dL', 'até 150 mg/dL'),
        ex('Fibrinogênio', '390 mg/dL', '200–400 mg/dL'),
    ], introducao='Exames de controle durante a persistência da febre.'),

    Q('p6', 1, 'Quais dois padrões, se surgissem no próximo controle, exigiriam investigação urgente de complicação sistêmica?',
[('Plaquetas 70.000/mm³ e fibrinogênio 120 mg/dL', True),
 ('Ferritina 6.000 ng/mL em ascensão e novo aumento do baço', True),
 ('Neutrófilos 1.100/mm³, com hemoglobina e plaquetas estáveis', False),
 ('Ferritina 620 ng/mL, com queda da PCR e melhora da febre', False),
 ('VHS 70 mm/h, com PCR 8 mg/L e recuperação do hemograma', False),
 ('Linfócitos reativos no esfregaço, sem piora das demais linhagens', False)],
[('Padrões que mudam a prioridade',
  'Queda de plaquetas com redução do fibrinogênio sugere um processo sistêmico novo, incluindo consumo '
  'e síndrome hemofagocítica. Ferritina muito elevada e crescente com esplenomegalia também muda a '
  'probabilidade. Ambos exigem avaliação urgente, sem confirmar uma causa isoladamente.'),
 ('Mudanças de menor peso isolado',
  'Neutrófilos de 1.100 ainda exigem controle, mas não representam, sozinhos, deterioração de múltiplas '
  'linhagens. Pequena elevação de ferritina com melhora clínica pode refletir a inflamação em '
  'resolução. O VHS cai lentamente e não deve sobrepor-se à melhora da PCR e do hemograma. Linfócitos '
  'reativos são inespecíficos e precisam da evolução para ganhar significado.'),
 ('Comparação com o painel atual',
  'Até aqui, plaquetas, fibrinogênio e triglicerídeos estão preservados, sem aumento do baço '
  'documentado. A comparação de tendências e órgãos acometidos é mais útil que usar um único ponto de '
  'corte como diagnóstico.')]),

    pg('conduta', 'Conduta após o diagnóstico',
       'Bianca está estável, sem disfunção orgânica e com sintomas em redução. A equipe propõe analgesia conforme necessidade, hidratação e seguimento. Não há evidência suficiente de infecção bacteriana a justificar novo antibiótico.',
       'Sintomas intensos ou persistentes, doença extranodal ou complicações mudariam a avaliação e poderiam justificar tratamento imunomodulador após revisão das alternativas. O diagnóstico não autoriza ignorar deterioração posterior.',
       'A resposta aos sintomáticos será acompanhada junto ao tamanho dos linfonodos, estado geral e hemograma. A cultura final também precisa ser conferida.'),

    pg('tratamento', 'Tratamento e seguimento',
       'Bianca recebe ibuprofeno por dez dias, sem antibiótico, e sai sabendo '
       'que o linfonodo diminui mais devagar que a febre e que o corticoide '
       'fica guardado para doença grave ou arrastada.',
       'Quatro semanas depois está afebril há oito dias. O maior linfonodo '
       'mede 1 cm e não dói. Hemoglobina 12,1 g/dL, leucócitos 4.300/mm³, PCR '
       '4 mg/L. A cultura do linfonodo termina sem crescimento em seis '
       'semanas. Voltou a trabalhar meio período.'),

    Q('p8', 1, 'Neste retorno, quais três grupos de exames você prioriza?',
[('Hemograma', True),
 ('Creatinina, urina e relação proteína/creatinina urinária', True),
 ('FAN, anti-DNA e complemento', True),
 ('Fator reumatoide e anti-CCP', False),
 ('Biópsia da lesão facial', False),
 ('Novas sorologias para EBV e CMV', False)],
[('Prioridades',
  'Hemograma procura novas citopenias. Creatinina, urina e proteinúria rastreiam lesão renal que pode '
  'existir sem edema ou perda de filtração. FAN, anti-DNA e complemento agora têm indicação clínica '
  'pela associação de sinovite e lesão cutânea após o sol, que não existia na apresentação inicial.'),
 ('Concorrentes',
  'Fator reumatoide e anti-CCP podem ajudar se o padrão articular sustentar artrite reumatoide, mas não '
  'integram tão bem a pele e os antecedentes. A biópsia de pele pode esclarecer lesão atípica ou '
  'diagnóstico incerto, sem substituir a busca de acometimento sistêmico. Repetir EBV/CMV não esclarece '
  'prioritariamente este quadro sem nova síndrome infecciosa compatível.')]),

    pg('alta', 'Oito semanas depois',
       'Bianca está sem febre, com linfonodos de menos de 1 cm, e voltou à '
       'sala de aula. A equipe revê com ela o que aconteceu, o que esperar e '
       'quando voltar antes do retorno marcado.',
       conforme=('b1', ['f0', 'f_ripe', 'alta_cort'])),

    fim('f0', 'Recuperação sem desvios',
        'Depois do retorno inicial em meio período, Bianca retoma o trabalho integral na avaliação seguinte, já sem febre ou dor. Não precisou de tratamento específico adicional.',
        'Tecido no momento em que a linfadenopatia passou a crescer, com parte '
        'a fresco, respondeu às hipóteses de uma vez e poupou tratamento '
        'empírico.', 'melhor', fecho='extensao'),

    pg('alta_cort', 'Oito semanas depois',
       'Bianca está sem febre, mas o corticoide deixou marcas: insônia, '
       'inchaço no rosto e glicemia de jejum de 112 mg/dL, que a equipe vai '
       'reavaliar depois da retirada.',
       conforme=('resgate', ['f_cort', 'f_pior'])),

    fim('f_ripe', 'Recuperação depois de uma hepatite medicamentosa',
        'A ALT volta ao normal três semanas depois da suspensão. Bianca fica '
        'sete semanas afastada e sai com uma notificação de tuberculose que '
        'precisou ser encerrada como erro diagnóstico.',
        'A prova tuberculínica não demonstrou doença ativa. A melhora durante o esquema não confirmou tuberculose; a trajetória incluiu toxicidade e atraso até a definição histológica.', 'medio', fecho='extensao'),

    fim('f_cort', 'Recuperação com diagnóstico atrasado',
        'A biópsia, com o patologista avisado, é conclusiva. A prednisona é '
        'retirada em três semanas, e Bianca fica seis semanas afastada.',
        'O corticoide aliviou a febre sem dizer o que ela era. Parar a tempo '
        'e contar ao patologista preservou a leitura da lâmina.', 'medio',
        fecho='extensao'),

    fim('f_pior', 'Dois ciclos de corticoide e dez semanas afastada',
        'Bianca fica dez semanas longe da escola, com 4 kg a mais e a febre '
        'voltando a cada redução. A lâmina, colhida sob corticoide, precisa de '
        'revisão por um segundo patologista antes do laudo.',
        'Ciclos empíricos podem dificultar a interpretação histológica e atrasar o reconhecimento de uma infecção ou neoplasia.', 'pior',
        fecho='extensao'),

    bifurcacao('extensao', 'Extensão opcional', 'Seis meses depois',
      'O caso principal terminou. Quer encerrar ou explorar um cenário de '
      'seguimento?', [
      caminho('Encerrar e ver os pontos de ensino', 'retrospectiva',
              'Retoma o que o caso quis ensinar.'),
      caminho('Explorar um retorno seis meses depois', 'novo_quadro',
              'Cenário independente: não é consequência de nenhuma escolha '
              'anterior nem a evolução de toda paciente com essa doença.'),
    ]),

    pg('novo_quadro', 'Seis meses depois',
       'Bianca volta por dor e rigidez matinal nas mãos há três semanas, e '
       'por manchas vermelhas no rosto depois de uma tarde na praia. Os '
       'linfonodos não voltaram. Sente-se cansada de novo.',
       'Ao exame, sinovite nas metacarpofalângicas e interfalângicas '
       'proximais, e eritema malar poupando os sulcos nasolabiais. Pressão '
       '124/80 mmHg, sem edema.'),

    estudo('eritema_face', 'Fotografia: o rosto',
           'Fotografia de outra paciente com o mesmo tipo de lesão que Bianca '
           'tem no rosto, com os olhos cobertos. Descreva onde fica o eritema '
           'e o que acontece com a pele dos sulcos nasolabiais antes de abrir '
           'os achados.',
           IMG / 'eritema_facial.jpg',
           'Fotografia de outra paciente · olhos cobertos · comparação didática.',
           credito_meta(IMG / 'eritema_facial.jpg.json').replace(
               'setas adicionadas', 'olhos cobertos, recorte e setas adicionadas'),
        [
         ((190, 300), (55, 440), '**Eritema** confluente na região malar direita, plano, sem pápulas nem pústulas.', 12),
         ((700, 360), (905, 470), '**Eritema** na região malar esquerda, com a mesma cor e a mesma textura: a lesão é simétrica.', -12),
         ((242, 470), (120, 615), '**Sulco nasolabial poupado**: a pele da dobra, do lado do nariz até o canto da boca, tem a cor normal.', 12),
        ],
        ['Eritema malar poupando os sulcos nasolabiais, surgido depois de uma '
         'tarde de sol.',
         'Eritema das duas bochechas que respeita os sulcos nasolabiais separa '
         'esse desenho da dermatite seborreica, que ocupa as dobras, e da '
         'rosácea, que traz pápulas e pústulas.']),

    bifurcacao('b2', 'Decisão', 'Os sintomas novos',
      'Como você conduz esse retorno?', [
      caminho('Investigar doença sistêmica agora, incluindo urina e função '
              'renal', 'seguimento',
              'Os sintomas são novos e cabem no lúpus que o seguimento '
              'procurava.'),
      caminho('Atribuir tudo a uma recorrência e observar', 'encerramento',
              'A recorrência faz febre e linfonodo, não sinovite com eritema '
              'malar.'),
    ]),

    painel('seguimento', 'Reavaliação', 'O que a equipe pediu', [
        ex('FAN', '1:640, padrão homogêneo', 'não reagente', True),
        ex('Anti-DNA nativo', 'Reagente', 'não reagente', True),
        ex('C3 / C4', '54 / 7 mg/dL', '90–180 / 10–40 mg/dL', True),
        ex('Hemograma', 'Hb 11,2 g/dL · leucócitos 3.100/mm³ · plaquetas 142.000/mm³', '—', True),
        ex('Creatinina', '0,9 mg/dL', '0,5–1,1 mg/dL'),
        ex('Sedimento urinário', '18 hemácias por campo, 30% dismórficas · sem cilindros', 'sem hemácias', True),
        ex('Relação proteína/creatinina urinária', '0,8 g/g', 'abaixo de 0,2 g/g', True),
    ], introducao='Exames colhidos neste retorno.'),

    pg('nova_doenca', 'O diagnóstico longitudinal',
       'É lúpus eritematoso sistêmico com nefrite: FAN em título alto, '
       'anti-DNA reagente, complemento consumido, hematúria dismórfica e '
       'proteinúria de 0,8 g/g. Proteinúria de 0,5 g/g ou mais com sedimento '
       'ativo indica biópsia renal mesmo com creatinina normal, porque a '
       'classe histológica decide o tratamento.',
       'A biópsia mostra nefrite lúpica classe III. Ela inicia '
       'hidroxicloroquina, salvo contraindicações, bloqueio do '
       'sistema renina-angiotensina pela proteinúria e indução com a '
       'nefrologia e a reumatologia. O primeiro diagnóstico continua válido: '
       'a associação não prova que o episódio anterior já fosse lúpus; a relação exige revisão longitudinal.',
       segue='f1'),

    fim('f1', 'Lúpus reconhecido cedo',
        'Bianca inicia o tratamento da nefrite com creatinina normal, e a '
        'proteinúria cai nos meses seguintes.',
        'Reconhecer manifestações novas evitou que o diagnóstico anterior '
        'explicasse tudo.', 'melhor'),

    pg('encerramento', 'Dois meses depois',
       'Bianca volta com edema de membros inferiores e urina espumosa. A '
       'pressão é 150/96 mmHg. Proteinúria de 2,4 g/g e creatinina de 1,5 '
       'mg/dL.',
       segue='resgate_renal'),

    bifurcacao('resgate_renal', 'Decisão', 'Edema e creatinina subindo',
      'O que acompanha a avaliação do edema?', [
      caminho('Investigação renal e reumatológica imediata, com biópsia',
              'f2', 'Ainda há rim a salvar; o atraso não é, sozinho, '
                    'irreversibilidade.'),
      caminho('Diurético e nova consulta em um mês', 'atraso_renal',
              'Aliviar o edema não trata a nefrite que o produz.'),
    ]),

    pg('atraso_renal', 'Um mês depois',
       'Bianca é internada com creatinina de 2,8 mg/dL e pressão de 170/104 '
       'mmHg. A biópsia mostra nefrite lúpica classe IV com crescentes em 30% '
       'dos glomérulos e algum grau de fibrose.',
       segue='f3'),

    fim('f2', 'Diagnóstico tardio, ainda a tempo',
        'A nefrite lúpica é tratada com a creatinina em 1,5 mg/dL. A função '
        'renal volta perto do basal, com proteinúria residual.',
        'O atraso custou dois meses de proteinúria, não o rim.', 'medio'),

    fim('f3', 'Nefrite com dano crônico',
        'A indução controla a atividade, mas a creatinina estabiliza em 1,9 '
        'mg/dL, com fibrose documentada na biópsia.',
        'Sinovite com eritema malar foi atribuída a uma recorrência que não '
        'fazia aquilo. A lesão renal progrediu no intervalo.', 'pior'),

    pagina('retrospectiva', 'Pontos de ensino', '',
      pontos(
        'Começar pela linfonodomegalia: distribuição, duração, drenagem, exposições e sinais de alarme. Sintomas sistêmicos podem acompanhar adenopatia localizada.',
        'Dor, ultrassom de aspecto reacional e ausência de blastos não excluem neoplasia. Nenhum deles encerra o diferencial.',
        'Selecionar exames para uma pergunta. Sorologia de contato passado não explica automaticamente febre atual; prova tuberculínica não confirma doença ativa.',
        'Crescimento com sintomas persistentes mudou o limiar para biópsia. Planejar a amostra permite investigar infecção e neoplasia sem perder material.',
        'O diagnóstico raro exige evidência positiva e integração. Negativos reduzem probabilidades em graus diferentes; não são uma lista de exclusões absolutas.',
        'Uma evolução discordante reabre o raciocínio. O diagnóstico anterior não deve impedir reconhecer uma doença nova.'),so_kicker=True),

    pg('referencias', 'Fontes e limites',
       'Paciente, valores e percursos são ficcionais. A extensão de seguimento '
       'é um cenário separado, não a evolução necessária da doença. A cena de '
       'abertura é uma ilustração gerada por inteligência artificial, sem '
       'valor diagnóstico.',
       'Gaddey HL, Riegel AM. Unexplained lymphadenopathy: evaluation and '
       'differential diagnosis. Am Fam Physician, 2016. Dumas e cols., '
       'Medicine, 2014: 91 casos de Kikuchi–Fujimoto. Yoo e cols., J '
       'Ultrasound Med, 2011 (ultrassonografia). Ministério da Saúde, Manual de '
       'Recomendações para o Controle da Tuberculose no Brasil, 2.ª ed., 2019 '
       '(prova tuberculínica e hepatotoxicidade). Henter e cols., Pediatr '
       'Blood Cancer, 2007 (HLH-2004). CDC, Epstein-Barr Virus: Laboratory '
       'Testing. KDIGO 2024 Clinical Practice Guideline for the Management of '
       'Lupus Nephritis.',
       'Imagens de outros pacientes, com setas adicionadas: ultrassonografia, '
       'Nevit Dilmen, Wikimedia Commons, CC BY-SA 3.0; radiografia, Mikael '
       'Häggström, Wikimedia Commons, CC0; lâminas, Nephron, Wikimedia '
       'Commons, CC BY-SA 3.0; fotografia do rosto, Doktorinternet, Wikimedia '
       'Commons, CC BY-SA 4.0, com olhos cobertos e recorte '
       '(commons.wikimedia.org/wiki/File:Lupusfoto.jpg).'),
]

REVISAO = []


# Revisão sindrômica de 21/10/2026. A doença permanece oculta até o tecido.
def _inserir_antes(destino, nova):
    pos = next(i for i, e in enumerate(ETAPAS) if e['k'] == destino)
    ETAPAS.insert(pos, nova)

_inserir_antes('res1', pagina('diferencial_inicial', 'Discussão', 'Linfonodomegalia cervical',
    tabela(['Grupo', 'O que procurar nesta paciente', 'O que mudaria a conduta'], [
      ['Infecção local', 'Dentes, orofaringe, ouvido e couro cabeludo; coleção', 'Foco tratável ou necessidade de drenagem'],
      ['Infecção sistêmica', 'Faringite, exposições e janela dos testes', 'Evidência de infecção recente compatível'],
      ['Neoplasia', 'Progressão, outras cadeias, baço e repercussão', 'Persistência ou crescimento que justifique tecido'],
      ['Inflamação / medicamentos', 'Pele, articulações, urina e cronologia de fármacos', 'Achados associados que direcionem exames'],
    ])))

_inserir_antes('b1', Q('p_probabilidade', 1, 'Qual resultado mais fortaleceria tuberculose como causa dos linfonodos?',
[('Cultura do linfonodo positiva para Mycobacterium tuberculosis', True),
 ('Granulomas necrosantes no exame do linfonodo', False),
 ('Nova prova tuberculínica com reação maior', False),
 ('Redução da febre durante tratamento empírico', False)],
[('Mais específico',
  'A identificação de M. tuberculosis na cultura do linfonodo fornece evidência etiológica no órgão '
  'acometido. O teste molecular rápido também pode contribuir; resultados negativos não descartam '
  'sozinhos doença com poucos bacilos.'),
 ('Evidências concorrentes',
  'Granulomas necrosantes apoiam a hipótese, mas também aparecem em outras infecções. Uma prova '
  'tuberculínica maior demonstra resposta imune e não localiza doença. A queda da febre sob tratamento '
  'é inespecífica e pode coincidir com a evolução natural.'),
 ('PPD de 14 mm',
  'O PPD mantém a hipótese em discussão. BCG prévia não permite descartá-lo automaticamente, e '
  'radiografia normal não exclui tuberculose ganglionar.')]))

_inserir_antes('diagnostico', pagina('diferencial_final', 'Discussão', 'Revisão das hipóteses',
    tabela(['Hipótese', 'Dados que a enfraquecem', 'Limite da conclusão'], [
      ['Infecção viral aguda', 'Sorologias sem padrão recente e progressão', 'Janela e exposição sempre importam'],
      ['Tuberculose ganglionar', 'Sem granulomas; teste molecular e pesquisa de bacilos negativos', 'Negativos isolados não excluem; acompanhar cultura'],
      ['Linfoma', 'Revisão morfológica e imuno-histoquímica sem suporte', 'Citometria isolada não basta'],
      ['Linfadenite associada a lúpus', 'Sem manifestações associadas, autoanticorpos ou consumo de complemento', 'Seguimento permanece aberto'],
    ])))

for _n, _e in enumerate((x for x in ETAPAS if x['t'] in ('pergunta','pareamento')), 1):
    _e['kicker'] = f'Pergunta {_n}'
ETAPAS[-1]['corpo'] += p('Referências da revisão sindrômica: <a href="https://www.cdc.gov/epstein-barr/php/laboratories/index.html">CDC — sorologia para EBV</a>; <a href="https://www.cdc.gov/tb/hcp/testing-diagnosis/index.html">CDC — investigação de tuberculose</a>; <a href="https://www.nice.org.uk/guidance/ng52/chapter/Recommendations">NICE NG52 — amostragem em suspeita de linfoma</a>.')


_inserir_antes('conduta', pg('relacao_lupus', 'Relação com o lúpus',
    'A doença de Kikuchi–Fujimoto tem associação descrita com lúpus eritematoso sistêmico (LES). Pode ocorrer antes, ao mesmo tempo ou depois do diagnóstico de LES. Essa associação não significa que toda paciente desenvolverá lúpus nem que o episódio atual já seja uma manifestação dele.',
    'O lúpus também pode causar linfadenite com necrose e se parecer com Kikuchi na biópsia. Por isso, o laudo precisa ser integrado à história, ao exame físico e aos exames laboratoriais. Em Bianca, a avaliação atual não sustenta LES; FAN e anti-DNA negativos e complemento normal devem ser interpretados nesse contexto.',
    'No seguimento, artrite persistente, lesões relacionadas ao sol, úlceras orais, dor pleurítica, edema ou alterações na urina justificam nova avaliação. Conforme os achados, reavaliam-se hemograma, creatinina, urina/proteinúria e autoanticorpos/complemento. O objetivo é reconhecer um novo quadro clínico, sem repetir mensalmente um painel autoimune em quem está bem.'))
for _e in ETAPAS:
    if _e.get('segue') == 'conduta':
        _e['segue'] = 'relacao_lupus'

for _n, _e in enumerate((x for x in ETAPAS if x['t'] in ('pergunta', 'pareamento')), 1):
    _e['kicker'] = f'Pergunta {_n}'

_inserir_antes('diferencial_final', pagina('leitura_imuno', 'Discussão', 'Como interpretar a imuno-histoquímica',
    p('O patologista usa anticorpos para marcar proteínas nas células do tecido. Isso ajuda a reconhecer quais células participam da lesão. “Positivo” significa que a proteína foi identificada; não significa, por si só, câncer.'),
    tabela(['Marcador', 'O que ajuda a identificar', 'Significado nesta biópsia'], [
        ['CD68 e mieloperoxidase (MPO)', 'Histiócitos: macrófagos presentes no tecido', 'Destacam os histiócitos junto às áreas de necrose'],
        ['CD123', 'Células dendríticas plasmocitoides, que participam da resposta imune', 'Sua presença compõe o padrão inflamatório observado'],
        ['CD8', 'Uma população de linfócitos T', 'Mostra o predomínio de linfócitos T citotóxicos na lesão'],
    ]),
    p('O conjunto é compatível com Kikuchi quando acompanha a morfologia já discutida. Nenhum desses marcadores, isoladamente, confirma o diagnóstico ou exclui linfoma; pode haver sobreposição com linfadenite do lúpus. Para o clínico, o essencial é integrar o laudo à evolução, sem decorar os marcadores.'),
    p('MPO aqui é uma proteína marcada no tecido: não é o exame de sangue anti-MPO/ANCA. Referências: <a href="https://pubmed.ncbi.nlm.nih.gov/11549584/">estudo dos histiócitos CD68/MPO</a>; <a href="https://meridian.allenpress.com/aplm/article/147/7/767/488040/Clinicopathologic-Analysis-of-Kikuchi-Fujimoto">série clinicopatológica de 170 casos</a>.'), so_kicker=True))

_pos = next(i for i,e in enumerate(ETAPAS) if e['k'] == 'tecido')
ETAPAS[_pos:_pos] = [
 bifurcacao('b_toxicidade', 'Decisão', 'Reavaliação durante o tratamento',
    'Como conduzir as alterações da terceira semana?', [
      caminho('Suspender o esquema e investigar a lesão hepática', 'toxicidade_revisao',
              'ALT acima de três vezes o limite com sintomas exige interromper os fármacos hepatotóxicos e avaliar gravidade e outras causas. A indicação do esquema também precisa ser revista.'),
      caminho('Manter o esquema, tratar as náuseas e repetir exames em uma semana', 'toxicidade_piora',
              'A presença de sintomas com esse aumento de ALT torna insegura a manutenção. A queda da febre não confirma a indicação do tratamento.'),
    ]),
 pg('toxicidade_revisao', 'Reavaliação',
    'O esquema é interrompido. A equipe avalia outras causas de hepatite, acompanha ALT, bilirrubina e INR e discute a hipótese de tuberculose. Os sintomas melhoram, mas o linfonodo permanece aumentado.',
    'A biópsia é organizada após a avaliação clínica. O patologista e o laboratório recebem a informação de que houve tratamento prévio.', segue='tecido'),
 pg('toxicidade_piora', 'Quatro dias depois',
    'Neste percurso simulado, Bianca retorna antes do exame programado por vômitos persistentes. ALT: 740 U/L; bilirrubina: 2,1 mg/dL; INR: 1,1. Está alerta e sem hipotensão. É internada para avaliação, e o esquema é interrompido.',
    'Não há falência hepática documentada, mas a evolução exige vigilância. A piora é uma possibilidade clínica deste ramo, não uma consequência inevitável em todo paciente.', segue='b_resgate_hepatico'),
 bifurcacao('b_resgate_hepatico', 'Decisão', 'Durante a internação',
    'Como retomar a investigação dos linfonodos?', [
      caminho('Reavaliar as hipóteses e obter tecido quando clinicamente seguro', 'toxicidade_resgate',
              'Estabilizar a paciente e rever o diagnóstico permite investigar sem reexposição a um esquema cuja indicação não foi confirmada.'),
      caminho('Planejar reintrodução do esquema após melhora da ALT, sem obter tecido', 'f_sem_confirmacao',
              'A reintrodução pode ser necessária em tuberculose confirmada, com planejamento especializado. Aqui, a causa dos linfonodos continua sem demonstração e exige reavaliação antes dessa decisão.'),
    ]),
 pg('toxicidade_resgate', 'Após estabilização',
    'A lesão hepática começa a regredir. A equipe obtém uma amostra do linfonodo e comunica todos os medicamentos recebidos. O percurso passa a incluir os riscos e o afastamento decorrentes da internação.', segue='tecido'),
 fim('f_sem_confirmacao', 'Investigação incompleta',
    'Neste encerramento alternativo, a causa dos linfonodos não foi demonstrada. A paciente continua em acompanhamento por lesão hepática, e a proposta de reexposição precisa de revisão especializada.',
    'A melhora da febre durante um tratamento empírico não substitui confirmação diagnóstica. Este ramo termina com incerteza, não com o diagnóstico raro presumido.', 'pior'),
]

_inserir_antes('nova_doenca', bifurcacao('b_renal_inicial', 'Decisão', 'Após os novos exames',
    'Qual é o próximo passo?', [
      caminho('Confirmar as alterações urinárias e organizar avaliação renal e reumatológica', 'nova_doenca',
              'Proteinúria de 0,8 g/g e hematúria, no contexto clínico e sorológico, justificam avaliação de nefrite e discussão de biópsia, mesmo com creatinina normal.'),
      caminho('Tratar as manifestações cutâneas e articulares e rever a urina em dois meses', 'encerramento',
              'A função de filtração preservada não afasta inflamação renal. Adiar a investigação pode permitir progressão antes de a creatinina subir.'),
    ]))
for _n, _e in enumerate((x for x in ETAPAS if x['t'] in ('pergunta', 'pareamento')), 1):
    _e['kicker'] = f'Pergunta {_n}'

# Medida aproximada baseada na escala visível da imagem original (D = 4 cm).
from .medida_us import sobreposicao as _medida_us
_us = next(e for e in ETAPAS if e['k'] == 'us_cervical')
_us['corpo'] = _us['corpo'].replace('</g></svg>', _medida_us() + '</g></svg>', 1)
_us['corpo'] = _us['corpo'].replace('A imagem não apresenta medidas assinaladas.',
    'Medida aproximada no corte: 3,5 × 1,1 cm, estimada pela escala de profundidade de 4 cm da imagem original. Cálipers A/B e régua de 1 cm adicionados para ensino; não são medidas registradas no exame original.')
_us['corpo'] = _us['corpo'].replace('setas adicionadas', 'setas, cálipers e régua adicionados · estimativa didática')

# Retorno tardio: pergunta antes de investigar a nova síndrome, com resultados logo adiante.
_p8 = next(e for e in ETAPAS if e['k'] == 'p8')
ETAPAS.remove(_p8)
_inserir_antes('b2', _p8)
for _n, _e in enumerate((x for x in ETAPAS if x['t'] in ('pergunta', 'pareamento')), 1):
    _e['kicker'] = f'Pergunta {_n}'

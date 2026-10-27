"""Febre prolongada numa valvopata reumática, com baço palpável, em Sobral.

Reescrito em 26/09/2026 no molde do //New England// (piloto: leptospirose;
ver Artifacts/nejm-casos-classicos/GRAMATICA_LIDA_2026-09-26.md). Apresentação
curta, ficha, exame com os vitais em primeiro, primeiros exames entregues
prontos. Revisto em 30/09 ("mais slides de conteúdo e menos de perguntas"):
seis perguntas, nunca duas telas interativas seguidas, e as duas perguntas
antes da virada só interpretam e localizam (o mecanismo da anemia, o sítio da
lesão renal), com alternativas que são categorias. A âncora da equipe
(calazar, linfoma, tuberculose) fica registrada na evolução, como texto. A
virada é a hemocultura colhida antes de mais um antibiótico; o agente manda
olhar o cólon (página de discussão) e o nome só aparece no ecocardiograma,
depois da metade do percurso. As decisões de conduta continuam mudando o
desfecho.

Paciente ficcional. Critérios de Duke-ISCVID 2023 (Fowler, Clin Infect Dis
2023); conduta pela diretriz da ESC de 2023; filtração pelo CKD-EPI 2021.
"""
import json
from pathlib import Path

from motor.estudo_imagem import estudo
from motor.etapas import (alt, bifurcacao, caminho, capa, desfecho, op, p,
                          pagina, painel, par, pareamento, pergunta, pontos,
                          topicos, vitais)

TITULO = 'Pequenos sinais'
RODAPE = 'Paciente ficcional · evoluções simuladas para ensino'
COR = '#db2777'
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
    capa(TITULO, fundo='cena.png', kicker='Caso interativo',
         selo='Paciente ficcional · procedência e créditos na última tela'),

    pg('historia', 'Apresentação',
       'Lúcia, costureira de 59 anos, moradora de Sobral, no Ceará, é encaminhada '
       'ao ambulatório de clínica médica por cinco semanas de febre no fim da '
       'tarde, suor à noite e cansaço. Perdeu 5 kg. "Não tenho mais força nem '
       'para a máquina de costura."',
       'Na terceira semana, a unidade básica tratou como infecção urinária, com '
       'ciprofloxacino por sete dias; a febre sumiu e voltou quatro dias depois. '
       'Na quarta semana recebeu amoxicilina por cinco dias por sinusite, sem '
       'mudança. Está sem antibiótico há seis dias e trouxe as anotações do '
       'termômetro: entre 37,8 e 38,4 °C, quase sempre depois das 16 horas.',
       'Tem dor nos joelhos e na lombar, sem inchaço. Nega tosse, disúria, '
       'diarreia, dor de garganta, manchas na pele, viagens e contato recente '
       'com tuberculose.'),

    pagina('ficha', 'Ficha do paciente', '',
           topicos(('Antecedentes', 'Hipertensão há oito anos. Febre reumática aos 11 '
                    'anos; o posto acompanha um sopro, e um ecocardiograma de três '
                    'anos atrás descreveu insuficiência mitral moderada. Anemia '
                    'ferropriva há seis meses, tratada com sulfato ferroso, sem outra '
                    'investigação. Duas cesáreas.'),
                   ('Medicações', 'Losartana 50 mg ao dia. O sulfato ferroso foi '
                    'suspenso há dois meses, por "estômago ruim". Paracetamol quando a '
                    'febre incomoda.'),
                   ('Hábitos', 'Nunca fumou, não bebe. Usa prótese dentária superior '
                    'e vai pouco ao dentista.'),
                   ('Vida social', 'Mora com a filha numa casa com quintal, num bairro '
                    'da periferia de Sobral, e costura em casa. Tem um gato; os '
                    'vizinhos criam cães e galinhas.'),
                   ('Família', 'Mãe morreu aos 70 anos de acidente vascular cerebral. '
                    'Um irmão tratou tuberculose pulmonar há dez anos. Sem câncer '
                    'conhecido na família.')),
           so_kicker=True),

    pagina('exame', 'Exame físico', '',
           vitais(('Temperatura', '38,1 °C', True),
                  ('Pressão arterial', '132/70', False),
                  ('Frequência cardíaca', '98', False),
                  ('Frequência respiratória', '18', False),
                  ('SpO₂ em ar ambiente', '96%', False),
                  ('Peso', '54 kg', False)),
           topicos(('Estado geral', 'Emagrecida, mucosas descoradas, anictérica.'),
                   ('Linfonodos', 'Sem adenomegalias cervicais, supraclaviculares, '
                    'axilares ou inguinais.'),
                   ('Coração', 'Ritmo regular. Sopro holossistólico 3+/6 no foco '
                    'mitral, irradiado para a axila. Sem terceira bulha.'),
                   ('Pulmões', 'Murmúrio presente, sem ruídos adventícios.'),
                   ('Abdome', 'Baço palpável a 2 cm do rebordo costal esquerdo, '
                    'indolor. Fígado no rebordo.'),
                   ('Membros e pele', 'Dor à mobilização dos joelhos, sem calor nem '
                    'derrame. Sem exantema.')),
           so_kicker=True),

    painel('res1', 'Primeiros exames', 'Sangue', [
        ex('Hemoglobina / hematócrito', '9,8 g/dL / 30%', 'Hb 12–16 g/dL', True),
        ex('VCM / RDW', '76 fL / 17,8%', '80–100 fL / 11,5–14,5%', True),
        ex('Leucócitos', '11.200/mm³ · neutrófilos 78%', '4.000–11.000/mm³', True),
        ex('Plaquetas', '180.000/mm³', '150.000–450.000/mm³'),
        ex('VHS / proteína C reativa', '86 mm/h / 74 mg/L', 'até 20 / até 5', True),
        ex('Ureia / creatinina', '48 / 1,3 mg/dL {{(TFG 47, CKD-EPI 2021)}}', 'até 42 / 0,6–1,1', True),
        ex('Proteínas totais / albumina', '7,8 / 3,0 g/dL {{(globulinas 4,8)}}', '6,0–8,0 / 3,5–5,0', True),
        ex('AST / ALT / bilirrubina total', '28 / 24 U/L / 0,6 mg/dL', 'até 40 / 41 / 1,2'),
    ], introducao='Colhidos na primeira consulta. Três pares de hemoculturas foram '
                  'colhidos por punções separadas, antes de qualquer antibiótico.'),

    painel('res1b', 'Primeiros exames', 'Urina e eletrocardiograma', [
        ex('Urina, tira e leitura inicial', 'Densidade 1.018 · 15 hemácias por campo · proteína 1+ · sem leucocitúria', '—', True),
        ex('Eletrocardiograma', 'Ritmo sinusal, 96 bpm · PR 180 ms · sem outras alterações', '—'),
    ]),

    pg('reavaliacao_rotina', 'Após os primeiros resultados',
       'Lúcia continua febril, sem hipotensão ou dispneia. O hemograma mostra anemia microcítica, e a creatinina de 1,3 vem acompanhada de sangue e proteína na urina. A equipe separa duas questões: investigar a anemia anterior à febre e esclarecer a alteração urinária atual.',
       'Solicita ferritina e saturação da transferrina, revisão manual do sedimento, quantificação da proteinúria e complemento. Pela febre com artralgia e alteração renal, acrescenta FAN e fator reumatoide como investigação dirigida, sem tomá-los como rastreio automático.',
       'Em paralelo, a febre prolongada numa valva previamente doente já motivou três pares de hemoculturas. Lúcia é internada, inicia antibiótico empírico endovenoso após a coleta e tem ecocardiografia solicitada; essas medidas não aguardam ferro, complemento ou autoanticorpos.'),

    painel('dirigidos_anemia', 'Investigação dirigida', 'Anemia', [
        ex('Ferritina / saturação da transferrina', '18 ng/mL / 7%', '15–150 ng/mL / 20–45%', True),
    ], introducao='Resultados solicitados após reconhecer microcitose e recuperar a cronologia da anemia, ainda na avaliação inicial.'),

    Q('p1', 1,
      'Quais duas conclusões você tira da avaliação da anemia?', [
      ('Há deficiência absoluta de ferro, mesmo com inflamação concomitante', True),
      ('A investigação gastrointestinal continua indicada após a menopausa', True),
      ('A faixa de referência da ferritina favorece inflamação isolada', False),
      ('A febre de cinco semanas explica satisfatoriamente toda a cronologia da anemia', False),
      ('Microcitose e RDW elevado priorizam hemoglobinopatia sobre perda de ferro', False),
    ], [('Integração', 'A ferritina deveria subir com a inflamação; 18 torna estoques reduzidos muito prováveis. Saturação baixa e microcitose reforçam a falta de ferro, sem excluir um componente inflamatório associado.'), ('Cronologia', 'A anemia precede a febre e não deve ser atribuída integralmente à doença atual. Na mulher após a menopausa, investigar trato gastrointestinal, em geral com endoscopia alta e colonoscopia. Hemoglobinopatia pode dar microcitose, mas explica pior o conjunto de estoques baixos e cronologia.'), ('Como comparar as anemias', 'Inflamação pode elevar a ferritina e esconder deficiência de ferro. Uma ferritina baixa, mesmo nesse contexto, pesa a favor de deficiência real. A cronologia impede atribuir seis meses de anemia apenas à febre recente; causas coexistentes precisam ser procuradas.')]),

    painel('dirigidos_rim', 'Investigação dirigida', 'Urina e mecanismo renal', [
        ex('Sedimento, revisão manual', '15 hemácias por campo, 40% dismórficas', '—', True),
        ex('Proteína / creatinina na urina', '0,8 g/g', 'até 0,2 g/g', True),
        ex('Fator antinuclear', 'Não reagente', 'não reagente'),
        ex('Fator reumatoide', '64 UI/mL', 'até 14 UI/mL', True),
        ex('Complemento C3 / C4', '58 / 22 mg/dL', '90–180 / 10–40', True),
    ], introducao='A hematúria e a proteína na urina motivaram estes pedidos; os resultados chegam ao longo do primeiro dia, com a investigação cardíaca já em curso.'),

    Q('p2', 2,
      'Qual mecanismo melhor explica a alteração renal?', [
      ('Glomerulonefrite relacionada a infecção persistente', True),
      ('Nefrite intersticial pelos antibióticos recentes', False),
      ('Hipoperfusão com hematúria incidental de via baixa', False),
      ('Vasculite pauci-imune como hipótese prioritária', False),
      ('Crioglobulinemia como hipótese prioritária', False),
    ], [('Integração', 'Dismorfismo e proteinúria favorecem origem glomerular. C3 baixo com febre prolongada sustenta mecanismo associado a infecção e imunocomplexos; fator reumatoide pode acompanhar esse processo, sem provar artrite reumatoide.'), ('Comparação', 'Antibióticos tornam nefrite intersticial possível, mas ela integra pior o complemento e o sedimento. Pauci-imune costuma preservar complemento; crioglobulinemia costuma reduzir C4. São diferenças de probabilidade, não exclusões. A TFG calculada é estimativa pontual e não estabelece doença renal crônica.'), ('Como comparar as lesões renais', 'Infecção persistente pode causar lesão glomerular por resposta imune. Vasculite primária, nefrite por medicamento e hipoperfusão permanecem alternativas. Sedimento, complemento, culturas e cronologia ajudam a distingui-las; nenhum deles encerra o diferencial sozinho.')]),

    estudo('rx_adm', 'Radiografia de tórax',
           'Radiografia da primeira consulta, parte da rodada inicial de febre '
           'prolongada: procura infiltrado, cavidade e linfonodos no mediastino.',
           IMG / 'rx_torax_normal.jpg',
           'Radiografia.',
           credito_meta(IMG / 'rx_torax_normal.jpg.json'),
        [
         ((300, 180), (130, 105), '**Ápice direito** sem opacidade nem cavidade.', 12),
         ((370, 462), (140, 560), '**Hilo direito** de tamanho e densidade normais.', -12),
         ((455, 300), (620, 150), '**Traqueia** central, sem desvio; mediastino superior sem alargamento.', 12),
        ],
        ['Pulmões sem infiltrado, cavidade ou nódulo. Hilos e mediastino sem '
         'alargamento. Sem derrame pleural.']),

    pg('plano', 'Plano inicial',
 'Lúcia é internada. A equipe considera infecção persistente com repercussão renal, doença linfoproliferativa e infecções endêmicas. A valvopatia, a febre e o sedimento mantêm a possibilidade de foco cardíaco desde esta etapa; ausência de lesões típicas na pele não a afasta.',
 'As três hemoculturas já foram colhidas. Pela suspeita de infecção valvar, mantém-se a antibioticoterapia empírica endovenosa já iniciada, conforme o protocolo local e a função renal, sem aguardar identificação do agente. A ecocardiografia já solicitada segue prioritária; acrescenta-se teste rK39. Não há instabilidade, edema pulmonar nem sinal neurológico focal. A ferropenia também requer investigação gastrointestinal, organizada conforme a estabilidade.'),

    pg('investiga', 'Primeiro dia, à tarde',
 'O teste rK39 não é reagente. Lúcia permanece sem hipotensão e conversa normalmente, mas ainda tem pouca disposição para comer. A filha percebe que ela se levanta menos do leito por cansaço.',
 'O resultado isolado não encerra a investigação de leishmaniose. A equipe revê a cronologia da anemia, a função renal e a valva previamente doente, antes de indicar novos procedimentos invasivos.'),

    pg('dor_nova', 'Primeira noite',
 'Depois do jantar, Lúcia sente dor contínua abaixo das costelas à esquerda, que não existia na consulta. Está com 38,2 °C, frequência cardíaca de 106 e pressão de 126/68 mmHg. O abdome apresenta dor localizada, sem defesa ou rigidez.',
 'Não houve queda, esforço ou vômito. Não há dor torácica nem dispneia. A equipe mantém vigilância e precisa decidir qual informação buscar primeiro para integrar esse evento à febre e à alteração urinária.'),

    bifurcacao('b_foco_inicial', 'Decisão', 'Novo sintoma',
 'Qual exame você prioriza nesta reavaliação?', [
 caminho('Ecocardiograma transtorácico', 'eco_inicial', 'Procura uma fonte cardíaca possível no contexto de febre, valvopatia e fenômenos em órgãos distintos. Não substitui avaliar a dor abdominal se ela persistir.'),
 caminho('Tomografia de abdome com contraste', 'abdome_inicial', 'Pode caracterizar uma complicação esplênica. O benefício é ponderado com a função renal e a situação clínica; a avaliação cardíaca continua indicada em paralelo.')]),

    pg('eco_inicial', 'Avaliação inicial da valva',
 'O exame portátil mostra a valva mitral espessada e regurgitação, mas a janela é limitada e não permite caracterizar uma eventual massa pequena. Não há derrame pericárdico. O resultado não encerra a suspeita clínica, e a equipe solicita avaliação ecocardiográfica complementar.',
 'A dor abdominal diminui com analgesia, sem desaparecer. Lúcia continua sem sinais de peritonite ou instabilidade, e a investigação do baço permanece programada.', segue='segundo_dia'),

    pg('abdome_inicial', 'Avaliação do abdome',
 'A tomografia mostra esplenomegalia e uma pequena área periférica em cunha, sem realce, compatível com infarto esplênico; não há coleção drenável ou adenomegalias volumosas. O resultado descreve a lesão, mas não estabelece sua causa.',
 'Lúcia permanece estável e a dor reduz com analgesia. O achado aumenta a importância de procurar uma fonte embólica, sem excluir outros mecanismos de oclusão. A ecocardiografia é mantida como prioridade.', segue='segundo_dia'),

    pg('segundo_dia', 'Segundo dia, 7 horas',
       'A febre de 38,4 °C voltou às 16 horas da véspera, como todos os dias. '
       'Às 7 horas, a microbiologia liga: os três pares positivaram durante a '
       'madrugada, entre 16 e 22 horas de incubação, todos com cocos '
       'gram-positivos em cadeia. A identificação e o antibiograma estão em '
       'curso. A antibioticoterapia empírica iniciada após a coleta é mantida '
       'até o ajuste pelo agente e pela sensibilidade.',
       'A avaliação abdominal é completada: a TC mostra pequeno infarto '
       'esplênico periférico, sem abscesso. No percurso que priorizou a TC, '
       'trata-se do achado já conhecido; no que priorizou o eco, é o resultado '
       'da investigação que estava programada.'),

    Q('p4', 3,
      'Após os novos resultados, quais dois exames você prioriza?', [
      ('Ecocardiograma transesofágico', True),
      ('Colonoscopia', False),
      ('Antibiograma das hemoculturas positivas', True),
      ('Nova punção de medula para leishmaniose', False),
      ('PET-CT', False),
      ('Procalcitonina', False),
    ], [('Prioridades', 'O transesofágico é indicado para esclarecer a suspeita, sobretudo quando o estudo transtorácico é limitado. Bacteremia concordante, valvopatia e possível embolia justificam prosseguir. A imagem ilustrativa adiante é transtorácica; o resultado do transesofágico é descrito na evolução. O antibiograma orienta o tratamento dirigido, sem deduzir espécie apenas do Gram.'), ('Alternativas', 'Colonoscopia continua indicada pela ferropenia, mas não é o exame para localizar o foco cardíaco agora; a identificação posterior reforçará sua prioridade. Punção de medula repete investigação de menor rendimento diante deste dado novo. PET-CT não substitui ecocardiografia inicial de valva nativa. Procalcitonina não invalida três coletas concordantes. O tempo de positividade sozinho não prova foco intravascular.')]),

    pg('identificacao', 'Terceiro dia',
       'Com 44 horas de incubação sai a identificação: três de três pares com '
       '//Streptococcus gallolyticus// (antigo //S. bovis// biotipo I), sensível '
       'à penicilina, concentração inibitória mínima de 0,06 µg/mL.',
       'Perguntada de novo sobre o intestino, Lúcia conta que há três meses as '
       'fezes às vezes vêm mais escuras. Atribuía ao sulfato ferroso, mas o '
       'ferro foi suspenso há dois meses e as fezes escuras continuaram.'),

    pagina('agente', 'Discussão', 'Uma porta de entrada ainda aberta', p('A identificação do agente faz a equipe rever a anemia de seis meses. Lúcia está após a menopausa e não completou a investigação gastrointestinal. As fezes escuras persistiram depois da suspensão do ferro; não há endoscopia prévia disponível.')),

    pagina('beira_leito', 'À beira do leito', '',
           p('Durante o acompanhamento, Lúcia refere um ponto doloroso novo no dedo. O residente examina mãos, pés '
             'e olhos com calma, sob luz boa. Lúcia também lembra de "dois caroços '
             'doloridos" na ponta dos dedos na semana anterior, que sumiram em '
             'dois dias.'),
           topicos(('Unhas', 'Três hemorragias lineares, finas e avermelhadas, sob as '
                    'unhas do segundo e do terceiro dedos da mão direita.'),
                   ('Dedos', 'Nódulo de 4 mm, doloroso, na polpa do quarto dedo direito.'),
                   ('Plantas', 'Duas máculas eritematosas de 3 mm na planta esquerda, '
                    'indolores à pressão.'),
                   ('Olhos', 'Duas petéquias na conjuntiva palpebral inferior esquerda, '
                    'vistas só com a pálpebra evertida. Fundo de olho sem '
                    'hemorragias.')),
           so_kicker=True),

    estudo('unhas', 'Hemorragias sob a unha',
           'Observe a região sob as unhas. Olhe a direção dos traços e onde eles ficam no leito ungueal.',
           IMG / 'unhas_hemorragia.jpg',
           'Fotografia · recortada na unha.',
           credito_meta(IMG / 'unhas_hemorragia.jpg.json'),
        [
         ((437, 690), (215, 560), '**Traços finos**, vermelho-escuros, no terço distal do leito '
          'ungueal, alinhados no sentido em que a unha cresce.', 12),
         ((684, 727), (870, 590), 'Outro **traço isolado** do mesmo tipo, junto à faixa branca da '
          'borda livre.', -12),
         ((560, 390), (800, 200), '**Leito ungueal** rosado e liso no restante: a lesão é linear e '
          'pontual, não uma mancha difusa.', 12),
        ],
        ['No exame de Lúcia: três hemorragias lineares, finas e avermelhadas, sob as '
         'unhas do segundo e do terceiro dedos da mão direita.']),

    estudo('plantas', 'Máculas sem dor',
           'Observe as lesões na palma da mão. Repare no relevo e na cor, e lembre que ela não sente dor ao apertá-las.',
           IMG / 'palma_maculas.jpg',
           'Fotografia.',
           credito_meta(IMG / 'palma_maculas.jpg.json'),
        [
         ((421, 346), (200, 225), '**Mácula eritematosa** de poucos milímetros, plana, de borda '
          'irregular, na base da palma.', 12),
         ((529, 381), (470, 575), 'Outra **mácula** do mesmo tipo, separada da primeira por pele '
          'de cor normal.', -12),
         ((607, 371), (790, 250), 'Mais uma, perto da borda da mão: as lesões se espalham sem se '
          'juntar e sem relevo.', 12),
        ],
        ['No exame de Lúcia: duas máculas eritematosas de 3 mm na planta esquerda, '
         'indolores à pressão.',
         'Plana e indolor é o que a separa do nódulo da polpa digital, que tem '
         'relevo e dói.']),

    estudo('eco', 'Ecocardiograma transtorácico',
           'Bacteremia contínua por um estreptococo de origem intestinal, numa '
           'valva reumática, com lesões novas nas mãos, nos pés e na conjuntiva: '
           'o estudo detalhado da valva é feito pela equipe de ecocardiografia. Corte apical de quatro '
           'câmaras.',
           IMG / 'eco_4c.jpg',
           'Quadro de vídeo.',
           credito_meta(IMG / 'eco_4c.jpg.json'),
        [
         ((743, 655), (900, 520), '**Massa ecogênica** presa à valva mitral, que no vídeo se move com os folhetos.', 12),
         ((690, 785), (880, 890), '**Átrio esquerdo**, que recebe o jato da regurgitação.', -12),
         ((535, 470), (300, 370), '**Septo interventricular**: à direita dele, o ventrículo esquerdo.', 12),
        ],
        ['Vegetação móvel de 12 mm no folheto anterior mitral. Insuficiência '
         'mitral importante ao Doppler, com jato excêntrico. Ventrículo esquerdo '
         'de tamanho normal, fração de ejeção de 62%. Sem derrame pericárdico.']),

    Q('p6', 4, 'Quais dois exames você solicita após identificar a bactéria?', [('Hemoculturas de controle após terapia dirigida', True), ('Colonoscopia quando clinicamente estabilizada', True), ('Fator reumatoide', False), ('Pesquisa de sangue oculto nas fezes', False), ('Tomografia de abdome', False), ('Biópsia renal antes de iniciar betalactâmico', False)], [('Prioridades', 'Hemoculturas de controle documentam depuração e revelam persistência sob terapia. Colonoscopia pesquisa lesão colorretal associada a este agente; a ferropenia já era indicação independente. A sequência mostra culturas negativas e o resultado endoscópico.'), ('Comparação', 'Fator reumatoide pode persistir e não documenta esterilização. Sangue oculto negativo não descarta fonte intermitente nem deve condicionar endoscopia. Tomografia não substitui avaliação mucosa com possibilidade de biópsia. Biópsia renal pode ser útil em evolução discordante, mas não precede tratar esta infecção.')]),

    pg('virada', 'O diagnóstico',
       'É **endocardite infecciosa** de valva mitral nativa, sobre cardiopatia '
       'reumática, por //Streptococcus gallolyticus//.',
       'A valva deformada pela febre reumática tem endotélio irregular, onde '
       'plaquetas e fibrina formam um trombo estéril. Uma bacteremia coloniza '
       'esse trombo, e a vegetação cresce protegida dos neutrófilos, soltando '
       'bactérias no sangue o tempo todo: daí a bacteremia contínua. Os '
       'imunocomplexos explicam o fator reumatoide, o consumo de C3, a '
       'glomerulonefrite e o nódulo doloroso da polpa digital (nódulo de '
       'Osler); os microêmbolos explicam as máculas plantares (lesões de '
       'Janeway) e as petéquias conjuntivais.',
       'O curso subagudo, de semanas, é o dos estreptococos. Os dois '
       'antibióticos curtos baixaram a carga bacteriana a ponto de a febre '
       'ceder, sem esterilizar a vegetação. Calazar, linfoma e tuberculose permaneceram entre '
       'as hipóteses para febre com baço palpável em Sobral; o que reorganizou sua prioridade '
       'foi a hemocultura colhida antes de mais um antibiótico.'),

    bifurcacao('b1', 'Decisão', 'Terapia dirigida',
 'Qual antibiótico você mantém como tratamento dirigido desta infecção de valva nativa?', [
 caminho('Ceftriaxona endovenosa', 'tratamento', 'O agente é sensível a betalactâmico; ceftriaxona é opção de tratamento dirigido, com duração e seguimento adequados ao quadro. A equipe de endocardite acompanha a valva e as complicações.'),
 caminho('Amoxicilina oral', 'oral', 'A transição oral existe em pacientes selecionados e estabilizados após terapia endovenosa. Ela não equivale a iniciar este quadro complicado com amoxicilina oral isolada.'),
 caminho('Vancomicina endovenosa', 'vanco', 'Pode ter indicação em alergia grave ou outros contextos. Sem contraindicação a betalactâmico e com sensibilidade conhecida, não oferece vantagem como escolha dirigida e exige monitorar a exposição.')]),

    pg('oral', 'Dez dias depois',
       'Após a troca precoce do esquema endovenoso por amoxicilina oral e '
       'alta, Lúcia volta com febre de 38,6 °C e falta de ar ao deitar. As '
       'hemoculturas voltam a crescer //S. gallolyticus//. É internada para '
       'antibiótico endovenoso, com dez dias perdidos.',
       segue='tratamento'),

    pg('vanco', 'Revisão da prescrição',
 'A equipe inicia vancomicina e acompanha os níveis e a função renal. Na revisão com infectologia, confirma que Lúcia não tem alergia grave e que o estreptococo é sensível à penicilina. O esquema é trocado para ceftriaxona.',
 'A escolha do antibiótico é revista sem aguardar nova deterioração. A hematúria e a função renal continuam em seguimento; não se atribui automaticamente qualquer aumento da creatinina à vancomicina.', segue='tratamento'),

    pg('tratamento', 'Primeiros dias de terapia dirigida',
 'Lúcia recebe ceftriaxona 2 g endovenosa uma vez ao dia. A febre desaparece no quarto dia de terapia efetiva, e as hemoculturas de controle do terceiro dia não mostram crescimento. Ela volta a comer melhor e pede à filha que traga material de costura.',
 'O transesofágico inicial confirma vegetação mitral, sem abscesso perivalvar ou perfuração identificável naquele exame. A cirurgia cardíaca acompanha o caso. Culturas negativas documentam depuração, sem demonstrar recuperação mecânica do folheto.'),

    pg('piora', 'Sexto dia de terapia endovenosa efetiva, madrugada',
       'Lúcia acorda sufocada e não consegue deitar. Crepitações até o terço '
       'médio dos dois pulmões, saturação de 88% em ar ambiente, pressão de '
       '100/60 mmHg, frequência cardíaca de 124. O sopro mitral ficou mais curto '
       'e surgiu uma terceira bulha. O eletrocardiograma segue com PR de 180 ms. '
       'A radiografia é feita no leito.'),

    Q('p7', 5,
      'Qual mecanismo melhor explica a intercorrência do sexto dia?', [
      ('Disfunção mecânica mitral com insuficiência cardíaca aguda', True),
      ('Abscesso perivalvar como mecanismo mais sustentado pelo ECG', False),
      ('Falha microbiológica como explicação principal, apesar da depuração', False),
      ('Embolia pulmonar séptica da vegetação mitral', False),
      ('Glomerulonefrite isolada como explicação suficiente da descompensação', False),
    ], [('Dado decisivo', 'Regurgitação importante, novo quadro congestivo, terceira bulha e sopro que encurta favorecem piora mecânica valvar. Cultura negativa mostra controle sanguíneo, sem reparar tecido destruído; avaliação cirúrgica não deve esperar o fim do antibiótico.'), ('Concorrentes', 'PR estável não exclui abscesso, mas não fornece o sinal de extensão sugerido na alternativa. Vegetação esquerda emboliza usualmente para circulação sistêmica, não pulmonar. Não há dado de piora renal suficiente para atribuir o quadro apenas à retenção de volume. A urgência final depende da resposta ao suporte e da estabilidade.')]),

    estudo('rx_piora', 'Radiografia de tórax no leito',
           'Incidência anteroposterior, feita no leito na madrugada do sexto dia. '
           'Compare com a radiografia da admissão, que não tinha opacidades.',
           IMG / 'rx_edema.jpg',
           'Radiografia.',
           credito_meta(IMG / 'rx_edema.jpg.json'),
        [
         ((290, 540), (95, 440), '**Opacidades alveolares** confluentes no pulmão direito, a partir do hilo.', 12),
         ((740, 440), (905, 330), 'O mesmo padrão no **pulmão esquerdo**: a doença é bilateral.', -12),
         ((290, 210), (120, 120), '**Terço superior** relativamente poupado: o predomínio é central e inferior.', 12),
        ],
        ['Opacidades alveolares bilaterais, peri-hilares, que não existiam na '
         'admissão. Com a queda da saturação e as crepitações, é edema pulmonar.',
         'A instalação é aguda: a valva que passa a regurgitar de repente joga '
         'pressão num átrio esquerdo que não teve tempo de se dilatar.']),

    bifurcacao('b2', 'Decisão', 'A valva perfurada',
      'Na reavaliação urgente, o transesofágico mostra perfuração de folheto '
      'mitral e regurgitação importante, com edema pulmonar no sexto dia de '
      'terapia efetiva. Qual conduta você indica?', [
      caminho('Cirurgia cardíaca urgente',
              'cirurgia',
              'Insuficiência cardíaca por destruição valvar é a indicação '
              'clássica de cirurgia precoce.'),
      caminho('Adiar a cirurgia até o fim do antibiótico', 'espera',
              'A valva não vai se refazer com antibiótico, e o coração não '
              'aguenta quatro semanas de regurgitação aguda.'),
    ]),

    pg('espera', 'Nona noite',
       'Com furosemida e nitroglicerina, Lúcia melhora por dois dias. Na '
       'nona noite, entra em edema pulmonar de novo, agora com pressão de '
       '78/46 e lactato de 4,2 mmol/L. Vai para a UTI com noradrenalina.',
       segue='b3'),

    bifurcacao('b3', 'Decisão', 'Choque cardiogênico',
      'Qual a conduta?', [
      caminho('Cirurgia de emergência', 'cirurgia_tardia',
              'O risco cirúrgico subiu muito, mas sem cirurgia não há saída.'),
      caminho('Manter suporte clínico e esperar estabilizar para operar',
              'obito_pagina',
              'O suporte pode ser uma ponte, mas a disfunção mecânica mantém a necessidade de correção urgente; esta trajetória descreve uma possibilidade grave, não um prognóstico individual inevitável.'),
    ]),

    pg('obito_pagina', 'Décimo dia',
       'Com duas drogas vasoativas e ventilação mecânica, a pressão não se '
       'sustenta. Lúcia evolui com disfunção de múltiplos órgãos.',
       segue='f_obito'),

    pg('cirurgia_tardia', 'Cirurgia de emergência',
       'A troca valvar mitral por prótese biológica é feita no décimo dia, '
       'sob choque. O pós-operatório tem lesão renal com três sessões de '
       'diálise e onze dias de UTI.',
       segue='colono'),

    pg('cirurgia', 'Cirurgia no sétimo dia',
       'A cirurgia encontra perfuração de 6 mm no folheto anterior, sem '
       'abscesso. A equipe faz plástica mitral com remendo de pericárdio, '
       'preservando a valva nativa. A cultura da vegetação é negativa, e o '
       'antibiótico segue contando a partir da primeira hemocultura negativa.',
       segue='colono'),

    pg('colono', 'Terceira semana de antibiótico',
       'A colonoscopia encontra uma lesão séssil de 25 mm no cólon sigmoide, '
       'ressecada em peça única por mucosectomia. Não há outras lesões até o '
       'ceco.',
       'A peça vai para a anatomia patológica.'),

    estudo('histo', 'Anatomia patológica da lesão do sigmoide',
           'Peça da mucosectomia em hematoxilina-eosina, pequeno aumento. A '
           'pergunta é o tipo de lesão e o grau de displasia.',
           IMG / 'adenoma_histo.jpg',
           'Lâmina.',
           credito_meta(IMG / 'adenoma_histo.jpg.json'),
        [
         ((445, 75), (250, 30), '**Superfície com displasia de alto grau**: núcleos que perdem a polaridade.', 12),
         ((572, 305), (700, 250), '**Projeção vilosa**, em dedo de luva, revestida por epitélio displásico.', -12),
         ((755, 525), (880, 640), '**Glândulas tubulares** cortadas de través: o componente tubular.', 12),
        ],
        ['Adenoma tubuloviloso com displasia de alto grau na superfície e de '
         'baixo grau no restante, sem invasão da submucosa. Margens livres.',
         'Adenoma avançado pelos três critérios: 10 mm ou mais, componente '
         'viloso e displasia de alto grau. A anemia de seis meses antes e as '
         'fezes escuras vinham dele.']),

    Q('p8', 6,
      'Após a alta, em quais dois procedimentos você indica profilaxia de endocardite, segundo a AHA?', [
      ('Raspagem periodontal subgengival', True),
      ('Extração de dente permanente', True),
      ('Ajuste da prótese dentária removível sem lesão de mucosa', False),
      ('Radiografia odontológica intraoral', False),
      ('Colonoscopia de vigilância, mesmo com possível biópsia', False),
      ('Ecocardiograma transesofágico de controle', False),
    ], [('Procedimentos odontológicos', 'Endocardite prévia define alto risco qualquer que tenha sido a cirurgia. Raspagem subgengival e extração manipulam gengiva ou região periapical e justificam profilaxia. Ajuste de prótese sem lesão e radiografia intraoral não têm esse tipo de manipulação.'), ('Procedimentos não odontológicos', 'Pela AHA, colonoscopia, inclusive com biópsia, e transesofágico não recebem profilaxia apenas por esse antecedente quando não há infecção ativa. A associação do agente ao cólon justifica investigar e acompanhar a lesão, não acrescentar profilaxia à colonoscopia.')]),

    pg('alta', 'Preparando a alta',
       'Lúcia completa o antibiótico com culturas negativas. O '
       'ecocardiograma de controle mostra a valva funcionando.',
       conforme=('b2', ['alta_cedo', 'f2'])),

    pg('alta_cedo', 'Última semana',
       'Ela já sobe um lance de escada sem parar e voltou a costurar no '
       'quarto do hospital.',
       conforme=('b1', ['f1', 'f2', 'f1'])),

    fim('f1', 'Alta com a valva preservada',
        'Plástica mitral funcionando, sem regurgitação significativa, '
        'fração de ejeção preservada. Seguimento com a cardiologia, reposição '
        'de ferro e colonoscopia de vigilância em três anos.',
        'O antibiótico certo desde o início, a cirurgia no primeiro sinal de '
        'insuficiência cardíaca e o cólon investigado pelo agente: as três '
        'decisões contaram.', 'melhor'),

    fim('f2', 'Alta depois de um percurso mais longo',
        'Lúcia sai viva, com a infecção controlada, depois de uma internação '
        'mais longa. Neste percurso, o atraso no tratamento endovenoso ou na '
        'cirurgia exigiu estabilização e recuperação adicionais.',
        'O atraso teve consequências neste curso simulado. A necessidade de '
        'trocar ou reparar a valva depende da anatomia encontrada, e a piora '
        'renal exige avaliação própria; não é uma consequência obrigatória '
        'de qualquer escolha de antibiótico.', 'medio'),

    fim('f_obito', 'Óbito no décimo primeiro dia',
        'Lúcia morre em choque cardiogênico refratário, com a infecção já '
        'controlada pelo antibiótico.',
        'A insuficiência mitral aguda por perfuração valvar é indicação de '
        'cirurgia de urgência. Nesta trajetória, o atraso na correção da lesão que a '
        'cirurgia poderia corrigir acompanhou uma evolução fatal; o resultado é simulado e não prevê o de todo paciente.', 'pior'),

    pagina('retrospectiva', 'Pontos de ensino', '',
        pontos(
            'Febre que cede com antibiótico curto e volta pede hemoculturas '
            'colhidas sem antibiótico, antes do próximo; numa valvopata, antes '
            'de qualquer outro passo.',
            'Ferritina abaixo de 30 ng/mL confirma falta de ferro mesmo com '
            'inflamação. Depois da menopausa, falta de ferro é perda digestiva '
            'até prova em contrário e pede endoscopia alta e colonoscopia.',
            'Hematúria dismórfica com C3 baixo é glomerulonefrite por '
            'imunocomplexo; com FAN negativo e febre há semanas, a fonte mais '
            'comum é uma infecção persistente.',
            'Três de três hemoculturas positivas são bacteremia contínua, a '
            'marca de uma fonte intravascular. Cocos em cadeia são estreptococos '
            'ou enterococos.',
            '//Streptococcus gallolyticus// no sangue obriga a colonoscopia, '
            'mesmo sem sintoma intestinal.',
            'Insuficiência cardíaca por regurgitação valvar é a principal '
            'indicação de cirurgia precoce, sem esperar o fim do antibiótico.',
            'Depois do primeiro episódio, a paciente passa a ter indicação de '
            'profilaxia antes de procedimentos dentários que manipulam a '
            'gengiva.'),
        so_kicker=True),

    pg('referencias', 'Fontes e limites',
       'Paciente, valores e percursos são ficcionais. A cena de abertura é uma '
       'ilustração autoral gerada por inteligência artificial para este caso; '
       'não é fotografia nem documentação clínica.',
       'Fowler e cols. The 2023 Duke-ISCVID Criteria for Infective '
       'Endocarditis, Clin Infect Dis 2023. Delgado e cols. 2023 ESC Guidelines '
       'for the management of endocarditis, Eur Heart J 2023. Iversen e cols. '
       'POET, N Engl J Med 2019. Wilson e cols. Prevention of Viridans Group '
       'Streptococcal Infective Endocarditis, Circulation 2021. Snook e cols. '
       'British Society of Gastroenterology guidelines for the management of '
       'iron deficiency anaemia in adults, Gut 2021. Haidar e Singh. Fever of '
       'Unknown Origin, N Engl J Med 2022. Ministério da Saúde, Manual de '
       'Vigilância e Controle da Leishmaniose Visceral.',
       'Imagens, com setas adicionadas: radiografia de tórax normal, Mikael Häggström, Wikimedia Commons, CC0; ecocardiograma apical de quatro câmaras, CardioNetworks ECHOpedia (AMC Echolab), Wikimedia Commons, CC BY-SA 3.0, quadro extraído do vídeo E00405; hemorragias sob a unha, Splarka, Wikimedia Commons, domínio público, recortada (commons.wikimedia.org/wiki/File:Splinter_hemorrhage.jpg); máculas palmares, Warfieldian, Wikimedia Commons, CC BY-SA 4.0 (commons.wikimedia.org/wiki/File:Janeway_lesion.JPG); radiografia de tórax no leito, Jeremy Jones (Radiopaedia), Wikimedia Commons, CC BY-SA 3.0; micrografia de adenoma tubuloviloso, Mikael Häggström, Wikimedia Commons, CC0.'),
]

REVISAO = []

# Revisão das perguntas: fontes consultadas em 22/10/2026.
# https://www.nbme.org/sites/default/files/2021-02/NBME_Item%20Writing%20Guide_R_6.pdf
# https://www.escardio.org/guidelines/clinical-practice-guidelines/all-esc-practice-guidelines/endocarditis/
# https://doi.org/10.1136/gutjnl-2021-325210
# https://www.heart.org/--/media/files/health-topics/infective-endocarditis/infective-endocarditis-wallet-card.pdf

next(e for e in ETAPAS if e['k']=='referencias')['corpo'] += p('Revisão da evolução e do tempo dos exames: <a href="https://academic.oup.com/eurheartj/article/44/39/3948/7243107">ESC 2023 — endocardite</a>. A dor nova pode exigir investigação de embolia; ecocardiografia limitada não exclui infecção; melhora infecciosa não repara necessariamente destruição valvar. Os percursos são ficcionais.')

"""Abordagem sindrômica da linfonodomegalia, revisada em 23/10/2026.

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

    Q('p1', 1, 'Entre as alternativas, quais três hipóteses você prioriza inicialmente?',
 [('Mononucleose por EBV', True), ('Toxoplasmose', True), ('Linfoma', True),
  ('Linfadenite bacteriana supurativa', False), ('Metástase de carcinoma de orofaringe', False),
  ('Reação a medicamento', False)],
 [('Hipóteses selecionadas', 'EBV e toxoplasmose podem causar adenopatia cervical subaguda. A faringite inicial favorece EBV, mas não o confirma. Linfoma deve permanecer pela sudorese e perda de peso; dor e mobilidade não o excluem. Não é necessário escolher agora uma única causa.'),
  ('Menor apoio nesta apresentação', 'Não há coleção, rubor nem lesão dentária ou de orofaringe que sustentem supuração. A idade, o exame e a ausência de lesão mucosa tornam metástase menos provável. O linfonodo precedeu a amoxicilina, e não houve medicamento novo antes dos sintomas. Essas comparações organizam prioridades, sem exclusões absolutas.'),
  ('Investigação aberta', 'HIV, tuberculose e doenças autoimunes também podem entrar no diferencial. Os primeiros exames e a evolução decidirão o peso dessas possibilidades; esta seleção não é uma lista completa de causas.')]),

    painel('res1', 'Primeiros exames', 'Sangue', [
        ex('Hemoglobina / VCM', '11,7 g/dL / 86 fL', 'Hb 12–16 g/dL · VCM 80–100 fL', True),
        ex('Leucócitos', '2.900/mm³', '4.000–11.000/mm³', True),
        ex('Neutrófilos / linfócitos / monócitos', '1.450 / 1.100 / 260 por mm³',
           'N 1.800–7.500 · L 1.000–4.000', True),
        ex('Plaquetas', '188.000/mm³', '150.000–450.000/mm³'),
        ex('Proteína C reativa', '24 mg/L', 'até 5 mg/L', True),
    ], introducao='Colhidos na primeira consulta, no mesmo dia da '
                  'ultrassonografia do pescoço e da radiografia de tórax.'),

    painel('res1b', 'Primeiros exames', 'Bioquímica e urina', [
        ex('Creatinina', '0,7 mg/dL', '0,5–1,1 mg/dL'),
        ex('Urina tipo 1', 'Densidade 1.018 · sem proteína, hemácias ou leucócitos', 'normal'),
    ]),

    pg('reexame_inicial', 'Depois dos exames básicos',
 'Enquanto o hemograma fica disponível, Bianca continua com febre ao fim da tarde e desconforto para virar o pescoço. Permanece hidratada, sem dificuldade para engolir ou respirar. A equipe revê pele, articulações e focos locais, sem encontrar uma explicação nova.',
 'A anemia leve associada à leucopenia muda a pergunta: além da adenopatia, é preciso investigar as duas linhagens. O esfregaço, a LDH, as transaminases e a avaliação infecciosa e autoimune são acrescentados agora, na mesma etapa de atendimento; não se espera uma manifestação cutânea para justificar FAN e complemento.'),

    Q('p2', 2, 'Quais três exames melhor investigam causas distintas deste quadro agora?',
 [('FAN', True), ('HIV de quarta geração', True), ('EBV anti-VCA IgM', True),
  ('Anti-CCP', False), ('ANCA', False), ('PET-CT', False)],
 [('FAN', 'A anemia associada à leucopenia, febre e adenopatia justifica investigar autoimunidade desde agora, mesmo sem artrite ou lesão cutânea. C3 e C4, urina e função renal compõem a avaliação clínica; essa avaliação deve ocorrer em paralelo à investigação infecciosa.'),
  ('HIV e EBV', 'São causas possíveis de adenopatia com alterações hematológicas. O teste de HIV deve considerar a janela de exposição. No EBV, a IgM precisa ser interpretada com IgG e EBNA: um anticorpo positivo isolado não estabelece a causa da febre.'),
  ('Outras opções', 'Anti-CCP responde a uma suspeita de artrite reumatoide que não se apresenta aqui. ANCA tem maior valor diante de manifestações compatíveis com vasculite, ausentes até agora. PET-CT mostra atividade tanto em inflamação quanto em neoplasia e não define a causa do linfonodo. Toxoplasmose e CMV também podem justificar investigação dirigida.')]),

    pg('coleta_dirigida', 'Investigação',
 'A equipe colhe os exames selecionados. Acrescenta C3 e C4, sorologias para CMV e toxoplasmose e os marcadores complementares de EBV. Solicita revisão do esfregaço, LDH e transaminases. A anemia é investigada com reticulócitos, bilirrubinas, haptoglobina e Coombs direto; LDH isolada não demonstra hemólise.',
 'A ultrassonografia cervical e a radiografia de tórax, pedidas na primeira consulta, ficam disponíveis. Bianca continua com febre ao final do dia, mas não há instabilidade nem dificuldade para engolir.'),

    painel('complemento_hematologico', 'Exames dirigidos', 'Após as citopenias', [
        ex('Esfregaço', 'Linfócitos reativos ocasionais, 4% · sem blastos', '—'),
        ex('Desidrogenase láctica', '330 U/L', '120–250 U/L', True),
        ex('AST / ALT', '42 / 47 U/L', 'até 32 / 33 U/L', True),
    ], introducao='Primeiros resultados da complementação. Sorologias, FAN, complemento e marcadores da anemia seguem para conferência no retorno.'),

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
         'Neste corte, o eixo longo predomina sobre o curto e o hilo permanece visível.']),

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
         'Não há alargamento mediastinal ou hilar visível nesta radiografia.']),

    bifurcacao('b_inicial', 'Decisão', 'Continuação da investigação',
 'Os exames para investigar a causa ainda estão em processamento. Qual estratégia de imagem você escolhe?', [
 caminho('Tomografia de tórax', 'tc_precoce', 'Pode procurar adenopatias profundas não visíveis na radiografia. Forma oval, hilo preservado e fluxo hilar favorecem morfologia reacional, mas não excluem linfoma ou tuberculose. A utilidade da TC depende da evolução, da radiação e dos exames em andamento.'),
 caminho('Reavaliação clínica em uma semana', 'retorno_programado', 'Um retorno curto é possível em paciente estável, com investigação em andamento. A aparência reacional ao ultrassom e uma radiografia normal não excluem linfoma ou tuberculose. Crescimento, piora do estado geral ou sintomas compressivos antecipam a avaliação; observar não significa encerrar o caso.')]),

    pg('tc_precoce', 'Tomografia de tórax',
 'A tomografia não mostra linfonodos mediastinais ou hilares aumentados, lesões pulmonares ou derrame. O exame não identifica outra área para amostragem. Os linfonodos cervicais permanecem palpáveis e dolorosos.',
 'Bianca pergunta se isso afasta câncer. A ausência de alterações torácicas não exclui uma doença restrita ao pescoço. A equipe mantém a investigação da causa e o retorno combinado.', segue='hipotese'),

    pg('retorno_programado', 'Retorno combinado',
 'A equipe combina retorno em uma semana, conferência dos exames e reexame das cadeias linfonodais. Orienta Bianca a antecipar a consulta se houver piora importante, dificuldade para engolir ou respirar, sangramento ou aumento rápido do pescoço.',
 'Durante o intervalo, a febre persiste sem instabilidade. Não surge um foco dentário, cutâneo ou de orofaringe que explique a adenopatia.', segue='hipotese'),

    pg('hipotese', 'Entre as consultas',
 'No 15.º e no 16.º dia, Bianca acorda com menos cansaço, volta a comer melhor e não registra temperatura acima de 37,5 °C. Pensa que a amoxicilina finalmente fez efeito e cogita cancelar o retorno. O caroço, porém, continua do mesmo tamanho.',
 'Dois dias depois, a febre reaparece ao final da tarde. Ela volta a perder o apetite e precisa sair da escola antes do fim das aulas. O paracetamol reduz a temperatura, sem resolver a dor no pescoço.',
 'A equipe mantém o retorno e confere as coletas já realizadas. Bianca nega aumento do fluxo menstrual, outros sangramentos ou icterícia. Na revisão das exposições, não lembra de contato com tuberculose, leite não pasteurizado, arranhadura de gato ou lesão na pele antes do início dos sintomas.'),

    painel('res2', 'Retorno', 'Sorologias', [
        ex('EBV IgM (anti-VCA)', 'Não reagente', 'não reagente'),
        ex('EBV IgG (anti-VCA)', 'Reagente', '—', True),
        ex('EBV: marcador complementar (EBNA IgG)', 'Reagente', '—', True),
        ex('CMV: IgM / IgG', 'Não reagente / reagente', '—', True),
        ex('Toxoplasmose: IgM / IgG', 'Não reagente / não reagente', 'não reagente'),
        ex('HIV, teste de quarta geração', 'Não reagente', 'não reagente'),
    ], introducao='Coleta na segunda semana de febre; resultados revistos no retorno, no 19.º dia.'),

    painel('citopenias_iniciais', 'Investigação complementar', 'Autoimunidade e anemia', [
        ex('FAN por imunofluorescência em HEp-2', 'Não reagente na diluição de 1:80', 'não reagente'),
        ex('C3 / C4', '112 / 25 mg/dL', '90–180 / 10–40 mg/dL'),
        ex('Reticulócitos, contagem absoluta', '38.000/mm³', '25.000–100.000/mm³'),
        ex('Bilirrubina total / indireta', '0,6 / 0,4 mg/dL', 'até 1,2 / 0,9 mg/dL'),
        ex('Haptoglobina', '130 mg/dL', '30–200 mg/dL'),
        ex('Coombs direto', 'Negativo', 'negativo'),
    ], introducao='Colhidos na mesma etapa das sorologias, após o hemograma inicial.'),

    Q('sorologias_leitura', 1, 'Qual interpretação integra melhor os resultados para EBV?',
[('Infecção passada, sem evidência sorológica de infecção primária recente', True),
 ('Infecção primária em fase tardia, com IgM já desaparecida', False),
 ('Reativação como explicação mais provável para a febre atual', False),
 ('Fase inicial de infecção primária, antes do aparecimento de IgM', False)],
[('Dado decisivo',
  'VCA IgG e EBNA IgG reagentes, com VCA IgM não reagente, favorecem infecção passada. Nesta '
  'fase dos sintomas, não é coerente atribuir o EBNA já presente a essa nova infecção primária: ele '
  'costuma aparecer após meses. A coleta foi feita na segunda semana deste episódio.'),
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
       'Bianca deixou de dar aulas: sente cansaço ao final da manhã e come menos porque o pescoço incomoda ao mastigar. Não há dificuldade para engolir nem alteração da voz. A temperatura entre os picos é normal, e ela permanece hidratada, sem hipotensão.',
       'No reexame, não há linfonodos axilares ou inguinais, aumento do baço, lesões cutâneas ou sinovite. O comprometimento cervical agora é bilateral. Os dentes, a orofaringe e o couro cabeludo continuam sem lesões que expliquem os linfonodos.' ,
       'A prova tuberculínica solicitada na avaliação dirigida mede 14 mm. Bianca recebeu BCG na infância e não refere contato conhecido com tuberculose. A radiografia de tórax não mostrou alterações.'),

    pg('sintoma_novo', 'Quatro dias depois',
 'No 23.º dia de sintomas, Bianca entra em contato por dor nos dois punhos e nos joelhos. Pela manhã, sente o corpo preso durante cerca de 15 minutos; não percebe articulações inchadas. Não houve exercício intenso nem medicamento novo desde o fim da amoxicilina.',
 'No reexame, há dor à movimentação dos punhos, sem calor, derrame ou sinovite. O pescoço continua doloroso. Não há eritema no rosto, úlceras orais, lesões no tronco, dor pleurítica ou edema. A pressão permanece normal.',
 'O quadro já não se limita ao pescoço. A equipe retoma as hipóteses à luz dessa mudança, levando em conta que FAN e complemento já foram avaliados, mas não substituem a observação clínica.'),

    Q('p_probabilidade', 4, 'Quais três hipóteses você prioriza agora?',
 [('Linfoma', True), ('Linfadenite tuberculosa', True), ('Lúpus eritematoso sistêmico', True),
  ('Mononucleose primária por EBV', False), ('Linfadenite bacteriana supurativa', False),
  ('Reação medicamentosa', False)],
 [('Persistência e progressão', 'Linfoma e tuberculose ganglionar continuam relevantes pelo crescimento e pelos sintomas constitucionais. A prova tuberculínica não demonstra doença ativa, e linfonodo doloroso não exclui linfoma.'),
  ('Novo componente articular', 'Artralgias, febre e citopenias justificam rever LES. FAN não reagente, complemento preservado e urina normal reduzem o suporte atual, mas uma mudança clínica exige nova avaliação. As artralgias sem sinovite não confirmam doença autoimune.'),
  ('Demais hipóteses', 'O padrão sorológico enfraquece uma infecção primária recente por EBV. Não há coleção ou foco local que favoreça supuração. A febre e a adenopatia começaram antes da amoxicilina; uma reação ao fármaco poderia explicar sintomas superpostos, mas não integra bem a trajetória inteira. A seleção ordena por prioridade as opções apresentadas, sem excluir outras infecções ou causas inflamatórias.')]),

    pg('reavaliacao_articular', 'Reavaliação',
 'A equipe revê os exames colhidos: FAN não reagente, C3 e C4 preservados e ausência de sinais laboratoriais de hemólise. A urina e a creatinina continuam normais. Pelo novo componente articular, complementa a avaliação com anti-DNA nativo, que não é reagente.',
 'Três dias depois, as dores articulares desaparecem sem corticoide. A febre, porém, ainda aparece em alguns fins de tarde, e os linfonodos continuam aumentados. A melhora das articulações não esclarece a adenopatia nem explica as citopenias.',
 'A equipe mantém o seguimento clínico e a discussão da amostra do linfonodo. Não há motivo para considerar todas as hipóteses resolvidas pelos exames autoimunes negativos.'),

    pg('encaminhamento', 'Avaliação do linfonodo',
 'A equipe discute o caso com cirurgia e hematologia. Bianca mantém febre, perda de peso e crescimento cervical, sem diagnóstico nos exames iniciais. O linfonodo é superficial e acessível; não há contraindicação cirúrgica identificada.',
 'A prova tuberculínica não basta para iniciar tratamento de doença ativa. Antes da coleta, patologia e microbiologia combinam como receber o material, incluindo amostra adequada para pesquisa e cultura de micobactérias.'),

    Q('p_amostra', 5, 'Qual exame tem maior chance de esclarecer a causa nesta situação?',
 [('Biópsia excisional do linfonodo', True), ('Punção aspirativa por agulha fina', False),
  ('PET-CT', False), ('Biópsia de medula óssea', False), ('Ultrassom cervical de controle', False)],
 [('Excisão', 'O linfonodo é acessível e as hipóteses incluem doenças em que a arquitetura importa. A excisão permite estudar a distribuição da lesão e obter material para os exames complementares planejados. O benefício deve ser ponderado com os riscos do procedimento.'),
  ('Amostras e imagem', 'A punção pode ser útil para perguntas específicas, mas pode não classificar linfomas ou linfadenites. PET-CT não distingue inflamação de câncer. Novo ultrassom pode registrar a progressão, mas a progressão já está documentada. Medula pode ser indicada se surgir suspeita medular; neste contexto não substitui a avaliação do linfonodo.')]),

    bifurcacao('b_amostra', 'Decisão', 'Obtenção de tecido',
 'A excisão demorará dez dias. Há biópsia por agulha grossa disponível amanhã. Qual procedimento você programa?', [
 caminho('Biópsia excisional', 'aguarda_excisao', 'Com estabilidade e linfonodo acessível, pode-se aguardar um intervalo curto para preservar a arquitetura. Deve haver reavaliação se a evolução mudar.'),
 caminho('Biópsia por agulha grossa', 'fragmentos', 'Pode antecipar informação e ser diagnóstica. Se não responder à dúvida, a amostra parcial não deve ser interpretada como exclusão de doença; será necessário rever a estratégia.')]),

    pg('aguarda_excisao', 'Durante o agendamento',
 'Bianca mantém contato com a equipe enquanto aguarda a data da excisão. Não surgem sintomas compressivos ou instabilidade. Após a melhora das dores articulares, passa a ter dias inteiros sem febre e volta a almoçar normalmente.',
 'Os linfonodos, entretanto, permanecem bem palpáveis. A equipe programa reexame antes de decidir se o procedimento continua indicado.', segue='nova_evolucao'),

    pg('fragmentos', 'Resultado da biópsia por agulha',
       'Uma semana depois, os fragmentos mostram tecido linfoide com áreas de necrose. O patologista não encontra uma população maligna inequívoca, mas considera o material insuficiente para classificar a lesão e avaliar sua distribuição no linfonodo.',
       'Bianca ainda tem febre e dor no pescoço. O hemograma não mostra blastos, e as plaquetas continuam preservadas. O resultado parcial não explica o quadro.', segue='b_fragmentos'),

    bifurcacao('b_fragmentos', 'Decisão', 'Resultado parcial',
 'Qual procedimento acrescenta mais informação após essa amostra?', [
 caminho('Biópsia excisional', 'nova_evolucao', 'A limitação foi a distribuição e a arquitetura. Com linfonodo acessível, a excisão oferece uma chance maior de esclarecer a dúvida restante.'),
 caminho('Nova biópsia por agulha grossa', 'fragmentos_repetidos', 'Outra amostra pode ser considerada quando a excisão não é viável. Aqui permanece o risco de repetir a limitação arquitetural; a decisão precisa ser revista se o material continuar insuficiente.')]),

    pg('fragmentos_repetidos', 'Segunda amostra',
       'A nova biópsia também mostra fragmentos com necrose e tecido inflamatório, sem permitir uma conclusão. Os procedimentos não causaram complicações, mas a febre persiste e a investigação se prolonga.',
       'Na reunião com cirurgia e patologia, a equipe revê a necessidade de estudar o linfonodo inteiro. Bianca concorda com a retirada após discutir riscos e benefícios.', segue='nova_evolucao'),

    pg('nova_evolucao', 'Reexame antes da biópsia',
 'Bianca está há três dias sem febre. O apetite melhorou, as dores articulares não voltaram e ela pensa em retomar as aulas. Não iniciou corticoide nem outro tratamento específico.',
 'Ao exame, o maior linfonodo cervical continua com aproximadamente 3,7 cm, móvel e menos doloroso. Os contralaterais permanecem palpáveis. Não há sinovite, lesão cutânea ou aumento do baço. Hemoglobina: 11,5 g/dL; leucócitos: 2.600/mm³; plaquetas: 184.000/mm³.',
 'Ela pergunta se a melhora permite cancelar a biópsia. A febre e a capacidade funcional melhoraram antes dos linfonodos e do hemograma.'),

    bifurcacao('b_reavaliacao', 'Decisão', 'Após o reexame',
 'Como você ajusta o plano?', [
 caminho('Realizar a biópsia excisional programada', 'tecido2',
 'A melhora deve ser considerada, mas a adenopatia volumosa persistente e a investigação inconclusiva ainda justificam tecido. Nos percursos com amostra por agulha, sua insuficiência também pesa na decisão.'),
 caminho('Reavaliar clinicamente em sete dias', 'observacao_curta',
 'Uma observação curta requer decisão compartilhada, retorno garantido e critérios de antecipação. A melhora não confirma benignidade. Pela dimensão e pelo curso prévio, a amostra permanece uma opção importante.')]),

    pg('observacao_curta', 'Uma semana depois',
 'Bianca permanece melhor durante os primeiros dias e tenta voltar à escola. Na véspera do retorno, a febre reaparece, chegando a 38,7 °C, com sudorese noturna. O linfonodo não havia desaparecido; agora volta a doer. As articulações continuam sem sintomas.',
 'No reexame, o maior linfonodo mede aproximadamente 3,8 cm e permanece acessível. Ela está hidratada e sem sinais compressivos. O intervalo mostrou melhora clínica incompleta, seguida de recorrência; a equipe e Bianca retomam a excisão, sem presumir a causa.', segue='tecido2'),

    pg('tecido2', 'Amostra do linfonodo',
       'O cirurgião retira o linfonodo cervical mais representativo. A amostra é distribuída conforme o plano acordado: histologia e imuno-histoquímica, citometria de fluxo e investigação microbiológica.',
       'A citometria não identifica população clonal no material analisado; o TRM-TB não detecta micobactéria. Esses resultados, isoladamente, não excluem linfoma nem tuberculose ganglionar. O patologista precisa avaliar como as células estão organizadas no linfonodo e reunir esse dado à pesquisa de infecção. Se esses estudos não forem feitos no serviço, a peça será encaminhada a um laboratório de referência.'),

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
        ['Áreas de morte celular na região paracortical, com muitos fragmentos de núcleos (cariorrexe) e histiócitos, sem '
         'neutrófilos e sem granulomas.',
         'Não apresenta o padrão granulomatoso caseoso típico. Isso enfraquece, mas não exclui tuberculose; a conclusão depende da amostra completa e da microbiologia.']),

    Q('p5', 6, 'Quais duas informações ainda precisam ser integradas à histologia?',
 [('Imuno-histoquímica do linfonodo', True), ('Cultura de micobactérias do tecido', True),
  ('PET-CT', False), ('Nova sorologia para EBV', False), ('Biópsia de medula óssea', False)],
 [('Tecido', 'O painel imuno-histoquímico ajuda a caracterizar as células junto às áreas de necrose. A cultura mantém aberta a investigação de tuberculose: ausência de granulomas e testes negativos isolados não a excluem. Nenhum marcador imuno-histoquímico confirma sozinho a doença rara.'),
  ('Correlação clínica', 'A linfadenite do lúpus também pode ter necrose. FAN e complemento já foram investigados diante das citopenias; a amostra será correlacionada com essa avaliação e com pele, articulações e urina. Não se espera uma nova manifestação para começar a pensar em autoimunidade.'),
  ('Demais exames', 'PET-CT é inespecífico para essa distinção. Sem nova exposição ou mudança de cronologia, repetir EBV não resolve o padrão do tecido. A leucopenia segue em acompanhamento, mas sem sinais novos de doença medular a medula não substitui a integração do linfonodo retirado por cirurgia.')]),

    painel('res3', 'Complemento da biópsia', 'Tecido e autoanticorpos', [
        ex('Imuno-histoquímica', 'Histiócitos CD68 e mieloperoxidase positivos · '
           'células dendríticas plasmocitoides CD123 positivas · predomínio de '
           'linfócitos T CD8', '—', True),
        ex('Revisão morfológica e painel para linfoma', 'Sem células suspeitas de Hodgkin/Reed–Sternberg identificadas na amostra; painel integrado à morfologia, sem suporte para linfoma', '—'),
        ex('Pesquisa de bacilos da tuberculose no tecido (BAAR)', 'Negativa', 'negativa'),
        ex('Cultura de micobactérias e fungos', 'Em andamento', '—'),
    ], introducao='FAN e C3/C4 já haviam sido avaliados na investigação das citopenias. O anti-DNA, acrescentado após o aparecimento das artralgias, também não foi reagente. As culturas ainda estão em andamento.'),

    pg('diagnostico', 'Discussão anatomoclínica',
       'O hematopatologista integra o linfonodo retirado por cirurgia à evolução e conclui que o conjunto é compatível com doença de Kikuchi–Fujimoto, também chamada linfadenite necrosante histiocítica. A conclusão depende da amostra completa e de sua correlação com a avaliação clínica.',
       'O diagnóstico reúne três componentes: febre oscilante, linfonodos cervicais dolorosos e artralgias transitórias; leucopenia e investigação inicial sem causa definida; e necrose com fragmentos nucleares e histiócitos, sem padrão supurativo. Nenhum desses componentes clínicos é específico. A arquitetura e os estudos complementares do tecido dão sustentação ao diagnóstico.',
       'A investigação não sustenta infecção supurativa, linfoma ou linfadenite tuberculosa. As culturas ainda serão acompanhadas. FAN e anti-DNA não reagentes, complemento preservado e ausência de outros achados específicos reduzem o suporte a LES, sem representar exclusão definitiva.',
       'A conclusão é de alta compatibilidade anatomoclínica, não um diagnóstico por exclusão nem um marcador exclusivo. Ela orienta o acompanhamento enquanto as culturas terminam. Piora, progressão das citopenias ou manifestações novas exigem reavaliação.'),

    pagina('leitura_imuno', 'Discussão', 'Como interpretar a imuno-histoquímica',
    p('O patologista usa anticorpos para marcar proteínas nas células do tecido. Isso ajuda a reconhecer quais células participam da lesão. “Positivo” significa que a proteína foi identificada; não significa, por si só, câncer.'),
    tabela(['Marcador', 'O que ajuda a identificar', 'Significado nesta biópsia'], [
        ['CD68 e mieloperoxidase (MPO)', 'Histiócitos: macrófagos presentes no tecido', 'Destacam os histiócitos junto às áreas de necrose'],
        ['CD123', 'Células dendríticas plasmocitoides, que participam da resposta imune', 'Sua presença compõe o padrão inflamatório observado'],
        ['CD8', 'Uma população de linfócitos T', 'Mostra o predomínio de linfócitos T citotóxicos na lesão'],
    ]),
    p('O conjunto é compatível com Kikuchi quando acompanha a morfologia já discutida. Nenhum desses marcadores, isoladamente, confirma o diagnóstico ou exclui linfoma; pode haver sobreposição com linfadenite do lúpus. Para o clínico, o essencial é integrar o laudo à evolução, sem decorar os marcadores.'),
    p('MPO aqui é uma proteína marcada no tecido: não é o exame de sangue anti-MPO/ANCA. Referências: <a href="https://pubmed.ncbi.nlm.nih.gov/11549584/">estudo dos histiócitos CD68/MPO</a>; <a href="https://meridian.allenpress.com/aplm/article/147/7/767/488040/Clinicopathologic-Analysis-of-Kikuchi-Fujimoto">série clinicopatológica de 170 casos</a>.'), so_kicker=True),

    painel('res3b', 'No dia do laudo', 'Sangue', [
        ex('Hemoglobina', '11,4 g/dL', '12–16 g/dL', True),
        ex('Leucócitos / neutrófilos', '2.600 / 1.350 por mm³', 'L 4.000–11.000 · N 1.800–7.500', True),
        ex('Plaquetas', '176.000/mm³', '150.000–450.000/mm³'),
        ex('Ferritina', '480 ng/mL', '15–150 ng/mL', True),
        ex('Triglicerídeos, em jejum', '126 mg/dL', 'até 150 mg/dL'),
        ex('Fibrinogênio', '390 mg/dL', '200–400 mg/dL'),
    ], introducao='Controle do hemograma e da atividade inflamatória durante a investigação.'),

    pg('conduta', 'Tratamento e acompanhamento',
 'Bianca está estável, sem disfunção orgânica. A equipe revê a melhora parcial anterior: os sintomas oscilaram antes do diagnóstico, sem que isso esclarecesse a causa. Propõe hidratação, analgesia individualizada e controle clínico e do hemograma. Não há indicação de antibiótico adicional nem de corticoide de rotina nesta apresentação.',
 'Sintomas intensos ou persistentes, comprometimento extranodal ou complicações poderiam justificar tratamento imunomodulador após revisão das alternativas. A cultura deve ser acompanhada até o resultado final. Piora, novas citopenias ou aumento do baço exigem reavaliação, sem atribuir tudo automaticamente ao diagnóstico estabelecido.'),

    pg('tratamento', 'Quatro semanas após o plano de seguimento',
       'Bianca está afebril há oito dias. As dores articulares não retornaram. O maior linfonodo mede cerca de 1 cm à palpação e não dói. Hemoglobina: 12,1 g/dL; leucócitos: 4.300/mm³; PCR: 4 mg/L. Voltou a trabalhar meio período.',
       'A cultura do linfonodo continua em acompanhamento, ainda sem crescimento nesta revisão. A melhora clínica é coerente com o diagnóstico estabelecido, mas não substitui a conferência do resultado final.'),

    pg('alta', 'Oito semanas depois',
 'Bianca está sem febre, os linfonodos medem menos de 1 cm e ela retomou o trabalho integral. As culturas finais do linfonodo não mostraram crescimento após seis semanas de incubação.',
 'A melhora é coerente com um curso autolimitado. Não torna desnecessária a biópsia que foi indicada antes de conhecer a evolução. A equipe combina seguimento e explica a associação descrita com lúpus: manifestações novas precisam de avaliação, mas nem toda paciente desenvolverá LES.'),

    bifurcacao('extensao', 'Seguimento', 'Continuação opcional',
 'Deseja discutir um novo quadro no seguimento?', [
 caminho('Encerrar a discussão', 'retrospectiva', 'Revisão do raciocínio percorrido.'),
 caminho('Avaliar o retorno após seis meses', 'novo_quadro', 'Cenário didático adicional, não consequência das escolhas anteriores nem evolução obrigatória de Kikuchi.')]),

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
         'A distribuição e a relação com o sol apoiam a investigação de lúpus neste contexto. A aparência isolada não confirma LES: rosácea e outras dermatoses continuam no diferencial, com avaliação dermatológica quando necessário.']),

    painel('seguimento', 'Reavaliação', 'O que a equipe pediu', [
        ex('FAN', '1:640, padrão homogêneo', 'não reagente', True),
        ex('Anti-DNA nativo', 'Reagente', 'não reagente', True),
        ex('C3 / C4', '54 / 7 mg/dL', '90–180 / 10–40 mg/dL', True),
        ex('Hemograma', 'Hb 11,2 g/dL · leucócitos 3.100/mm³ · plaquetas 142.000/mm³', '—', True),
        ex('Creatinina', '0,9 mg/dL', '0,5–1,1 mg/dL'),
        ex('Sedimento urinário', '18 hemácias por campo, 30% dismórficas · sem cilindros', 'sem hemácias', True),
        ex('Relação proteína/creatinina urinária', '0,8 g/g', 'abaixo de 0,2 g/g', True),
    ], introducao='Exames colhidos neste retorno.'),

    pg('nova_doenca', 'Integração do novo quadro',
       'Sinovite, lesão cutânea fotossensível, FAN e anti-DNA positivos, complemento baixo e alterações urinárias sustentam forte suspeita de LES com acometimento renal. A equipe confirma a proteinúria e a hematúria e discute biópsia renal, apesar da creatinina normal. Proteinúria significativa persistente pode justificar a biópsia mesmo sem sedimento ativo; a hematúria reforça a suspeita nesta paciente.',
       'A biópsia demonstra nefrite lúpica classe III. A integração dos achados estabelece LES. Nefrologia e reumatologia planejam a indução e o seguimento; incluem hidroxicloroquina, salvo contraindicação, e avaliam bloqueio do sistema renina–angiotensina, com controle de pressão, potássio e função renal.',
       'O episódio inicial havia sido interpretado como compatível com Kikuchi. O surgimento de LES justifica rever a história e, se houver dúvida, o tecido original. Pode haver associação entre as doenças ou linfadenite relacionada ao lúpus; a evolução posterior não prova sozinha nem erro nem independência do primeiro diagnóstico.',
       segue='retrospectiva'),

    pagina('retrospectiva', 'Pontos de ensino', '',
      pontos(
        'Começar pela linfonodomegalia: distribuição, duração, exposições, sinais de alarme e possíveis infecções próximas aos linfonodos. Sintomas sistêmicos podem acompanhar adenopatia localizada.',
        'Dor, ultrassom de aspecto reacional e ausência de blastos não excluem neoplasia. Nenhum deles encerra o diferencial.',
        'Selecionar exames para uma pergunta. Sorologia de contato passado não explica automaticamente febre atual; prova tuberculínica não confirma doença ativa.',
        'Crescimento com sintomas persistentes mudou o limiar para biópsia. Planejar a amostra permite investigar infecção e neoplasia sem perder material.',
        'Anemia com leucopenia exige investigar as duas linhagens. Autoimunidade deve ser considerada desde essa etapa; LDH elevada isoladamente não prova hemólise. O diagnóstico raro exige integração, não uma lista de exclusões absolutas.',
        'Uma evolução discordante reabre o raciocínio. O diagnóstico anterior não deve impedir reconhecer uma doença nova.'),so_kicker=True),

    pg('referencias', 'Fontes e limites',
       'Paciente, valores e percursos são ficcionais. As oscilações clínicas e as escolhas de investigação são simuladas; não reproduzem uma sequência obrigatória da doença. A extensão de seguimento '
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
       '(commons.wikimedia.org/wiki/File:Lupusfoto.jpg).')
]

REVISAO = []

# Calibrated didactic overlay retained from the published image audit.
from .medida_us import sobreposicao as _medida_us
_us = next(e for e in ETAPAS if e['k'] == 'us_cervical')
_us['corpo'] = _us['corpo'].replace('</g></svg>', _medida_us() + '</g></svg>', 1)
_us['corpo'] = _us['corpo'].replace('A imagem não apresenta medidas assinaladas.',
 'Medida aproximada no corte: 3,5 × 1,1 cm, estimada pela escala de profundidade de 4 cm da imagem original. Cálipers e régua adicionados para ensino; não são medidas registradas no exame original.')
_us['corpo'] = _us['corpo'].replace('setas adicionadas', 'setas, cálipers e régua adicionados · estimativa didática')
for _n, _e in enumerate((e for e in ETAPAS if e['t'] == 'pergunta'), 1):
    _e['kicker'] = f'Pergunta {_n}'
next(e for e in ETAPAS if e['k'] == 'referencias')['corpo'] += p('Estrutura editorial estudada: <a href="https://www.nejm.org/doi/full/10.1056/NEJMimc1302497">An Unusual Case of Abdominal Pain, NEJM, 2013</a>. Referência de narrativa e perguntas; nenhuma imagem, texto de paciente ou recomendação de 2013 foi reproduzida. Revisão clínica: <a href="https://www.cdc.gov/epstein-barr/php/laboratories/index.html">CDC — EBV</a>; <a href="https://arupconsult.com/content/systemic-lupus-erythematosus">ARUP — LES</a>; <a href="https://www.nice.org.uk/guidance/ng52/chapter/Recommendations">NICE NG52 — amostragem</a>.')

next(e for e in ETAPAS if e['k'] == 'referencias')['corpo'] += p('Evolução clínica ficcional informada pela variedade de manifestações descrita em <a href="https://pubmed.ncbi.nlm.nih.gov/25500707/">Dumas et al., 2014, série de 91 casos</a>. A série sustenta a possibilidade de artralgias e de evolução autolimitada, não uma cronologia diária individual.')

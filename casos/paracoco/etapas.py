"""Caso ficcional reformulado em 23/10/2026: evolução clínica antes da resolução.

Imagens, créditos e marcações preservados. Fontes e limites no fechamento.
"""
import json
from pathlib import Path

from motor.estudo_imagem import estudo
from motor.etapas import (alt, bifurcacao, caminho, capa, desfecho, op, p,
                          pagina, painel, par, pareamento, pergunta, pontos,
                          topicos, vitais)

TITULO = 'A ferida do lábio'
RODAPE = 'Paciente ficcional · evoluções simuladas para ensino'
COR = '#a16207'
IMG = Path(__file__).parent / 'img'
BANCO = []
MOLDE = 'nejm'
CENA = 'cena-paciente.png'


def credito_meta(meta):
    m = json.loads(Path(meta).read_text())
    return m['autor'] + ' · Wikimedia Commons · ' + m['licenca'] + ' · setas adicionadas'


def pg(k, titulo, *textos, segue='', conforme=None):
    return pagina(k, titulo, '', *(p(t) for t in textos), so_kicker=True,
                  segue=segue, conforme=conforme)


def disc(k, titulo, *textos):
    return pagina(k, 'Discussão', titulo, *(p(t) for t in textos))


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
    capa(TITULO, fundo=CENA, kicker='Caso interativo',
         selo='Paciente ficcional · procedência e créditos na última tela'),

    pg('historia', 'Apresentação',
       'Valdir, lavrador de 52 anos, é encaminhado pela unidade básica de '
       'Cacoal, em Rondônia, ao ambulatório de clínica médica do hospital '
       'regional. Tosse há quatro meses e perdeu o fôlego para subir o morro '
       'do cafezal. Pesava 70 kg; hoje pesa 61.',
       'Há três meses apareceu uma ferida no lábio inferior que dói para '
       'comer e não fecha, e há dois meses a voz ficou rouca. A tosse tem '
       'pouco catarro claro.',
       'Na unidade básica recebeu amoxicilina por sete dias e nistatina para '
       'a boca, sem mudança. Duas baciloscopias de escarro foram negativas, e '
       'o teste rápido molecular para tuberculose no escarro não detectou o '
       'bacilo. Nega febre medida, suor noturno, sangue no catarro, dor no '
       'peito, dificuldade para engolir e diarreia.'),

    pagina('ficha', 'Ficha do paciente', '',
           topicos(('Antecedentes', 'Hipertensão diagnosticada há três anos na '
                    'unidade básica. Uma pneumonia aos 40 anos, tratada em casa. '
                    'Nunca fez endoscopia nem exame de pulmão.'),
                   ('Medicações', 'Hidroclorotiazida 25 mg ao dia, quando lembra. '
                    'Omeprazol 20 mg comprado na farmácia, quase todo dia, para '
                    'queimação. Dipirona para a dor da boca.'),
                   ('Hábitos', 'Fuma desde os 12 anos, um maço por dia, hoje mais '
                    'cigarro de palha: cerca de 40 maços-ano. Três a quatro doses '
                    'de cachaça por dia, mais no fim de semana.'),
                   ('Trabalho e moradia', 'Nasceu no norte do Paraná e trabalha na '
                    'roça de café desde os 9 anos. Aos 24 veio para Rondônia, '
                    'onde ajudou a derrubar mata para abrir o sítio. Hoje planta '
                    'café e mandioca e colhe e abana o café à mão. Na colheita, '
                    'o alojamento do sítio recebe trabalhadores de fora.'),
                   ('Família', 'Pai morreu aos 61 anos de "câncer na garganta"; '
                    'fumava. Mãe viva, diabética. Um colega do alojamento tratou '
                    'tuberculose há dois anos.')),
           so_kicker=True),

    pagina('exame', 'Exame físico', '',
           vitais(('Temperatura', '37,4 °C', False),
                  ('Pressão arterial', '112/70', False),
                  ('Frequência cardíaca', '94', False),
                  ('Frequência respiratória', '22', True),
                  ('SpO₂ em ar ambiente', '93%', True),
                  ('Peso', '61 kg', True)),
           topicos(('Estado geral', 'Emagrecido, descorado, voz rouca e soprosa. '
                    'Altura de 1,70 m.'),
                   ('Boca e face', 'No lábio inferior, à esquerda, lesão de 1,5 cm, '
                    'endurecida, de superfície granulosa com pontos vermelho-escuros '
                    'e crosta central. Duas lesões menores, de 5 a 8 mm, no sulco '
                    'nasolabial direito e no mento. Na gengiva inferior, área '
                    'granulosa que sangra ao toque. Dentes em mau estado.'),
                   ('Linfonodos', 'Submandibulares e cervicais anteriores dos dois '
                    'lados, de 1 a 2 cm, endurecidos, pouco dolorosos, móveis, sem '
                    'fístula.'),
                   ('Pulmões', 'Murmúrio diminuído. Estertores finos nas regiões '
                    'infraescapulares e entre as escápulas, dos dois lados.'),
                   ('Coração e abdome', 'Ritmo regular, sem sopros. Fígado no '
                    'rebordo, baço não palpável.'),
                   ('Pele', 'Queimada de sol no rosto, no pescoço e nos antebraços. '
                    'As dobras das palmas são mais escuras que o resto da mão.')),
           so_kicker=True),

    painel('res1', 'Primeiros exames', 'Sangue', [
        ex('Hemoglobina / hematócrito', '11,6 g/dL / 35% · VCM 86 fL', 'Hb 13,5–17,5 g/dL', True),
        ex('Leucócitos', '9.400/mm³ · neutrófilos 68% · eosinófilos 6% {{(564/mm³)}}', '4.000–11.000 · eos até 500', True),
        ex('Plaquetas', '412.000/mm³', '150.000–450.000/mm³'),
        ex('Proteína C reativa', '38 mg/L', 'até 5 mg/L', True),
        ex('Sódio / potássio', '133 / 5,0 mmol/L', '135–145 / 3,5–5,1', True),
        ex('Ureia / creatinina', '30 / 0,9 mg/dL {{(TFG 103, CKD-EPI 2021)}}', 'até 42 / 0,7–1,3'),
        ex('Glicemia de jejum', '84 mg/dL', '70–99 mg/dL'),
    ], introducao='Colhidos na primeira consulta, com a nova amostra de escarro '
                  'para cultura de micobactérias.'),

    painel('res1b', 'Primeiros exames', 'Urina', [
        ex('Urina', 'Sem alterações', '—'),
    ]),

    pg('reavaliacao_basica', 'Reavaliação após a rotina',
 'Valdir continua precisando parar ao atravessar o corredor, e a oximetria repetida em repouso permanece em 93%. A equipe revê os estertores e a perda de peso; a anemia leve, sozinha, não explica toda a limitação. Não há instabilidade ou estridor.',
 'A dispneia com saturação reduzida justifica gasometria e radiografia na mesma avaliação. Pela associação de doença respiratória crônica, emagrecimento e lesões mucosas, solicita-se HIV. Proteínas séricas e enzimas hepáticas complementam a avaliação nutricional e sistêmica. A investigação de micobactérias já começou na unidade básica e continua em paralelo.'),

    painel('avaliacao_dirigida', 'Exames dirigidos', 'Respiração e doença sistêmica', [
        ex('Gasometria arterial em ar ambiente', 'pH 7,45 · pCO₂ 33 · pO₂ 64 mmHg · HCO₃ 22,5 · SatO₂ 93%', '—', True),
        ex('Teste rápido para HIV', 'Não reagente', 'não reagente'),
        ex('Proteínas totais / albumina', '7,9 / 3,1 g/dL {{(globulinas 4,8)}}', '6,0–8,0 / 3,5–5,0', True),
        ex('AST / ALT / fosfatase alcalina', '28 / 22 / 96 U/L', 'até 40 / 41 / 129'),
    ], introducao='Complementação pedida após o reexame, ainda na primeira avaliação; sem aguardar progressão da dispneia.'),

    Q('p1', 1,
      'Qual conclusão a gasometria permite antes de atribuir a hipoxemia a uma doença específica?', [
      ('Há defeito de troca gasosa; a gasometria isolada não separa V/Q, difusão e shunt', True),
      ('Hipoventilação isolada explica pO₂ de 64 com pCO₂ de 33', False),
      ('A anemia de 11,6 g/dL explica a redução da pO₂', False),
      ('O gradiente alvéolo-arterial é normal para a idade', False),
      ('A pCO₂ baixa demonstra causa exclusivamente extrapulmonar', False),
     ], [
      ('O limite do cálculo', 'Em ar ambiente e baixa altitude, PAO₂ estimada em 109 mmHg e PaO₂ de 64 dão gradiente de cerca de 45, acima do esperado para 52 anos. Estertores e doença respiratória crônica favorecem processo pulmonar, mas o gradiente não identifica sozinho o mecanismo preciso.'),
      ('Comparação', 'Hipoventilação isolada elevaria a pCO₂. Anemia reduz conteúdo de oxigênio, sem necessariamente baixar sua pressão arterial. pCO₂ de 33 indica ventilação aumentada, compatível com compensação da doença pulmonar.'),
     ]),

    estudo('rx_adm', 'Radiografia de tórax',
           'Radiografia em incidência posteroanterior, feita na primeira '
           'consulta. Antes de abrir os achados, compare a extensão da imagem '
           'com a saturação de 93% e os estertores discretos.',
           IMG / 'rx_torax.jpg',
           'Radiografia de outro paciente · comparação didática.',
           credito_meta(IMG / 'rx_torax.jpg.json'),
        [
         ((300, 650), (90, 560), '**Linhas finas e pequenos nódulos** que se somam junto ao hilo '
          'direito, no terço inferior.', 12),
         ((849, 700), (935, 560), 'O mesmo desenho no **pulmão esquerdo**, em espelho.', -12),
         ((349, 131), (150, 80), '**Ápice direito** com transparência preservada.', 12),
        ],
        ['Opacidades reticulares e micronodulares nos dois pulmões, simétricas, '
         'mais densas junto aos hilos e nos terços médio e inferior; ápices '
         'relativamente preservados.',
         'Sem cavidade evidente, sem derrame pleural, área cardíaca normal.']),

    pg('alivio_parcial', 'Primeiro dia: volta a comer, mas não a trabalhar',
 'Com analgesia e alimentação macia, Valdir consegue terminar uma refeição. A ferida continua endurecida e sangra ao escovar os dentes. Ao atravessar o corredor, precisa parar para recuperar o fôlego; a melhora da boca não recuperou sua capacidade de esforço.',
 'Na revisão do atendimento anterior, conta que a nistatina não mudou a lesão. A equipe organiza avaliação em hospital-dia, orientação nutricional e vigilância respiratória, sem atribuir todos os sintomas à dor ao comer. A hidroclorotiazida é suspensa diante do sódio baixo e da pressão sem elevação.'),

    Q('p2', 2, 'Quais dois exames para investigar a causa você prioriza com escarro disponível e lesão oral acessível?',
 [('Exame micológico direto do escarro', True), ('Biópsia da lesão oral', True), ('Lavado broncoalveolar', False), ('Biópsia laríngea sob anestesia geral', False), ('Tomografia de tórax', False)],
 [('Amostras', 'Exame direto pode identificar fungos; a biópsia oral discrimina infecção e neoplasia e permite pesquisa microbiológica. A cultura de micobactérias já está em curso. Patologia e laboratório combinam a distribuição e o transporte antes da coleta.'),
 ('Prioridade relativa', 'Lavado ou tecido laríngeo podem ser necessários se houver discordância ou amostras insuficientes. A lesão oral oferece acesso menos complexo agora. TC caracteriza extensão, mas não substitui identificação do agente. Os exames indicados serão feitos mesmo que a seleção do aluno seja incompleta.')]),

    estudo('lesoes', 'As lesões do rosto',
           'Fotografia de outro paciente, com lesões do mesmo tipo das de '
           'Valdir, porém mais numerosas. A lesão do lábio dele, as duas da face '
           'e a área da gengiva têm essa mesma superfície.',
           IMG / 'lesoes_periorais.jpg',
           'Fotografia de outro paciente · recortada na região da boca.',
           credito_meta(IMG / 'lesoes_periorais.jpg.json'),
        [
         ((370, 260), (230, 110), '**Fundo granuloso**, salpicado de pontos vermelho-escuros e '
          'amarelados.', 12),
         ((712, 290), (875, 385), '**Centro ulcerado com crosta escura**, cercado por borda '
          'elevada e violácea.', -12),
         ((560, 565), (390, 640), 'Lesão na **junção do lábio com a pele**, com o mesmo fundo.', 12),
        ],
        ['Pápulas e placas infiltradas, de borda elevada e violácea, com centro '
         'ulcerado de fundo granuloso, pontilhado de vermelho-escuro, e crostas.',
         'No caso de Valdir: uma lesão de 1,5 cm no lábio, duas menores na face '
         'e uma área granulosa na gengiva, todas com meses de evolução.']),

    Q('p3', 3, 'Quais duas hipóteses merecem investigação prioritária entre estas alternativas?',
 [('Micose sistêmica endêmica', True), ('Carcinoma epidermoide de via aerodigestiva', True), ('Candidíase oral isolada', False), ('Doença pulmonar obstrutiva como explicação única', False), ('Aftose recorrente isolada', False)],
 [('Integração e concorrência', 'A exposição rural, a doença pulmonar e as múltiplas lesões granulosas favorecem micose sistêmica. Fumo, álcool e lesão endurecida impõem investigar carcinoma, inclusive doença coexistente. A amostra deve responder às duas perguntas.'),
 ('Limites', 'Tuberculose continua no diferencial e a cultura será acompanhada; não foi excluída por testes iniciais negativos. Candidíase, obstrução e aftas isoladas não integram o padrão pulmonar, os linfonodos e a lesão crônica infiltrada.')]),

    pg('mudanca_laringea', 'No dia seguinte: engolir também passa a doer',
 'Desde a noite anterior, Valdir sente dor ao engolir sólidos e a voz fica mais fraca. Continua engolindo líquidos e saliva, sem estridor ou esforço respiratório em repouso. É uma mudança em relação à ausência de disfagia na apresentação.',
 'A otorrinolaringologia o examina no mesmo dia: pregas vocais espessadas e granulosas, epiglote com lesões semelhantes, mobilidade preservada, sem massa obstrutiva. O resultado aproxima boca e laringe, sem excluir câncer. Dor progressiva, estridor ou incapacidade de ingerir líquidos exigiriam internação e proteção da via aérea.'),

    pg('ortostatismo', 'Ainda antes do resultado da biópsia',
 'Ao levantar após o exame, Valdir refere tontura. Deitado, pressão 110/70; em pé, 88/58, com reprodução do sintoma. Não há febre ou sangramento volumoso. Com hidratação supervisionada, a tontura diminui, mas a fraqueza persiste. Sódio 131 e potássio 5,2 mmol/L, creatinina 0,9.',
 'Baixa ingestão e tiazida podem contribuir, mas hiperpigmentação, perda de peso e alterações eletrolíticas exigem avaliar reserva adrenal agora. A investigação não pode esperar confirmar a micose. Não há choque ou vômitos; se surgissem, a hidrocortisona de emergência não aguardaria testes.'),

    Q('p_adrenal', 4, 'Qual exame inicial mais ajuda a avaliar a hipótese endócrina levantada pela evolução?',
 [('Cortisol sérico matinal', True), ('Tomografia das adrenais', False), ('Aldosterona isolada', False), ('TSH isolado', False)],
 [('Função antes de anatomia', 'Cortisol matinal é interpretado com ACTH, colhido junto, e com o contexto. Resultado indeterminado requer teste de estímulo se o paciente estiver estável. Imagem não mede reserva hormonal.'),
 ('Segurança', 'Não se deve retardar tratamento de crise adrenal para obter uma prova dinâmica. Neste paciente estável, é possível colher as amostras e realizar o teste sem adiar a reposição necessária.')]),

    painel('reserva_adrenal', 'Avaliação precoce', 'Antes do antifúngico', [
 ex('Cortisol às 8 h', '7,4 µg/dL', 'interpretação clínica; faixa basal do laboratório 5–25'),
 ex('ACTH', '112 pg/mL', 'até 46 pg/mL', True),
 ex('Cortisol 60 min após 250 µg de cosintropina', '11,8 µg/dL', 'resposta inadequada pelo método do laboratório', True),
 ex('Renina / aldosterona', 'Renina elevada e aldosterona inadequadamente baixa após suspensão da tiazida', 'interpretar com volume e medicamentos', True),
 ], introducao='Coletas realizadas antes da hidrocortisona. O serviço interpreta o pico pelo ensaio utilizado, sem aplicar um corte universal de 18 a qualquer método.'),

    pg('reposicao', 'Uma disfunção tratada, causa ainda em investigação',
 'A combinação de resposta inadequada ao estímulo e ACTH alto sustenta insuficiência adrenal primária. O teste de estímulo foi realizado no centro de referência. Se não houver acesso, a equipe usa cortisol da manhã e ACTH, discute a necessidade de confirmação com endocrinologia e não espera por esse teste para tratar uma possível crise. Inicia-se hidrocortisona oral em dose ajustada ao estresse da doença, com plano de redução para reposição fisiológica, usualmente 15–25 mg/dia fracionados. A endocrinologia acrescenta fludrocortisona 0,05 mg/dia pela deficiência mineralocorticoide, com controle de pressão, sódio e potássio.',
 'No dia seguinte, Valdir levanta sem tontura e volta a beber água com facilidade. As lesões, a rouquidão e a limitação respiratória continuam. A resposta à reposição não identifica a causa da adrenal; tuberculose e micose sistêmica permanecem em avaliação. Se houver deterioração, o local de cuidado será revisto.'),

    bifurcacao('b1', 'Decisão', 'Qual tecido primeiro?',
 'Amostras de escarro para micologia e micobactérias já foram enviadas. Há lesões acessíveis na gengiva e no lábio; qual local você escolhe para a primeira biópsia?', [
 caminho('Biópsia da borda da lesão labial', 'biopsia_labio', 'A borda ativa oferece material para agentes e avaliação epitelial, importante também pelo risco de carcinoma.'),
 caminho('Biópsia da lesão gengival', 'biopsia_gengiva', 'É uma alternativa acessível para histologia e microbiologia. Se a evolução do lábio permanecer discordante, ele precisará de amostra própria.')]),

    pg('biopsia_labio', 'Amostra do lábio',
 'Sob anestesia local, a borda ativa é amostrada em profundidade adequada. Fragmentos separados seguem para histologia e cultura, conforme orientação do laboratório. A gengiva e a laringe serão reavaliadas pela resposta; uma lesão persistente não será presumida como parte da mesma doença.', segue='biopsia'),

    pg('biopsia_gengiva', 'Amostra da gengiva',
 'A área granulosa gengival é amostrada para histologia e cultura. A equipe mantém avaliação do lábio endurecido: mesmo que a gengiva mostre infecção, persistência ou aspecto discordante do lábio exigirá biópsia específica. Não se agenda ressecção oncológica sem diagnóstico.', segue='biopsia'),

    pg('biopsia', 'Histologia e microbiologia',
 'O exame direto do escarro retorna com leveduras de parede espessa e brotamento múltiplo. O laboratório comunica imediatamente à equipe. Esse resultado já sustenta iniciar tratamento dirigido; não se espera a cultura terminar.',
 'No tecido, há hiperplasia pseudoepiteliomatosa sem atipia neoplásica identificada, granulomas e microabscessos com estruturas fúngicas. A coloração pela prata confirma o padrão do exame direto. A lesão escolhida foi diagnóstica; a resposta das demais será conferida.'),

    estudo('lamina', 'Coloração pela prata',
           'Lâmina de outro paciente, com o mesmo achado da biópsia de Valdir, '
           'em aumento maior. A prata (Grocott) cora de preto a parede dos '
           'fungos.',
           IMG / 'lamina_prata.jpg',
           'Lâmina de outro paciente · comparação didática.',
           credito_meta(IMG / 'lamina_prata.jpg.json'),
        [
         ((447, 470), (250, 600), '**Célula-mãe** grande, de parede espessa, com o centro '
          'claro.', 12),
         ((650, 475), (820, 400), '**Broto** pequeno preso à célula-mãe por uma base estreita; '
          'há vários em volta dela.', -12),
         ((321, 175), (150, 80), '**Células menores em cadeia**, também com brotos, de '
          'tamanhos diferentes.', 12),
        ],
        ['Leveduras de tamanho variado, de parede espessa, com vários brotos '
         'ao redor da mesma célula-mãe, como os raios de uma roda de leme.',
         'A morfologia é característica de Paracoccidioides spp. no contexto clínico; não identifica a espécie dentro do gênero.']),

    pg('virada', 'Integração diagnóstica',
 'Exame direto e histologia estabelecem paracoccidioidomicose crônica multifocal: pulmão, mucosas, pele e linfonodos. A insuficiência adrenal primária é compatível com acometimento associado, embora a causa adrenal não tenha sido comprovada por biópsia própria.',
 'Exposição ao solo e atividade rural sustentam a epidemiologia; a data da infecção não pode ser deduzida da lembrança de uma derrubada. A identificação morfológica não distingue as espécies. Sorologia pode ajudar a acompanhar, mas depende do antígeno e tem limitações, inclusive nas infecções por P. lutzii.',
 'O agente no tecido não exclui coinfecção por tuberculose nem carcinoma concomitante. A cultura respiratória para micobactérias segue em andamento e uma lesão residual ou discordante requer nova avaliação.'),

    painel('estadio', 'Referência para o seguimento', 'Sem adiar o tratamento', [
 ex('Imunodifusão para Paracoccidioides', 'Reagente, 1:8', 'método do laboratório de referência', True),
 ex('Espirometria pós-broncodilatador', 'VEF₁/CVF 0,63 · VEF₁ 61% do previsto · sem reversibilidade significativa', '—', True),
 ex('Sódio / potássio após reposição adrenal', '135 / 4,6 mmol/L', '135–145 / 3,5–5,1'),
 ex('Cultura para micobactérias', 'Em incubação', 'resultado final será conferido'),
 ], introducao='A investigação funcional e sorológica ocorre em paralelo à terapia. Dispneia não será atribuída apenas à micose num tabagista com obstrução.'),

    Q('p_tratamento', 5, 'Com ingestão oral preservada e estabilidade após reposição adrenal, qual antifúngico é a opção inicial mais apropriada neste percurso?',
 [('Itraconazol oral', True), ('Anfotericina B lipossomal', False), ('Fluconazol oral', False), ('Nistatina tópica', False)],
 [('Escolha contextual', 'Após avaliação especializada, a doença é conduzida como forma crônica sem instabilidade ou insuficiência respiratória grave, com absorção oral viável. Itraconazol é opção de primeira linha para formas leves a moderadas. A perda ponderal e a adrenal exigem monitorização próxima e não podem ser banalizadas por um rótulo.'),
 ('Alternativas', 'Anfotericina é apropriada para doença grave, deterioração ou impossibilidade de terapia oral; não é um erro absoluto nem necessariamente causa lesão renal. Nistatina não trata doença sistêmica e fluconazol não é a primeira escolha habitual. A classificação e o local de cuidado serão revistos se a evolução mudar.')]),

    pg('tratamento', 'Começar e conferir exposição',
 'Valdir inicia itraconazol em cápsulas convencionais, 200 mg/dia após refeição, com acompanhamento próximo de ingestão, peso, função hepática e interações. O omeprazol sem indicação clara é suspenso antes da primeira dose; não se espera falha terapêutica para reconhecer a interação.',
 'A duração será guiada pelos critérios de resposta e cura: a diretriz global de 2021 usa em geral 9–12 meses nas formas leves/moderadas; o consenso brasileiro admite 9–18 meses. Não se promete um prazo universal. Progressão ou má absorção pode exigir internação e terapia intravenosa.',
 'Ele recebe orientação sobre doses de estresse da hidrocortisona, cartão de alerta e reposição parenteral se não conseguir reter comprimidos. Tratamento antifúngico não autoriza interromper a reposição adrenal por conta própria.'),

    Q('p6', 6, 'Se a cultura posteriormente confirmar tuberculose e houver indicação de rifampicina, qual ação é mais apropriada?',
 [('Reorganizar o esquema antifúngico', True), ('Separar as doses por duas horas', False), ('Dobrar empiricamente o itraconazol', False), ('Manter o esquema sem revisão', False)],
 [('Interação', 'A indução enzimática pela rifampicina reduz muito a exposição ao itraconazol. A equipe precisa escolher estratégia antifúngica alternativa, conforme gravidade e função renal. Não se corrige essa interação apenas com horário ou aumento empírico. Também é necessário rever a reposição adrenal: rifampicina acelera a depuração de glicocorticoides e pode exigir ajuste da hidrocortisona.'),
 ('Outra interação', 'Supressores de acidez reduzem absorção das cápsulas convencionais e devem ser revistos; outras formulações têm instruções distintas. As culturas serão acompanhadas mesmo após a confirmação da micose.')]),

    pg('seguimento', 'Do primeiro ao sexto mês',
 'Em 30 dias as lesões labial, gengival e da face cicatrizam, sem área endurecida residual. A cultura fúngica confirma Paracoccidioides spp.; a de micobactérias termina sem crescimento em oito semanas. A laringoscopia de controle mostra regressão das lesões, com disfonia residual.',
 'Valdir deixa de fumar no segundo mês com apoio da unidade básica. No sexto, pesa 68 kg e a imunodifusão caiu para 1:2, mas ainda para ao subir o morro. A equipe revê a obstrução e a possibilidade de sequela pulmonar, em vez de supor atividade fúngica só pela dispneia.',
 'A cicatrização da boca foi mais rápida que a recuperação de peso, função respiratória e voz. O antifúngico continua; não há uma decisão de suspensão precoce usada para produzir uma recaída obrigatória.'),

    pg('cura', 'Do 12.º ao 18.º mês',
 'No 12.º mês, a avaliação ainda não satisfaz todos os critérios de suspensão, e o tratamento é prolongado. No 18.º, peso estável em 70 kg, ausência de lesões novas, sorologia não reagente e radiografias estáveis em avaliações sucessivas sustentam a suspensão supervisionada.',
 'A reserva adrenal continua reduzida e a reposição é mantida. A dispneia residual motiva TC e tratamento funcional, sem prolongar antifúngico automaticamente por uma cicatriz ou pelo tabagismo prévio.'),

    estudo('tc_seq', 'Tomografia de tórax no fim do tratamento',
           'Corte axial nos lobos superiores, em janela de pulmão. A pergunta é '
           'como interpretar alterações residuais junto da evolução clínica e funcional; a TC isolada não confirma cura nem atividade.',
           IMG / 'tc_controle.jpg',
           'Tomografia de outro paciente · comparação didática.',
           credito_meta(IMG / 'tc_controle.jpg.json'),
        [
         ((246, 399), (110, 610), 'Parênquima salpicado de **pequenas áreas escuras, sem '
          'parede**, em todo o lobo: enfisema centrolobular.', 12),
         ((313, 268), (150, 150), '**Ponto branco**: ramo da artéria pulmonar cortado de través.', -12),
         ((786, 469), (900, 300), '**Pulmão esquerdo** com o mesmo padrão difuso, sem nódulo nem '
          'consolidação.', 12),
        ],
        ['Enfisema centrolobular difuso nos lobos superiores. Sem nódulos, '
         'cavidades, consolidação ou vidro fosco neste corte.',
         'A imagem de referência mostra enfisema. No caso, o laudo completo é integrado à obstrução e à estabilidade clínica para orientar broncodilatador e reabilitação; uma única fatia não exclui atividade em outro local.']),

    desfecho('alta', 'Depois do antifúngico',
 p('Valdir segue em consultas semestrais por pelo menos dois anos após a suspensão, com avaliação clínica, sorológica e radiológica conforme evolução. Mantém broncodilatador, reabilitação e acompanhamento endócrino.'),
 p('Dois anos depois, sem recaída documentada, sobe o morro com uma pausa e a voz continua mais grave. Há controle da infecção com sequelas; não se afirma que cada atraso causaria fibrose nem que a cura esteriliza todos os focos.'),
 qualidade='medio', porque='A infecção foi controlada neste percurso, mas a recuperação funcional e o cuidado das sequelas continuam.', fecho='retrospectiva'),

    pagina('retrospectiva', 'Pontos de ensino', '', pontos(
 'Pulmão, boca e laringe exigem integrar micose, tuberculose e neoplasia; uma hipótese pode não explicar todos os sítios.',
 'Melhorar a alimentação não recupera automaticamente a troca gasosa. Odinófagia nova exige examinar a via aérea.',
 'Hiperpigmentação, ortostatismo e alterações eletrolíticas motivam avaliar a adrenal antes da confirmação da causa.',
 'Amostra acessível e exame direto podem antecipar o diagnóstico. Cultura pendente não deve adiar tratamento quando há agente demonstrado.',
 'A resposta das lesões, da voz, do peso e da função pulmonar ocorre em ritmos diferentes. Interações e critérios de suspensão precisam de acompanhamento.'), so_kicker=True),

    pg('referencias', 'Fontes e limites',
       'Paciente, valores e percursos são ficcionais.',
       'Shikanai-Yasuda e cols. II Consenso Brasileiro em Paracoccidioidomicose '
       '2017, Epidemiol Serv Saúde 2018;27(núm. esp.):e0500001 (versão em '
       'inglês: Brazilian guidelines for the clinical management of '
       'paracoccidioidomycosis, Rev Soc Bras Med Trop 2017;50:715–40): formas '
       'clínicas, critérios de gravidade, doses, interações, seguimento, '
       'critérios de cura, adrenal e sequelas. Bornstein e cols. Diagnosis and '
       'Treatment of Primary Adrenal Insufficiency, Endocrine Society, J Clin '
       'Endocrinol Metab 2016. Ministério da Saúde. Manual de Recomendações '
       'para o Controle da Tuberculose no Brasil, 2.ª ed., 2019. Inker e cols. '
       'CKD-EPI 2021, N Engl J Med 2021.',
       'Capa: ilustração original do paciente ficcional, gerada com OpenAI '
       'imagegen para este projeto em 24/10/2026. Imagens clínicas de outros '
       'pacientes, com setas adicionadas. Radiografia: CDC/M. Renz, domínio '
       'público, commons.wikimedia.org/wiki/'
       'File:Chest_X-ray_acute_pulmonary_histoplasmosis_PHIL_3954.jpg (usada '
       'pelo padrão intersticial). Lesões da face: CDC/Dr. Martins Castro e Dr. '
       'Lucille K. Georg, domínio público, recortada na região da boca, '
       'commons.wikimedia.org/wiki/File:Paracoccidioidomycosis_lesions.png. '
       'Prata: CDC/Dr. Lucille K. Georg, domínio público, '
       'commons.wikimedia.org/wiki/File:Paracoccidioides_brasiliensis_01.jpg. '
       'Tomografia: Hellerhoff, CC BY-SA 4.0, commons.wikimedia.org/wiki/'
       'File:Zentrilobulaeres_Lungenemphysem_61W_-_CT_axial_-_001.jpg.',
 'Revisão de 23/10/2026: <a href="https://pubmed.ncbi.nlm.nih.gov/34364529/">ECMM/ISHAM 2021, micoses endêmicas</a>; <a href="https://pubmed.ncbi.nlm.nih.gov/30133688/">consenso brasileiro publicado em 2018</a>; <a href="https://www.endocrine.org/clinical-practice-guidelines/primary-adrenal-insufficiency">Endocrine Society, diretriz de insuficiência adrenal primária de 2016</a>. A data de cada documento é explícita; a cronologia individual é ficcional. Não se pretende demonstrar uma nova diretriz de 2026.')
]

REVISAO = []

for _n, _e in enumerate((e for e in ETAPAS if e['t'] == 'pergunta'), 1):
    _e['kicker'] = f'Pergunta {_n}'

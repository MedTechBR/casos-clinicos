"""Adaptação autoral de relatos de pseudo-obstrução intestinal no lúpus.
Marina, resultados, cronologia e ramificações são ficcionais para ensino.
"""
from pathlib import Path
from casos.apoio import pg, Q, ex, fim, vitais
from motor.etapas import capa, pagina, painel, p, topicos, bifurcacao, caminho, pontos
from motor.estudo_imagem import estudo
TITULO='Entre uma refeição e outra'
RODAPE='Paciente ficcional · evolução simulada para ensino'
COR='#0f766e'
IMG=Path(__file__).parent/'img'
BANCO=[]
MOLDE='nejm'

ETAPAS=[
 capa(TITULO,fundo='cena.png',kicker='Caso interativo',selo='Paciente ficcional · fontes na última tela'),
 pg('historia','Apresentação',
 'Marina, auxiliar administrativa de 34 anos, chega à emergência por distensão abdominal e vômitos. Há cinco semanas sente cólicas depois das refeições. Nos primeiros dias evacuava a cada dois ou três dias; há quatro dias não evacua e, desde ontem, não elimina gases. Nas últimas 24 horas vomitou quatro vezes, mesmo depois de beber água.',
 'Perdeu 4 kg porque passou a comer menos. Teve temperatura de até 37,8 °C em algumas tardes. Numa unidade de pronto atendimento recebeu escopolamina e orientação para tratar constipação; a dor melhorava por algumas horas, mas o abdome continuava aumentando.',
 'Nega diarreia, sangue nas fezes, disúria ou sangramento genital. A última menstruação ocorreu há duas semanas. Não relata lesões na pele, dor nas articulações ou feridas na boca.'),
 pagina('antecedentes','Antecedentes','',topicos(
 ('Patológicos','Apendicectomia aos 18 anos, sem complicações. Nenhuma doença crônica conhecida; duas gestações sem intercorrências.'),
 ('Medicamentos','Sulfato ferroso há um mês, prescrito por cansaço e anemia leve. Escopolamina por quatro dias; dipirona ocasional. Não usa opioides, imunossupressores ou suplementos para emagrecer.'),
 ('Hábitos e exposições','Não fuma; álcool esporádico. Não viajou, não teve contato conhecido com tuberculose e não usa drogas. Trabalha sentada e mantém alimentação habitual com carne e vegetais.'),
 ('Família','Mãe com hipotireoidismo. Sem câncer intestinal ou doença inflamatória intestinal conhecidos na família.')),so_kicker=True),
 pagina('exame','Exame físico','',vitais(('Temperatura','37,6 °C'),('Pressão arterial','110/70 mmHg'),('Frequência cardíaca','108 bpm',True),('Frequência respiratória','20 irpm'),('SpO₂','98% em ar ambiente')),
 topicos(('Estado geral','Lúcida, cansada, mucosas um pouco secas; sem icterícia.'),('Cardiopulmonar','Ritmo regular, sem sopros. Ausculta pulmonar sem alterações.'),('Abdome','Distendido, timpânico, ruídos pouco frequentes. Dor difusa à palpação profunda, sem defesa ou descompressão dolorosa. Sem hérnia palpável.'),('Pele e articulações','Sem exantema, sinovite ou edema. Cicatriz de apendicectomia.'),('Neurológico','Força e sensibilidade preservadas.')),so_kicker=True),
 painel('rotina','Na admissão','Exames iniciais',[
 ex('Hemoglobina / VCM','10,2 g/dL / 88 fL','12–16 g/dL / 80–100 fL',True),
 ex('Leucócitos','2.900/mm³ · neutrófilos 1.800 · linfócitos 700','4.000–11.000/mm³',True),
 ex('Plaquetas','142.000/mm³','150.000–450.000/mm³',True),
 ex('Sódio / potássio','133 / 2,9 mmol/L','135–145 / 3,5–5,0 mmol/L',True),
 ex('Creatinina / albumina','0,8 mg/dL / 2,8 g/dL','0,6–1,1 / 3,5–5,0',True),
 ex('Lipase / lactato','32 U/L / 1,2 mmol/L','até 60 / 0,5–2,0'),
 ex('Urina / teste de gravidez','Sem proteinúria ou hematúria · β-hCG negativo','—')],introducao='Hemograma, eletrólitos e avaliação renal foram colhidos na chegada. Enzimas hepáticas e bilirrubinas não apresentam alterações.'),
 Q('q1',1,'Quais três hipóteses você mantém inicialmente?',[
 ('Obstrução por bridas',True),('Íleo paralítico',True),('Doença inflamatória intestinal',True),('Pancreatite aguda',False),('Gastroenterite viral',False),('Cólica biliar',False)],
 [('Hipóteses de trabalho','Cirurgia prévia torna bridas plausíveis. Potássio baixo e anticolinérgico podem reduzir a motilidade; isso não prova que expliquem todo o quadro. Uma doença intestinal inflamatória também pode produzir perda de peso e obstrução.'),('O que ainda falta','A duração e a ausência de diarreia enfraquecem gastroenterite. Dor difusa, lipase normal e ausência de padrão biliar reduzem as demais opções. Exame seriado e imagem devem procurar obstrução, sofrimento de alça e causas sistêmicas.')]),
 pg('suporte_inicial','Primeiras medidas',
 'Marina permanece em jejum, recebe hidratação venosa com reavaliação e reposição de potássio e magnésio. Uma sonda nasogástrica drena 700 mL e reduz os vômitos. Escopolamina e ferro são suspensos. A cirurgia acompanha o exame abdominal; não há peritonite ou sinal clínico de isquemia.'),
 bifurcacao('b_imagem','Decisão','Investigação inicial','Qual exame você solicita agora?',[
 caminho('Tomografia de abdome com contraste','ct_precoce','Avalia ponto de transição, parede, mesentério e complicações. A função renal está preservada; suporte e exame seriado continuam.'),
 caminho('Trânsito intestinal contrastado','transito','Pode estudar trânsito em situações selecionadas, mas vômitos e suspeita de obstrução exigem avaliar segurança e podem impedir completar o exame.')]),
 pg('ct_precoce','Tomografia solicitada','Após a descompressão e a reposição inicial, Marina realiza TC. A cirurgia revê as imagens junto da clínica. Não se identificam alça fechada, pneumoperitônio ou lesão vascular.',segue='tc'),
 pg('transito','Durante o exame','Marina recebe a primeira porção do contraste oral, mas volta a vomitar. O exame é interrompido e a sonda retorna à drenagem. Ela continua sem defesa abdominal; não há imagem conclusiva de uma estenose.',
 'A equipe solicita TC para esclarecer a anatomia antes de insistir no contraste enteral. O episódio acrescenta perdas digestivas e reposição; não demonstra sozinho uma obstrução mecânica.',segue='tc'),
 # A imagem será inserida após revisão visual da figura real.
 pg('tc','Tomografia de abdome',
 'A TC mostra dilatação difusa do intestino delgado, espessamento de alguns segmentos e líquido livre moderado. Não há ponto de transição definido, massa obstrutiva, pneumatose ou ar livre. Há também discreta dilatação bilateral dos ureteres e sistemas coletores, sem cálculo visível.',
 'O exame não determina a causa da redução do trânsito. A equipe mantém vigilância cirúrgica e acompanha a função renal.'),
 Q('q2',2,'Quais duas conclusões são sustentadas pela avaliação até aqui?',[
 ('Não há obstrução mecânica demonstrada',True),('A alteração do potássio pode contribuir sem explicar o quadro inteiro',True),('A cirurgia prévia estabelece bridas como causa',False),('A ausência de uma massa exclui neoplasia intestinal',False),('O espessamento intestinal confirma doença de Crohn',False)],
 [('Anatomia e função','Alças dilatadas sem transição definida favorecem uma alteração de motilidade, mas não dispensam reavaliação se surgir peritonite ou piora. A TC não confirma uma doença específica pela espessura da parede.'),('Integração','Hipocalemia e medicamentos são causas tratáveis. A perda de peso, a albumina baixa e as citopenias pedem acompanhamento além da retirada do anticolinérgico. Uma hipótese funcional intestinal primária ainda seria prematura.')]),
 pg('evolucao','Terceiro dia',
 'O potássio chega a 4,0 mmol/L e o magnésio a 2,0 mg/dL. Marina está melhor hidratada, mas a sonda continua drenando cerca de 900 mL por dia. Uma tentativa de líquidos provoca distensão e náusea. A temperatura atinge 38,1 °C, sem instabilidade.',
 'O hemograma mantém leucopenia e anemia. A perda de peso precedia o uso de escopolamina; a suspensão do medicamento e a correção dos eletrólitos não resolveram o problema. Hemoculturas foram colhidas; a equipe revisa exposições, infecção e doença sistêmica.'),
 Q('q3',3,'Quais três exames você acrescenta nesta reavaliação?',[
 ('FAN',True),('Complemento C3',True),('Relação proteína/creatinina urinária',True),('CA-125',False),('ANCA',False),('Cortisol sérico',False),('Calprotectina fecal',False)],
 [('Investigar doença sistêmica','Citopenias persistentes e alterações em mais de um território justificam pesquisar autoimunidade e avaliar o rim, mesmo sem queixas urinárias. FAN é um teste de entrada; C3 e urina ajudam a interpretar o conjunto, não a confirmar isoladamente uma doença.'),('Prioridade relativa','CA-125 pode subir por irritação peritoneal e não resolveria a causa. Não há padrão de vasculite, crise adrenal ou diarreia inflamatória que dê maior prioridade às outras opções. Elas podem ganhar utilidade se surgirem novos dados.')]),
 painel('painel_sistemico','Reavaliação','Exames solicitados',[
 ex('FAN','Reagente, 1:640, padrão nuclear pontilhado','não reagente',True),
 ex('C3','52 mg/dL','90–180 mg/dL',True),
 ex('Relação proteína/creatinina urinária','0,18 g/g','abaixo de 0,2 g/g'),
 ex('Leucócitos / plaquetas','2.700 / 128.000 por mm³','4.000–11.000 / 150.000–450.000',True),
 ex('Hemoculturas','Sem crescimento até o momento','—')],introducao='FAN, C3 e avaliação urinária foram feitos em paralelo à reavaliação do abdome. O laboratório complementa o painel conforme a suspeita clínica.'),
 Q('q4',4,'Quais três hipóteses ainda precisam ser comparadas?',[
 ('Lúpus eritematoso sistêmico',True),('Tuberculose peritoneal',True),('Linfoma com comprometimento abdominal',True),('Íleo exclusivamente medicamentoso',False),('Esclerose sistêmica estabelecida',False),('Síndrome do intestino irritável',False)],
 [('O que o resultado muda','FAN e complemento baixo tornam lúpus uma hipótese relevante, sem fechar o diagnóstico. Infecção e neoplasia continuam no diferencial da febre, perda de peso e ascite. Investigar essas possibilidades influencia a segurança da imunossupressão.'),('O que não explica tudo','Não foram demonstrados os achados necessários para afirmar esclerose sistêmica. Um transtorno funcional ou efeito medicamentoso isolado integra mal as citopenias, a febre e a alteração do complemento. A atribuição final exige clínica, exames e evolução.')]),
 bifurcacao('b_amostra','Decisão','Complementar a investigação','Qual amostra você prioriza entre as opções disponíveis?',[
 caminho('Paracentese diagnóstica','liquido','Há janela segura ao ultrassom; o líquido permite avaliar celularidade, proteínas, culturas e citologia.'),
 caminho('Biópsia endoscópica de mucosa intestinal','mucosa','Pode investigar doença da mucosa e algumas infecções. Um resultado normal não avalia toda a parede nem exclui distúrbio de motilidade.')]),
 pg('liquido','Líquido ascítico','A paracentese obtém líquido claro, com 280 células/mm³ e predomínio linfocitário. Não há neutrofilia que sustente peritonite bacteriana. Cultura bacteriana e citologia são negativas. A pesquisa inicial para micobactérias é negativa; a cultura permanece em processamento.',
 'Nenhum desses resultados, isoladamente, exclui tuberculose ou neoplasia. A equipe reúne o baixo volume de ascite, a ausência de massa e a evolução dos demais órgãos.',segue='novo_exame'),
 pg('mucosa','Endoscopia com biópsias','Após descompressão, a endoscopia encontra mucosa duodenal sem ulceração. As biópsias não demonstram granulomas, neoplasia ou inflamação mucosa relevante. O procedimento não avalia de forma adequada o músculo e os nervos responsáveis pela motilidade.',
 'As amostras não estabelecem a causa. A equipe mantém acompanhamento clínico, microbiologia e reavaliação das citopenias.',segue='novo_exame'),
 pg('novo_exame','Quinto dia','Marina passa a ter duas úlceras no palato e dor nas mãos. Ao reexame, há sinovite em articulações metacarpofalângicas, ausente na chegada. Ela continua sem tolerar alimentação, apesar de eletrólitos normais e da retirada dos medicamentos constipantes.',
 'Anti-DNA nativo retorna reagente em título elevado e C4 é 6 mg/dL (referência: 10–40). A reumatologia revê os dados. Culturas bacterianas permanecem negativas e não se identificou foco que explique o conjunto.'),
 Q('q5',5,'Quais duas interpretações melhor integram a evolução?',[
 ('Os novos achados tornam uma doença autoimune sistêmica a explicação mais consistente',True),('Uma biópsia mucosa normal não exclui comprometimento da motilidade por doença sistêmica',True),('O FAN positivo, sozinho, já estabelecia o diagnóstico na primeira coleta',False),('A ausência de proteinúria importante exclui lúpus',False),('Culturas iniciais negativas excluem toda infecção abdominal',False)],
 [('Do resultado à doença','As manifestações surgiram em momentos diferentes. Citopenias, consumo de complemento, anticorpo específico, úlceras orais e sinovite passam a formar um conjunto coerente para lúpus; a interpretação não depende apenas do FAN.'),('Abdome','O quadro de pseudo-obstrução é atribuído à doença sistêmica após excluir razoavelmente obstrução mecânica e outras causas. Nem toda manifestação de lúpus exige nefrite, e a mucosa pode ser pouco alterada em distúrbios neuromusculares intestinais.')]),
 pg('discussao','Discussão anatomoclínica','O diagnóstico de trabalho é lúpus eritematoso sistêmico com pseudo-obstrução intestinal. Não foi uma biópsia isolada que nomeou a doença: a evolução acrescentou manifestações clínicas e laboratoriais que não estavam presentes na primeira consulta.',
 'A equipe mantém o exame abdominal seriado e acompanha culturas pendentes. Dor com defesa, elevação de lactato ou novos sinais de isquemia obrigariam a rever a hipótese e a urgência cirúrgica. A baixa tolerância alimentar exige suporte nutricional individualizado.'),
 bifurcacao('b_tratamento','Decisão','Tratamento inicial','Qual via você escolhe para iniciar o glicocorticoide neste momento?',[
 caminho('Intravenosa','via_ev','Vômitos e trânsito muito reduzido tornam a exposição oral incerta; a via intravenosa garante a administração.'),
 caminho('Oral','via_oral','É viável quando há absorção e tolerância. Nesta fase, vômitos e drenagem pela sonda exigem acompanhar se a dose é efetivamente recebida.')]),
 pg('via_ev','Após iniciar tratamento','Após avaliação conjunta e revisão de infecção, Marina recebe metilprednisolona intravenosa, 500 mg/dia por três dias. Nas 48 horas seguintes a drenagem diminui, ela elimina gases e a dor das mãos cede. A dieta é retomada em pequenas porções.',
 'A resposta apoia a interpretação clínica, mas não funciona como teste exclusivo para lúpus. A equipe faz transição para prednisona oral e planeja redução conforme atividade e tolerância.',segue='manutencao'),
 pg('via_oral','Após a primeira tentativa','Marina vomita a dose oral e continua com drenagem elevada pela sonda. Não há exposição confiável ao medicamento. A equipe muda para metilprednisolona intravenosa e mantém suporte nutricional; a retomada alimentar será mais lenta neste percurso.',
 'Vômitos não demonstram resistência imunológica. Antes de aumentar uma dose ou trocar de imunossupressor, é preciso distinguir falha de absorção de falha de efeito.',segue='manutencao'),
 Q('q6',6,'Quais duas medidas você inclui no plano após o controle inicial?',[
 ('Hidroxicloroquina conforme peso e avaliação clínica',True),('Redução programada do glicocorticoide',True),('Manter a dose de pulso até normalizar o FAN',False),('Retomar anticolinérgico regularmente',False),('Definir atividade da doença apenas pelo título do FAN',False)],
 [('Controle sustentado','Hidroxicloroquina integra o manejo do lúpus quando não há contraindicação; dose, interações e seguimento ocular são revistos. Glicocorticoide deve ser reduzido conforme atividade, com objetivo de minimizar exposição.'),('O que acompanhar','Sintomas, exame, hemograma, função renal, urina e complemento têm utilidade clínica. O FAN não é um alvo para manter pulsos. A recuperação nutricional e do trânsito deve ser acompanhada, inclusive após melhora articular.')],segue='manutencao'),
 pg('manutencao','Plano e seguimento','Com 54 kg, o plano inclui hidroxicloroquina 200 mg/dia e seguimento reumatológico e oftalmológico. A prednisona oral é ajustada e reduzida de acordo com atividade; o objetivo é evitar dependência de dose alta. São revistos risco infeccioso, vacinação e prevenção de complicações do corticoide.',
 'Hemograma, urina, creatinina, eletrólitos e recuperação alimentar são reavaliados. A dieta e o suporte são conduzidos em conjunto com nutrição. A resposta dos órgãos pode ocorrer em velocidades diferentes.',segue='q7'),
 Q('q7',7,'Quais duas mudanças no seguimento exigem reabrir a investigação abdominal?',[
 ('Dor nova com defesa abdominal',True),('Recorrência de vômitos com perda de peso',True),('FAN ainda reagente sem mudança clínica',False),('Persistência de anticorpo isolado em paciente assintomática',False),('Recuperação lenta do peso com ingestão progressivamente melhor',False)],
 [('Reavaliar a síndrome','Uma pessoa com lúpus também pode ter obstrução, infecção e complicações vasculares. O diagnóstico anterior não deve explicar automaticamente todo novo sintoma. Defesa abdominal pede avaliação urgente; recorrência com perda de peso exige revisão de trânsito, nutrição, remédios e atividade.'),('Evitar exames sem pergunta','Anticorpos podem persistir após melhora. A conduta deve responder à mudança clínica e dos órgãos, sem tratar isoladamente a permanência do FAN.')],segue='encaminhamento_final'),
 pg('encaminhamento_final','Fim da internação','O plano é revisto com Marina e sua família, incluindo sinais para retorno, acesso aos medicamentos e consultas.',conforme={'de':'b_tratamento','para':['alta_alimentacao','suporte_nutricional']}),
 fim('alta_alimentacao','Seguimento ambulatorial',['Marina recebe alta após voltar a tolerar refeições. Em seis semanas, recupera 2 kg, não apresenta novos vômitos e mantém creatinina normal. A leucopenia melhora parcialmente. A dilatação urinária e as alterações intestinais diminuem no controle de imagem.'],'Neste percurso, houve exposição adequada ao tratamento e recuperação alimentar suficiente para seguimento ambulatorial.',qualidade='melhor'),
 fim('suporte_nutricional','Continuidade do suporte nutricional',['Após a troca para a via intravenosa, Marina melhora, mas permanece com intolerância alimentar por mais dias. Precisa de suporte nutricional prolongado e transição supervisionada antes da alta. O objetivo é recuperar ingestão e função, sem insistir em medicamento que não estava sendo absorvido.'],'A diferença deste percurso é a exposição inicial incerta e a necessidade prolongada de suporte; não se afirma que toda tentativa oral tenha esse desfecho.'),
 pagina('retrospectiva','Pontos de ensino','',pontos('Distinguir obstrução mecânica de alteração da motilidade exige clínica e imagem, sem ignorar sinais cirúrgicos.','Hipocalemia e medicamentos podem contribuir sem explicar toda a evolução.','FAN não confirma lúpus sozinho; as manifestações podem surgir em consultas diferentes.','A investigação de infecção e neoplasia deve acompanhar a hipótese inflamatória.','Uma via de administração inadequada pode parecer falha do tratamento.'),so_kicker=True,segue='referencias'),
 pg('referencias','Fontes e limites','Caso e percursos autorais, inspirados em relatos de pseudo-obstrução como apresentação do lúpus. Valores, cronologia e respostas simulados para ensino; não reproduzem um paciente real.',
 '<a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC4479744/">Oh et al., Intestinal Research 2015</a>; <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC7683163/">Nyabera et al., 2020, figuras abdominais, CC BY 4.0</a>; <a href="https://ard.bmj.com/content/early/2023/10/11/ard-2023-224762">EULAR 2023, manejo de lúpus</a>. Capas: ilustração original de paciente ficcional. Material do atlas: acervo de Matheus Parente, com referência original junto à figura. As amostras invasivas e respostas dos ramos são construções didáticas.')
]
REVISAO=[]
# Depois das páginas de via, a pergunta de manutenção é comum aos dois percursos.
for e in ETAPAS:
 if e['k'] in ('via_ev','via_oral'):e['segue']='q6'

# Figuras com contexto e laudo revelável; o texto não antecipa a interpretação.
from motor.estudo_imagem import inserir_antes
inserir_antes(ETAPAS,'b_imagem',[
 estudo('rx_inicial','Radiografia de abdome','O exame é obtido durante a descompressão inicial. Como você descreve a distribuição do gás?',IMG/'CRIGM2020-8873917.001.jpg','Abdome em incidência frontal.','Nyabera et al., 2020 · CC BY 4.0 · marcação vermelha original',[],
 ['Alças de intestino delgado distendidas.','A radiografia não determina sozinha se existe um bloqueio mecânico. A avaliação clínica e, quando indicada, a TC esclarecem melhor a anatomia.'])])
i=next(i for i,e in enumerate(ETAPAS) if e['k']=='tc')
ETAPAS[i]=estudo('tc','Tomografia de abdome','A cirurgia e a clínica reveem a TC. Compare o intestino e os sistemas coletores antes de abrir o laudo.',IMG/'CRIGM2020-8873917.002.jpg','Corte axial (a) e reconstrução coronal (b).','Nyabera et al., 2020 · CC BY 4.0 · marcações vermelhas originais',[],
 ['O estudo completo descreve distensão do delgado e espessamento de segmentos, ascite e dilatação bilateral dos sistemas coletores e ureteres.','Não se identifica ponto de transição ou massa obstrutiva no estudo completo. Esses achados não definem a causa. Ausência de cálculo e avaliação de isquemia dependem da série completa, não apenas destes dois painéis.'])
inserir_antes(ETAPAS,'evolucao',[
 estudo('comparacao_mecanica','Comparação de padrões','Após discutir a TC, compare este padrão radiográfico de obstrução mecânica com a investigação de Marina. Qual informação a radiografia não fornece?',IMG/'rx_obstrucao_comparacao.jpg','Radiografia para discussão do padrão de distensão.','Acervo de Matheus Parente · Szejnfeld e Abdala, 2015 · cap. 66, p. 423 · marcações originais',[],
 ['Alças distendidas e níveis hidroaéreos no exemplo de obstrução mecânica.','Distensão e níveis podem ocorrer em mecanismos diferentes. A localização de uma transição, a evolução e os sinais de sofrimento intestinal ajudam a decidir a conduta; a aparência do gás não confirma a etiologia.'])])
# Não afirmar um procedimento de um ramo como se tivesse ocorrido no outro.
for e in ETAPAS:
 if e['k']=='q5':
  for a in e['alts']:
   if 'biópsia mucosa normal' in a['t'].lower():
    a['t']='O exame urinário pouco alterado não impede uma doença sistêmica'
ETAPAS.insert(next(i for i,e in enumerate(ETAPAS) if e['k']=='retrospectiva'),
 estudo('controle_imagem','Controle de imagem','Depois da recuperação alimentar, o controle radiológico é comparado ao estudo inicial. A imagem acompanha a avaliação clínica, sem definir sozinha remissão.',IMG/'CRIGM2020-8873917.003.jpg','Controle tomográfico após tratamento.','Nyabera et al., 2020 · CC BY 4.0 · marcações vermelhas originais',[],
 ['Redução da distensão e da dilatação dos sistemas coletores descrita no controle.','A resposta em conjunto com manifestações sistêmicas e investigação de alternativas sustenta a interpretação clínica. Resposta ao corticoide isolada não confirma lúpus.'],segue='retrospectiva'))
for e in ETAPAS:
 if e['t']=='desfecho':e['fecho']='controle_imagem'

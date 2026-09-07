"""Caso ficcional. Evoluções autorais; não constituem previsão de prognóstico."""
from pathlib import Path
from motor.etapas import (alt, bifurcacao, caminho, capa, desfecho, grade, grupo,
    lamina, op, p, pagina, pedido, pergunta, resultados, tabela, topicos, vitais)
from motor.desenhos import corpo
TITULO = 'O peso dos dias'
RODAPE = 'Caso ficcional · evoluções simuladas para ensino'
IMG = Path(__file__).parent / 'img'
BANCO = []
CENA = 'cena.png'
CREDITO = 'Ilustração gerada por IA para este paciente ficcional; não é documentação de achado clínico.'
def pg(k, titulo, *blocos, **kw):
    return pagina(k, titulo, '', *blocos, fundo=CENA, so_kicker=True, **kw)
def ex(n, r, ref='—', a=False):
    return op(n, resultado=r, referencia=ref, alterado=a)
def q(k, texto, itens, segue=''):
    return pergunta(k, 'Pergunta '+k[1:], texto,
        [alt(t, c, certa=ok) for t,c,ok in itens],
        titulo_resposta='Discussão', fundo=CENA, segue=segue)
def fim(k, titulo, texto, porque, qualidade='medio'):
    return desfecho(k,titulo,p(texto),qualidade=qualidade,porque=porque,
        fundo=CENA,fecho='retrospectiva')
ETAPAS = [
    capa(TITULO,fundo=CENA,procedencia='Paciente ficcional. Curso simulado.'),
    pg('historia','Apresentação',
       p('Antônio, um homem de 71 anos, é levado pela esposa ao pronto atendimento porque, naquela manhã, não conseguiu ir sozinho ao banheiro. Há quatro dias apresenta febre e cefaleia. Ao entrar no consultório, diz que está “sem firmeza nas pernas” e que deve ter se alimentado mal.'),
       p('Até a semana anterior, caminhava até o mercado, cuidava das próprias contas e buscava o neto na escola. A esposa estranhou que ele precisasse se apoiar nos móveis e demorasse a responder a perguntas simples.'),
       lamina_=lamina(CENA,'Antônio, na admissão','Ilustração do paciente ficcional.',CREDITO)),
    pg('hda','História da doença atual',
       p('Quatro dias antes, começou a sentir indisposição e dor de cabeça difusa, de instalação gradual, acompanhadas de calafrios. A temperatura chegou a 38,4 °C em casa. Tomou paracetamol, com alívio por algumas horas, mas permaneceu sem apetite. Não havia tosse, coriza, dor torácica ou ardor ao urinar.'),
       p('No dia seguinte passou a maior parte do tempo deitado. Teve náusea, sem vômitos persistentes ou diarreia. A cefaleia não era súbita nem semelhante a uma dor que já conhecesse. Não descrevia diplopia, perda visual ou formigamento.')),
    pg('hda2','História da doença atual',
       p('Na véspera da admissão, precisou interromper o banho para sentar-se. A esposa percebeu que ele derrubou um copo e perguntou duas vezes sobre um compromisso já cancelado. Ele atribuiu o cansaço à febre e preferiu não procurar atendimento naquela noite.'),
       p('Pela manhã, ao tentar levantar da cama, a perna direita cedeu. Não perdeu a consciência e não bateu a cabeça. A dificuldade persistiu mesmo depois de se alimentar. A esposa não observou convulsão, desvio da boca ou fala arrastada.')),
    pg('antecedentes','Antecedentes pessoais',
       p('Tem hipertensão há catorze anos e diabetes tipo 2 há sete, acompanhadas na unidade de saúde. Não conhece doença renal, retinopatia ou perda de sensibilidade nos pés. Nunca teve acidente vascular cerebral, crise convulsiva ou dificuldade semelhante para caminhar. Não usa bengala e não havia queixa cognitiva progressiva.'),
       p('Foi submetido a herniorrafia inguinal há cerca de vinte anos. Não tem câncer, transplante ou tratamento imunossupressor. Nega alergias medicamentosas conhecidas. O pai tinha hipertensão; não há doença neuromuscular conhecida na família.')),
    pg('medicacoes','Medicações e contexto de vida',
       p('Usa losartana 50 mg pela manhã e metformina 850 mg duas vezes ao dia. A esposa confirma as caixas e a ausência de mudança recente. Durante a doença tomou apenas paracetamol, sem sedativos, anti-histamínicos ou medicamentos emprestados.'),
       p('É aposentado, mora com a esposa e mantém convívio frequente com filhos e netos. Parou de fumar há vinte anos, após aproximadamente doze anos-maço; bebe cerveja ocasionalmente, sem consumo pesado. A história de deslocamentos e exposições será complementada com a família durante a internação.')),
    pg('exame','Exame físico',
       vitais(('PA','146/84 mmHg',False),('FC','102 bpm',True),('FR','20 irpm',False),('Temperatura','38,7 °C',True),('SpO₂','96% em ar ambiente',False)),
       topicos(('Estado geral','Desperto, responde lentamente e erra o dia do mês. Mucosas discretamente secas.'),
               ('Cardiopulmonar','Ritmo regular, sem sopro; murmúrio vesicular presente, sem ruídos adventícios.'),
               ('Abdome e pele','Abdome indolor. Sem lesão cutânea ou edema.'),
               ('Neurológico','Sem rigidez de nuca evidente. Face simétrica e fala compreensível. Eleva os quatro membros, mas não se mantém em pé sem auxílio. Exame motor detalhado será repetido após analgesia.'))),
    q('p1','A dificuldade para caminhar surgiu durante uma doença febril, com lentificação nova. Quais duas avaliações têm prioridade antes de atribuir tudo à desidratação?',[
      ('Pesquisar déficit motor focal e sinais meníngeos.','A observação inicial não localiza a dificuldade para andar.',True),
      ('Solicitar rastreio de neuropatia diabética crônica.','Pode explicar perda sensitiva antiga, mas não a febre e a mudança cognitiva agudas.',False),
      ('Medir glicemia e pesquisar alterações metabólicas.','Causas reversíveis podem produzir ou agravar alteração do estado mental.',True),
      ('Programar avaliação neurológica apenas se não melhorar com soro.','Melhora parcial da perfusão não exclui infecção do sistema nervoso.',False),
      ('Priorizar investigação de hipotensão postural medicamentosa.','Não há hipotensão nem mudança de dose que sustente essa explicação.',False)]),
    pg('avaliacao_atencao','Avaliação inicial',
       p('Antônio reconhece a esposa e informa onde mora, mas perde o fio da conversa quando duas pessoas falam ao mesmo tempo. Ao pedir que repita uma sequência curta de palavras, é preciso retomar a instrução. Não parece compreender por que o atendimento está demorando.'),
       p('A esposa esclarece que esse comportamento começou com a doença atual. A equipe registra a alteração da atenção e mantém observação para acompanhar consciência, mobilidade e capacidade de engolir.')),

    pedido('ex1','Investigação inicial','Primeira rodada','Febre, cefaleia e perda recente da autonomia acompanham alteração cognitiva. Quais quatro exames você prioriza para investigar causas tratáveis e avaliar a gravidade?',[
      grupo('Sangue','sangue',[
        ex('Hemograma','Hb 13,2 g/dL · leucócitos 10.900/mm³ · plaquetas 181.000/mm³','Hb 13–17 · leucócitos 4.000–11.000 · plaquetas 150.000–450.000'),
        ex('Glicemia','132 mg/dL','70–140 (valor casual adotado no caso)'),
        ex('Eletrólitos e função renal','Na 131 mmol/L · K 4,1 mmol/L · creatinina 1,1 mg/dL','Na 135–145 · K 3,5–5,0 · Cr 0,7–1,3',True),
        ex('Creatinoquinase','124 U/L','40–200'),
        ex('Transaminases','AST 39 U/L · ALT 35 U/L','Até 40'),
        ex('Proteína C reativa','42 mg/L','Menor que 5',True)]),
      grupo('Avaliação complementar','geral',[
        ex('Urina tipo 1','0–2 leucócitos/campo · nitrito negativo · sem sangue'),
        ex('Radiografia de tórax','Sem opacidade focal ou derrame pleural.'),
        ex('Hemoculturas iniciais','Coletadas; em processamento nesta etapa.'),
        ex('Eletrocardiograma','Ritmo sinusal, frequência 102 bpm.'),
        ex('TSH','2,4 mUI/L','0,4–4,0'),
        ex('Vitamina B12','410 pg/mL','200–900')])],banco=BANCO,limite=4,fundo=CENA),
    resultados('res1','Resultados','Primeira rodada','ex1',fundo=CENA,laminas={'Radiografia de tórax':lamina('rx_torax_normal.jpg','Radiografia de tórax','Imagem comparativa de outro adulto. Ausência de opacidade focal evidente não exclui infecção precoce.','Mikael Häggström · Wikimedia Commons · CC0. Imagem ilustrativa.')}),
    pg('reexame','Reavaliação',
       p('Depois de analgesia e hidratação cautelosa, continua desorientado. A perna direita não vence a gravidade; a esquerda vence resistência leve. O braço direito está discretamente mais fraco que o esquerdo. A sensibilidade ao toque e à picada permanece simétrica.'),
       p('Os reflexos patelar e aquileu direitos estão abolidos; à esquerda estão diminuídos. Não há nível sensitivo. Surge rigidez de nuca discreta. A dificuldade não se limita à dor ou à fadiga.'),
       segue='p2'),
    q('p2','A paresia é assimétrica, flácida e hiporreflexa, durante febre e alteração cognitiva. Quais duas conclusões são sustentáveis?',[
      ('A arreflexia estabelece Guillain–Barré.','Também ocorre em lesões do neurônio motor inferior por outros mecanismos.',False),
      ('A ausência de nível sensitivo exclui doença medular.','Lesões da substância cinzenta podem poupar vias sensitivas.',False),
      ('A fraqueza deve ser atribuída à encefalopatia.','Há déficit motor lateralizado que exige localização própria.',False),
      ('A localização motora precisa ser investigada junto da síndrome encefalítica.','Uma única doença pode comprometer mais de um compartimento neurológico.',True),
      ('Infecção do sistema nervoso continua prioritária.','Febre, alteração cognitiva e meningismo exigem investigação e tratamento empírico oportunos.',True)]),
    pg('imagem_localizacao','Discussão de imagem',
       p('Observe o corte transversal da medula. Que estruturas você relacionaria à força, à sensibilidade e aos reflexos? Localize-as antes de abrir a discussão.'),
       '<details class="leitura"><summary>Revelar pontos de discussão</summary><p>Os cornos anteriores abrigam corpos celulares motores; as raízes ventrais levam axônios motores para a periferia. O comprometimento dessas estruturas pode produzir fraqueza e hiporreflexia sem o padrão sensitivo de uma lesão medular transversa. O esquema não identifica a etiologia.</p></details>',
       lamina_=lamina('medula.svg','Medula espinal','Esquema anatômico comparativo; não é exame do paciente. Rótulos originais em inglês.','Polarlys · Wikimedia Commons · CC BY 2.5 · sem alterações.')),

    bifurcacao('b1','Decisão','Conduta inicial','Qual caminho você escolhe diante da reavaliação?',[
      caminho('Internar, colher amostras e iniciar cobertura empírica para meningoencefalite.','r_interna','A coleta é importante, mas não deve atrasar antimicrobianos quando a suspeita é relevante.'),
      caminho('Conduzir como polirradiculoneuropatia e priorizar imunoglobulina.','r_ig','Guillain–Barré é um diferencial, mas febre ativa e encefalopatia tornam insuficiente essa hipótese isolada.'),
      caminho('Manter observação com hidratação antes de ampliar a investigação.','r_observa','A observação sem investigação dirigida pode retardar o reconhecimento da progressão neurológica.')],fundo=CENA),
    pg('r_interna','Primeiro dia',p('Antônio é internado em leito monitorizado. A esposa permanece disponível para complementar a história, e a equipe registra força, consciência e deglutição como parâmetros de reavaliação. São iniciados aciclovir e cobertura para meningite bacteriana, incluindo Listeria pela idade, com ajuste à função renal e ao protocolo local. A coleta de amostras e a avaliação de segurança da punção são organizadas sem atrasar o tratamento.'),segue='reavaliacao_internacao'),
    pg('r_ig','Primeiro dia',p('A imunoglobulina é iniciada sob a hipótese de polirradiculoneuropatia. Ele mantém febre e confusão e desenvolve tremor de ação. Na revisão conjunta, a equipe amplia a abordagem para meningoencefalite e inicia cobertura empírica. A hipótese inicial será reavaliada, sem esperar resposta imediata à imunoglobulina.'),segue='reavaliacao_internacao'),
    pg('r_observa','Primeiro dia',p('Durante a observação, a perna direita passa a apresentar apenas contração, sem movimento e ele se torna mais sonolento. É transferido para internação monitorizada. A equipe de resgate inicia a abordagem empírica de meningoencefalite; os resultados etiológicos ainda dependem da investigação.'),segue='reavaliacao_internacao'),
    pg('reavaliacao_internacao','Reavaliação na internação',
       p('Na transferência para o leito, precisa de duas pessoas para se acomodar. Ao tentar ajustar o lençol, usa mais a mão esquerda. Mantém sensibilidade ao toque e responde quando chamado, mas alterna períodos de conversa com sonolência.'),
       p('A cefaleia permanece. A equipe revê a evolução da consciência e o déficit focal antes de definir a segurança da punção e a necessidade de imagem prévia. A investigação não deve atrasar o tratamento empírico já indicado.'),segue='ex2'),

    pedido('ex2','Investigação','Segunda rodada','A paresia assimétrica persiste com febre e confusão. Quais quatro investigações distinguiriam os mecanismos possíveis e mudariam a conduta?',[
      grupo('Sistema nervoso','nervo',[
        ex('Líquor: celularidade, proteína, glicose e Gram','86 células/mm³ (58% neutrófilos) · proteína 92 mg/dL · glicose 68 mg/dL, sérica 120 · Gram sem bactérias','Até 5 células · proteína 15–45 · relação glicose >0,4',True),
        ex('Cultura e PCR bacteriana do líquor','Sem crescimento até o momento · painel bacteriano negativo.'),
        ex('PCR para HSV e VZV no líquor','Não detectados em amostra obtida no sexto dia de sintomas.'),
        ex('Tomografia de crânio sem contraste','Sem hemorragia intracraniana, hidrocefalia ou efeito de massa significativo. TC sem lesão evidente não exclui encefalite ou isquemia precoce.'),
        ex('Ressonância de encéfalo e medula','Sem infarto, compressão medular ou lesão temporal. Ausência de alteração específica não exclui inflamação.'),
        ex('Eletroneuromiografia','Respostas motoras reduzidas, assimétricas; respostas sensitivas preservadas. Sem critérios de desmielinização. Estudo precoce requer correlação clínica.', '—',True),
        ex('Eletroencefalograma','Lentificação difusa, sem atividade epiléptica registrada.')]),
      grupo('Outras hipóteses','geral',[
        ex('HIV Ag/Ac','Não reagente.'),ex('Sífilis: teste treponêmico e VDRL','Não reagentes.'),
        ex('Dengue: NS1 e IgM','Não reagentes.'),ex('Leptospira: PCR','Não detectado.'),
        ex('Amônia','28 µmol/L','11–35'),ex('Cortisol matinal','18 µg/dL','5–25')])],banco=BANCO,limite=4,fundo=CENA),
    resultados('res2','Resultados','Segunda rodada','ex2',fundo=CENA,
      laminas={'Tomografia de crânio sem contraste':lamina('tc_cranio.png','TC de crânio','Corte axial e localizador sagital de outro adulto. Figura ilustrativa; não representa o exame completo nem exclui encefalite.','Mikael Häggström · Wikimedia Commons · CC0 · sem alterações.'),
      'Ressonância de encéfalo e medula':lamina('rm_encefalo.png','RM do encéfalo','A figura ilustra somente um corte axial T2 do encéfalo de outro adulto. Não mostra a medula nem todas as sequências do estudo. Não permite excluir encefalite ou isquemia.','Sean Novak · Wikimedia Commons · CC BY-SA 4.0 · sem alterações.')},
      rota={'pediu':['Líquor: celularidade, proteína, glicose e Gram'],'entao':'p3','senao':'sem_lcr'}),
    q('p3','O líquor tem 86 células/mm³, predomínio neutrofílico e glicose preservada. Qual interpretação é a mais adequada?',[
      ('O predomínio neutrofílico comprova meningite bacteriana.','A celularidade inicial de algumas infecções virais também pode ser neutrofílica.',False),
      ('O perfil admite etiologia viral, mas exige avaliação microbiológica.','O conjunto e o momento da coleta pesam mais que um tipo celular isolado.',True),
      ('A glicose preservada permite interromper toda cobertura agora.','Esse valor não exclui isoladamente etiologia bacteriana ou herpes.',False),
      ('Há dissociação albuminocitológica típica de Guillain–Barré.','A pleocitose expressiva exige procurar uma explicação alternativa.',False),
      ('A proteína elevada localiza a lesão no nervo periférico.','A hiperproteinorraquia não fornece essa localização específica.',False)],segue='historia2'),
    pg('sem_lcr','Discussão',p('A equipe ainda não dispõe de caracterização do líquor neste percurso. O diagnóstico permanece sindrômico: doença febril com alteração do estado mental e paresia flácida assimétrica.'),p('As hipóteses infecciosas seguem cobertas empiricamente. A falta de definição não impede monitorização respiratória ou nova avaliação neurológica.'),segue='historia2'),
    pg('historia2','História complementar',p('Ao reconstruir o mês anterior com a esposa, a equipe confirma que voltaram de uma visita a familiares na Louisiana, no sul dos Estados Unidos, doze dias antes da febre. Ele passava o fim de tarde no quintal, próximo de uma área alagada. Ambos tiveram várias picadas de insetos. Não houve mordida de animal, contato com água de enchente ou consumo de leite não pasteurizado. Ela permaneceu bem. Antônio já havia tido dengue anos antes, sem complicação neurológica.'),p('No segundo dia de internação, a tosse fica fraca. Ele engasga com água, embora mantenha saturação de 96% em ar ambiente. A avaliação à beira do leito mostra queda da capacidade vital de 24 para 17 mL/kg e piora da força inspiratória.')),
    bifurcacao('b2','Decisão','Suporte respiratório','Como você conduz essa mudança?',[
      caminho('Transferir para terapia intensiva e proteger a via aérea de forma planejada.','r_via','A progressão bulbar e ventilatória permite antecipar uma via aérea difícil em vez de esperar o colapso.'),
      caminho('Tentar ventilação não invasiva com vigilância intensiva.','r_vni','Uma tentativa exige seleção e critérios precoces de falha; disfagia e secreções reduzem a margem de segurança.'),
      caminho('Manter oxigênio e vigilância na enfermaria enquanto investiga.','r_atraso','A saturação não mede adequadamente a reserva ventilatória nem a proteção contra aspiração.')],fundo=CENA),
    pg('r_via','Terceiro dia',p('É intubado de forma planejada por progressão da disfunção bulbar e fraqueza ventilatória. Não há aspiração reconhecida. A febre começa a ceder, mas a paresia permanece. Ao reduzir a sedação, reconhece a esposa e segue comandos; movimenta menos o lado direito. A família pergunta se a melhora da febre significa que voltará a andar. O suporte permite continuar a investigação.'),segue='p4'),
    pg('r_vni','Reavaliação respiratória',p('Com ventilação não invasiva, acumula secreções e não consegue expectorar. Mantém episódios de engasgo. A oxigenação segue preservada, mas a proteção da via aérea piora.'),segue='b_resgate'),
    pg('r_atraso','Reavaliação respiratória',p('Na enfermaria, apresenta engasgo seguido de aumento do esforço respiratório. É levado à sala de emergência. O cenário agora exige decidir sobre proteção da via aérea e suporte intensivo.'),segue='b_resgate'),
    bifurcacao('b_resgate','Decisão','Reavaliação da conduta','Diante da falha de eliminação de secreções, qual é a próxima conduta?',[
      caminho('Interromper a estratégia inicial e realizar intubação.','r_resgate','A mudança de plano é uma resposta à evolução, não precisa esperar falência completa.'),
      caminho('Prolongar o suporte não invasivo e reavaliar após a investigação.','f_obito','A incapacidade de proteger a via aérea torna perigoso adiar o suporte invasivo.')],fundo=CENA),
    pg('r_resgate','Quarto dia',p('Após intubação de resgate, necessita de suporte ventilatório prolongado. Quando desperto, tenta comunicar-se por gestos e demonstra frustração por não conseguir elevar a perna direita. O episódio de aspiração motiva investigação e tratamento de complicação pulmonar. A fraqueza assimétrica continua presente quando a sedação é reduzida.'),segue='p4'),
    q('p4','A saturação está preservada, mas há disfagia, tosse fraca e queda seriada da capacidade vital. Quais duas medidas são prioritárias?',[
      ('Suspender ingestão oral até avaliar a deglutição.','A disfunção bulbar aumenta o risco de aspiração.',True),
      ('Aguardar dessaturação para solicitar avaliação intensiva.','A oximetria pode permanecer normal durante a deterioração ventilatória.',False),
      ('Reavaliar somente pela gasometria após oferecer oxigênio.','Oxigênio não corrige falência da bomba respiratória.',False),
      ('Acionar terapia intensiva e planejar proteção de via aérea.','Tendência funcional, tosse e proteção da via aérea orientam a intervenção.',True),
      ('Manter líquidos por via oral para fluidificar secreções.','A disfagia exige avaliação antes de manter essa via.',False)],segue='visita_dia4'),
    pg('visita_dia4','Quarto dia',
       p('Quando a sedação é reduzida, acompanha a esposa com o olhar e responde por gestos. Consegue apertar sua mão, mas não eleva a perna direita do leito. A família percebe que ele está mais presente na conversa, embora o movimento não tenha melhorado na mesma proporção.'),
       p('A equipe organiza a cronologia com os familiares: início da febre, aparecimento da dificuldade para caminhar, mudança do comportamento e piora da tosse. A evolução continua sendo reavaliada junto dos resultados disponíveis.'),segue='ex3'),

    pedido('ex3','Investigação','Terceira rodada','Após complementar a exposição e acompanhar a evolução neurológica, quais quatro exames acrescentariam informação etiológica ou ajudariam a rever as hipóteses concorrentes?',[
      grupo('Agentes e exposição','geral',[
        ex('IgM para vírus do Nilo Ocidental em soro e líquor','Reagente nas duas amostras; resultado presuntivo, sujeito a reação cruzada.', 'Não reagente',True),
        ex('PCR para enterovírus no líquor','Não detectado.'),
        ex('Sorologia para encefalite de Saint Louis','IgM não reagente.'),
        ex('Chikungunya: IgM','Não reagente.'),
        ex('Pesquisa de malária','Gota espessa sem parasitas.'),
        ex('Pesquisa de vírus rábico em laboratório de referência','Não detectado nas amostras do protocolo; interpretar com história de exposição.')]),
      grupo('Mecanismos alternativos','nervo',[
        ex('Anticorpos anti-GM1','Não reagentes; resultado negativo não exclui neuropatia imune.'),
        ex('Anticorpos de encefalite autoimune','Painel sem reatividade; resultado isolado não exclui encefalite autoimune.'),
        ex('Porfobilinogênio urinário','Dentro do intervalo do método.'),
        ex('Nova eletroneuromiografia','Denervação ativa assimétrica, respostas motoras reduzidas e sensitivas preservadas; sem desmielinização.', '—',True),
        ex('Nova PCR para HSV no líquor','Não detectado.'),
        ex('Cobre sérico','102 µg/dL','70–140')])],banco=BANCO,limite=4,fundo=CENA),
    resultados('res3','Resultados','Terceira rodada','ex3',fundo=CENA,rota={'pediu':['IgM para vírus do Nilo Ocidental em soro e líquor'],'entao':'p5','senao':'indefinido'}),
    q('p5','A IgM reagente para Nilo Ocidental combina com o contexto, mas o paciente já teve dengue. Qual é a melhor forma de consolidar a atribuição etiológica?',[
      ('Interpretar qualquer IgM como confirmação definitiva.','Anticorpos contra flavivírus podem apresentar reação cruzada.',False),
      ('Excluir a hipótese se a PCR sérica for negativa.','A detecção molecular tem sensibilidade limitada em imunocompetentes.',False),
      ('Substituir a IgM por uma IgG isolada.','IgG isolada pode refletir contato antigo.',False),
      ('Solicitar neutralização em laboratório de referência.','O teste ajuda a distinguir reatividade entre flavivírus; amostras pareadas podem acrescentar evidência.',True),
      ('Exigir biópsia cerebral antes de aceitar etiologia viral.','Não é investigação rotineira para este cenário.',False)],segue='b3'),
    bifurcacao('b3','Decisão','Definição etiológica','Como você prossegue com a sorologia?',[
      caminho('Enviar confirmação por neutralização e manter suporte.','confirmado','A confirmação resolve uma limitação do método sem interromper o cuidado.'),
      caminho('Manter a classificação presuntiva e seguimento clínico.','provavel','É possível manejar a síndrome sem afirmar uma confirmação que não foi obtida.')],fundo=CENA),
    pg('confirmado','Resultado complementar',p('O laboratório de referência informa neutralização compatível com vírus do Nilo Ocidental, sem padrão de neutralização cruzada que explique o resultado. A investigação sustenta doença neuroinvasiva com comprometimento motor.'),p('O exame foi solicitado na decisão anterior. O resultado define a etiologia; não determina quanto da força muscular será recuperado.'),segue='p6'),
    pg('provavel','Avaliação etiológica',p('A associação clínica e sorológica sustenta doença neuroinvasiva provavelmente pelo vírus do Nilo Ocidental. Sem a confirmação complementar, permanece registrada a limitação de reação cruzada.'),segue='p6'),
    pg('indefinido','Avaliação etiológica',p('Neste percurso, a etiologia não foi estabelecida. A documentação permanece como meningoencefalite com paresia flácida assimétrica. O seguimento em neurologia e infectologia inclui reavaliar amostras e exposição, sem registrar um agente confirmado.'),segue='p6'),
    q('p6','O paciente deixa a fase aguda, mas continua com déficit motor. Quais duas afirmações devem orientar o plano de cuidado?',[
      ('Suporte, prevenção de complicações e reabilitação são tratamentos ativos.','A ausência de antiviral específico não significa ausência de cuidado efetivo.',True),
      ('Desaparecimento da febre demonstra recuperação do neurônio motor.','A recuperação funcional pode ser lenta e incompleta.',False),
      ('Imunoglobulina deve ser mantida para qualquer mielite infecciosa.','Benefício não está estabelecido de forma geral; o mecanismo precisa orientar a indicação.',False),
      ('A ausência de confirmação dispensa acompanhamento etiológico.','A incerteza precisa ser registrada e revista.',False),
      ('Deglutição, respiração e capacidade funcional precisam de seguimento.','As necessidades de suporte podem persistir após resolução da infecção aguda.',True)],segue='tratamento'),
    pg('tratamento','Tratamento e seguimento',p('O suporte inclui ventilação conforme necessidade, manejo de secreções, nutrição por via segura, prevenção de trombose e lesão por pressão e mobilização progressiva. Antimicrobianos empíricos são revistos segundo os resultados disponíveis e a evolução, não retirados apenas porque apareceu uma sorologia.'),p('Para Nilo Ocidental, não há terapia específica com benefício conclusivo. Imunoglobulina e corticoide não são apresentados como tratamento comprovado. Neurologia, fisioterapia e fonoaudiologia acompanham recuperação e limitações.'),segue='cuidado_diario'),
    pg('cuidado_diario','Evolução no leito',
       p('Nos períodos acordado, Antônio tenta participar da higiene e escolhe como prefere se comunicar. A perna direita permanece mais fraca; a esquerda consegue ajudar na mudança de posição. A equipe repete o exame motor em condições semelhantes de vigília.'),
       p('A esposa nota que ele se cansa com visitas longas. São combinados períodos de descanso, orientação sobre o ambiente e participação gradual nos cuidados. A melhora do contato não equivale à recuperação da força.'),segue='avaliacao_degluticao'),
    pg('avaliacao_degluticao','Reavaliação funcional',
       p('A necessidade de ajuda para eliminar secreções é revista diariamente. A equipe acompanha tosse, proteção da via aérea e tolerância ao suporte; uma saturação confortável, isoladamente, não responde a essas questões.'),
       p('A família pergunta quando poderá oferecer água. A via de alimentação permanece vinculada à avaliação da deglutição, enquanto fonoaudiologia e fisioterapia acompanham a recuperação. As metas do dia são registradas de forma que o paciente também possa entendê-las.'),segue='imagem_neuronio'),

    pg('imagem_neuronio','Discussão de imagem',
       p('Compare o corpo celular, o axônio e a bainha de mielina. Por que quadros com fraqueza semelhante podem ter tempos de recuperação diferentes?'),
       '<details class="leitura"><summary>Revelar pontos de discussão</summary><p>Bloqueio de condução, perda de mielina e destruição do neurônio não são equivalentes. Localização, extensão e mecanismo da lesão influenciam a recuperação. Uma figura anatômica não prevê o prognóstico individual, e a melhora da febre não comprova recuperação motora.</p></details>',
       lamina_=lamina('neuronio.svg','Neurônio','Diagrama anatômico, sem achados específicos deste caso.','LadyofHats · Wikimedia Commons · domínio público · sem alterações.'),
       conforme=('b2',['pre_reabilitacao','pre_prolongada','pre_prolongada'])),
    pg('pre_reabilitacao','Terceira semana',
       p('Com a redução do suporte, Antônio volta a conversar sobre a casa e pergunta pelo neto. Senta-se na borda do leito com assistência. Ao tentar ficar em pé, a perna direita não sustenta o peso e o movimento é interrompido com apoio da equipe.'),
       p('A família recebe orientação sobre transferências e prevenção de quedas. A alta será articulada com um serviço capaz de continuar a reabilitação; caminhar sozinho ainda não é uma condição presente.'),segue='f_reabilita'),
    pg('pre_prolongada','Internação prolongada',
       p('A retirada do suporte progride mais lentamente. Antônio compreende as orientações nos períodos de vigília, mas precisa de ajuda para se posicionar e eliminar secreções. As sessões de mobilização são ajustadas à tolerância de cada dia.'),
       p('A equipe conversa com a família sobre transferência para cuidados de continuidade. São revistos o suporte respiratório, a via de alimentação e as necessidades de assistência. A persistência do déficit motor impede estabelecer uma data segura para retorno ao domicílio.'),segue='f_longa'),

    fim('f_reabilita','Reabilitação','Na terceira semana está desperto, sem suporte invasivo e com deglutição em recuperação. Continua sem caminhar sozinho. Segue para reabilitação; aos três meses usa auxílio para marcha e mantém fraqueza maior à direita.','O suporte antecipado reduz riscos secundários, mas não garante recuperação da lesão motora. Este é um desfecho ficcional possível.','melhor'),
    fim('f_longa','Internação prolongada','A complicação respiratória prolonga a internação. Necessita de suporte ventilatório e reabilitação por mais tempo. Na transferência, mantém dependência para mobilidade e alimentação por via alternativa.','Aspiração e falência ventilatória podem acrescentar morbidade à lesão neurológica. A duração e a recuperação deste roteiro não são previsões individuais.'),
    fim('f_obito','Evolução desfavorável','A manutenção da estratégia apesar da piora bulbar é seguida, neste ramo simulado, de aspiração grave e parada hipóxica. O paciente não sobrevive. A causa infecciosa não chegou a ser definida neste percurso.','Este ramo ilustra um risco possível do atraso na proteção de via aérea, não uma consequência inevitável nem uma probabilidade estimada.','pior'),
    pg('retrospectiva','Retrospectiva',p('A primeira tarefa era distinguir prostração de déficit motor. Depois, localizar a fraqueza sem separar artificialmente febre, cognição e força. A sorologia só passou a fazer sentido após a evolução e a história de exposição.'),p('O diagnóstico etiológico e o suporte respiratório correm em paralelo: é possível proteger o paciente antes de saber o nome do agente, e é possível nomear o agente sem recuperar a força.')),
    pg('fontes','Procedência e referências',p('Paciente, valores e evoluções são autorais e ficcionais. A cena é uma ilustração gerada por IA, não uma imagem diagnóstica. Os diferentes finais não estimam o efeito causal ou a probabilidade de cada conduta.'),
       '<p><a href="https://www.cdc.gov/west-nile-virus/hcp/diagnosis-testing/index.html" target="_blank" rel="noopener">CDC — diagnóstico</a> · <a href="https://www.cdc.gov/west-nile-virus/hcp/treatment-prevention/index.html" target="_blank" rel="noopener">CDC — tratamento</a></p>',
       '<p><a href="https://wwwnc.cdc.gov/eid/article/9/7/03-0129_article" target="_blank" rel="noopener">Sejvar et al., 2003 — paralisia flácida</a> · <a href="https://www.idsociety.org/practice-guideline/encephalitis" target="_blank" rel="noopener">IDSA — encefalite</a></p>')
]
REVISAO = [dict(chave='Líquor: celularidade, proteína, glicose e Gram',rotulo='Caracterização do líquor',porque='A ausência dessa investigação limitou a diferenciação entre causas infecciosas e pós-infecciosas neste percurso.'),dict(chave='IgM para vírus do Nilo Ocidental em soro e líquor',rotulo='Atribuição etiológica',porque='A hipótese epidemiológica pode orientar testes dirigidos; sem eles, o registro deve preservar a incerteza.')]

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
       p('Um homem de 71 anos procura atendimento com febre, cefaleia difusa e falta de apetite há quatro dias. Naquela manhã precisou apoiar-se nos móveis para chegar ao banheiro. A esposa percebeu respostas mais lentas, mas ele atribuiu isso a uma noite sem dormir.'),
       p('Era independente e caminhava diariamente. Tem hipertensão e diabetes; usa losartana e metformina, sem mudança recente. Não refere tosse, disúria, diarreia ou queda.'),
       lamina_=lamina(CENA,'Admissão','Cena ilustrativa, sem representação de um sinal diagnóstico.',CREDITO)),
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
    pedido('ex1','Investigação inicial','Primeira rodada','Escolha até quatro exames para orientar a avaliação inicial.',[
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
    resultados('res1','Resultados','Primeira rodada','ex1',fundo=CENA),
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
    bifurcacao('b1','Decisão','Conduta inicial','Qual caminho você escolhe diante da reavaliação?',[
      caminho('Internar, colher amostras e iniciar cobertura empírica para meningoencefalite.','r_interna','A coleta é importante, mas não deve atrasar antimicrobianos quando a suspeita é relevante.'),
      caminho('Conduzir como polirradiculoneuropatia e priorizar imunoglobulina.','r_ig','Guillain–Barré é um diferencial, mas febre ativa e encefalopatia tornam insuficiente essa hipótese isolada.'),
      caminho('Manter observação com hidratação antes de ampliar a investigação.','r_observa','A observação sem investigação dirigida pode retardar o reconhecimento da progressão neurológica.')],fundo=CENA),
    pg('r_interna','Primeiro dia',p('O paciente é internado. São iniciados aciclovir e cobertura para meningite bacteriana, incluindo Listeria pela idade, com ajuste à função renal e ao protocolo local. A coleta de amostras e a avaliação de segurança da punção são organizadas sem atrasar o tratamento.'),segue='ex2'),
    pg('r_ig','Primeiro dia',p('A imunoglobulina é iniciada sob a hipótese de polirradiculoneuropatia. Ele mantém febre e confusão e desenvolve tremor de ação. Na revisão conjunta, a equipe amplia a abordagem para meningoencefalite e inicia cobertura empírica. A hipótese inicial será reavaliada, sem esperar resposta imediata à imunoglobulina.'),segue='ex2'),
    pg('r_observa','Primeiro dia',p('Durante a observação, a perna direita passa a apresentar apenas contração, sem movimento e ele se torna mais sonolento. É transferido para internação monitorizada. A equipe de resgate inicia a abordagem empírica de meningoencefalite; os resultados etiológicos ainda dependem da investigação.'),segue='ex2'),
    pedido('ex2','Investigação','Segunda rodada','Escolha até quatro investigações. A punção inclui avaliação de segurança; imagem prévia será obtida se indicada.',[
      grupo('Sistema nervoso','nervo',[
        ex('Líquor: celularidade, proteína, glicose e Gram','86 células/mm³ (58% neutrófilos) · proteína 92 mg/dL · glicose 68 mg/dL, sérica 120 · Gram sem bactérias','Até 5 células · proteína 15–45 · relação glicose >0,4',True),
        ex('Cultura e PCR bacteriana do líquor','Sem crescimento até o momento · painel bacteriano negativo.'),
        ex('PCR para HSV e VZV no líquor','Não detectados em amostra obtida no sexto dia de sintomas.'),
        ex('Ressonância de encéfalo e medula','Sem infarto, compressão medular ou lesão temporal. Ausência de alteração específica não exclui inflamação.'),
        ex('Eletroneuromiografia','Respostas motoras reduzidas, assimétricas; respostas sensitivas preservadas. Sem critérios de desmielinização. Estudo precoce requer correlação clínica.', '—',True),
        ex('Eletroencefalograma','Lentificação difusa, sem atividade epiléptica registrada.')]),
      grupo('Outras hipóteses','geral',[
        ex('HIV Ag/Ac','Não reagente.'),ex('Sífilis: teste treponêmico e VDRL','Não reagentes.'),
        ex('Dengue: NS1 e IgM','Não reagentes.'),ex('Leptospira: PCR','Não detectado.'),
        ex('Amônia','28 µmol/L','11–35'),ex('Cortisol matinal','18 µg/dL','5–25')])],banco=BANCO,limite=4,fundo=CENA),
    resultados('res2','Resultados','Segunda rodada','ex2',fundo=CENA,
      rota={'pediu':['Líquor: celularidade, proteína, glicose e Gram'],'entao':'p3','senao':'sem_lcr'}),
    q('p3','O líquor tem 86 células/mm³, predomínio neutrofílico e glicose preservada. Qual interpretação é a mais adequada?',[
      ('O predomínio neutrofílico comprova meningite bacteriana.','A celularidade inicial de algumas infecções virais também pode ser neutrofílica.',False),
      ('O perfil admite etiologia viral, mas exige avaliação microbiológica.','O conjunto e o momento da coleta pesam mais que um tipo celular isolado.',True),
      ('A glicose preservada permite interromper toda cobertura agora.','Esse valor não exclui isoladamente etiologia bacteriana ou herpes.',False),
      ('Há dissociação albuminocitológica típica de Guillain–Barré.','A pleocitose expressiva exige procurar uma explicação alternativa.',False),
      ('A proteína elevada localiza a lesão no nervo periférico.','A hiperproteinorraquia não fornece essa localização específica.',False)],segue='historia2'),
    pg('sem_lcr','Discussão',p('A equipe ainda não dispõe de caracterização do líquor neste percurso. O diagnóstico permanece sindrômico: doença febril com alteração do estado mental e paresia flácida assimétrica.'),p('As hipóteses infecciosas seguem cobertas empiricamente. A falta de definição não impede monitorização respiratória ou nova avaliação neurológica.'),segue='historia2'),
    pg('historia2','História complementar',p('A esposa relata que voltaram de uma visita familiar ao sul dos Estados Unidos doze dias antes da febre. Ele passava o fim de tarde no quintal, próximo de uma área alagada. Ambos tiveram várias picadas de insetos. Não houve mordida de animal, água de enchente ou consumo de leite não pasteurizado.'),p('No segundo dia de internação, a tosse fica fraca. Ele engasga com água, embora mantenha saturação de 96% em ar ambiente. A avaliação à beira do leito mostra queda da capacidade vital de 24 para 17 mL/kg e piora da força inspiratória.')), 
    bifurcacao('b2','Decisão','Suporte respiratório','Como você conduz essa mudança?',[
      caminho('Transferir para terapia intensiva e proteger a via aérea de forma planejada.','r_via','A progressão bulbar e ventilatória permite antecipar uma via aérea difícil em vez de esperar o colapso.'),
      caminho('Tentar ventilação não invasiva com vigilância intensiva.','r_vni','Uma tentativa exige seleção e critérios precoces de falha; disfagia e secreções reduzem a margem de segurança.'),
      caminho('Manter oxigênio e vigilância na enfermaria enquanto investiga.','r_atraso','A saturação não mede adequadamente a reserva ventilatória nem a proteção contra aspiração.')],fundo=CENA),
    pg('r_via','Terceiro dia',p('É intubado de forma planejada por progressão da disfunção bulbar e fraqueza ventilatória. Não há aspiração reconhecida. A febre começa a ceder, mas a paresia permanece. O suporte permite continuar a investigação.'),segue='p4'),
    pg('r_vni','Reavaliação respiratória',p('Com ventilação não invasiva, acumula secreções e não consegue expectorar. Mantém episódios de engasgo. A oxigenação segue preservada, mas a proteção da via aérea piora.'),segue='b_resgate'),
    pg('r_atraso','Reavaliação respiratória',p('Na enfermaria, apresenta engasgo seguido de aumento do esforço respiratório. É levado à sala de emergência. O cenário agora exige decidir sobre proteção da via aérea e suporte intensivo.'),segue='b_resgate'),
    bifurcacao('b_resgate','Decisão','Reavaliação da conduta','Diante da falha de eliminação de secreções, qual é a próxima conduta?',[
      caminho('Interromper a estratégia inicial e realizar intubação.','r_resgate','A mudança de plano é uma resposta à evolução, não precisa esperar falência completa.'),
      caminho('Prolongar o suporte não invasivo e reavaliar após a investigação.','f_obito','A incapacidade de proteger a via aérea torna perigoso adiar o suporte invasivo.')],fundo=CENA),
    pg('r_resgate','Quarto dia',p('Após intubação de resgate, necessita de suporte ventilatório prolongado. O episódio de aspiração motiva investigação e tratamento de complicação pulmonar. A fraqueza assimétrica continua presente quando a sedação é reduzida.'),segue='p4'),
    q('p4','A saturação está preservada, mas há disfagia, tosse fraca e queda seriada da capacidade vital. Quais duas medidas são prioritárias?',[
      ('Suspender ingestão oral até avaliar a deglutição.','A disfunção bulbar aumenta o risco de aspiração.',True),
      ('Aguardar dessaturação para solicitar avaliação intensiva.','A oximetria pode permanecer normal durante a deterioração ventilatória.',False),
      ('Reavaliar somente pela gasometria após oferecer oxigênio.','Oxigênio não corrige falência da bomba respiratória.',False),
      ('Acionar terapia intensiva e planejar proteção de via aérea.','Tendência funcional, tosse e proteção da via aérea orientam a intervenção.',True),
      ('Manter líquidos por via oral para fluidificar secreções.','A disfagia exige avaliação antes de manter essa via.',False)],segue='ex3'),
    pedido('ex3','Investigação','Terceira rodada','A viagem e a evolução ampliam a investigação. Escolha até quatro exames.',[
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
    pg('tratamento','Tratamento e seguimento',p('O suporte inclui ventilação conforme necessidade, manejo de secreções, nutrição por via segura, prevenção de trombose e lesão por pressão e mobilização progressiva. Antimicrobianos empíricos são revistos segundo os resultados disponíveis e a evolução, não retirados apenas porque apareceu uma sorologia.'),p('Para Nilo Ocidental, não há terapia específica com benefício conclusivo. Imunoglobulina e corticoide não são apresentados como tratamento comprovado. Neurologia, fisioterapia e fonoaudiologia acompanham recuperação e limitações.'),conforme=('b2',['f_reabilita','f_longa','f_longa'])),
    fim('f_reabilita','Reabilitação','Na terceira semana está desperto, sem suporte invasivo e com deglutição em recuperação. Continua sem caminhar sozinho. Segue para reabilitação; aos três meses usa auxílio para marcha e mantém fraqueza maior à direita.','O suporte antecipado reduz riscos secundários, mas não garante recuperação da lesão motora. Este é um desfecho ficcional possível.','melhor'),
    fim('f_longa','Internação prolongada','A complicação respiratória prolonga a internação. Necessita de suporte ventilatório e reabilitação por mais tempo. Na transferência, mantém dependência para mobilidade e alimentação por via alternativa.','Aspiração e falência ventilatória podem acrescentar morbidade à lesão neurológica. A duração e a recuperação deste roteiro não são previsões individuais.'),
    fim('f_obito','Evolução desfavorável','A manutenção da estratégia apesar da piora bulbar é seguida, neste ramo simulado, de aspiração grave e parada hipóxica. O paciente não sobrevive. A causa infecciosa não chegou a ser definida neste percurso.','Este ramo ilustra um risco possível do atraso na proteção de via aérea, não uma consequência inevitável nem uma probabilidade estimada.','pior'),
    pg('retrospectiva','Retrospectiva',p('A primeira tarefa era distinguir prostração de déficit motor. Depois, localizar a fraqueza sem separar artificialmente febre, cognição e força. A sorologia só passou a fazer sentido após a evolução e a história de exposição.'),p('O diagnóstico etiológico e o suporte respiratório correm em paralelo: é possível proteger o paciente antes de saber o nome do agente, e é possível nomear o agente sem recuperar a força.')),
    pg('fontes','Procedência e referências',p('Paciente, valores e evoluções são autorais e ficcionais. A cena é uma ilustração gerada por IA, não uma imagem diagnóstica. Os diferentes finais não estimam o efeito causal ou a probabilidade de cada conduta.'),
       '<p><a href="https://www.cdc.gov/west-nile-virus/hcp/diagnosis-testing/index.html" target="_blank" rel="noopener">CDC — diagnóstico</a> · <a href="https://www.cdc.gov/west-nile-virus/hcp/treatment-prevention/index.html" target="_blank" rel="noopener">CDC — tratamento</a></p>',
       '<p><a href="https://wwwnc.cdc.gov/eid/article/9/7/03-0129_article" target="_blank" rel="noopener">Sejvar et al., 2003 — paralisia flácida</a> · <a href="https://www.idsociety.org/practice-guideline/encephalitis" target="_blank" rel="noopener">IDSA — encefalite</a></p>')
]
REVISAO = [dict(chave='Líquor: celularidade, proteína, glicose e Gram',rotulo='Caracterização do líquor',porque='A ausência dessa investigação limitou a diferenciação entre causas infecciosas e pós-infecciosas neste percurso.'),dict(chave='IgM para vírus do Nilo Ocidental em soro e líquor',rotulo='Atribuição etiológica',porque='A hipótese epidemiológica pode orientar testes dirigidos; sem eles, o registro deve preservar a incerteza.')]

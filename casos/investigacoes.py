"""Questões de priorização diagnóstica; a equipe realiza os exames prioritários.

As alternativas são conjuntos clinicamente coerentes, não um catálogo livre.
O comentário avalia a prioridade no cenário, não uma proibição universal.
"""
from motor.etapas import texto

def alternativa(t, exames, c, ok=False, situacao='Menor prioridade'):
    return dict(t=texto(t), exames=exames.split('|'), c=texto(c), ok=ok,
                situacao='Mais indicado agora' if ok else situacao)

def aplicar(etapas, especificacoes):
    por_id={e['k']:e for e in etapas}
    for k,enunciado,itens in especificacoes:
        e=por_id[k]
        disponiveis={o['e'] for g in e['grupos'] for o in g['o']}
        usados=[n for a in itens for n in a['exames']]
        assert set(usados)<=disponiveis,(k,set(usados)-disponiveis)
        assert len(usados)==len(set(usados)),(k,'exame repetido entre alternativas')
        assert 1<=sum(a['ok'] for a in itens)<len(itens)
        e.update(comentado=True, alts=itens, escolhas=sum(a['ok'] for a in itens),
                 enunciado=texto(enunciado),
                 tr='A equipe realiza os exames mais indicados; sua resposta fica registrada para a discussão')

A=alternativa
ESPECIFICACOES={
'pulmao_rim':[
('ex_amb','Os sintomas nasais persistem, com febre baixa e perda de peso apesar do tratamento. Quais três conjuntos acrescentam mais informação para distinguir doença localizada de um processo sistêmico?',[
 A('Hemograma e proteína C reativa','Hemoglobina|Leucócitos|Plaquetas|Proteína C reativa','Buscam anemia, alterações celulares e inflamação. Nenhum desses achados, isoladamente, define a causa.',True),
 A('TSH e glicemia de jejum','TSH|Glicemia de jejum','Podem esclarecer causas de cansaço e perda ponderal, mas não são a primeira forma de integrar febre e sintomas inflamatórios persistentes.'),
 A('Creatinina e exame do sedimento urinário','Creatinina|Sedimento urinário','Rastreiam lesão renal que pode ser silenciosa. O objetivo é procurar outro órgão acometido, sem pressupor o mecanismo.',True),
 A('Espirometria e eletrocardiograma','Espirometria|Eletrocardiograma','Ganham valor com sintomas respiratórios funcionais ou cardíacos; não esclarecem primeiro a combinação apresentada.'),
 A('Radiografia de tórax','Radiografia de tórax','Procura alterações torácicas associadas ao quadro constitucional, inclusive infecciosas. Um exame normal não encerra a investigação.',True),
 A('Tomografia de seios da face e ultrassom renal','Tomografia de seios da face|Ultrassonografia de rins e vias urinárias','A tomografia pode ser útil na doença nasal persistente; o ultrassom renal depende da avaliação inicial. O conjunto não substitui o rastreio sistêmico.',situacao='Indicação dirigida'),
]),
('ex_adm','Dispneia, sangue no escarro e oligúria surgiram durante a evolução. Quais três conjuntos melhor caracterizam a gravidade e os mecanismos possíveis, em paralelo à estabilização?',[
 A('D-dímero e angiotomografia de tórax','D-dímero|Angiotomografia de tórax','Cabem se a avaliação sustentar embolia. D-dímero elevado em doença inflamatória não estabelece essa indicação.',situacao='Depende da probabilidade clínica'),
 A('Creatinina, potássio e sedimento urinário','Creatinina|Potássio|Sedimento urinário','Avaliam lesão renal, risco eletrolítico e origem do sangramento urinário. A tendência da creatinina importa mais que uma estimativa isolada de filtração.',True),
 A('Hemoglobina, gasometria e radiografia de tórax','Hemoglobina|pH arterial|Relação PaO2/FiO2|Radiografia de tórax','Relacionam anemia, troca gasosa e padrão radiológico. São dados complementares; nenhum deles identifica sozinho o conteúdo dos alvéolos.',True),
 A('Hemoculturas','Hemocultura','Investigam infecção sistêmica antes de ampliar o tratamento. A coleta não deve atrasar antimicrobianos nem a estabilização.',True),
 A('Sorologias para HIV e hepatite B','Anti-HIV|HBsAg e anti-HBc','Podem integrar a investigação e o preparo terapêutico, mas não esclarecem primeiro a deterioração respiratória e renal.'),
 A('Ecocardiograma e albumina','Ecocardiograma transtorácico|Albumina','Ajudam se houver suspeita de congestão cardíaca ou redução da pressão oncótica. Não substituem a avaliação imediata da anemia e da função renal.',situacao='Indicação dirigida'),
]),
('ex_mec','A evolução respiratória e renal não ficou esclarecida pela abordagem inicial. Quais três estratégias têm maior potencial de distinguir mecanismos e orientar o tratamento?',[
 A('Ferritina, VHS e eletroforese de proteínas','Ferritina|VHS|Eletroforese de proteínas','Podem ampliar diferenciais, mas marcadores inflamatórios inespecíficos não distinguem primeiro os mecanismos que ameaçam os órgãos.'),
 A('ANCA com especificidade MPO/PR3 e anti-MBG','ANCA por imunofluorescência indireta|Anti-mieloperoxidase|Anti-proteinase 3|Anticorpo anti-membrana basal glomerular','Investigam causas distintas de lesão capilar. A sorologia precisa ser integrada à clínica e ao tecido; positividade não equivale a diagnóstico isolado.',True),
 A('Eosinofilúria e urocultura','Eosinofilúria|Urocultura','Urocultura responde à suspeita de infecção urinária; eosinofilúria não discrimina bem nefrite intersticial. Nenhuma explica, por si, o conjunto respiratório e renal.'),
 A('Complemento C3/C4 e anti-DNA nativo','Complemento C3|Complemento C4|Anti-DNA nativo','Acrescentam evidência sobre mecanismos por imunocomplexos. Resultados normais ou negativos modificam a probabilidade, sem excluir todas as causas.',True),
 A('Sedimento, quantificação de proteína e biópsia renal se segura','Sedimento urinário|Relação proteína/creatinina urinária|Biópsia renal','Confirma-se primeiro a indicação renal e avalia-se a segurança. A biópsia distingue padrões; em deterioração rápida, não deve atrasar tratamento necessário.',True),
 A('Galactomanana, beta-D-glucana e pesquisa de Pneumocystis','Galactomanana e beta-D-glucana|Pesquisa de Pneumocystis no lavado','O rendimento depende de imunossupressão, exposição e padrão pulmonar. Não constituem um painel inicial universal para esta associação.',situacao='Depende de risco infeccioso'),
])],
'west_nile':[
('ex1','A febre e a cefaleia acompanham lentificação recente e dificuldade para caminhar. Quais três conjuntos você prioriza enquanto repete o exame neurológico e avalia investigação do sistema nervoso?',[
 A('TSH e vitamina B12','TSH|Vitamina B12','Investigam causas habitualmente mais crônicas. Não explicam primeiro uma mudança cognitiva associada a febre de poucos dias.'),
 A('Glicemia, eletrólitos e função renal','Glicemia|Eletrólitos e função renal','Procuram causas reversíveis de disfunção cerebral e orientam tratamento. Alteração discreta não deve encerrar a investigação.',True),
 A('Creatinoquinase','Creatinoquinase','É útil quando há suspeita de lesão muscular. A dificuldade para andar ainda requer localização; o exame não esclarece a alteração cognitiva.'),
 A('Hemograma','Hemograma','Avalia células sanguíneas e plaquetas, compondo a avaliação de gravidade e a segurança de procedimentos. Não separa sozinho infecção viral de bacteriana.',True),
 A('Urina tipo 1 e radiografia de tórax','Urina tipo 1|Radiografia de tórax','Procuram focos extracranianos conforme sinais e exame físico. Mesmo um achado positivo pode não explicar o déficit neurológico.',situacao='Pesquisa de foco dirigida'),
 A('Hemoculturas','Hemoculturas iniciais','Podem identificar infecção invasiva antes dos antimicrobianos. A coleta não deve retardar tratamento nem a investigação neurológica.',True),
]),
('ex2','Persistem febre e confusão; agora se documentam paresia assimétrica, hiporreflexia e sensibilidade preservada. Quais três estratégias melhor investigam essa combinação?',[
 A('Líquor com análise celular, bioquímica e microbiológica','Líquor: celularidade, proteína, glicose e Gram|Cultura e PCR bacteriana do líquor|PCR para HSV e VZV no líquor','Avalia inflamação e agentes tratáveis. O déficit focal exige avaliar imagem e segurança antes da punção, sem atrasar a cobertura empírica.',True),
 A('Amônia e cortisol matinal','Amônia|Cortisol matinal','Têm indicação com suspeitas metabólicas específicas. Não são os exames mais discriminantes para déficit focal com meningismo.'),
 A('Ressonância de encéfalo e medula','Ressonância de encéfalo e medula','Procura lesões encefálicas e medulares, além de causas estruturais. Exame sem alteração específica não exclui inflamação.',True),
 A('Sorologias para HIV e sífilis','HIV Ag/Ac|Sífilis: teste treponêmico e VDRL','Podem integrar a investigação etiológica, mas não substituem o estudo inicial dos compartimentos neurológicos envolvidos.',situacao='Complementares'),
 A('Eletroneuromiografia','Eletroneuromiografia','Ajuda a distinguir comprometimento motor axonal de desmielinização e de doença muscular. O tempo de evolução limita a interpretação precoce.',True),
 A('Eletroencefalograma','Eletroencefalograma','É útil para crises não convulsivas e alteração de consciência persistente. Isoladamente, não localiza nem explica a paresia flácida.',situacao='Complementar'),
]),
('ex3','A investigação passa a considerar exposição vetorial e comprometimento motor persistente. Quais duas estratégias têm maior rendimento para avançar na etiologia e na localização?',[
 A('Anticorpos de encefalite autoimune e anti-GM1','Anticorpos de encefalite autoimune|Anticorpos anti-GM1','São direcionados por fenótipos específicos. Painéis negativos não excluem essas doenças, e não substituem a investigação infecciosa compatível.',situacao='Segunda linha dirigida'),
 A('Porfobilinogênio urinário e cobre sérico','Porfobilinogênio urinário|Cobre sérico','Ganham valor em síndromes específicas, como crises neuroviscerais ou mielopatia carencial. O curso febril atual não os coloca à frente.'),
 A('Sorologia para Nilo Ocidental e Saint Louis','IgM para vírus do Nilo Ocidental em soro e líquor|Sorologia para encefalite de Saint Louis','O contexto justifica pesquisar flavivírus. IgM pode apresentar reação cruzada; eventual positividade exige interpretação e, quando indicada, neutralização.',True),
 A('Repetir a PCR para HSV no líquor','Nova PCR para HSV no líquor','Cabe se a suspeita de herpes permanece alta, especialmente após amostra muito precoce. A primeira coleta e o fenótipo orientam essa decisão.',situacao='Se persistir suspeita de HSV'),
 A('Repetir a eletroneuromiografia','Nova eletroneuromiografia','O intervalo permite caracterizar melhor a distribuição do déficit e a denervação. Esclarece a localização, mas não identifica o vírus.',True),
 A('Pesquisa de malária e vírus rábico','Pesquisa de malária|Pesquisa de vírus rábico em laboratório de referência','São investigações dependentes de exposição e epidemiologia. Não devem ser agrupadas como rastreio indiscriminado.',situacao='Depende da exposição'),
])],
'cocaina_levamisol':[
('p1','Febre e placas dolorosas não branqueáveis podem ter mecanismos diferentes. Quais três conjuntos você prioriza para avaliar risco sistêmico e orientar a abordagem inicial?',[
 A('Hemograma diferencial e esfregaço','Hemograma diferencial|Esfregaço periférico','Avaliam neutrófilos, plaquetas e morfologia. Citopenias mudam a urgência; não se deve deduzir o mecanismo da púrpura apenas pela aparência.',True),
 A('Doppler arterial de pernas','Doppler arterial de pernas','Investiga oclusão de grandes vasos se houver sinais de isquemia. Pulsos preservados e lesões cutâneas não tornam esse o primeiro exame discriminante.'),
 A('Hemoculturas e lactato','Hemoculturas iniciais|Lactato','Buscam infecção invasiva e repercussão perfusional. Lactato normal não exclui infecção; coletas não devem atrasar antibiótico quando indicado.',True),
 A('Radiografia de tórax','Radiografia de tórax','É direcionada por suspeita de foco pulmonar e contexto clínico. Não explica primeiro as lesões sem manifestações respiratórias.',situacao='Pesquisa de foco dirigida'),
 A('Coagulograma, creatinina e urina','Coagulograma|Creatinina inicial|Urina inicial','Procuram coagulopatia e acometimento renal. Esses dados ajudam a separar uma lesão restrita à pele de comprometimento sistêmico.',True),
 A('Proteína C reativa','Proteína C reativa','Pode acompanhar inflamação, mas não distingue infecção, toxicidade ou mecanismo imune. Não substitui os conjuntos acima.'),
]),
('p2','As lesões mudaram e surgiu urina escura. Quais três estratégias melhor distinguem o mecanismo cutâneo e o possível acometimento renal?',[
 A('Crioglobulinas e complemento','Crioglobulinas|Complemento C3','Investigam um mecanismo por imunocomplexos, sobretudo com contexto compatível. São complementares, sem substituir urina e análise do tecido.',situacao='Complementares'),
 A('Biópsia de uma lesão cutânea adequada','Biópsia cutânea','Amostra de lesão representativa permite distinguir trombose e inflamação vascular. O achado precisa ser integrado à evolução e às exposições.',True),
 A('Anticardiolipina IgG isolada','Anticardiolipina IgG','Um resultado isolado não estabelece síndrome antifosfolípide nem explica automaticamente as placas. A hipótese requer critérios clínicos e laboratoriais.'),
 A('Creatinina e sedimento urinário','Creatinina de reavaliação|Sedimento urinário','Verificam se há lesão renal e sinais de origem glomerular. Urina escura, sem essa caracterização, não basta.',True),
 A('Teste combinado para HIV','Antígeno e anticorpos HIV','Pode integrar a avaliação etiológica e o preparo terapêutico. Não é o exame mais direto para caracterizar agora pele e rim.',situacao='Complementar'),
 A('ANCA, anti-MPO e anti-PR3','ANCA por imunofluorescência|Anti-MPO|Anti-PR3','A associação de pele e possível lesão renal justifica a pesquisa. Reatividade não define sozinha uma doença primária nem exclui causa secundária.',True),
]),
('p3','A história de exposição foi complementada e a queixa urinária persiste. Quais três estratégias acrescentam informação para a decisão terapêutica?',[
 A('Toxicologia urinária dirigida','Benzoilecgonina urinária|Levamisol urinário por LC-MS/MS','Documenta exposição quando a janela de detecção permite. Levamisol negativo em amostra tardia não afasta exposição prévia.',True),
 A('Novas hemoculturas','Novas hemoculturas','Repetição é orientada por febre persistente, instabilidade ou suspeita de foco. Coletas sob antibiótico também têm sensibilidade reduzida.',situacao='Se houver indicação infecciosa'),
 A('Creatinina, proteinúria e biópsia renal se segura','Creatinina atual|Relação proteína/creatinina urinária|Biópsia renal','Quantificam lesão e definem o padrão renal quando há indicação. A necessidade de tratamento depende da gravidade, não apenas da história de exposição.',True),
 A('Cultura de tecido cutâneo','Cultura de tecido cutâneo','É útil se houver suspeita de infecção da lesão. Não caracteriza sozinha lesão trombótica ou imune.',situacao='Se houver suspeita de infecção'),
 A('Hemograma de controle','Hemograma de controle','Acompanha recuperação ou persistência da neutropenia, informação necessária para avaliar risco infeccioso e planejar tratamento.',True),
 A('Anticorpo anti-MBG','Anti-MBG','Pode investigar outra causa de lesão glomerular, sobretudo com manifestações pulmonares. Não é a principal forma de investigar a associação descrita.',situacao='Diferencial dirigido'),
])]

}

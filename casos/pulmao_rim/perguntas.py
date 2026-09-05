"""Perguntas do caso pulmão-rim.

Cada pergunta é escrita uma vez e gera os dois slides — a escolha e a resposta
comentada. A letra anunciada é calculada a partir de quem tem `certa=True`, e o
texto da alternativa é o mesmo objeto nos dois slides: não há como divergirem.

Regra editorial: 4 ou 5 alternativas, 1 ou 2 corretas, coluna única. O enunciado
começa pelo dado e termina pelo pedido. A pergunta 1 nunca lista as hipóteses
diagnósticas — a lista é o destino, não o ponto de partida.
"""

from motor.perguntas import alt, pergunta


P1 = pergunta(
    1,
    "Que estrutura anatômica é compartilhada pelos territórios acometidos?",
    [
        alt(
            "A drenagem linfática regional que os conecta",
            "Pulmão e rim drenam para cadeias linfáticas distintas, e a "
            "pele e o nervo periférico não compartilham nenhuma delas.",
        ),
        alt(
            "O território de uma única artéria de médio calibre",
            "Vasculites de médio calibre, como a poliarterite nodosa, "
            "produzem aneurismas e infartos segmentares. Elas não causam "
            "glomerulonefrite nem capilarite alveolar.",
        ),
        alt(
            "A mesma origem embriológica dos epitélios",
            "Pulmão e rim têm origens embriológicas diferentes. A "
            "coincidência aqui é funcional, não embriológica.",
        ),
        alt(
            "Os vasos de pequeno calibre",
            "O capilar glomerular e o capilar alveolar têm a mesma "
            "arquitetura básica: parede finíssima apoiada em membrana "
            "basal, submetida a pressão. Uma agressão a esse "
            "compartimento aparece nos dois órgãos ao mesmo tempo, e "
            "também na pele e no vasa nervorum.", certa=True,
        ),
        alt(
            "A inervação autonômica que compartilham",
            "A inervação não explica lesão tecidual simultânea em quatro "
            "territórios.",
        ),
    ],
    ordem=[0, 1, 2, 4, 3],
    titulo_resposta="Quatro territórios, um só compartimento vascular",
)

P2 = pergunta(
    2,
    "O paciente está no pronto-socorro há quarenta minutos. Qual exame muda "
    "a sua conduta ainda nesta hora?",
    [
        alt(
            "Espirometria com medida da difusão de monóxido de carbono",
            "A difusão aumenta na hemorragia alveolar e é um dado elegante. Um "
            "paciente com saturação de 88% e dispneia em repouso não consegue "
            "executar a manobra, e o resultado não chegaria nesta hora.",
        ),
        alt(
            "Sedimento urinário com pesquisa de dismorfismo e de cilindros",
            "É o único exame desta lista que fica pronto em minutos, custa "
            "quase nada e responde à pergunta que separa dois mundos: o "
            "sangramento vem do glomérulo ou do trato urinário? Depende de "
            "urina fresca e de alguém disposto a olhar no microscópio.",
            certa=True,
        ),
        alt(
            "Angiotomografia de tórax em busca de tromboembolismo pulmonar",
            "A hemoptise levanta a suspeita, mas o quadro tem oito semanas, "
            "cursa com anemia e o infiltrado é difuso e bilateral. Não é "
            "apresentação embólica, e o contraste custa caro num rim que já "
            "está caindo.",
        ),
        alt(
            "Painel sorológico completo para doenças autoimunes",
            "As sorologias serão pedidas, e algumas delas decidirão o "
            "tratamento — mas nenhuma volta nesta hora. Pedir tudo de uma vez "
            "não é a mesma coisa que saber o que fazer enquanto se espera.",
        ),
        alt(
            "Ecocardiograma transtorácico com janela para vegetação",
            "Faz falta mais adiante, quando for preciso julgar uma das "
            "hipóteses da lista. Não muda nada nos próximos sessenta minutos.",
        ),
    ],
    ordem=[1, 0, 2, 3, 4],
    titulo_resposta="O exame que responde antes de a sorologia voltar",
)

P3 = pergunta(
    3,
    "O sedimento mostra cilindros hemáticos. O que isso permite afirmar?",
    [
        alt(
            "Que há sangramento em algum ponto do trato urinário",
            "É verdade, mas insuficiente. Cálculo, tumor e infecção "
            "também sangram, e nenhum deles produz cilindro.",
        ),
        alt(
            "Que existe infecção urinária associada",
            "Cilindro leucocitário sugere nefrite intersticial ou "
            "pielonefrite. O cilindro hemático não informa nada sobre "
            "infecção.",
        ),
        alt(
            "Que o sangramento é glomerular",
            "O cilindro se forma dentro do túbulo, a partir de hemácias "
            "que atravessaram a parede do glomérulo e ficaram "
            "aprisionadas na matriz de proteína de Tamm-Horsfall. Nenhuma "
            "outra topografia produz esse achado.", certa=True,
        ),
        alt(
            "Que a proteinúria tem origem tubular",
            "A origem da proteinúria se avalia por eletroforese urinária "
            "ou pela relação entre proteínas de baixo e alto peso "
            "molecular, não pelo cilindro.",
        ),
    ],
    ordem=[0, 1, 3, 2],
    titulo_resposta="Cilindro hemático localiza o sangramento no glomérulo",
)

P4 = pergunta(
    4,
    "O C3 e o C4 vieram normais. Que diagnósticos isso torna menos "
    "prováveis?",
    [
        alt(
            "Nefropatia por IgA e síndrome de Alport",
            "As duas cursam com complemento normal, de modo que o "
            "resultado não as afasta. Elas saem da lista por outros "
            "motivos.",
        ),
        alt(
            "Endocardite infecciosa e nefrite pós-infecciosa",
            "Ao contrário: são justamente duas das causas que CONSOMEM "
            "complemento, e o resultado normal argumenta contra elas — não a "
            "favor. Vale conferir a direção da inferência antes de marcar.",
        ),
        alt(
            "Nenhum; o complemento não discrimina nesta situação",
            "Discrimina, e é uma das poucas bifurcações baratas da "
            "investigação da glomerulonefrite.",
        ),
        alt(
            "Lúpus e crioglobulinemia",
            "Ambas lesam o glomérulo por deposição de imunocomplexos, e o "
            "consumo de complemento faz parte do mecanismo. A "
            "crioglobulinemia consome C4 de forma particularmente "
            "marcante.", certa=True,
        ),
    ],
    ordem=[0, 3, 1, 2],
    titulo_resposta="O complemento separa quem consome de quem não consome",
)

P5 = pergunta(
    5,
    "O que, no lavado broncoalveolar, comprova hemorragia alveolar?",
    [
        alt(
            "Cultura positiva no lavado",
            "Indica infecção, que é justamente o diagnóstico que se quer "
            "afastar antes de imunossuprimir.",
        ),
        alt(
            "Alíquotas sequencialmente mais hemorrágicas",
            "Sangue que vem do alvéolo aumenta a cada alíquota. Sangue de "
            "um ponto do brônquio se dilui e clareia.", certa=True,
        ),
        alt(
            "Coágulo aderido a um brônquio segmentar",
            "Aponta para sangramento localizado de via aérea, não para "
            "capilarite difusa.",
        ),
        alt(
            "Hemossiderófagos em mais de 20% dos macrófagos",
            "O macrófago precisa de 48 a 72 horas para digerir a "
            "hemoglobina e acumular hemossiderina. A presença deles data "
            "o sangramento.", certa=True,
        ),
        alt(
            "Predomínio de neutrófilos na contagem diferencial",
            "Achado inespecífico, presente em infecção, aspiração e "
            "inflamação de qualquer causa.",
        ),
    ],
    ordem=[0, 2, 1, 4, 3],
    titulo_resposta="Dois achados, e cada um diz uma coisa diferente",
)

P6 = pergunta(
    6,
    "A microscopia óptica mostra crescentes celulares. O que a "
    "imunofluorescência acrescenta?",
    [
        alt(
            "Quantifica a fibrose intersticial e o grau de cronicidade",
            "Isso se avalia na microscopia óptica, com colorações para "
            "tecido conjuntivo.",
        ),
        alt(
            "Define a classe histológica de Berden pelo padrão glomerular",
            "A classificação de Berden é morfológica, e se estabelece "
            "contando glomérulos normais, com crescentes e escleróticos "
            "na microscopia óptica.",
        ),
        alt(
            "Separa os três mecanismos possíveis de lesão glomerular",
            "As três produzem crescentes idênticos na óptica. A "
            "imunofluorescência mostra ausência de depósitos na "
            "pauci-imune, depósito linear ao longo da membrana basal na "
            "anti-MBG, e depósitos granulosos nas mediadas por "
            "imunocomplexos.", certa=True,
        ),
        alt(
            "Estima a probabilidade de recuperar a função renal com tratamento",
            "Quem estima isso é a proporção entre lesão ativa e lesão "
            "crônica, também na microscopia óptica.",
        ),
    ],
    ordem=[2, 0, 1, 3],
    titulo_resposta="A imunofluorescência separa mecanismos, não gradua lesão",
)

P7 = pergunta(
    7,
    "Quais são as duas peças que compõem a indução de remissão?",
    [
        alt(
            "Azatioprina",
            "É droga de manutenção. Usada para induzir, é lenta demais "
            "para um rim que está perdendo glomérulos por semana.",
        ),
        alt(
            "Glicocorticoide",
            "Controla a inflamação em horas a dias. O braço de dose "
            "reduzida do PEXIVAS mostrou eficácia semelhante à dose alta, "
            "com menos infecção grave.", certa=True,
        ),
        alt(
            "Metotrexato",
            "Tem lugar na doença limitada, sem acometimento renal. Com "
            "creatinina de 3,8 mg/dL está contraindicado.",
        ),
        alt(
            "Rituximabe ou ciclofosfamida",
            "Eficácia equivalente na indução, nos ensaios RAVE e "
            "RITUXVAS. O rituximabe é preferido em jovens, na recidiva e "
            "quando a preservação da fertilidade importa.", certa=True,
        ),
        alt(
            "Plasmaférese",
            "É uma medida adicional em situações selecionadas, não um "
            "componente da indução. E retira anticorpo sem desligar a "
            "produção.",
        ),
    ],
    ordem=[0, 1, 2, 3, 4],
    titulo_resposta="A indução tem duas peças, e nenhuma delas é opcional",
)

P8 = pergunta(
    8,
    "Anti-MBG não reagente, creatinina de 3,8 mg/dL e hemorragia alveolar com "
    "saturação de 88%. Qual dessas situações **impõe** plasmaférese, e não "
    "apenas a considerar?",
    [
        alt(
            "Toda glomerulonefrite crescêntica, pela gravidade da lesão",
            "Indicação indiscriminada foi justamente o que o PEXIVAS derrubou: "
            "704 pacientes, sem redução do desfecho composto de morte ou "
            "doença renal terminal (28,4% contra 31,0%).",
        ),
        alt(
            "Creatinina acima de 3,4 mg/dL, como a deste paciente",
            "É gatilho para **considerar**, e o limiar não desapareceu: ele "
            "baixou. O KDIGO de 2021 falava em 5,7 mg/dL; o de 2024 desceu "
            "para 3,4. Este paciente preenche — mas preencher um gatilho de "
            "'considerar' não é o mesmo que ter indicação imposta.",
        ),
        alt(
            "Hemorragia alveolar difusa com hipoxemia",
            "Também é gatilho para considerar, e é onde as sociedades "
            "divergem de verdade: o KDIGO 2024 manda considerar, o ACR/VF "
            "2021 recomenda condicionalmente contra o acréscimo de rotina. "
            "Divergência não é desatualização de um dos lados.",
        ),
        alt(
            "Sobreposição com doença anti-membrana basal glomerular",
            "É a única das quatro em que a diretriz diz **acrescentar**, e não "
            "considerar. Neste paciente o anti-MBG veio não reagente, de modo "
            "que ela não se aplica — e é por isso que o anti-MBG é pedido "
            "junto com o ANCA, e não depois dele.",
            certa=True,
        ),
    ],
    titulo_resposta="Considerar não é o mesmo que acrescentar",
    ordem=[1, 3, 0, 2],
)


P9 = pergunta(
    9,
    "Quinto dia de indução: febre de 38,9 °C, 620 neutrófilos, "
    "procalcitonina de 0,4 para 3,1. Qual a primeira conduta?",
    [
        alt(
            "Intensificar a imunossupressão, presumindo atividade da "
            "vasculite",
            "A doença pode estar ativa, e às vezes está. Mas "
            "imunossuprimir mais no momento em que a procalcitonina "
            "saltou e os neutrófilos caíram inverte a ordem das "
            "prioridades.",
        ),
        alt(
            "Aguardar 24 horas e reavaliar",
            "Com hipotensão, hipoxemia e neutropenia, a espera é uma "
            "decisão com consequência.",
        ),
        alt(
            "Suspender o glicocorticoide",
            "A retirada abrupta em quem recebeu pulso produz "
            "insuficiência adrenal e não trata a infecção.",
        ),
        alt(
            "Colher culturas e iniciar antibiótico de amplo espectro",
            "Neutropenia febril em quem recebeu ciclofosfamida há cinco "
            "dias é infecção até prova em contrário. As culturas são "
            "colhidas antes, mas a primeira dose não espera o resultado.", certa=True,
        ),
    ],
    ordem=[0, 1, 2, 3],
    titulo_resposta="Nem toda piora sob tratamento é a doença piorando",
)


# ─────────────────────── perguntas de decisão ───────────────────────
#
# As nove primeiras cobrem o diagnóstico. Estas três cobrem as decisões que o
# interno e o residente vão de fato tomar, e que o caso respondia sozinho em
# caixas — resposta de pergunta que nunca foi feita.

P10 = pergunta(
    10,
    "O lavado está estéril, as sorologias específicas não voltaram e a "
    "creatinina segue subindo — está em <<creatinina>>, com <<horas>> de "
    "internação. Começa a imunossupressão hoje?",
    [
        alt(
            "Não: sem sorologia e sem biópsia, tratar é tratar às cegas",
            "Rigor que custa néfron. A glomerulonefrite rapidamente progressiva "
            "perde função em dias, e a janela de recuperação fecha junto. "
            "Esperar o laudo de uma biópsia que ainda vai ser marcada não é "
            "prudência, é adiamento.",
        ),
        alt(
            "Sim: pulso de glicocorticoide agora, e o resto quando os "
            "resultados chegarem",
            "É a conduta defensável. O pulso é reversível, cobre as três "
            "hipóteses que sobraram, e o que ele muda na biópsia feita nos "
            "dias seguintes é pequeno. O que não se pode antecipar é o "
            "imunossupressor de manutenção, que decide o resto do ano.",
            certa=True,
        ),
        alt(
            "Sim: pulso de glicocorticoide e rituximabe, para não perder tempo",
            "Antecipa demais. O rituximabe compromete o paciente por seis a "
            "doze meses e a escolha depende do que a sorologia e a biópsia "
            "vão dizer. Pressa no reversível é diferente de pressa no "
            "irreversível.",
        ),
        alt(
            "Só depois de excluir endocardite com hemocultura e ecocardiograma",
            "A exclusão é obrigatória e já está em curso — mas ela não precisa "
            "estar concluída para o pulso começar. O que a endocardite proíbe "
            "é a imunossupressão prolongada, não a primeira dose.",
        ),
    ],
    titulo_resposta="Pressa no reversível, cautela no irreversível",
    ordem=[1, 0, 3, 2],
)

P11 = pergunta(
    11,
    "O p-ANCA veio 1:640 e o anti-MPO, 148 U/mL. O que esse resultado, "
    "sozinho, autoriza a concluir?",
    [
        alt(
            "Que o diagnóstico é vasculite associada ao ANCA",
            "Sorologia não é diagnóstico. O ANCA tem sensibilidade e "
            "especificidade altas no contexto certo, mas é positivo em "
            "endocardite, tuberculose, uso de cocaína adulterada com levamisol "
            "e em várias doenças que este caso ainda não afastou por completo.",
        ),
        alt(
            "Que a probabilidade da hipótese subiu muito, e que ela precisa "
            "do tecido para fechar",
            "É o que um resultado faz: move a probabilidade. Num paciente com "
            "sedimento glomerular, hemorragia alveolar e complemento normal, "
            "esse título move muito — mas quem separa pauci-imune de "
            "imunocomplexo é a imunofluorescência da biópsia.",
            certa=True,
        ),
        alt(
            "Que a doença anti-membrana basal está afastada",
            "Isso quem afasta é o anti-MBG não reagente, que veio no mesmo "
            "painel. Um ANCA positivo não exclui a sobreposição: ela ocorre "
            "justamente em quem tem os dois.",
        ),
        alt(
            "Que o título prediz a gravidade e vai guiar o tratamento",
            "O título não acompanha a atividade de forma confiável ao longo do "
            "tempo, e não se ajusta terapia por ele. O que prediz recidiva é o "
            "antígeno, e não a altura do título.",
        ),
    ],
    titulo_resposta="Sorologia move probabilidade, não fecha diagnóstico",
    ordem=[1, 0, 2, 3],
)

P12 = pergunta(
    12,
    "Cresceu //Staphylococcus aureus// em dois de dois pares. Que hipótese "
    "esse resultado obriga a reabrir?",
    [
        alt(
            "Nenhuma: é infecção de cateter no paciente neutropênico, e o "
            "diagnóstico já está fechado pela biópsia",
            "É a leitura mais provável, e provavelmente a certa. Mas “mais "
            "provável” não é o mesmo que “não preciso olhar”, e o custo de "
            "olhar aqui é um ecocardiograma.",
        ),
        alt(
            "Endocardite infecciosa, que foi derrubada da lista com "
            "hemoculturas que agora se sabe que podem ter sido colhidas cedo "
            "demais",
            "É o mimetizador perfeito da síndrome que a turma acabou de "
            "diagnosticar: a endocardite produz ANCA positivo, "
            "glomerulonefrite pauci-imune, púrpura e hemorragia alveolar — e o "
            "tratamento é o oposto do que este paciente está recebendo. Com "
            "//S. aureus// em dois de dois pares, ela volta para a mesa até "
            "que o ecocardiograma diga o contrário.",
            certa=True,
        ),
        alt(
            "Vasculite induzida por droga, agora que há antibiótico em uso",
            "A vasculite por droga é causada por hidralazina, "
            "propiltiouracila, minociclina e levamisol, e leva semanas a meses "
            "para se instalar. Oxacilina iniciada hoje não produz o quadro que "
            "começou há oito semanas.",
        ),
        alt(
            "Doença anti-membrana basal, pela recaída da hemorragia alveolar",
            "O anti-MBG veio não reagente e a imunofluorescência não mostrou "
            "depósito linear. Nada no quinto dia muda esses dois resultados.",
        ),
    ],
    titulo_resposta="O mimetizador que estava na lista desde o começo",
    ordem=[2, 1, 0, 3],
)


# ─────────────── perguntas de ramo ───────────────
#
# Estas duas não existem no tronco: cada uma pertence a um caminho que o grupo
# escolheu no nó da investigação, e discute o preço daquela escolha. Um grupo
# que pediu certo nunca as vê — e é justamente por isso que elas existem.

P13 = pergunta(
    13,
    "Os nove exames pedidos em bloco voltaram juntos e a creatinina está em "
    "<<creatinina>>. Que exame de bancada, disponível desde a admissão e "
    "ausente daquele pedido, teria podado a lista na primeira hora?",
    [
        alt(
            "Sedimento urinário examinado em urina fresca, com pesquisa de "
            "dismorfismo eritrocitário e de cilindros",
            "Fica pronto em minutos, custa quase nada e é o único exame do "
            "conjunto que localiza o sangramento. Cilindro hemático só se "
            "forma no túbulo, a partir de hemácias que atravessaram o "
            "glomérulo: encontrá-lo põe a lesão dentro do glomérulo e derruba "
            "de uma vez a hipótese de sangramento urológico com pneumopatia à "
            "parte. Nenhum dos nove exames pedidos fazia isso.",
            certa=True,
        ),
        alt(
            "Desidrogenase láctica e haptoglobina, para caracterizar hemólise "
            "como causa da anemia",
            "A anemia deste paciente tem duas explicações já visíveis — o "
            "sangue que está no alvéolo e oito semanas de doença sistêmica. "
            "Caracterizar hemólise seria útil se houvesse esquizócitos ou "
            "plaquetopenia, e não separaria nenhuma das linhas da lista.",
        ),
        alt(
            "Proteinúria de vinte e quatro horas, para quantificar a "
            "intensidade da lesão glomerular",
            "Quantifica o dano e não o localiza, e a coleta consome o dia "
            "inteiro. Numa glomerulonefrite que evolui em horas, medir a "
            "proteinúria de ontem para decidir a conduta de hoje é chegar "
            "atrasado à própria pergunta.",
        ),
        alt(
            "Ureia e eletrólitos seriados de seis em seis horas, para "
            "acompanhar a velocidade da queda de função",
            "Acompanhar a velocidade é obrigatório e não substitui saber a "
            "causa. A curva em ascensão é compatível com todas as linhas de "
            "pé, e o tempo gasto observando-a custou 1,4 mg/dL.",
        ),
        alt(
            "Radiografia de tórax em ortostatismo, mais rápida e mais barata "
            "que a tomografia que foi pedida",
            "Já foi feita na admissão, e o infiltrado bilateral que ela "
            "mostrou é o que motivou o resto. Repeti-la não distingue "
            "hemorragia de edema nem de infecção.",
        ),
    ],
    ordem=[0, 1, 2, 3, 4],
    titulo_resposta="O exame que faltava custava menos que todos os outros",
    ident="p_painel",
)

P14 = pergunta(
    14,
    "A tomografia mostrou vidro fosco difuso e bilateral e a broncoscopia "
    "confirmou hemorragia alveolar, nove horas depois da admissão. Que efeito "
    "esse par de exames tem sobre a lista de hipóteses levantada pelo grupo?",
    [
        alt(
            "Descarta o sangramento urinário com pneumopatia à parte, porque "
            "agora está provado que o pulmão está doente",
            "O pulmão doente não diz nada sobre a origem da hematúria. As "
            "duas doenças independentes continuam sendo uma explicação "
            "possível enquanto ninguém tiver olhado a urina — e é a urina, "
            "não o pulmão, que derruba essa linha.",
        ),
        alt(
            "Descarta infecção pulmonar grave, porque o lavado voltou "
            "hemorrágico em vez de purulento",
            "Hemorragia alveolar e infecção convivem, e algumas infecções "
            "cursam justamente com sangramento — leptospirose, influenza, "
            "aspergilose invasiva. O que exclui infecção é a cultura do "
            "lavado, que ainda não voltou, e não o aspecto do líquido.",
        ),
        alt(
            "Descarta neoplasia broncopulmonar sangrante, porque não há massa "
            "nem nódulo à tomografia",
            "Esta é a única das cinco que quase acerta, e por isso é a mais "
            "instrutiva: a tomografia realmente torna a neoplasia muito "
            "improvável. Mas a broncoscopia é que fecha essa linha, ao "
            "percorrer a árvore brônquica sem achar lesão — e nenhuma das "
            "duas explica o rim, que segue sem ter sido investigado.",
        ),
        alt(
            "Confirma vasculite de pequeno vaso, porque o vidro fosco difuso "
            "e bilateral é o padrão da capilarite alveolar",
            "A capilarite alveolar produz vidro fosco difuso, e o vidro fosco "
            "difuso não é produzido só por ela. Ler a imagem de trás para "
            "frente — do padrão para a doença — é o erro que a tomografia "
            "mais convida a cometer numa sala escura.",
        ),
        alt(
            "Nenhum: as duas confirmam o sangramento que a hemoptise e as "
            "crepitações já indicavam, e são compatíveis com todas as linhas "
            "ainda de pé",
            "Nove horas e um contraste depois, a lista continua inteira. O "
            "par tomografia-broncoscopia documenta a hemorragia alveolar com "
            "precisão e não a atribui a ninguém: é exame de extensão, não de "
            "causa. A pergunta que decide a conduta continua sendo onde o "
            "sangue do rim está passando.",
            certa=True,
        ),
    ],
    ordem=[1, 2, 3, 0, 4],
    titulo_resposta="Exame de extensão não é exame de causa",
    ident="p_imagem",
)


# ─────────────── pergunta sindrômica ───────────────
#
# Vem antes de qualquer lista de doenças, e não menciona nenhuma. O que ela
# cobra é o passo que costuma ser pulado: dizer de onde vem o sangue antes de
# dizer por quê.

P15 = pergunta(
    15,
    "Hemoptise de cerca de 50 mL em duas ocasiões, crepitações finas difusas, "
    "saturação de 88% em ar ambiente e hemoglobina de 7,8 g/dL, que era 13,9 "
    "g/dL há dois meses. Que achado desse conjunto mais restringe a origem do "
    "sangramento?",
    [
        alt(
            "A queda de 6,1 g/dL na hemoglobina, desproporcional ao volume "
            "que foi expectorado",
            "O paciente expectorou cerca de 100 mL, que não derrubam a "
            "hemoglobina em 6 g/dL. O sangue que falta está retido em algum "
            "compartimento, e no pulmão o compartimento que retém sangue sem "
            "devolvê-lo pela boca é o alvéolo. É essa desproporção — e não a "
            "hemoptise — que desloca a origem do brônquio para o espaço "
            "aéreo distal.",
            certa=True,
        ),
        alt(
            "O volume expectorado, que classifica a hemoptise como não maciça",
            "A classificação por volume decide a urgência da via aérea e a "
            "necessidade de embolização; não diz de onde o sangue vem. "
            "Hemoptise não maciça é compatível com todas as origens.",
        ),
        alt(
            "As crepitações finas difusas nos dois hemitórax",
            "Crepitação fina difusa acompanha ocupação alveolar de qualquer "
            "natureza — sangue, água, pus ou fibrose. Localiza o processo no "
            "parênquima e não distingue o que o preenche.",
        ),
        alt(
            "A saturação de 88% em ar ambiente, com resposta ao cateter nasal",
            "Mede a gravidade da troca gasosa e a fração de shunt. Um alvéolo "
            "cheio de sangue e um alvéolo cheio de secreção purulenta "
            "produzem a mesma dessaturação.",
        ),
        alt(
            "A ausência de febre alta e de expectoração purulenta",
            "Argumenta contra pneumonia bacteriana típica e não exclui "
            "infecção — este paciente, aliás, tem 37,8 °C e PCR de 186 mg/L. "
            "Afastar uma causa não localiza a origem do sangramento.",
        ),
    ],
    ordem=[1, 2, 0, 3, 4],
    titulo_resposta="A hemoglobina que sumiu diz onde o sangue ficou",
    ident="p_origem",
)

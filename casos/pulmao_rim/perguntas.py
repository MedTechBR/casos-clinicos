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
    "O lavado está estéril, o ANCA foi pedido e não voltou, e a creatinina "
    "subiu de 3,4 para 3,8 em vinte e quatro horas. Começa a imunossupressão "
    "hoje?",
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

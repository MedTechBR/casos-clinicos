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
            "A drenagem linfática regional",
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
            "A mesma origem embriológica",
            "Pulmão e rim têm origens embriológicas diferentes. A "
            "coincidência aqui é funcional, não embriológica.",
        ),
        alt(
            "Vasos de pequeno calibre: capilar, arteríola e vênula",
            "O capilar glomerular e o capilar alveolar têm a mesma "
            "arquitetura básica: parede finíssima apoiada em membrana "
            "basal, submetida a pressão. Uma agressão a esse "
            "compartimento aparece nos dois órgãos ao mesmo tempo, e "
            "também na pele e no vasa nervorum.", certa=True,
        ),
        alt(
            "A inervação autonômica comum",
            "A inervação não explica lesão tecidual simultânea em quatro "
            "territórios.",
        ),
    ],
)

P2 = pergunta(
    2,
    "Quais exames você não pode deixar de pedir na primeira hora?",
    [
        alt(
            "Espirometria com difusão de monóxido de carbono",
            "A difusão aumenta na hemorragia alveolar e é um dado "
            "elegante. Um paciente com saturação de 88% e dispneia em "
            "repouso não consegue realizar o exame.",
        ),
        alt(
            "Sedimento urinário, com pesquisa de dismorfismo "
            "eritrocitário e de cilindros",
            "Custa pouco, fica pronto em minutos e localiza o "
            "sangramento. Depende de urina fresca e de alguém no "
            "microscópio.", certa=True,
        ),
        alt(
            "Angiotomografia de tórax para tromboembolismo pulmonar",
            "A hemoptise levanta a suspeita, mas o quadro tem oito "
            "semanas, cursa com anemia e o infiltrado é difuso. Não é "
            "apresentação embólica.",
        ),
        alt(
            "ANCA e anticorpo anti-membrana basal glomerular, no mesmo "
            "pedido",
            "São as duas sorologias que decidem a conduta das próximas "
            "horas. O anti-MBG tem prioridade porque, na doença de "
            "Goodpasture, a demora de poucos dias custa a função renal de "
            "forma definitiva.", certa=True,
        ),
        alt(
            "Painel de autoanticorpos de miosite",
            "Não há fraqueza proximal, elevação de CPK ou lesão cutânea "
            "compatível. O exame não responde a nenhuma pergunta que "
            "esteja em aberto.",
        ),
    ],
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
            "Vasculite associada ao ANCA e doença anti-membrana basal "
            "glomerular",
            "As duas cursam com complemento normal. É por isso que elas "
            "seguem no topo da lista depois deste resultado.",
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
)

P6 = pergunta(
    6,
    "A microscopia óptica mostra crescentes celulares. O que a "
    "imunofluorescência acrescenta?",
    [
        alt(
            "Quantifica a fibrose intersticial e a cronicidade",
            "Isso se avalia na microscopia óptica, com colorações para "
            "tecido conjuntivo.",
        ),
        alt(
            "Define a classe histológica de Berden",
            "A classificação de Berden é morfológica, e se estabelece "
            "contando glomérulos normais, com crescentes e escleróticos "
            "na microscopia óptica.",
        ),
        alt(
            "Separa a doença pauci-imune da anti-membrana basal e das "
            "mediadas por imunocomplexos",
            "As três produzem crescentes idênticos na óptica. A "
            "imunofluorescência mostra ausência de depósitos na "
            "pauci-imune, depósito linear ao longo da membrana basal na "
            "anti-MBG, e depósitos granulosos nas mediadas por "
            "imunocomplexos.", certa=True,
        ),
        alt(
            "Estima a probabilidade de recuperação da função renal",
            "Quem estima isso é a proporção entre lesão ativa e lesão "
            "crônica, também na microscopia óptica.",
        ),
    ],
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
)

P8 = pergunta(
    8,
    "Em qual situação a plasmaférese permanece claramente indicada?",
    [
        alt(
            "Todo paciente com glomerulonefrite crescêntica",
            "Indicação indiscriminada foi justamente o que o PEXIVAS "
            "derrubou.",
        ),
        alt(
            "Doença anti-membrana basal glomerular concomitante",
            "Na doença anti-MBG a plasmaférese segue indicada de forma "
            "inequívoca, e a dupla positividade com ANCA ocorre em "
            "parcela não desprezível dos pacientes. É o motivo de o "
            "anti-MBG ser pedido junto com o ANCA.", certa=True,
        ),
        alt(
            "Creatinina acima de 3 mg/dL",
            "Era a prática antes de 2020. O PEXIVAS, com mais de "
            "setecentos pacientes, não encontrou redução de morte ou de "
            "doença renal terminal com o uso guiado por creatinina.",
        ),
        alt(
            "Hemorragia alveolar com hipoxemia",
            "Continua sendo considerada caso a caso, e muitos serviços a "
            "indicam. Mas o benefício não foi demonstrado, e por isso a "
            "indicação não é clara.",
        ),
    ],
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
)

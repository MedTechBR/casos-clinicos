"""A árvore do caso pulmão-rim.

Três nós de decisão, dois ramos cada, oito desfechos que não reconvergem.
Depois do primeiro nó, o paciente que o grupo tem nas mãos é outro — e os
blocos seguintes são outros, não os mesmos com um número trocado.

Erro é recuperável, com custo: o ramo ruim produz piora imediata e visível, o
caso continua, e dentro dele ainda há uma decisão de resgate. Mas o melhor
final do ramo ruim é pior que o pior final do ramo certo.
"""

from motor.arvore import custa, desfecho, efeito, no, ramo
from motor.conteudo import box, nota, p
from motor.desenhos import quadro
from motor.slides import narrativa

from .hipoteses import RIM

# ═══════════════════════ NÓ 1 — a primeira hora ═══════════════════════

N1 = no(
    "n1", "Decisão · primeira hora", "O que você faz na próxima hora",
    "O paciente está internado há <<horas>>, com saturação de <<spo2>> em ar "
    "ambiente, creatinina de <<creatinina>> e sedimento glomerular. As "
    "sorologias específicas levam de dois a cinco dias, e podem já ter sido "
    "pedidas ou não, conforme o que se decidiu na investigação.",
    [
        ramo("colher_e_tratar",
             "Colher sorologia, hemocultura e biópsia em fila, e iniciar pulso "
             "de metilprednisolona hoje",
             vai_para="b_cedo",
             rotulo="trata cedo, sem fechar o diagnóstico",
             efeito_=efeito(horas=+4, creatinina=+0.1,
                            liga=["imunossupressao"]),
             porque="O pulso é reversível e cobre as três hipóteses que "
                    "sobraram. Colher antes preserva a hemocultura e a "
                    "imunofluorescência, que é o que a biópsia dos próximos "
                    "dias ainda vai poder dizer. A creatinina sobe um pouco "
                    "pela hipoperfusão da própria doença, não pela conduta."),
        ramo("esperar_sorologia",
             "Aguardar as sorologias antes de qualquer imunossupressão",
             vai_para="b_espera",
             rotulo="rigor que custa néfron",
             efeito_=efeito(horas=+38, creatinina=+1.6, spo2=-4, hb=-0.9),
             porque="A glomerulonefrite rapidamente progressiva perde função "
                    "em dias, e a janela de recuperação fecha junto com ela. "
                    "Em trinta e oito horas a creatinina subiu 1,6 mg/dL, a "
                    "hemoglobina caiu com o sangramento alveolar em curso e a "
                    "saturação acompanhou. Nada disso foi causado por esperar "
                    "— foi causado por não tratar enquanto se esperava."),
    ],
)

N2B = no(
    "n2b", "Decisão · resgate", "O rim já está em falência",
        "Creatinina de 5,4 mg/dL, diurese de 400 mL em vinte e quatro horas, "
    "potássio de 6,1 mEq/L, saturação de 84%. As sorologias ainda não "
    "voltaram.",
    [
        ramo("dialise_e_pulso",
             "Diálise de urgência pela hipercalemia, pulso de "
             "metilprednisolona e plasmaférese, sem esperar sorologia",
             vai_para="b_resgate",
             rotulo="trata a doença e a complicação juntas",
             efeito_=efeito(horas=+12, creatinina=-0.3, spo2=+3,
                            liga=["dialise", "imunossupressao", "plasmaferese"]),
             porque="A hipercalemia com oligúria é emergência por si só, e "
                    "esperar a sorologia agora custaria o que ainda restou. A "
                    "creatinina de 5,4 e a hemorragia alveolar com hipoxemia "
                    "são os dois gatilhos do KDIGO 2024 para considerar "
                    "plasmaférese — este é o paciente em que ela faz sentido."),
        ramo("so_dialise",
             "Diálise de urgência e aguardar as sorologias, agora que o "
             "potássio está controlado",
             vai_para="b_so_dialise",
             rotulo="corrige o número, não a doença",
             efeito_=efeito(horas=+30, creatinina=+0.4, spo2=-5, hb=-0.7,
                            liga=["dialise", "vm"]),
             porque="A diálise corrige o potássio e não toca no que está "
                    "destruindo o glomérulo. Nas trinta horas seguintes a "
                    "hemorragia alveolar progrediu, a saturação caiu abaixo do "
                    "que a máscara sustenta e o paciente foi intubado. O "
                    "número tratado melhorou; a doença não."),
    ],
)

# ─────────────── ramo 1A: tratou cedo ───────────────

B_CEDO = narrativa("O caso · ramo A", "Primeiras quarenta e oito horas",
    p("O pulso de metilprednisolona foi administrado quatro horas após a "
      "admissão, depois de colhidas as três hemoculturas e as sorologias. A "
      "hemoptise diminuiu no segundo dia e a saturação subiu para 93% com "
      "cateter nasal."),
    p("A creatinina estabilizou em 3,9 mg/dL. A biópsia renal foi feita no "
      "terceiro dia e mostrou glomerulonefrite crescêntica pauci-imune, com "
      "62% de crescentes celulares. O p-ANCA voltou em 1:640 e o anti-MPO em "
      "148 U/mL; o anti-MBG veio não reagente."),
    box("O que o tempo comprou",
        p("Função renal preservada no patamar da admissão e diagnóstico "
          "fechado com a imunofluorescência intacta. A partir daqui a decisão "
          "é sobre o imunossupressor — e essa, ao contrário do pulso, "
          "compromete o paciente por meses."),
        tipo="regra"),
    ident="b_cedo", segue="n2a", densidade=None)

# ─────────────── ramo 1B: esperou ───────────────

B_ESPERA = narrativa("O caso · ramo B", "Trinta e oito horas depois",
    p("As sorologias não voltaram no primeiro dia. Na manhã do segundo, a "
      "creatinina estava em 5,4 mg/dL, a diurese havia caído para 400 mL nas "
      "últimas vinte e quatro horas e o potássio subira para 6,1 mEq/L. A "
      "saturação caiu para 84% em ar ambiente e o paciente passou a precisar "
      "de máscara com reservatório."),
    p("A hemoglobina caiu de 7,8 para 6,9 g/dL, sem sangramento externo: o "
      "alvéolo continuou sangrando durante a espera. A radiografia mostra "
      "infiltrado que progrediu nos dois terços inferiores."),
    box("O que a espera custou",
        p("O rigor de não tratar sem diagnóstico é defensável em quase toda "
          "doença — e é errado nesta. A crescente celular vira crescente "
          "fibrosa em dias, e o que fibrosa não volta com nenhum tratamento. "
          "O paciente ainda pode ser tratado; parte do rim que ele tinha na "
          "chegada, não."),
        tipo="alerta"),
    nota("Antes de avançar",
        p("Pergunte à turma o que exatamente foi perdido. A resposta não é "
          "'tempo' — é néfron. E pergunte quem, na sala, teria feito a mesma "
          "escolha: ela é a mais comum entre internos, e é por isso que ela "
          "está aqui.")),
    ident="b_espera", segue="n2b", densidade=None)

# ═══════════════════════ NÓ 2 — a indução ═══════════════════════

N2A = no(
    "n2a", "Decisão · indução", "Com que imunossupressor",
    "Diagnóstico fechado em quarenta e oito horas, função renal preservada no "
    "patamar da admissão, sem infecção ativa. Sessenta e três anos, creatinina "
    "de 3,9 mg/dL.",
    [
        ramo("rtx",
             "Rituximabe, com glicocorticoide em desmame rápido",
             vai_para="b_rtx",
             rotulo="preferido pelo ACR/VF 2021",
             efeito_=efeito(horas=+72, creatinina=-0.4, spo2=+5, hb=+0.3),
             porque="Eficácia equivalente à da ciclofosfamida na indução, com "
                    "menos toxicidade gonadal e vesical, e é o que o ACR/VF "
                    "2021 recomenda condicionalmente como preferência. O "
                    "desmame rápido do corticoide, validado pelo PEXIVAS, "
                    "reduz infecção grave em um ano sem perder eficácia."),
        ramo("cfx_plena",
             "Ciclofosfamida endovenosa em dose plena, sem ajuste renal",
             vai_para="b_cfx",
             rotulo="a dose que o protocolo antigo trazia",
             efeito_=efeito(horas=+72, creatinina=-0.2, spo2=+4,
                            liga=["imunossupressao"]),
             porque="A ciclofosfamida é depurada pelo rim. Com filtração de 17 "
                    "mL/min/1,73 m² e sessenta e três anos, a dose plena "
                    "produz exposição muito acima da pretendida — e a "
                    "consequência não aparece hoje, aparece no nadir, entre o "
                    "sétimo e o décimo quarto dia."),
    ],
)

# ─────────────── blocos dos ramos do nó 2 ───────────────

B_RTX = narrativa("O caso · ramo A1", "Quinto dia, sob rituximabe",
    p("Rituximabe em quatro doses semanais, com metilprednisolona em desmame "
      "rápido. No quinto dia a creatinina caiu para 3,5 mg/dL, a saturação "
      "está em 93% com cateter nasal e a hemoptise cessou."),
    p("Na manhã do quinto dia, contudo, surgiu febre de 38,9 °C com calafrio. "
      "O hemograma mostra 1.900 leucócitos com 620 neutrófilos e a "
      "procalcitonina subiu de 0,4 para 3,1 ng/mL."),
    ident="b_rtx", segue="n3a", densidade=None)

B_CFX = narrativa("O caso · ramo A2", "Quinto dia, sob ciclofosfamida",
    p("Ciclofosfamida endovenosa em dose plena. No quinto dia a creatinina "
      "caiu para 3,7 mg/dL e a hemoptise cessou, mas o hemograma mostra 900 "
      "leucócitos com 210 neutrófilos — neutropenia profunda, mais precoce e "
      "mais grave do que o esperado para o quinto dia."),
    p("Febre de 39,2 °C com calafrio e hipotensão que respondeu a volume. "
      "Procalcitonina de 5,8 ng/mL."),
    nota("Antes de avançar",
        p("A tela não diz por que a neutropenia é tão precoce — pergunte. Com "
          "filtração de 17 mL/min/1,73 m², a dose plena produziu exposição "
          "muito acima da pretendida, e 210 neutrófilos no quinto dia não são "
          "os do esquema: são os da dose. A turma tem de chegar nisso antes "
          "de escolher a conduta.")),
    ident="b_cfx", segue="n3b", densidade=None)

B_RESGATE = narrativa("O caso · ramo B1", "Quinto dia, já em diálise",
    p("Três sessões de hemodiálise, pulso de metilprednisolona e três sessões "
      "de plasmaférese. A creatinina estabilizou em 5,1 mg/dL, ainda sem "
      "recuperação de diurese, e a saturação subiu para 90% com máscara."),
    p("O p-ANCA voltou em 1:640 e o anti-MPO em 148 U/mL. A biópsia renal, "
      "feita no quarto dia, mostra 58% de crescentes — mas agora com metade "
      "delas já fibrocelulares, e fibrose intersticial em 25% do córtex."),
    p("Na manhã do quinto dia, febre de 38,7 °C com 640 neutrófilos e "
      "procalcitonina de 3,4 ng/mL."),
    ident="b_resgate", segue="n3c", densidade=None)

B_SO_DIALISE = narrativa("O caso · ramo B2", "Quinto dia, intubado",
    p("A diálise corrigiu o potássio. Nas trinta horas seguintes a hemorragia "
      "alveolar progrediu, a saturação caiu para 79% com máscara com "
      "reservatório e o paciente foi intubado no terceiro dia. A imunossupressão "
      "começou no quarto dia, quando as sorologias voltaram."),
    p("A biópsia renal foi adiada pela instabilidade. No quinto dia, febre de "
      "38,8 °C com 700 neutrófilos, e infiltrado que piorou de forma "
      "assimétrica à direita."),
    nota("Antes de avançar",
        p("Deixe o infiltrado assimétrico no ar antes de comentar. Vasculite "
          "em atividade e pneumonia associada à ventilação explicam o mesmo "
          "quadro, pedem condutas opostas, e a assimetria é a única pista na "
          "tela. Se ninguém a mencionar, a decisão seguinte vai ser tomada "
          "sem ela.")),
    ident="b_so_dialise", segue="n3d", densidade=None)

# ═══════════════════════ NÓ 3 — o quinto dia ═══════════════════════

def _n3(ident, titulo, pergunta, ramos):
    return no(ident, "Decisão · quinto dia", titulo, pergunta, ramos)


N3A = _n3("n3a", "Febre no quinto dia",
    "Creatinina em queda, hemoptise cessada, e agora febre de 38,9 °C com 620 "
    "neutrófilos e procalcitonina de 3,1 ng/mL.",
    [
        ramo("cultura_atb", "Colher culturas e iniciar antibiótico de amplo "
             "espectro, mantendo a imunossupressão",
             vai_para="f_aa", rotulo="trata a hipótese que mata mais rápido",
             efeito_=efeito(horas=+96, creatinina=-0.5, spo2=+3, hb=+0.6,
                            liga=["antibiotico"]),
             porque="Neutropenia com febre é neutropenia febril até prova em "
                    "contrário, e a janela para o antibiótico é de uma hora. "
                    "A vasculite em atividade não produz 620 neutrófilos nem "
                    "procalcitonina de 3,1: produz o contrário."),
        ramo("intensificar", "Intensificar a imunossupressão, presumindo "
             "atividade da vasculite",
             vai_para="f_ab", rotulo="a leitura que a febre convida a fazer",
             efeito_=efeito(horas=+96, creatinina=+0.3, spo2=-6, hb=-0.5,
                            liga=["vm"]),
             porque="É a armadilha do caso. Febre durante a indução tem duas "
                    "leituras opostas, e a neutropenia decide entre elas: "
                    "vasculite ativa não neutropeniza. Intensificar aqui "
                    "aprofunda a neutropenia enquanto a bacteremia avança."),
    ])

N3B = _n3("n3b", "Neutropenia profunda no quinto dia",
    "Duzentos e dez neutrófilos, febre de 39,2 °C, hipotensão que respondeu a "
    "volume, procalcitonina de 5,8 ng/mL.",
    [
        ramo("atb_e_fator", "Antibiótico de amplo espectro, culturas e fator "
             "estimulador de colônias, suspendendo a ciclofosfamida",
             vai_para="f_ba", rotulo="trata e corrige a causa da neutropenia",
             efeito_=efeito(horas=+120, creatinina=-0.3, spo2=+2, hb=+0.4,
                            liga=["antibiotico"]),
             porque="A neutropenia aqui é iatrogênica e previsível, e "
                    "suspender a droga é parte do tratamento. O fator "
                    "estimulador encurta o nadir num paciente com 210 "
                    "neutrófilos e bacteremia."),
        ramo("so_atb", "Antibiótico de amplo espectro e culturas, mantendo a "
             "ciclofosfamida para não perder o controle da vasculite",
             vai_para="f_bb", rotulo="protege a doença, não o paciente",
             efeito_=efeito(horas=+120, creatinina=0, spo2=-4, hb=-0.4,
                            liga=["antibiotico", "vm"]),
             porque="Manter a droga que está causando a neutropenia enquanto "
                    "se trata a infecção que a neutropenia permitiu prolonga o "
                    "nadir por mais uma semana. A vasculite não recidiva em "
                    "sete dias sem ciclofosfamida; a bacteremia, sim, se "
                    "aprofunda."),
    ])

N3C = _n3("n3c", "Febre no quinto dia, com o rim já em diálise",
    "Creatinina estabilizada em 5,1 mg/dL sem diurese, biópsia com metade das "
    "crescentes já fibrocelulares, e agora febre de 38,7 °C com 640 "
    "neutrófilos.",
    [
        ramo("atb_manter", "Antibiótico de amplo espectro e culturas, "
             "mantendo a indução",
             vai_para="f_ca", rotulo="não abre mão do rim que ainda resta",
             efeito_=efeito(horas=+120, creatinina=-0.2, spo2=+3, hb=+0.5,
                            liga=["antibiotico"]),
             porque="A fração fibrocelular já não volta, mas a fração celular "
                    "ainda responde — e é ela que decide se o paciente sai da "
                    "diálise. Tratar a infecção sem suspender a indução é o "
                    "que preserva as duas frentes."),
        ramo("suspender_tudo", "Suspender a imunossupressão até a infecção "
             "estar controlada",
             vai_para="f_cb", rotulo="segurança que custa o rim que sobrou",
             efeito_=efeito(horas=+120, creatinina=+0.6, spo2=+1, hb=+0.2),
             porque="Sete a dez dias sem indução, num rim com 58% de "
                    "crescentes, é o tempo de a fração celular restante "
                    "fibrosar. A infecção é controlada e o paciente sai vivo "
                    "— e sai dialítico."),
    ])

N3D = _n3("n3d", "Intubado, febril, e com duas doenças em cima",
    "Em ventilação mecânica desde o terceiro dia, infiltrado assimétrico à "
    "direita, febre de 38,8 °C com 700 neutrófilos, e vasculite ainda ativa.",
    [
        ramo("lavado_dirigido", "Novo lavado broncoalveolar dirigido ao lobo "
             "que piorou, antibiótico empírico enquanto se espera",
             vai_para="f_da", rotulo="pergunta ao tecido qual das duas é",
             efeito_=efeito(horas=+144, creatinina=+0.2, spo2=+4,
                            liga=["antibiotico"]),
             porque="Quando as duas hipóteses pedem condutas opostas e nenhuma "
                    "pode esperar, o que resolve é material. O lavado dirigido "
                    "separa hemorragia alveolar em curso de pneumonia "
                    "associada à ventilação, e o antibiótico empírico cobre a "
                    "espera sem fechar nenhuma porta."),
        ramo("presumir_vasculite", "Presumir atividade da vasculite e "
             "intensificar a imunossupressão",
             vai_para="f_db", rotulo="escolhe uma das duas sem perguntar",
             efeito_=efeito(horas=+144, creatinina=+0.5, spo2=-3, hb=-0.6),
             porque="Escolher entre duas hipóteses opostas sem material é "
                    "apostar. Se for pneumonia, a intensificação a alimenta; e "
                    "no paciente já intubado, com 700 neutrófilos e trinta "
                    "horas de atraso acumuladas, a margem para errar acabou."),
    ])


# ═══════════════════════ os oito desfechos ═══════════════════════
#
# Nenhum ramo termina no nó, e nenhum final é o mesmo. O melhor final do ramo
# ruim (f_ca) é pior que o pior final do ramo certo (f_ab): o aluno nunca fica
# travado, mas paga.

F = [
    desfecho("f_aa", "Alta no vigésimo primeiro dia",
        p("Hemocultura com **//Staphylococcus aureus// sensível a oxacilina** "
          "em dois de dois pares, cateter central retirado, oxacilina por "
          "quatorze dias. A febre cedeu em quarenta e oito horas e os "
          "neutrófilos recuperaram no oitavo dia."),
        p("Alta no vigésimo primeiro dia com creatinina de 2,1 mg/dL e sem "
          "necessidade de diálise em nenhum momento. Rituximabe de manutenção "
          "programado para o sexto mês. Em seis meses, creatinina de 1,7 "
          "mg/dL — perda definitiva de cerca de 40% da função basal."),
        box("Por que este é o melhor final possível",
            p("O pulso precoce preservou a fração celular das crescentes, o "
              "rituximabe evitou a neutropenia da dose renal errada, e a febre "
              "foi lida como infecção e não como doença. Três decisões, "
              "nenhuma delas heroica — cada uma apenas não fez o erro "
              "disponível."),
            tipo="regra"),
        qualidade="melhor"),

    desfecho("f_ab", "Alta no trigésimo quarto dia, após a UTI",
        p("A intensificação foi feita com o paciente bacterêmico. Em trinta e "
          "seis horas houve choque séptico, intubação e cinco dias de "
          "noradrenalina. A hemocultura, colhida tarde, cresceu **//S. "
          "aureus//**; o cateter permaneceu no lugar por mais dois dias."),
        p("Extubado no décimo primeiro dia. Alta no trigésimo quarto, com "
          "creatinina de 2,8 mg/dL. Em seis meses, 2,4 mg/dL — perda de cerca "
          "de 60% da função basal, e uma internação de UTI que não precisava "
          "ter acontecido."),
        box("O erro e o resgate",
            p("O erro foi ler a febre como atividade. O resgate — antibiótico "
              "e retirada do cateter — funcionou, e é por isso que este final "
              "não é o pior. Mas a diferença entre ele e a alta no vigésimo "
              "primeiro dia é de treze dias, uma UTI e 0,7 mg/dL de "
              "creatinina permanente."),
            tipo="erro"),
        qualidade="medio"),

    desfecho("f_ba", "Alta no vigésimo sexto dia",
        p("Ciclofosfamida suspensa, fator estimulador de colônias e antibiótico "
          "de amplo espectro. Os neutrófilos recuperaram no sexto dia e a "
          "hemocultura cresceu **//S. aureus// sensível a oxacilina**. A "
          "indução foi retomada com rituximabe no décimo quarto dia."),
        p("Alta no vigésimo sexto dia com creatinina de 2,3 mg/dL. Em seis "
          "meses, 1,9 mg/dL. A cistite hemorrágica não ocorreu, mas a "
          "contagem de leucócitos levou dois meses para normalizar."),
        box("O ajuste que não foi feito, e o que o corrigiu",
            p("A dose plena num rim com filtração de 17 produziu neutropenia "
              "profunda e precoce. Reconhecer que a neutropenia era "
              "iatrogênica — e não da doença — foi o que permitiu suspender a "
              "droga certa em vez de tratar em torno dela."),
            tipo="erro"),
        qualidade="medio"),

    desfecho("f_bb", "Alta no quadragésimo primeiro dia, com sequela",
        p("A ciclofosfamida foi mantida durante a bacteremia. O nadir se "
          "prolongou por mais nove dias, houve candidemia associada ao cateter "
          "no décimo segundo dia e o paciente ficou dezoito dias em ventilação "
          "mecânica."),
        p("Alta no quadragésimo primeiro dia com creatinina de 3,1 mg/dL e "
          "fraqueza adquirida na UTI, ainda em reabilitação aos seis meses. "
          "Creatinina de 2,9 mg/dL — perda de cerca de 65% da função."),
        box("Duas decisões que se somaram",
            p("A dose não ajustada criou a neutropenia; mantê-la durante a "
              "bacteremia a prolongou. Nenhuma das duas, isolada, produziria "
              "este desfecho — foi a soma. É o final que mais custa, e é "
              "também o mais fácil de alcançar por caminhos defensáveis."),
            tipo="alerta"),
        qualidade="pior"),

    desfecho("f_ca", "Fora da diálise no quadragésimo dia",
        p("Antibiótico de amplo espectro com a indução mantida. **//S. "
          "aureus//** em dois de dois pares, cateter retirado, oxacilina por "
          "quatorze dias. A diurese voltou no décimo nono dia e a última "
          "sessão de hemodiálise foi no vigésimo terceiro."),
        p("Alta no quadragésimo dia com creatinina de 3,4 mg/dL. Em seis "
          "meses, 2,9 mg/dL, fora de diálise, em acompanhamento em ambulatório "
          "de doença renal crônica estágio 4."),
        box("O melhor final deste ramo é pior que o pior do outro",
            p("Trinta e oito horas de espera na primeira hora custaram a "
              "metade fibrocelular das crescentes, vinte e três dias de "
              "diálise e 1,2 mg/dL de creatinina permanente a mais. Todas as "
              "decisões seguintes foram acertadas — e nenhuma delas devolveu o "
              "que se perdeu antes de a primeira ser tomada."),
            tipo="alerta"),
        qualidade="medio"),

    desfecho("f_cb", "Diálise definitiva",
        p("A imunossupressão foi suspensa por onze dias até a infecção estar "
          "controlada. A diurese não retornou. A biópsia de controle, no "
          "trigésimo dia, mostra crescentes agora fibrosas e fibrose "
          "intersticial em 55% do córtex."),
        p("Alta no quadragésimo quinto dia em hemodiálise três vezes por "
          "semana, com fístula programada. Aos seis meses segue dialítico, e "
          "foi inscrito em lista de transplante."),
        box("A segurança que custou o rim",
            p("Suspender a indução na vigência de infecção é conduta "
              "defensável, e em muitos contextos é a certa. Aqui, num rim com "
              "58% de crescentes e metade delas ainda celulares, onze dias "
              "foram o tempo de a fração recuperável fibrosar. O paciente saiu "
              "vivo, e sem rim."),
            tipo="alerta"),
        qualidade="pior"),

    desfecho("f_da", "Extubado no décimo sexto dia",
        p("O lavado dirigido ao lobo que piorou mostrou **//Pseudomonas "
          "aeruginosa//** em cultura quantitativa acima do limiar, com "
          "hemossiderófagos em queda — pneumonia associada à ventilação, e "
          "não hemorragia alveolar em recidiva. Antibiótico dirigido, indução "
          "mantida."),
        p("Extubado no décimo sexto dia. Alta no quinquagésimo, em "
          "hemodiálise, com retirada do cateter no terceiro mês quando a "
          "diurese retornou parcialmente. Aos seis meses, creatinina de 3,6 "
          "mg/dL, fora de diálise, doença renal crônica estágio 4."),
        box("O material desempatou",
            p("Duas hipóteses opostas, nenhuma podendo esperar, e a decisão "
              "resolvida por um lavado que levou seis horas. É o mesmo "
              "princípio do sedimento na primeira hora, e é o que este ramo "
              "inteiro não fez lá atrás."),
            tipo="regra"),
        qualidade="medio"),

    desfecho("f_db", "Óbito no vigésimo nono dia",
        p("A imunossupressão foi intensificada sem material. A cultura de "
          "aspirado traqueal, colhida depois, cresceu **//Pseudomonas "
          "aeruginosa//** multirresistente. Houve choque séptico refratário no "
          "vigésimo terceiro dia, sem recuperação de função renal em nenhum "
          "momento."),
        p("Óbito no vigésimo nono dia de internação, por choque séptico de "
          "foco pulmonar, em paciente sob imunossupressão intensificada e em "
          "diálise."),
        box("Onde este caminho começou",
            p("Não foi aqui. Começou trinta e oito horas antes do primeiro "
              "tratamento, seguiu na diálise que corrigiu o número e não a "
              "doença, e terminou numa escolha entre duas hipóteses opostas "
              "feita sem perguntar ao tecido. Nenhuma das três decisões é "
              "absurda isoladamente. Juntas, são este desfecho."),
            tipo="alerta"),
        nota("Antes de encerrar",
            p("Este é o único desfecho com óbito, e ele existe de propósito. "
              "Volte ao primeiro nó com V, escolha o outro ramo e mostre o "
              "contrafactual: a mesma doença, o mesmo paciente, alta no "
              "vigésimo primeiro dia.")),
        qualidade="pior"),
]


# ═══════ NÓ 0 — que exames você pede, e é isso que o caso mostra ═══════
#
# Antes deste nó o caso desfilava resultado que ninguém tinha pedido. Agora a
# investigação que aparece nas telas seguintes é a que o grupo escolheu, e o
# que ele não pediu simplesmente não está lá quando faz falta.

N0 = no(
    "n0", "Decisão · a investigação", "Que exames você pede agora",
    "A lista está levantada e nada foi pedido. O que você pedir decide o que "
    "este caso mostra — e o que não.",
    [
        ramo("beira_do_leito",
             "Sedimento urinário em urina fresca agora, com as sorologias "
             "no mesmo pedido; imagem na sequência",
             vai_para="sedimento_urinario",
             rotulo="o que fica pronto em minutos",
             efeito_=efeito(horas=+1),
             porque="O sedimento separa sangramento glomerular de urológico "
                    "em minutos e por quase nada, e poda a primeira linha da "
                    "lista. As sorologias vão no mesmo pedido — mas não são "
                    "elas que orientam a próxima hora."),
        ramo("painel_completo",
             "Painel completo de uma vez: sorologias, tomografia e "
             "broncoscopia, e reavaliar quando tudo voltar",
             vai_para="b_painel",
             rotulo="pedir tudo não é o mesmo que saber o que fazer",
             efeito_=efeito(horas=+34, creatinina=+1.4, spo2=-3, hb=-0.7),
             porque="Nenhum dos três volta nesta hora, e o mais rápido e "
                    "barato ficou de fora. Trinta e quatro horas depois a "
                    "lista segue inteira e o rim perdeu 1,4 mg/dL."),
        ramo("imagem_primeiro",
             "Tomografia de tórax e broncoscopia primeiro, para achar a fonte "
             "do sangramento",
             vai_para="b_imagem",
             rotulo="persegue o órgão que sangra visível",
             efeito_=efeito(horas=+9, creatinina=+0.4, spo2=-1),
             porque="A hemoptise chama atenção; o rim sangra calado. A "
                    "imagem confirma o que já se sabia e não distingue "
                    "nenhuma linha da lista das outras."),
    ],
    densidade="xd",
)

B_PAINEL = narrativa("O caso · ramo do painel", "Trinta e quatro horas depois",
    p("As sorologias, a tomografia e a broncoscopia foram pedidas no mesmo "
      "momento. A tomografia saiu em seis horas e mostrou vidro fosco difuso e "
      "bilateral; a broncoscopia foi feita no dia seguinte e confirmou "
      "hemorragia alveolar, com culturas em andamento. As sorologias seguem "
      "pendentes."),
    p("Nesse intervalo a creatinina subiu de 3,8 para 5,2 mg/dL e a saturação "
      "caiu para 85%. Ninguém olhou a urina."),
    # A caixa que ficava aqui dizia à turma o que ela tinha deixado de pedir.
    # Entregar a leitura na tela é o oposto de fazê-la: a tela narra o que
    # aconteceu, e quem conduz decide se e quando aponta.
    nota("Antes de avançar",
        p("Pergunte qual dos exames pedidos mudou alguma conduta, e espere. "
          "Depois pergunte o que ficou de fora. Pedir tudo de uma vez parece "
          "cauteloso e é o oposto: adia a decisão pelo tempo do exame mais "
          "lento do pedido.")),
    ident="b_painel")

B_IMAGEM = narrativa("O caso · ramo da imagem", "Nove horas depois",
    p("A tomografia mostrou opacidades em vidro fosco difusas e bilaterais, "
      "sem nódulo escavado, massa ou derrame. A broncoscopia mostrou alíquotas "
      "progressivamente hemorrágicas e hemossiderófagos em 34% dos macrófagos: "
      "hemorragia alveolar confirmada, com pelo menos quarenta e oito horas de "
      "evolução."),
    p("A creatinina subiu para 4,2 mg/dL. O contraste da tomografia não ajudou "
      "nisso."),
    nota("Antes de avançar",
        p("Peça à turma que releia a lista do tórax com estes dois exames na "
          "mão e diga quantas linhas caíram. O rim sangra calado e o pulmão "
          "sangra visível: é por isso que a hemoptise puxa a investigação para "
          "o tórax, e é por isso que a urina é o exame esquecido.")),
    ident="b_imagem")


# ─────────── o que cada rota da investigação ainda tem de atravessar ───────────
#
# Antes, estes dois ramos saltavam do nó da investigação direto para o nó do
# tratamento: quem pedisse errado nunca via a imunofluorescência, a biópsia nem
# a classificação de Berden. Punir a escolha ruim tirando a aula é o contrário
# de ensinar. Agora cada rota atravessa a sua própria aquisição — outra ordem,
# outro preço, outra conversa — e as três desembocam nas imagens que elas
# mesmas pediram e no resultado imunológico, que é onde o diagnóstico fecha.
# A tomografia e o lavado foram feitos nos três caminhos: o que muda é quando,
# a que custo e depois de quanta coisa já ter sido decidida sem eles.

B_PAINEL_2 = custa(narrativa("O caso · ramo do painel", "A lista, podada de uma vez",
    p("O sedimento urinário foi enfim examinado, em urina fresca: hemácias "
      "dismórficas em 62% do campo e cilindros hemáticos numerosos. "
      "Complemento normal, FAN e anti-DNA não reagentes, crioglobulinas "
      "negativas em tubo aquecido, hemoculturas estéreis. A infecção segue de "
      "pé: a cultura do lavado ainda não voltou. A creatinina está em "
      "<<creatinina>> e o paciente completou <<horas>> de internação sem uma "
      "única droga dirigida à doença."),
    quadro(RIM, {
        "glomerular": ("confirmada",
                       "Hemácias dismórficas em 62% e cilindros hemáticos"),
        "pre_renal": ("derrubada", "Sedimento com cilindros, e nenhum volume "
                                   "corrige um glomérulo"),
        "nta": ("derrubada", "Cilindro hemático não se forma na necrose tubular"),
        "nia": ("derrubada", "Sem cilindro leucocitário e sem droga nova"),
        "obstrutiva": ("derrubada", "Sem dilatação pielocalicial à "
                                    "ultrassonografia"),
    }, titulo="A pergunta renal, respondida com trinta e seis horas de atraso",
       passo_a_passo=False),
    # O comentário é sobre o método do próprio grupo, não sobre o paciente:
    # é fala de quem conduz, não linha de slide. Vai para a nota, que a tela
    # não mostra e o PDF imprime.
    p("As imagens e o lavado daquele pedido em bloco são os que seguem."),
    nota("O que se perdeu no caminho",
        p("Seis hipóteses caíram juntas e nenhuma foi discutida. Pedir em "
          "bloco apaga a sequência em que o raciocínio se constrói: a turma "
          "recebe a lista já podada e não sabe dizer qual exame podou o quê. "
          "Peça que reconstruam — qual dos nove derrubou o lúpus, qual "
          "derrubou a endocardite — e a conta do bloco aparece sozinha.")),
    ident="b_painel_2", segue="tomografia_de_torax", densidade="xd"),
    efeito(horas=+2, creatinina=+0.2))

B_IMAGEM_2 = custa(narrativa("O caso · ramo da imagem", "Voltando à urina, com atraso",
    p("Depois da broncoscopia, a urina foi examinada, e resolveu em quatro "
      "minutos o que nove horas de imagem não resolveram: hemácias "
      "dismórficas em 62% do campo e cilindros hemáticos numerosos. "
      "Complemento, FAN, anti-DNA e crioglobulinas foram pedidos junto e "
      "voltaram negativos; as hemoculturas, estéreis. O "
      "ANCA e o anti-membrana basal glomerular só foram solicitados agora, e "
      "é por eles que o caso passa a esperar, com <<creatinina>> e <<horas>> "
      "de relógio."),
    quadro(RIM, {
        "glomerular": ("confirmada",
                       "Hemácias dismórficas em 62% e cilindros hemáticos"),
        "pre_renal": ("derrubada", "Sedimento com cilindros, e nenhum volume "
                                   "corrige um glomérulo"),
        "nta": ("derrubada", "Cilindro hemático não se forma na necrose tubular"),
        "nia": ("derrubada", "Sem cilindro leucocitário e sem droga nova"),
        "obstrutiva": ("derrubada", "Sem dilatação pielocalicial à "
                                    "ultrassonografia"),
    }, titulo="O que a urina fez em quatro minutos", passo_a_passo=False),
    p("A tomografia e o lavado que abriram esta rota são os que seguem."),
    nota("Antes de avançar",
        p("A investigação começou pelo órgão que chamava atenção, não pelo que "
          "decidia. O pedido das sorologias, que leva dias, saiu com quinze "
          "horas de atraso — e é esse atraso que vai aparecer na biópsia.")),
    ident="b_imagem_2", segue="tomografia_de_torax", densidade="xd"),
    efeito(horas=+6, creatinina=+0.3))

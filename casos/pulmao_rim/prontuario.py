"""A condução do caso pulmão-rim, em prontuário.

Mesmo paciente do baralho, outra forma de encontrá-lo: aqui ele está num leito,
o relógio anda, e nada aparece na tela sem que alguém peça. Quem não perguntar
pelos medicamentos não vai saber que ele só usa losartana; quem não olhar a
urina vai passar dois dias atrás do pulmão; quem esperar a sorologia vai ver a
creatinina subir enquanto espera.

O paciente é ficcional. Os números foram desenhados para serem internamente
coerentes e para que a fisiologia da condução — o que o tempo custa, o que o
tratamento devolve — apareça no cabeçalho sem ninguém precisar comentar.
"""

from pathlib import Path

from motor.prontuario import (
    aliquota, caminho, campo, decisao, desfecho, efeito, evolucao, examinar,
    marco, paciente, perguntar, prescrever, rumo, sinal, taxa,
)

from .banco import BANCO  # noqa: F401  — a gaveta de exames é a mesma

TITULO = "Homem de 63 anos com hemoptise, púrpura e queda de função renal"
SLUG = "pulmao-rim"


PACIENTE = paciente(
    identificacao="Homem, 63 anos",
    leito="Emergência · leito 12",
    admissao="14:20",
    queixa="Hemoptise e dispneia",
    estado=dict(creatinina=3.8, spo2=88, hb=7.8, potassio=5.4, diurese=35),
    resumo=(
        "Homem de 63 anos, trazido pela esposa por dispneia progressiva e "
        "expectoração com sangue. Está sentado na maca, dispneico, completa "
        "frases curtas. A triagem colheu exames e mediu os sinais vitais; os "
        "resultados da bioquímica de entrada já estão no sistema. "
        "**O resto está com você.**"
    ),
)


# ═══════════════════════ a história, em alíquotas ═══════════════════════
#
# Ela é contada, não consultada. Quem conduz aperta "continuar" e o caso abre o
# pedaço seguinte, no ritmo da sala — como no //Case Records//. O que continua
# sendo pergunta é só o que o paciente não conta por conta própria: os
# medicamentos que ele não considera medicamento, a exposição que ele não
# relaciona com nada, a queixa que ele acha que não vem ao caso.

ABERTURA = [
    aliquota("Oito semanas antes",
        "A esposa conta que tudo começou com rinorreia purulenta persistente, "
        "crostas nas narinas e sangramento nasal quase diário. Ele foi tratado "
        "duas vezes como rinossinusite bacteriana, primeiro com amoxicilina e "
        "depois com amoxicilina-clavulanato, sem melhora. Nesse período parou "
        "de sentir cheiro.",
        minutos=3),

    aliquota("Cinco semanas antes",
        "Vieram dores articulares que mudavam de lugar — punhos numa semana, "
        "tornozelos na outra — sem inchaço. Febre no fim da tarde, até 37,9 °C, "
        "suor à noite, e 6 kg perdidos sem mudar a alimentação. Ela reparou que "
        "ele passou a cansar subindo a rampa da garagem.",
        minutos=3),

    aliquota("Duas semanas antes",
        "Começou uma tosse seca, que em poucos dias passou a ter raias de "
        "sangue. Procurou uma emergência, onde a radiografia de tórax foi lida "
        "como normal, e voltou para casa com antitussígeno.",
        minutos=2),

    aliquota("Nos últimos três dias",
        "A falta de ar progrediu até aparecer em repouso. Ele expectorou cerca "
        "de 50 mL de sangue vivo em duas ocasiões — a segunda hoje de manhã, e "
        "foi ela que os trouxe. A urina, diz a esposa, está escura há uma "
        "semana.",
        minutos=2),

    aliquota("O que consta do cadastro",
        "Hipertenso há dez anos, em acompanhamento na unidade básica. "
        "Ex-tabagista de 30 anos-maço, parou há oito anos. Sem diabetes e sem "
        "doença renal conhecida. Os exames de rotina de dois meses atrás estão "
        "anexados: creatinina 1,0 mg/dL, hemoglobina 13,9 g/dL, urina sem "
        "alterações.",
        minutos=2),
]


# ═══════════════════════════ o que se pode fazer ═══════════════════════════
#
# Não há menu na tela: nada disto aparece em lista. Chega-se aqui escrevendo, e
# os sinônimos são os nomes pelos quais a coisa é chamada de verdade na
# enfermaria.

ACOES = [
    # ───────────────────── anamnese dirigida ─────────────────────
    perguntar("medicacoes",
        "Medicamentos em uso, incluindo os que não foram prescritos",
        "Losartana 50 mg/dia para hipertensão e sinvastatina 20 mg/dia. Nega "
        "anti-inflamatório, chá, suplemento, fórmula de emagrecimento e "
        "medicação comprada sem receita. Perguntado nominalmente, nega "
        "hidralazina, propiltiouracila e minociclina, e nega uso de cocaína em "
        "qualquer momento da vida.",
        minutos=5, liga=("medicacoes_revisadas",),
        detalhe="a pergunta que decide uma das linhas da lista",
        sin=["medicamentos", "medicacao", "remedios", "drogas",
             "uso de medicacao", "o que ele toma", "lista de medicamentos",
             "hidralazina", "cocaina", "propiltiouracila", "minociclina",
             "levamisol", "farmacos", "medicamentosa"]),

    perguntar("exposicoes", "Exposições, viagens e contato com animais",
        "Mora em Quixadá, em casa de alvenaria com água encanada. Não houve "
        "enchente na região nem contato com água parada; nega roedores no "
        "domicílio e nega viagem recente. Trabalhou trinta anos como "
        "comerciante, sem exposição a sílica, asbesto ou solventes.",
        minutos=5, detalhe="epidemiologia local, incluindo leptospirose",
        sin=["exposicao", "viagem", "epidemiologia", "enchente", "rato", "roedor", "agua", "contato", "ocupacional", "trabalho"]),

    perguntar("sistemas", "Revisão de sistemas dirigida",
        "Nega dor torácica, ortopneia e dispneia paroxística noturna. Nega "
        "úlcera oral ou genital, olho vermelho, fotossensibilidade e "
        "fenômeno de Raynaud. Nega diarreia, dor abdominal e sangue nas "
        "fezes. Nota que a urina ficou escura na última semana, e que os pés "
        "ficaram manchados há cerca de dez dias. Diz que o pé direito "
        "'está pesado' — queixa que não havia mencionado.",
        minutos=6, detalhe="o que ele não conta se não for perguntado",
        sin=["revisao de sistemas", "sintomas", "interrogatorio", "anamnese complementar"]),

    perguntar("familiar", "História familiar",
        "Pai falecido de infarto aos 71 anos, mãe viva com hipertensão. Sem "
        "doença renal, autoimune ou pulmonar na família.",
        minutos=3,
        sin=["historia familiar", "antecedentes familiares", "familia"]),

    # ───────────────────── exame físico ─────────────────────
    examinar("respiratorio", "Ausculta pulmonar e mecânica respiratória",
        "Frequência respiratória de 28 incursões por minuto, uso de "
        "musculatura acessória. Crepitações finas difusas nos dois "
        "hemitórax, sem sibilos e sem atrito pleural. Percussão sem "
        "macicez. Expansibilidade simétrica.",
        minutos=4,
        sin=["torax", "pulmao", "pulmonar", "ausculta pulmonar", "aparelho respiratorio"]),

    examinar("cardiovascular", "Ausculta cardíaca e avaliação de volemia",
        "Pressão arterial de 148/92 mmHg, frequência cardíaca de 104 "
        "batimentos por minuto, ritmo regular em dois tempos, sem sopros. "
        "Não há estase jugular, terceira bulha ou edema de membros "
        "inferiores. Extremidades quentes, enchimento capilar de 2 segundos.",
        minutos=4, detalhe="volemia decide muita coisa aqui",
        sin=["coracao", "cardiaco", "cardio", "volemia", "jugular", "precordio", "ausculta cardiaca", "perfusao"]),

    examinar("pele", "Inspeção da pele e das extremidades",
        "Na face anterior das pernas e no dorso dos pés há lesões purpúricas "
        "palpáveis, algumas com centro escurecido, que não desaparecem à "
        "digitopressão. Não há livedo reticular, nódulo subcutâneo, úlcera "
        "ou infarto digital. Palidez cutâneo-mucosa acentuada.",
        minutos=3,
        sin=["cutaneo", "purpura", "lesoes", "dermatologico", "extremidades", "pernas"]),

    examinar("nasal", "Inspeção nasal e dos seios da face",
        "Crostas hemáticas aderidas ao septo em ambas as narinas, com mucosa "
        "friável ao toque. Não há perfuração septal, deformidade em sela ou "
        "massa. Os seios da face são indolores à percussão.",
        minutos=3,
        sin=["nariz", "rinoscopia", "seios da face", "via aerea superior", "otorrino"]),

    examinar("neuro", "Exame neurológico dirigido",
        "Pé caído à direita, com força 2/5 para dorsiflexão e eversão, e "
        "hipoestesia no dorso do pé, no território fibular. À esquerda, "
        "fraqueza para abdução do quinto dedo e hipoestesia no território "
        "ulnar. Déficits assimétricos, sem nível medular e sem raiz única. "
        "Reflexos preservados nos demais segmentos.",
        minutos=6, detalhe="leva tempo e quase nunca é feito",
        sin=["neurologico", "forca", "sensibilidade", "reflexos", "pe caido", "nervo"]),

    examinar("articular", "Exame das articulações",
        "Sem sinovite, derrame articular, calor ou deformidade. As "
        "articulações doem à mobilização, sem sinal inflamatório objetivo.",
        minutos=3,
        sin=["articulacoes", "artrite", "sinovite", "osteoarticular"]),

    examinar("abdome", "Exame do abdome e punho-percussão lombar",
        "Abdome plano, indolor, sem visceromegalia, sem massa pulsátil. "
        "Punho-percussão lombar indolor bilateralmente. Bexiga não palpável.",
        minutos=3,
        sin=["abdominal", "barriga", "giordano", "punho percussao", "loja renal"]),

    examinar("fundo_olho", "Fundo de olho",
        "Sem hemorragia, exsudato, papiledema ou lesão vasculítica retiniana. "
        "Cruzamentos arteriovenosos com discreto sinal de hipertensão "
        "crônica.",
        minutos=5, detalhe="normal — e cinco minutos são cinco minutos",
        sin=["fundoscopia", "oftalmoscopia", "retina", "olho"]),

    # ───────────────────── condutas ─────────────────────
    prescrever("oxigenio", "Oxigênio suplementar por cateter nasal",
        "Cateter nasal a 4 L/min. A saturação subiu para 93%.",
        minutos=5, efeito=efeito(spo2=+5), liga=("o2",),
        detalhe="corrige o número, não a causa",
        sin=["o2", "cateter nasal", "suplementar", "mascara", "oxigenoterapia"]),

    prescrever("culturas",
        "Colher três pares de hemocultura e as sorologias antes de qualquer "
        "imunossupressor",
        "Três pares de hemocultura de sítios distintos, sorologias virais e "
        "painel imunológico colhidos e enviados. O material está guardado: "
        "o que for pedido a partir de agora usa esta coleta.",
        minutos=25, liga=("culturas_colhidas",),
        pede=["Hemocultura", "ANCA por imunofluorescência indireta",
              "Anticorpo anti-membrana basal glomerular", "Complemento C3",
              "Complemento C4", "FAN"],
        detalhe="o corticoide estraga a cultura, não o contrário",
        sin=["coletar antes de imunossuprimir", "guardar material", "coleta pre imunossupressao", "colher tudo antes", "preservar culturas"]),

    prescrever("pulso",
        "Pulso de metilprednisolona 1 g por dia, por três dias",
        "Metilprednisolona 1 g endovenosa iniciada. É reversível, cobre as "
        "hipóteses inflamatórias que restam e não compromete o paciente por "
        "meses.",
        minutos=30, liga=("imunossupressao",),
        perigo_sem=("culturas_colhidas",), perigo_liga=("culturas_prejudicadas",),
        perigo="As culturas ainda não haviam sido colhidas quando o "
               "corticoide entrou. A partir daqui, cultura negativa não "
               "afasta infecção neste paciente, e a decisão de imunossuprimir "
               "por meses vai ter de ser tomada sem esse apoio.",
        detalhe="reversível, e é isso que o torna defensável cedo",
        sin=["metilprednisolona", "corticoide", "pulsoterapia", "solumedrol", "corticoterapia"]),

    prescrever("rituximabe",
        "Rituximabe 375 mg/m² por semana, quatro doses",
        "Rituximabe iniciado. Não exige ajuste para a função renal, poupa "
        "gônada e tem eficácia equivalente à ciclofosfamida na indução.",
        minutos=60, liga=("imunossupressao", "rituximabe"),
        detalhe="não precisa de ajuste renal",
        sin=["rtx", "anti cd20", "mabthera"]),

    prescrever("cfx_plena",
        "Ciclofosfamida endovenosa 15 mg/kg, dose plena",
        "Ciclofosfamida endovenosa em dose plena, sem correção.",
        minutos=60, liga=("imunossupressao", "cfx_plena"),
        detalhe="15 mg/kg, sem correção",
        sin=["ciclofosfamida dose plena", "ciclofosfamida sem ajuste", "ciclofosfamida cheia"]),

    prescrever("cfx_ajustada",
        "Ciclofosfamida endovenosa com dose reduzida pela idade e pela "
        "função renal",
        "Ciclofosfamida endovenosa com redução por idade acima de 60 anos e "
        "por filtração glomerular abaixo de 30 mL/min/1,73 m².",
        minutos=60, liga=("imunossupressao", "cfx_ajustada"),
        detalhe="a redução que a bula pede e quase ninguém faz",
        sin=["ciclofosfamida ajustada", "ciclofosfamida reduzida", "ciclofosfamida com ajuste renal"]),

    prescrever("pjp",
        "Sulfametoxazol-trimetoprima profilático para //Pneumocystis//",
        "Sulfametoxazol-trimetoprima 400/80 mg por dia iniciado, pelo tempo "
        "do curso de indução.",
        minutos=10, liga=("pjp",), detalhe="400/80 mg/dia",
        sin=["bactrim", "sulfametoxazol", "smz tmp", "profilaxia pneumocystis", "cotrimoxazol"]),

    prescrever("plasmaferese",
        "Plasmaférese, sessões diárias",
        "Plasmaférese iniciada, com reposição de albumina. Retira o "
        "anticorpo circulante; não interrompe a produção dele.",
        minutos=180, liga=("plasmaferese",),
        detalhe="ganho renal, custo infeccioso",
        sin=["plasma exchange", "aferese", "troca plasmatica", "pex"]),

    prescrever("dialise", "Hemodiálise de urgência",
        "Cateter de duplo lúmen em veia jugular interna direita e primeira "
        "sessão de hemodiálise. Corrige o potássio e a volemia; não trata a "
        "doença.",
        minutos=240, liga=("dialise",), efeito=efeito(potassio=-1.2),
        detalhe="corrige o potássio, não o glomérulo",
        sin=["hemodialise", "terapia de substituicao renal", "cateter de dialise", "trs"]),

    prescrever("transfusao", "Transfundir duas unidades de concentrado de hemácias",
        "Duas unidades de concentrado de hemácias transfundidas, sem "
        "intercorrência.",
        minutos=180, efeito=efeito(hb=+1.6), liga=("transfundido",),
        uma_vez=False, detalhe="corrige o número, e o alvéolo segue sangrando",
        sin=["transfundir", "concentrado de hemacias", "hemotransfusao", "sangue"]),

    prescrever("intubar", "Intubação orotraqueal e ventilação mecânica",
        "Intubação em sequência rápida, ventilação protetora. A saturação "
        "estabilizou.",
        minutos=45, liga=("vm",), efeito=efeito(spo2=+6),
        detalhe="ganha tempo; não devolve alvéolo",
        sin=["intubacao", "ventilacao mecanica", "iot", "tubo", "ventilar"]),

    prescrever("antibiotico",
        "Antibiótico de amplo espectro, empírico",
        "Piperacilina-tazobactam iniciada após coleta de culturas.",
        minutos=20, liga=("antibiotico",),
        detalhe="cobre o que a imunossupressão pode ter aberto",
        sin=["atb", "amplo espectro", "piperacilina", "tazobactam", "antibioticoterapia"]),
]

# ═══════════════════════ os pontos de decisão ═══════════════════════
#
# Não é o cardápio de condutas à vista o tempo todo — isso é prova de múltipla
# escolha, e o grupo escolhe pela lista em vez de pensar. São dois ou três
# caminhos concretos, oferecidos no momento em que o caso realmente exige uma
# decisão. A linha de comando continua aberta: quem quiser fazer outra coisa,
# escreve, e o bloco de caminhos some.

DECISOES = [
    decisao("primeira_hora",
        "Começa a imunossupressão hoje, ou espera o resultado?",
        contexto="Duas horas de internação. A creatinina segue subindo, e as "
                 "sorologias específicas levam de dois a cinco dias para "
                 "voltar. O que for decidido agora vale para os dois dias em "
                 "que não haverá resultado nenhum.",
        quando=[campo("horas", ">=", 2), sinal("imunossupressao", False)],
        volta_em=8,
        caminhos=[
            caminho("Colher culturas e sorologias agora e iniciar pulso de "
                    "metilprednisolona hoje",
                    faz=["culturas", "pulso"],
                    porque="O pulso é reversível e cobre as hipóteses "
                           "inflamatórias que restam. Colher antes preserva a "
                           "hemocultura e a imunofluorescência, que é o que a "
                           "biópsia dos próximos dias ainda vai poder dizer."),
            caminho("Colher tudo agora e aguardar o resultado antes de "
                    "qualquer imunossupressor",
                    faz=["culturas"], espera=1440,
                    porque="O rigor de não tratar sem diagnóstico é "
                           "defensável em quase toda doença, e é caro nesta: a "
                           "crescente celular vira crescente fibrosa em dias, "
                           "e o que fibrosa não volta."),
            caminho("Ainda não decidir — seguir investigando por mais uma hora",
                    espera=60,
                    porque="Adiar também é uma decisão, e ela tem preço no "
                           "cabeçalho."),
        ]),

    decisao("hipoxemia",
        "A saturação não sustenta. O que você faz?",
        contexto="A troca gasosa vem piorando apesar do que já foi feito, e o "
                 "alvéolo cheio de sangue é um shunt: oxigênio ofertado não "
                 "encontra membrana para atravessar.",
        quando=[campo("spo2", "<", 82), sinal("vm", False)],
        volta_em=4,
        caminhos=[
            caminho("Intubar e ventilar", faz=["intubar"],
                    porque="Não trata a vasculite; compra o tempo de que a "
                           "imunossupressão precisa para agir."),
            caminho("Aumentar a oferta de oxigênio e reavaliar em uma hora",
                    faz=["oxigenio"], espera=60,
                    porque="Num shunt verdadeiro, aumentar a fração inspirada "
                           "corrige pouco — e a hora passa."),
        ]),

    decisao("hipercalemia",
        "O potássio passou de 6,5 mEq/L. O que você faz?",
        contexto="Lesão renal aguda oligúrica com potássio em ascensão. A "
                 "hipercalemia é previsível, mensurável, e mata antes da "
                 "doença de base.",
        quando=[campo("potassio", ">", 6.5), sinal("dialise", False)],
        volta_em=6,
        caminhos=[
            caminho("Hemodiálise de urgência", faz=["dialise"],
                    porque="Corrige o potássio e a volemia. Não trata a "
                           "doença, e não é sentença de diálise definitiva."),
            caminho("Medidas clínicas e reavaliar em seis horas", espera=360,
                    porque="Insulina com glicose e beta-agonista deslocam o "
                           "potássio para dentro da célula por poucas horas. "
                           "Num rim que não filtra, deslocar não é retirar."),
        ]),

    decisao("febre_inducao",
        "Febre sob imunossupressão. Vasculite em atividade, ou infecção?",
        contexto="O mesmo quadro admite as duas leituras, e elas pedem "
                 "condutas opostas: uma manda aumentar a imunossupressão, a "
                 "outra manda cobrir o que ela abriu.",
        quando=[sinal("imunossupressao"), sinal("infeccao"),
                sinal("antibiotico", False)],
        volta_em=12,
        caminhos=[
            caminho("Colher culturas e iniciar antibiótico de amplo espectro, "
                    "mantendo a imunossupressão",
                    faz=["antibiotico"],
                    porque="A causa de morte precoce na vasculite ANCA tratada "
                           "é a infecção, não a vasculite. Quando as duas são "
                           "possíveis, trata-se a que mata mais rápido e "
                           "reavalia-se."),
            caminho("Presumir atividade da vasculite e manter a conduta, "
                    "reavaliando em doze horas",
                    espera=720,
                    porque="É a leitura que a febre convida a fazer, e é a "
                           "que o hemograma costuma desmentir."),
        ]),
]


# ═══════════════════════════ a doença anda ═══════════════════════════
#
# As taxas foram calibradas para reproduzir o curso descrito na literatura de
# glomerulonefrite rapidamente progressiva não tratada: creatinina subindo
# cerca de 1 mg/dL por dia, saturação caindo com o acúmulo de sangue alveolar,
# e hemoglobina caindo sem sangramento externo visível.

EVOLUCAO = evolucao(
    # a doença não tratada não tem para onde ir: piora em linha reta
    base=taxa(creatinina=+0.042, spo2=-0.10, hb=-0.024, potassio=+0.018,
              diurese=-0.45),
    # bônus e ônus que somam por cima do rumo, sem substituí-lo
    quando={
        "o2": taxa(spo2=+0.10),
        "plasmaferese": taxa(creatinina=-0.012),
        "infeccao": taxa(spo2=-0.30, creatinina=+0.035),
        "antibiotico": taxa(spo2=+0.14),
        "transfundido": taxa(hb=+0.004),
        # sem tratamento a capilarite não fica parada: o alvéolo que ainda
        # trocava gás vai sendo ocupado, e a queda acelera
        "hemorragia_macica": taxa(spo2=-0.28, potassio=+0.014, hb=-0.012),
    },
    # a recuperação tem patamar, e chega nele desacelerando. A ordem importa:
    # a fibrose vem depois e sobrepõe o alvo renal da imunossupressão, porque
    # cicatriz não responde a tratamento nenhum.
    alvos={
        "imunossupressao": rumo(creatinina=(1.6, 40), spo2=(95, 16),
                                hb=(9.4, 70), potassio=(4.2, 14),
                                diurese=(72, 22)),
        "fibrose": rumo(creatinina=(4.8, 55), diurese=(20, 40)),
        "dialise": rumo(potassio=(4.2, 5), creatinina=(3.9, 9)),
        "vm": rumo(spo2=(93, 5)),
    },
    marcos=[
        marco(48, "Segundo dia sem tratamento dirigido. A hemoptise aumentou, "
                  "o infiltrado progrediu nos dois terços inferiores e a "
                  "hemoglobina segue caindo sem sangramento externo: o alvéolo "
                  "continua sangrando.",
              liga=("hemorragia_macica",), impede=("imunossupressao",)),
        marco(72, "Terceiro dia sem tratamento dirigido. A perda de função "
                  "renal deixa de ser inteiramente reversível: a crescente "
                  "celular, que é tecido inflamado, começa a virar crescente "
                  "fibrosa, que é cicatriz.",
              liga=("fibrose",), impede=("imunossupressao",)),
        marco(120, "Quinto dia de ciclofosfamida em dose plena com filtração "
                   "glomerular abaixo de 30 mL/min/1,73 m². Hemograma com 900 "
                   "leucócitos e 210 neutrófilos; febre de 39,2 °C com "
                   "calafrio. Neutropenia febril, mais precoce e mais grave do "
                   "que o esperado para o esquema.",
              liga=("neutropenia", "infeccao"), exige=("cfx_plena",)),
        marco(96, "Febre de 38,6 °C com nova opacidade assimétrica à direita, "
                  "sob imunossupressão e sem profilaxia. Culturas em "
                  "andamento.",
              liga=("infeccao",), exige=("imunossupressao",),
              impede=("pjp", "antibiotico")),
        marco(168, "Sétimo dia. A hemoptise cessou e a diurese vem subindo há "
                   "quarenta e oito horas.",
              exige=("imunossupressao",), impede=("infeccao",)),
    ],
)


# ═══════════════════════════ o que fecha o diagnóstico ═══════════════════════

GATILHOS = {
    # o diagnóstico não é anunciado por nenhuma tela: ele acende quando o
    # exame que o estabelece volta do laboratório
    "ANCA por imunofluorescência indireta": ["diagnostico"],
    "Anti-mieloperoxidase": ["diagnostico"],
    "Biópsia renal — imunofluorescência": ["diagnostico"],
    "Biópsia renal — microscopia óptica": ["diagnostico"],
    "Sedimento urinário": ["sedimento_visto"],
    "Hemocultura": ["culturas_colhidas"],
    "Cultura do lavado broncoalveolar": ["culturas_colhidas"],
}


# ═══════════════ a imagem que o exame devolve ═══════════════
#
# O resultado de imagem e de anatomia patológica não é texto: é a lâmina e o
# corte. Quem pede a tomografia recebe a tomografia, no fundo escuro em que ela
# é lida, com o crédito e a licença ao pé.

IMG = Path(__file__).parent / "img"

IMAGENS = {
    "Tomografia de tórax": dict(
        arquivo="tc_torax_vidro_fosco.jpg",
        legenda="Cortes axiais, coronal e sagital. Imagem ilustrativa, de "
                "repositório aberto; não pertence a este paciente.",
        credito="Hellerhoff · Wikimedia Commons · CC BY-SA 4.0"),
    "Biópsia renal — microscopia óptica": dict(
        arquivo="biopsia_renal_cortex.jpg",
        legenda="Córtex renal, grande aumento. Imagem ilustrativa, de "
                "repositório aberto; não pertence a este paciente.",
        credito="Nephron · Wikimedia Commons · CC BY-SA 3.0"),
    "ANCA por imunofluorescência indireta": dict(
        arquivo="panca_imunofluorescencia.jpg",
        legenda="Neutrófilos fixados em etanol, imunofluorescência indireta. "
                "Imagem ilustrativa, de repositório aberto.",
        credito="Simon Caulton · Wikimedia Commons · CC BY-SA 3.0"),
}


# ═══════════════════════════ os desfechos ═══════════════════════════
#
# Calculados do estado final, na ordem: vence o primeiro que casar. O último é
# incondicional, para que nunca exista uma condução sem desfecho.

DESFECHOS = [
    desfecho("obito_hemorragia", "Óbito por hemorragia alveolar",
        "A saturação caiu abaixo do que a troca gasosa suporta, sem via aérea "
        "protegida. A parada foi hipoxêmica.",
        quando=[campo("spo2", "<", 63), sinal("vm", False)],
        qualidade="pior", automatico=True,
        porque="O alvéolo cheio de sangue é um shunt: o oxigênio ofertado não "
               "encontra membrana para atravessar. Suporte ventilatório não "
               "trata a vasculite, mas é o que mantém o paciente vivo até o "
               "tratamento agir. Sem ele, o tempo que a imunossupressão "
               "precisa não existe."),

    desfecho("obito_sepse", "Óbito por infecção sob imunossupressão",
        "Choque séptico refratário em paciente sob imunossupressão de indução, "
        "com foco pulmonar.",
        quando=[sinal("infeccao"), campo("spo2", "<", 70)],
        qualidade="pior", automatico=True,
        porque="A causa de morte precoce na vasculite ANCA tratada é a "
               "infecção, não a vasculite. Ela vem da dose, da ausência de "
               "profilaxia e da imunossupressão mantida enquanto a febre "
               "corria. As três são decisões, não acaso."),

    desfecho("obito_hipercalemia", "Óbito por hipercalemia",
        "Parada em atividade elétrica sem pulso, com potássio acima de "
        "7,5 mEq/L e sem terapia de substituição renal instituída.",
        quando=[campo("potassio", ">", 7.5), sinal("dialise", False)],
        qualidade="pior", automatico=True,
        porque="A hipercalemia da lesão renal aguda oligúrica é previsível e "
               "mensurável, e mata antes da doença de base. Nenhuma "
               "investigação diagnóstica muda essa conta."),

    desfecho("alta_boa", "Alta no vigésimo primeiro dia, sem diálise",
        "Creatinina em queda sustentada, diurese recuperada, hemoptise "
        "cessada. Segue em manutenção, com consulta e exames já agendados.",
        quando=[sinal("diagnostico"), sinal("dialise", False),
                sinal("fibrose", False), sinal("infeccao", False),
                campo("creatinina", "<", 2.6)],
        qualidade="melhor",
        porque="O tratamento entrou enquanto a crescente ainda era celular. "
               "Crescente celular é tecido inflamado e responde; crescente "
               "fibrosa é cicatriz e não responde. Toda a diferença entre "
               "este desfecho e os outros está em quantas horas se passaram "
               "antes da primeira dose."),

    desfecho("alta_complicada",
        "Alta no trigésimo quarto dia, após passagem pela terapia intensiva",
        "A vasculite entrou em remissão e a função renal recuperou. No meio do "
        "caminho houve um episódio infeccioso grave sob imunossupressão, com "
        "treze dias de antibiótico e suporte em terapia intensiva.",
        quando=[sinal("diagnostico"), sinal("infeccao"),
                campo("creatinina", "<", 3.0), sinal("dialise", False)],
        qualidade="medio",
        porque="A doença foi tratada a tempo e o rim respondeu. O que custou "
               "duas semanas de internação foi a infecção — e ela vem da dose "
               "não ajustada à filtração glomerular, da profilaxia que não foi "
               "prescrita, ou da imunossupressão iniciada com as culturas "
               "ainda por colher. As três são decisões, não azar."),

    desfecho("alta_sequela", "Alta com doença renal crônica estabelecida",
        "Função renal estabilizada num patamar pior que o da admissão, sem "
        "necessidade de diálise. Segue em acompanhamento nefrológico.",
        quando=[sinal("diagnostico"), sinal("dialise", False),
                campo("creatinina", "<", 5.0)],
        qualidade="medio",
        porque="Parte dos glomérulos foi perdida antes de o tratamento "
               "começar, e não volta. O paciente está vivo e fora de diálise, "
               "e a reserva renal que ele tem hoje é a que sobrou do tempo "
               "que se levou para decidir."),

    desfecho("dialise_definitiva", "Diálise definitiva",
        "Sem recuperação de função renal após o controle da doença. Entrou em "
        "programa crônico de hemodiálise e foi encaminhado à fila de "
        "transplante.",
        quando=[sinal("dialise"), sinal("fibrose")],
        qualidade="pior",
        porque="A doença foi controlada, e o rim não. Quando a maioria dos "
               "glomérulos já fibrosou, controlar a inflamação preserva o "
               "pulmão e a vida, e não devolve filtração."),

    desfecho("dialise_temporaria", "Alta em diálise, com chance de recuperação",
        "Saiu do hospital dependente de diálise, com biópsia mostrando "
        "crescentes ainda em parte celulares. Recuperação possível em semanas "
        "a meses.",
        quando=[sinal("dialise"), sinal("diagnostico")],
        qualidade="medio",
        porque="Diálise instituída por indicação metabólica não é sentença: "
               "parte dos pacientes com glomerulonefrite crescêntica tratada a "
               "tempo recupera função ao longo de três a seis meses. O que "
               "define é a proporção de crescentes ainda celulares na biópsia."),

    desfecho("sem_diagnostico", "Encerrado sem diagnóstico",
        "A condução terminou sem que a causa da síndrome pulmão-rim tivesse "
        "sido estabelecida. O paciente segue internado, ainda sem tratamento "
        "dirigido.",
        quando=[sinal("diagnostico", False)],
        qualidade="pior",
        porque="Sem o painel imunológico ou a biópsia, não há como separar as "
               "causas que exigem imunossupressão das que a contraindicam — e "
               "o tempo gasto sem essa separação é tempo cobrado do glomérulo."),

    desfecho("indefinido", "Evolução indeterminada",
        "O paciente segue internado, com a doença sob tratamento e a função "
        "renal ainda em definição.",
        quando=[], qualidade="medio",
        porque="A condução foi encerrada antes de a evolução se definir. Em "
               "sala, este é o momento de perguntar ao grupo o que ele faria "
               "no dia seguinte, e por quê."),
]


# ═══════════════════ o que a revisão cobra no fim ═══════════════════
#
# Não é gabarito: é a lista do que teria mudado a condução e ficou de fora.
# Aparece uma vez só, depois do desfecho, quando não há mais o que decidir.

REVISAO = [
    dict(rotulo="Sedimento urinário", chave="Sedimento urinário",
         porque="É o exame mais barato do caso e o único que separa "
                "sangramento glomerular de urológico em minutos. Sem ele, a "
                "hipótese de duas doenças independentes fica de pé, e a "
                "investigação segue atrás do pulmão."),
    dict(rotulo="ANCA e anti-mieloperoxidase",
         chave="ANCA por imunofluorescência indireta", sinalizador="diagnostico",
         porque="É o que nomeia a doença. Leva dois dias, e é por isso que "
                "precisa ser pedido na primeira hora, não quando a dúvida "
                "aperta."),
    dict(rotulo="Anticorpo anti-membrana basal glomerular",
         chave="Anticorpo anti-membrana basal glomerular",
         porque="É o exame de maior urgência do painel: na doença anti-MBG a "
                "demora de poucos dias custa a função renal de forma "
                "definitiva, e o tratamento é diferente."),
    dict(rotulo="Complemento C3 e C4", chave="Complemento C3",
         porque="Separa em dois grupos as glomerulonefrites — as que consomem "
                "complemento e as que não consomem — por quase nada e em "
                "poucas horas."),
    dict(rotulo="Culturas antes de imunossuprimir", chave="Hemocultura",
         sinalizador="culturas_colhidas",
         porque="Endocardite faz síndrome pulmão-rim e contraindica "
                "imunossupressão. E, uma vez iniciado o corticoide, cultura "
                "negativa deixa de valer."),
    dict(rotulo="Lavado broncoalveolar", chave="Lavado broncoalveolar",
         porque="Comprova a hemorragia alveolar pelas alíquotas "
                "progressivamente hemorrágicas e pelos hemossiderófagos, e é "
                "a cultura dele que autoriza a imunossupressão."),
    dict(rotulo="Biópsia renal", chave="Biópsia renal — microscopia óptica",
         porque="Distingue pauci-imune de depósito linear e de depósito "
                "granular, classifica por Berden e diz quanto ainda é "
                "reversível. É o que separa tratar de tratar em vão."),
    dict(rotulo="Revisão nominal dos medicamentos", chave="medicacoes",
         sinalizador="medicacoes_revisadas",
         porque="Hidralazina, propiltiouracila, minociclina e levamisol "
                "produzem vasculite ANCA indistinguível da primária, e o "
                "tratamento começa por suspender a droga. A pergunta tem de "
                "ser nominal — “que remédios você toma?” não a responde."),
    dict(rotulo="Profilaxia para //Pneumocystis//", chave="pjp",
         sinalizador="pjp",
         porque="Sob indução com ciclofosfamida ou rituximabe em dose plena, "
                "a pneumocistose é a infecção oportunista que mais aparece, e "
                "a profilaxia com sulfametoxazol-trimetoprima é barata. "
                "Recomendação de grau B da EULAR, sobre evidência de nível 3b."),
]

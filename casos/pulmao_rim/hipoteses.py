"""As listas do caso, em níveis — do problema à doença.

O caso não abre com o diferencial de síndrome pulmão-rim. Abrir assim é entregar
o desfecho: quem lê "vasculite associada ao ANCA" e "doença anti-membrana basal"
lado a lado no fim do exame físico já sabe onde o caso vai parar, e o resto da
sessão vira confirmação.

Aqui a lista começa larga e no nível em que o paciente se apresenta — de onde
vem o sangue, o que amarra oito semanas de doença — e só estreita quando um
resultado autoriza. São quatro níveis:

    1. as síndromes  ·  tórax, sistêmica e, quando o rim aparecer, renal
    2. a etiologia   ·  só depois que hemorragia alveolar E glomerulonefrite
                        estiverem estabelecidas é que existe "pulmão-rim"
    3. dentro do ANCA ·  qual das vasculites, e por quais critérios

`exige` diz o que TERIA de ser verdade para o candidato ser a resposta — não o
que este paciente tem. É a diferença entre o método do discussant e apontar o
dedo: escrever "púrpura palpável e mononeurite múltipla" na linha da vasculite
ANCA entrega o caso antes do primeiro exame.

Este módulo vive separado de `caso.py` porque os blocos de ramo em `arvore.py`
também precisam das listas, e o import de `caso.py` seria circular.
"""

from motor.desenhos import hip

# ───────────────── nível 1 · o tórax, antes de qualquer exame ─────────────────
#
# A pergunta não é "que doença é". É "de onde vem o sangue" — e sangue que sai
# pela boca pode vir do nariz, do brônquio, do alvéolo ou do capilar pulmonar.
# A hemorragia alveolar é uma linha desta lista, não o ponto de partida dela.

TORAX = [
    hip("via_aerea", "Sangramento de via aérea superior, deglutido ou aspirado",
        "A fonte visível à rinoscopia ou à broncoscopia, com parênquima "
        "poupado à tomografia"),
    hip("hemorragia", "Hemorragia alveolar difusa",
        "Alíquotas progressivamente hemorrágicas ao lavado, ou hemossiderófagos "
        "acima de 20% dos macrófagos"),
    hip("pneumonia", "Pneumonia com escarro hemoptoico",
        "Consolidação com broncograma aéreo, e um agente isolado no escarro, "
        "no lavado ou na hemocultura"),
    hip("tuberculose", "Tuberculose pulmonar",
        "Baciloscopia, teste molecular ou cultura positivos, com padrão "
        "radiológico compatível"),
    hip("neoplasia", "Neoplasia broncopulmonar sangrante",
        "Massa, nódulo ou lesão endobrônquica, e o tecido ao anatomopatológico"),
    hip("tep", "Tromboembolismo com infarto pulmonar",
        "Falha de enchimento à angiotomografia, com opacidade de base pleural"),
    hip("congestao", "Congestão pulmonar por insuficiência cardíaca",
        "Cardiomegalia, derrame, terceira bulha ou peptídeo natriurético "
        "elevado"),
]

# ───────────────── nível 1 · o que amarra oito semanas de doença ─────────────
#
# Febre, perda de peso, artralgia migratória, púrpura e mononeurite múltipla.
# A pergunta é se existe um mecanismo único — e "vasculite" é uma resposta
# possível entre outras, não a resposta.

SISTEMICO = [
    hip("infeccao_arrastada", "Infecção arrastada com repercussão sistêmica",
        "Um foco e um agente identificados, e regressão ao tratá-lo"),
    hip("endocardite", "Endocardite infecciosa",
        "Hemocultura positiva em amostras separadas e vegetação ao "
        "ecocardiograma"),
    hip("vasculite_sist", "Vasculite sistêmica de pequenos vasos",
        "Lesão simultânea de leitos capilares distantes, sem outro mecanismo "
        "que os una"),
    hip("conectivopatia", "Doença difusa do tecido conjuntivo",
        "Autoanticorpo específico, e um padrão de órgão-alvo que lhe "
        "corresponda"),
    hip("neoplasia_oculta", "Neoplasia oculta com síndrome paraneoplásica",
        "O tumor, encontrado — e a síndrome que regride quando ele é tratado"),
    hip("droga_sist", "Reação sistêmica a droga",
        "Uma droga com esse perfil em uso, e regressão ao suspendê-la"),
]

# ───────────────── nível 1 · onde está a lesão renal ─────────────────
#
# Só entra em cena quando o rim entra: até a creatinina voltar, esta lista não
# existe. Nenhuma linha aqui é uma doença — são compartimentos do néfron.

RIM = [
    hip("pre_renal", "Hipoperfusão renal",
        "Sódio urinário baixo, sedimento limpo, e resposta à reposição de "
        "volume"),
    hip("nta", "Necrose tubular aguda",
        "Cilindros granulosos pigmentares, sem dismorfismo e sem cilindro "
        "hemático"),
    hip("nia", "Nefrite intersticial aguda",
        "Leucocitúria estéril com cilindros leucocitários, e uma droga ou "
        "infecção que a expliquem"),
    hip("glomerular", "Glomerulonefrite",
        "Hemácias dismórficas e cilindros hemáticos, com proteinúria"),
    hip("obstrutiva", "Obstrução do trato urinário",
        "Dilatação pielocalicial à ultrassonografia"),
]

# ───────────────── nível 2 · a etiologia ─────────────────
#
# Esta lista só se justifica depois que as duas síndromes estiverem
# estabelecidas: hemorragia alveolar de um lado, glomerulonefrite do outro.
# Antes disso ela é um chute com nome bonito.

HIPOTESES = [
    hip("anca", "Vasculite de pequeno vaso associada ao ANCA",
        "ANCA reagente e glomerulonefrite sem depósitos imunes na biópsia"),
    hip("mbg", "Doença anti-membrana basal glomerular",
        "Anti-MBG reagente e depósito linear ao longo da membrana basal"),
    hip("lupus", "Lúpus eritematoso sistêmico",
        "FAN e anti-DNA reagentes, complemento consumido, depósitos granulosos"),
    hip("crio", "Crioglobulinemia mista",
        "Crioglobulinas positivas e C4 desproporcionalmente baixo"),
    hip("iga", "Vasculite por IgA",
        "Depósito mesangial dominante de IgA à imunofluorescência, com púrpura "
        "e artrite"),
    hip("endocardite", "Endocardite infecciosa",
        "Hemocultura positiva e vegetação ao ecocardiograma"),
    hip("lepto", "Leptospirose na forma pulmonar hemorrágica",
        "Exposição a água de enchente ou a roedor, e sorologia ou PCR "
        "reagente — no Ceará, entra na lista por epidemiologia"),
    hip("droga", "Vasculite induzida por droga",
        "Hidralazina, propiltiouracila, minociclina ou levamisol em uso"),
]

# ───────────────── nível 3 · dentro da vasculite associada ao ANCA ────────────
#
# O ANCA reagente não é o fim da linha: fecha um grupo, não uma doença. O que
# separa as quatro é o órgão acometido e o tecido, não o anticorpo.

DENTRO = [
    hip("mpa", "Poliangeíte microscópica",
        "MPO-ANCA, sem granuloma e sem doença destrutiva de via aérea superior"),
    hip("gpa", "Granulomatose com poliangeíte",
        "Doença de via aérea superior e granuloma em qualquer tecido — mais "
        "frequente com PR3-ANCA, e não exclusiva dele"),
    hip("egpa", "Granulomatose eosinofílica com poliangeíte",
        "Asma, eosinofilia acima de 1.000/mm³ e infiltrado eosinofílico ao "
        "tecido"),
    hip("renal_limitada", "Vasculite associada ao ANCA limitada ao rim",
        "Glomerulonefrite pauci-imune sem acometimento de nenhum outro órgão"),
    hip("droga_anca", "Vasculite associada ao ANCA induzida por droga",
        "Hidralazina, propiltiouracila, minociclina ou levamisol, com títulos "
        "muito altos e positividade dupla frequente"),
]

"""A lista de hipóteses do caso, em módulo próprio.

Ela vive aqui, e não em `caso.py`, porque os blocos de ramo em `arvore.py`
também precisam dela: um grupo que escolheu o painel completo não passa pelos
quadros do tronco, e ficaria sem ver a lista ser podada. Se `arvore.py`
importasse de `caso.py`, o import seria circular.
"""

from motor.desenhos import hip

# ─────────────────────────── o diferencial ───────────────────────────
#
# A lista que o grupo levanta depois do exame físico, e que cada dado novo
# poda. `exige` diz o que TERIA de ser verdade para o candidato ser o
# diagnóstico — não o que este paciente tem. É a diferença entre o método do
# discussant e apontar o dedo: escrever "púrpura palpável e mononeurite
# múltipla" na linha da vasculite ANCA entrega o caso antes do primeiro exame.

HIPOTESES = [
    hip("urologico", "Sangramento urinário com pneumopatia à parte",
        "Hemácias isomórficas, sem cilindros — e duas doenças independentes"),
    hip("anca", "Vasculite de pequeno vaso associada ao ANCA",
        "ANCA reagente e glomerulonefrite sem depósitos imunes na biópsia"),
    hip("mbg", "Doença anti-membrana basal glomerular",
        "Anti-MBG reagente e depósito linear ao longo da membrana basal"),
    hip("lupus", "Lúpus eritematoso sistêmico",
        "FAN e anti-DNA reagentes, complemento consumido, depósitos granulosos"),
    hip("crio", "Crioglobulinemia mista",
        "Crioglobulinas positivas e C4 desproporcionalmente baixo"),
    hip("endocardite", "Endocardite infecciosa",
        "Hemocultura positiva e vegetação ao ecocardiograma"),
    hip("infeccao", "Infecção pulmonar grave com lesão renal aguda",
        "Um foco infeccioso identificado, e o rim acompanhando a sepse"),
    hip("lepto", "Leptospirose na forma pulmonar hemorrágica",
        "Exposição a água de enchente ou a roedor, e sorologia ou PCR "
        "reagente — no Ceará, entra na lista por epidemiologia"),
    hip("droga", "Vasculite induzida por droga",
        "Hidralazina, propiltiouracila, minociclina ou levamisol em uso"),
]

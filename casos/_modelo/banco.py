"""Banco de exames do caso modelo.

Regra de ferro: o banco entrega o valor encontrado e o valor de referência.
Nada de interpretação, comentário didático ou selo de relevância. Um analito
por entrada; nome de painel existe só como sinônimo.
"""

from motor.exames import an

BANCO = [
    an("Creatinina", "1,0 mg/dL", ref="até 1,3 mg/dL", cat="Bioquímica",
       sin=["creatinina", "função renal"]),
]

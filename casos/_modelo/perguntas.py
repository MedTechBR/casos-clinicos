"""Perguntas do caso modelo.

4 ou 5 alternativas, 1 ou 2 corretas. O enunciado começa pelo dado e termina
pelo pedido. A primeira pergunta NUNCA lista as hipóteses diagnósticas.

`ordem` permuta as alternativas na tela: sem isso a letra correta se concentra,
e `verificar.py::v_gabarito` recusa. `titulo_resposta` é a ideia que a pergunta
ensina — vira a manchete do slide de resposta, no lugar da letra.
"""

from motor.perguntas import alt, pergunta

P1 = pergunta(
    1,
    "O dado, e então o pedido?",
    [
        alt("Primeira alternativa", "Por que ela não fecha."),
        alt("Segunda alternativa", "Por que ela fecha.", certa=True),
        alt("Terceira alternativa", "Por que ela não fecha."),
        alt("Quarta alternativa", "Por que ela não fecha."),
    ],
    titulo_resposta="A ideia que esta pergunta ensina",
    ordem=[0, 2, 1, 3],
)

"""Modelo de caso novo. Copie a pasta e troque o conteúdo.

    cp -r casos/_modelo casos/<nome_do_caso>
    python3 build.py <nome_do_caso>
    python3 ferramentas/densidade.py <nome_do_caso> --aplicar
    python3 ferramentas/verificar.py <nome_do_caso>

A arquitetura que este modelo já traz é a do Case Records: o caso se abre aos
poucos, o grupo levanta o diferencial, cada dado poda uma linha, e o nome da
doença só aparece quando o percurso terminou. Não entregue o diagnóstico numa
tabela antes do primeiro exame — `verificar.py::v_sem_spoiler` recusa.
"""

from pathlib import Path

from motor.conteudo import box, cols, exame, nota, p, painel, passo, tabela
from motor.desenhos import hip, linha_do_tempo, marco, quadro
from motor.slides import bloco, capa, discussao, momento, narrativa

# O diferencial. `exige` diz o que TERIA de ser verdade para o candidato ser o
# diagnóstico — nunca o que este paciente tem.
HIPOTESES = [
    hip("a", "Primeira hipótese", "O que teria de ser verdade para ela fechar"),
    hip("b", "Segunda hipótese", "O que teria de ser verdade para ela fechar"),
    hip("c", "Terceira hipótese", "O que teria de ser verdade para ela fechar"),
]

from .banco import BANCO  # noqa: E402
from .perguntas import P1  # noqa: E402

TITULO = "Título do caso, na forma do periódico"
SLUG = "modelo"
RODAPE = "Nome da síndrome · caso interativo"
IMG = Path(__file__).parent / "img"

SLIDES = [
    capa(
        TITULO,
        "Uma linha de subtítulo, com o arco temporal.",
        "**N blocos de caso · N perguntas · N minutos** O caso avança em blocos "
        "de informação nova. As perguntas servem para abrir discussão, não para "
        "testar memória.",
        "Caso autoral, construído para ensino. O paciente é ficcional. As "
        "imagens são ilustrativas, de repositórios de licença aberta. Créditos "
        "no slide final.",
    ),
    narrativa("O caso · bloco 1", "Apresentação",
        p("Prosa corrida, como no periódico. Marcos temporais dentro da frase, "
          "sinais vitais narrados. Nunca em tópicos."),
        passo(p("Cada parágrafo seguinte é um passo da revelação.")),
    ),
    momento("Segunda parte", "Diagnóstico diferencial",
        "A partir daqui o caso para de contar e começa a testar.",
        ident="p2"),
    discussao("O que pode explicar o conjunto",
        quadro(HIPOTESES, titulo="Levantado pelo grupo, ao fim do exame físico"),
        nota("Como conduzir",
            p("Não mostre o quadro pronto. Peça as hipóteses à turma primeiro.")),
        ident="quadro_1",
    ),
    P1,
    discussao("O que o primeiro exame poda",
        quadro(HIPOTESES, {"a": ("derrubada", "o motivo, que é o que se ensina")},
               titulo="Depois do primeiro exame", novos=["a"]),
        ident="quadro_2",
    ),
]

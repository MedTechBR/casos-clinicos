"""Monta a biblioteca — a tela que lista os casos.

Uso:  python3 build_biblioteca.py
"""

import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent
sys.path.insert(0, str(RAIZ))

from motor.biblioteca import caso, montar  # noqa: E402

CASOS = [
    caso(slug="pulmao_rim",
         titulo="O sangue que não saiu",
         # O cartão precisa deixar você escolher o caso sem entregar o
         # diagnóstico ao aluno: o subtítulo diz de quem se trata e o que
         # aconteceu, em sinais e sintomas.
         subtitulo="Homem de 63 anos, oito semanas de doença tratada duas "
                   "vezes como outra coisa, e uma piora que começou três "
                   "dias antes da internação.",
         # "Nefrologia · Pneumologia" no cartão entrega a síndrome antes de o
         # aluno abrir o caso, do mesmo jeito que o título entregava.
         especialidade="Clínica médica · Emergência",
         minutos=60, decisoes=12, desfechos=4, nivel="os dois", cor="vermelho",
         capa="cena_admissao.jpg", arquivo="pulmao-rim.html?v=20260909-nejm"),

    caso(slug="cocaina_levamisol", titulo="À flor da pele",
         subtitulo="Uma mulher de 34 anos volta ao atendimento após uma mudança nas lesões da pele.",
         especialidade="Clínica médica · Emergência", minutos=55, decisoes=12,
         desfechos=4, nivel="os dois", cor="roxo",
         capa="../../cocaina_levamisol/img/cena.png", arquivo="cocaina-levamisol.html?v=20260909-nejm"),
    caso(slug="west_nile", titulo="O peso dos dias",
         subtitulo="Um homem de 71 anos com febre passa a precisar de ajuda para caminhar.",
         especialidade="Clínica médica · Emergência", minutos=55, decisoes=13,
         desfechos=3, nivel="os dois", cor="azul",
         capa="../../west_nile/img/cena.png", arquivo="west-nile.html?v=20260909-nejm"),
    caso(slug="kikuchi",
         titulo="Mulher de 27 anos com febre prolongada e linfonodomegalia cervical",
         subtitulo="Três semanas de febre, linfonodo doloroso e um hemograma "
                   "que não fecha com infecção bacteriana.",
         especialidade="Clínica médica · Hematologia", minutos=30, decisoes=6,
         desfechos=2, nivel="interno", cor="laranja", pronto=False),
    caso(slug="sarcoidose",
         titulo="Homem de 41 anos com dispneia, eritema nodoso e hipercalcemia",
         subtitulo="Linfonodomegalia hilar bilateral e um cálcio que sobe sem "
                   "paratormônio para explicá-lo.",
         especialidade="Pneumologia · Reumatologia", minutos=35, decisoes=6,
         desfechos=2, nivel="os dois", cor="verde", pronto=False),
    caso(slug="cmv",
         titulo="Mulher de 58 anos transplantada com febre e citopenias",
         subtitulo="Quarto mês de transplante renal, febre sem foco, e a "
                   "profilaxia terminou há três semanas.",
         especialidade="Infectologia · Nefrologia", minutos=40, decisoes=7,
         desfechos=3, nivel="residente", cor="ocre", pronto=False),
]

RODAPE = (
    "<b>Procedência.</b> Os pacientes são ficcionais e cada caso é autoral, "
    "escrito para ensino: os desfechos dos ramos são inferência fisiológica, "
    "não extração de artigo. As cenas dos pacientes são ilustrações geradas "
    "por inteligência artificial a partir da descrição clínica. As imagens de "
    "radiologia, ultrassom, microscopia e anatomia patológica são reais, "
    "ilustrativas, de repositórios de licença aberta, e não pertencem aos "
    "pacientes dos casos — crédito e licença ao pé de cada figura. "
    "Cada caso abre e roda no próprio navegador, sem servidor e sem internet."
)


def construir() -> Path:
    destino = RAIZ / "saida" / "biblioteca.html"
    destino.parent.mkdir(parents=True, exist_ok=True)
    destino.write_text(montar(
        titulo="Casos para conduzir, não para ler",
        subtitulo="Cada caso avança em alíquotas: um dado novo do paciente, e "
                  "a pergunta que ele abre — o diferencial de um sintoma, a "
                  "leitura de um resultado, o mecanismo de um achado. Você "
                  "escolhe os exames, e suas decisões mudam o rumo e o desfecho.",
        casos=CASOS, rodape=RODAPE,
        img_dir=RAIZ / "casos" / "pulmao_rim" / "img",
    ), encoding="utf-8")
    kb = destino.stat().st_size / 1024
    prontos = sum(c["pronto"] for c in CASOS)
    print(f"{destino.relative_to(RAIZ)}  ·  {len(CASOS)} casos "
          f"({prontos} pronto{'s' if prontos > 1 else ''})  ·  {kb:,.0f} KB")
    return destino


if __name__ == "__main__":
    construir()

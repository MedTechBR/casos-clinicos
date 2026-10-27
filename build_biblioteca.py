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
         subtitulo="Homem de 63 anos com oito semanas de sintomas nasais que "
                   "não melhoraram e uma piora nos três dias antes da "
                   "internação.",
         # "Nefrologia · Pneumologia" no cartão entrega a síndrome antes de o
         # aluno abrir o caso, do mesmo jeito que o título entregava.
         especialidade="Clínica médica · Emergência",
         minutos=50, decisoes=6, desfechos=4, nivel="os dois", cor="vermelho",
         capa="cena_admissao.jpg", arquivo="o-sangue-que-nao-saiu.html?v=20261027-discussao"),

    caso(slug="cocaina_levamisol", titulo="À flor da pele",
         subtitulo="Uma vendedora de 34 anos chega ao pronto-socorro com manchas dolorosas nas coxas e febre.",
         especialidade="Clínica médica · Emergência", minutos=45, decisoes=6,
         desfechos=4, nivel="os dois", cor="roxo",
         capa="../../cocaina_levamisol/img/cena.png", arquivo="a-flor-da-pele.html?v=20261027-discussao"),
    caso(slug="west_nile", titulo="O peso dos dias",
         subtitulo="Um homem de 71 anos com febre passa a precisar de ajuda para caminhar.",
         especialidade="Clínica médica · Emergência", minutos=45, decisoes=6,
         desfechos=3, nivel="os dois", cor="azul",
         capa="../../west_nile/img/cena.png", arquivo="o-peso-dos-dias.html?v=20261027-discussao"),
    caso(slug="kikuchi", titulo="O que ficou no pescoço",
         subtitulo="Uma professora de 27 anos chega no 12º dia de febre, com um caroço doloroso no pescoço que o antibiótico não mudou.",
         especialidade="Clínica médica", minutos=45, decisoes=9,
         desfechos=2, nivel="residente", cor="laranja", capa="../../kikuchi/img/cena.png", arquivo="o-que-ficou-no-pescoco.html?v=20261027-discussao"),
    caso(slug="sarcoidose", titulo="Entre a sede e o fôlego",
         subtitulo="Um analista administrativo chega ao pronto-socorro nauseado, confuso e com o intestino preso há cinco dias.",
         especialidade="Clínica médica", minutos=50, decisoes=6,
         desfechos=3, nivel="os dois", cor="verde", capa="../../sarcoidose/img/cena.png", arquivo="entre-a-sede-e-o-folego.html?v=20261027-discussao"),
    caso(slug="leptospirose", titulo="O sexto dia",
         subtitulo="Um homem de 38 anos chega à emergência no sexto dia de febre, com tosse com sangue e falta de ar.",
         especialidade="Clínica médica · Emergência", minutos=45, decisoes=6,
         desfechos=3, nivel="os dois", cor="azul", capa="../../leptospirose/img/cena.png", arquivo="o-sexto-dia.html?v=20261027-investigacao"),
    caso(slug="endocardite", titulo="Pequenos sinais",
         subtitulo="Uma costureira de 59 anos perdeu 5 kg em cinco semanas de febre no fim da tarde.",
         especialidade="Clínica médica · Ambulatório", minutos=45, decisoes=6,
         desfechos=3, nivel="os dois", cor="vermelho", capa="../../endocardite/img/cena.png", arquivo="pequenos-sinais.html?v=20261027-discussao"),
    caso(slug="adrenal", titulo="Oito meses de cansaço",
         subtitulo="Uma professora de 44 anos chega em choque no terceiro dia de uma diarreia que o filho superou em um dia.",
         especialidade="Clínica médica · Emergência", minutos=40, decisoes=6,
         desfechos=3, nivel="os dois", cor="ocre", capa="../../adrenal/img/cena.png", arquivo="oito-meses-de-cansaco.html?v=20261027-discussao"),
    caso(slug="cmv", titulo="Depois da travessia",
         subtitulo="Depois de retomar a rotina, uma mulher precisa voltar ao hospital por febre e diarreia.",
         especialidade="Clínica médica", minutos=50, decisoes=6,
         desfechos=3, nivel="residente", cor="ocre", capa="../../cmv/img/cena.png", arquivo="depois-da-travessia.html?v=20261027-discussao"),
    caso(slug="encefalite_nmda", titulo="Dez noites",
         subtitulo="Uma estudante de 24 anos chega com dez dias sem dormir, ideias de perseguição e uma fala que a família não reconhece.",
         especialidade="Neurologia · Psiquiatria", minutos=35, decisoes=6,
         desfechos=3, nivel="os dois", cor="roxo", capa="../../encefalite_nmda/img/cena-paciente.png", arquivo="dez-noites.html?v=20261027-discussao"),
    caso(slug="ptt", titulo="Do outro lado do plantão",
         subtitulo="Uma técnica de enfermagem chega à emergência com febre, dor de cabeça e uma confusão que vai e volta.",
         especialidade="Clínica médica · Hematologia", minutos=35, decisoes=6,
         desfechos=4, nivel="os dois", cor="vermelho", capa="../../ptt/img/cena-paciente.png", arquivo="do-outro-lado-do-plantao.html?v=20261027-discussao"),
    caso(slug="paracoco", titulo="A ferida do lábio",
         subtitulo="Um lavrador de Rondônia com tosse há quatro meses, voz rouca e uma ferida no lábio que não fecha.",
         especialidade="Clínica médica · Infectologia", minutos=35, decisoes=6,
         desfechos=3, nivel="os dois", cor="verde", capa="../../paracoco/img/cena-paciente.png", arquivo="a-ferida-do-labio.html?v=20261027-discussao"),
    caso(slug="feocromocitoma", titulo="Pressão de nervoso",
         subtitulo="Uma contadora de 41 anos, tratada há seis meses por crises de pânico, chega à emergência com dor no peito e a pressão em 228/124.",
         especialidade="Clínica médica · Endocrinologia", minutos=40, decisoes=6,
         desfechos=4, nivel="os dois", cor="laranja", capa="../../feocromocitoma/img/cena-paciente.png", arquivo="pressao-de-nervoso.html?v=20261027-discussao"),
    caso(slug="lupus_abdominal", titulo="Entre uma refeição e outra",
         subtitulo="Marina deixa de tolerar as refeições depois de semanas de cólicas e distensão abdominal.",
         especialidade="Clínica médica · Emergência", minutos=55, decisoes=7,
         desfechos=2, nivel="residente", cor="verde", capa="../../lupus_abdominal/img/cena.png", arquivo="entre-uma-refeicao-e-outra.html?v=20261027-novos"),
    caso(slug="tb_peritoneal", titulo="O espaço entre os dias",
         subtitulo="Elisa perde peso enquanto o abdome aumenta e passa a precisar de roupas mais largas.",
         especialidade="Clínica médica", minutos=55, decisoes=7,
         desfechos=2, nivel="residente", cor="ocre", capa="../../tb_peritoneal/img/cena.png", arquivo="o-espaco-entre-os-dias.html?v=20261027-novos"),
    caso(slug="b12_microangiopatia", titulo="Os passos de volta",
         subtitulo="Antônio precisa parar para descansar ao atravessar o estacionamento do hospital.",
         especialidade="Clínica médica · Emergência", minutos=50, decisoes=6,
         desfechos=2, nivel="residente", cor="roxo", capa="../../b12_microangiopatia/img/cena.png", arquivo="os-passos-de-volta.html?v=20261027-novos"),

]

RODAPE = (
    "<b>Procedência.</b> Os pacientes são ficcionais e cada caso é autoral, "
    "escrito para ensino: os desfechos dos ramos são inferência fisiológica, "
    "não extração de artigo. As capas são ilustrações geradas por inteligência "
    "artificial a partir da descrição clínica ou fotografias de licença aberta. As imagens de "
    "radiologia, ultrassom, microscopia e anatomia patológica são reais, "
    "ilustrativas, de repositórios de licença aberta e do acervo didático fornecido, e não pertencem aos "
    "pacientes dos casos — crédito e licença ao pé de cada figura. "
    "Cada caso abre e roda no próprio navegador, sem servidor e sem internet."
)


def construir() -> Path:
    destino = RAIZ / "saida" / "biblioteca.html"
    destino.parent.mkdir(parents=True, exist_ok=True)
    destino.write_text(montar(
        titulo="Casos para conduzir, não para ler",
        subtitulo="Doenças raras e apresentações incomuns abordadas a partir "
                  "das síndromes: hipóteses, investigação dirigida e evolução clínica.",
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

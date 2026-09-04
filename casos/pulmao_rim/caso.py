"""Caso pulmão-rim — os slides, em prosa.

Homem de 63 anos com hemoptise, púrpura e queda de função renal.
Paciente ficcional, construído para ensino.

Regra editorial: história e exame físico em parágrafos corridos, como no NEJM.
Nunca em tópicos. Marcos temporais dentro da frase. Sinais vitais narrados.
Títulos são substantivos simples, sem efeito.
"""

from pathlib import Path

from motor.conteudo import (
    box, cap, circulo, cols, exame, figura, figura_anotada, h3, lista, nota, p,
    painel, passo, revelar, rotulo, seta, sinais, tabela,
)
from motor.desenhos import (
    capilar_compartilhado, crescente_glomerular, hip, linha_do_tempo,
    mapa_do_corpo, marco, padroes_imunofluorescencia, quadro,
)
from motor.slides import bloco, capa, discussao, momento, narrativa, tela

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
    hip("droga", "Vasculite induzida por droga",
        "Hidralazina, propiltiouracila, minociclina ou levamisol em uso"),
]

from .banco import BANCO
from .perguntas import P1, P2, P3, P4, P5, P6, P7, P8, P9

TITULO = "Homem de 63 anos com hemoptise, púrpura e queda de função renal"
SLUG = "pulmao-rim"
RODAPE = "Síndrome pulmão-rim · caso interativo"
IMG = Path(__file__).parent / "img"

SLIDES = [
    capa(
        "Homem de 63 anos com hemoptise, púrpura e queda de função renal",
        "Sintomas nasais, articulares, pulmonares e renais ao longo de oito "
        "semanas.",
        "**13 blocos de caso · 9 perguntas · 90 a 110 minutos** O caso avança "
        "em blocos de informação nova. As perguntas são curtas e servem para "
        "abrir discussão, não para testar memória.",
        "Caso autoral, construído para ensino. O paciente é ficcional. As "
        "imagens são ilustrativas, de repositórios de licença aberta, e não "
        "pertencem a este paciente. Créditos no slide final.",
    ),
    narrativa("O caso · bloco 1", "Apresentação",
        p("Um homem de 63 anos, ex-tabagista, aposentado, foi admitido neste "
          "hospital por dispneia e hemoptise."),
        passo(p("O paciente estava em seu estado habitual de saúde, com "
                "hipertensão em uso de losartana, até oito semanas antes da "
                "apresentação atual, quando surgiu rinorreia purulenta "
                "persistente, acompanhada de crostas nasais e epistaxe quase "
                "diária. Foi tratado como rinossinusite bacteriana em duas "
                "ocasiões, com amoxicilina e depois com "
                "amoxicilina-clavulanato, sem melhora. Nesse período perdeu o "
                "olfato.")),
        passo(p("Cinco semanas antes da apresentação, desenvolveu dores "
                "articulares migratórias, que acometiam punhos numa semana e "
                "tornozelos na seguinte, sem edema ou calor local. Passou a "
                "apresentar febre vespertina de até 37,9 °C, sudorese noturna "
                "e perda de 6 kg sem alteração da dieta. A esposa notou que "
                "ele passou a se cansar ao subir a rampa da garagem, o que "
                "antes não ocorria.")),
        passo(p("Duas semanas antes da apresentação, iniciou tosse seca, que "
                "em poucos dias passou a apresentar raias de sangue no "
                "escarro. Procurou o serviço de emergência, onde uma "
                "radiografia de tórax foi interpretada como normal, e recebeu "
                "alta com antitussígeno.")),
        passo(p("Nos três dias que antecederam a internação, a dispneia "
                "progrediu até surgir em repouso, e ele expectorou cerca de "
                "50 mL de sangue vivo em duas ocasiões. A filha, que o trouxe "
                "ao hospital, relatou que o pai vinha arrastando o pé direito "
                "havia aproximadamente dez dias, queixa que ele próprio não "
                "havia mencionado.")),
        passo(p("Não havia história de viagem recente, contato com "
                "tuberculose, uso de drogas ilícitas ou exposição "
                "ocupacional. As únicas medicações em uso eram losartana e "
                "sinvastatina. Não usava hidralazina, propiltiouracila ou "
                "minociclina.")),
        densidade="dense",
    ),
    bloco("O caso · bloco 1", "Curso de oito semanas",
        linha_do_tempo([
            marco("8 semanas antes",
                  "Rinorreia purulenta, crostas nasais, epistaxe quase diária. "
                  "Perda do olfato. Dois cursos de antibiótico, sem melhora."),
            marco("5 semanas antes",
                  "Artralgia migratória, febre vespertina, sudorese noturna, "
                  "perda de 6 kg. Cansaço aos esforços habituais."),
            marco("2 semanas antes",
                  "Tosse seca que passa a ter raias de sangue. Radiografia de "
                  "tórax lida como normal; alta com antitussígeno."),
            marco("10 dias antes",
                  "Passa a arrastar o pé direito — queixa que ele não menciona."),
            marco("3 dias antes",
                  "Dispneia em repouso. Cerca de 50 mL de sangue vivo em duas "
                  "ocasiões.", agora=True),
        ]),
        nota("Antes de avançar",
            p("Peça à turma que descreva o curso antes de você comentar: onde "
              "a doença começou, para onde foi, e o que oito semanas excluem "
              "nas duas pontas. A inferência é o exercício — entregá-la "
              "impressa ao lado dos dados é o que transforma raciocínio em "
              "leitura.")),
        centro=True,
    ),
    narrativa("O caso · bloco 2", "Exame físico",
        p("Ao exame, a temperatura era de 37,8 °C, a pressão arterial de "
          "148/92 mmHg, a frequência cardíaca de 104 batimentos por minuto e "
          "a frequência respiratória de 28 incursões por minuto. A saturação "
          "de oxigênio era de 88% enquanto o paciente respirava ar ambiente, "
          "e subiu para 94% com cateter nasal a 4 L por minuto."),
        passo(p("O paciente estava dispneico, preferia permanecer sentado e "
                "completava apenas frases curtas. Havia palidez "
                "cutâneo-mucosa acentuada. À ausculta pulmonar, crepitações "
                "finas difusas nos dois hemitórax, sem sibilos e sem atrito "
                "pleural. A ausculta cardíaca era normal, sem sopros. Não "
                "havia estase jugular, terceira bulha ou edema de membros "
                "inferiores.")),
        passo(p("Na face anterior das pernas e no dorso dos pés havia lesões "
                "purpúricas palpáveis, algumas com centro escurecido, que não "
                "desapareciam à digitopressão. Não havia livedo reticular, "
                "nódulo subcutâneo ou úlcera cutânea.")),
        passo(p("Na inspeção nasal, observaram-se crostas hemáticas aderidas "
                "ao septo em ambas as narinas, com mucosa friável ao toque. "
                "Não havia perfuração septal, deformidade em sela ou massa. "
                "Os seios da face eram indolores à percussão.")),
        passo(p("Ao exame neurológico, havia pé caído à direita, com força de "
                "2/5 para dorsiflexão e eversão, e hipoestesia no dorso do "
                "pé, no território do nervo fibular. À esquerda, havia "
                "fraqueza para a abdução do quinto dedo da mão e hipoestesia "
                "no território ulnar. Os déficits eram assimétricos e não "
                "obedeciam a um nível medular nem a uma raiz única. A força e "
                "os reflexos estavam preservados nos demais segmentos.")),
        nota("Antes de avançar",
            p("Antes de mostrar a pergunta, peça à turma que nomeie os "
              "territórios acometidos. São quatro: via aérea superior, "
              "pulmão, pele e nervo periférico. O rim ainda não apareceu.")),
        densidade="dense",
    ),
    bloco("O caso · síntese do exame", "Territórios acometidos",
        mapa_do_corpo([
            ("via_aerea",
             "Crostas hemáticas aderidas ao septo, mucosa friável, anosmia. "
             "Sem perfuração septal e sem deformidade em sela."),
            ("pulmao",
             "Crepitações finas difusas nos dois hemitórax, saturação de 88% "
             "em ar ambiente, hemoptise."),
            ("pele",
             "Púrpura palpável na face anterior das pernas e no dorso dos pés, "
             "algumas lesões com centro escurecido."),
            ("nervo",
             "Pé caído à direita e déficit ulnar à esquerda. Assimétrico, sem "
             "nível medular e sem raiz única."),
        ], altura=344),
        nota("Antes de avançar",
            p("Revele um território por vez e peça à turma que nomeie o "
              "seguinte antes de mostrar. São quatro. O rim ainda não "
              "apareceu — e é justamente o que a próxima pergunta persegue.")),
        densidade="dense",
    ),
    P1,
    discussao("A parede compartilhada",
        cols(
            [capilar_compartilhado(altura=252)],
            [
                p("O capilar glomerular e o capilar alveolar têm a mesma "
                  "arquitetura: endotélio finíssimo apoiado em membrana basal, "
                  "submetido a pressão, e responsável por filtrar de um lado e "
                  "trocar gás do outro."),
                p("Uma agressão dirigida a esse compartimento aparece nos dois "
                  "órgãos ao mesmo tempo — e também na pele e no vasa nervorum, "
                  "que são feitos do mesmo material. É por isso que os quatro "
                  "territórios do exame físico e o rim caem juntos."),
                nota("Antes de avançar",
                    p("Pergunte por que o fígado e o baço não entram nessa "
                      "lista. A resposta é a arquitetura do leito: sinusoide "
                      "fenestrado não se comporta como capilar de barreira.")),
            ],
        ),
        densidade="dense",
        centro=True,
        ident="parede_compartilhada",
    ),
    momento("Segunda parte",
        "Diagnóstico diferencial",
        "A partir daqui o caso para de contar e começa a testar. A lista que o "
        "grupo levantar agora é a que vai sendo podada, um resultado por vez.",
        ident="p2_diferencial"),
    discussao("O que pode fazer as duas coisas",
        p("Hemorragia alveolar com glomerulonefrite é uma lista curta, e a "
          "turma consegue levantá-la em voz alta antes de qualquer resultado. "
          "A coluna da direita não diz o que este paciente tem: diz o que "
          "**teria de ser verdade** para cada candidato ser o diagnóstico. É "
          "essa coluna que a investigação vai testar, uma linha por vez."),
        quadro(HIPOTESES, titulo="Levantado pelo grupo, ao fim do exame físico"),
        nota("Como conduzir",
            p("Não mostre o quadro pronto. Peça as hipóteses à turma primeiro e "
              "escreva no quadro branco; só então revele esta tela, e compare. "
              "O que a turma esqueceu costuma ser mais instrutivo do que o que "
              "ela lembrou — em geral esquecem a endocardite e a droga.")),
        densidade="dense",
        ident="quadro_1",
    ),
    P2,
    tela("O caso · bloco 3", "Exames da admissão",
        cols(
            [
                cap("Hemograma"),
                painel([
                    exame("Hemoglobina", "7,8 g/dL {{(13,9 há dois meses)}}",
                           "13,5 a 17,5", "critico"),
                    exame("Reticulócitos", "2,1%",
                           "0,5 a 2,0", "alterado"),
                    exame("Leucócitos", "14.200/mm³",
                           "4.000 a 11.000", "alterado"),
                    exame("Neutrófilos", "11.800/mm³",
                           "1.800 a 7.000", "alterado"),
                    exame("Eosinófilos", "320/mm³",
                           "50 a 500"),
                    exame("Plaquetas", "468.000/mm³",
                           "150.000 a 450.000", "alterado"),
                    exame("Esfregaço", "Sem esquizócitos",
                           "—"),
                ]),
                cap("Inflamação"),
                painel([
                    exame("PCR", "186 mg/L",
                           "até 5", "critico"),
                    exame("VHS", "98 mm/h",
                           "até 20", "alterado"),
                    exame("Procalcitonina", "0,4 ng/mL",
                           "abaixo de 0,5"),
                ]),
            ],
            [
                cap("Função renal e gasometria"),
                painel([
                    exame("Creatinina", "3,8 mg/dL {{(1,0 há dois meses)}}",
                           "até 1,3", "critico"),
                    exame("Ureia", "128 mg/dL",
                           "até 45", "alterado"),
                    exame("Filtração glomerular estimada", "16 mL/min/1,73 m²",
                           "acima de 90", "critico"),
                    exame("Potássio", "5,4 mEq/L",
                           "3,5 a 5,0", "alterado"),
                    exame("Bicarbonato", "17 mEq/L",
                           "22 a 26", "alterado"),
                    exame("pH / pO2", "7,30 / 56 mmHg",
                           "7,35 a 7,45 / 80 a 100", "alterado"),
                    exame("PaO2/FiO2", "186",
                           "acima de 300", "critico"),
                    exame("Albumina", "2,9 g/dL",
                           "3,5 a 5,2", "alterado"),
                ]),
            ],
        ),
    ),
    tela("O caso · bloco 4", "Sedimento urinário",
        cols(
            [
                cap("Urina de jato médio, fresca, examinada ao microscópio"),
                painel([
                    exame("Proteína na fita", "3+",
                           "negativa", "alterado"),
                    exame("Sangue na fita", "4+",
                           "negativo", "critico"),
                    exame("Hemácias dismórficas", "40% das hemácias",
                           "ausentes", "critico"),
                    exame("Cilindros hemáticos", "Presentes",
                           "ausentes", "critico"),
                    exame("Cilindros granulosos", "Presentes",
                           "ausentes", "alterado"),
                    exame("Leucócitos", "8 por campo",
                           "até 5", "alterado"),
                    exame("Bacteriúria", "Ausente",
                           "ausente"),
                    exame("Proteinúria de 24 horas", "2,4 g",
                           "abaixo de 0,15", "alterado"),
                ]),
            ],
            [
                box("Complemento e autoanticorpos, colhidos na mesma punção",
                    p("C3 de 112 mg/dL e C4 de 28 mg/dL, ambos dentro da "
                      "faixa de referência. FAN não reagente. Anti-DNA nativo "
                      "não reagente. Crioglobulinas negativas, com coleta em "
                      "tubo aquecido a 37 °C e transporte aquecido.")),
                nota("Antes de avançar",
                    p("Este é o slide mais importante do caso e o exame mais "
                      "barato dele. Vale perguntar quantas vezes na semana "
                      "alguém do grupo olha um sedimento no microscópio, em "
                      "vez de ler o laudo automatizado.")),
            ],
        ),
        densidade="dense",
    ),
    P3,
    discussao("Sedimento urinário",
        p("A hematúria pode vir de qualquer ponto entre o glomérulo e o meato "
          "uretral. O cilindro hemático restringe a topografia ao glomérulo, "
          "porque ele se forma dentro do túbulo, a partir de hemácias que "
          "atravessaram a parede capilar glomerular e ficaram presas na "
          "matriz proteica."),
        cols(
            [
                tabela(["Achado", "Significado"], [
                    ["Hemácia dismórfica", "Atravessou uma parede glomerular lesada e se "
                            "deformou no trajeto"],
                    ["Cilindro hemático", "Glomerulonefrite"],
                    ["Hemácia isomórfica, sem cilindro", "Sangramento de via urinária: cálculo, tumor, "
                            "infecção"],
                    ["Proteinúria acima de 3,5 g em 24 horas", "Lesão podocitária, com padrão nefrótico"],
                    ["Cilindro leucocitário", "Nefrite intersticial ou pielonefrite"],
                    ["Cilindro granuloso pigmentar", "Necrose tubular aguda"],
                ], tamanho="sm"),
            ],
            [
                box("Por que este exame se perde na prática",
                    p("A fita reagente detecta hemoglobina, mas não vê "
                      "cilindro nem dismorfismo. O sedimento exige urina "
                      "fresca, centrifugação e leitura ao microscópio. Um "
                      "laudo automatizado que informa apenas “hemácias: "
                      "numerosas” não respondeu à pergunta que foi feita.")),
                box("A síndrome, nomeada",
                    p("Hematúria dismórfica com cilindros hemáticos, "
                      "proteinúria em faixa não nefrótica, hipertensão e "
                      "queda rápida da filtração glomerular constituem "
                      "síndrome nefrítica com glomerulonefrite rapidamente "
                      "progressiva.")),
            ],
        ),
        densidade="dense",
    ),
    discussao("A primeira linha cai",
        p("O sedimento não nomeou nenhuma doença. Ele fez outra coisa, que vem "
          "antes: eliminou a possibilidade de que houvesse duas doenças "
          "independentes, uma no pulmão e outra na bexiga. A partir daqui o "
          "caso tem um mecanismo só, e é glomerular."),
        quadro(HIPOTESES, {
            "urologico": ("derrubada",
                          "Hemácias dismórficas em 40% e cilindros hemáticos: "
                          "o sangue atravessou o glomérulo"),
        }, titulo="Depois do sedimento urinário"),
        densidade="xd",
        ident="quadro_2",
    ),
    P4,
    discussao("O complemento poda a lista",
        p("Complemento normal não é resultado sem graça: é uma das bifurcações "
          "mais baratas da investigação da glomerulonefrite. Ele separa as "
          "causas que consomem complemento das que não consomem, e derruba "
          "três linhas de uma vez."),
        quadro(HIPOTESES, {
            "urologico": ("derrubada", "Sedimento glomerular"),
            "lupus": ("derrubada",
                      "C3 e C4 normais, FAN e anti-DNA não reagentes"),
            "crio": ("derrubada",
                     "C4 de 28 mg/dL: a crioglobulinemia consome C4 de forma "
                     "desproporcional"),
            "endocardite": ("enfraquecida",
                            "Complemento normal ou baixo; hemoculturas em "
                            "andamento, sem sopro novo"),
        }, titulo="Depois do complemento e do painel de autoanticorpos",
           novos=["lupus", "crio", "endocardite"]),
        nota("Antes de avançar",
            p("Pergunte quem sobrou e por quê. Três candidatos em pé, e nenhum "
              "deles foi testado ainda — as sorologias específicas ainda não "
              "voltaram. É este o momento de decidir se a imunossupressão "
              "espera o resultado.")),
        densidade="xd",
        ident="quadro_3",
    ),
    bloco("O caso · bloco 5", "Tomografia de tórax",
        cols(
            [
                figura_anotada("tc_torax_vidro_fosco.jpg",
                    "Cortes axiais, coronal e sagital. Imagem ilustrativa.",
                    "Hellerhoff · Wikimedia Commons · CC BY-SA 4.0",
                    [
                        rotulo(19, 4, "axial"),
                        rotulo(67, 4, "coronal"),
                        rotulo(70, 54, "sagital"),
                        circulo(12, 13, 4),
                        circulo(57, 22, 6, "atenuação em vidro fosco"),
                    ],
                    altura=318,
                    legenda_anotada="Os círculos marcam áreas representativas "
                                    "do padrão, difuso e bilateral nos três "
                                    "planos. Não há nódulo escavado, massa, "
                                    "derrame nem cardiomegalia."),
                revelar("Laudo do radiologista",
                    p("“Opacidades em vidro fosco difusas e bilaterais, "
                      "confluentes em alguns lobos. Ausência de nódulo "
                      "escavado, massa, linfonodomegalia mediastinal e "
                      "derrame pleural. Sem sinais de fibrose estabelecida.”")),
            ],
            [
                box("O que o padrão permite dizer",
                    p("Vidro fosco difuso e bilateral é compatível com "
                      "hemorragia alveolar, edema, infecção difusa e "
                      "pneumonite. A ausência de nódulo escavado torna menos "
                      "provável a apresentação clássica da granulomatose com "
                      "poliangiite. A ausência de derrame e de cardiomegalia "
                      "argumenta contra congestão.")),
                box("O que ainda falta",
                    p("Vidro fosco não estabelece o diagnóstico de hemorragia "
                      "alveolar. A comprovação é feita na broncoscopia, que "
                      "também fornece o material para afastar infecção antes "
                      "de imunossuprimir.")),
            ],
        ),
        densidade="dense",
    ),
    tela("O caso · bloco 6", "Broncoscopia com lavado broncoalveolar",
        cols(
            [
                box("Descrição do procedimento",
                    p("Lavado do lobo médio em três alíquotas de 60 mL. Não "
                      "havia lesão endobrônquica, sangramento de sítio único "
                      "ou coágulo obstruindo brônquio. O aspecto das alíquotas "
                      "e a contagem diferencial saem a seguir.")),
                cap("Lavado broncoalveolar"),
                painel([
                    exame("Cultura para bactérias", "Negativa",
                           "negativa"),
                    exame("Cultura para fungos", "Negativa",
                           "negativa"),
                    exame("Pesquisa de //Pneumocystis//", "Não detectado",
                           "não detectado"),
                    exame("BAAR e teste molecular para tuberculose", "Negativos",
                           "negativos"),
                    exame("Galactomanana no lavado", "Não reagente",
                           "não reagente"),
                ]),
            ],
            [
                nota("Antes de avançar",
                    p("As culturas já estão na tela; o aspecto das alíquotas e "
                      "a contagem diferencial, não. Faça a pergunta antes de "
                      "mostrá-los: o grupo tem de dizer o que PROCURA no "
                      "lavado, e não reconhecer o que já leu.")),
                box("A função das culturas",
                    p("As culturas negativas são o que autoriza a "
                      "imunossupressão. Tratar infecção difusa como "
                      "vasculite, com pulso de corticoide e ciclofosfamida, "
                      "tem consequência previsível.")),
            ],
        ),
        densidade="xd",
    ),
    P5,
    tela("O caso · bloco 6", "O que o lavado mostrou",
        cols(
            [
                cap("Aspecto e contagem"),
                painel([
                    exame("Aspecto das alíquotas",
                          "Progressivamente hemorrágicas, da primeira à terceira",
                          "claras", "critico"),
                    exame("Hemossiderófagos", "34% dos macrófagos",
                          "abaixo de 20%", "critico"),
                    exame("Neutrófilos", "18% da celularidade",
                          "abaixo de 3%", "alterado"),
                    exame("Linfócitos", "12% da celularidade",
                          "10 a 15%"),
                ]),
            ],
            [
                box("Por que os dois juntos",
                    p("Alíquotas sequencialmente mais hemorrágicas dizem que o "
                      "sangue vem do alvéolo, e não de um ponto do brônquio: "
                      "sangramento localizado clareia com a lavagem, "
                      "sangramento difuso não."),
                    p("Hemossiderófagos acima de 20% dizem outra coisa, e é a "
                      "que muda a conversa: o sangramento tem pelo menos 48 a "
                      "72 horas, tempo de o macrófago digerir a hemoglobina e "
                      "acumular hemossiderina. Não é o episódio de ontem — "
                      "vem acontecendo.")),
                box("O que ainda não sabemos",
                    p("Hemorragia alveolar está provada, e infecção está "
                      "afastada como causa. Nada disso diz qual das linhas do "
                      "quadro é a responsável.")),
            ],
        ),
        densidade="dense",
        ident="lavado_achado",
    ),
    discussao("O que sobra antes do resultado",
        p("O lavado provou hemorragia alveolar e não cresceu nada. As três "
          "linhas que sobram não podem ser separadas por mais nenhum exame "
          "barato: daqui em diante, quem decide é a sorologia e a biópsia."),
        quadro(HIPOTESES, {
            "urologico": ("derrubada", "Sedimento glomerular"),
            "lupus": ("derrubada", "Complemento normal, FAN não reagente"),
            "crio": ("derrubada", "C4 normal"),
            "endocardite": ("enfraquecida",
                            "Três pares de hemocultura negativos em cinco dias, "
                            "ecocardiograma sem vegetação"),
            "infeccao": ("enfraquecida",
                         "Lavado sem bactéria, fungo, micobactéria ou "
                         "Pneumocystis"),
        }, titulo="Depois do lavado broncoalveolar",
           novos=["endocardite", "infeccao"]),
        nota("Antes de avançar",
            p("Este é o momento de fazer a pergunta que o caso não fez até "
              "aqui: começar a imunossupressão hoje, ou esperar o laudo? "
              "Deixe a turma se dividir antes de virar a tela.")),
        densidade="xd",
        ident="quadro_4",
    ),
    momento("Terceira parte",
        "O resultado que estava pendente",
        "As sorologias foram pedidas na primeira hora. Voltaram agora.",
        ident="p3_resultado"),
    tela("O caso · bloco 7", "Painel imunológico",
        cols(
            [
                cap("Autoanticorpos"),
                painel([
                    exame("ANCA {{(imunofluorescência indireta)}}", "Padrão perinuclear, título 1:640",
                           "não reagente", "critico"),
                    exame("Anti-mieloperoxidase", "148 U/mL",
                           "até 20", "critico"),
                    exame("Anti-proteinase 3", "3 U/mL, não reagente",
                           "até 20"),
                    exame("Anti-membrana basal glomerular", "Não reagente",
                           "não reagente"),
                    exame("C3 / C4", "112 / 28 mg/dL",
                           "90 a 180 / 10 a 40"),
                    exame("FAN / anti-DNA", "Não reagentes",
                           "não reagentes"),
                    exame("Crioglobulinas", "Negativas {{(tubo aquecido)}}",
                           "negativas"),
                    exame("Antifosfolípides", "Não reagentes",
                           "não reagentes"),
                    exame("Anti-HIV, HBsAg, anti-HCV", "Não reagentes",
                           "não reagentes"),
                ]),
            ],
            [
                figura_anotada("panca_imunofluorescencia.jpg",
                    "Padrão p-ANCA. Imagem ilustrativa.",
                    "Simon Caulton · Wikimedia Commons · CC BY-SA 3.0",
                    [
                        circulo(29.5, 30, 4),
                        seta(40, 44, 32, 33, "fluorescência acompanhando os lóbulos do núcleo"),
                    ],
                    altura=240,
                    legenda_anotada="Cada aglomerado é um neutrófilo fixado em etanol. A fluorescência se concentra junto aos lóbulos nucleares, e não difusa pelo citoplasma."),
                revelar("O que a lâmina mostra",
                    p("Imunofluorescência indireta sobre neutrófilos fixados "
                      "em etanol, com conjugado marcado por fluoresceína. A "
                      "fluorescência se concentra ao redor do núcleo, "
                      "configurando o padrão perinuclear, distinto do padrão "
                      "citoplasmático granular difuso do c-ANCA.")),
                box("Tomografia de seios da face, do mesmo dia",
                    p("Espessamento mucoso discreto em seios maxilares. Sem "
                      "erosão óssea, massa ou destruição do septo nasal.")),
            ],
        ),
        densidade="xd",
    ),
    discussao("Sobra uma",
        p("O p-ANCA em 1:640 com anti-MPO de 148 U/mL, o anti-MBG não reagente "
          "e a lista de medicações limpa fecham a poda começada no exame "
          "físico. O nome só aparece agora, e aparece como resultado do "
          "percurso — não como ponto de partida."),
        quadro(HIPOTESES, {
            "urologico": ("derrubada", "Sedimento glomerular"),
            "lupus": ("derrubada", "Complemento normal, FAN não reagente"),
            "crio": ("derrubada", "C4 normal, crioglobulinas negativas"),
            "endocardite": ("derrubada",
                            "Hemoculturas negativas, ecocardiograma sem "
                            "vegetação"),
            "infeccao": ("derrubada", "Lavado estéril"),
            "mbg": ("derrubada", "Anti-MBG não reagente"),
            "droga": ("derrubada",
                      "Em uso apenas de losartana e sinvastatina; nenhuma das "
                      "quatro drogas implicadas"),
            "anca": ("confirmada",
                     "p-ANCA 1:640, anti-MPO 148 U/mL — falta a biópsia dizer "
                     "se é pauci-imune"),
        }, titulo="Depois do painel imunológico",
           novos=["mbg", "droga", "anca"]),
        densidade="xd",
        ident="quadro_5",
    ),
    bloco("O caso · bloco 8", "Biópsia renal percutânea",
        cols(
            [
                figura_anotada("biopsia_renal_crescente.jpg",
                    "Córtex renal, grande aumento. Imagem ilustrativa.",
                    "Nephron · Wikimedia Commons · CC BY-SA 3.0",
                    [
                        circulo(30, 45, 12, "glomérulo"),
                        seta(90, 52, 79, 60, "túbulos e interstício"),
                    ],
                    altura=266,
                    legenda_anotada="Glomérulos e compartimento "
                                    "tubulointersticial. A crescente deste "
                                    "paciente está no esquema abaixo, onde a "
                                    "morfologia é inequívoca."),
                revelar("Laudo do patologista",
                    p("“Vinte e quatro glomérulos amostrados, com crescentes "
                      "celulares em quinze deles, o que corresponde a 62%, e "
                      "necrose fibrinoide segmentar da alça capilar. Não se "
                      "observa esclerose global significativa. Fibrose "
                      "intersticial em cerca de 10% do córtex. À "
                      "imunofluorescência, ausência de depósitos "
                      "significativos de IgG, IgA, IgM, C3 e C1q, "
                      "configurando padrão pauci-imune. Não há depósito "
                      "linear ao longo da membrana basal glomerular.”")),
            ],
            [
                box("Classe crescêntica",
                    p("Mais da metade dos glomérulos ocupados por crescentes "
                      "celulares. Guarde o número: ele volta na conversa sobre "
                      "prognóstico renal.")),
                box("Eletroneuromiografia, do mesmo dia",
                    p("Mononeuropatia múltipla de padrão axonal, com "
                      "comprometimento assimétrico do nervo fibular comum à "
                      "direita e do ulnar à esquerda, e redução dos "
                      "potenciais sensitivos nos mesmos territórios.")),
            ],
        ),
        densidade="xd",
    ),
    bloco("O caso · bloco 8", "Crescente celular",
        cols(
            [crescente_glomerular(altura=248)],
            [
                box("O que a crescente é",
                    p("Proliferação de células no espaço de Bowman, em resposta "
                      "à ruptura da parede capilar. Ela ocupa o espaço, comprime "
                      "o tufo e interrompe a filtração daquele glomérulo. É a "
                      "lesão que explica queda de função renal em dias, e não "
                      "em meses.")),
                box("Por que a classe importa",
                    p("Crescente **celular** é lesão ativa, e lesão ativa "
                      "responde a imunossupressão. Crescente fibrosa e "
                      "esclerose global não respondem: são cicatriz. A "
                      "proporção entre uma coisa e outra é o que a "
                      "classificação de Berden mede, e é de onde vem a "
                      "estimativa de recuperação da função renal.")),
                nota("Antes de avançar",
                    p("Pergunte quantos por cento de crescentes eles esperam "
                      "encontrar antes de revelar o laudo. A turma costuma "
                      "subestimar — e a distância entre o palpite e os 62% é "
                      "o que fixa a noção de urgência.")),
            ],
        ),
        densidade="dense",
        ident="crescente_celular",
    ),
    P6,
    discussao("Os três padrões da imunofluorescência",
        cols(
            [padroes_imunofluorescencia(altura=214)],
            [
                p("A imunofluorescência da biópsia renal não gradua a lesão: "
                  "ela separa mecanismos. Depósito **linear** ao longo da "
                  "membrana basal é anticorpo contra o colágeno tipo IV. "
                  "Depósito **granular** é imunocomplexo. **Ausência** de "
                  "depósito é o padrão pauci-imune da vasculite associada ao "
                  "ANCA."),
                box("Pauci-imune não é exame negativo",
                    p("É o achado que fecha o diagnóstico. Quando o laudo diz "
                      "que não há depósitos significativos, ele está afirmando "
                      "alguma coisa, não deixando de afirmar. Vale insistir "
                      "nisso com a turma: a ausência aqui tem valor "
                      "diagnóstico positivo.")),
            ],
        ),
        densidade="dense",
        centro=True,
        ident="padroes_if",
    ),
    discussao("Classificação das vasculites associadas ao ANCA",
        p("Duas classificações convivem: uma clínica, pelo fenótipo, e outra "
          "sorológica, pelo antígeno reconhecido. Elas concordam na maioria "
          "dos pacientes e discordam numa minoria relevante. A sorológica "
          "prediz melhor o risco de recidiva e a resposta ao tratamento."),
        tabela(["", "Poliangiite microscópica", "Granulomatose com poliangiite", "Granulomatose eosinofílica"], [
            ["Sorologia típica", "Anti-MPO, p-ANCA", "Anti-PR3, c-ANCA", "Anti-MPO em 30 a 40%"],
            ["Granuloma", "Ausente", "Presente", "Presente, com eosinófilos"],
            ["Via aérea superior", "Ausente ou leve", "Destrutiva: sela, perfuração", "Pólipo nasal, rinite"],
            ["Pulmão", "Capilarite, hemorragia alveolar", "Nódulo escavado, massa, estenose", "Asma, infiltrado migratório"],
            ["Rim", "Muito frequente", "Frequente", "Menos frequente"],
            ["Asma e eosinofilia", "Ausentes", "Ausentes", "Obrigatórias"],
            ["Risco de recidiva", "Menor", "Maior", "Intermediário"],
            ["Neste paciente", "Compatível", "Improvável: sem granuloma e sem lesão destrutiva", "Excluída: sem asma, 320 eosinófilos"],
        ], tamanho="xs"),
        box("Revisar a lista de medicamentos",
            p("Hidralazina, propiltiouracila, minociclina e levamisol, este "
              "último como adulterante de cocaína, produzem anti-MPO em "
              "título alto e vasculite clinicamente indistinguível. Nenhum "
              "deles está em uso neste paciente, mas a pergunta é obrigatória "
              "e costuma não ser feita.")),
        densidade="xd",
    ),
    P7,
    momento("Quarta parte",
        "Tratamento",
        "O diagnóstico está fechado. A partir daqui as perguntas deixam de ser "
        "sobre o que o paciente tem e passam a ser sobre o que fazer com ele.",
        ident="p4_tratamento"),
    discussao("Indução de remissão",
        p("A indução tem duas peças que não se substituem. O glicocorticoide "
          "controla a inflamação em horas a dias. O imunossupressor impede "
          "que ela recomece. Corticoide isolado controla e recai; "
          "imunossupressor isolado é lento demais para um rim que está "
          "perdendo glomérulos."),
        cols(
            [
                tabela(["Componente", "Escolha", "Observação"], [
                    ["Glicocorticoide", "Pulso de metilprednisolona, seguido de oral em "
                            "desmame rápido", "O braço de dose reduzida do PEXIVAS teve "
                            "eficácia semelhante, com menos infecção grave"],
                    ["Imunossupressor", "Rituximabe ou ciclofosfamida", "Eficácia equivalente na indução. Rituximabe "
                            "preferido em jovens, na recidiva e quando a "
                            "fertilidade importa"],
                    ["Profilaxia", "Sulfametoxazol-trimetoprima para //Pneumocystis//", "Obrigatória. É a medida mais esquecida e a que "
                            "mais evita morte na indução"],
                    ["Ajuste de dose", "Ciclofosfamida reduzida pela idade e pela função "
                            "renal", "Com 63 anos e creatinina de 3,8, a dose plena "
                            "produz neutropenia previsível"],
                ], tamanho="sm"),
            ],
            [
                box("O que mudou nos últimos anos",
                    p("O avacopan, inibidor do receptor C5a, foi aprovado "
                      "como poupador de glicocorticoide e permite reduzir a "
                      "exposição acumulada ao corticoide. A disponibilidade e "
                      "o custo variam entre serviços.")),
                box("A ordem importa",
                    p("Imunossuprimir antes de ter a cultura do lavado é "
                      "apostar que não há infecção. Neste caso as culturas "
                      "voltaram negativas primeiro. Quando não é possível "
                      "esperar, cobre-se empiricamente e imunossuprime, mas a "
                      "decisão é registrada.")),
            ],
        ),
        densidade="dense",
    ),
    P8,
    discussao("Plasmaférese na vasculite ANCA",
        p("Durante décadas, creatinina elevada ou hemorragia alveolar "
          "indicavam plasmaférese quase automaticamente. O PEXIVAS, com 704 "
          "pacientes, não encontrou redução de morte ou de doença renal "
          "terminal com o uso amplo, e a conduta foi reorganizada."),
        tabela(["Situação", "Onde a conduta está hoje"], [
            ["Creatinina elevada, isoladamente", "Deixou de ser indicação automática"],
            ["Hemorragia alveolar com hipoxemia", "Ainda considerada caso a caso. O benefício não foi "
                    "demonstrado, e a decisão é individual"],
            ["Doença anti-membrana basal glomerular concomitante", "Indicação inequívoca. A dupla positividade com ANCA "
                    "ocorre em parcela não desprezível dos pacientes"],
            ["Doença refratária à indução", "Considerada como terapia de resgate"],
            ["Escolha do fluido de reposição", "Plasma fresco congelado se houver sangramento ativo ou "
                    "biópsia recente; albumina nas demais situações"],
        ], tamanho="sm"),
        box("O que a plasmaférese faz",
            p("Ela retira o anticorpo circulante. Não interrompe a produção. "
              "Sem imunossupressão concomitante, o título retorna em poucos "
              "dias.")),
        densidade="dense",
    ),
    momento("Quinta parte",
        "A complicação",
        "Nem toda piora sob tratamento é a doença piorando.",
        ident="p5_complicacao"),
    narrativa("O caso · bloco 9", "Evolução no quinto dia",
        cols(
            [
                p("O paciente recebeu pulso de metilprednisolona por três "
                  "dias, primeira dose de ciclofosfamida com ajuste para a "
                  "função renal, sulfametoxazol-trimetoprima profilático e "
                  "três sessões de plasmaférese com reposição de plasma "
                  "fresco congelado. Ao terceiro dia a hemoptise havia "
                  "cessado e a saturação subira para 94% com cateter nasal."),
                passo(p("Na manhã do quinto dia surgiu febre de 38,9 °C com "
                        "calafrio. Tornou-se taquipneico e passou a "
                        "necessitar de máscara com reservatório. A filha "
                        "notou que ele ficou confuso ao fim da tarde. A "
                        "diurese das últimas 24 horas foi de 380 mL, com "
                        "balanço hídrico acumulado positivo de 4,2 litros. A "
                        "pressão arterial era de 96/54 mmHg, a frequência "
                        "cardíaca de 118 batimentos por minuto e a frequência "
                        "respiratória de 32 incursões por minuto, com "
                        "saturação de 90% sob máscara.")),
            ],
            [
                cap("Exames colhidos naquela manhã"),
                painel([
                    exame("Hemoglobina", "6,9 g/dL {{(era 7,8)}}",
                           "13,5 a 17,5", "critico"),
                    exame("Leucócitos", "1.900/mm³ {{(eram 14.200)}}",
                           "4.000 a 11.000", "critico"),
                    exame("Neutrófilos", "620/mm³",
                           "1.800 a 7.000", "critico"),
                    exame("Plaquetas", "172.000/mm³",
                           "150.000 a 450.000"),
                    exame("Creatinina", "4,6 mg/dL {{(era 3,8)}}",
                           "até 1,3", "critico"),
                    exame("Procalcitonina", "3,1 ng/mL {{(era 0,4)}}",
                           "abaixo de 0,5", "critico"),
                    exame("PCR", "204 mg/L",
                           "até 5", "alterado"),
                    exame("Radiografia de tórax", "Infiltrado que piorou, agora assimétrico",
                           "—", "alterado"),
                ]),
                nota("Antes de avançar",
                    p("Peça três hipóteses e, para cada uma, um exame. O dado "
                      "que reorganiza a lista é a neutropenia de 620, "
                      "produzida pelo tratamento que foi prescrito cinco dias "
                      "antes.")),
            ],
        ),
        densidade="dense",
    ),
    P9,
    discussao("Deterioração durante a indução",
        p("A partir do momento em que a indução começa, toda piora passa a "
          "ter duas explicações possíveis, e elas pedem condutas opostas. "
          "Doença não controlada pede mais imunossupressão. Complicação do "
          "tratamento pede menos."),
        tabela(["Hipótese", "O que favorece", "O que pedir", "Conduta se confirmada"], [
            ["Infecção", "Procalcitonina de 0,4 para 3,1; neutrófilos de 620; "
                    "febre com calafrio; infiltrado assimétrico", "Hemoculturas, cultura de aspirado traqueal, radiografia, "
                    "tomografia", "Antibiótico para neutropenia febril, e considerar "
                    "postergar a próxima dose"],
            ["Doença ativa", "Hemoptise que retorna, sedimento com mais cilindros, "
                    "ANCA em ascensão", "Sedimento urinário, hemoglobina seriada, broncoscopia", "Intensificar a indução, considerar resgate"],
            ["Sobrecarga volêmica", "Balanço de +4,2 L com diurese de 380 mL; infiltrado "
                    "bilateral difuso", "Peso diário, balanço hídrico, ultrassom de veia cava e "
                    "pulmão", "Diurético, ou diálise por hipervolemia"],
            ["Novo sangramento alveolar", "Queda adicional de hemoglobina com infiltrado que piora", "Broncoscopia com lavado", "Corrigir coagulação e intensificar o tratamento da "
                    "vasculite"],
            ["Tromboembolismo", "Vasculite ativa é estado protrombótico reconhecido; "
                    "imobilidade", "Angiotomografia de tórax", "Anticoagulação, pesando o risco de sangramento alveolar"],
        ], tamanho="xs"),
        densidade="dense",
    ),
    narrativa("O caso · bloco 10", "Evolução",
        cols(
            [
                p("Foram colhidas hemoculturas e iniciado cefepima empírico "
                  "na primeira hora. As culturas cresceram //Staphylococcus "
                  "aureus// sensível a oxacilina em dois de dois pares, com o "
                  "cateter venoso central como foco provável. O cateter foi "
                  "retirado e o esquema desescalonado no terceiro dia. A "
                  "segunda dose de ciclofosfamida foi postergada até a "
                  "recuperação dos neutrófilos, e filgrastim foi administrado "
                  "por três dias."),
                passo(p("A partir do sexto dia necessitou de hemodiálise "
                        "intermitente por hipervolemia e uremia, durante "
                        "dezoito dias. Recuperou diurese na quarta semana e "
                        "saiu de diálise, com creatinina estabilizando em 2,1 "
                        "mg/dL, o que corresponde a filtração glomerular "
                        "estimada de 32 mL/min/1,73 m².")),
            ],
            [
                p("A hemoptise não retornou. A hemoglobina subiu para 9,4 "
                  "g/dL sem nova transfusão. O pé direito mantinha força de "
                  "3/5 para dorsiflexão na alta, em fisioterapia, com uso de "
                  "órtese. As lesões purpúricas desapareceram na segunda "
                  "semana."),
                passo(p("Recebeu alta no 32º dia, com prednisona em desmame, "
                        "rituximabe programado para manutenção, "
                        "sulfametoxazol-trimetoprima profilático, plano de "
                        "vacinação respeitando a janela do rituximabe, e "
                        "consultas de nefrologia e reumatologia agendadas "
                        "para duas semanas.")),
                box("Registrado no resumo de alta",
                    p("Anti-MPO de 148 U/mL na admissão e de 28 U/mL na alta. "
                      "Sedimento urinário com 6 hemácias por campo, sem "
                      "cilindros hemáticos. Proteinúria de 0,7 g em 24 horas.")),
            ],
        ),
        densidade="dense",
    ),
    bloco("Síntese", "Pontos principais",
        cols(
            [
                lista([
                     "Dois territórios distantes acometidos simultaneamente "
                     "pedem uma explicação única. No pulmão e no rim, essa "
                     "explicação costuma estar no vaso de pequeno calibre.",
                     "O cilindro hemático localiza o sangramento no "
                     "glomérulo. A fita reagente não o detecta.",
                     "Complemento normal mantém a vasculite ANCA e a doença "
                     "anti-MBG na lista, e torna lúpus e crioglobulinemia "
                     "menos prováveis.",
                     "O anti-MBG é o exame de maior urgência do painel, "
                     "porque nele a demora de poucos dias custa a função "
                     "renal de forma definitiva.",
                     "Crioglobulina colhida em tubo frio precipita no "
                     "trajeto, e o resultado negativo não vale.",
                    ], ordenada=True),
            ],
            [
                lista([
                     "A hemorragia alveolar se comprova na broncoscopia: "
                     "alíquotas progressivamente hemorrágicas e "
                     "hemossiderófagos acima de 20%.",
                     "As culturas negativas do lavado são o que autoriza a "
                     "imunossupressão.",
                     "Creatinina elevada isoladamente deixou de indicar "
                     "plasmaférese. A doença anti-MBG concomitante continua "
                     "indicando.",
                     "Toda piora durante a indução admite duas leituras "
                     "opostas. A neutropenia febril decide a favor da "
                     "infecção.",
                    ], ordenada=True),
            ],
        ),
        densidade="dense",
    ),
    bloco("Anexo", "Checklist: síndrome pulmão-rim",
        cols(
            [
                h3("Na primeira hora"),
                lista([
                     "Sedimento urinário em urina fresca, com pesquisa de "
                     "dismorfismo e de cilindros.",
                     "Anti-MBG e ANCA, por imunofluorescência e por ELISA "
                     "para PR3 e MPO, no mesmo pedido.",
                     "Complemento C3 e C4, FAN, crioglobulinas em tubo "
                     "aquecido.",
                     "Hemoculturas e sorologias virais antes de qualquer "
                     "imunossupressor.",
                     "Tomografia de tórax e gasometria arterial.",
                     "Avaliar necessidade de suporte ventilatório e de "
                     "diálise por critério clínico.",
                    ]),
                h3("Antes de imunossuprimir"),
                lista([
                     "Broncoscopia com lavado, com cultura para bactérias, "
                     "fungos e micobactérias.",
                     "Rastreio de tuberculose e de hepatite B.",
                     "Revisar a lista de medicamentos: hidralazina, "
                     "propiltiouracila, minociclina, levamisol.",
                     "Discutir preservação de fertilidade antes da "
                     "ciclofosfamida.",
                    ]),
            ],
            [
                h3("Indução"),
                lista([
                     "Pulso de metilprednisolona, com desmame rápido do "
                     "corticoide oral.",
                     "Rituximabe ou ciclofosfamida, com dose ajustada à idade "
                     "e à função renal.",
                     "Sulfametoxazol-trimetoprima para //Pneumocystis//.",
                     "Plasmaférese se o anti-MBG for positivo; caso a caso na "
                     "hemorragia alveolar.",
                    ]),
                h3("Manutenção e alta"),
                lista([
                     "Manutenção por anos, com rituximabe programado ou "
                     "azatioprina.",
                     "Vacinação planejada em torno da janela do rituximabe. "
                     "Vacina viva contraindicada.",
                     "Proteção óssea e gástrica, controle de pressão arterial "
                     "e de lipídios.",
                     "Creatinina, sedimento urinário e proteinúria em série. "
                     "O sedimento detecta a recidiva primeiro.",
                     "Consulta e exame agendados na alta, e não retorno por "
                     "demanda espontânea.",
                    ]),
            ],
        ),
        densidade="xd",
    ),
    bloco("Fontes e créditos", "Fontes, créditos e licenças",
        cols(
            [
                h3("Referências"),
                lista([
                     "Walsh M et al. Plasma exchange and glucocorticoids in "
                     "severe ANCA-associated vasculitis (PEXIVAS). //N Engl J "
                     "Med// 2020;382:622-31.",
                     "Stone JH et al. Rituximab versus cyclophosphamide for "
                     "ANCA-associated vasculitis (RAVE). //N Engl J Med// "
                     "2010;363:221-32.",
                     "Jones RB et al. Rituximab versus cyclophosphamide in "
                     "ANCA-associated renal vasculitis (RITUXVAS). //N Engl J "
                     "Med// 2010;363:211-20.",
                     "Jayne DRW et al. Avacopan for the treatment of "
                     "ANCA-associated vasculitis (ADVOCATE). //N Engl J Med// "
                     "2021;384:599-609.",
                     "Berden AE et al. Histopathologic classification of "
                     "ANCA-associated glomerulonephritis. //J Am Soc "
                     "Nephrol// 2010;21:1628-36.",
                     "Guillevin L et al. Rituximab versus azathioprine for "
                     "maintenance (MAINRITSAN). //N Engl J Med// "
                     "2014;371:1771-80.",
                     "Chung SA et al. 2021 ACR/VF guideline for the "
                     "management of ANCA-associated vasculitis. //Arthritis "
                     "Rheumatol// 2021;73:1366-83.",
                     "Suppiah R, Robson JC et al. 2022 ACR/EULAR "
                     "classification criteria for microscopic polyangiitis "
                     "and granulomatosis with polyangiitis. //Ann Rheum Dis// "
                     "2022;81:315-20 e 321-6.",
                    ]),
            ],
            [
                h3("Imagens"),
                lista([
                     "Tomografia de tórax: Hellerhoff · Wikimedia Commons · "
                     "CC BY-SA 4.0.",
                     "Biópsia renal: Nephron · Wikimedia Commons · CC BY-SA "
                     "3.0.",
                     "Imunofluorescência p-ANCA: Simon Caulton · Wikimedia "
                     "Commons · CC BY-SA 3.0.",
                    ]),
                h3("Desenhos"),
                lista([
                     "Mapa de territórios, parede capilar compartilhada, "
                     "crescente glomerular e padrões de imunofluorescência: "
                     "esquemas autorais em SVG, desenhados para este caso.",
                    ]),
                box("Sobre este material",
                    p("Caso autoral, construído para ensino de internos e "
                      "residentes. O paciente é ficcional e os dados "
                      "laboratoriais foram desenhados para serem internamente "
                      "coerentes. As imagens são ilustrativas, de "
                      "repositórios de licença aberta, e não pertencem a este "
                      "paciente. As condutas devem ser confrontadas com as "
                      "diretrizes vigentes e com os protocolos do serviço.")),
            ],
        ),
        densidade="xd",
    ),
]

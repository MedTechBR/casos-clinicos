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
    capilar_compartilhado, crescente_glomerular, linha_do_tempo,
    mapa_do_corpo, marco, padroes_imunofluorescencia, quadro,
)
from motor.slides import bloco, capa, discussao, momento, narrativa, tela

from motor.arvore import estado
from .arvore import (
    B_CEDO, B_CFX, B_ESPERA, B_IMAGEM, B_IMAGEM_2, B_PAINEL, B_PAINEL_2,
    B_RESGATE, B_RTX, B_SO_DIALISE, F, N0, N1, N2A, N2B, N3A, N3B, N3C, N3D,
)
from .banco import BANCO
from .hipoteses import DENTRO, HIPOTESES, RIM, SISTEMICO, TORAX
from .perguntas import (
    P1, P3, P4, P5, P6, P7, P8, P9, P10, P11, P12, P13, P14, P15,
)

TITULO = "Homem de 63 anos com hemoptise, púrpura e queda de função renal"
SLUG = "pulmao-rim"
RODAPE = "Síndrome pulmão-rim · caso interativo"
IMG = Path(__file__).parent / "img"

# O estado do paciente na admissão. A partir do primeiro nó ele muda com a
# conduta, com os exames pedidos e com o relógio, e a barra mostra sempre.
ESTADO = estado(horas=0, creatinina=3.8, spo2=88, hb=7.8)


SLIDES = [
    capa(
        "Homem de 63 anos com hemoptise, púrpura e queda de função renal",
        "Sintomas nasais, articulares, pulmonares e renais ao longo de oito "
        "semanas.",
        "**4 decisões · 8 desfechos · 100 a 120 minutos** O caso começa nas "
        "síndromes e só estreita quando um resultado autoriza. Não corre em "
        "linha reta: o que o grupo pedir e o que decidir mudam o que as telas "
        "seguintes mostram, e o paciente que chega ao fim é outro. "
        "{{M abre o mapa da árvore; V volta ao nó anterior.}}",
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
        densidade="xd",
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
        "De que síndromes se trata",
        "Ainda não é hora de nomear doença. Antes disso há duas perguntas mais "
        "baratas e mais difíceis: de onde vem o sangue, e o que amarra oito "
        "semanas de sintomas em quatro territórios.",
        ident="p2_diferencial"),
    discussao("De onde vem o sangue",
        p("Sangue que sai pela boca pode vir do nariz, do brônquio, do alvéolo "
          "ou do capilar pulmonar, e cada origem manda pedir um exame "
          "diferente. A coluna do meio não diz o que este paciente tem — diz "
          "o que **teria de ser verdade** para cada linha ser a resposta, e é "
          "essa coluna que a investigação vai testar."),
        quadro(TORAX, {
            "congestao": ("derrubada",
                          "Sem estase jugular, terceira bulha ou edema; "
                          "ausculta cardíaca normal"),
        }, titulo="Levantado pelo grupo, ao fim do exame físico",
           novos=["congestao"]),
        nota("Como conduzir",
            p("Não mostre a lista pronta. Peça as origens à turma primeiro — "
              "nariz, brônquio, alvéolo — e escreva no quadro branco. Quem "
              "responde “vasculite” está pulando um degrau: vasculite é "
              "explicação, não topografia.")),
        densidade="xd",
        ident="sind_torax",
    ),
    discussao("O que amarra oito semanas",
        p("Febre vespertina, perda de 6 kg, artralgia migratória, púrpura "
          "palpável e mononeurite múltipla, instalados em oito semanas. A "
          "pergunta é se existe um mecanismo único ou se são coisas "
          "independentes num paciente de 63 anos — e, se for único, de que "
          "natureza."),
        quadro(SISTEMICO,
               titulo="Levantado pelo grupo, ao fim do exame físico"),
        nota("Como conduzir",
            p("Pergunte o que a turma esqueceu. Em geral esquecem a neoplasia "
              "oculta e a droga — e a droga importa aqui porque ele usa "
              "losartana, que não causa isto, e a pergunta certa é o que mais "
              "ele toma, incluindo o que não foi prescrito.")),
        densidade="xd",
        ident="sind_sistemica",
    ),
    *P15,
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
                    exame("Filtração glomerular estimada", "17 mL/min/1,73 m²",
                           "acima de 90", "critico"),
                    exame("Potássio", "5,4 mEq/L",
                           "3,5 a 5,0", "alterado"),
                    exame("Bicarbonato", "15 mEq/L",
                           "22 a 26", "alterado"),
                    exame("pH / pO2", "7,29 / 56 mmHg",
                           "7,35 a 7,45 / 80 a 100", "alterado"),
                    exame("PaO2/FiO2", "267",
                           "acima de 300", "critico"),
                    exame("Albumina", "2,9 g/dL",
                           "3,5 a 5,2", "alterado"),
                    exame("Ultrassom renal",
                           "Rins de 11,2 e 11,0 cm, sem hidronefrose",
                           "sem dilatação"),
                ]),
            ],
        ),
        ident="exames_admissao",
    ),
    discussao("Topografia da lesão renal",
        p("A creatinina era de 1,0 mg/dL há dois meses e está em 3,8 agora. "
          "Isso diz que o rim parou e não diz em que compartimento — e as "
          "condutas dos cinco compartimentos são incompatíveis entre si. Um "
          "exame de bancada responde a pergunta; nenhum exame de sangue "
          "responde."),
        quadro(RIM,
               titulo="A terceira pergunta em aberto, com o rim já dentro do caso"),
        nota("Como conduzir",
            p("Pergunte que exame decide entre as cinco linhas antes de "
              "mostrar a próxima tela. Se a turma responder “biópsia”, "
              "pergunte o que ela faria se a biópsia levasse três dias — que "
              "é o que ela leva.")),
        densidade="xd",
        ident="sind_rim",
    ),
    N0,
    # Cada rota da investigação corre inteira aqui, na ordem em que o grupo a
    # pediu, e só depois desemboca no resultado imunológico. O ramo A não passa
    # por nada disto: ele salta direto para os exames da admissão.
    B_PAINEL, *P13, B_PAINEL_2,
    B_IMAGEM, *P14, B_IMAGEM_2,
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
    discussao("Topografia da lesão renal",
        p("O sedimento não nomeou nenhuma doença. Ele fez o que vem antes: "
          "localizou a lesão dentro do néfron. Creatinina de 3,8 mg/dL diz que "
          "o rim parou de funcionar e não diz em que compartimento — e as "
          "condutas dos cinco compartimentos são incompatíveis entre si."),
        quadro(RIM, {
            "glomerular": ("confirmada",
                           "Hemácias dismórficas em 40% e cilindros hemáticos, "
                           "com proteinúria de 2,4 g em 24 horas"),
            "pre_renal": ("derrubada",
                          "Sedimento com cilindros: hipoperfusão dá sedimento "
                          "limpo, e nenhum volume corrige um glomérulo"),
            "nta": ("derrubada",
                    "Cilindro hemático não se forma na necrose tubular; os "
                    "granulosos aqui acompanham a lesão glomerular"),
            "nia": ("derrubada",
                    "Oito leucócitos por campo, sem cilindro leucocitário, "
                    "sem eosinofilúria e sem droga nova"),
            "obstrutiva": ("derrubada",
                           "Rins de tamanho preservado, sem dilatação "
                           "pielocalicial à ultrassonografia"),
        }, titulo="Depois do sedimento urinário", passo_a_passo=False),
        nota("Antes de avançar",
            p("Vale dizer em voz alta o que este quadro NÃO fez: ele não "
              "aproximou o caso de nenhum diagnóstico. Trocou uma pergunta "
              "grande — “por que o rim parou?” — por uma menor e respondível, "
              "que é “o que agride este glomérulo?”. É assim que se estreita.")),
        densidade="xd",
        ident="rim_fechado",
    ),
    P4,
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
                      "pneumonite: quatro das linhas do quadro do tórax, e a "
                      "imagem não escolhe entre elas. O que ela resolve é por "
                      "exclusão — sem massa nem nódulo escavado, sem derrame, "
                      "sem cardiomegalia, e sem falha de enchimento.")),
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
    discussao("A primeira síndrome se fecha",
        p("O lavado resolveu a pergunta com que o caso começou. O sangue não "
          "vem do nariz nem de um brônquio: vem do alvéolo, difusamente, e há "
          "pelo menos dois dias. E nada cresceu."),
        quadro(TORAX, {
            "hemorragia": ("confirmada",
                           "Alíquotas progressivamente hemorrágicas e "
                           "hemossiderófagos em 34% dos macrófagos"),
            "via_aerea": ("derrubada",
                          "Sem lesão endobrônquica, sem sangramento de sítio "
                          "único e com o parênquima difusamente acometido"),
            "pneumonia": ("derrubada",
                          "Culturas do lavado e hemoculturas negativas, "
                          "procalcitonina de 0,4 ng/mL"),
            "tuberculose": ("derrubada",
                            "Baciloscopia e teste molecular negativos no "
                            "lavado"),
            "neoplasia": ("derrubada",
                          "Sem massa, nódulo ou lesão endobrônquica"),
            "tep": ("derrubada",
                    "Sem falha de enchimento e sem opacidade de base pleural"),
            "congestao": ("derrubada",
                          "Sem estase jugular, terceira bulha ou edema; "
                          "ausculta cardíaca normal"),
        }, titulo="Depois da tomografia e do lavado broncoalveolar",
           novos=["hemorragia", "via_aerea", "pneumonia", "tuberculose",
                  "neoplasia", "tep"]),
        densidade="xd",
        ident="torax_fechado",
    ),
    discussao("O que o complemento separa",
        p("Complemento normal não é resultado sem graça: é uma das "
          "bifurcações mais baratas da investigação da glomerulonefrite. Ele "
          "divide as causas em dois grupos que quase não se misturam — as que "
          "consomem complemento e as que não consomem — e a divisão vale "
          "independentemente de qual doença esteja por trás."),
        cols(
            [
                h3("Consomem complemento"),
                lista([
                     "Lúpus eritematoso sistêmico, com C3 e C4 baixos.",
                     "Crioglobulinemia mista, com C4 desproporcionalmente "
                     "baixo em relação ao C3.",
                     "Glomerulonefrite pós-infecciosa e endocardite, com C3 "
                     "baixo e C4 preservado.",
                     "Glomerulopatia por C3, com C3 baixo persistente.",
                    ]),
            ],
            [
                h3("Não consomem"),
                lista([
                     "Vasculites de pequeno vaso associadas ao ANCA.",
                     "Doença anti-membrana basal glomerular.",
                     "Vasculite por IgA e nefropatia por IgA.",
                    ]),
                box("O que este resultado faz, e o que não faz",
                    p("C3 de 112 e C4 de 28 mg/dL, com FAN e anti-DNA não "
                      "reagentes, empurram o caso inteiro para a coluna da "
                      "direita. Nenhuma doença foi nomeada, e nenhuma foi "
                      "testada: o que mudou foi a probabilidade a priori de "
                      "dois grupos inteiros.")),
            ],
        ),
        densidade="xd",
        ident="complemento",
    ),
    discussao("A segunda síndrome se fecha",
        p("Do lado sistêmico, o mesmo movimento. Nenhum foco, nenhum agente, "
          "nenhum autoanticorpo de conectivopatia, nenhuma droga que explique. "
          "Sobra o mecanismo que o exame físico já sugeria e que nenhum exame "
          "ainda testou."),
        quadro(SISTEMICO, {
            "vasculite_sist": ("confirmada",
                               "Capilar alveolar e capilar glomerular "
                               "acometidos ao mesmo tempo, com pele e nervo "
                               "periférico juntos"),
            "infeccao_arrastada": ("derrubada",
                                   "Lavado e hemoculturas estéreis, sem foco "
                                   "à tomografia"),
            "endocardite": ("derrubada",
                            "Três pares de hemocultura negativos em cinco "
                            "dias, ecocardiograma sem vegetação"),
            "conectivopatia": ("derrubada",
                               "FAN e anti-DNA não reagentes, complemento "
                               "normal"),
            "droga_sist": ("enfraquecida",
                           "Losartana não tem esse perfil; a lista das que "
                           "têm precisa ser perguntada de novo, e nominalmente"),
        }, titulo="Depois do complemento, das culturas e do ecocardiograma",
           novos=["vasculite_sist", "infeccao_arrastada", "endocardite",
                  "conectivopatia", "droga_sist"]),
        densidade="xd",
        ident="sist_fechado",
    ),
    momento("Terceira parte",
        "As duas síndromes se encontram",
        "Hemorragia alveolar de um lado, glomerulonefrite rapidamente "
        "progressiva do outro, no mesmo paciente e ao mesmo tempo. Só agora a "
        "palavra pulmão-rim significa alguma coisa — e só agora a lista de "
        "doenças cabe na tela.",
        ident="p_encontro"),
    discussao("O que faz as duas coisas ao mesmo tempo",
        p("Esta lista é curta, e a turma consegue levantá-la em voz alta. Ela "
          "não podia ter sido feita duas horas atrás: fazer o diferencial de "
          "síndrome pulmão-rim antes de provar hemorragia alveolar e "
          "glomerulonefrite é responder a uma pergunta que ainda não tinha "
          "sido feita."),
        quadro(HIPOTESES, {
            "lepto": ("derrubada",
                      "Oito semanas de curso, sem exposição a enchente ou "
                      "roedor: a forma pulmonar hemorrágica se instala em "
                      "dias, não em meses"),
            "lupus": ("derrubada",
                      "C3 e C4 normais, FAN e anti-DNA não reagentes"),
            "crio": ("derrubada",
                     "C4 de 28 mg/dL: a crioglobulinemia consome C4 de forma "
                     "desproporcional"),
            "endocardite": ("derrubada",
                            "Hemoculturas negativas, ecocardiograma sem "
                            "vegetação"),
        }, titulo="O que o caminho até aqui já derrubou",
           novos=["lepto", "lupus", "crio", "endocardite"]),
        nota("Antes de avançar",
            p("Quatro linhas de pé, e nenhuma delas foi testada — as "
              "sorologias específicas ainda não voltaram. É este o momento de "
              "decidir se a imunossupressão espera o resultado. Deixe a turma "
              "se dividir antes de virar a tela.")),
        densidade="xd",
        ident="pulmao_rim",
    ),
    P10,
    momento("Quarta parte",
        "O resultado que estava pendente",
        "O painel imunológico voltou. Quanto tempo ele levou depende de "
        "quando foi pedido.",
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
    P11,
    discussao("Sobram duas",
        p("O p-ANCA em 1:640 com anti-MPO de 148 U/mL, o anti-MBG não reagente "
          "e a lista de medicações limpa reduzem a lista a duas linhas — e o "
          "painel imunológico não sabe separá-las, porque a vasculite por IgA "
          "não tem sorologia. Quem decide é o tecido."),
        quadro(HIPOTESES, {
            "lepto": ("derrubada", "Curso de oito semanas, sem exposição"),
            "lupus": ("derrubada", "Complemento normal, FAN não reagente"),
            "crio": ("derrubada", "C4 normal, crioglobulinas negativas"),
            "endocardite": ("derrubada",
                            "Hemoculturas negativas, ecocardiograma sem "
                            "vegetação"),
            "mbg": ("derrubada", "Anti-MBG não reagente"),
            "droga": ("derrubada",
                      "Em uso apenas de losartana e sinvastatina; nenhuma das "
                      "quatro drogas implicadas"),
            "anca": ("confirmada",
                     "p-ANCA 1:640, anti-MPO 148 U/mL — falta a biópsia dizer "
                     "se é pauci-imune"),
        }, titulo="Depois do painel imunológico",
           novos=["mbg", "droga", "anca"]),
        nota("Antes de avançar",
            p("Pergunte por que a vasculite por IgA continua de pé. Púrpura "
              "palpável, artralgia e glomerulonefrite com complemento normal "
              "descrevem os dois candidatos igualmente bem, e não existe "
              "exame de sangue que a confirme. A imunofluorescência da "
              "biópsia é o único árbitro — e é a próxima tela.")),
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
                box("Ativa contra cicatriz",
                    p("Crescente **celular** é lesão ativa e responde a "
                      "imunossupressão. Crescente fibrosa e esclerose global "
                      "são cicatriz e não respondem. A distinção é verdadeira — "
                      "e não é o que a classificação de Berden faz.")),
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
    discussao("A classificação de Berden",
        cols(
            [
                p("Berden não calcula proporção entre lesão ativa e crônica. "
                  "Ela é **categórica**: aloca a biópsia inteira numa de quatro "
                  "classes mutuamente exclusivas, pela regra dos 50%, contando "
                  "na microscopia óptica apenas três coisas — glomérulos "
                  "globalmente escleróticos, glomérulos normais e glomérulos "
                  "com crescentes celulares —, e nessa ordem."),
                tabela(["Se…", "A classe é"], [
                    ["Metade ou mais globalmente esclerosados", "Esclerótica"],
                    ["Senão, metade ou mais **normais**", "Focal"],
                    ["Senão, metade ou mais com crescente celular", "Crescêntica"],
                    ["Sem predomínio de nenhum padrão", "Mista"],
                ], tamanho="sm"),
            ],
            [
                box("A variável que mais pesa não é o crescente",
                    p("É o glomérulo poupado: a classe focal é definida pela "
                      "preservação, não pela lesão. E repare no que fica de "
                      "fora — Berden só olha o glomérulo, de modo que a fibrose "
                      "intersticial de 10% deste laudo, a atrofia tubular e a "
                      "própria creatinina não entram na conta."),
                    tipo="pausa"),
                box("A contraintuição que vale discutir",
                    p("Na coorte original, a sobrevida renal em cinco anos foi "
                      "de 93% na focal, 76% na crescêntica, 61% na mista e 50% "
                      "na esclerótica. A crescêntica, apesar do aspecto "
                      "dramático, teve a segunda melhor: muito crescente "
                      "celular é muita lesão potencialmente reversível. A "
                      "urgência deste caso vem da velocidade da perda e da "
                      "hemorragia alveolar, não de a classe ser a pior.")),
                nota("Se a turma perguntar",
                    p("A literatura posterior sustenta os extremos e desmancha "
                      "o meio: a metanálise de 2017 confirmou focal melhor que "
                      "crescêntica e crescêntica melhor que esclerótica, mas "
                      "não achou diferença entre crescêntica e mista. Vinte e "
                      "quatro glomérulos amostrados, acima do mínimo de dez que "
                      "a classificação exige, tornam a classe confiável aqui.")),
            ],
        ),
        densidade="dense",
        ident="berden",
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
            ["Granuloma", "Ausente", "Esperado na via aérea e no pulmão; quase nunca no rim", "Presente, com eosinófilos"],
            ["Via aérea superior", "Ausente ou leve", "Destrutiva: sela, perfuração", "Pólipo nasal, rinite"],
            ["Pulmão", "Capilarite, hemorragia alveolar", "Nódulo escavado, massa, estenose", "Asma, infiltrado migratório"],
            ["Rim", "Muito frequente", "Frequente", "Menos frequente"],
            ["Asma e eosinofilia", "Ausentes", "Ausentes", "Obrigatórias"],
            ["Risco de recidiva", "Menor", "Maior", "Intermediário"],
            ["Neste paciente", "Compatível", "Improvável, mas **não pela biópsia**: pesa o anti-MPO e a ausência de nódulo escavado", "Excluída: sem asma, 320 eosinófilos"],
        ], tamanho="xs"),
        densidade="xd",
    ),
    discussao("Duas armadilhas da classificação",
        cols(
            [
                box("Ausência de granuloma no rim não conta contra a GPA",
                    p("A biópsia deste paciente é **renal**, e granuloma "
                      "praticamente não aparece no rim — nem mesmo na "
                      "granulomatose com poliangiite. Na meta-análise de Bajema "
                      "e cols., de 1997, que reuniu 349 casos publicados, das "
                      "134 biópsias renais apenas sete mostravam granuloma "
                      "renal, cerca de 5%, contra 70% de proliferação "
                      "extracapilar e 54% de necrose fibrinoide."),
                    p("O granuloma da GPA mora na via aérea e no pulmão; no "
                      "rim, a lesão da GPA e a da poliangiite microscópica são "
                      "a mesma glomerulonefrite pauci-imune necrosante. E nos "
                      "critérios ACR/EULAR de 2022 o item é granuloma em "
                      "qualquer tecido, somando dois pontos quando presente e "
                      "zero quando ausente: a ausência jamais subtrai."),
                    tipo="erro"),
            ],
            [
                box("Revisar a lista de medicamentos",
                    p("Hidralazina, propiltiouracila, minociclina e levamisol, "
                      "este último como adulterante de cocaína, produzem "
                      "anti-MPO em título alto e vasculite clinicamente "
                      "indistinguível. Nenhum deles está em uso neste paciente, "
                      "mas a pergunta é obrigatória e costuma não ser feita."),
                    tipo="erro"),
                nota("Antes de avançar",
                    p("Pergunte em qual das duas a turma cairia. A primeira é "
                      "erro de raciocínio: concluir a partir do tecido errado. "
                      "A segunda é erro de anamnese: não perguntar. As duas são "
                      "mais comuns do que erro de leitura de exame.")),
            ],
        ),
        densidade="dense",
        ident="armadilhas_classificacao",
    ),
    discussao("O fenótipo desta vasculite",
        p("O funil chegou ao último nível, e ele não fecha inteiramente. "
          "Vasculite associada ao ANCA está estabelecida; qual delas é uma "
          "questão de fenótipo, e o fenótipo deste paciente tem uma peça "
          "ambígua — crostas e anosmia são doença de via aérea superior, mas "
          "não a doença destrutiva da granulomatose."),
        quadro(DENTRO, {
            "mpa": ("confirmada",
                    "Anti-MPO em título alto, capilarite alveolar, "
                    "glomerulonefrite pauci-imune, sem granuloma e sem lesão "
                    "destrutiva de via aérea"),
            "egpa": ("derrubada",
                     "Sem asma e com 320 eosinófilos/mm³"),
            "renal_limitada": ("derrubada",
                               "Pulmão, pele e nervo periférico acometidos"),
            "droga_anca": ("derrubada",
                           "Nenhuma das quatro drogas implicadas em uso"),
            "gpa": ("enfraquecida",
                    "Sintomas nasais existem, mas sem perfuração, sela ou "
                    "nódulo escavado; anti-PR3 não reagente"),
        }, titulo="Depois da biópsia e da revisão do fenótipo",
           passo_a_passo=False),
        nota("Antes de avançar",
            p("Diga à turma que a linha enfraquecida vai ficar enfraquecida. "
              "O tratamento de indução das duas é o mesmo, e a distinção só "
              "muda a conversa sobre risco de recidiva e duração da "
              "manutenção. Nem todo caso termina com uma linha só — terminar "
              "com duas e saber o que cada uma implicaria também é resposta.")),
        densidade="xd",
        ident="dentro_anca",
    ),
    P7,
    momento("Quinta parte",
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
                    ["Profilaxia", "Sulfametoxazol-trimetoprima para //Pneumocystis//", "400/80 mg por dia, ou 800/160 mg em dias "
                            "alternados. Recomendação de grau B, apoiada em "
                            "estudo observacional, não em ensaio"],
                    ["Ajuste de dose", "Ciclofosfamida reduzida pela idade e pela função "
                            "renal", "Com 63 anos e creatinina de <<creatinina>>, a dose plena "
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
    discussao("O que o PEXIVAS derrubou, e o que não",
        p("O PEXIVAS randomizou 704 pacientes com filtração abaixo de 50 "
          "mL/min/1,73 m² ou hemorragia pulmonar difusa e não encontrou "
          "benefício no desfecho composto de morte ou doença renal terminal: "
          "28,4% contra 31,0%. O que ele derrubou foi a indicação ampla e "
          "automática. O que ele **não** mostrou é que a plasmaférese não "
          "serve para ninguém — o desfecho era composto e dominado pela "
          "mortalidade."),
        p("A meta-análise posterior separou os componentes, e é aí que a "
          "decisão muda de natureza: sem efeito sobre mortalidade, com "
          "**redução** de doença renal terminal em doze meses e com "
          "**aumento** de infecção grave. Deixou de ser uma pergunta sobre "
          "sobrevida e virou uma troca explícita entre rim e infecção."),
        box("Onde as três sociedades concordam, e onde não",
            tabela(["", "Creatinina alta", "Hemorragia alveolar com hipoxemia",
                    "Sobreposição anti-MBG"], [
                ["KDIGO 2024", "Considerar acima de 3,4 mg/dL",
                 "Considerar", "**Acrescentar**"],
                ["EULAR 2022", "Considerar acima de 3,4 mg/dL",
                 "Não de rotina", "Acrescentar"],
                ["ACR/VF 2021", "Condicionalmente contra o acréscimo de rotina",
                 "Condicionalmente contra", "Aconselhável"],
            ], tamanho="sm")),
        box("O limiar de creatinina não sumiu: baixou",
            p("O KDIGO de 2021 falava em 5,7 mg/dL. O de 2024 desceu para 3,4, "
              "justificando com redução absoluta de doença renal terminal em "
              "doze meses de 4,6% na faixa entre 3,4 e 5,7 — cerca de vinte e "
              "dois pacientes tratados para evitar um rim terminal. Este "
              "paciente, com <<creatinina>>, preenche o gatilho."),
            tipo="pausa"),
        densidade="dense",
        ident="plasmaferese",
    ),
    discussao("A conduta neste paciente",
        cols(
            [
                p("Anti-MBG não reagente: não há a sobreposição que **impõe** "
                  "plasmaférese. Creatinina de <<creatinina>> e hemorragia alveolar "
                  "com saturação de <<spo2>>: dois dos três gatilhos que mandam "
                  "**considerar**."),
                p("Foram feitas três sessões, com albumina como reposição, em "
                  "dias alternados, junto da indução — e não no lugar dela. A "
                  "plasmaférese retira o anticorpo circulante e não interrompe "
                  "a produção: sem imunossupressão concomitante o título volta "
                  "em poucos dias."),
            ],
            [
                box("O que o PEXIVAS mudou, e o que não",
                    p("Ele não acabou com a plasmaférese: acabou com a "
                      "plasmaférese indiscriminada, e mostrou que ela não "
                      "reduz mortalidade. O ganho é renal, o custo é "
                      "infeccioso, e o cálculo é feito paciente a paciente."),
                    tipo="regra"),
                nota("Antes de avançar",
                    p("Pergunte quem indicaria, e peça o motivo antes do voto. "
                      "A divergência entre nefrologia e reumatologia na "
                      "hemorragia alveolar é real e recente — quem responder "
                      "“depende do serviço” está mais certo do que quem "
                      "responder sim ou não.")),
            ],
        ),
        densidade="dense",
        ident="plasmaferese_paciente",
    ),
    momento("Sexta parte",
        "A partir daqui, quem decide é você",
        "O caso deixa de correr em linha reta. A conduta escolhida e o tempo "
        "gasto levam este paciente por caminhos que não se reencontram. "
        "M abre o mapa, V volta ao nó anterior.",
        ident="p5_arvore"),
    N1,
    B_CEDO, N2A, B_RTX, N3A,
    B_CFX, N3B,
    B_ESPERA, N2B, B_RESGATE, N3C,
    B_SO_DIALISE, N3D,
    *[dict(f, segue="pontos_principais") for f in F],
    # Depois dos oito desfechos vem a síntese. O quinto dia, a deterioração e
    # a evolução deixaram de ser um bloco linear: cada um deles agora existe
    # dentro do ramo que o produziu, com números diferentes.
    bloco("Síntese", "Pontos principais",
        cols(
            [
                lista([
                     "A lista se levanta no nível em que o paciente se "
                     "apresenta. Hemoptise pede a pergunta de onde vem o "
                     "sangue, não a lista das vasculites: o diferencial de "
                     "síndrome pulmão-rim só existe depois de provadas as "
                     "duas síndromes.",
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
                     "Plasmaférese: a sobreposição anti-MBG é a única "
                     "situação em que a diretriz manda acrescentar. "
                     "Creatinina acima de 3,4 mg/dL e hemorragia alveolar com "
                     "hipoxemia mandam considerar — e é aí que as sociedades "
                     "divergem.",
                     "Toda piora durante a indução admite duas leituras "
                     "opostas. A neutropenia febril decide a favor da "
                     "infecção.",
                    ], ordenada=True),
            ],
        ),
        densidade="dense",
        ident="pontos_principais",
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
                     "Sulfametoxazol-trimetoprima para //Pneumocystis//: "
                     "400/80 mg/dia ou 800/160 mg em dias alternados, pelo "
                     "tempo do curso de ciclofosfamida, ou seis meses após "
                     "indução com rituximabe.",
                     "Plasmaférese: acrescentar na sobreposição anti-MBG; "
                     "considerar com creatinina acima de 3,4 mg/dL, diálise, "
                     "creatinina em ascensão rápida ou hemorragia alveolar com "
                     "hipoxemia.",
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

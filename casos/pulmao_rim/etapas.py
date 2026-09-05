"""O caso pulmão-rim em etapas.

Página a página, seis decisões, sem relógio. O título segue a regra da série
interativa do //New England//: nomeia o achado, nunca a doença.

Duas coisas governam a estrutura:

1. **O painel de exames tem teto.** Sem teto, marcar tudo é a jogada dominante,
   e quem marca tudo recebe o diagnóstico pronto na virada da folha sem ter
   decidido nada. Com teto, deixar um exame de fora custa — que é o custo real
   da beira do leito.

2. **O caso ramifica pelo que foi pedido, e não só pela conduta escolhida.**
   Quem não pediu a imunofluorescência do tecido e o anticorpo não recebe a
   página que os discute: recebe outra, sobre conduzir sem eles. É a única
   forma honesta de manter a promessa de que o que não foi pedido não aparece.

O paciente é ficcional. Os números foram desenhados para serem internamente
coerentes: gasometria que fecha por Henderson-Hasselbalch, filtração por
CKD-EPI 2021, e a relação PaO₂/FiO₂ calculada, não estimada.
"""

from pathlib import Path

from motor.desenhos import anotada, corpo, seta
from motor.etapas import (
    alt, bifurcacao, caminho, capa, desfecho, grade, grupo, lamina, numeros,
    op, p, pagina, pedido, pergunta, quadro, resultados, tabela, territorios,
)

from .banco import BANCO  # noqa: F401  — a gaveta de exames é a mesma

TITULO = ("Homem de 63 anos com hemoptise, púrpura e queda da "
          "função renal")
RODAPE = "Caso interativo · curso simulado"
IMG = Path(__file__).parent / "img"

CENA = "cena_admissao.jpg"
TC = "tc_torax_vidro_fosco.jpg"
RX = "rx_torax_alveolar.jpg"
US = "us_rim.jpg"
EAS = "sedimento_cilindro_hematico.jpg"
# a foto do córtex mostra o compartimento; a crescente tem foto própria,
# de grande aumento, e é nela que as setas apontam
BIOPSIA = "biopsia_renal_cortex.jpg"
CRESCENTE = "glomerulo_crescente.jpg"
IF = "panca_imunofluorescencia.jpg"


# ═════════════════ o que é comum aos três esquemas de indução ═══════════════

def _esquema_comum():
    """Tudo o que não muda com a escolha da segunda droga, em dois pares.

    Devolve dois blocos, não quatro: a página da prescrição é uma grade de
    três colunas — a droga escolhida numa, e os dois pares do que é comum nas
    outras duas. Quatro quadros empilhados passavam 400 px da tela.

    Estava faltando inteiro: o caso pulava da escolha para o desfecho sem
    dizer a dose do glicocorticoide, sem citar o PEXIVAS e sem mencionar o
    avacopan — e essas três coisas são metade do tratamento moderno desta
    doença.
    """
    glicocorticoide = quadro("O glicocorticoide, igual nos três caminhos",
            p("Metilprednisolona 500 mg por via endovenosa ao dia por três "
              "dias, seguida de prednisona 1 mg/kg/dia — aqui 60 mg, que é o "
              "teto — em desmame. O PEXIVAS (2020) comparou o desmame padrão "
              "com um **desmame reduzido**, que chega à metade da dose "
              "acumulada em seis meses: a eficácia foi não-inferior e as "
              "infecções graves em um ano caíram. É o desmame que este "
              "paciente recebe."),
            sistema="geral")
    plasma = quadro("Troca plasmática: o que mudou em 2020",
            p("O mesmo PEXIVAS randomizou troca plasmática em 704 pacientes "
              "com vasculite ANCA grave e **não** mostrou redução de morte ou "
              "de doença renal em estágio terminal, inclusive no subgrupo com "
              "hemorragia alveolar. As sociedades divergem no que sobrou: a "
              "KDIGO de 2021 ainda sugere considerá-la com creatinina muito "
              "alta ou necessidade de diálise, e a EULAR de 2022 a reserva "
              "para creatinina acima de 5,7 mg/dL ou anti-MBG associado. Este "
              "paciente, com 3,8 mg/dL, sem diálise e sem anti-MBG, **não** "
              "tem indicação de rotina."),
            sistema="sangue")
    avacopan = quadro("Avacopan, e por que ele não entra aqui",
            p("O ADVOCATE (2021) mostrou não-inferioridade na remissão em 26 "
              "semanas e **superioridade na remissão sustentada em 52**, com "
              "menos toxicidade de glicocorticoide. É adjuvante, não "
              "substituto da indução. O limite deste paciente não é a "
              "evidência: é a disponibilidade — a droga não está no SUS, e "
              "escrever no plano o que não se pode entregar é planejamento "
              "de mentira."),
            sistema="geral")
    cerco = quadro("Antes da primeira dose, e depois dela",
            p("Antes: sorologias de hepatite B e C e HIV, e a cultura que "
              "autoriza imunossuprimir. Depois: sulfametoxazol-trimetoprima "
              "**400/80 mg três vezes por semana** como profilaxia para "
              "//Pneumocystis// — a dose diária plena não cabe com filtração "
              "de 17 mL/min, e o trimetoprim sobe potássio e creatinina num "
              "paciente que chegou com 5,4 mEq/L. Cálcio e vitamina D pelo "
              "corticoide, e hemograma semanal."),
            sistema="pulmao")
    return glicocorticoide + plasma, avacopan + cerco


ETAPAS = [

    # ═══════════════════════════ abertura ═══════════════════════════

    capa(
        "Homem de 63 anos com hemoptise, púrpura e queda da função renal",
        "Oito semanas de doença, quatro territórios acometidos, e um paciente "
        "que já foi tratado duas vezes como outra coisa.",
        kicker="Caso interativo · 6 decisões · curso simulado",
        fundo=CENA,
        numeros_=numeros(
            ("3,8", "creatinina mg/dL", "rim"),
            ("88%", "SpO₂ em ar ambiente", "pulmao"),
            ("7,8", "hemoglobina g/dL", "sangue"),
        ),
        territorios_=territorios(
            ("via", "Via aérea superior", "Crostas no septo, epistaxe, anosmia"),
            ("pulmao", "Pulmão", "Hemoptise e crepitações difusas"),
            ("rim", "Rim", "Creatinina 3,8 — era 1,0 há dois meses"),
            ("pele", "Pele", "Lesões elevadas nas pernas e no dorso dos pés"),
            ("nervo", "Nervo periférico", "Pé caído à direita, déficit ulnar"),
            colunas=2,
        ),
        ressalva="**Procedência: autoral, curso simulado.** O paciente é "
                 "ficcional e nenhum ramo deste caso é o curso real de uma "
                 "pessoa: cada desfecho é inferência fisiológica, escrita para "
                 "ensino, e não extração de artigo. Os números foram "
                 "desenhados para fechar entre si. As cenas do paciente são "
                 "ilustrações geradas por inteligência artificial a partir da "
                 "descrição clínica. As imagens de radiologia, ultrassom, "
                 "microscopia de urina e anatomia patológica são reais, "
                 "ilustrativas, de repositórios de licença aberta, e não "
                 "pertencem a este paciente. Créditos ao pé de cada figura.",
    ),

    # ═══════════════════════ apresentação ═══════════════════════

    pagina("apresentacao", "Apresentação", "Como ele chegou",
        p("Um homem de 63 anos foi trazido pela esposa ao pronto-socorro por "
          "falta de ar que progrediu ao longo de três dias até aparecer em "
          "repouso, e por dois episódios de sangue vivo na expectoração, cerca "
          "de 50 mL cada, o segundo naquela manhã."),
        p("**Oito semanas antes** começou com secreção nasal purulenta "
          "persistente, crostas em ambas as narinas e sangramento nasal quase "
          "diário. Foi tratado duas vezes como rinossinusite bacteriana, "
          "primeiro com amoxicilina e depois com amoxicilina-clavulanato, sem "
          "melhora. Nesse período perdeu o olfato."),
        p("**Cinco semanas antes**, surgiram dores articulares que mudavam de "
          "lugar — punhos numa semana, tornozelos na outra — sem edema ou calor "
          "local. Passou a ter febre no fim da tarde, até 37,9 °C, sudorese "
          "noturna, e perdeu 6 kg sem mudar a alimentação."),
        p("**Duas semanas antes**, iniciou tosse seca que em poucos dias passou "
          "a ter raias de sangue. Procurou uma emergência, onde a radiografia "
          "de tórax foi lida como normal, e recebeu alta com antitussígeno."),
        p("**Na última semana**, a esposa notou que a urina dele estava escura, "
          "e que ele passou a levantar menos vezes à noite. Ele não deu "
          "importância e não procurou atendimento por isso."),
        fundo=CENA,
        lamina_=lamina(CENA, "Na admissão",
            "Sentado, dispneico, completando apenas frases curtas. Lesões "
            "arredondadas e elevadas na face anterior das pernas e no dorso "
            "dos pés.",
            "Ilustração gerada por inteligência artificial para este caso, a partir da descrição clínica. Paciente ficcional."),
    ),

    pagina("antecedentes", "Apresentação", "O que se sabia dele",
        p("Hipertenso há dez anos, em uso de losartana 50 mg por dia, "
          "acompanhado na unidade básica. Ex-tabagista de 30 anos-maço, parou "
          "há oito anos. Sem diabetes e sem doença renal conhecida."),
        p("Os exames de rotina de dois meses atrás, que a esposa trouxe "
          "impressos, mostravam **creatinina de 1,0 mg/dL, hemoglobina de "
          "13,9 g/dL e urina sem alterações**. Há dois meses, portanto, os "
          "rins funcionavam."),
        quadro("Perguntado nominalmente",
            p("Nega anti-inflamatório, chá, suplemento e fórmula de "
              "emagrecimento. Nega hidralazina, propiltiouracila e "
              "minociclina, e nega uso de cocaína em qualquer momento da vida. "
              "Mora em Quixadá, em casa de alvenaria com água encanada; não "
              "houve enchente na região, e nega contato com roedores."),
            sistema="geral"),
        fundo=CENA,
    ),

    pagina("exame", "Exame físico", "O que o exame mostrou",
        p("Temperatura de 37,8 °C, pressão arterial de 148/92 mmHg, frequência "
          "cardíaca de 104 batimentos por minuto, frequência respiratória de "
          "28 incursões por minuto. Saturação de 88% em ar ambiente, que subiu "
          "para 94% com cateter nasal a 4 L por minuto. Dispneico, preferindo "
          "permanecer sentado, completando apenas frases curtas, com palidez "
          "cutâneo-mucosa acentuada."),
        # Cinco territórios descritos em prosa obrigam quem lê a montar o mapa
        # de cabeça. Desenhados, o mapa já está montado — e a pergunta
        # seguinte, que é o que esses cinco compartilham, passa a ter uma
        # figura para apontar em sala.
        corpo([
            ("via", "Crostas hemáticas aderidas ao septo em ambas as narinas, "
                    "mucosa friável. Sem perfuração septal, deformidade em "
                    "sela ou massa."),
            ("pulmao", "Crepitações finas difusas nos dois hemitórax, sem "
                       "sibilos e sem atrito pleural. Ausculta cardíaca "
                       "normal, sem estase jugular e sem edema."),
            ("rim", "Sem massa palpável e sem dor à punho-percussão. No exame "
                    "físico o rim aparece só pela pressão de 148/92 mmHg."),
            ("pele", "Lesões purpúricas palpáveis na face anterior das pernas "
                     "e no dorso dos pés, algumas com centro escurecido, que "
                     "não desaparecem à digitopressão."),
            ("nervo", "Pé caído à direita, com força 2/5 para dorsiflexão, e "
                      "déficit sensitivo ulnar à esquerda. Assimétrico, sem "
                      "nível medular e sem raiz única."),
        ], altura=316),
        fundo=CENA,
        so_kicker=True,
    ),

    # ═══════════════════════ pergunta 1 ═══════════════════════

    pergunta("p1", "Pergunta 1 · enquadramento sindrômico",
        "Quatro territórios acometidos ao mesmo tempo — via aérea superior, "
        "pulmão, pele e nervo periférico — em oito semanas. Que estrutura "
        "anatômica é compartilhada por eles?",
        [
            alt("A drenagem linfática regional",
                "Pulmão e pele drenam para cadeias distintas, e o nervo "
                "periférico não compartilha nenhuma delas. Linfa não explica "
                "lesão simultânea nesses quatro sítios."),
            alt("O território de uma única artéria de médio calibre",
                "Vasos de médio calibre, quando acometidos, produzem aneurismas "
                "e infartos segmentares — território de outra família de "
                "doenças. Eles não são o leito onde a troca gasosa e a "
                "filtração acontecem, e por isso a lesão deles não aparece "
                "simultaneamente no alvéolo e no glomérulo."),
            alt("A mesma origem embriológica dos epitélios",
                "Os quatro territórios têm origens embriológicas diferentes. A "
                "coincidência aqui é de arquitetura vascular, não de "
                "desenvolvimento."),
            alt("Os vasos de pequeno calibre",
                "O capilar alveolar, o capilar glomerular, a vênula pós-capilar "
                "da derme e o vasa nervorum têm a mesma arquitetura básica: "
                "parede finíssima apoiada em membrana basal, submetida a "
                "pressão. Uma agressão dirigida a esse compartimento aparece "
                "nos quatro ao mesmo tempo.", certa=True),
            alt("A inervação autonômica compartilhada",
                "A inervação não explica lesão tecidual simultânea em quatro "
                "territórios, e não produz púrpura palpável nem hemoptise."),
        ],
        titulo_resposta="Quatro territórios, um só compartimento vascular",
        fundo=CENA,
    ),

    # A página anterior aqui era uma reflexão sobre "o compartimento e não o
    # órgão" que não dizia o que fazer com aquilo. Agora é uma tabela: qual é o
    # vaso de cada território, e o que se vê quando ele sangra.
    pagina("parede", "Discussão", "O mesmo vaso, quatro endereços",
        p("A resposta anterior tem uma consequência prática, e ela cabe numa "
          "frase: o que adoeceu não foi o pulmão, nem o rim, nem a pele — foi "
          "**o vaso que existe dentro dos três**."),
        tabela(["Território", "O vaso pequeno que ele tem",
                "O que aparece quando esse vaso sangra"], [
            ["Pulmão", "Capilar alveolar",
             "Sangue dentro do alvéolo: hemoptise, queda de hemoglobina, "
             "crepitação fina difusa"],
            ["Rim", "Capilar glomerular",
             "Sangue e cilindros na urina, creatinina subindo"],
            ["Pele", "Vênula pós-capilar da derme",
             "Púrpura elevada, que não desaparece à digitopressão"],
            ["Nervo periférico", "Vasa nervorum",
             "Um nervo de cada vez, assimétrico — o pé caído de um lado, a "
             "mão do outro"],
        ]),
        quadro("O que fazer com isso agora, à beira do leito",
            p("Procurar os territórios da mesma lista que ainda não foram "
              "examinados. Olho, intestino e sistema nervoso central têm o "
              "mesmo tipo de vaso e nenhum dos três foi avaliado neste "
              "paciente. Fígado e baço ficam de fora: sinusoide fenestrado "
              "não é capilar de barreira, e não é alvo do mesmo mecanismo."),
            sistema="geral"),
        fundo=CENA,
    ),

    # ═══════════════════════ pergunta 2 — o pedido ═══════════════════════

    # Este painel era o vazamento mais grave do caso: oferecia ANCA, anti-MBG,
    # C3 e FAN na primeira tela. Quem lê o painel lê a resposta — a lista de
    # exames pedidos é, ela própria, uma lista de hipóteses. A imunologia
    # dirigida foi para a segunda rodada, depois que as duas síndromes estão
    # provadas, que é quando ela de fato se pede.
    pedido("ex1", "Pergunta 2 · caracterizar as síndromes",
        "Que exames você pede agora?",
        "Seis vagas. Nada é obrigatório e nada é sugerido — mas o que não for "
        "pedido não volta, nem agora nem depois.",
        [
            grupo("Bancada, em minutos", "rim", [
                op("Sedimento urinário", "urina fresca, dismorfismo e cilindros"),
                op("Creatinina",
                   resultado="3,8 mg/dL {{(1,0 há dois meses)}}",
                   referencia="até 1,3 mg/dL", alterado=True),
                op("Taxa de filtração glomerular estimada",
                   "CKD-EPI 2021 — decide a dose de vários esquemas",
                   resultado="17 mL/min/1,73 m²",
                   referencia="acima de 90 mL/min/1,73 m²", alterado=True),
                op("Potássio", resultado="5,4 mEq/L",
                   referencia="3,5 a 5,0 mEq/L", alterado=True),
                op("Proteinúria de 24 horas"),
                op("Ultrassonografia de rins e vias urinárias"),
            ]),
            grupo("Sangue e gasometria", "sangue", [
                op("Hemoglobina", resultado="7,8 g/dL {{(13,9 há dois meses)}}",
                   referencia="13,5 a 17,5 g/dL", alterado=True),
                op("Leucócitos", resultado="14.200/mm³",
                   referencia="4.000 a 11.000/mm³", alterado=True),
                op("Plaquetas", resultado="468.000/mm³",
                   referencia="150.000 a 400.000/mm³", alterado=True),
                op("Reticulócitos"),
                op("pH arterial"),
                op("Relação PaO2/FiO2"),
                op("Proteína C reativa", resultado="186 mg/L",
                   referencia="até 5 mg/L", alterado=True),
                op("Esfregaço de sangue periférico"),
            ]),
            grupo("Imagem do tórax", "pulmao", [
                op("Radiografia de tórax"),
                op("Tomografia de tórax"),
                op("Ecocardiograma transtorácico"),
                op("Angiotomografia de tórax"),
            ]),
            grupo("Infecção", "geral", [
                op("Hemocultura",
                   "três pares, colhidos antes de qualquer antibiótico",
                   resultado="Em andamento na admissão · aos cinco dias: "
                             "**três pares negativos**",
                   referencia="negativa"),
                op("Urocultura"),
                op("Anti-HIV"),
                op("HBsAg e anti-HBc"),
            ]),
        ],
        fundo=TC, banco=BANCO, limite=6,
    ),

    resultados("res1", "O que voltou", "Os exames que você pediu", "ex1",
        introducao="Só o que foi marcado. O que não foi pedido não está aqui — "
                   "nem agora, nem depois.",
        fundo=TC,
        laminas={
            "Radiografia de tórax": lamina(RX, "Radiografia de tórax",
                "Opacidades alveolares bilaterais. Imagem ilustrativa: o "
                "padrão não distingue sangue de água ou de pus.",
                "Samir · Wikimedia Commons · CC BY-SA 3.0"),
            "Tomografia de tórax": lamina(TC, "Tomografia de tórax",
                "Montagem em janela de pulmão: três cortes axiais, um coronal "
                "e um sagital. Imagem ilustrativa. Janela de mediastino não "
                "incluída — linfonodo mediastinal não é avaliável aqui.",
                "Hellerhoff · Wikimedia Commons · CC BY-SA 4.0"),
            "Ultrassonografia de rins e vias urinárias": lamina(US,
                "Ultrassonografia renal",
                "Rim de tamanho e ecotextura normais. Imagem ilustrativa; os "
                "asteriscos são da fonte — * coluna de Bertin, ** pirâmide, "
                "*** córtex, **** seio renal.",
                "Hansen, Nielsen e Ewertsen · Wikimedia Commons · CC BY 4.0"),
            "Sedimento urinário": lamina(EAS, "Sedimento urinário",
                "Cilindro celular em urina fresca — a estrutura alongada é o "
                "molde do túbulo. Imagem ilustrativa.",
                "Rian Kabir · Wikimedia Commons · CC BY 2.0"),
        },
    ),

    # ═══════════════════════ pergunta 3 ═══════════════════════

    pergunta("p2", "Pergunta 3 · interpretação de um dado isolado",
        "Hemoptise de cerca de 50 mL em duas ocasiões, crepitações finas "
        "difusas, saturação de 88% e hemoglobina de 7,8 g/dL — que era 13,9 "
        "g/dL há dois meses. Que achado desse conjunto mais restringe a origem "
        "do sangramento?",
        [
            alt("O volume expectorado, que classifica a hemoptise como não maciça",
                "A classificação por volume decide a urgência da via aérea e a "
                "necessidade de embolização; não diz de onde o sangue vem. "
                "Hemoptise não maciça é compatível com todas as origens."),
            alt("As crepitações finas difusas nos dois hemitórax",
                "Crepitação fina difusa acompanha ocupação alveolar de qualquer "
                "natureza — sangue, água, pus ou fibrose. Localiza o processo "
                "no parênquima e não distingue o que o preenche."),
            alt("A saturação de 88% em ar ambiente",
                "Mede a gravidade da troca gasosa. Um alvéolo cheio de sangue e "
                "um alvéolo cheio de secreção purulenta produzem a mesma "
                "dessaturação."),
            alt("A ausência de febre alta e de expectoração purulenta",
                "Argumenta contra pneumonia bacteriana típica e não exclui "
                "infecção — ele tem 37,8 °C. Afastar uma causa não localiza a "
                "origem do sangramento."),
            alt("A queda de 6,1 g/dL na hemoglobina, desproporcional ao volume "
                "expectorado",
                "Ele expectorou cerca de 100 mL, que não derrubam a hemoglobina "
                "em 6 g/dL. O sangue que falta está retido em algum "
                "compartimento, e no pulmão o compartimento que retém sangue "
                "sem devolvê-lo pela boca é o alvéolo. É essa desproporção — e "
                "não a hemoptise — que desloca a origem do brônquio para o "
                "espaço aéreo distal.", certa=True),
        ],
        titulo_resposta="A hemoglobina que sumiu diz onde o sangue ficou",
        fundo=TC,
    ),

    pagina("duas_sindromes", "Discussão", "Duas síndromes, e só então um nome",
        p("Do lado do tórax, a desproporção entre o que foi expectorado e o que "
          "sumiu do hematócrito aponta para o alvéolo. Do lado do rim, "
          "creatinina que sai de 1,0 e chega a 3,8 em dois meses é lesão em "
          "curso, e o compartimento em que ela está ainda não foi determinado."),
        tabela(["A pergunta em aberto", "O exame que a decidiria"], [
            ["De onde vem o sangue do pulmão?",
             "Lavado broncoalveolar — o aspecto sequencial das alíquotas e a "
             "contagem de hemossiderófagos"],
            ["Em que compartimento do néfron está a lesão?",
             "Biópsia renal em microscopia óptica — proliferação dentro ou "
             "fora do tufo"],
            ["O mecanismo é imune, e de que tipo?",
             "Imunofluorescência do tecido renal — depósito linear, granular, "
             "ou ausência de depósito — e o anticorpo circulante"],
        ]),
        quadro("O que ainda não se pode dizer",
            p("A expressão síndrome pulmão-rim só significa alguma coisa depois "
              "de provadas as duas coisas que ela nomeia. Fazer o diferencial "
              "dela antes disso é responder a uma pergunta que ainda não foi "
              "feita."),
            sistema="geral"),
        fundo=BIOPSIA,
    ),

    # ═══════════════════════ pergunta 4 — segundo pedido ═══════════════════

    # Aqui saíram a biópsia pulmonar, a de nervo sural e a de pele: as três
    # devolviam "não realizada". Oferecer um exame que não devolve nada é pior
    # do que não oferecer — o grupo gasta uma das seis vagas para descobrir que
    # gastou uma vaga.
    pedido("ex2", "Pergunta 4 · provar o mecanismo",
        "E agora, o que você pede?",
        "As perguntas em aberto são a origem do sangramento alveolar, o "
        "compartimento da lesão renal e o mecanismo imune. Seis vagas de novo.",
        [
            grupo("Procedimento", "pulmao", [
                op("Lavado broncoalveolar", "aspecto das alíquotas e contagem"),
                op("Cultura do lavado broncoalveolar"),
            ]),
            grupo("Tecido renal", "rim", [
                op("Biópsia renal — microscopia óptica"),
                op("Biópsia renal — imunofluorescência",
                   "separa depósito linear, granular e ausência de depósito"),
                op("Biópsia renal — classificação de Berden"),
            ]),
            grupo("Imunologia dirigida", "via", [
                op("ANCA por imunofluorescência indireta",
                   "padrão e título, sobre neutrófilos fixados"),
                op("Anti-mieloperoxidase"),
                op("Anti-proteinase 3"),
                op("Anticorpo anti-membrana basal glomerular"),
                op("Complemento C3"),
                op("Crioglobulinas", "coleta em tubo aquecido"),
                op("FAN"),
                op("Anti-DNA nativo"),
            ]),
            grupo("Outros", "geral", [
                op("Complemento C4"),
                op("Tomografia de seios da face"),
                op("Eletroneuromiografia"),
            ]),
        ],
        fundo=BIOPSIA, banco=BANCO, limite=6,
    ),

    # A rota: o caso só segue para a página que discute o mecanismo se as duas
    # provas do mecanismo tiverem sido pedidas. Quem não as pediu vai para a
    # outra página, que é sobre conduzir sem elas — e é a página mais útil das
    # duas, porque é a situação mais comum no hospital de verdade.
    resultados("res2", "O que voltou", "A segunda rodada", "ex2",
        introducao="De novo, só o que foi marcado.",
        fundo=BIOPSIA,
        laminas={
            "ANCA por imunofluorescência indireta": lamina(IF,
                "Imunofluorescência indireta sobre neutrófilos",
                "Neutrófilos fixados em etanol. Imagem ilustrativa: a "
                "imunofluorescência indireta devolve padrão e título, nunca "
                "um valor em U/mL.",
                "Simon Caulton · Wikimedia Commons · CC BY-SA 3.0"),
        },
        rota={"pediu": ["Biópsia renal — imunofluorescência",
                        "Anti-mieloperoxidase"],
              "entao": "crescente", "senao": "sem_prova"},
    ),

    # ─────────────── rota A: as duas provas foram pedidas ───────────────

    pagina("crescente", "Discussão", "O que é uma crescente",
        grade(
        # O esquema autoral que estava aqui foi trocado por fotografia de
        # licença aberta com setas: o desenho ensina a forma idealizada, e a
        # forma idealizada é justamente a que não aparece na lâmina do
        # hospital. A seta resolve o que fazia o desenho necessário — dizer
        # qual das estruturas da foto é a que interessa.
        anotada(CRESCENTE, 1400, 933,
            # coordenadas lidas sobre a própria lâmina, com grade em milésimos
            # da largura: o tufo é a massa lobulada densa à direita, a cápsula
            # é a linha PAS-positiva contínua que delimita a estrutura à
            # esquerda, e a crescente é o tecido celular entre as duas
            seta((760, 235), (612, 72), "Tufo capilar", curva=16),
            seta((432, 292), (24, 152), "Cápsula de Bowman", curva=22),
            seta((505, 362), (24, 636),
                 "Crescente celular, no espaço de Bowman", curva=-30),
            titulo="Glomérulo com crescente celular · PAS, grande aumento",
            legenda="As setas são leitura editorial deste caso. A imagem é "
                    "ilustrativa, de repositório aberto, e não pertence ao "
                    "paciente.",
            credito="Nephron · Wikimedia Commons · CC BY-SA 3.0"),
        p("A biópsia foi feita, e a mesma agulha que serviu à "
          "imunofluorescência serviu à microscopia óptica: 24 glomérulos, "
          "**crescentes celulares em 15 deles**, com necrose fibrinoide "
          "segmentar. A figura ao lado é uma lâmina de outro paciente, no "
          "aumento em que a morfologia aparece.")
        + quadro("Por que a palavra celular importa",
            p("Crescente é proliferação de células **fora do tufo**, dentro do "
              "espaço de Bowman: epitélio parietal, monócitos e fibrina que "
              "escaparam por uma ruptura da parede capilar. Celular quer dizer "
              "que essas células ainda estão vivas e proliferando; fibrosa "
              "quer dizer que já viraram colágeno. A transição leva dias, não "
              "semanas, e é unidirecional — por isso a proporção de crescentes "
              "ainda celulares, 62% neste paciente, é o número que mais prediz "
              "o que vai sobrar de rim."),
            sistema="rim"),
        ),
        fundo=BIOPSIA,
    ),

    pergunta("p3", "Pergunta 5 · leitura de um achado de tecido",
        "A imunofluorescência da biópsia renal não mostra depósito imune "
        "significativo. Que valor esse achado tem?",
        [
            alt("É o padrão pauci-imune, e tem valor diagnóstico positivo",
                "A imunofluorescência separa três mecanismos: depósito linear "
                "ao longo da membrana basal é anticorpo contra o colágeno tipo "
                "IV; depósito granular é imunocomplexo; ausência de depósito é "
                "o padrão pauci-imune das vasculites associadas ao ANCA. "
                "Quando o laudo diz que não há depósitos significativos, ele "
                "está afirmando alguma coisa.", certa=True),
            alt("Nenhum: é um exame negativo, e o diagnóstico terá de vir de "
                "outro lugar",
                "É o erro mais comum diante deste laudo. A ausência de "
                "depósito, aqui, não é a falta de um achado — é o achado."),
            alt("Afasta glomerulonefrite e obriga a rever o sedimento",
                "A glomerulonefrite está estabelecida pelo sedimento e pela "
                "microscopia óptica, que mostra proliferação extracapilar. A "
                "imunofluorescência não gradua a lesão: ela separa mecanismos."),
            alt("Indica lúpus com nefrite de classe silenciosa",
                "A nefrite lúpica é doença por imunocomplexo, e a "
                "imunofluorescência dela é exuberante — o chamado full house, "
                "com IgG, IgA, IgM, C3 e C1q."),
            alt("Sugere doença anti-membrana basal glomerular em fase inicial",
                "A doença anti-MBG tem depósito linear e contínuo de IgG ao "
                "longo da membrana basal desde o começo. Ausência de depósito "
                "é o oposto do que ela produz."),
        ],
        titulo_resposta="Pauci-imune não é exame negativo",
        fundo=BIOPSIA,
    ),

    pagina("fenotipo", "Discussão", "Onde a lista para",
        p("Vasculite associada ao ANCA está estabelecida: tecido pauci-imune e "
          "anticorpo circulante. Qual delas é uma questão de fenótipo — e o "
          "fenótipo deste paciente tem uma peça ambígua."),
        tabela(["", "Poliangeíte microscópica", "Granulomatose com poliangeíte"], [
            ["Sorologia típica", "Anti-MPO, p-ANCA", "Anti-PR3, c-ANCA"],
            ["Via aérea superior", "Ausente ou leve",
             "Destrutiva: perfuração septal, deformidade em sela"],
            ["Granuloma", "Ausente",
             "Esperado na via aérea e no pulmão; quase nunca no rim"],
            ["Neste paciente", "Compatível",
             "Improvável — mas não pela biópsia renal: pesa o anti-MPO e a "
             "ausência de lesão destrutiva"],
        ]),
        quadro("A armadilha do tecido errado",
            p("A biópsia deste paciente é **renal**, e granuloma praticamente "
              "não aparece no rim — nem mesmo na granulomatose com "
              "poliangeíte. Na série de Bajema e cols. //(Kidney Int. "
              "1997;52:538-48)//, das 134 biópsias renais reunidas apenas sete "
              "mostravam granuloma renal, cerca de 5%, contra proliferação "
              "extracapilar na larga maioria. E nos critérios ACR/EULAR de "
              "2022 o item é granuloma **em qualquer tecido**, somando pontos "
              "quando presente e zero quando ausente: a ausência jamais "
              "subtrai."),
            sistema="rim"),
        fundo=IF, segue="b1",
    ),

    # ─────────────── rota B: faltou prova, e o caso segue assim ───────────

    pagina("sem_prova", "Discussão", "Conduzir sem a prova",
        p("As duas provas que separam esta doença das que se parecem com ela "
          "são o **mecanismo no tecido** — a imunofluorescência da biópsia "
          "renal, que distingue depósito linear, depósito granular e ausência "
          "de depósito — e o **anticorpo circulante**. Pelo menos uma delas "
          "não foi pedida, e por isso não está aqui."),
        p("Isso não interrompe o caso, porque não interromperia o paciente. "
          "Ele continua sangrando no alvéolo com creatinina de 3,8, e alguém "
          "vai ter de decidir se imunossuprime. O que muda é o que se pode "
          "afirmar em voz alta na passagem de plantão."),
        tabela(["O que continua de pé", "O que fica sem lastro"], [
            ["Hemorragia alveolar e lesão renal aguda coexistindo, com quatro "
             "territórios de vaso pequeno acometidos",
             "Que o mecanismo seja pauci-imune, e não imunocomplexo ou "
             "anti-membrana basal"],
            ["A urgência: crescente celular vira fibrosa em dias",
             "Que a doença seja associada ao ANCA — e, portanto, que o alvo "
             "terapêutico seja este"],
            ["Que infecção precisa estar afastada antes de imunossuprimir",
             "A escolha entre esquemas que dependem do fenótipo e do título "
             "do anticorpo"],
        ]),
        quadro("O custo real da vaga não gasta",
            p("A doença anti-membrana basal glomerular é o exemplo caro: ela "
              "faz exatamente esta síndrome, perde função renal em dias, e o "
              "tratamento dela **inclui troca plasmática**, que nesta não é de "
              "rotina. Ela se separa por um exame de sangue e por um padrão "
              "linear na imunofluorescência. Sem esses dois, tratar é apostar "
              "na doença mais provável — e a mais provável não é a única."),
            sistema="rim"),
        fundo=BIOPSIA,
    ),

    pergunta("p3b", "Pergunta 5 · o limite do que se pode afirmar",
        "Sem a imunofluorescência do tecido e sem o anticorpo circulante, o "
        "paciente segue com hemorragia alveolar e creatinina de 3,8 mg/dL. "
        "Qual é a conduta defensável?",
        [
            alt("Aguardar a estabilização clínica antes de qualquer decisão "
                "imunossupressora",
                "É a resposta que parece prudente e é a que perde o rim. "
                "Crescente celular vira crescente fibrosa em dias, e crescente "
                "fibrosa não responde a nada. Esperar aqui não é neutro: é "
                "escolher a alternativa irreversível."),
            alt("Colher agora as duas provas que faltam e iniciar o "
                "glicocorticoide sem esperar o resultado",
                "É o que se faz. O glicocorticoide não some com o padrão da "
                "imunofluorescência nem com o título do anticorpo — colhido o "
                "material, ele pode entrar. O que **não** pode entrar antes "
                "das culturas é a segunda droga, e é essa a ordem que a "
                "pressa costuma inverter.", certa=True),
            alt("Iniciar ciclofosfamida empiricamente, pela gravidade",
                "A gravidade justifica a pressa, não a escolha da segunda "
                "droga sem diagnóstico. E imunossuprimir de forma profunda com "
                "hemocultura ainda em andamento é a decisão que transforma "
                "endocardite em morte."),
            alt("Tratar como pneumonia grave e reavaliar em 48 horas",
                "É a leitura que já foi feita duas vezes com este paciente, e "
                "não respondeu nas duas. Sinusite e infiltrado que não cedem a "
                "antibiótico são dado, não fracasso de adesão."),
            alt("Indicar troca plasmática empírica, que cobre as duas "
                "possibilidades",
                "Cobre a hipótese anti-membrana basal e não muda o desfecho na "
                "vasculite ANCA — o PEXIVAS mostrou isso em 2020. Tratamento "
                "que cobre tudo é tratamento que não decidiu nada, e a troca "
                "plasmática tem custo próprio: cateter, coagulopatia, "
                "depleção de imunoglobulina."),
        ],
        titulo_resposta="Colher e começar o corticoide não são a mesma decisão "
                        "que imunossuprimir a fundo",
        fundo=BIOPSIA, segue="b1",
    ),

    # ═══════════════════════ pergunta 6 — a bifurcação ═══════════════════

    bifurcacao("b1", "Pergunta 6 · limite de uma terapia",
        "Com que esquema você induz a remissão?",
        "Filtração glomerular estimada de 17 mL/min/1,73 m² por CKD-EPI 2021, "
        "63 anos, hemorragia alveolar em curso. O glicocorticoide é comum aos "
        "três caminhos; a segunda droga é a decisão.",
        [
            caminho("Rituximabe 375 mg/m² por semana, quatro doses",
                    "t_rituximabe",
                    "Não exige ajuste para a função renal, poupa gônada e tem "
                    "eficácia equivalente à ciclofosfamida na indução. O RAVE "
                    "mostrou não-inferioridade e superioridade na doença "
                    "recidivante — mas **excluiu creatinina acima de 4,0 "
                    "mg/dL**, e este paciente está no limite dessa faixa. Para "
                    "filtração como a dele a referência é o RITUXVAS, menor, "
                    "com filtração média de 18 mL/min, que também não mostrou "
                    "diferença. A vantagem prática aqui é não depender de "
                    "acertar uma correção de dose."),
            caminho("Ciclofosfamida endovenosa com dose reduzida pela idade e "
                    "pela função renal", "t_cfx_ajustada",
                    "A redução vem do esquema do CYCLOPS, adotado pela EULAR: "
                    "**15 mg/kg menos 2,5 mg/kg por idade acima de 60 anos, e "
                    "menos 2,5 mg/kg por creatinina entre 300 e 500 µmol/L — "
                    "10 mg/kg, com teto de 1,2 g por pulso.** É a conta que "
                    "mais se esquece de fazer, e é toda a diferença entre este "
                    "caminho e o seguinte. Cobra hemograma semanal e mesna."),
            caminho("Ciclofosfamida endovenosa em dose plena, 15 mg/kg",
                    "t_cfx_plena",
                    "A dose plena com filtração de 17 mL/min produz exposição "
                    "muito acima da pretendida, porque o metabólito ativo é "
                    "eliminado por via renal. A neutropenia que vem depois não "
                    "é a esperada do esquema: é a da dose."),
        ],
        fundo=CENA,
    ),

    # ═══════════ o que foi prescrito, antes de saber como terminou ═══════════

    # Faltava esta camada inteira: a escolha caía direto no desfecho, e o caso
    # nunca dizia o que exatamente foi prescrito. A prescrição é o objeto de
    # ensino; o desfecho é só a consequência dela.

    pagina("t_rituximabe", "A prescrição", "O que foi prescrito — caminho A",
        grade(
            p("**Rituximabe 375 mg/m² por via endovenosa, uma vez por semana, "
              "quatro doses.** Superfície corporal de 1,86 m², portanto 697 mg por "
              "dose, arredondados para 700 mg. Sem correção para a função renal: o "
              "anticorpo monoclonal não é depurado pelo rim.")
            + quadro("O que este caminho pede de vigilância",
                p("Pré-medicação com anti-histamínico, paracetamol e o próprio "
                  "glicocorticoide, pela reação infusional da primeira dose. "
                  "Rastrear hepatite B antes — o anti-HBc isolado reativa sob "
                  "rituximabe, e a reativação é grave. Imunoglobulinas séricas na "
                  "linha de base, porque a hipogamaglobulinemia tardia é o efeito "
                  "que aparece nos ciclos seguintes, não neste."),
                sistema="sangue"),
            *_esquema_comum(), colunas=3,
        ),
        fundo=CENA, segue="d_rituximabe",
    ),

    pagina("t_cfx_ajustada", "A prescrição", "O que foi prescrito — caminho B",
        grade(
            p("**Ciclofosfamida endovenosa em pulso, 10 mg/kg.** A conta do "
              "CYCLOPS, escrita por extenso: parte de 15 mg/kg; subtrai 2,5 mg/kg "
              "por idade acima de 60 anos; subtrai mais 2,5 mg/kg por creatinina "
              "entre 300 e 500 µmol/L — os 3,8 mg/dL dele são 336 µmol/L. "
              "Restam **10 mg/kg**. Com 78 kg, 780 mg por pulso, abaixo do teto de "
              "1,2 g. Pulsos nas semanas 0, 2 e 4, depois a cada três semanas.")
            + quadro("O que este caminho pede de vigilância",
                p("Mesna e hidratação em cada pulso, pela cistite hemorrágica da "
                  "acroleína. Hemograma no sétimo e no décimo dia de cada pulso, "
                  "que é onde cai o nadir; se os neutrófilos ficarem abaixo de "
                  "1.000/mm³, o pulso seguinte desce mais um degrau. E a conversa "
                  "sobre fertilidade antes da primeira dose — que neste paciente, "
                  "de 63 anos, pesa menos, mas não se pula por isso."),
                sistema="sangue"),
            *_esquema_comum(), colunas=3,
        ),
        fundo=CENA, segue="d_cfx_ajustada",
    ),

    pagina("t_cfx_plena", "A prescrição", "O que foi prescrito — caminho C",
        grade(
            p("**Ciclofosfamida endovenosa em pulso, 15 mg/kg.** Com 78 kg, 1,17 g "
              "por pulso. A dose de bula para indução, sem as duas subtrações — "
              "nem a da idade acima de 60 anos, nem a da creatinina entre 300 e "
              "500 µmol/L.")
            + quadro("O que esta prescrição assume, sem dizer",
                p("Que a exposição depende só do peso. Ela depende também da "
                  "eliminação: os metabólitos ativos da ciclofosfamida saem por "
                  "via renal, e com filtração de 17 mL/min a área sob a curva de "
                  "1,17 g não é a de 1,17 g — é maior. A conta do CYCLOPS existe "
                  "porque essa diferença foi medida, e o que ela protege não é a "
                  "eficácia: é a medula."),
                sistema="rim"),
            *_esquema_comum(), colunas=3,
        ),
        fundo=CENA, segue="d_cfx_plena",
    ),

    # ═══════════════════════ desfechos ═══════════════════════

    desfecho("d_rituximabe", "Alta no vigésimo primeiro dia, sem diálise",
        p("A hemoptise cessou no terceiro dia e a saturação subiu para 94% em "
          "ar ambiente na primeira semana. A creatinina, que havia chegado a "
          "4,1 mg/dL, caiu de forma sustentada e estava em 1,9 mg/dL na alta, "
          "com diurese recuperada."),
        p("Completou as quatro doses semanais sem reação infusional além da "
          "primeira, e segue em manutenção programada com rituximabe, com "
          "consulta e exames já agendados."),
        qualidade="melhor", fecho="tres_caminhos",
        porque="O tratamento entrou enquanto a crescente ainda era celular. "
               "Crescente celular é tecido inflamado e responde; crescente "
               "fibrosa é cicatriz e não responde. Com filtração de "
               "17 mL/min/1,73 m², o rituximabe entrega a indução sem depender "
               "de uma correção de dose que, na prática, quase nunca é feita.",
        fundo=CENA),

    desfecho("d_cfx_ajustada", "Alta no vigésimo sexto dia, sem diálise",
        p("A indução funcionou: a hemoptise cessou no quarto dia e a creatinina "
          "estabilizou em 2,3 mg/dL. O hemograma foi vigiado semanalmente e o "
          "nadir de neutrófilos, no décimo dia, foi de 1.400/mm³ — dentro do "
          "esperado para a dose corrigida."),
        p("Recebeu a profilaxia prescrita e completou os três primeiros pulsos "
          "sem intercorrência infecciosa."),
        qualidade="melhor", fecho="tres_caminhos",
        porque="A ciclofosfamida com dose corrigida pela idade e pela filtração "
               "é tão eficaz quanto o rituximabe na indução. Custa mais "
               "vigilância — hemograma semanal, ajuste a cada ciclo, "
               "mesna — e cobra a conversa sobre fertilidade que o rituximabe "
               "dispensa. Neste paciente, de 63 anos, essa conversa pesa menos.",
        fundo=CENA),

    desfecho("d_cfx_plena", "Alta no trigésimo quarto dia, após a terapia intensiva",
        p("A vasculite respondeu: a hemoptise cessou no quarto dia e a "
          "creatinina caiu para 2,6 mg/dL. No décimo dia, no nadir esperado "
          "para o esquema, o hemograma mostrou 900 leucócitos com **210 "
          "neutrófilos**, e veio febre de 39,2 °C com calafrio e hipotensão "
          "que respondeu a volume."),
        p("Neutropenia febril muito mais profunda do que a esperada — o nadir "
          "de um pulso ajustado fica em torno de 1.400 neutrófilos. Foram "
          "treze dias de antibiótico de amplo espectro, fator estimulador de "
          "colônias e suporte em terapia intensiva antes de recuperar."),
        qualidade="pior", fecho="tres_caminhos",
        porque="Com filtração glomerular de 17 mL/min/1,73 m², a dose plena "
               "produziu exposição muito acima da pretendida — o metabólito "
               "ativo da ciclofosfamida é eliminado por via renal, e a conta do "
               "CYCLOPS teria pedido 10 mg/kg. A causa de morte precoce na "
               "vasculite associada ao ANCA tratada é a infecção, não a "
               "vasculite. Aqui ela veio da dose, e só da dose: foi a única "
               "coisa que esta decisão mudou.",
        fundo=CENA),

    # ═══════════════ o fecho, igual para os três ramos ═══════════════

    pagina("tres_caminhos", "Onde o caso se dividiu", "Os três caminhos",
        p("O caso ramificou em dois lugares. O primeiro foi silencioso: quem "
          "pediu a imunofluorescência do tecido e o anticorpo discutiu o "
          "mecanismo; quem não pediu discutiu como conduzir sem ele. O segundo "
          "foi a escolha da segunda droga, e é o que a tabela compara — "
          "inclusive os caminhos que você não seguiu."),
        tabela(["Caminho", "O que muda na prescrição", "O que muda no curso"], [
            ["A · Rituximabe 375 mg/m² semanal",
             "Sem correção para a filtração. Rastreio de hepatite B e "
             "imunoglobulinas antes",
             "Alta no 21º dia, creatinina 1,9 mg/dL, sem diálise"],
            ["B · Ciclofosfamida 10 mg/kg",
             "As duas subtrações do CYCLOPS — idade e creatinina — aplicadas. "
             "Mesna, hemograma no 7º e no 10º dia",
             "Alta no 26º dia, creatinina 2,3 mg/dL, nadir de 1.400 "
             "neutrófilos"],
            ["C · Ciclofosfamida 15 mg/kg",
             "A dose de bula, sem as subtrações",
             "Mesma resposta da vasculite, mas neutropenia febril de 210 "
             "neutrófilos e terapia intensiva"],
        ]),
        quadro("O que a comparação mostra",
            p("A vasculite respondeu nos três. A diferença entre eles não está "
              "na eficácia — está na exposição de um paciente com 17 mL/min de "
              "filtração a uma droga eliminada pelo rim. É por isso que a "
              "decisão da Pergunta 6 não era entre drogas: era entre fazer e "
              "não fazer uma conta."),
            sistema="geral"),
        fundo=CENA,
    ),

    pagina("lacuna", "O que fica sem explicação", "A lacuna",
        p("Um caso bem conduzido quase sempre deixa alguma coisa por explicar, "
          "e dizer isso em voz alta é parte do ensino. Três achados deste "
          "paciente continuam incômodos depois do diagnóstico fechado."),
        quadro("Os sintomas nasais",
            p("Crostas hemáticas, epistaxe diária e anosmia por oito semanas "
              "descrevem doença de via aérea superior, que é o território "
              "próprio da granulomatose com poliangeíte — e o anticorpo dele é "
              "anti-mieloperoxidase, não anti-proteinase 3. A poliangeíte "
              "microscópica pode acometer a via aérea superior de forma leve, "
              "e é a leitura que sustentamos; mas quem disser que este é um "
              "fenótipo sobreposto não está errado, e a literatura não fecha "
              "essa fronteira."),
            sistema="via"),
        quadro("A resposta medular",
            p("A queda de hemoglobina localiza o sangue no alvéolo, e isso a "
              "Pergunta 3 já estabeleceu. O que fica sem explicação é a "
              "resposta a ela: reticulócitos de 2,1% num hematócrito de 23,6% "
              "dão índice reticulocitário em torno de 1,0 — medula que não "
              "está repondo o que se perde. Doença inflamatória de oito "
              "semanas e deficiência de eritropoetina na lesão renal aguda "
              "explicam boa parte, e nenhuma das duas foi medida neste "
              "paciente. Fica como hipótese, não como fato."),
            sistema="sangue"),
        quadro("A artralgia migratória",
            p("Compatível com a doença e inespecífica: acompanha vasculite, "
              "infecção arrastada e doença do tecido conjuntivo com a mesma "
              "facilidade. Entra na história como ruído honesto, não como "
              "pista."),
            sistema="geral"),
        fundo=CENA,
        so_kicker=True,
    ),

    pagina("retrospectiva", "Onde dava para ter chegado antes",
        "A retrospectiva",
        p("O diagnóstico foi feito no hospital, com sorologia e biópsia. A "
          "pergunta útil é outra: em que momento, antes disso, a informação já "
          "estava disponível — e o que impediu que fosse usada."),
        tabela(["Quando", "O que estava à mão", "O que aconteceu"], [
            ["Oito semanas antes",
             "Rinossinusite que não respondeu a dois cursos de antibiótico, "
             "com crostas e epistaxe diária",
             "Mantida como infecção depois de dois cursos sem resposta. Sinusite "
             "que não cede a antibiótico é um dado, não um fracasso de adesão"],
            ["Duas semanas antes",
             "Radiografia de tórax de um paciente com hemoptise",
             "Lida como normal. A radiografia é pouco sensível para hemorragia "
             "alveolar precoce, e um laudo normal não encerra a investigação "
             "de quem escarra sangue"],
            ["Uma semana antes",
             "Urina escura, referida pela esposa",
             "Não foi perguntada nem examinada. Um sedimento naquele momento "
             "teria custado quase nada e mudado o rumo"],
            ["Dois meses antes",
             "Creatinina de 1,0 mg/dL em exame de rotina",
             "Guardada. Só virou informação quando alguém comparou — e é a "
             "comparação, não o valor, que faz o diagnóstico de lesão aguda"],
        ]),
        quadro("O viés que operou aqui",
            p("Fechamento precoce: a primeira explicação plausível foi mantida "
              "por oito semanas, e cada sintoma novo foi encaixado nela ou "
              "tratado como evento separado. O que quebra esse viés não é "
              "conhecimento raro — é a pergunta de por que a doença anterior "
              "não respondeu ao tratamento correto."),
            sistema="geral"),
        fundo=CENA,
        so_kicker=True,
    ),
]


# ═══════════════ o que a revisão cobra, quando não há mais o que decidir ══════

REVISAO = [
    dict(rotulo="Sedimento urinário", chave="Sedimento urinário",
         porque="É o exame mais barato do caso e o único que localiza a lesão "
                "renal em minutos. Hemácia dismórfica e cilindro hemático "
                "põem o sangramento dentro do glomérulo e derrubam a hipótese "
                "de duas doenças independentes."),
    dict(rotulo="Lavado broncoalveolar", chave="Lavado broncoalveolar",
         porque="Comprova a hemorragia alveolar pelas alíquotas "
                "progressivamente hemorrágicas e pelos hemossiderófagos acima "
                "de 20%, e diz que o sangramento tem pelo menos 48 horas."),
    dict(rotulo="Cultura do lavado broncoalveolar",
         chave="Cultura do lavado broncoalveolar",
         porque="É a cultura negativa que autoriza a imunossupressão. Tratar "
                "infecção difusa como vasculite, com pulso de corticoide e "
                "ciclofosfamida, tem consequência previsível."),
    dict(rotulo="ANCA por imunofluorescência indireta",
         chave="ANCA por imunofluorescência indireta",
         porque="Junto com o anti-MPO e o anti-PR3, é o que nomeia a doença. "
                "Leva dois dias, e é por isso que precisa ser pedido cedo."),
    dict(rotulo="Anticorpo anti-membrana basal glomerular",
         chave="Anticorpo anti-membrana basal glomerular",
         porque="É o exame de maior urgência do painel: na doença anti-MBG a "
                "demora de poucos dias custa a função renal de forma "
                "definitiva, e o tratamento inclui troca plasmática."),
    dict(rotulo="Complemento C3", chave="Complemento C3",
         porque="Separa em dois grupos as glomerulonefrites — as que consomem "
                "complemento e as que não consomem — por quase nada e em "
                "poucas horas."),
    dict(rotulo="Hemocultura", chave="Hemocultura",
         porque="Endocardite faz síndrome pulmão-rim e contraindica "
                "imunossupressão. E, uma vez iniciado o corticoide, cultura "
                "negativa deixa de valer."),
    dict(rotulo="Biópsia renal — imunofluorescência",
         chave="Biópsia renal — imunofluorescência",
         porque="É o único árbitro entre pauci-imune, depósito linear e "
                "depósito granular. Sem ela, vasculite ANCA e vasculite por "
                "IgA descrevem este paciente igualmente bem."),
]

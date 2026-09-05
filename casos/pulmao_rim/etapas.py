"""O caso pulmão-rim em etapas.

Página a página, seis perguntas, sem relógio. O título segue a regra da série
interativa do //New England//: nomeia o achado, nunca a doença.

A pergunta que carrega o caso é a de exames — grupos com marcação múltipla, e
só o que for marcado volta na página seguinte. O que não foi pedido não
aparece, e a revisão do fim é o único lugar em que o caso comenta o que faltou.

O paciente é ficcional. Os números foram desenhados para serem internamente
coerentes: gasometria que fecha por Henderson-Hasselbalch, filtração por
CKD-EPI 2021, e a relação PaO₂/FiO₂ calculada, não estimada.
"""

from pathlib import Path

from motor.desenhos import crescente_glomerular
from motor.etapas import (
    alt, bifurcacao, caminho, capa, desfecho, grupo, lamina, lista, numeros, op,
    p, pagina, pedido, pergunta, quadro, resultados, tabela, territorios,
)

from .banco import BANCO  # noqa: F401  — a gaveta de exames é a mesma

TITULO = ("Homem de 63 anos com hemoptise, púrpura e queda da "
          "função renal")
RODAPE = "Caso interativo · síndrome pulmão-rim"
IMG = Path(__file__).parent / "img"

CENA = "cena_admissao.jpg"
TC = "tc_torax_vidro_fosco.jpg"
# a foto mostra córtex renal; a crescente vive no esquema autoral,
# porque não é identificável com segurança neste plano
BIOPSIA = "biopsia_renal_cortex.jpg"
IF = "panca_imunofluorescencia.jpg"


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
            ("pele", "Pele", "Púrpura palpável nas pernas e nos pés"),
            ("nervo", "Nervo periférico", "Pé caído à direita, déficit ulnar"),
            colunas=2,
        ),
        ressalva="**Procedência: autoral, curso simulado.** O paciente é "
                 "ficcional e nenhum ramo deste caso é o curso real de uma "
                 "pessoa: cada desfecho é inferência fisiológica, escrita para "
                 "ensino, e não extração de artigo. Os números foram "
                 "desenhados para fechar entre si. As cenas do paciente são "
                 "ilustrações geradas por inteligência artificial a partir da "
                 "descrição clínica. As imagens de tomografia e de anatomia "
                 "patológica são reais, ilustrativas, de repositórios de "
                 "licença aberta, e não pertencem a este paciente. Créditos ao "
                 "pé de cada figura.",
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
        fundo=CENA,
        lamina_=lamina(CENA, "Na admissão",
            "Sentado, dispneico, completando apenas frases curtas. Púrpura "
            "palpável nas pernas e no dorso dos pés.",
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
          "para 94% com cateter nasal a 4 L por minuto."),
        p("Dispneico, preferindo permanecer sentado, completando apenas frases "
          "curtas, com palidez cutâneo-mucosa acentuada. À ausculta pulmonar, "
          "crepitações finas difusas nos dois hemitórax, sem sibilos e sem "
          "atrito pleural. A ausculta cardíaca era normal, sem sopros, e não "
          "havia estase jugular, terceira bulha ou edema de membros "
          "inferiores."),
        territorios(
            ("via", "Nariz", "Crostas hemáticas aderidas ao septo em ambas as "
             "narinas, mucosa friável. Sem perfuração septal, deformidade em "
             "sela ou massa."),
            ("pele", "Pernas e pés", "Lesões purpúricas palpáveis na face "
             "anterior das pernas e no dorso dos pés, algumas com centro "
             "escurecido, que não desaparecem à digitopressão."),
            ("nervo", "Neurológico", "Pé caído à direita, com força 2/5 para "
             "dorsiflexão, e déficit sensitivo ulnar à esquerda. Assimétrico, "
             "sem nível medular e sem raiz única."),
        ),
        fundo=CENA,
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
                "Vasculites de médio calibre, como a poliarterite nodosa, "
                "produzem aneurismas e infartos segmentares. Elas não causam "
                "capilarite alveolar nem glomerulonefrite."),
            alt("Os vasos de pequeno calibre",
                "O capilar alveolar, o capilar glomerular, a vênula pós-capilar "
                "da derme e o vasa nervorum têm a mesma arquitetura básica: "
                "parede finíssima apoiada em membrana basal, submetida a "
                "pressão. Uma agressão dirigida a esse compartimento aparece "
                "nos quatro ao mesmo tempo.", certa=True),
            alt("A mesma origem embriológica dos epitélios",
                "Os quatro territórios têm origens embriológicas diferentes. A "
                "coincidência aqui é de arquitetura vascular, não de "
                "desenvolvimento."),
            alt("A inervação autonômica compartilhada",
                "A inervação não explica lesão tecidual simultânea em quatro "
                "territórios, e não produz púrpura palpável nem hemoptise."),
        ],
        titulo_resposta="Quatro territórios, um só compartimento vascular",
        fundo=CENA,
    ),

    pagina("parede", "Discussão", "A parede compartilhada",
        p("O capilar glomerular e o capilar alveolar têm a mesma arquitetura: "
          "endotélio finíssimo apoiado em membrana basal, submetido a pressão, "
          "e responsável por filtrar de um lado e trocar gás do outro."),
        p("Uma agressão dirigida a esse compartimento aparece nos dois órgãos "
          "ao mesmo tempo — e também na pele e no vasa nervorum, que são feitos "
          "do mesmo material. É por isso que os quatro territórios do exame "
          "físico e o rim caem juntos."),
        quadro("Onde isso não vale",
            p("Fígado e baço não entram nessa lista, e a razão é a arquitetura "
              "do leito: sinusoide fenestrado não se comporta como capilar de "
              "barreira, e por isso não é alvo do mesmo mecanismo."),
            sistema="sangue"),
        fundo=CENA,
    ),

    # ═══════════════════════ pergunta 2 — o pedido ═══════════════════════

    pedido("ex1", "Pergunta 2 · próximo exame, com hipótese", "Que exames você pede agora?",
        "Marque o que quiser. Na página seguinte volta o que você pediu — e só "
        "isso. Nada é obrigatório e nada é sugerido.",
        [
            grupo("Bancada, minutos", "rim", [
                op("Sedimento urinário", "urina fresca, dismorfismo e cilindros"),
                op("Proteinúria de 24 horas"),
                op("Creatinina"),
                op("Potássio"),
                op("Ultrassonografia de rins e vias urinárias"),
            ]),
            grupo("Sangue e gasometria", "sangue", [
                op("Hemograma"),
                op("Gasometria arterial"),
                op("Proteína C reativa"),
                op("Desidrogenase láctica"),
                op("Esfregaço de sangue periférico"),
            ]),
            grupo("Imagem do tórax", "pulmao", [
                op("Radiografia de tórax"),
                op("Tomografia de tórax"),
                op("Ecocardiograma transtorácico"),
                op("Angiotomografia de artérias pulmonares"),
            ]),
            grupo("Imunologia e microbiologia", "via", [
                op("ANCA por imunofluorescência indireta", "leva dois dias"),
                op("Anticorpo anti-membrana basal glomerular"),
                op("Complemento C3"),
                op("FAN"),
                op("Hemocultura", "três pares, colhidos antes de qualquer antibiótico",
                   resultado="Em andamento na admissão. Aos cinco dias: "
                             "**três pares negativos**",
                   referencia="negativa"),
            ]),
        ],
        fundo=TC,
    ),

    resultados("res1", "O que voltou", "Os exames que você pediu", "ex1",
        introducao="Só o que foi marcado. O que não foi pedido não está aqui — "
                   "nem agora, nem depois.",
        fundo=TC,
        laminas={
            "Tomografia de tórax": lamina(TC, "Tomografia de tórax",
                "Montagem em janela de pulmão: três cortes axiais, um coronal "
                "e um sagital. Imagem ilustrativa. Janela de mediastino não "
                "incluída — linfonodo mediastinal não é avaliável aqui.",
                "Hellerhoff · Wikimedia Commons · CC BY-SA 4.0"),
            # a imunofluorescência indireta produz PADRÃO e título, não um
            # número em U/mL: ela pertence a este exame, não ao anti-MPO
            "ANCA por imunofluorescência indireta": lamina(IF,
                "Imunofluorescência indireta sobre neutrófilos",
                "Neutrófilos fixados em etanol. Imagem ilustrativa.",
                "Simon Caulton · Wikimedia Commons · CC BY-SA 3.0"),
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
            alt("A queda de 6,1 g/dL na hemoglobina, desproporcional ao volume "
                "expectorado",
                "Ele expectorou cerca de 100 mL, que não derrubam a hemoglobina "
                "em 6 g/dL. O sangue que falta está retido em algum "
                "compartimento, e no pulmão o compartimento que retém sangue "
                "sem devolvê-lo pela boca é o alvéolo. É essa desproporção — e "
                "não a hemoptise — que desloca a origem do brônquio para o "
                "espaço aéreo distal.", certa=True),
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
        ],
        titulo_resposta="A hemoglobina que sumiu diz onde o sangue ficou",
        fundo=TC,
    ),

    pagina("duas_sindromes", "Discussão", "Duas síndromes, e só então um nome",
        p("Do lado do tórax, a desproporção entre o que foi expectorado e o que "
          "sumiu do hematócrito aponta para o alvéolo. Do lado do rim, "
          "creatinina que sai de 1,0 e chega a 3,8 em dois meses é lesão em "
          "curso, e o compartimento em que ela está ainda não foi determinado."),
        tabela(["A pergunta", "O que a responde"], [
            ["De onde vem o sangue do pulmão?",
             "Lavado broncoalveolar: alíquotas progressivamente hemorrágicas, "
             "hemossiderófagos acima de 20% dos macrófagos"],
            ["Em que compartimento está a lesão renal?",
             "Sedimento urinário em urina fresca: hemácia dismórfica e cilindro "
             "hemático põem a lesão dentro do glomérulo"],
            ["Existe um mecanismo único?",
             "A simultaneidade em quatro territórios, e a ausência de outra "
             "explicação que os una"],
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

    pedido("ex2", "Pergunta 4 · próximo exame, com hipótese", "E agora, o que você pede?",
        "As duas perguntas em aberto são a origem do sangramento alveolar e o "
        "compartimento da lesão renal. Marque o que for testá-las.",
        [
            grupo("Procedimento", "pulmao", [
                op("Lavado broncoalveolar", "aspecto das alíquotas e contagem"),
                op("Cultura do lavado broncoalveolar"),
                op("Biópsia pulmonar"),
                op("Biópsia de nervo sural"),
            ]),
            grupo("Tecido renal", "rim", [
                op("Biópsia renal — microscopia óptica"),
                op("Biópsia renal — imunofluorescência"),
                op("Biópsia renal — classificação de Berden"),
            ]),
            grupo("Sorologia dirigida", "via", [
                op("Anti-mieloperoxidase"),
                op("Anti-proteinase 3"),
                op("Crioglobulinas", "coleta em tubo aquecido"),
                op("Anti-DNA nativo"),
            ]),
            grupo("Outros", "geral", [
                op("Complemento C4"),
                op("Anti-HIV"),
                op("HBsAg"),
                op("Tomografia de seios da face"),
            ]),
        ],
        fundo=BIOPSIA,
    ),

    resultados("res2", "O que voltou", "A segunda rodada", "ex2",
        introducao="De novo, só o que foi marcado.",
        fundo=BIOPSIA,
        # Nenhuma lâmina aqui. A fotomicrografia disponível mostra o córtex —
        # glomérulos, túbulos, interstício — e não a crescente que o laudo
        # conta. Pendurá-la no cartão do resultado ensinaria a ler no tecido um
        # achado que não está no plano. Ela ilustra a página seguinte, que é de
        # discussão do compartimento, e a morfologia da crescente vem em
        # esquema autoral.
    ),

    pagina("crescente", "Discussão", "O que é uma crescente",
        p("A fotomicrografia da página anterior mostra o compartimento — "
          "córtex, glomérulos, túbulos, interstício. A morfologia que o laudo "
          "descreve não é identificável com segurança naquele plano, e por "
          "isso ela vem aqui, em esquema."),
        crescente_glomerular(altura=286),
        p("Crescente é proliferação de células no **espaço de Bowman**, fora "
          "do tufo: células epiteliais parietais, monócitos e fibrina que "
          "escaparam por uma ruptura da parede capilar. Ela comprime o tufo "
          "para um lado e obstrui a saída do filtrado."),
        quadro("Por que a palavra celular importa",
            p("Crescente **celular** é tecido inflamado, e tecido inflamado "
              "responde a imunossupressão. Crescente **fibrosa** é cicatriz, e "
              "cicatriz não responde a tratamento nenhum. A transição de uma "
              "para a outra leva dias — e é a única razão pela qual a demora, "
              "neste caso, custa função renal em vez de custar apenas tempo."),
            sistema="rim"),
        fundo=BIOPSIA,
        lamina_=lamina(BIOPSIA, "Biópsia renal, microscopia óptica",
            "Córtex renal em coloração de PAS: glomérulos, túbulos e "
            "interstício. Imagem ilustrativa, de repositório aberto; não "
            "pertence a este paciente e não demonstra a crescente descrita no "
            "laudo — para essa morfologia, o esquema ao lado.",
            "Nephron · Wikimedia Commons · CC BY-SA 3.0"),
    ),

    # ═══════════════════════ pergunta 5 ═══════════════════════

    pergunta("p3", "Pergunta 5 · leitura de um achado de tecido",
        "A imunofluorescência da biópsia renal não mostra depósito imune "
        "significativo. Que valor esse achado tem?",
        [
            alt("Nenhum: é um exame negativo, e o diagnóstico terá de vir de "
                "outro lugar",
                "É o erro mais comum diante deste laudo. A ausência de "
                "depósito, aqui, não é a falta de um achado — é o achado."),
            alt("Afasta glomerulonefrite e obriga a rever o sedimento",
                "A glomerulonefrite está estabelecida pelo sedimento e pela "
                "microscopia óptica, que mostra proliferação extracapilar. A "
                "imunofluorescência não gradua a lesão: ela separa mecanismos."),
            alt("É o padrão pauci-imune, e tem valor diagnóstico positivo",
                "A imunofluorescência separa três mecanismos: depósito linear "
                "ao longo da membrana basal é anticorpo contra o colágeno tipo "
                "IV; depósito granular é imunocomplexo; ausência de depósito é "
                "o padrão pauci-imune das vasculites associadas ao ANCA. "
                "Quando o laudo diz que não há depósitos significativos, ele "
                "está afirmando alguma coisa.", certa=True),
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
        p("Vasculite associada ao ANCA está estabelecida. Qual delas é uma "
          "questão de fenótipo — e o fenótipo deste paciente tem uma peça "
          "ambígua."),
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
              "poliangeíte. Na meta-análise de Bajema e cols., de 1997, das "
              "134 biópsias renais reunidas apenas sete mostravam granuloma "
              "renal, cerca de 5%, contra 70% de proliferação extracapilar. E "
              "nos critérios ACR/EULAR de 2022 o item é granuloma em qualquer "
              "tecido, somando dois pontos quando presente e zero quando "
              "ausente: a ausência jamais subtrai."),
            sistema="rim"),
        fundo=IF,
    ),

    # ═══════════════════════ pergunta 6 — a bifurcação ═══════════════════

    bifurcacao("b1", "Pergunta 6 · limite de uma terapia", "Com que esquema você induz a remissão?",
        "Filtração glomerular estimada de 17 mL/min/1,73 m² por CKD-EPI 2021, "
        "63 anos, hemorragia alveolar em curso. O glicocorticoide é comum aos "
        "três caminhos; a segunda droga é a decisão.",
        [
            caminho("Rituximabe 375 mg/m² por semana, quatro doses",
                    "d_rituximabe",
                    "Não exige ajuste para a função renal, poupa gônada e tem "
                    "eficácia equivalente à ciclofosfamida na indução — o "
                    "RAVE mostrou não-inferioridade, e superioridade na doença "
                    "recidivante. Com filtração de 17 mL/min e 63 anos, é o "
                    "esquema que não depende de acertar uma correção de dose."),
            caminho("Ciclofosfamida endovenosa com dose reduzida pela idade e "
                    "pela função renal", "d_cfx_ajustada",
                    "É a escolha correta quando se opta pela ciclofosfamida: a "
                    "bula pede redução acima de 60 anos e abaixo de "
                    "30 mL/min/1,73 m², e essa redução é justamente a que mais "
                    "se esquece de fazer. Funciona, e cobra vigilância "
                    "hematológica semanal."),
            caminho("Ciclofosfamida endovenosa em dose plena, 15 mg/kg",
                    "d_cfx_plena",
                    "A dose plena com filtração de 17 mL/min produz exposição "
                    "muito acima da pretendida, porque o metabólito ativo é "
                    "eliminado por via renal. A neutropenia que vem no quinto "
                    "dia não é a esperada do esquema: é a da dose."),
        ],
        fundo=CENA,
    ),

    # ═══════════════════════ desfechos ═══════════════════════

    desfecho("d_rituximabe", "Alta no vigésimo primeiro dia, sem diálise",
        p("A hemoptise cessou no terceiro dia e a saturação subiu para 94% em "
          "ar ambiente na primeira semana. A creatinina, que havia chegado a "
          "4,1 mg/dL, caiu de forma sustentada e estava em 1,9 mg/dL na alta, "
          "com diurese recuperada."),
        p("Recebeu sulfametoxazol-trimetoprima 400/80 mg por dia como "
          "profilaxia para //Pneumocystis//, e segue em manutenção programada "
          "com rituximabe, com consulta e exames já agendados."),
        qualidade="melhor", fecho="lacuna",
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
        p("Recebeu profilaxia para //Pneumocystis// e completou o curso de "
          "indução sem intercorrência infecciosa."),
        qualidade="medio", fecho="lacuna",
        porque="A ciclofosfamida com dose corrigida pela idade e pela filtração "
               "é tão eficaz quanto o rituximabe na indução. Custa mais "
               "vigilância — hemograma semanal, ajuste a cada ciclo, "
               "mesna — e cobra a conversa sobre fertilidade que o rituximabe "
               "dispensa. Neste paciente, de 63 anos, essa conversa pesa menos.",
        fundo=CENA),

    desfecho("d_cfx_plena", "Alta no trigésimo quarto dia, após a terapia intensiva",
        p("A vasculite respondeu: a hemoptise cessou no quarto dia e a "
          "creatinina caiu para 2,6 mg/dL. No quinto dia, porém, o hemograma "
          "mostrou 900 leucócitos com 210 neutrófilos, e veio febre de 39,2 °C "
          "com calafrio e hipotensão que respondeu a volume."),
        p("Neutropenia febril, mais precoce e mais grave do que o esperado para "
          "o esquema. Foram treze dias de antibiótico de amplo espectro, fator "
          "estimulador de colônias e suporte em terapia intensiva antes de "
          "recuperar."),
        qualidade="pior", fecho="lacuna",
        porque="Com filtração glomerular de 17 mL/min/1,73 m², a dose plena "
               "produziu exposição muito acima da pretendida — o metabólito "
               "ativo da ciclofosfamida é eliminado por via renal. A causa de "
               "morte precoce na vasculite ANCA tratada é a infecção, não a "
               "vasculite, e ela vem da dose, da profilaxia que não foi "
               "prescrita e da imunossupressão mantida enquanto a febre corria.",
        fundo=CENA),

    # ═══════════════ o fecho, igual para os três ramos ═══════════════

    pagina("lacuna", "Fecho · o que fica sem explicação",
        "A lacuna",
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
        quadro("A anemia",
            p("Hemoglobina de 13,9 para 7,8 g/dL em dois meses é mais queda do "
              "que a hemorragia alveolar sozinha costuma produzir. Doença "
              "inflamatória de oito semanas explica parte, e a hemodiluição "
              "explica outra parte — mas a soma continua não fechando com "
              "conforto, e não há hemólise nem sangramento digestivo neste "
              "paciente."),
            sistema="sangue"),
        quadro("A artralgia migratória",
            p("Compatível com a doença e inespecífica: acompanha vasculite, "
              "infecção arrastada e doença do tecido conjuntivo com a mesma "
              "facilidade. Entra na história como ruído honesto, não como "
              "pista."),
            sistema="geral"),
        fundo=CENA,
    ),

    pagina("retrospectiva", "Fecho · onde dava para ter chegado antes",
        "A retrospectiva",
        p("O diagnóstico foi feito no hospital, com sorologia e biópsia. A "
          "pergunta útil é outra: em que momento, antes disso, a informação já "
          "estava disponível — e o que impediu que fosse usada."),
        tabela(["Quando", "O que estava à mão", "O que aconteceu"], [
            ["Oito semanas antes",
             "Rinossinusite que não respondeu a dois cursos de antibiótico, "
             "com crostas e epistaxe diária",
             "Tratada uma terceira vez como infecção. Sinusite que não cede a "
             "antibiótico é um dado, não um fracasso de adesão"],
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
                "definitiva, e o tratamento é diferente."),
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

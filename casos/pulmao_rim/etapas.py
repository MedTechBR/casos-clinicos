"""O caso pulmão-rim em etapas, na gramática do //New England//.

A unidade do caso é o par **alíquota → pergunta**: uma página curta com um
dado novo do paciente, e em seguida uma pergunta que aquele dado autoriza. A
pergunta raramente é "o que você pede agora": ela é o diferencial que o
sintoma abre, a interpretação de um resultado, o mecanismo de um achado, a
associação entre padrões, e a conduta só quando é hora de decidir.

Os dados que estreitam o diagnóstico chegam em alíquotas: a apresentação traz
sintomas nasais e constitucionais inespecíficos; a urina e a creatinina vêm no
ambulatório; a hemoptise, depois; a púrpura e a mononeuropatia só são
reconhecidas no reexame do segundo dia. O nome da doença aparece pela
primeira vez no diferencial da síndrome pulmão-rim, e o diagnóstico se fecha
na biópsia e no anticorpo.

Três decisões de estrutura permanecem: o caso tem uma **virada** (a leitura
de infecção, e a piora sob antibiótico adequado), o paciente **reaparece**
entre um exame e o outro, e a **segunda virada é no tratamento**: a febre
do quinto dia de indução.

O paciente é ficcional. Os números fecham entre si: gasometria por
Henderson-Hasselbalch, filtração por CKD-EPI 2021, hiato aniônico corrigido
pela albumina, índice reticulocitário pelo hematócrito.
"""

from pathlib import Path

from motor.desenhos import anotada, corpo, seta, chave_corpusculo
from motor.estudo_imagem import ecg, estudo
from motor.etapas import (
    alt, balanco, bifurcacao, caminho, capa, consequencia, desfecho, grade,
    grupo, lamina, op, p, pagina, painel, par, pareamento, pedido, pergunta,
    quadro, resultados, tabela, topicos, vitais,
)

from .banco import BANCO  # noqa: F401  (a gaveta de exames é a mesma)

TITULO = "O sangue que não saiu"
RODAPE = "Caso interativo · curso simulado"
COR = '#e11d48'
IMG = Path(__file__).parent / "img"

CENA = "cena_admissao.jpg"
TC = "tc_torax_vidro_fosco.jpg"
RX = "rx_torax_alveolar.jpg"
US = "us_rim.jpg"
EAS = "sedimento_cilindro.jpg"
RX_NORMAL = "rx_torax_normal.jpg"
TC_SEIOS = "tc_seios_face.jpg"
ECO = "eco_4camaras.jpg"
ESFREGACO = "esfregaco_sangue.jpg"
BIOPSIA = "biopsia_renal_cortex.jpg"
CRESCENTE = "glomerulo_crescente.jpg"
IF = "panca_imunofluorescencia.jpg"


def Q(n):
    return f"Pergunta {n}"


# ═════════════════ o que é comum aos três esquemas de indução ═══════════════

def _esquema_comum():
    glicocorticoide = quadro("O glicocorticoide, igual nos três caminhos",
        p("Metilprednisolona 500 mg/dia por três dias, depois prednisona, "
          "**75 mg/dia** pela faixa de peso acima de 75 kg. No PEXIVAS (2020), "
          "o **desmame reduzido**, com pouco mais da metade da dose acumulada "
          "em seis meses, não foi inferior e reduziu as infecções graves no "
          "primeiro ano."),
        sistema="geral")
    plasma = quadro("Troca plasmática: uma decisão em disputa",
        p("O PEXIVAS não mostrou redução de morte ou de doença renal terminal "
          "em 704 pacientes. A EULAR de 2022 diz que ela **pode ser "
          "considerada** com creatinina acima de 300 µmol/L (ele está em "
          "**407**), e a KDIGO 2024 inclui a hemorragia alveolar com "
          "hipoxemia. Aqui ela é discutível, e não está descartada."),
        sistema="sangue")
    avacopan = quadro("Avacopan, e por que ele não entra aqui",
        p("O ADVOCATE (2021) mostrou **superioridade na remissão sustentada em "
          "52 semanas**, poupando glicocorticoide. É adjuvante da indução, não "
          "substituto, e o limite aqui é a disponibilidade."),
        sistema="geral")
    cerco = quadro("Antes da primeira dose, e depois dela",
        p("Antes: sorologias de hepatite B e C e HIV. Depois: "
          "sulfametoxazol-trimetoprima **400/80 mg três vezes por semana**, "
          "metade da dose habitual. A bula desaconselha abaixo de 15 mL/min, "
          "mas a meia dose é a prática aceita, com potássio vigiado: ele "
          "chegou com 5,4. Cálcio, vitamina D e hemograma semanal."),
        sistema="pulmao")
    return glicocorticoide + plasma, avacopan + cerco


ETAPAS = [

    # ═══════════════════════════ capa ═══════════════════════════

    capa(TITULO, fundo=CENA,
         kicker="Caso interativo · 8 perguntas · 3 decisões",
         selo="Paciente ficcional · procedência e créditos na última tela"),

    # ══════════════ ATO I — as oito semanas que ninguém fechou ══════════════

    pagina("abertura", "Oito semanas antes", "O primeiro atendimento",
        p("Um homem de 63 anos estava em seu estado habitual de saúde até oito "
          "semanas antes desta admissão, quando surgiram obstrução nasal e "
          "secreção nasal espessa, que não passavam."),
        p("Foi atendido na unidade básica e tratado como rinossinusite "
          "bacteriana com amoxicilina por dez dias. Não melhorou. Voltou "
          "quatro semanas depois e recebeu amoxicilina-clavulanato por catorze "
          "dias, com adesão confirmada pela esposa. Também não melhorou."),
        fundo=CENA,
    ),


    pagina("evolucao_a", "Cinco semanas antes", "Os sintomas que se somaram",
        p("Três semanas depois do início dos sintomas nasais, surgiram dores "
          "articulares que mudavam de lugar, punhos numa semana e tornozelos "
          "na outra, sem edema, calor ou rigidez matinal prolongada."),
        p("Passou a ter febre no fim da tarde, medida em casa até 37,9 °C, com "
          "sudorese noturna. Perdeu 6 kg em cinco semanas sem mudar a "
          "alimentação. A esposa insistiu para que voltasse ao médico, e ele "
          "foi encaminhado ao ambulatório de clínica médica."),
        fundo=CENA,
    ),


    pagina("anamnese", "No ambulatório", "O que se sabia dele",
        p("Hipertenso há dez anos, em uso de losartana 50 mg por dia. "
          "Ex-tabagista de 30 anos-maço, parou há oito anos. Sem diabetes e "
          "sem doença renal conhecida. Trabalhou como pedreiro dos 18 aos 58 "
          "anos e hoje cuida de uma pequena horta."),
        p("Trouxe impressos os exames de rotina de dois meses antes, pedidos "
          "na unidade básica: **creatinina 1,0 mg/dL**, hemoglobina 13,9 g/dL "
          "e urina sem alterações."),
        quadro("Hábitos e exposições",
            p("Nega anti-inflamatório, chá, suplemento e fórmula de "
              "emagrecimento. Nega drogas ilícitas. Mora em Quixadá, em casa de "
              "alvenaria com água encanada. Sem viagem recente, sem animais em "
              "casa e sem contato com pessoa com tosse crônica."),
            sistema="geral"),
        fundo=CENA,
    ),


    pagina("retorno_ambulatorial", "Consulta ambulatorial", "Reavaliação",
        p("A esposa acrescenta que ele abandonou a horta há duas semanas. "
          "Antes passava a manhã fora de casa; agora precisa sentar-se depois "
          "de tarefas simples. Ele atribui o cansaço ao sono interrompido pela "
          "obstrução nasal, e conta que o nariz tem sangrado um pouco ao "
          "assoar."),
        p("Não refere vômitos, diarreia ou redução importante da ingestão de "
          "líquidos. Ao fim da consulta, pergunta se outro antibiótico "
          "resolveria o problema. A equipe revê o que mudou desde o primeiro "
          "atendimento antes de organizar a investigação."),
        fundo=CENA),

    pergunta("ex_amb", Q(1),
        "Sintomas nasais que não cederam a dois antibióticos, febre "
        "vespertina, artralgia migratória e 6 kg a menos em cinco semanas. "
        "**Quais quatro** exames são os mais apropriados agora?",
        [
            alt("Hemograma completo",
                "Anemia e plaquetose documentariam inflamação de semanas; a "
                "hemoglobina de dois meses serve de comparação.",
                certa=True),
            alt('TSH e T4 livre',
                "Cansaço e perda de peso cabem, mas febre vespertina e "
                "sintomas nasais, não."),
            alt("Proteína C reativa e VHS",
                "Separam doença inflamatória sistêmica de queixa local e "
                "servem de linha de base.",
                certa=True),
            alt("Espirometria",
                "Sem dispneia nem sibilo nesta consulta; não responde à "
                "pergunta de agora."),
            alt("Creatinina",
                "Doença sistêmica sem causa definida pede função renal, e o "
                "valor de 1,0 permite comparar.", certa=True),
            alt("Ácido úrico",
                "Não há artrite, e dor que migra sem sinal flogístico não "
                "sugere gota."),
            alt('Urina com sedimento',
                "Barato e sensível para lesão renal que ainda não dá sintoma; "
                "pede-se junto com a creatinina.",
                certa=True),
            alt("Tomografia de seios da face",
                "Mostraria mucosa espessada, o que já se presume, e não muda "
                "a conduta desta consulta."),
            alt("Eletrocardiograma",
                "Nada na história pede um traçado nesta consulta."),
            alt('Ferritina e saturação de transferrina',
                "Sobe como reagente de fase aguda e repete a proteína C "
                "reativa."),
        ],
        titulo_resposta="Triagem de doença sistêmica, e os resultados vêm a seguir",
        fundo=CENA,
    ),

    painel("res_amb", "O que voltou do ambulatório", "Os exames que a equipe pediu", [
            op("Hemoglobina", resultado="11,2 g/dL {{(13,9 há dois meses)}}",
               referencia="13,5 a 17,5 g/dL", alterado=True),
            op("Leucócitos", resultado="9.800/mm³", referencia="4.000 a 11.000/mm³"),
            op("Plaquetas", resultado="431.000/mm³",
               referencia="150.000 a 400.000/mm³", alterado=True),
            op("Proteína C reativa", resultado="62 mg/L", referencia="até 5 mg/L",
               alterado=True),
            op("VHS", resultado="88 mm/h", referencia="até 20 mm/h", alterado=True),
            op("Creatinina", resultado="1,4 mg/dL {{(1,0 há dois meses)}}",
               referencia="até 1,3 mg/dL", alterado=True),
            op("Sedimento urinário",
               resultado="Proteinúria 1+ · hemácias 12 por campo · sem "
                         "cilindros · sem bacteriúria",
               referencia="sem hemácias, sem proteinúria", alterado=True),
            op("Relação proteína/creatinina urinária", resultado="0,6 mg/mg",
               referencia="abaixo de 0,2 mg/mg", alterado=True),
            op("Radiografia de tórax", resultado="Sem alterações", referencia="normal"),
        ],
        introducao="Estamos oito semanas depois do início e seis semanas antes "
                   "da internação. Clique na imagem para ampliar; o laudo abre "
                   "no botão.",
        fundo=CENA, banco=BANCO,
        laminas={
            "Radiografia de tórax": lamina(RX_NORMAL,
                "Radiografia de tórax, póstero-anterior",
                "Imagem ilustrativa de licença aberta; não pertence a este "
                "paciente.",
                "Mikael Häggström · Wikimedia Commons · CC0"),
        },
    ),

    pergunta("p4", Q(2),
        "Creatinina de 1,4 mg/dL hoje, com referência até 1,3, e 1,0 mg/dL há "
        "dois meses. **Quais três** afirmações essa comparação autoriza?",
        [
            alt('Subiu 40% em relação ao valor dele',
                "A referência é populacional; contra o próprio basal, 1,4 é "
                "aumento de 40%.",
                certa=True),
            alt('A lesão está no glomérulo, pelo padrão da creatinina',
                "Creatinina não localiza o compartimento; quem aproxima isso é "
                "o sedimento."),
            alt('A lesão é recente e tem causa a procurar',
                "Mudança em semanas, sem doença renal prévia, tem causa "
                "procurável e janela de tratamento.", certa=True),
            alt('Caiu cerca de um terço da filtração',
                "Por CKD-EPI 2021, aos 63 anos, cai de cerca de 85 para 56 "
                "mL/min/1,73 m².", certa=True),
            alt("Trata-se de doença renal crônica estágio 2",
                "Cronicidade exige alteração mantida por mais de três meses; "
                "aqui há dois valores diferentes em dois meses."),
            alt("O achado é efeito esperado da losartana",
                "O bloqueador do receptor eleva a creatinina nas primeiras "
                "semanas de uso, e ele usa há dez anos."),
            alt('Já há indicação de diálise, pela velocidade da queda',
                "Não há critério de urgência, e a creatinina isolada não "
                "indica diálise."),
        ],
        titulo_resposta="O valor basal do paciente muda a leitura",
        fundo=CENA,
    ),

    # ══════════════ ATO II — a deterioração, e a leitura de infecção ═════════

    pagina("evolucao_b", "Duas semanas antes", "O atendimento na emergência",
        p("Quatro semanas depois da consulta ambulatorial, iniciou tosse seca "
          "que em poucos dias passou a ter raias de sangue no escarro. "
          "Procurou uma emergência, onde foi feita radiografia de tórax, lida "
          "como normal. Recebeu alta com antitussígeno e orientação de "
          "retorno."),
        fundo=CENA,
    ),

    pergunta("p6", Q(3),
        "Hemoptise de pequeno volume com radiografia de tórax normal, em "
        "ex-tabagista de 63 anos. **Quais quatro** causas devem permanecer no "
        "diferencial?",
        [
            alt("Tromboembolismo pulmonar",
                "Hemoptise ocorre numa parcela dos embolismos, e a radiografia "
                "costuma ser normal.", certa=True),
            alt('Pneumonia lobar em fase inicial',
                "Consolidação lobar costuma aparecer no filme; radiografia "
                "normal não a sustenta."),
            alt("Carcinoma brônquico",
                "Tumor central em ex-tabagista pode ter radiografia normal; "
                "exclui-se por tomografia e broncoscopia.",
                certa=True),
            alt('Abscesso pulmonar por aspiração',
                "Cavidade com nível hidroaéreo aparece no filme, e o escarro "
                "seria purulento e fétido."),
            alt("Bronquite crônica e bronquiectasias",
                "Causa comum de hemoptise com filme normal em quem fumou; "
                "bronquiectasia só aparece na tomografia.",
                certa=True),
            alt('Aspergiloma em cavidade antiga',
                "Exige cavidade prévia, que a radiografia mostraria."),
            alt("Hemorragia alveolar difusa incipiente",
                "A radiografia é pouco sensível para ocupação alveolar "
                "precoce; filme normal não a exclui.", certa=True),
            alt("Edema agudo de pulmão cardiogênico",
                "Congestão capaz de sangrar apareceria no filme como "
                "cefalização, linhas B ou derrame."),
        ],
        titulo_resposta="A radiografia normal não encerrou a investigação",
        fundo=CENA,
    ),


    pagina("evolucao_c", "Na última semana", "A última semana",
        p("Nos sete dias que antecederam a internação, a esposa notou que a "
          "urina dele estava escura, cor de refrigerante de cola, sem "
          "coágulos e sem dor para urinar, e que ele deixou de levantar à "
          "noite para urinar, o que fazia duas vezes por noite há anos."),
        p("Nos últimos três dias, a falta de ar progrediu de esforços grandes "
          "para esforços mínimos e depois para o repouso. Na manhã da "
          "internação teve o segundo episódio de sangue vivo na expectoração, "
          "cerca de 50 mL, e a esposa o trouxe ao pronto-socorro."),
        fundo=CENA,
    ),


    pagina("exame", "Exame físico", "O que o exame mostrou",
        vitais(
            ("Temperatura", "37,8 °C", True),
            ("Pressão arterial", "148/92", True),
            ("Frequência cardíaca", "104", True),
            ("Frequência respiratória", "28", True),
            ("SpO₂ em ar ambiente", "88%", True),
            ("Peso", "78 kg", False),
            ("Altura", "1,72 m", False),
        ),
        grade(
            topicos(
                ("Estado geral",
                 "Dispneico, prefere permanecer sentado, completa apenas "
                 "frases curtas. **Palidez cutâneo-mucosa acentuada.** Pesava "
                 "84 kg há dois meses."),
                ("Cabeça e pescoço",
                 "Crostas hemáticas aderidas ao septo em ambas as narinas, "
                 "mucosa friável que sangra ao toque. Septo íntegro. "
                 "Orofaringe sem lesões. Sem linfonodomegalia."),
                ("Cardiovascular",
                 "Bulhas rítmicas, sem sopros. **Sem estase jugular a 45°.** "
                 "Pulsos amplos e simétricos."),
                ("Respiratório",
                 "Crepitações finas difusas nos dois hemitórax, da base ao "
                 "terço médio. Sem sibilos e sem atrito pleural."),
            ),
            corpo([("via", ""), ("pulmao", "")], altura=300, so_marcas=True), colunas=2),
        fundo=CENA, so_kicker=True),

    pagina("exame_complementar", "Exame físico", "Abdome, pele, membros e exame neurológico",
        grade(
            topicos(
                ("Abdome",
                 "Flácido, indolor, sem massas ou visceromegalias. "
                 "Punho-percussão lombar indolor."),
                ("Membros inferiores",
                 "**Sem edema.** Sem empastamento de panturrilha. Pulsos "
                 "pediosos e tibiais posteriores palpáveis."),
                ("Pele",
                 "Pálida. No dorso dos pés, algumas pápulas avermelhadas de 1 "
                 "a 2 mm, que ele atribui a picadas de inseto na horta. Sem "
                 "lesão em polpas digitais e sem hemorragia subungueal."),
                ("Neurológico",
                 "Consciente e orientado. Força proximal preservada nos quatro "
                 "membros, reflexos patelares presentes. Marcha não testada, "
                 "pela dispneia."),
            ),
            corpo([("pele", "")], altura=320, so_marcas=True), colunas=2),
        fundo=CENA),

    pagina("observacao_admissao", "Pronto-socorro", "Primeira reavaliação",
        p("Com oxigênio suplementar, consegue contar a história em frases mais "
          "longas, mas volta a ficar ofegante ao mudar de posição. A esposa "
          "mostra no lenço pequenas estrias de sangue misturadas ao escarro. "
          "Não houve vômito com sangue."),
        p("A bancada devolve, em vinte minutos, o que a equipe colheu na "
          "chegada: **creatinina 3,8 mg/dL** {{(1,4 há seis semanas)}}, "
          "potássio 5,4 mEq/L, **hemoglobina 7,8 g/dL** {{(11,2 há seis "
          "semanas)}}, leucócitos 14.200/mm³ e proteína C reativa de 186 "
          "mg/L. A hipótese de trabalho é pneumonia grave com lesão renal "
          "aguda."),
        fundo=CENA),

    *ecg('ecg_evolucao',
         'Na observação, o pulso permanece acelerado enquanto ele recebe '
         'oxigênio. A equipe registra um ECG durante essa reavaliação. Como '
         'você descreve o ritmo e como o integra à dispneia?', IMG,
         'A frequência pode acompanhar hipóxia, anemia ou infecção. O traçado '
         'não distingue essas causas: reavalie perfusão e oxigenação antes de '
         'tratar o número isoladamente.'),

    painel("res_adm", "A investigação da admissão", "O que a equipe pediu", [
            op("Sedimento urinário"),
            op("Ultrassonografia de rins e vias urinárias"),
            op("Radiografia de tórax"),
            op("Tomografia de tórax"),
            op("Hemocultura",
               resultado="Três pares em andamento, coletados antes da "
                         "primeira dose", referencia="negativa"),
            op("Procalcitonina", resultado="0,4 ng/mL",
               referencia="abaixo de 0,5 ng/mL"),
        ],
        introducao="Sedimento, imagem e culturas colhidas antes do antibiótico. "
                   "Clique em qualquer figura para ampliar; o laudo abre no botão.",
        fundo=TC, banco=BANCO,
        laminas={
            "Radiografia de tórax": lamina(RX, "Radiografia de tórax",
                "Opacidades alveolares bilaterais, em mancha, predominando nos "
                "campos médios e inferiores. Imagem ilustrativa: o padrão "
                "alveolar não distingue sangue de água ou de pus.",
                "Samir · Wikimedia Commons · CC BY-SA 3.0"),
            "Tomografia de tórax": lamina(TC, "Tomografia de tórax",
                "Cortes axiais em janela de pulmão. Vidro fosco difuso e "
                "bilateral. Imagem ilustrativa: no vidro fosco cabem sangue, "
                "água, pus, células e proteína.",
                "Hellerhoff · Wikimedia Commons · CC BY-SA 4.0"),
            "Ultrassonografia de rins e vias urinárias": lamina(US,
                "Ultrassonografia renal",
                "Rim de ecotextura normal, com diferenciação córtico-medular "
                "preservada e sem hidronefrose. Imagem ilustrativa; o tamanho "
                "vem do laudo, não desta figura.",
                "Hansen, Nielsen e Ewertsen · Wikimedia Commons · CC BY 4.0"),
            "Sedimento urinário": lamina(EAS, "Sedimento urinário",
                "Cilindro urinário: estrutura alongada, de bordas paralelas, "
                "que é o molde do lúmen do túbulo. Imagem ilustrativa, em "
                "preparação corada.",
                "Rian Kabir · Wikimedia Commons · CC BY 2.0"),
        },
    ),

    pagina("gaso", "Pronto-socorro", "A gasometria colhida na chegada",
        p("Enquanto a rodada de exames corre, a equipe lê a gasometria "
          "arterial colhida em ar ambiente na chegada: **pH 7,29 · pCO₂ 32 "
          "mmHg · pO₂ 56 mmHg · HCO₃⁻ 15 mEq/L**. Sódio 136, cloro 104, "
          "albumina 2,9 g/dL, lactato 1,6 mmol/L."),
        p("Pela fórmula de Winters, o pCO₂ esperado é 1,5 × 15 + 8 = 30,5 ± 2, "
          "e o medido cabe nessa faixa: a compensação respiratória está "
          "adequada. O hiato aniônico é 17 e, corrigido pela albumina, cerca "
          "de 20. É acidose metabólica de hiato aumentado com lactato normal, "
          "o que aponta para a função renal, e não para hipoperfusão."),
        fundo=TC),

    pagina("hemo", "Pronto-socorro", "O hemograma, por dentro",
        p("A equipe acrescenta ao hemograma da chegada o que falta para ler "
          "uma anemia: **hemoglobina 7,8 g/dL · hematócrito 23,6% · VCM 88 "
          "fL · reticulócitos 2,1%**. DHL e bilirrubinas normais, Coombs "
          "direto negativo, esfregaço sem esquizócitos."),
        p("Há dois meses a hemoglobina era 13,9 g/dL. A queda de 6 g/dL "
          "aconteceu sem melena, hematêmese ou sangramento nasal volumoso. "
          "Corrigido pelo hematócrito e pelo tempo de maturação, o índice "
          "reticulocitário fica em cerca de 0,5."),
        fundo=ESFREGACO),


    pagina("leitura_infeccao", "Discussão", "A conduta inicial",
        p("Com febre, infiltrado bilateral, proteína C reativa de 186 mg/L e "
          "insuficiência respiratória, a equipe assumiu pneumonia grave com "
          "lesão renal aguda de causa mista, sepse e hipoperfusão, e iniciou "
          "**ceftriaxona e azitromicina** depois de colher as culturas."),
        tabela(["O que sustenta a leitura de infecção",
                "O que já não se encaixa nela"], [
            ["Febre, taquipneia, infiltrado bilateral e proteína C reativa "
             "muito elevada",
             "Oito semanas de doença de via aérea superior que não respondeu a "
             "dois antibióticos"],
            ["Lesão renal aguda é comum na sepse, por hipoperfusão e por "
             "necrose tubular",
             "A creatinina já subia seis semanas antes, sem hipotensão e com "
             "hematúria"],
            ["Ele é ex-tabagista de 30 anos-maço, com fator de risco para "
             "pneumonia",
             "A hemoglobina caiu 6 g/dL em dois meses sem sangramento "
             "digestivo"],
        ]),
        fundo=TC,
    ),

    # ══════════════════════ ATO III — a virada ══════════════════════

    pagina("dia2", "Segundo dia de internação", "A evolução das últimas 36 horas",
        p("Trinta e seis horas depois da primeira dose, a saturação caiu para "
          "89% com cateter nasal a 4 L/min e foi preciso passar para máscara "
          "com reservatório a 10 L/min. A frequência respiratória subiu para "
          "32. Ele expectorou mais duas vezes sangue vivo, cerca de 30 mL cada."),
        p("A hemoglobina, que era 7,8 g/dL na admissão, está em **6,9 g/dL**, "
          "sem melena, sem hematêmese e sem sangramento nasal volumoso nesta "
          "internação. A creatinina subiu para 4,1 mg/dL e o débito urinário "
          "das últimas 24 horas foi de 620 mL."),
        fundo=TC,
    ),

    pagina("reexame", "Segundo dia de internação", "O reexame à beira do leito",
        grade(
            topicos(
                ("Marcha",
                 "Levado ao banheiro com apoio, arrasta a ponta do pé direito. "
                 "Diz que tropeça há cerca de dez dias e achou que era "
                 "fraqueza."),
                ("Neurológico",
                 "Dorsiflexão do pé direito com força 2/5 e aquileu direito "
                 "abolido. Hipoestesia no território ulnar esquerdo. Sem nível "
                 "sensitivo e sem padrão de raiz única."),
                ("Pele",
                 "As pápulas dos pés se multiplicaram e subiram para as "
                 "pernas: lesões elevadas de 2 a 8 mm, algumas com centro "
                 "escurecido, que não desaparecem à digitopressão."),
            ),
            corpo([("pele", ""), ("nervo", "")], altura=320, so_marcas=True), colunas=2),
        fundo=TC),

    estudo('rx_evolucao', 'Radiografia de tórax',
        'Com a piora respiratória, a equipe repete a radiografia à beira do '
        'leito. Descreva a distribuição das opacidades antes de propor uma '
        'causa.',
        IMG / 'rx_torax_alveolar.jpg',
        'Radiografia ilustrativa de outro paciente. A figura não documenta a '
        'evolução temporal deste caso.',
        'Samir · Wikimedia Commons · CC BY-SA 3.0. Recorte prévio e setas; adaptação sob a mesma licença.',
        [
         ((308, 427), (110, 345), '**Opacidades alveolares** no pulmão direito, mais densas nos campos médio e inferior.', 12),
         ((704, 430), (912, 320), 'O mesmo padrão no **pulmão esquerdo**: a doença é bilateral.', -12),
         ((620, 160), (760, 60), '**Ápices relativamente poupados**: o predomínio é central e inferior.', 12),
        ],
        ['Opacidades alveolares bilaterais, em campos médios e inferiores.', 'A distribuição bilateral amplia a discussão para líquido, sangue ou material inflamatório no alvéolo; a radiografia isolada não separa esses mecanismos. Compare com a oxigenação e com a evolução da hemoglobina.']),


    pergunta("p15", Q(4),
        "Ele piorou sob antibiótico adequado. **Quais quatro** achados deste "
        "paciente sustentam hemorragia alveolar difusa?",
        [
            alt("Derrame pleural",
                "A hemorragia alveolar é intraparenquimatosa, e nem a "
                "radiografia nem a tomografia mostram derrame."),
            alt("Nódulos escavados",
                "Apontariam para embolia séptica, micobactéria ou fungo; a "
                "tomografia não os mostra."),
            alt("Escarro purulento",
                "Sugeriria infecção de via aérea; a expectoração dele é "
                "sanguinolenta, nunca purulenta."),
            alt("Queda de hemoglobina desproporcional ao volume expectorado",
                "Cerca de 110 mL expectorados não explicam 7 g/dL a menos; o "
                "sangue ficou no espaço aéreo.", certa=True),
            alt("Hemoptise",
                "Sustenta, mas é pouco confiável: falta em cerca de um terço "
                "das hemorragias alveolares.", certa=True),
            alt("Relação PaO₂/FiO₂ reduzida",
                "Alvéolo cheio de sangue é perfundido e não ventilado: shunt, "
                "que responde mal ao oxigênio.",
                certa=True),
            alt("Capacidade de difusão de monóxido de carbono reduzida",
                "É o contrário: a DLCO sobe, porque a hemoglobina no alvéolo "
                "capta o monóxido de carbono."),
            alt("Infiltrado alveolar bilateral",
                "Compatível e inespecífico: o alvéolo pode estar cheio de "
                "sangue, água, pus ou células.", certa=True),
        ],
        titulo_resposta="A hemoglobina que caiu indica onde o sangue ficou",
        fundo=TC,
    ),

    bifurcacao("b_dia2", "Decisão",
        "Ele piorou sob antibiótico adequado. O que você faz agora?",
        "Trinta e seis horas de ceftriaxona, mais oxigênio, mais hemoptise e "
        "0,9 g/dL a menos de hemoglobina. As culturas ainda não voltaram.",
        [
            caminho("Escalonar o antibiótico para carbapenêmico e vancomicina",
                    "r_escalona",
                    "É a leitura de que o espectro foi insuficiente, e germe "
                    "resistente existe. Mas trinta e seis horas é cedo para "
                    "declarar falha numa pneumonia comunitária, e antibiótico "
                    "mais largo não retém sangue no alvéolo."),
            caminho("Investigar a hemorragia alveolar antes de mudar o "
                    "tratamento", "r_investiga",
                    "A broncoscopia com lavado mostra de onde vem o sangue, e a "
                    "cultura do lavado responde ao que sobrou da hipótese de "
                    "infecção. O antibiótico continua correndo enquanto isso."),
            caminho("Iniciar corticoide em dose imunossupressora agora",
                    "r_corticoide",
                    "A hemorragia alveolar é uma emergência, e o corticoide "
                    "costuma contê-la. O preço é o momento: as culturas ainda "
                    "estão em curso, e nenhum material foi colhido antes."),
        ],
        fundo=TC,
    ),

    pagina("r_escalona", "Terceiro e quarto dias", "Sob o esquema ampliado",
        p("Meropeném e vancomicina correram por 48 horas. A saturação caiu "
          "para 91% em máscara com reservatório a 12 L/min e a hemoglobina "
          "está em **6,3 g/dL**, com nova hemoptise de cerca de 40 mL. A "
          "creatinina subiu para 4,9 mg/dL e a diurese caiu para 380 mL."),
        p("As três hemoculturas da admissão estão negativas em 48 horas. A "
          "urocultura, negativa."),
        fundo=TC, segue="virada",
    ),

    pagina("r_investiga", "Terceiro dia", "A broncoscopia",
        p("Broncoscopia à beira do leito, sob oxigênio a 100%. Árvore "
          "brônquica sem lesão endobrônquica e sem ponto de sangramento "
          "identificável: **sangue difuso escorrendo dos óstios segmentares "
          "dos dois pulmões.**"),
        p("Lavado em três alíquotas de 60 mL no mesmo segmento: a primeira "
          "rosada, a segunda vermelha, a terceira francamente hemorrágica. "
          "Material enviado para citologia e cultura."),
        fundo=TC, segue="virada",
    ),

    pagina("r_corticoide", "Terceiro e quarto dias", "Sob corticoide",
        p("Metilprednisolona 500 mg ao dia. Em 48 horas a hemoptise cessou e a "
          "saturação subiu para 95% em cateter a 4 L/min. A hemoglobina "
          "estabilizou em 6,9 g/dL e a creatinina parou de subir, em 4,6."),
        p("As hemoculturas da admissão estão negativas em 48 horas. **A partir "
          "de agora, toda cultura negativa terá sido colhida sob "
          "imunossupressão**, e o valor dela é menor."),
        fundo=TC, segue="virada",
    ),

    pagina("virada", "Quinto dia de internação", "As culturas",
        p("**As três hemoculturas colhidas antes do antibiótico vieram "
          "negativas em cinco dias.** A urocultura e os antígenos urinários de "
          "pneumococo e de legionela também são negativos."),
        p("Com cinco dias de antibiótico e nenhuma cultura positiva, a equipe "
          "volta ao que o paciente acumulou desde o ambulatório."),
        fundo=TC,
    ),

    pagina("painel_lab", "Evolução laboratorial", "",
        '<div class="painel-lab">'
        + p("A equipe coloca lado a lado o ambulatório, a admissão e o segundo "
            "dia, antes da piora que dividiu as condutas.")
        + tabela(["Exame", "Ambulatório", "Admissão", "Segundo dia", "Referência"], [
            ["Hemoglobina", "11,2 g/dL", "7,8 g/dL", "6,9 g/dL", "13,5–17,5 g/dL"],
            ["Leucócitos", "9.800/mm³", "14.200/mm³", "12.600/mm³", "4.000–11.000/mm³"],
            ["Plaquetas", "431.000/mm³", "468.000/mm³", "452.000/mm³", "150.000–400.000/mm³"],
            ["Creatinina", "1,4 mg/dL", "3,8 mg/dL", "4,1 mg/dL", "até 1,3 mg/dL"],
            ["Proteína C reativa", "62 mg/L", "186 mg/L", "192 mg/L", "até 5 mg/L"],
            ["Procalcitonina", "não dosada", "0,4 ng/mL", "0,3 ng/mL", "abaixo de 0,5 ng/mL"],
            ["Sedimento", "12 hemácias/campo", "Dismorfismo 40%, cilindros hemáticos",
             "não repetido", "sem hemácias"],
        ]) + '</div>',
        fundo=TC, so_kicker=True),

    pergunta("p17", Q(5),
        "Hemorragia alveolar difusa e glomerulonefrite com cilindros "
        "hemáticos, no mesmo paciente e no mesmo mês. **Quais cinco** das "
        "condições abaixo produzem esse par?",
        [
            alt("Tromboembolismo pulmonar com nefropatia por contraste",
                "Dois órgãos por duas vias, mas infarto pulmonar não sangra de "
                "forma difusa, e não houve contraste."),
            alt("Pneumonia comunitária grave com necrose tubular aguda",
                "Necrose tubular dá cilindro granuloso, não hemácia dismórfica "
                "nem cilindro hemático."),
            alt("Lúpus eritematoso sistêmico",
                "Nefrite proliferativa e, numa minoria, hemorragia alveolar, "
                "de alta mortalidade.", certa=True),
            alt("Doença anti-membrana basal glomerular",
                "Anticorpo contra o colágeno tipo IV, presente no alvéolo e "
                "no glomérulo.", certa=True),
            alt("Endocardite infecciosa",
                "Glomerulonefrite por imunocomplexo e êmbolos sépticos; se "
                "presente, contraindica imunossuprimir.",
                certa=True),
            alt("Púrpura trombocitopênica trombótica",
                "Microtrombo no rim, sem hemorragia alveolar; exigiria "
                "esquizócitos e plaquetopenia, que ele não tem."),
            alt("Crioglobulinemia mista",
                "Imunocomplexo em vaso pequeno: glomerulonefrite "
                "membranoproliferativa e capilarite, com C4 consumido.",
                certa=True),
            alt("Leptospirose ictero-hemorrágica",
                "Faz hemorragia alveolar e insuficiência renal, mas a lesão "
                "renal é tubulointersticial, sem cilindro hemático."),
            alt("Vasculite de pequenos vasos associada ao ANCA",
                "Capilarite no alvéolo e no glomérulo pelo mesmo mecanismo, "
                "sem depósito imune.",
                certa=True),
            alt("Síndrome cardiorrenal tipo 1",
                "Congestão dá infiltrado bilateral, mas não cilindro hemático, "
                "e não há estase jugular."),
        ],
        titulo_resposta="Cinco mecanismos, e um deles contraindica o tratamento dos outros",
        fundo=TC,
    ),

    pergunta("ex_mec", Q(6),
        "Hemorragia alveolar e glomerulonefrite, sem resposta a antibiótico e "
        "com culturas negativas. **Quais cinco** exames são os mais "
        "apropriados agora?",
        [
            alt('ANCA, com anti-MPO e anti-PR3',
                "Identifica o grupo pauci-imune e o alvo antigênico; leva "
                "dias, por isso se pede hoje.",
                certa=True),
            alt("Biópsia pulmonar cirúrgica",
                "Exige anestesia em quem está em máscara com reservatório; o "
                "rim responde à mesma pergunta com menos risco."),
            alt('Anti-membrana basal glomerular',
                "A causa que perde rim em dias e muda o tratamento; com o "
                "laboratório avisado, sai em horas.", certa=True),
            alt('PET-CT de corpo inteiro',
                "Não mostra mecanismo nem substitui tecido; não responde à "
                "pergunta de hoje."),
            alt('C3, C4 e crioglobulinas',
                "Complemento consumido aponta imunocomplexo; crioglobulina "
                "exige coleta e transporte aquecidos.", certa=True),
            alt('Angiografia renal por cateter',
                "Procura aneurisma de vaso médio, que não produz "
                "glomerulonefrite nem hemorragia alveolar."),
            alt("FAN e anti-DNA nativo",
                "O lúpus produz esse par com alta mortalidade; FAN negativo "
                "praticamente o afasta.", certa=True),
            alt("Eletroneuromiografia",
                "Documentaria a mononeuropatia já evidente ao exame, sem mudar "
                "a decisão desta semana."),
            alt("Biópsia renal",
                "Diferencia depósito linear, granular ou ausente e gradua a "
                "lesão; o ultrassom já autoriza a punção.",
                certa=True),
            alt("Biópsia de nervo sural",
                "Rende menos que o rim, sacrifica um nervo e só entra se o "
                "rim não puder ser puncionado."),
        ],
        titulo_resposta="Anticorpos, complemento, FAN e tecido: a equipe pede os cinco",
        fundo=BIOPSIA,
    ),

    painel("res_mec", "A investigação do mecanismo", "O que a equipe pediu", [
            op("ANCA por imunofluorescência indireta"),
            op("Anti-mieloperoxidase"),
            op("Anti-proteinase 3"),
            op("Anticorpo anti-membrana basal glomerular"),
            op("Complemento C3 e C4", resultado="C3 112 mg/dL · C4 28 mg/dL",
               referencia="C3 90 a 180 · C4 10 a 40 mg/dL"),
            op("Crioglobulinas"),
            op("FAN e anti-DNA nativo", resultado="Não reagentes",
               referencia="não reagentes"),
            op("Biópsia renal",
               resultado="**Microscopia óptica:** 24 glomérulos · crescentes "
                         "celulares em 15 deles (62%) · necrose fibrinoide "
                         "segmentar · sem esclerose global significativa · "
                         "fibrose intersticial em 10% do córtex · "
                         "**Imunofluorescência:** ausência de depósitos "
                         "significativos de IgG, IgA, IgM, C3 e C1q, "
                         "**padrão pauci-imune** · sem depósito linear",
               referencia="sem proliferação extracapilar, sem depósitos",
               alterado=True),
        ],
        introducao="O anti-MBG voltou em horas; a biópsia, em três dias; o "
                   "ANCA, em quatro. Clique na figura para ampliar; o laudo "
                   "abre no botão.",
        fundo=BIOPSIA, banco=BANCO,
        laminas={
            "Biópsia renal": lamina(BIOPSIA,
                "Biópsia renal, córtex em pequeno aumento",
                "Coloração de PAS: glomérulos, túbulos e interstício. Imagem "
                "ilustrativa de licença aberta; a morfologia da crescente "
                "aparece adiante, em grande aumento.",
                "Nephron · Wikimedia Commons · CC BY-SA 3.0"),
            "ANCA por imunofluorescência indireta": lamina(IF,
                "Imunofluorescência indireta sobre neutrófilos",
                "A fluorescência acompanha o contorno dos lóbulos do núcleo e "
                "poupa o citoplasma: é o **padrão perinuclear**. Neutrófilos "
                "fixados em etanol. Imagem ilustrativa.",
                "Simon Caulton · Wikimedia Commons · CC BY-SA 3.0"),
        },
    ),

    pagina("diferencial", "Discussão", "O diferencial pelo mecanismo",
        p("A síndrome pulmão-rim tem vários mecanismos possíveis. Agrupá-los "
          "pelo que a imunofluorescência mostra permite ler a biópsia deste "
          "paciente: sem depósito, com complemento normal e FAN negativo."),
        tabela(["Mecanismo", "Quem mora nele", "O que decide"], [
            ["Anticorpo contra a membrana basal",
             "Doença anti-MBG (Goodpasture)",
             "Anticorpo circulante e **depósito linear** de IgG. Perde rim em "
             "dias e tem tratamento próprio"],
            ["Deposição de imunocomplexo",
             "Lúpus, crioglobulinemia, vasculite por IgA, pós-infecciosa",
             "**Depósito granular**; complemento consumido em boa parte delas; "
             "sorologia específica"],
            ["Pauci-imune",
             "As vasculites de pequenos vasos associadas ao ANCA",
             "**Ausência de depósito**, com ANCA circulante na maioria"],
            ["Duas vias separadas, não uma doença",
             "Endocardite, leptospirose, sepse com síndrome do desconforto "
             "respiratório e necrose tubular, intoxicação",
             "Hemocultura, ecocardiograma, epidemiologia e a resposta ao "
             "tratamento da infecção"],
        ]),
        fundo=BIOPSIA,
    ),

    pagina("crescente", "Discussão visual", "Corpúsculo renal",
        p("Antes de interpretar a microfotografia, localize a cápsula, o "
          "espaço urinário e o tufo capilar neste esquema. O que significa "
          "uma proliferação ocorrer fora do tufo?"),
        '<details class="leitura"><summary>Revelar pontos de discussão</summary>'
        '<p>O espaço de Bowman está entre o tufo e o epitélio parietal da '
        'cápsula. Uma crescente ocupa esse espaço. O esquema normal orienta a '
        'leitura da microfotografia seguinte, mas não demonstra lesão ou '
        'proporção de glomérulos afetados.</p></details>',
        chave_corpusculo(), fundo=CENA,
        lamina_=lamina("corpusculo.svg", "Corpúsculo renal",
                       "Esquema normal. 2: camada parietal; 4: espaço urinário; "
                       "10: capilares.",
                       "Michał Komorniczak · Wikimedia Commons · CC BY-SA 3.0 · "
                       "sem alterações.")),

    estudo("crescente_histologia", "Biópsia renal",
        "Microfotografia de outro paciente, com a mesma lesão descrita no "
        "laudo. Localize o tufo, a cápsula e o que ocupa o espaço entre eles.",
        IMG / CRESCENTE,
        "PAS. Microfotografia ilustrativa de outro paciente; não permite contar "
        "os glomérulos do laudo do caso.",
        "Nephron · Wikimedia Commons · CC BY-SA 3.0. Setas editoriais; "
        "adaptação sob a mesma licença.",
        [((795, 285), (750, 110), "**Tufo glomerular**: alças capilares, à direita da "
          "proliferação extracapilar.", 14),
         ((432, 292), (230, 210), "**Cápsula de Bowman**: o limite externo do "
          "corpúsculo renal.", 20),
         ((505, 362), (320, 490), "**Crescente**: proliferação extracapilar que ocupa "
          "o espaço de Bowman, na periferia do tufo.", -26)],
        ["Crescentes celulares em 15 dos 24 glomérulos, necrose fibrinoide "
         "segmentar e imunofluorescência sem depósitos significativos (laudo "
         "do caso ficcional).",
         "A microfotografia ilustra a morfologia; não demonstra essa contagem "
         "nem o padrão da imunofluorescência."],
        kicker="Discussão de imagem", fundo=BIOPSIA),

    pagina("crescente_correlacao", "Discussão", "Biópsia renal",
        p("A crescente é uma proliferação extracapilar que ocupa o espaço de "
          "Bowman. O predomínio celular indica atividade e potencial de "
          "resposta; a fibrose representa dano crônico."),
        p("Na classificação de Berden, 50% ou mais de glomérulos com crescente "
          "celular é **classe crescêntica**: prognóstico renal intermediário, "
          "e a classe em que a rapidez do tratamento mais muda a função "
          "residual, porque a crescente celular ainda pode regredir."),
        fundo=BIOPSIA),

    pareamento("p19", Q(7),
        "O anticorpo veio: padrão perinuclear 1:640, anti-MPO 148 U/mL, "
        "anti-PR3 não reagente, anti-MBG não reagente. Associe cada padrão "
        "sorológico ao contexto em que ele é característico.",
        [
            par("c-ANCA com anti-PR3",
                "Granulomatose com poliangeíte",
                "Padrão citoplasmático com anti-PR3; via aérea destrutiva, "
                "granuloma e nódulo escavado."),
            par("p-ANCA com anti-MPO",
                "Poliangeíte microscópica",
                "O perfil dele: rim e capilarite pulmonar, em geral sem "
                "granuloma."),
            par("Anti-PR3 e anti-MPO simultâneos, com anti-elastase",
                "Vasculite por cocaína adulterada com levamisol",
                "Dupla positividade com anti-elastase é atípica das vasculites "
                "primárias e sugere levamisol."),
            par("Anti-MPO com anticorpo anti-membrana basal, os dois positivos",
                "Doença anti-membrana basal com ANCA (dupla positividade)",
                "Rim com prognóstico de anti-MBG e recidiva de vasculite; a "
                "troca plasmática entra."),
            par("p-ANCA atípico, sem anti-MPO nem anti-PR3",
                "Colite ulcerativa, colangite esclerosante e hepatite autoimune",
                "Fluorescência perinuclear sem alvo definido acompanha doença "
                "intestinal e hepatopatia autoimune."),
        ],
        opcoes=[
            "Granulomatose com poliangeíte",
            "Poliangeíte microscópica",
            "Vasculite por cocaína adulterada com levamisol",
            "Doença anti-membrana basal com ANCA (dupla positividade)",
            "Colite ulcerativa, colangite esclerosante e hepatite autoimune",
            "Poliarterite nodosa",
        ],
        titulo_resposta="O alvo do anticorpo orienta o fenótipo",
        nota="A opção que sobrou é a armadilha: a poliarterite nodosa é ANCA "
             "negativa e de vaso médio.",
        fundo=IF,
    ),


    pagina("fenotipo", "Discussão", "Os dois fenótipos",
        p("Tecido pauci-imune e anti-MPO circulante estabelecem vasculite de "
          "pequenos vasos associada ao ANCA. A equipe revê os medicamentos com "
          "a esposa: sem hidralazina, propiltiouracila ou minociclina, e ele "
          "volta a negar cocaína, perguntado a sós."),
        tabela(["", "Poliangeíte microscópica", "Granulomatose com poliangeíte"], [
            ["Sorologia típica", "Anti-MPO, padrão perinuclear",
             "Anti-PR3, padrão citoplasmático"],
            ["Via aérea superior", "Ausente ou leve",
             "Destrutiva: perfuração septal, deformidade em sela"],
            ["Granuloma", "Ausente",
             "Esperado na via aérea e no pulmão; raro no rim"],
            ["Granuloma no rim", "Ausente",
             "Raro também aqui: Bajema e cols. //(Clin Nephrol. "
             "1997;48:16-21)// acharam granuloma renal em 16 de 157 biópsias "
             "de vasculite sistêmica"],
            ["Neste paciente", "Compatível",
             "Improvável, mas não pela biópsia renal: pesam o anticorpo e a "
             "ausência de lesão destrutiva"],
        ]),
        fundo=IF, segue="b1",
    ),

    # ═══════════ ATO IV — o tratamento, e a segunda virada ═══════════

    bifurcacao("b1", "Decisão",
        "Com que esquema você induz a remissão?",
        "Creatinina de 4,6 mg/dL (407 µmol/L), filtração estimada de 14 "
        "mL/min/1,73 m² por CKD-EPI 2021, 78 kg, 63 anos, hemorragia alveolar "
        "em curso. O glicocorticoide é comum aos três caminhos; a segunda "
        "droga é a decisão.",
        [
            caminho("Rituximabe 375 mg/m² por semana, quatro doses",
                    "t_rituximabe",
                    "Não exige ajuste para a função renal e tem eficácia "
                    "equivalente à ciclofosfamida na indução. O RAVE mostrou "
                    "não-inferioridade, mas **excluiu creatinina acima de 4,0 "
                    "mg/dL**, e ele está em 4,6. Para função como a dele, a "
                    "referência é o RITUXVAS, com filtração mediana de 18 "
                    "mL/min, que também não mostrou diferença; ali o braço de "
                    "rituximabe recebeu **dois pulsos de ciclofosfamida** "
                    "junto. A vantagem prática é não depender de uma correção "
                    "de dose."),
            caminho("Ciclofosfamida endovenosa com dose reduzida pela idade e "
                    "pela função renal", "t_cfx_ajustada",
                    "A redução vem do esquema do CYCLOPS, adotado pela EULAR: "
                    "parte de 15 mg/kg e subtrai **2,5 mg/kg entre 60 e 70 "
                    "anos** (5,0 acima de 70) e mais **2,5 mg/kg com "
                    "creatinina entre 300 e 500 µmol/L**. Aqui: 15 − 2,5 − 2,5 "
                    "= **10 mg/kg**, com teto de 1,2 g por pulso."),
            caminho("Ciclofosfamida endovenosa em dose plena, 15 mg/kg",
                    "t_cfx_plena",
                    "A dose de indução sem as duas subtrações. Com filtração "
                    "de 14 mL/min, a exposição fica bem acima da pretendida, "
                    "porque os metabólitos ativos da ciclofosfamida são "
                    "eliminados por via renal."),
        ],
        fundo=CENA,
    ),

    pagina("t_rituximabe", "A prescrição", "O que foi prescrito: caminho A",
        p("**Rituximabe 375 mg/m², uma vez por semana, quatro doses.** "
          "Superfície corporal de 1,93 m² por Mosteller, com 78 kg e "
          "1,72 m: cerca de **725 mg** por dose. Sem correção para a função "
          "renal: o anticorpo monoclonal não é depurado pelo rim.")
        + quadro("O que este caminho pede de vigilância",
            p("Pré-medicação com anti-histamínico, paracetamol e o próprio "
              "glicocorticoide, pela reação infusional da primeira dose. "
              "Rastrear hepatite B **antes**: o anti-HBc isolado reativa sob "
              "rituximabe, e a reativação é grave. Imunoglobulinas séricas na "
              "linha de base, porque a hipogamaglobulinemia tardia é efeito "
              "dos ciclos seguintes."),
            sistema="sangue"),
        fundo=CENA, segue="esquema",
    ),

    pagina("t_cfx_ajustada", "A prescrição", "O que foi prescrito: caminho B",
        p("**Ciclofosfamida endovenosa em pulso, 10 mg/kg.** A conta do "
          "CYCLOPS por extenso: 15 mg/kg de base; −2,5 mg/kg por idade "
          "entre 60 e 70 anos; −2,5 mg/kg por creatinina entre 300 e 500 "
          "µmol/L, e os 4,6 mg/dL de hoje são **407 µmol/L**. Restam "
          "**10 mg/kg**. Com 78 kg, **780 mg** por pulso, abaixo do teto "
          "de 1,2 g. Pulsos nas semanas 0, 2 e 4, depois a cada três "
          "semanas.")
        + quadro("O que este caminho pede de vigilância",
            p("Mesna e hidratação em cada pulso, pela cistite hemorrágica da "
              "acroleína. Hemograma entre o 10º e o 14º dia de cada pulso, "
              "onde cai o nadir: leucócitos abaixo de 3.000/mm³ reduzem o "
              "pulso seguinte para 80% da dose, e abaixo de 2.000, para 60%. "
              "E a conversa sobre fertilidade antes da primeira dose, que aos "
              "63 anos pesa menos, mas não se pula."),
            sistema="sangue"),
        fundo=CENA, segue="esquema",
    ),

    pagina("t_cfx_plena", "A prescrição", "O que foi prescrito: caminho C",
        p("**Ciclofosfamida endovenosa em pulso, 15 mg/kg.** Com 78 kg, "
          "**1,17 g** por pulso. É a dose de indução dos ensaios sem as duas "
          "subtrações, nem a da idade entre 60 e 70 anos, nem a da "
          "creatinina entre 300 e 500 µmol/L. Os metabólitos ativos são "
          "eliminados por via renal, e com filtração de 14 mL/min a "
          "exposição a 1,17 g é maior que a dos ensaios."),
        fundo=CENA, segue="esquema",
    ),

    pagina("esquema", "A prescrição", "O que é igual nos três caminhos",
        grade(*_esquema_comum(), colunas=2),
        fundo=CENA, segue="dia3",
    ),

    pagina("dia3", "Terceiro dia de indução", "A evolução",
        p("Setenta e duas horas depois do primeiro pulso de "
          "metilprednisolona, a hemoptise cessou. A necessidade de oxigênio "
          "caiu de máscara com reservatório para cateter nasal a 3 L/min, com "
          "saturação de 95%. A hemoglobina estabilizou em 6,8 g/dL depois de "
          "**duas unidades de concentrado de hemácias** no primeiro dia."),
        p("A creatinina parou de subir e ficou em 4,6 mg/dL, com diurese de "
          "780 mL. Ele voltou a completar frases inteiras e pediu para comer. "
          "Ao tentar caminhar com ajuda, ainda arrasta a ponta do pé direito."),
        fundo=CENA,
    ),

    pagina("dia5", "Quinto dia de indução", "Quinto dia",
        p("Na madrugada do quinto dia, temperatura de **38,9 °C**, com "
          "calafrio. A pressão arterial caiu para 92/54 mmHg e respondeu a 500 "
          "mL de cristaloide. A frequência cardíaca é de 118 e a saturação, "
          "94% no mesmo cateter nasal a 3 L/min, sem nova hemoptise e sem "
          "piora do infiltrado na radiografia de leito."),
        p("Ele está com um cateter venoso central em jugular interna direita, "
          "puncionado no segundo dia de internação, e o sítio de inserção "
          "está hiperemiado e doloroso à palpação. A proteína C reativa, que "
          "havia caído para 88 mg/L com a indução, está em **204 mg/L**, e a "
          "procalcitonina, que era 0,3, está em **3,1 ng/mL**."),
        fundo=CENA,
    ),

    pergunta("p22", Q(8),
        "Febre de 38,9 °C no quinto dia de indução, hipotensão que respondeu "
        "a volume, sem nova hemoptise. **Quais quatro** causas devem entrar na "
        "lista?",
        [
            alt("Infecção de corrente sanguínea relacionada ao cateter",
                "Cateter de mais de uma semana com sítio inflamado, calafrio e "
                "procalcitonina de 0,3 para 3,1.", certa=True),
            alt("Atividade da vasculite",
                "Entra na lista, mas o órgão-alvo desmente: a hemoptise cessou "
                "e o infiltrado não piorou.", certa=True),
            alt("Pneumocistose",
                "O risco cresce após semanas de glicocorticoide, e a "
                "profilaxia já corre; no quinto dia, é cedo."),
            alt("Tromboembolismo venoso",
                "Vasculite ativa eleva o risco de trombose venosa, e febre com "
                "taquicardia e hipotensão é apresentação possível.",
                certa=True),
            alt("Nadir de neutrófilos da ciclofosfamida",
                "O nadir cai entre o 10º e o 14º dia, e o rituximabe não o "
                "produz."),
            alt("Reação hemolítica transfusional tardia",
                "Transfundido no primeiro dia da indução; febre de 3 a 14 dias "
                "depois pede Coombs e bilirrubina.", certa=True),
            alt("Reativação de citomegalovírus",
                "A reativação exige semanas de imunossupressão; no quinto dia, "
                "é cedo."),
            alt("Reação infusional ao rituximabe",
                "Surge durante a infusão ou nas horas seguintes, não dias "
                "depois."),
        ],
        titulo_resposta="O órgão-alvo está estável; a procalcitonina, não",
        fundo=CENA,
    ),

    bifurcacao("b_febre", "Decisão",
        "Febre no quinto dia de indução. O que você faz?",
        "38,9 °C com calafrio, hipotensão que respondeu a volume, "
        "procalcitonina de 0,3 para 3,1, cateter central com sítio inflamado. "
        "Sem nova hemoptise e sem piora do infiltrado.",
        [
            caminho("Retirar o cateter, colher hemoculturas pareadas e "
                    "iniciar antibiótico com cobertura para "
                    "//Staphylococcus aureus//", "f_retira",
                    "Órgão-alvo estável, procalcitonina subindo e porta de "
                    "entrada visível. Retirar o cateter faz parte do "
                    "tratamento."),
            caminho("Intensificar a imunossupressão, por recidiva da vasculite",
                    "f_intensifica",
                    "Tem lógica se a leitura for de doença descontrolada. Mas a "
                    "hemoptise cessou, o infiltrado não piorou e a "
                    "procalcitonina subiu, o marcador que mais separa "
                    "inflamação estéril de infecção bacteriana."),
            caminho("Suspender toda a imunossupressão até esclarecer a febre",
                    "f_suspende",
                    "Parece prudente. Mas a vasculite acabou de ser controlada "
                    "e a crescente ainda é celular: tratar a infecção e manter "
                    "a indução é possível."),
        ],
        fundo=CENA,
    ),

    pagina("f_retira", "Sétimo dia", "Sob oxacilina",
        p("Cateter retirado; a ponta cultivou o mesmo agente das hemoculturas "
          "pareadas, **//Staphylococcus aureus// sensível a oxacilina**, com "
          "tempo diferencial de positivação compatível com origem no cateter. "
          "O ecocardiograma transesofágico não mostrou vegetação."),
        p("A febre cedeu em 48 horas, sem interromper a indução."),
        fundo=CENA, segue="dia10",
    ),

    pagina("f_suspende", "Sétimo ao nono dia", "Sem imunossupressão",
        p("A febre cedeu com a retirada tardia do cateter e o antibiótico, no "
          "sétimo dia. Mas no nono, com 48 horas sem corticoide, voltou a "
          "hemoptise, dois episódios de cerca de 40 mL, e a saturação caiu "
          "para 90% em cateter a 4 L/min. A hemoglobina caiu de 8,6 para "
          "**7,4 g/dL** e a creatinina voltou a subir, de 4,2 para 4,8."),
        p("A indução foi reiniciada no décimo dia, em dose plena, sobre um "
          "paciente que passou 48 horas sangrando de novo no alvéolo."),
        fundo=CENA, segue="dia10",
    ),

    pagina("f_intensifica", "Sétimo dia", "Sob imunossupressão intensificada",
        p("Metilprednisolona voltou a 1 g ao dia por três dias, sobre a "
          "bacteremia não tratada. **O cateter permaneceu.** Em 24 horas a "
          "temperatura chegou a 39,6 °C, a pressão caiu para 78/44 mmHg e não "
          "respondeu a 2.000 mL de cristaloide. Lactato 4,8 mmol/L."),
        p("As hemoculturas voltaram no sétimo dia com **//Staphylococcus "
          "aureus// em 2 de 2 pares**. Ele foi transferido para a terapia "
          "intensiva em choque, com noradrenalina."),
        fundo=CENA,
        conforme=("b1", ["fi_grave", "fi_grave", "fi_obito"]),
    ),

    pagina("fi_grave", "Do sétimo ao vigésimo dia", "Na terapia intensiva",
        p("Choque séptico por //S. aureus//, com foco em cateter mantido por "
          "48 horas depois do primeiro pico febril. Noradrenalina por seis "
          "dias, oxacilina por 28 dias, a duração de bacteremia complicada, "
          "e diálise por três sessões durante o choque, por oligúria e "
          "acidose refratária."),
        p("Sobreviveu. Saiu da terapia intensiva treze dias depois, com "
          "creatinina de 3,2 mg/dL e diurese recuperada, ainda dependente de "
          "oxigênio suplementar."),
        fundo=CENA,
        conforme=("b1", ["prealta_rituximabe", "prealta_cfx", "prealta_uti"]),
    ),

    desfecho("fi_obito", "Óbito na terceira semana de internação",
        p("O choque séptico se instalou sobre uma medula que a ciclofosfamida "
          "em dose plena, sem correção para a filtração de 14 mL/min, havia "
          "levado a **210 neutrófilos**. A intensificação do corticoide no "
          "sétimo dia foi dada sobre uma bacteremia já em curso, com a porta "
          "de entrada ainda no pescoço."),
        p("Evoluiu com disfunção de múltiplos órgãos e choque refratário a "
          "três drogas vasoativas. Faleceu no nono dia de bacteremia."),
        p("**A vasculite estava respondendo.** A hemoptise havia cessado no "
          "terceiro dia de indução e o infiltrado não voltou a piorar."),
        qualidade="pior", fecho="tres_caminhos",
        porque="Três decisões se somaram, e nenhuma delas era sobre o "
               "diagnóstico. A dose plena da ciclofosfamida com filtração de "
               "14 mL/min entregou uma neutropenia que o esquema corrigido não "
               "produziria. A febre do quinto dia foi lida como recidiva "
               "quando a procalcitonina, o órgão-alvo estável e o sítio de "
               "inserção indicavam infecção. E o cateter, a porta de entrada, "
               "permaneceu. No primeiro ano da vasculite ANCA tratada, a "
               "infecção mata mais do que a própria vasculite.",
        fundo=CENA),

    pagina("dia10", "Décimo dia de indução", "Décimo dia",
        p("O que vem a seguir depende do esquema de indução escolhido, e é "
          "aqui que os três caminhos deixam de ser o mesmo caso."),
        fundo=CENA,
        conforme=("b1", ["d10_rituximabe", "d10_cfx_ajustada", "d10_cfx_plena"]),
    ),

    pagina("d10_rituximabe", "Décimo dia · caminho A", "O hemograma do décimo dia",
        p("O hemograma do décimo dia mostra **6.400 leucócitos com 4.100 "
          "neutrófilos**, sem citopenia. O rituximabe depleta linfócito B e "
          "não produz nadir de neutrófilos: a bacteremia veio do cateter e do "
          "corticoide, não da segunda droga."),
        p("Completou as quatro doses semanais e catorze dias de oxacilina. A "
          "creatinina caiu de forma sustentada."),
        fundo=CENA, segue="prealta_rituximabe",
    ),

    pagina("d10_cfx_ajustada", "Décimo dia · caminho B", "O hemograma do décimo dia",
        p("O hemograma do décimo dia, no nadir esperado do pulso, mostra "
          "**3.600 leucócitos com 1.900 neutrófilos**. É citopenia leve, "
          "dentro do previsto para 10 mg/kg; com nadir acima de 3.000 "
          "leucócitos, o pulso seguinte fica na mesma dose, e o hemograma "
          "passa a ser duas vezes por semana durante a bacteremia."),
        p("A febre cedeu, completou catorze dias de oxacilina, e o segundo "
          "pulso foi dado na semana 2 como programado."),
        fundo=CENA, segue="prealta_cfx",
    ),

    pagina("d10_cfx_plena", "Décimo dia · caminho C", "O hemograma do décimo dia",
        p("O hemograma do décimo dia mostra **900 leucócitos com 210 "
          "neutrófilos**. A febre, que havia cedido com a oxacilina, voltou a "
          "39,4 °C, agora com hipotensão que exigiu noradrenalina, e ele foi "
          "transferido para a terapia intensiva."),
        p("A neutropenia é muito mais profunda do que a esperada: o nadir de "
          "um pulso ajustado fica em torno de 1.900 neutrófilos. Foram "
          "acrescentados antibiótico de amplo espectro, cobertura antifúngica "
          "empírica ao quinto dia de neutropenia febril e fator estimulador de "
          "colônias."),
        fundo=CENA, segue="prealta_uti",
    ),

    pagina("prealta_rituximabe", "Após estabilização", "Preparação do seguimento",
        p("Passa a fazer os trajetos da enfermaria com apoio. A dispneia em "
          "repouso deixou de dominar a conversa; agora pergunta como retomará "
          "as atividades em casa. A dificuldade com o pé exige orientação "
          "para marcha e segurança."),
        p("Na reconciliação da prescrição, a equipe escreve as datas das "
          "próximas infusões e retornos, além do desmame indicado."),
        fundo=CENA, segue="d_rituximabe"),

    pagina("prealta_cfx", "Após estabilização", "Planejamento dos próximos pulsos",
        p("Está mais disposto e volta a comer fora do leito. Ainda precisa de "
          "ajuda em percursos longos e não se sente seguro para andar sozinho "
          "à noite. A esposa pretende permanecer com ele na primeira semana em "
          "casa."),
        p("A equipe organiza a avaliação antes de cada pulso, com revisão da "
          "tolerância e dos exames programados. Ele recebe um calendário por "
          "escrito e orientações para procurar atendimento diante de febre ou "
          "nova piora respiratória."),
        fundo=CENA, segue="d_cfx_ajustada"),

    pagina("prealta_uti", "Depois da terapia intensiva", "Recuperação na enfermaria",
        p("Fora da terapia intensiva, o paciente está desperto e reconhece a "
          "família. Precisa interromper a caminhada até o banheiro e se apoia "
          "no acompanhante para levantar. Conta que não se lembra de parte da "
          "internação e teme voltar a piorar."),
        p("A equipe revê com a família o que ocorreu, organiza reabilitação e "
          "reconcilia os medicamentos."),
        fundo=CENA, segue="d_cfx_plena"),

    desfecho("d_rituximabe", "Alta sem diálise",
        p("A creatinina, que havia chegado a 4,6 mg/dL, caiu de forma "
          "sustentada e a diurese se recuperou, **sem necessidade de diálise "
          "em nenhum momento**. Saiu em ar ambiente, com saturação de 96%."),
        p("Segue em manutenção programada com rituximabe, com consulta e "
          "exames agendados, e com o pé caído em reabilitação: a mononeurite "
          "é o achado que mais demora a melhorar, quando melhora."),
        qualidade="melhor", fecho="tres_caminhos",
        porque="O tratamento entrou enquanto a crescente ainda era celular, "
               "que é lesão ativa e capaz de responder. Com filtração de 14 "
               "mL/min/1,73 m², o rituximabe entrega a indução sem depender "
               "de uma correção de dose, e a infecção de cateter não encontrou "
               "uma medula deprimida pela segunda droga.",
        fundo=CENA),

    desfecho("d_cfx_ajustada", "Alta sem diálise, com vigilância semanal",
        p("A creatinina estabilizou acima do valor do caminho A e a diurese se "
          "recuperou, sem diálise. O hemograma foi vigiado duas vezes por "
          "semana durante a bacteremia e o nadir do segundo pulso foi de "
          "1.600 neutrófilos."),
        p("Completou catorze dias de oxacilina e os três primeiros pulsos de "
          "ciclofosfamida sem nova intercorrência infecciosa."),
        qualidade="melhor", fecho="tres_caminhos",
        porque="A ciclofosfamida com dose corrigida pela idade e pela "
               "filtração é tão eficaz quanto o rituximabe na indução. Custa "
               "mais vigilância (hemograma seriado, mesna, ajuste a cada "
               "ciclo) e cobra a conversa sobre fertilidade que o rituximabe "
               "dispensa. Neste paciente, de 63 anos, essa conversa pesa "
               "menos; a conta da dose, não.",
        fundo=CENA),

    desfecho("d_cfx_plena", "Alta após a terapia intensiva",
        p("A vasculite respondeu como nos outros dois caminhos: a hemoptise "
          "cessou no terceiro dia e a creatinina caiu. O que mudou foi o "
          "resto. Foram treze dias de terapia intensiva, noradrenalina por "
          "quatro deles, antibiótico de amplo espectro, antifúngico empírico "
          "e fator estimulador de colônias."),
        p("Saiu andando, com mais dias de internação e menos função renal que "
          "nos outros caminhos."),
        qualidade="pior", fecho="tres_caminhos",
        porque="Com filtração glomerular de 14 mL/min/1,73 m², a dose plena "
               "produziu exposição bem acima da pretendida: os metabólitos "
               "ativos da ciclofosfamida são eliminados por via renal, e a "
               "conta do CYCLOPS teria pedido 10 mg/kg. No primeiro ano da "
               "vasculite ANCA tratada, a infecção mata mais do que a "
               "vasculite. Aqui a infecção veio do cateter, que os três "
               "caminhos tinham; a profundidade dela veio da dose, que só "
               "este caminho escolheu.",
        fundo=CENA),

    # ═══════════════ o fecho, igual para os três ramos ═══════════════

    pagina("tres_caminhos", "Onde o caso se dividiu", "Os três caminhos",
        p("O caso ramificou em três lugares. O primeiro foi o que fazer "
          "quando ele piorou sob antibiótico. O segundo, a segunda droga da "
          "indução, que a tabela compara abaixo. O terceiro foi a febre do "
          "quinto dia, o único com um ramo que termina em óbito."),
        tabela(["Caminho", "A conta que ele exige",
                "Neutrófilos no 10º dia", "Desfecho"], [
            ["A · Rituximabe 375 mg/m² semanal",
             "Nenhuma correção para a filtração",
             "4.100", "Alta mais precoce · melhor função residual"],
            ["B · Ciclofosfamida 10 mg/kg",
             "15 − 2,5 (idade) − 2,5 (creatinina)",
             "1.900", "Cinco dias a mais · função um degrau abaixo"],
            ["C · Ciclofosfamida 15 mg/kg",
             "Nenhuma, e esse é o erro",
             "210", "Treze dias a mais · terapia intensiva"],
        ]),
        fundo=CENA,
    ),


    balanco("balanco", "O balanço da sua condução",
        "O percurso e o preço",
        p("O que cada decisão custou, contra o melhor percurso que este caso "
          "permite. Os números são inferência autoral, coerente com a "
          "fisiologia do caso, e cada linha traz o motivo que a sustenta."),
        base_dias=21, base_tfg=39, base_creatinina="1,9 mg/dL",
        obito_se={"escolheu_todos": [["b_febre", 1], ["b1", 2]]},
        obito_texto="Ciclofosfamida em dose plena com filtração de 14 mL/min, "
                    "e a febre do quinto dia lida como recidiva da doença. A "
                    "vasculite estava respondendo: a hemoptise havia cessado "
                    "no terceiro dia e o infiltrado nunca voltou a piorar. "
                    "Nenhuma das decisões que levaram ao óbito era sobre o "
                    "diagnóstico.",
        consequencias=[
            consequencia(
                chave="escalonou",
                titulo="Escalonou o antibiótico em vez de investigar o sangramento",
                quando={"escolheu": ["b_dia2", 0]}, dias=3, tfg=6,
                porque="Trinta e seis horas é cedo para declarar falha de "
                       "antibiótico numa pneumonia comunitária, e nenhum "
                       "espectro retém sangue no alvéolo. Foram 48 horas a "
                       "mais de sangramento e de creatinina subindo, com "
                       "crescentes celulares em formação."),
            consequencia(
                chave="corticoide_antes_das_provas",
                titulo="Imunossuprimiu antes de colher qualquer prova",
                quando={"escolheu": ["b_dia2", 2]}, dias=2, tfg=2,
                porque="Parou o sangramento, e isso conta. Mas toda cultura "
                       "colhida a partir dali foi colhida sob corticoide, e o "
                       "negativo delas vale menos justamente quando se "
                       "precisa dele para justificar o que já foi feito."),
            consequencia(
                chave="febre_intensificou",
                titulo="Leu a febre do quinto dia como recidiva da vasculite",
                quando={"escolheu": ["b_febre", 1]}, dias=14, tfg=14,
                porque="A hemoptise havia cessado, o infiltrado não piorou e a "
                       "procalcitonina subiu de 0,3 para 3,1. Intensificar a "
                       "imunossupressão sobre uma bacteremia com a porta de "
                       "entrada ainda no pescoço levou a choque séptico e a "
                       "três sessões de diálise."),
            consequencia(
                chave="febre_suspendeu",
                titulo="Suspendeu toda a imunossupressão",
                quando={"escolheu": ["b_febre", 2]}, dias=6, tfg=9,
                porque="Quarenta e oito horas sem corticoide bastaram para o "
                       "alvéolo voltar a sangrar e a creatinina voltar a "
                       "subir. Tratar a infecção e manter a indução era "
                       "possível."),
            consequencia(
                chave="cfx_ajustada",
                titulo="Escolheu ciclofosfamida, com a conta feita",
                quando={"escolheu": ["b1", 1]}, dias=5, tfg=8,
                porque="Tão eficaz quanto o rituximabe na indução, e o nadir de "
                       "1.900 neutrófilos ficou onde a dose corrigida prevê. "
                       "Custa mais vigilância e mais dias, e o preço é da "
                       "droga, não de um erro de conduta."),
            consequencia(
                chave="cfx_plena",
                titulo="Escolheu ciclofosfamida sem a correção de dose",
                quando={"escolheu": ["b1", 2]}, dias=13, tfg=12,
                porque="Os metabólitos ativos saem por via renal, e com "
                       "filtração de 14 mL/min a exposição de 15 mg/kg é bem "
                       "maior do que a pretendida. A vasculite respondeu igual "
                       "nos três caminhos; o que mudou foi a medula, e a "
                       "bacteremia encontrou 210 neutrófilos em vez de 1.900."),
        ],
        fundo=CENA,
    ),

    pagina("lacuna", "O que fica sem explicação", "A lacuna",
        p("Três achados deste paciente continuam sem explicação completa "
          "depois do diagnóstico fechado."),
        quadro("Os sintomas nasais",
            p("Obstrução, crostas hemáticas e sangramento ao assoar por oito "
              "semanas, sem resposta a dois antibióticos, descrevem doença de "
              "via aérea superior, território próprio da granulomatose com "
              "poliangeíte. A poliangeíte microscópica pode acometê-la de "
              "forma leve, e é a leitura que sustentamos; quem disser que é um "
              "fenótipo sobreposto não está errado, e a literatura não fecha "
              "essa fronteira."),
            sistema="via"),
        quadro("A resposta medular",
            p("A queda de hemoglobina localiza o sangue no alvéolo, e a "
              "Pergunta 4 estabeleceu isso. O que fica sem explicação é a "
              "resposta a ela: o índice reticulocitário de 0,5 é medula que "
              "não repõe o que se perde. Inflamação de oito semanas e "
              "deficiência de eritropoetina na lesão renal aguda explicam boa "
              "parte, e **nenhuma das duas foi medida** neste paciente."),
            sistema="sangue"),
        quadro("A artralgia migratória",
            p("Compatível com a doença e inespecífica: acompanha vasculite, "
              "infecção arrastada e doença do tecido conjuntivo com a mesma "
              "facilidade. Entra na história como achado compatível, sem valor "
              "de pista."),
            sistema="geral"),
        fundo=CENA,
        so_kicker=True,
    ),

    pagina("retrospectiva", "Onde dava para ter chegado antes",
        "A retrospectiva",
        p("Em que momento, antes do quinto dia, a informação já estava "
          "disponível, e o que impediu que fosse usada."),
        tabela(["Quando", "O que estava à mão", "O que aconteceu"], [
            ["Oito e quatro semanas antes",
             "Rinossinusite que não respondeu a **dois** cursos de antibiótico, "
             "com adesão confirmada",
             "Mantida como infecção. Doença de mucosa que não cede a "
             "antibiótico correto é um dado a investigar"],
            ["Seis semanas antes",
             "Creatinina de 1,4 mg/dL com hematúria de 12 por campo, num "
             "paciente cuja creatinina era 1,0",
             "Lida como quase normal. Era perda de um terço da filtração em "
             "dois meses, com sangue na urina; a pesquisa de dismorfismo "
             "naquele dia teria custado quase nada"],
            ["Duas semanas antes",
             "Radiografia de tórax normal num paciente com hemoptise",
             "Tratada como exclusão. A radiografia é pouco sensível para "
             "ocupação alveolar precoce"],
            ["Na última semana",
             "Urina escura e noctúria que desapareceu, referidas pela esposa",
             "Não foram perguntadas. Quem deixa de acordar para urinar depois "
             "de anos fazendo isso pode estar oligúrico"],
            ["Na admissão",
             "Pápulas nos pés atribuídas a picada de inseto; marcha não testada",
             "Reconhecidas como púrpura e mononeuropatia múltipla só no "
             "segundo dia"],
        ]),
        quadro("O viés que operou aqui",
            p("Fechamento precoce: a primeira explicação plausível foi mantida "
              "por oito semanas, e cada sintoma novo foi encaixado nela ou "
              "tratado como evento separado: sinusite, depois artralgia, "
              "depois tosse, depois pneumonia. A pergunta que quebra esse viés "
              "é **por que a doença anterior não respondeu ao tratamento "
              "correto**."),
            sistema="geral"),
        fundo=CENA,
        so_kicker=True,
    ),

    pagina("procedencia", "Procedência e créditos", "Procedência",
        grade(
            quadro("O caso",
                p("**Autoral, curso simulado.** Paciente ficcional. Os "
                  "números fecham entre si."),
                sistema="geral")
            + quadro("As cenas do paciente",
                p("**Ilustração gerada por inteligência artificial** a partir "
                  "da descrição clínica deste caso. Não retrata pessoa real."),
                sistema="geral"),
            quadro("As imagens médicas",
                p("Reais, ilustrativas, de licença aberta, e **não pertencem "
                  "a este paciente**. Radiografia de tórax: "
                  "Samir, Wikimedia Commons, CC BY-SA 3.0. Tomografia: "
                  "Hellerhoff, Wikimedia Commons, CC BY-SA 4.0. Ultrassom "
                  "renal: Hansen, Nielsen e Ewertsen, CC BY 4.0. Sedimento "
                  "urinário: Rian Kabir, CC BY 2.0. Glomérulo e córtex renal: "
                  "Nephron, CC BY-SA 3.0. Imunofluorescência: Simon Caulton, "
                  "CC BY-SA 3.0. Radiografia normal e tomografia de seios: "
                  "Mikael Häggström, CC0 e CC BY 4.0. ECG: Ewingdo, CC BY-SA "
                  "4.0. Corpúsculo renal: Michał Komorniczak, CC BY-SA 3.0. "
                  "As setas sobre as figuras são leitura editorial deste caso."),
                sistema="pulmao"),
            quadro("As diretrizes citadas",
                p("PEXIVAS //(N Engl J Med. 2020;382:622-31)// para troca "
                  "plasmática e desmame de glicocorticoide; CYCLOPS "
                  "//(Ann Intern Med. 2009;150:670-80)// para a correção de "
                  "dose da ciclofosfamida; RAVE //(N Engl J Med. "
                  "2010;363:221-32)// e RITUXVAS //(N Engl J Med. "
                  "2010;363:211-20)// para o rituximabe."),
                p("ADVOCATE //(N Engl J "
                  "Med. 2021;384:599-609)// para o avacopan; EULAR 2022 e "
                  "KDIGO 2024 para as recomendações; Berden //(J Am Soc "
                  "Nephrol. 2010;21:1628-36)// para a classificação "
                  "histológica; Bajema //(Clin Nephrol. 1997;48:16-21)// para "
                  "o granuloma renal."),
                sistema="rim"),
            colunas=4,
        ),
        fundo=CENA, so_kicker=True,
    ),
]


# ═══════════════ o que a revisão cobra, quando não há mais o que decidir ══════

REVISAO = []

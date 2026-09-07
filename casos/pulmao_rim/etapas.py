"""O caso pulmão-rim em etapas.

Página a página, sem relógio. O título segue a regra da CPC: idade, sexo e de
dois a quatro achados de apresentação — nunca o diagnóstico.

Três decisões de estrutura, tiradas dos casos interativos do //New England//:

1. **O caso tem uma virada.** Ele não caminha em linha reta da síndrome ao
   diagnóstico. A leitura natural na admissão é infecção grave, o paciente
   recebe antibiótico, e é **sob antibiótico adequado que ele piora**. A
   cultura negativa e o lavado hemorrágico é que viram o caso. Sem virada, o
   diagnóstico está disponível na metade da apresentação e a segunda metade
   vira confirmação — que é o defeito que este arquivo existe para não ter.

2. **O paciente reaparece.** Entre um painel de exames e o seguinte há sempre
   uma página de evolução: o que mudou nele, não no laboratório. São oito
   páginas de evolução clínica, do ambulatório ao décimo dia de indução.

3. **A segunda virada é no tratamento.** No quinto dia de indução vem febre, e
   separar falha terapêutica, complicação do tratamento e segunda doença é a
   pergunta mais difícil e a mais real do caso.

O paciente é ficcional. Os números foram desenhados para serem internamente
coerentes: gasometria que fecha por Henderson-Hasselbalch, filtração por
CKD-EPI 2021, e a relação PaO₂/FiO₂ calculada, não estimada.
"""

from pathlib import Path

from motor.desenhos import anotada, corpo, seta
from motor.etapas import (
    alt, balanco, bifurcacao, caminho, capa, consequencia, desfecho, grade,
    grupo, lamina, op, p, pagina, pedido, pergunta, quadro, resultados, tabela,
    topicos, vitais,
)

from .banco import BANCO  # noqa: F401  — a gaveta de exames é a mesma

# O título anterior — "hemoptise, púrpura e queda da função renal" — era a
# tríade inteira. Quem conhece o padrão lia síndrome pulmão-rim por vasculite
# antes da primeira página, e o título fica no topo das 55 telas: vazava em
# todas. Além disso "queda da função renal" é resultado de exame, e a regra da
# CPC é que o título traga sintomas e sinais da APRESENTAÇÃO — nunca um
# diagnóstico, nunca um exame que entregue o caso.
#
# O que trouxe este paciente ao pronto-socorro foi falta de ar e sangue no
# escarro. A púrpura apareceu no exame físico; a creatinina, no laboratório.
# O título descritivo da CPC — idade, sexo e dois a quatro achados — resolvia o
# vazamento e ainda dizia demais: "dispneia e hemoptise" já entrega o órgão.
#
# A série interativa permite o título evocativo, e é o único lugar em que o
# //New England// permite. O documento de referência avisa que em português
# isso descamba para efeito barato, e a saída é a mesma dos bons originais
# (//Painful Purple Toes//, //A Sleeping Giant//): o título nomeia uma coisa
# LITERAL do caso e só ganha o segundo sentido no fim. Aqui, a hemoglobina que
# desapareceu sem que ninguém visse sangue sair — que é a virada — e, no
# fecho, o preço que não apareceu em lugar nenhum até a última tela.
TITULO = "O sangue que não saiu"
RODAPE = "Caso interativo · curso simulado"
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


# ═════════════════ o que é comum aos três esquemas de indução ═══════════════

def _esquema_comum():
    """Tudo o que não muda com a escolha da segunda droga, em dois pares."""
    glicocorticoide = quadro("O glicocorticoide, igual nos três caminhos",
        p("Metilprednisolona 500 mg/dia por três dias, depois prednisona — "
          "**75 mg/dia** pela faixa de peso acima de 75 kg. O PEXIVAS (2020) "
          "mostrou que o **desmame reduzido**, que chega a cerca de 60% da "
          "dose acumulada em seis meses, é não-inferior e derruba as infecções "
          "graves em um ano."),
        sistema="geral")
    plasma = quadro("Troca plasmática: uma decisão em disputa",
        p("O PEXIVAS não mostrou redução de morte ou de doença renal terminal "
          "em 704 pacientes. Mas a EULAR de 2022 diz que ela **pode ser "
          "considerada** acima de 300 µmol/L — ele está em **336** — e a KDIGO "
          "mantém a hemorragia alveolar com hipoxemia na lista. Aqui ela é "
          "**discutível**, não descartada: quem indicar não está errado, e "
          "quem não indicar também não."),
        sistema="sangue")
    avacopan = quadro("Avacopan, e por que ele não entra aqui",
        p("O ADVOCATE (2021) mostrou **superioridade na remissão sustentada em "
          "52 semanas**, poupando glicocorticoide. É adjuvante, não substituto "
          "da indução — e o limite aqui não é a evidência, é a "
          "disponibilidade."),
        sistema="geral")
    cerco = quadro("Antes da primeira dose, e depois dela",
        p("Antes: sorologias de hepatite B e C e HIV, e a cultura que autoriza "
          "imunossuprimir. Depois: sulfametoxazol-trimetoprima **400/80 mg "
          "três vezes por semana** — dose reduzida pela filtração de 17, "
          "porque o trimetoprim ainda empurra potássio num paciente que chegou "
          "com 5,4. Cálcio, vitamina D e hemograma semanal."),
        sistema="pulmao")
    return glicocorticoide + plasma, avacopan + cerco


ETAPAS = [

    # ═══════════════════════════ capa ═══════════════════════════

    capa(TITULO, fundo=CENA,
         kicker="Caso interativo · 12 decisões · curso simulado",
         selo="Paciente ficcional · procedência e créditos na última tela"),

    # ══════════════ ATO I — as oito semanas que ninguém fechou ══════════════

    pagina("abertura", "Oito semanas antes", "O primeiro atendimento",
        p("Um homem de 63 anos, ex-tabagista, estava em seu estado habitual de "
          "saúde até oito semanas antes desta admissão, quando surgiu secreção "
          "nasal purulenta persistente, com crostas em ambas as narinas e "
          "sangramento nasal quase diário."),
        p("Foi atendido na unidade básica e tratado como rinossinusite "
          "bacteriana com amoxicilina por dez dias. Não melhorou. Voltou "
          "quatro semanas depois e recebeu amoxicilina-clavulanato por catorze "
          "dias, com adesão confirmada pela esposa. **Também não melhorou.** "
          "Nesse período deixou de sentir cheiro."),
        # Sem lâmina aqui: o fundo desta página JÁ é a mesma ilustração, e
        # pendurar uma cópia dela num quadro ao lado é ruído, não figura.
        fundo=CENA,
    ),

    pergunta("p1", "Pergunta 1",
        "Rinossinusite com crostas e epistaxe diária, sem resposta a dois "
        "cursos de antibiótico adequados. **Quais quatro** categorias entram "
        "no diferencial agora?",
        [
            alt("Doença inflamatória sistêmica",
                "Mucosa que ulcera e sangra por semanas sem infecção é "
                "apresentação de várias delas — e a nasal costuma ser a "
                "primeira.", certa=True),
            alt("Desvio de septo",
                "Causa obstrução fixa e sangramento por ressecamento, sem "
                "curso progressivo em semanas."),
            alt("Infecção por agente não coberto por betalactâmico",
                "Fungo e micobactéria não respondem a amoxicilina e produzem "
                "exatamente crosta, sangramento e destruição lenta.",
                certa=True),
            alt("Rinite alérgica",
                "Prurido, espirro e secreção clara. Não faz crosta hemática "
                "nem epistaxe diária por oito semanas."),
            alt("Lesão por substância inalada",
                "Cocaína e descongestionante tópico crônico destroem mucosa e "
                "cartilagem. É pergunta obrigatória, e quase nunca feita.",
                certa=True),
            alt("Neoplasia de cavidade nasal",
                "Carcinoma e linfoma de linha média dão obstrução, crosta e "
                "epistaxe, com anosmia progressiva.", certa=True),
            alt("Resistência bacteriana ao esquema usado",
                "Possível, mas sobreviver a dois espectros diferentes com "
                "adesão confirmada deixou de ser a explicação mais provável."),
            alt("Trauma digital local",
                "Explica epistaxe recorrente. Não explica secreção purulenta "
                "por oito semanas com perda de olfato."),
        ],
        titulo_resposta="Não responder ao tratamento correto é um dado",
        fundo=CENA,
    ),

    pagina("evolucao_a", "Cinco semanas antes", "Os sintomas que se somaram",
        p("Três semanas depois do início dos sintomas nasais, surgiram dores "
          "articulares que mudavam de lugar — punhos numa semana, tornozelos "
          "na outra — sem edema, calor ou rigidez matinal prolongada."),
        p("Passou a ter febre no fim da tarde, medida em casa até 37,9 °C, com "
          "sudorese noturna que molhava a camisa. Perdeu 6 kg em cinco semanas "
          "sem mudar a alimentação. A esposa insistiu para que voltasse ao "
          "médico, e ele foi encaminhado ao ambulatório de clínica médica."),
        fundo=CENA,
    ),

    pagina("anamnese", "No ambulatório", "O que se sabia dele",
        p("Hipertenso há dez anos, em uso de losartana 50 mg por dia. "
          "Ex-tabagista de 30 anos-maço, parou há oito anos. Sem diabetes e "
          "sem doença renal conhecida. Trabalhou como pedreiro até os 58 anos "
          "e hoje cuida de uma pequena horta."),
        p("Trouxe impressos os exames de rotina de dois meses antes, pedidos "
          "na unidade básica: **creatinina 1,0 mg/dL, hemoglobina 13,9 g/dL e "
          "urina sem alterações.**"),
        quadro("Perguntado nominalmente",
            p("Nega anti-inflamatório, chá, suplemento e fórmula de "
              "emagrecimento. Nega hidralazina, propiltiouracila e "
              "minociclina, e nega uso de cocaína em qualquer momento da vida "
              "— perguntado duas vezes, em consultas diferentes. Mora em "
              "Quixadá, em casa de alvenaria com água encanada; não houve "
              "enchente na região, e nega contato com roedores. Sem viagem "
              "recente, sem contato com pessoa com tosse crônica."),
            sistema="geral"),
        fundo=CENA,
    ),

    pedido("ex_amb", "Pergunta 2",
        "Que exames você pede aqui?",
        "Ambulatório de unidade básica, resultado em três a cinco dias. "
        "**Quatro vagas.** O que não for pedido não volta, nem agora nem "
        "depois.",
        [
            grupo("Sangue", "sangue", [
                op("Hemoglobina", resultado="11,2 g/dL {{(13,9 há dois meses)}}",
                   referencia="13,5 a 17,5 g/dL", alterado=True),
                op("Leucócitos", resultado="9.800/mm³",
                   referencia="4.000 a 11.000/mm³"),
                op("Plaquetas", resultado="431.000/mm³",
                   referencia="150.000 a 400.000/mm³", alterado=True),
                op("Proteína C reativa", resultado="62 mg/L",
                   referencia="até 5 mg/L", alterado=True),
                op("VHS", resultado="88 mm/h", referencia="até 20 mm/h",
                   alterado=True),
                op("Ferritina", resultado="410 ng/mL",
                   referencia="30 a 400 ng/mL", alterado=True),
                op("Albumina", resultado="3,6 g/dL", referencia="3,5 a 5,2 g/dL"),
                op("Glicemia de jejum", resultado="94 mg/dL",
                   referencia="até 99 mg/dL"),
                op("TSH", resultado="2,1 mUI/L", referencia="0,4 a 4,0 mUI/L"),
                op("Eosinófilos", resultado="280/mm³ (2,9%)",
                   referencia="50 a 500/mm³"),
            ]),
            grupo("Rim e urina", "rim", [
                op("Creatinina",
                   resultado="1,4 mg/dL {{(1,0 há dois meses)}}",
                   referencia="até 1,3 mg/dL", alterado=True),
                op("Sedimento urinário",
                   resultado="Proteinúria 1+ · **hemácias 12 por campo** · "
                             "sem cilindros · sem bacteriúria",
                   referencia="sem hemácias, sem proteinúria", alterado=True),
                op("Relação proteína/creatinina urinária",
                   resultado="0,6 mg/mg", referencia="abaixo de 0,2 mg/mg",
                   alterado=True),
                op("Ureia", resultado="46 mg/dL", referencia="até 45 mg/dL",
                   alterado=True),
                op("Potássio", resultado="4,4 mEq/L",
                   referencia="3,5 a 5,0 mEq/L"),
                op("Ácido úrico", resultado="6,8 mg/dL",
                   referencia="até 7,0 mg/dL"),
            ]),
            grupo("Imagem", "pulmao", [
                op("Radiografia de tórax",
                   resultado="Sem alterações", referencia="normal"),
                op("Tomografia de seios da face"),
                op("Ultrassonografia de rins e vias urinárias"),
                op("Eletrocardiograma"),
                op("Espirometria",
                   resultado="Capacidade vital forçada 88% do previsto · "
                             "VEF1/CVF 0,79 · sem resposta a broncodilatador",
                   referencia="normal"),
            ]),
        ],
        fundo=CENA, banco=BANCO, limite=4,
    ),

    resultados("res_amb", "O que voltou do ambulatório",
        "Os exames que você pediu", "ex_amb",
        introducao="Só o que foi marcado. Estamos oito semanas depois do "
                   "início e seis semanas antes da internação. Clique na "
                   "imagem para ampliar; o laudo abre no botão.",
        fundo=CENA,
        laminas={
            "Radiografia de tórax": lamina(RX_NORMAL,
                "Radiografia de tórax, póstero-anterior",
                "Imagem ilustrativa de licença aberta; não pertence a este "
                "paciente.",
                "Mikael Häggström · Wikimedia Commons · CC0"),
            "Tomografia de seios da face": lamina(TC_SEIOS,
                "Tomografia de seios da face, plano coronal",
                "Imagem ilustrativa de licença aberta; não pertence a este "
                "paciente.",
                "Mikael Häggström · Wikimedia Commons · CC BY 4.0"),
        },
    ),

    pergunta("p2", "Pergunta 3",
        "Creatinina de 1,4 mg/dL hoje — referência do laboratório até 1,3 — e "
        "1,0 mg/dL há dois meses. **Quais três** afirmações essa comparação "
        "autoriza?",
        [
            alt("Está pouco acima da referência e muito acima do que era dele",
                "1,4 contra um teto de 1,3 é um laudo que quase não chama "
                "atenção. Contra os 1,0 dele, é outra coisa: a referência é "
                "populacional, e o paciente é a referência dele mesmo.",
                certa=True),
            alt("A lesão está no glomérulo",
                "Nada aqui localiza o compartimento. Creatinina não distingue "
                "pré-renal, glomerular, tubular ou obstrutivo — quem faz isso "
                "é o sedimento."),
            alt("A lesão é aguda ou subaguda, e portanto investigável",
                "É a consequência prática: doença que se instalou em semanas "
                "tem causa procurável e janela de tratamento.", certa=True),
            alt("Perda de cerca de um terço da filtração glomerular",
                "Por CKD-EPI 2021, um homem de 63 anos sai de cerca de 80 para "
                "cerca de 53 mL/min/1,73 m² com essa mudança.", certa=True),
            alt("Trata-se de doença renal crônica estágio 2",
                "Crônico exige alteração mantida por mais de três meses. Dois "
                "valores separados por dois meses, diferentes entre si, são o "
                "oposto disso."),
            alt("O achado é efeito esperado da losartana",
                "Bloqueador do receptor eleva a creatinina nas primeiras "
                "semanas de uso — e ele usa losartana há dez anos."),
            alt("Há indicação de diálise",
                "Nenhum critério de urgência está presente, e a creatinina "
                "sozinha nunca foi indicação."),
        ],
        titulo_resposta="É a comparação, não o valor",
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

    pagina("evolucao_c", "Na última semana", "A última semana",
        p("Nos sete dias que antecederam a internação, a esposa notou que a "
          "urina dele estava escura, cor de refrigerante, e que ele deixou de "
          "levantar à noite para urinar, o que fazia duas vezes por noite há "
          "anos. Ele não deu importância e não procurou atendimento por isso."),
        p("**Nos últimos três dias**, a falta de ar progrediu de esforços "
          "grandes para esforços mínimos e depois para o repouso. Na manhã da "
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
                 "mucosa friável que sangra ao toque. Sem perfuração septal, "
                 "deformidade em sela ou massa. Orofaringe sem lesões. Sem "
                 "linfonodomegalia."),
                ("Cardiovascular",
                 "Bulhas rítmicas, sem sopros. **Sem estase jugular a 45°.** "
                 "Pulsos amplos e simétricos."),
                ("Respiratório",
                 "Crepitações finas difusas nos dois hemitórax, da base ao "
                 "terço médio. Sem sibilos e sem atrito pleural."),
            ),
            corpo([("via", ""), ("pulmao", "")], altura=300, so_marcas=True), colunas=2),
        fundo=CENA, so_kicker=True),
    pagina("exame_complementar", "Exame físico", "Pele, membros e exame neurológico",
        grade(
            topicos(
                ("Abdome",
                 "Flácido, indolor, sem massas ou visceromegalias. "
                 "Punho-percussão lombar indolor."),
                ("Membros inferiores",
                 "**Sem edema.** Sem empastamento de panturrilha, sem sinais "
                 "de trombose. Pulsos pediosos e tibiais posteriores "
                 "palpáveis."),
                ("Pele",
                 "Lesões arredondadas, elevadas e purpúricas na face anterior "
                 "de ambas as pernas e no dorso dos pés, algumas com centro "
                 "escurecido, **que não desaparecem à digitopressão**. Sem "
                 "lesão em polpa digital, sem hemorragia subungueal."),
                ("Neurológico",
                 "Força 2/5 para dorsiflexão do pé **direito**, com pé caído "
                 "à marcha. Hipoestesia ulnar à **esquerda**. Assimétrico, sem "
                 "nível sensitivo e sem raiz única. Reflexo aquileu direito "
                 "abolido."),
            ),
            corpo([("pele", ""), ("nervo", "")], altura=320, so_marcas=True), colunas=2),
        fundo=CENA),

    pergunta("p3", "Pergunta 4",
        "Primeiras duas horas de pronto-socorro. A hipótese de trabalho é "
        "pneumonia grave, e a creatinina está em 3,8 mg/dL. **Quais três** "
        "condutas?",
        [
            alt("Sedimento urinário em urina fresca",
                "É o exame mais barato do caso e o único que localiza a lesão "
                "renal em minutos. Fresco, porque cilindro se desfaz.",
                certa=True),
            alt("Iniciar antibiótico empírico sem esperar resultado",
                "A suspeita de infecção grave é legítima com estes dados, e a "
                "distância entre colher e infundir é de minutos, não de "
                "horas.", certa=True),
            alt("Anticoagulação plena empírica",
                "Sem suspeita estabelecida de tromboembolismo, e num paciente "
                "que já sangra por alguma via não identificada."),
            alt("Tomografia antes de qualquer antibiótico",
                "Inverte a ordem de risco com saturação de 88%. A tomografia "
                "descreve o padrão; ela não exclui infecção."),
            alt("Colher hemoculturas antes da primeira dose",
                "Cultura colhida depois do antibiótico deixa de valer — e é "
                "ela que vai autorizar imunossuprimir dentro de poucos dias.",
                certa=True),
            alt("Hemodiálise de urgência",
                "Sem hipercalemia com repercussão, sem acidose refratária, sem "
                "congestão e sem sintoma urêmico. Creatinina alta sozinha não "
                "indica."),
            alt("Furosemida pelo infiltrado bilateral",
                "Não há congestão documentada: jugular vazia, sem terceira "
                "bulha, sem edema. Diurético aqui deplete um paciente já "
                "oligúrico e sobe a creatinina."),
            alt("Corticoide em dose imunossupressora",
                "A decisão mais perigosa da lista. Imunossuprimir com culturas "
                "em andamento transforma endocardite em desfecho que não se "
                "recupera."),
        ],
        titulo_resposta="Cultura, depois antibiótico — e a distância é de minutos",
        fundo=TC,
    ),

    pedido("ex_adm", "Pergunta 5",
        "Que exames você pede agora?",
        "Pronto-socorro, com a hipótese de infecção grave em curso. **Seis "
        "vagas.** De novo: o que não for pedido não volta.",
        [
            grupo("Bancada, em minutos", "rim", [
                op("Creatinina",
                   resultado="3,8 mg/dL {{(1,4 há seis semanas)}}",
                   referencia="até 1,3 mg/dL", alterado=True),
                op("Taxa de filtração glomerular estimada",
                   resultado="17 mL/min/1,73 m²",
                   referencia="acima de 90 mL/min/1,73 m²", alterado=True),
                op("Potássio", resultado="5,4 mEq/L",
                   referencia="3,5 a 5,0 mEq/L", alterado=True),
                op("Sedimento urinário"),
                op("Ultrassonografia de rins e vias urinárias"),
            ]),
            grupo("Sangue e gasometria", "sangue", [
                op("Hemoglobina", resultado="7,8 g/dL {{(11,2 há seis semanas)}}",
                   referencia="13,5 a 17,5 g/dL", alterado=True),
                op("Leucócitos", resultado="14.200/mm³",
                   referencia="4.000 a 11.000/mm³", alterado=True),
                op("Reticulócitos"),
                op("pH arterial"),
                op("Relação PaO2/FiO2"),
                op("Proteína C reativa", resultado="186 mg/L",
                   referencia="até 5 mg/L", alterado=True),
                op("Procalcitonina", resultado="0,4 ng/mL",
                   referencia="abaixo de 0,5 ng/mL"),
                op("Neutrófilos", resultado="11.800/mm³",
                   referencia="1.800 a 7.000/mm³", alterado=True),
                op("Plaquetas", resultado="468.000/mm³",
                   referencia="150.000 a 450.000/mm³", alterado=True),
                op("Esfregaço de sangue periférico"),
                op("Lactato"),
                op("Bicarbonato"),
                op("Albumina", resultado="2,9 g/dL",
                   referencia="3,5 a 5,2 g/dL", alterado=True),
                op("TAP / INR"),
                op("D-dímero"),
            ]),
            grupo("Imagem do tórax", "pulmao", [
                op("Radiografia de tórax"),
                op("Tomografia de tórax"),
                op("Ecocardiograma transtorácico"),
                op("Angiotomografia de tórax"),
                op("Eletrocardiograma"),
            ]),
            grupo("Infecção", "geral", [
                op("Hemocultura",
                   resultado="Em andamento — coletada antes da primeira dose",
                   referencia="negativa"),
                op("Urocultura"),
                op("Anti-HIV"),
                op("HBsAg e anti-HBc"),
                op("Anti-HCV"),
                op("Baciloscopia e teste molecular para tuberculose"),
            ]),
        ],
        fundo=TC, banco=BANCO, limite=6,
    ),

    resultados("res_adm", "O que voltou", "A investigação da admissão", "ex_adm",
        introducao="Só o que foi marcado. Clique em qualquer figura para "
                   "ampliá-la na tela inteira.",
        fundo=TC,
        laminas={
            "Radiografia de tórax": lamina(RX, "Radiografia de tórax",
                "Opacidades alveolares bilaterais, em mancha, predominando nos "
                "campos médios e inferiores. Imagem ilustrativa: o padrão "
                "alveolar não distingue sangue de água ou de pus.",
                "Samir · Wikimedia Commons · CC BY-SA 3.0"),
            "Tomografia de tórax": lamina(TC, "Tomografia de tórax",
                "Três cortes axiais, um coronal e um sagital, em janela de "
                "pulmão. Vidro fosco difuso e bilateral. Imagem ilustrativa — "
                "e vidro fosco é ainda menos específico que a opacidade "
                "alveolar do filme: cabe sangue, água, pus, células e "
                "proteína. Janela de mediastino não incluída; linfonodo não é "
                "avaliável aqui.",
                "Hellerhoff · Wikimedia Commons · CC BY-SA 4.0"),
            "Ultrassonografia de rins e vias urinárias": lamina(US,
                "Ultrassonografia renal",
                "Rim de ecotextura normal, com diferenciação córtico-medular "
                "preservada e sem hidronefrose. Imagem ilustrativa; o tamanho "
                "vem do laudo, não desta figura. Os asteriscos são do autor da "
                "fonte — * coluna de Bertin, ** pirâmide, *** córtex, "
                "**** seio renal — e a linha pontilhada é o cursor de medida "
                "dele, sem valor associado.",
                "Hansen, Nielsen e Ewertsen · Wikimedia Commons · CC BY 4.0"),
            "Ecocardiograma transtorácico": lamina(ECO,
                "Ecocardiograma transtorácico, quatro câmaras",
                "Imagem ilustrativa de licença aberta; não pertence a este "
                "paciente.",
                "Wikimedia Commons · domínio público"),
            "Esfregaço de sangue periférico": lamina(ESFREGACO,
                "Esfregaço de sangue periférico",
                "Coloração de Wright. Imagem ilustrativa de licença aberta; "
                "não pertence a este paciente.",
                "Ajay Kumar Chaurasiya · Wikimedia Commons · CC BY-SA 4.0"),
            "Sedimento urinário": lamina(EAS, "Sedimento urinário",
                "Cilindro urinário: estrutura alongada, de bordas paralelas, "
                "que é o molde do lúmen do túbulo. Imagem ilustrativa, em "
                "preparação corada.",
                "Rian Kabir · Wikimedia Commons · CC BY 2.0"),
        },
    ),

    pagina("leitura_infeccao", "Discussão", "A conduta inicial",
        p("Com febre, infiltrado bilateral, proteína C reativa de 186 mg/L e "
          "insuficiência respiratória, a equipe assumiu pneumonia grave com "
          "lesão renal aguda de causa mista — sepse e hipoperfusão — e iniciou "
          "**ceftriaxona e azitromicina** depois de colher as culturas."),
        tabela(["O que sustenta a leitura de infecção",
                "O que já não se encaixa nela"], [
            ["Febre, taquipneia, infiltrado bilateral e proteína C reativa "
             "muito elevada",
             "Oito semanas de doença de via aérea superior que não respondeu a "
             "dois antibióticos"],
            ["Lesão renal aguda é comum na sepse, por hipoperfusão e por "
             "necrose tubular",
             "A creatinina já estava subindo seis semanas antes, sem febre e "
             "sem hipotensão"],
            ["Ele é ex-tabagista de 30 anos-maço, com fator de risco para "
             "pneumonia",
             "Púrpura palpável e pé caído não pertencem a pneumonia "
             "comunitária"],
        ]),

        fundo=TC,
    ),

    # ══════════════════════ ATO III — a virada ══════════════════════

    pagina("dia2", "Segundo dia de internação", "A evolução das últimas 36 horas",
        p("Trinta e seis horas depois da primeira dose, a saturação caiu para "
          "89% com cateter nasal a 4 L/min e foi preciso subir para máscara "
          "com reservatório a 10 L/min. A frequência respiratória subiu para "
          "32. Ele expectorou mais duas vezes sangue vivo, cerca de 30 mL cada."),
        p("A hemoglobina, que era 7,8 g/dL na admissão, está em **6,9 g/dL**, "
          "sem sangramento visível por qualquer outra via: sem melena, sem "
          "hematêmese, sem sangramento nasal volumoso nesta internação. A "
          "creatinina subiu para 4,1 mg/dL e o débito urinário das últimas 24 "
          "horas foi de 620 mL."),

        fundo=TC,
    ),

    pagina("imagem_alveolo", "Discussão visual", "Alvéolo e capilares",
        p("Observe a relação entre espaço aéreo e leito capilar. Em que compartimentos podem se acumular líquido, sangue ou células? A opacidade radiológica consegue distinguir sozinha esses materiais?"),
        '<details class="leitura"><summary>Revelar pontos de discussão</summary><p>O mesmo compartimento alveolar pode ser ocupado por materiais diferentes. A imagem do tórax precisa ser integrada à evolução clínica, à hemoglobina e aos exames dirigidos. O desenho apresenta anatomia normal, sem estabelecer o mecanismo deste paciente.</p></details>',
        fundo=CENA,lamina_=lamina("alveolo.svg", "Alvéolo", "Anatomia normal para discussão; não é exame do paciente.", "LadyofHats · Wikimedia Commons · domínio público · sem alterações.")),
    pergunta("p4", "Pergunta 6",
        "Ele piorou sob antibiótico adequado. **Quais quatro** achados deste "
        "paciente sustentam hemorragia alveolar difusa?",
        [
            alt("Derrame pleural",
                "A hemorragia alveolar é intraparenquimatosa e não produz "
                "derrame. A radiografia dele, aliás, não mostra nenhum."),
            alt("Nódulos escavados",
                "Sugerem doença granulomatosa ou embolia séptica, e não "
                "aparecem na tomografia dele."),
            alt("Escarro purulento",
                "Aponta para infecção das vias aéreas. Ele nunca teve — a "
                "expectoração é sanguinolenta, não purulenta."),
            alt("Queda de hemoglobina desproporcional ao volume expectorado",
                "É o achado mais específico da lista. Cerca de 160 mL "
                "expectorados não derrubam a hemoglobina em 7 g/dL: o sangue "
                "ficou no espaço aéreo.", certa=True),
            alt("Hemoptise",
                "Sustenta, e é o achado menos confiável da lista: **falta em "
                "cerca de um terço das hemorragias alveolares**, porque o "
                "sangue não precisa sair pela boca.", certa=True),
            alt("Relação PaO₂/FiO₂ reduzida",
                "Alvéolo cheio de sangue é alvéolo perfundido e não ventilado "
                "— shunt verdadeiro, que responde mal ao oxigênio.",
                certa=True),
            alt("Sibilos difusos",
                "Doença de via aérea, não de espaço alveolar. A ausculta dele "
                "tem crepitação fina, sem sibilo."),
            alt("Infiltrado alveolar bilateral",
                "Compatível, e inespecífico: cabe sangue, água, pus, células "
                "ou proteína. Sustenta sem provar.", certa=True),
        ],
        titulo_resposta="A hemoglobina que sumiu diz onde o sangue ficou",
        fundo=TC,
    ),

    bifurcacao("b_dia2", "Decisão",
        "Ele piorou sob antibiótico adequado. O que você faz agora?",
        "Trinta e seis horas de ceftriaxona, mais oxigênio, mais hemoptise e "
        "0,9 g/dL a menos de hemoglobina. As culturas ainda não voltaram.",
        [
            caminho("Escalonar o antibiótico para carbapenêmico e vancomicina",
                    "r_escalona",
                    "É a leitura de que o espectro foi insuficiente, e ela tem "
                    "lógica: germe resistente existe. Mas trinta e seis horas é "
                    "cedo para declarar falha numa pneumonia comunitária, e "
                    "antibiótico mais largo não retém sangue no alvéolo."),
            caminho("Investigar a hemorragia alveolar antes de mudar o "
                    "tratamento", "r_investiga",
                    "Broncoscopia com lavado responde à pergunta que a "
                    "aritmética levantou — de onde vem o sangue — e a cultura "
                    "do lavado responde à que sobrou da infecção. Não atrasa "
                    "nada: o antibiótico continua correndo enquanto isso."),
            caminho("Iniciar corticoide em dose imunossupressora agora",
                    "r_corticoide",
                    "A hemorragia alveolar é uma emergência e o corticoide é o "
                    "que a para. O preço é o momento: as culturas ainda estão "
                    "em curso, e nenhum material foi colhido antes."),
        ],
        fundo=TC,
    ),

    pagina("r_escalona", "Terceiro e quarto dias", "Sob o esquema ampliado",
        p("Meropeném e vancomicina correram por 48 horas. A saturação caiu "
          "para 91% em máscara com reservatório a 12 L/min e a hemoglobina "
          "está em **6,3 g/dL**, com nova hemoptise de cerca de 40 mL. A "
          "creatinina subiu para 4,9 mg/dL e a diurese caiu para 380 mL."),
        p("As três hemoculturas da admissão vieram negativas em 48 horas. A "
          "urocultura, negativa."),
        fundo=TC, segue="ex_mec",
    ),

    pagina("r_investiga", "Terceiro dia", "A broncoscopia",
        p("Broncoscopia à beira do leito, sob oxigênio a 100%. Árvore "
          "brônquica sem lesão endobrônquica e sem ponto de sangramento "
          "identificável: **sangue difuso escorrendo dos óstios segmentares "
          "dos dois pulmões.**"),
        p("Lavado em três alíquotas de 60 mL no mesmo segmento: a primeira "
          "rosada, a segunda vermelha, a terceira **francamente hemorrágica**. "
          "Material enviado para citologia e cultura."),
        fundo=TC, segue="ex_mec",
    ),

    pagina("r_corticoide", "Terceiro e quarto dias", "Sob corticoide",
        p("Metilprednisolona 500 mg ao dia. Em 48 horas a hemoptise cessou e a "
          "saturação subiu para 95% em cateter a 4 L/min. A hemoglobina "
          "estabilizou em 6,9 g/dL e a creatinina parou de subir, em 4,6."),
        p("As hemoculturas da admissão vieram negativas em 48 horas. **A "
          "partir de agora, toda cultura que vier negativa terá sido colhida "
          "sob imunossupressão** — e o valor dela é menor."),
        fundo=TC, segue="ex_mec",
    ),

    pedido("ex_mec", "Pergunta 7",
        "O que você pede agora?",
        "Origem do sangramento alveolar, compartimento da lesão renal e "
        "mecanismo. **Seis vagas.**",
        [
            grupo("Autoanticorpos", "sangue", [
                op("ANCA por imunofluorescência indireta"),
                op("Anti-mieloperoxidase"),
                op("Anti-proteinase 3"),
                op("Anticorpo anti-membrana basal glomerular"),
                op("Anti-DNA nativo"),
                op("Anti-ENA"),
                op("Fator reumatoide"),
            ]),
            grupo("Complemento e proteínas", "nervo", [
                op("Complemento C3"),
                op("Complemento C4"),
                op("Crioglobulinas"),
                op("Eletroforese de proteínas"),
                op("Imunoglobulinas séricas"),
            ]),
            grupo("Sorologias", "via", [
                op("Anti-HCV"),
                op("Sorologia para sífilis"),
                op("Anti-HIV"),
                op("HBsAg e anti-HBc"),
            ]),
            grupo("Sangue, outros", "pele", [
                op("Ferritina"),
                op("VHS"),
                op("D-dímero"),
                op("Coombs direto"),
                op("Anticorpos antifosfolípides"),
            ]),
            grupo("Via aérea", "pulmao", [
                op("Lavado broncoalveolar"),
                op("Cultura do lavado broncoalveolar"),
                op("Pesquisa de Pneumocystis no lavado"),
                op("Baciloscopia e teste molecular para tuberculose"),
                op("Galactomanana e beta-D-glucana"),
            ]),
            grupo("Tecido", "rim", [
                op("Biópsia renal",
                   exige=["Sedimento urinário",
                          "Ultrassonografia de rins e vias urinárias"],
                   porque="a nefrologia não punciona um rim sem sedimento que "
                          "localize a lesão e sem imagem que confirme dois "
                          "rins, tamanho e ausência de obstrução",
                   resultado="**Microscopia óptica:** 24 glomérulos · "
                             "crescentes celulares em 15 deles (62%) · necrose "
                             "fibrinoide segmentar · sem esclerose global "
                             "significativa · fibrose intersticial em 10% do "
                             "córtex · **Imunofluorescência:** ausência de "
                             "depósitos significativos de IgG, IgA, IgM, C3 e "
                             "C1q — **padrão pauci-imune** · sem depósito "
                             "linear · **Berden:** classe crescêntica",
                   referencia="sem proliferação extracapilar, sem depósitos",
                   alterado=True),
            ]),
            grupo("Urina", "geral", [
                op("Sedimento urinário"),
                op("Proteinúria de 24 horas"),
                op("Relação proteína/creatinina urinária"),
                op("Eosinofilúria"),
                op("Urocultura"),
            ]),
            grupo("Imagem e outros", "geral", [
                op("Ultrassonografia de rins e vias urinárias"),
                op("Tomografia de seios da face"),
                op("Ecocardiograma transtorácico"),
                op("Eletroneuromiografia"),
            ]),
        ],
        fundo=BIOPSIA, banco=BANCO, limite=6,
    ),

    resultados("res_mec", "O que voltou", "A segunda rodada", "ex_mec",
        introducao="De novo, só o que foi marcado.",
        fundo=BIOPSIA,
        laminas={
            "Tomografia de seios da face": lamina(TC_SEIOS,
                "Tomografia de seios da face, plano coronal",
                "Imagem ilustrativa de licença aberta; não pertence a este "
                "paciente.",
                "Mikael Häggström · Wikimedia Commons · CC BY 4.0"),
            "Biópsia renal": lamina(BIOPSIA,
                "Biópsia renal, córtex em pequeno aumento",
                "Coloração de PAS: glomérulos, túbulos e interstício. Imagem "
                "ilustrativa de licença aberta; a morfologia da crescente "
                "aparece na página seguinte, em grande aumento.",
                "Nephron · Wikimedia Commons · CC BY-SA 3.0"),
            "Sedimento urinário": lamina(EAS, "Sedimento urinário",
                "Cilindro urinário em preparação corada. Imagem ilustrativa "
                "de licença aberta.",
                "Rian Kabir · Wikimedia Commons · CC BY 2.0"),
            "ANCA por imunofluorescência indireta": lamina(IF,
                "Imunofluorescência indireta sobre neutrófilos",
                "A fluorescência acompanha o contorno dos lóbulos do núcleo e "
                "poupa o citoplasma: é o **padrão perinuclear**. Neutrófilos "
                "fixados em etanol — a fixação importa, porque é ela que "
                "produz este padrão. Imagem ilustrativa. A imunofluorescência "
                "indireta devolve padrão e título, nunca um valor em U/mL.",
                "Simon Caulton · Wikimedia Commons · CC BY-SA 3.0"),
        },
    ),

    pagina("virada", "Quinto dia de internação", "As culturas",
        p("**As três hemoculturas colhidas antes do antibiótico vieram "
          "negativas em cinco dias.** A urocultura é negativa. O antibiótico "
          "está no quinto dia e ele não melhorou: continua em máscara com "
          "reservatório, com creatinina de 4,6 mg/dL e débito urinário de "
          "480 mL nas últimas 24 horas."),
        p("Quem pediu o lavado broncoalveolar tem, além disso, a informação "
          "que fecha a questão do pulmão. Quem não pediu segue sem ela — e a "
          "decisão do próximo passo terá de ser tomada assim."),

        fundo=TC,
    ),

    pergunta("p5", "Pergunta 8",
        "Hemorragia alveolar difusa e glomerulonefrite, no mesmo paciente e no "
        "mesmo mês. **Quais cinco** das condições abaixo produzem esse par?",
        [
            alt("Tromboembolismo pulmonar com nefropatia por contraste",
                "Dois órgãos por duas vias. Mas infarto pulmonar não sangra "
                "difusamente, e o contraste viria depois do exame."),
            alt("Pneumonia comunitária grave com necrose tubular aguda",
                "A hipótese com que toda equipe começa. Não fecha no "
                "sedimento: necrose tubular não dá hemácia dismórfica."),
            alt("Lúpus eritematoso sistêmico",
                "Nefrite proliferativa e, numa minoria, hemorragia alveolar — "
                "a apresentação lúpica de maior mortalidade.", certa=True),
            alt("Doença anti-membrana basal glomerular",
                "Anticorpo contra o colágeno tipo IV, que existe no alvéolo e "
                "no glomérulo. A mais urgente das cinco.", certa=True),
            alt("Endocardite infecciosa",
                "Glomerulonefrite por imunocomplexo mais embolia séptica. É "
                "ela que contraindica a imunossupressão das outras quatro.",
                certa=True),
            alt("Púrpura trombocitopênica trombótica",
                "Lesa rim e pulmão por microtrombo, não por sangramento "
                "alveolar. Exigiria esquizócitos e plaquetopenia."),
            alt("Crioglobulinemia mista",
                "Imunocomplexo no vaso de pequeno calibre: glomerulonefrite "
                "membranoproliferativa e capilarite. Consome C4.", certa=True),
            alt("Leptospirose ictero-hemorrágica",
                "**O distrator mais honesto da lista.** Faz hemorragia "
                "alveolar e insuficiência renal, mas a lesão renal é "
                "tubulointersticial: não dá cilindro hemático."),
            alt("Vasculite de pequenos vasos associada ao ANCA",
                "Acomete capilar alveolar e capilar glomerular pelo mesmo "
                "mecanismo. É a causa mais frequente da síndrome em adultos.",
                certa=True),
            alt("Síndrome cardiorrenal tipo 1",
                "Congestão dá infiltrado bilateral, não hemoptise com queda "
                "de hemoglobina. Exigiria disfunção cardíaca aguda."),
        ],
        titulo_resposta="Cinco mecanismos, e um deles proíbe o tratamento dos outros quatro",
        fundo=TC,
    ),

    pagina("diferencial", "Discussão", "O diferencial da síndrome pulmão-rim",
        p("Síndrome pulmão-rim não é diagnóstico: é um endereço com pelo menos "
          "quatro inquilinos. Agrupar por **mecanismo** — e não por nome de "
          "doença — é o que permite podar com o dado que já se tem."),
        tabela(["Mecanismo", "Quem mora nele", "O que decide"], [
            ["Anticorpo contra a membrana basal",
             "Doença anti-MBG (Goodpasture)",
             "Anticorpo circulante e **depósito linear** de IgG na "
             "imunofluorescência do tecido. É a mais urgente das quatro: perde "
             "rim em dias e o tratamento é diferente"],
            ["Deposição de imunocomplexo",
             "Lúpus, crioglobulinemia, vasculite por IgA, pós-infecciosa",
             "**Depósito granular** na imunofluorescência; complemento "
             "consumido em boa parte delas; sorologia específica"],
            ["Pauci-imune",
             "As vasculites de pequenos vasos associadas ao ANCA",
             "**Ausência de depósito** na imunofluorescência, com ANCA "
             "circulante na maioria"],
            ["Duas vias separadas, não uma doença",
             "Endocardite, leptospirose, sepse com síndrome do desconforto "
             "respiratório e necrose tubular, intoxicação",
             "Hemocultura, ecocardiograma, epidemiologia e a resposta ao "
             "tratamento da infecção"],
        ]),

        fundo=BIOPSIA,
        rota={"pediu": ["Biópsia renal", "ANCA por imunofluorescência indireta"],
              "entao": "crescente", "senao": "sem_prova"},
    ),

    # ─────────────── rota A: o tecido e o anticorpo foram pedidos ───────────

    pagina("crescente", "Discussão visual", "Corpúsculo renal",
        p("Antes de interpretar a microfotografia, localize a cápsula, o espaço urinário e o tufo capilar neste esquema. O que significa uma proliferação ocorrer fora do tufo?"),
        '<details class="leitura"><summary>Revelar pontos de discussão</summary><p>O espaço de Bowman está entre o tufo e o epitélio parietal da cápsula. Uma crescente ocupa esse espaço. O esquema normal orienta a leitura da microfotografia seguinte, mas não demonstra lesão ou proporção de glomérulos afetados.</p></details>',
        fundo=CENA,lamina_=lamina("corpusculo.svg", "Corpúsculo renal", "Esquema anatômico normal.", "Michał Komorniczak · Wikimedia Commons · CC BY-SA 3.0 · sem alterações.")),
    pagina("crescente_histologia", "Discussão", "A biópsia renal",
        grade(
            anotada(IMG / CRESCENTE,
                seta((795, 285), (612, 66), "Tufo capilar", curva=14),
                seta((432, 292), (24, 150), "Cápsula de Bowman", curva=20),
                seta((505, 362), (24, 536),
                     "Crescente celular, no espaço de Bowman", curva=-26),
                # o distrator: no canto inferior esquerdo há um glomérulo
                # globalmente esclerosado, e o halo claro em volta dele parece
                # uma crescente para quem está aprendendo
                seta((398, 548), (168, 650),
                     "Glomérulo esclerosado — não é crescente", curva=10),
                titulo="Glomérulo com crescente celular · PAS, grande aumento",
                legenda="As quatro setas são leitura editorial deste caso, não "
                        "do autor da imagem. Lâmina ilustrativa, de "
                        "repositório aberto; não pertence a este paciente.",
                credito="Nephron · Wikimedia Commons · CC BY-SA 3.0"),
            p("**Crescentes celulares em 15 dos 24 glomérulos**, com necrose "
              "fibrinoide segmentar, e imunofluorescência **sem depósitos "
              "significativos**.")
            + quadro("O que é uma crescente, e por que a palavra celular importa",
                p("Crescente é proliferação de células **fora do tufo**, dentro "
                  "do espaço de Bowman: epitélio parietal, monócitos e fibrina "
                  "que escaparam por uma ruptura da parede capilar. Ela "
                  "comprime o tufo e obstrui a saída do filtrado. **Celular** "
                  "quer dizer tecido inflamado, que ainda responde; "
                  "**fibrosa** quer dizer colágeno, que não responde. A "
                  "transição corre ao longo de semanas — não de meses, e não "
                  "de horas — e é isso que dá urgência ao tratamento sem "
                  "torná-lo emergência de minutos."),
                sistema="rim"),
        ),
        fundo=BIOPSIA,
    ),

    pergunta("p6", "Pergunta 9",
        "A imunofluorescência da biópsia renal não mostra depósito imune. "
        "**Quais cinco** mecanismos esse achado torna improváveis?",
        [
            alt("Vasculite de pequenos vasos associada ao ANCA",
                "É justamente a que sobra: o padrão sem depósito **é** o dela, "
                "e por isso se chama pauci-imune."),
            alt("Nefrite lúpica",
                "Doença por imunocomplexo, com imunofluorescência exuberante — "
                "o //full house//, com IgG, IgA, IgM, C3 e C1q.", certa=True),
            alt("Nefroesclerose hipertensiva",
                "Lesão vascular crônica, sem depósito imune por definição — a "
                "imunofluorescência nunca a excluiu nem a confirmou."),
            alt("Necrose tubular aguda",
                "Não é doença glomerular. A imunofluorescência do glomérulo "
                "não fala dela, nem a favor nem contra."),
            alt("Nefropatia por IgA",
                "Definida pelo depósito mesangial de IgA. Sem depósito, não "
                "existe.", certa=True),
            alt("Glomerulonefrite pós-infecciosa",
                "Imunocomplexo com depósito granular grosseiro e C3 "
                "abundante.", certa=True),
            alt("Crioglobulinemia mista",
                "Deposição de imunocomplexo com padrão granular e consumo de "
                "complemento, sobretudo C4.", certa=True),
            alt("Doença anti-membrana basal glomerular",
                "Produz depósito **linear** e contínuo de IgG desde o começo. "
                "Ausência de depósito é o oposto do que ela faz.", certa=True),
        ],
        titulo_resposta="Exame sem depósito não é exame negativo",
        fundo=BIOPSIA,
    ),

    pagina("fenotipo", "Discussão", "Os dois fenótipos",
        p("Vasculite de pequenos vasos associada ao ANCA está estabelecida: "
          "tecido pauci-imune e anticorpo circulante. **Qual delas** é uma "
          "questão de fenótipo — e o fenótipo deste paciente tem uma peça "
          "ambígua."),
        tabela(["", "Poliangeíte microscópica", "Granulomatose com poliangeíte"], [
            ["Sorologia típica", "Anti-MPO, padrão perinuclear",
             "Anti-PR3, padrão citoplasmático"],
            ["Via aérea superior", "Ausente ou leve",
             "Destrutiva: perfuração septal, deformidade em sela"],
            ["Granuloma", "Ausente",
             "Esperado na via aérea e no pulmão; quase nunca no rim"],
            ["Granuloma no rim", "Ausente",
             "Ausente também aqui: Bajema e cols. //(Clin Nephrol. "
             "1997;48:16-21)// acharam granuloma renal em 16 de 157 biópsias "
             "de vasculite sistêmica"],
            ["Neste paciente", "Compatível",
             "Improvável — mas não pela biópsia renal: pesam o anticorpo e a "
             "ausência de lesão destrutiva"],
        ]),

        fundo=IF, segue="b1",
    ),

    # ─────────────── rota B: faltou prova, e o caso segue assim ─────────────

    pagina("sem_prova", "Discussão", "O que não foi pedido",
        p("As duas provas que separam os três mecanismos da tabela anterior "
          "são a **imunofluorescência do tecido renal** — que distingue "
          "depósito linear, depósito granular e ausência de depósito — e o "
          "**anticorpo circulante**. Pelo menos uma delas não foi pedida, e "
          "por isso não está aqui."),
        p("Isso não interrompe o caso, porque não interromperia o paciente. "
          "Ele continua sangrando no alvéolo, com creatinina de 4,6 e diurese "
          "caindo, e alguém vai ter de decidir se imunossuprime hoje. O que "
          "muda é o que se pode afirmar em voz alta na passagem de plantão."),
        tabela(["O que continua de pé", "O que fica sem lastro"], [
            ["Hemorragia alveolar difusa e lesão renal aguda coexistindo, com "
             "cinco territórios acometidos",
             "Que o mecanismo seja pauci-imune, e não imunocomplexo ou "
             "anti-membrana basal"],
            ["Que não houve resposta a cinco dias de antibiótico adequado, com "
             "culturas negativas colhidas antes da primeira dose",
             "Qual doença específica tratar — e, portanto, se o esquema "
             "escolhido é o certo"],
            ["Que esperar tem custo: crescente celular vira fibrosa ao longo "
             "de semanas, e o que virou não volta",
             "A gravidade histológica, que é o que mais prediz função renal "
             "residual e orienta a intensidade do tratamento"],
        ]),

        fundo=BIOPSIA,
    ),

    pergunta("p6b", "Pergunta 9",
        "Sem o tecido e sem o anticorpo, com creatinina de 4,6 e alvéolo "
        "sangrando. **Quais três** condutas?",
        [
            alt("Iniciar o glicocorticoide sem esperar o resultado",
                "Colhido o material, ele entra: a janela em que a crescente "
                "ainda responde é de dias, e o resultado leva o mesmo tempo.",
                certa=True),
            alt("Ciclofosfamida empírica, pela gravidade",
                "A gravidade justifica a pressa, não a escolha da segunda "
                "droga sem diagnóstico e sem infecção afastada."),
            alt("Confirmar que há cultura negativa antes de imunossuprimir",
                "É o que separa tratar vasculite de tratar uma infecção com "
                "corticoide. Sem isso, a decisão fica sem lastro.",
                certa=True),
            alt("Aguardar a estabilização clínica",
                "Parece prudente e custa o rim. Crescente celular vira fibrosa "
                "ao longo de semanas, e o que virou não volta."),
            alt("Troca plasmática empírica",
                "Cobre a hipótese anti-MBG e, na vasculite ANCA, não reduziu "
                "morte nem doença renal terminal no PEXIVAS."),
            alt("Escalonar o antibiótico",
                "É a leitura já feita três vezes com este paciente e que não "
                "respondeu nenhuma delas."),
            alt("Colher agora as duas provas que faltam",
                "O glicocorticoide não apaga o padrão da imunofluorescência "
                "nem o título do anticorpo — mas só se o material for colhido "
                "antes.", certa=True),
        ],
        titulo_resposta="Colher e começar o corticoide não é imunossuprimir a fundo",
        fundo=BIOPSIA, segue="b1",
    ),

    # ═══════════ ATO IV — o tratamento, e a segunda virada ═══════════

    bifurcacao("b1", "Pergunta 10",
        "Com que esquema você induz a remissão?",
        "Filtração glomerular estimada de 17 mL/min/1,73 m² por CKD-EPI 2021, "
        "78 kg, 63 anos, hemorragia alveolar em curso. O glicocorticoide é "
        "comum aos três caminhos; a segunda droga é a decisão.",
        [
            caminho("Rituximabe 375 mg/m² por semana, quatro doses",
                    "t_rituximabe",
                    "Não exige ajuste para a função renal, poupa gônada e tem "
                    "eficácia equivalente à ciclofosfamida na indução. O RAVE "
                    "mostrou não-inferioridade e superioridade na doença "
                    "recidivante — mas **excluiu creatinina acima de 4,0 "
                    "mg/dL**, e ele está em 4,6. Para filtração como a dele a "
                    "referência é o RITUXVAS, com filtração média de 18 "
                    "mL/min, que também não mostrou diferença; note que ali o "
                    "braço de rituximabe recebeu **dois pulsos de "
                    "ciclofosfamida** junto, e é uma folga do argumento. A "
                    "vantagem prática aqui é não depender de acertar uma "
                    "correção de dose."),
            caminho("Ciclofosfamida endovenosa com dose reduzida pela idade e "
                    "pela função renal", "t_cfx_ajustada",
                    "A redução vem do esquema do CYCLOPS, adotado pela EULAR: "
                    "parte de 15 mg/kg e subtrai **2,5 mg/kg entre 60 e 70 "
                    "anos** (5,0 acima de 70) e mais **2,5 mg/kg com "
                    "creatinina entre 300 e 500 µmol/L**. Aqui: 15 − 2,5 − 2,5 "
                    "= **10 mg/kg**, com teto de 1,2 g por pulso. É a conta "
                    "que mais se esquece de fazer, e é toda a diferença entre "
                    "este caminho e o seguinte."),
            caminho("Ciclofosfamida endovenosa em dose plena, 15 mg/kg",
                    "t_cfx_plena",
                    "A dose de indução sem as duas subtrações. Com filtração "
                    "de 17 mL/min ela produz exposição bem acima da "
                    "pretendida, porque os metabólitos ativos da "
                    "ciclofosfamida são eliminados por via renal. A "
                    "neutropenia que vem depois não é a esperada do esquema: "
                    "é a da dose."),
        ],
        fundo=CENA,
    ),

    pagina("t_rituximabe", "A prescrição", "O que foi prescrito — caminho A",
        p("**Rituximabe 375 mg/m², uma vez por semana, quatro doses.** "
          "Superfície corporal de 1,93 m² por Mosteller, com 78 kg e "
          "1,72 m: **725 mg** por dose. Sem correção para a função renal — "
          "o anticorpo monoclonal não é depurado pelo rim.")
        + quadro("O que este caminho pede de vigilância",
            p("Pré-medicação com anti-histamínico, paracetamol e o próprio "
              "glicocorticoide, pela reação infusional da primeira dose. "
              "Rastrear hepatite B **antes** — o anti-HBc isolado reativa "
              "sob rituximabe, e a reativação é grave. Imunoglobulinas "
              "séricas na linha de base, porque a hipogamaglobulinemia "
              "tardia é o efeito dos ciclos seguintes, não deste."),
            sistema="sangue"),
        fundo=CENA, segue="esquema",
    ),

    pagina("t_cfx_ajustada", "A prescrição", "O que foi prescrito — caminho B",
        p("**Ciclofosfamida endovenosa em pulso, 10 mg/kg.** A conta do "
          "CYCLOPS por extenso: 15 mg/kg de base; −2,5 mg/kg por idade "
          "entre 60 e 70 anos; −2,5 mg/kg por creatinina entre 300 e 500 "
          "µmol/L — os 3,8 mg/dL da admissão são **336 µmol/L**. Restam "
          "**10 mg/kg**. Com 78 kg, **780 mg** por pulso, abaixo do teto "
          "de 1,2 g. Pulsos nas semanas 0, 2 e 4, depois a cada três "
          "semanas.")
        + quadro("O que este caminho pede de vigilância",
            p("Mesna e hidratação em cada pulso, pela cistite hemorrágica "
              "da acroleína. Hemograma no sétimo e no décimo dia de cada "
              "pulso, que é onde cai o nadir; se os neutrófilos ficarem "
              "abaixo de 1.000/mm³, o pulso seguinte desce mais um "
              "degrau. E a conversa sobre fertilidade antes da primeira "
              "dose — que neste paciente, de 63 anos, pesa menos, mas não "
              "se pula por isso."),
            sistema="sangue"),
        fundo=CENA, segue="esquema",
    ),

    pagina("t_cfx_plena", "A prescrição", "O que foi prescrito — caminho C",
        p("**Ciclofosfamida endovenosa em pulso, 15 mg/kg.** Com 78 kg, "
          "**1,17 g** por pulso. A dose de indução dos ensaios, sem as "
          "duas subtrações — nem a da idade entre 60 e 70 anos, nem a da "
          "creatinina entre 300 e 500 µmol/L. Os metabólitos ativos são "
          "eliminados por via renal, e com filtração de 17 mL/min a área "
          "sob a curva de 1,17 g não é a de 1,17 g."),
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
          "duas unidades de concentrado de hemácias."),
        p("A creatinina parou de subir e ficou em 4,6 mg/dL, com diurese de "
          "780 mL. Ele voltou a completar frases inteiras e pediu para comer."),

        fundo=CENA,
    ),

    pagina("dia5", "Quinto dia de indução", "Quinto dia",
        p("Na madrugada do quinto dia, temperatura de **38,9 °C**, com "
          "calafrio. A pressão arterial caiu para 92/54 mmHg e respondeu a 500 "
          "mL de cristaloide. A frequência cardíaca é de 118 e a saturação, "
          "94% no mesmo cateter nasal a 3 L/min — **sem nova hemoptise e sem "
          "piora do infiltrado na radiografia de leito**."),
        p("Ele está com um cateter venoso central em jugular interna direita, "
          "puncionado no segundo dia, e o sítio de inserção está "
          "hiperemiado e doloroso à palpação. A proteína C reativa subiu de "
          "186 para **204 mg/L** e a procalcitonina, que era 0,4, está em "
          "**3,1 ng/mL**."),
        fundo=CENA,
    ),

    bifurcacao("b_febre", "Decisão",
        "Febre no quinto dia de indução. O que você faz?",
        "38,9 °C com calafrio, hipotensão que respondeu a volume, "
        "procalcitonina de 0,4 para 3,1, cateter central com sítio inflamado. "
        "Sem nova hemoptise e sem piora do infiltrado.",
        [
            caminho("Retirar o cateter, colher hemoculturas pareadas e "
                    "iniciar antibiótico com cobertura para "
                    "//Staphylococcus aureus//", "f_retira",
                    "É o que os dados sustentam. Órgão-alvo estável, "
                    "procalcitonina subindo e porta de entrada visível. "
                    "Retirar o cateter é tratamento, não investigação."),
            caminho("Intensificar a imunossupressão, por recidiva da vasculite",
                    "f_intensifica",
                    "Tem lógica se a leitura for de doença descontrolada — mas "
                    "a hemoptise cessou, o infiltrado não piorou e a "
                    "procalcitonina subiu, que é o marcador que separa "
                    "inflamação estéril de infecção bacteriana."),
            caminho("Suspender toda a imunossupressão até esclarecer a febre",
                    "f_suspende",
                    "O meio-termo que parece prudente. A vasculite acabou de "
                    "ser controlada e a crescente ainda é celular: tratar a "
                    "infecção e manter a indução é possível, e é o que se faz."),
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
          "hemoptise — dois episódios de cerca de 40 mL — e a saturação caiu "
          "para 90% em cateter a 4 L/min. A hemoglobina caiu de 8,6 para "
          "**7,4 g/dL** e a creatinina voltou a subir, de 4,2 para 4,8."),
        p("A indução foi reiniciada no décimo dia, em dose plena, agora sobre "
          "um paciente que passou 48 horas sangrando de novo no alvéolo."),
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
          "dias, oxacilina por 28 — a duração de bacteremia complicada —, e "
          "diálise por três sessões durante o choque, por oligúria e acidose "
          "refratária."),
        p("Sobreviveu. Saiu da terapia intensiva no décimo terceiro dia, com "
          "creatinina de 3,2 mg/dL e diurese recuperada, ainda dependente de "
          "oxigênio suplementar."),
        fundo=CENA,
        conforme=("b1", ["d_rituximabe", "d_cfx_ajustada", "d_cfx_plena"]),
    ),

    desfecho("fi_obito", "Óbito no décimo quarto dia de internação",
        p("O choque séptico se instalou sobre uma medula que a ciclofosfamida "
          "em dose plena, sem correção para a filtração de 17 mL/min, havia "
          "levado a **210 neutrófilos**. A intensificação do corticoide no "
          "sétimo dia foi dada sobre uma bacteremia já em curso, com a porta "
          "de entrada ainda no pescoço."),
        p("Evoluiu com disfunção de múltiplos órgãos e choque refratário a "
          "três drogas vasoativas. Faleceu no décimo quarto dia de "
          "internação, no nono dia de bacteremia."),
        p("**A vasculite estava respondendo.** A hemoptise havia cessado no "
          "terceiro dia e o infiltrado não voltou a piorar em momento algum."),
        qualidade="pior", fecho="tres_caminhos",
        porque="Três decisões se somaram, e nenhuma delas era sobre o "
               "diagnóstico. A dose plena da ciclofosfamida com filtração de "
               "17 mL/min entregou uma neutropenia que o esquema corrigido não "
               "produziria. A febre do quinto dia foi lida como recidiva da "
               "doença quando a procalcitonina, o órgão-alvo estável e o sítio "
               "de inserção diziam infecção. E o cateter — a porta de entrada "
               "— permaneceu. A causa de morte precoce na vasculite ANCA "
               "tratada é a infecção, não a vasculite, e este caso é essa "
               "frase.",
        fundo=CENA),



    pagina("dia10", "Décimo dia de indução", "Décimo dia",
        p("O que vem a seguir depende do esquema de indução que foi "
          "escolhido — e é aqui que os três caminhos deixam de ser o mesmo "
          "caso."),
        fundo=CENA,
        conforme=("b1", ["d10_rituximabe", "d10_cfx_ajustada", "d10_cfx_plena"]),
    ),

    # ─────────────── o décimo dia, um por caminho ───────────────

    pagina("d10_rituximabe", "Décimo dia · caminho A", "O hemograma do décimo dia",
        p("O hemograma do décimo dia mostra **6.400 leucócitos com 4.100 "
          "neutrófilos** — sem citopenia. O rituximabe depleta linfócito B e "
          "não produz nadir de neutrófilos: a bacteremia veio do cateter e do "
          "corticoide, não da segunda droga."),
        p("Completou as quatro doses semanais e catorze dias de oxacilina. A "
          "creatinina caiu de forma sustentada."),

        fundo=CENA, segue="d_rituximabe",
    ),

    pagina("d10_cfx_ajustada", "Décimo dia · caminho B", "O hemograma do décimo dia",
        p("O hemograma do décimo dia, no nadir esperado do pulso, mostra "
          "**2.900 leucócitos com 1.400 neutrófilos**. É citopenia leve, "
          "dentro do previsto para 10 mg/kg, e não muda a conduta: o "
          "antibiótico segue, o pulso seguinte fica mantido na mesma dose e o "
          "hemograma passa a ser duas vezes por semana."),
        p("A febre cedeu, completou catorze dias de oxacilina, e o segundo "
          "pulso foi dado na semana 2 como programado."),

        fundo=CENA, segue="d_cfx_ajustada",
    ),

    pagina("d10_cfx_plena", "Décimo dia · caminho C", "O hemograma do décimo dia",
        p("O hemograma do décimo dia mostra **900 leucócitos com 210 "
          "neutrófilos**. A febre, que havia cedido com a oxacilina, voltou a "
          "39,4 °C, agora com hipotensão que exigiu noradrenalina, e ele foi "
          "transferido para a terapia intensiva."),
        p("Neutropenia muito mais profunda do que a esperada: o nadir de um "
          "pulso ajustado fica em torno de 1.400 neutrófilos, não 210. Foram "
          "acrescentados antibiótico de amplo espectro, cobertura antifúngica "
          "empírica ao quinto dia de neutropenia febril e fator estimulador de "
          "colônias."),

        fundo=CENA, segue="d_cfx_plena",
    ),

    # ═══════════════════════ desfechos ═══════════════════════

    desfecho("d_rituximabe", "Alta sem diálise",
        p("A creatinina, que havia chegado a 4,6 mg/dL, caiu de forma "
          "sustentada e a diurese se recuperou, **sem necessidade de diálise "
          "em nenhum momento**. Saiu em ar ambiente, com saturação de 96%."),
        p("Segue em manutenção programada com rituximabe, com consulta e "
          "exames agendados, e com o pé caído em reabilitação — a mononeurite "
          "é o achado que mais demora a melhorar, quando melhora."),
        qualidade="melhor", fecho="tres_caminhos",
        porque="O tratamento entrou enquanto a crescente ainda era celular, e "
               "crescente celular é tecido inflamado, que responde. Com "
               "filtração de 17 mL/min/1,73 m², o rituximabe entrega a indução "
               "sem depender de acertar uma correção de dose — e, quando a "
               "infecção de cateter veio, ela não encontrou uma medula "
               "deprimida pela segunda droga.",
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
               "mais vigilância — hemograma seriado, mesna, ajuste a cada "
               "ciclo — e cobra a conversa sobre fertilidade que o rituximabe "
               "dispensa. Neste paciente, de 63 anos, essa conversa pesa "
               "menos; a conta da dose, não.",
        fundo=CENA),

    desfecho("d_cfx_plena", "Alta após a terapia intensiva",
        p("A vasculite respondeu como nos outros dois caminhos: a hemoptise "
          "cessou no terceiro dia e a creatinina caiu. O que mudou foi o "
          "resto. Foram treze dias de terapia intensiva, noradrenalina por "
          "quatro deles, antibiótico de amplo espectro, antifúngico empírico "
          "e fator estimulador de colônias."),
        p("Saiu andando. Nenhuma das decisões que fizeram a diferença tinha a "
          "ver com o diagnóstico."),
        qualidade="pior", fecho="tres_caminhos",
        porque="Com filtração glomerular de 17 mL/min/1,73 m², a dose plena "
               "produziu exposição bem acima da pretendida — os metabólitos "
               "ativos da ciclofosfamida são eliminados por via renal, e a "
               "conta do CYCLOPS teria pedido 10 mg/kg. A causa de morte "
               "precoce na vasculite associada ao ANCA tratada é a infecção, "
               "não a vasculite. Aqui a infecção veio do cateter, que os três "
               "caminhos tinham; a profundidade dela veio da dose, que só "
               "este caminho escolheu.",
        fundo=CENA),

    # ═══════════════ o fecho, igual para os três ramos ═══════════════

    pagina("tres_caminhos", "Onde o caso se dividiu", "Os três caminhos",
        p("O caso ramificou em quatro lugares. O primeiro foi silencioso: "
          "quem pediu a biópsia renal e o ANCA discutiu o mecanismo; quem não "
          "pediu discutiu como conduzir sem ele. O segundo foi o que fazer "
          "quando ele piorou sob antibiótico. O terceiro, a segunda droga da "
          "indução — que a tabela compara abaixo. O quarto foi a febre do "
          "quinto dia, e é o único do caso que tem um ramo que termina em "
          "óbito."),
        tabela(["Caminho", "A conta que ele exige",
                "Neutrófilos no 10º dia", "Desfecho"], [
            ["A · Rituximabe 375 mg/m² semanal",
             "Nenhuma correção para a filtração",
             "4.100", "Alta mais precoce · melhor função residual"],
            ["B · Ciclofosfamida 10 mg/kg",
             "15 − 2,5 (idade) − 2,5 (creatinina)",
             "1.400", "Cinco dias a mais · função um degrau abaixo"],
            ["C · Ciclofosfamida 15 mg/kg",
             "Nenhuma — e é esse o ponto",
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
        obito_texto="Ciclofosfamida em dose plena com filtração de 17 mL/min, "
                    "e a febre do quinto dia lida como recidiva da doença. A "
                    "vasculite estava respondendo: a hemoptise havia cessado "
                    "no terceiro dia e o infiltrado nunca voltou a piorar. "
                    "Nenhuma das três decisões que mataram este paciente era "
                    "sobre o diagnóstico.",
        consequencias=[
            consequencia(
                chave="sem_hemocultura",
                titulo="Imunossuprimiu sem cultura colhida antes do antibiótico",
                quando={"sem": ["Hemocultura"]}, dias=4, tfg=5,
                porque="A cultura negativa é o documento que autoriza o "
                       "corticoide, e ela só vale se for anterior à primeira "
                       "dose. Sem ela, o antibiótico empírico se estende — e "
                       "cefalosporina de amplo espectro por mais de uma semana, "
                       "sem foco, num idoso internado e imunossuprimido, é a "
                       "origem mais comum de colite por //Clostridioides "
                       "difficile// na enfermaria."),
            consequencia(
                chave="sem_lba",
                titulo="Tratou o infiltrado sem provar de que ele é feito",
                quando={"sem": ["Lavado broncoalveolar"]}, dias=3, tfg=0,
                porque="Sem alíquotas progressivamente hemorrágicas e sem "
                       "hemossiderófagos, a hemorragia alveolar fica sendo "
                       "inferência aritmética. Vidro fosco bilateral é "
                       "compatível com sangue, água, pus, células e proteína, "
                       "e o tratamento das cinco coisas é diferente."),
            consequencia(
                chave="sem_cultura_lba",
                titulo="Nenhuma cultura do próprio pulmão",
                quando={"sem": ["Cultura do lavado broncoalveolar"]},
                dias=2, tfg=0,
                porque="É a cultura negativa do pulmão que autoriza tratar o "
                       "infiltrado como imune. Sem ela, a decisão de "
                       "imunossuprimir carrega uma pergunta infecciosa aberta "
                       "sobre o órgão que está falhando."),
            consequencia(
                chave="sem_sedimento",
                titulo="A lesão renal nunca foi localizada",
                quando={"sem": ["Sedimento urinário"]}, dias=2, tfg=6,
                porque="Sem hemácia dismórfica e sem cilindro hemático, a "
                       "creatinina que sobe é tratada como pré-renal ou "
                       "necrose tubular, e o tratamento certo atrasa. "
                       "Crescente celular vira fibrosa no intervalo, e o que "
                       "virou não volta."),
            consequencia(
                chave="sem_tecido_nem_anticorpo",
                titulo="Tratou sem excluir a doença anti-membrana basal",
                quando={"sem": ["Biópsia renal",
                                "Anticorpo anti-membrana basal glomerular"]},
                dias=0, tfg=8,
                porque="A doença anti-MBG faz exatamente esta síndrome, perde "
                       "função renal em dias e o tratamento dela inclui troca "
                       "plasmática, que na vasculite ANCA é discutível. Sem o "
                       "tecido e sem o anticorpo, você tratou a doença mais "
                       "provável — e a mais provável não é a única."),
            consequencia(
                chave="escalonou",
                titulo="Escalonou o antibiótico em vez de investigar o sangramento",
                quando={"escolheu": ["b_dia2", 0]}, dias=3, tfg=6,
                porque="Trinta e seis horas é cedo para declarar falha de "
                       "antibiótico numa pneumonia comunitária, e nenhum "
                       "espectro retém sangue no alvéolo. Foram 48 horas a "
                       "mais de sangramento e de creatinina subindo, e a "
                       "crescente celular não espera."),
            consequencia(
                chave="corticoide_antes_das_provas",
                titulo="Imunossuprimiu antes de colher qualquer prova",
                quando={"escolheu": ["b_dia2", 2]}, dias=2, tfg=2,
                porque="Parou o sangramento, e isso conta. Mas toda cultura "
                       "colhida a partir dali foi colhida sob corticoide, e o "
                       "negativo delas vale menos justamente no dia em que se "
                       "precisa dele para justificar o que já foi feito."),
            consequencia(
                chave="febre_intensificou",
                titulo="Leu a febre do quinto dia como recidiva da vasculite",
                quando={"escolheu": ["b_febre", 1]}, dias=14, tfg=14,
                porque="A hemoptise havia cessado, o infiltrado não piorou e a "
                       "procalcitonina subiu de 0,4 para 3,1. Intensificar a "
                       "imunossupressão sobre uma bacteremia com a porta de "
                       "entrada ainda no pescoço levou a choque séptico e a "
                       "três sessões de diálise."),
            consequencia(
                chave="febre_suspendeu",
                titulo="Suspendeu toda a imunossupressão",
                quando={"escolheu": ["b_febre", 2]}, dias=6, tfg=9,
                porque="Quarenta e oito horas sem corticoide bastaram para o "
                       "alvéolo voltar a sangrar e a creatinina voltar a "
                       "subir. Tratar a infecção e manter a indução é "
                       "possível — e é o que se faz."),
            consequencia(
                chave="cfx_ajustada",
                titulo="Escolheu ciclofosfamida, com a conta feita",
                quando={"escolheu": ["b1", 1]}, dias=5, tfg=8,
                porque="Tão eficaz quanto o rituximabe na indução, e o nadir de "
                       "1.400 neutrófilos ficou onde a dose corrigida prevê. "
                       "Custa mais vigilância e mais dias — e o preço é da "
                       "droga, não de um erro seu."),
            consequencia(
                chave="cfx_plena",
                titulo="Escolheu ciclofosfamida sem a correção de dose",
                quando={"escolheu": ["b1", 2]}, dias=13, tfg=12,
                porque="Os metabólitos ativos saem por via renal, e com "
                       "filtração de 17 mL/min a exposição de 15 mg/kg é bem "
                       "maior do que a pretendida. A vasculite respondeu igual "
                       "nos três caminhos; o que mudou foi a medula, e a "
                       "bacteremia encontrou 210 neutrófilos em vez de 1.400."),
        ],
        fundo=CENA,
    ),

    pagina("lacuna", "O que fica sem explicação", "A lacuna",
        p("Três achados deste paciente continuam sem explicação depois do "
          "diagnóstico fechado."),
        quadro("Os sintomas nasais",
            p("Crostas hemáticas, epistaxe diária e anosmia por oito semanas "
              "descrevem doença de via aérea superior, que é o território "
              "próprio da granulomatose com poliangeíte. A poliangeíte "
              "microscópica pode acometer a via aérea superior de forma leve, "
              "e é a leitura que sustentamos; mas quem disser que este é um "
              "fenótipo sobreposto não está errado, e a literatura não fecha "
              "essa fronteira. Para quem não pediu a sorologia, a questão "
              "sequer chega a se colocar."),
            sistema="via"),
        quadro("A resposta medular",
            p("A queda de hemoglobina localiza o sangue no alvéolo, e isso a "
              "Pergunta 6 estabeleceu. O que fica sem explicação é a resposta "
              "a ela: reticulócitos de 2,1% num hematócrito baixo dão índice "
              "reticulocitário em torno de 1,0 — medula que não repõe o que se "
              "perde. Doença inflamatória de oito semanas e deficiência de "
              "eritropoetina na lesão renal aguda explicam boa parte, e "
              "**nenhuma das duas foi medida** neste paciente. Fica como "
              "hipótese, não como fato."),
            sistema="sangue"),
        quadro("A artralgia migratória",
            p("Compatível com a doença e inespecífica: acompanha vasculite, "
              "infecção arrastada e doença do tecido conjuntivo com a mesma "
              "facilidade. Entra na história como ruído honesto, não como "
              "pista — e é justamente o tipo de achado que, lido "
              "retrospectivamente, parece óbvio."),
            sistema="geral"),
        fundo=CENA,
        so_kicker=True,
    ),

    pagina("retrospectiva", "Onde dava para ter chegado antes",
        "A retrospectiva",
        p("Em que momento, antes do quinto dia, a informação já estava "
          "disponível — e o que impediu que fosse usada."),
        tabela(["Quando", "O que estava à mão", "O que aconteceu"], [
            ["Oito e quatro semanas antes",
             "Rinossinusite que não respondeu a **dois** cursos de antibiótico, "
             "com adesão confirmada",
             "Mantida como infecção e tratada uma terceira vez. Doença de "
             "mucosa que não cede a antibiótico correto é um dado, não um "
             "fracasso de adesão"],
            ["Seis semanas antes",
             "Creatinina de 1,4 mg/dL com hematúria de 12 por campo, num "
             "paciente cuja creatinina era 1,0",
             "Lida como 'quase normal'. Era perda de um terço da filtração em "
             "dois meses, com sangue na urina — e um sedimento com pesquisa de "
             "dismorfismo naquele dia teria custado quase nada"],
            ["Duas semanas antes",
             "Radiografia de tórax normal num paciente com hemoptise",
             "Tratada como exclusão. A radiografia é pouco sensível para "
             "ocupação alveolar precoce; um filme normal não encerra a "
             "investigação de quem escarra sangue"],
            ["Na última semana",
             "Urina escura e noctúria que desapareceu, referidas pela esposa",
             "Não foram perguntadas nem examinadas. Quem parou de acordar à "
             "noite para urinar depois de anos fazendo isso está oligúrico até "
             "prova em contrário"],
        ]),
        quadro("O viés que operou aqui",
            p("Fechamento precoce: a primeira explicação plausível foi mantida "
              "por oito semanas, e cada sintoma novo foi encaixado nela ou "
              "tratado como evento separado — sinusite, depois artrite, depois "
              "tosse, depois pneumonia. O que quebra esse viés não é "
              "conhecimento raro: é a pergunta de **por que a doença anterior "
              "não respondeu ao tratamento correto**. Ela apareceu três vezes "
              "neste caso e foi respondida uma."),
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
                  "Mikael Häggström, CC0 e CC BY 4.0. As setas sobre a "
                  "fotomicrografia são leitura editorial deste caso."),
                sistema="pulmao"),
            quadro("As diretrizes citadas",
                p("PEXIVAS //(N Engl J Med. 2020;382:622-31)// para troca "
                  "plasmática e desmame de glicocorticoide; CYCLOPS "
                  "//(Ann Intern Med. 2009;150:670-80)// para a correção de "
                  "dose da ciclofosfamida; RAVE //(N Engl J Med. "
                  "2010;363:221-32)// e RITUXVAS //(N Engl J Med. "
                  "2010;363:211-20)// para o rituximabe; ADVOCATE //(N Engl J "
                  "Med. 2021;384:599-609)// para o avacopan; EULAR 2022 e "
                  "KDIGO para as recomendações; Berden //(J Am Soc Nephrol. "
                  "2010;21:1628-36)// para a classificação histológica; "
                  "Bajema //(Clin Nephrol. 1997;48:16-21)// para o granuloma "
                  "renal; ACR/EULAR 2022 para os critérios de classificação."),
                sistema="rim"),
            colunas=4,
        ),
        fundo=CENA, so_kicker=True,
    ),
]


# ═══════════════ o que a revisão cobra, quando não há mais o que decidir ══════

REVISAO = [
    dict(rotulo="Creatinina (no ambulatório)", chave="Creatinina",
         porque="Era o exame que transformava oito semanas de sintomas em "
                "doença de órgão. 1,4 contra 1,0 de dois meses antes é perda "
                "de um terço da filtração — e ninguém compara o que não "
                "pediu."),
    dict(rotulo="Sedimento urinário", chave="Sedimento urinário",
         porque="É o exame mais barato do caso e o único que localiza a lesão "
                "renal em minutos. Hemácia dismórfica e cilindro hemático põem "
                "o sangramento dentro do glomérulo e derrubam a hipótese de "
                "duas doenças independentes."),
    dict(rotulo="Hemocultura, antes do antibiótico", chave="Hemocultura",
         porque="Endocardite faz síndrome pulmão-rim e contraindica "
                "imunossupressão. E, uma vez iniciado o antibiótico, a cultura "
                "negativa deixa de valer — que é justamente o documento "
                "necessário para autorizar o corticoide poucos dias depois."),
    dict(rotulo="Lavado broncoalveolar", chave="Lavado broncoalveolar",
         porque="Comprova a hemorragia alveolar pelas alíquotas "
                "progressivamente hemorrágicas e pelos hemossiderófagos acima "
                "de 20%, e diz que o sangramento tem pelo menos 48 horas. Sem "
                "ele, a hemorragia alveolar é inferência aritmética."),
    dict(rotulo="Cultura do lavado broncoalveolar",
         chave="Cultura do lavado broncoalveolar",
         porque="É a cultura negativa do próprio pulmão que autoriza tratar o "
                "infiltrado como imune. Tratar infecção difusa com pulso de "
                "corticoide e ciclofosfamida tem consequência previsível."),
    dict(rotulo="Biópsia renal", chave="Biópsia renal",
         porque="É o único árbitro entre pauci-imune, depósito linear e "
                "depósito granular — e o mesmo fragmento dá a gravidade "
                "histológica, que é o que mais prediz a função renal que vai "
                "sobrar."),
    dict(rotulo="ANCA por imunofluorescência indireta",
         chave="ANCA por imunofluorescência indireta",
         porque="Junto com o anti-MPO e o anti-PR3, é o que nomeia a doença e "
                "separa os dois fenótipos. Leva dias, e é por isso que precisa "
                "ser pedido cedo."),
    dict(rotulo="Anticorpo anti-membrana basal glomerular",
         chave="Anticorpo anti-membrana basal glomerular",
         porque="É o exame de maior urgência do painel do mecanismo: na doença "
                "anti-MBG a demora de poucos dias custa a função renal de "
                "forma definitiva, e o tratamento dela inclui troca "
                "plasmática, que nesta é discutível."),
]

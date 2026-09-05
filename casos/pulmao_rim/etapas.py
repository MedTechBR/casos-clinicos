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
    alt, bifurcacao, caminho, capa, desfecho, grade, grupo, lamina, op, p,
    pagina, pedido, pergunta, quadro, resultados, tabela,
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
EAS = "sedimento_cilindro.jpg"
BIOPSIA = "biopsia_renal_cortex.jpg"
CRESCENTE = "glomerulo_crescente.jpg"
IF = "panca_imunofluorescencia.jpg"


# ═════════════════ o que é comum aos três esquemas de indução ═══════════════

def _esquema_comum():
    """Tudo o que não muda com a escolha da segunda droga, em dois pares."""
    glicocorticoide = quadro("O glicocorticoide, igual nos três caminhos",
        p("Metilprednisolona 500 mg por via endovenosa ao dia por três dias, "
          "seguida de prednisona por via oral. O PEXIVAS (2020) comparou o "
          "desmame padrão com um **desmame reduzido**, que chega a cerca de "
          "60% da dose acumulada do braço padrão em seis meses: a eficácia foi "
          "não-inferior e as infecções graves em um ano caíram. A dose inicial "
          "do PEXIVAS é por faixa de peso — **acima de 75 kg, 75 mg/dia**, que "
          "é a faixa dos 78 kg dele."),
        sistema="geral")
    plasma = quadro("Troca plasmática: uma decisão em disputa",
        p("O PEXIVAS randomizou troca plasmática em 704 pacientes com vasculite "
          "ANCA grave e **não** mostrou redução de morte ou de doença renal em "
          "estágio terminal. Mas as diretrizes não a abandonaram: a EULAR de "
          "2022 diz que ela **pode ser considerada** com creatinina acima de "
          "300 µmol/L por glomerulonefrite ativa — e ele está em **336 "
          "µmol/L** —, e a KDIGO mantém a hemorragia alveolar com hipoxemia "
          "entre as situações em que se considera. Ou seja: neste paciente ela "
          "é **discutível**, não descartada. Quem indicar não está errado; "
          "quem não indicar também não."),
        sistema="sangue")
    avacopan = quadro("Avacopan, e por que ele não entra aqui",
        p("O ADVOCATE (2021) mostrou não-inferioridade na remissão em 26 "
          "semanas e **superioridade na remissão sustentada em 52**, com menos "
          "toxicidade de glicocorticoide. É adjuvante, não substituto da "
          "indução. O limite deste paciente não é a evidência: é a "
          "disponibilidade — conferir a oferta no serviço antes de escrever no "
          "plano o que não se pode entregar."),
        sistema="geral")
    cerco = quadro("Antes da primeira dose, e depois dela",
        p("Antes: sorologias de hepatite B e C e HIV, e a cultura que autoriza "
          "imunossuprimir. Depois: sulfametoxazol-trimetoprima como profilaxia "
          "para //Pneumocystis//, **em dose reduzida pela filtração** — 400/80 "
          "mg três vezes por semana em vez do comprimido diário, porque com "
          "17 mL/min a exposição sobe e o trimetoprim ainda empurra potássio e "
          "creatinina num paciente que chegou com 5,4 mEq/L. Cálcio e vitamina "
          "D pelo corticoide, e hemograma semanal."),
        sistema="pulmao")
    return glicocorticoide + plasma, avacopan + cerco


ETAPAS = [

    # ═══════════════════════════ capa ═══════════════════════════

    capa(TITULO, fundo=CENA,
         kicker="Caso interativo · 11 decisões · curso simulado",
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

    pergunta("p1", "Pergunta 1 · o tratamento que falhou",
        "Duas rinossinusites tratadas com o antibiótico correto, sem resposta. "
        "O que isso muda?",
        [
            alt("Nada — é resistência bacteriana",
                "Resistência acontece, mas duas falhas seguidas com adesão "
                "confirmada deslocam a probabilidade para fora da hipótese que "
                "está sendo tratada."),
            alt("Indica uso abusivo de vasoconstritor nasal",
                "Causa real de crosta e sangramento, e vale perguntar. Não "
                "explica a perda progressiva de olfato."),
            alt("Confirma rinite alérgica",
                "Rinite alérgica dá prurido, espirro e secreção clara — não "
                "crosta hemática com epistaxe diária."),
            alt("Obriga a rever o diagnóstico",
                "É o movimento que quebra o fechamento precoce: a hipótese em "
                "uso deixou de explicar o paciente. Mucosa nasal que não cede "
                "a antibiótico entra numa lista curta — inflamatória, "
                "granulomatosa, neoplásica, por substância inalada.",
                certa=True),
            alt("Pede um terceiro curso, mais largo",
                "É o caminho que este paciente percorreu, e consumiu oito "
                "semanas. Adia a pergunta em vez de respondê-la."),
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

    pedido("ex_amb", "Pergunta 2 · o que pedir no ambulatório",
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
            ]),
            grupo("Rim e urina", "rim", [
                op("Creatinina",
                   resultado="1,4 mg/dL {{(1,0 há dois meses)}}",
                   referencia="até 1,3 mg/dL", alterado=True),
                op("Sedimento urinário", "urina fresca",
                   resultado="Proteinúria 1+ · **hemácias 12 por campo** · "
                             "sem cilindros · sem bacteriúria",
                   referencia="sem hemácias, sem proteinúria", alterado=True),
                op("Relação proteína/creatinina urinária",
                   resultado="0,6 mg/mg", referencia="abaixo de 0,2 mg/mg",
                   alterado=True),
            ]),
            grupo("Imagem", "pulmao", [
                op("Radiografia de tórax",
                   resultado="Sem alterações", referencia="normal"),
                op("Tomografia de seios da face"),
            ]),
        ],
        fundo=CENA, banco=BANCO, limite=4,
    ),

    resultados("res_amb", "O que voltou do ambulatório",
        "Os exames que você pediu", "ex_amb",
        introducao="Só o que foi marcado. Estamos oito semanas depois do "
                   "início e seis semanas antes da internação.",
        fundo=CENA,
    ),

    pergunta("p2", "Pergunta 3 · interpretação de um dado isolado",
        "Creatinina de 1,4 mg/dL hoje; era 1,0 mg/dL há dois meses. O que esse "
        "par permite afirmar?",
        [
            alt("Variação de hidratação ou de massa muscular",
                "É a leitura que o laudo induz, porque 1,4 sai quase colado à "
                "referência. Mas a referência é populacional, e o paciente é a "
                "referência dele."),
            alt("Doença renal crônica estágio 2",
                "Crônico exige alteração mantida por mais de três meses. Aqui "
                "há dois valores separados por dois meses, diferentes entre "
                "si: é o oposto de crônico."),
            alt("Perda de um terço da filtração em dois meses",
                "Por CKD-EPI 2021, um homem de 63 anos sai de cerca de 80 para "
                "cerca de 53 mL/min/1,73 m². A trajetória, e não o valor, "
                "estabelece a lesão como aguda.", certa=True),
            alt("Efeito esperado da losartana",
                "Bloqueador do receptor eleva a creatinina em 20 a 30% nas "
                "primeiras semanas — e ele usa losartana há dez anos. O tempo "
                "não fecha."),
            alt("Obstrução da via urinária por coágulos",
                "Obstrução por coágulo exige sangramento macroscópico volumoso "
                "e costuma doer. Doze hemácias por campo não obstruem nada."),
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
        quadro("Uma radiografia normal, aqui, não encerra nada",
            p("A radiografia simples é pouco sensível para ocupação alveolar "
              "precoce e para sangramento de pequeno volume: é preciso "
              "preencher uma fração considerável do parênquima antes que a "
              "opacidade apareça no filme. Em quem escarra sangue, um filme "
              "normal reduz a probabilidade de doença extensa naquele momento "
              "e **não** dispensa a investigação da causa."),
            sistema="pulmao"),
        fundo=CENA,
    ),

    pagina("evolucao_c", "Na última semana", "Os sete dias antes da internação",
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
        p("Ao exame, a temperatura era de 37,8 °C, a pressão arterial de "
          "148/92 mmHg, a frequência cardíaca de 104 batimentos por minuto e a "
          "frequência respiratória de 28 incursões por minuto. A saturação de "
          "oxigênio era de 88% enquanto o paciente respirava ar ambiente, e "
          "subiu para 94% com cateter nasal a 4 litros por minuto. **Pesava "
          "78 kg e media 1,72 m** — eram 84 kg dois meses antes."),
        p("Estava dispneico, preferindo permanecer sentado, completando apenas "
          "frases curtas, com palidez cutâneo-mucosa acentuada."),
        corpo([
            ("via", "Crostas hemáticas aderidas ao septo em ambas as narinas, "
                    "mucosa friável. Sem perfuração septal, deformidade em "
                    "sela ou massa."),
            ("pulmao", "Crepitações finas difusas nos dois hemitórax, sem "
                       "sibilos e sem atrito pleural. Ausculta cardíaca "
                       "normal, sem sopro, sem estase jugular e sem edema."),
            ("rim", "Sem massa palpável e sem dor à punho-percussão. No exame "
                    "físico o rim aparece só pela pressão de 148/92 mmHg."),
            ("pele", "Lesões purpúricas palpáveis na face anterior das pernas "
                     "e no dorso dos pés, algumas com centro escurecido, que "
                     "não desaparecem à digitopressão. Sem lesão em polpa "
                     "digital, sem hemorragia subungueal."),
            ("nervo", "Pé caído à direita, com força 2/5 para dorsiflexão, e "
                      "déficit sensitivo ulnar à esquerda. Assimétrico, sem "
                      "nível medular e sem raiz única."),
        ], altura=316),
        fundo=CENA,
        so_kicker=True,
    ),

    pergunta("p3", "Pergunta 4 · conduta imediata",
        "Quarenta minutos de pronto-socorro, com hipótese de pneumonia grave. "
        "Qual a ordem?",
        [
            alt("Antibiótico agora; culturas depois, se não melhorar",
                "Vem de uma regra correta — antecipar o antibiótico salva vida "
                "na sepse. Mas cultura colhida depois da primeira dose deixa "
                "de valer, e é ela que vai autorizar imunossuprimir daqui a "
                "poucos dias."),
            alt("Tomografia antes de qualquer antibiótico",
                "Inverte a ordem de risco com saturação de 88%. A tomografia "
                "descreve o padrão; ela não exclui infecção."),
            alt("Corticoide em dose imunossupressora",
                "A decisão mais perigosa da lista — e ela vai reaparecer no "
                "caso com outro nome. Imunossuprimir com culturas em andamento "
                "transforma endocardite em desfecho que não se recupera."),
            alt("Hemodiálise de urgência",
                "Nenhuma indicação de urgência está presente: sem hipercalemia "
                "com repercussão, sem acidose refratária, sem congestão, sem "
                "sintoma urêmico. Creatinina alta sozinha não indica."),
            alt("Culturas e, em seguida, antibiótico empírico",
                "A distância entre as duas condutas é de minutos. A suspeita "
                "de infecção grave é legítima e o antibiótico entra; o que não "
                "pode é entrar antes do material que vai julgá-lo.",
                certa=True),
        ],
        titulo_resposta="Cultura, depois antibiótico — e a distância é de minutos",
        fundo=TC,
    ),

    pedido("ex_adm", "Pergunta 5 · a investigação da admissão",
        "Que exames você pede agora?",
        "Pronto-socorro, com a hipótese de infecção grave em curso. **Seis "
        "vagas.** De novo: o que não for pedido não volta.",
        [
            grupo("Bancada, em minutos", "rim", [
                op("Creatinina",
                   resultado="3,8 mg/dL {{(1,4 há seis semanas)}}",
                   referencia="até 1,3 mg/dL", alterado=True),
                op("Taxa de filtração glomerular estimada",
                   "CKD-EPI 2021 — decide a dose de vários esquemas",
                   resultado="17 mL/min/1,73 m²",
                   referencia="acima de 90 mL/min/1,73 m²", alterado=True),
                op("Potássio", resultado="5,4 mEq/L",
                   referencia="3,5 a 5,0 mEq/L", alterado=True),
                op("Sedimento urinário", "urina fresca, dismorfismo e cilindros"),
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
            ]),
            grupo("Imagem do tórax", "pulmao", [
                op("Radiografia de tórax"),
                op("Tomografia de tórax"),
                op("Ecocardiograma transtorácico"),
                op("Angiotomografia de tórax"),
            ]),
            grupo("Infecção", "geral", [
                op("Hemocultura", "três pares, antes do antibiótico",
                   resultado="Em andamento — coletada antes da primeira dose",
                   referencia="negativa"),
                op("Urocultura"),
                op("Anti-HIV"),
                op("HBsAg e anti-HBc"),
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
            "Sedimento urinário": lamina(EAS, "Sedimento urinário",
                "Cilindro urinário: estrutura alongada, de bordas paralelas, "
                "que é o molde do lúmen do túbulo. Imagem ilustrativa, em "
                "preparação corada.",
                "Rian Kabir · Wikimedia Commons · CC BY 2.0"),
        },
    ),

    pagina("leitura_infeccao", "Discussão", "A hipótese com que a equipe começou",
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
        quadro("Por que a leitura é razoável mesmo estando incompleta",
            p("Pneumonia grave é muito mais frequente que qualquer alternativa "
              "desta lista, e o custo de não tratá-la nas primeiras horas é "
              "alto. Tratar a hipótese provável enquanto se investiga a "
              "improvável é conduta correta. O erro não é começar por aqui — "
              "é **não marcar o ponto em que a hipótese deixaria de explicar "
              "o paciente**. Esse ponto vem no segundo dia."),
            sistema="geral"),
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
        quadro("A pergunta aritmética que muda o caso",
            p("Ele expectorou, somando tudo, cerca de **160 mL** de sangue. "
              "Um adulto de 78 kg tem por volta de 5,5 litros de sangue; para "
              "derrubar a hemoglobina de 13,9 para 6,9 g/dL seria preciso "
              "perder da ordem de **dois litros**. Os 160 mL expectorados não "
              "cobrem nem um décimo disso. O sangue que falta está em algum "
              "lugar — e não saiu pela boca."),
            sistema="sangue"),
        fundo=TC,
    ),

    pergunta("p4", "Pergunta 6 · deterioração sob tratamento",
        "Piorou sob antibiótico adequado, e a hemoglobina caiu de novo. Onde "
        "está o sangue que falta?",
        [
            alt("No trato digestivo",
                "Explicaria a anemia, não o infiltrado bilateral simétrico — e "
                "não houve melena nem hematêmese num paciente internado e "
                "observado."),
            alt("No alvéolo",
                "É o compartimento pulmonar capaz de reter grande volume sem "
                "devolvê-lo pela boca: o sangue fica no espaço aéreo, é "
                "fagocitado, e a hemoglobina cai sem hemorragia visível. E "
                "hemorragia alveolar difusa não é complicação de pneumonia "
                "comunitária tratada.", certa=True),
            alt("Em lugar nenhum — é hemodiluição",
                "Diluição explica quedas de 0,5 a 1,0 g/dL após ressuscitação "
                "volumosa. Ele recebeu volume restrito, está oligúrico, e a "
                "queda total é de 4,3 g/dL."),
            alt("Perdido pela urina",
                "Hematúria glomerular é microscópica: são miligramas de "
                "hemoglobina por dia, não gramas. Nenhuma glomerulonefrite "
                "sangra o suficiente para anemiar."),
            alt("Não há sangue perdido — é anemia inflamatória",
                "Anemia de doença inflamatória existe aqui e explica parte da "
                "queda ambulatorial. Ela não cai 0,9 g/dL em 36 horas."),
        ],
        titulo_resposta="A hemoglobina que sumiu diz onde o sangue ficou",
        fundo=TC,
    ),

    pedido("ex_mec", "Pergunta 7 · provar o que está acontecendo",
        "O que você pede agora?",
        "Duas perguntas em aberto: **de onde vem o sangue do pulmão** e **em "
        "que compartimento do rim está a lesão** — e ainda é preciso fechar a "
        "conta com a infecção. **Seis vagas.**",
        [
            grupo("Via aérea", "pulmao", [
                op("Lavado broncoalveolar",
                   "aspecto sequencial das alíquotas e contagem de macrófagos"),
                op("Cultura do lavado broncoalveolar"),
                op("Pesquisa de Pneumocystis no lavado"),
                op("Baciloscopia e teste molecular para tuberculose"),
            ]),
            grupo("Tecido renal", "rim", [
                # Uma agulha, um laudo: microscopia óptica, imunofluorescência
                # e classificação saem do mesmo fragmento. Oferecê-las como
                # três itens marcáveis cobrava três vagas por um exame só, e
                # tornava a revisão do fim aritmeticamente inalcançável.
                op("Biópsia renal",
                   "microscopia óptica, imunofluorescência e classificação, "
                   "do mesmo fragmento",
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
            grupo("Imunologia", "via", [
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
                op("Sedimento urinário", "se ainda não foi pedido"),
                op("Complemento C4"),
                op("Eletroneuromiografia"),
                op("Tomografia de seios da face"),
            ]),
        ],
        fundo=BIOPSIA, banco=BANCO, limite=6,
    ),

    resultados("res_mec", "O que voltou", "A segunda rodada", "ex_mec",
        introducao="De novo, só o que foi marcado.",
        fundo=BIOPSIA,
        laminas={
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

    pagina("virada", "Quinto dia de internação", "O que voltou das culturas",
        p("**As três hemoculturas colhidas antes do antibiótico vieram "
          "negativas em cinco dias.** A urocultura é negativa. O antibiótico "
          "está no quinto dia e ele não melhorou: continua em máscara com "
          "reservatório, com creatinina de 4,6 mg/dL e débito urinário de "
          "480 mL nas últimas 24 horas."),
        p("Quem pediu o lavado broncoalveolar tem, além disso, a informação "
          "que fecha a questão do pulmão. Quem não pediu segue sem ela — e a "
          "decisão do próximo passo terá de ser tomada assim."),
        quadro("O que uma cultura negativa vale, e o que não vale",
            p("Ela não exclui infecção: foi colhida em quem já vinha de "
              "antibiótico ambulatorial, e há agentes que não crescem em "
              "hemocultura de rotina. O que ela faz é **reduzir muito** a "
              "probabilidade de bacteremia e de endocardite — e, junto com a "
              "ausência de resposta a cinco dias de tratamento adequado, "
              "tirar a infecção bacteriana comum do lugar de explicação "
              "principal. Vale registrar: é também esta cultura negativa que, "
              "daqui a pouco, vai autorizar imunossuprimir."),
            sistema="geral"),
        fundo=TC,
    ),

    pergunta("p5", "Pergunta 8 · enquadramento sindrômico",
        "Sangramento alveolar e glomerulonefrite no mesmo paciente e no mesmo "
        "mês. Como se chama esse arranjo?",
        [
            alt("Pneumonia grave com necrose tubular aguda",
                "É a leitura que os cinco dias de antibiótico já testaram. "
                "Necrose tubular dá cilindro granuloso pigmentado, não "
                "hematúria dismórfica — e não põe sangue dentro do alvéolo."),
            alt("Síndrome cardiorrenal tipo 1",
                "Exigiria disfunção cardíaca aguda como motor, e o "
                "ecocardiograma é normal. Congestão não produz hemoptise "
                "recorrente com queda de hemoglobina."),
            alt("Síndrome pulmão-rim",
                "É o nome do arranjo, deliberadamente mais abstrato que "
                "qualquer diagnóstico: hemorragia alveolar difusa mais "
                "glomerulonefrite, sem dizer por quê. Subir um nível antes de "
                "descer para nomes de doença é o que organiza o diferencial.",
                certa=True),
            alt("Sepse com disfunção de múltiplos órgãos",
                "Foi tratada, e a trajetória não fecha: cinco dias de "
                "antibiótico adequado, culturas negativas, procalcitonina de "
                "0,4 e piora progressiva. Sepse também não faz hematúria "
                "dismórfica."),
            alt("Tromboembolismo com nefropatia por contraste",
                "Infarto pulmonar dá dor pleurítica e opacidade focal, e a "
                "angiotomografia não mostrou falha de enchimento. E a "
                "creatinina já subia seis semanas antes do contraste."),
        ],
        titulo_resposta="Nomear a síndrome antes de nomear a doença",
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
        quadro("O que este paciente já eliminou, e com qual dado",
            p("A quarta categoria perdeu força com três hemoculturas negativas "
              "colhidas antes do antibiótico, ecocardiograma sem vegetação, "
              "ausência de exposição a enchente ou roedor, e cinco dias de "
              "antibiótico sem resposta. **As outras três continuam de pé** — "
              "e as três se separam pela mesma coisa: o que a "
              "imunofluorescência do tecido renal mostrar, e qual anticorpo "
              "estiver circulando."),
            sistema="geral"),
        fundo=BIOPSIA,
        rota={"pediu": ["Biópsia renal", "ANCA por imunofluorescência indireta"],
              "entao": "crescente", "senao": "sem_prova"},
    ),

    # ─────────────── rota A: o tecido e o anticorpo foram pedidos ───────────

    pagina("crescente", "Discussão", "A biópsia renal",
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
            p("O laudo descreve **crescentes celulares em 15 dos 24 "
              "glomérulos**, com necrose fibrinoide segmentar, e "
              "imunofluorescência **sem depósitos significativos**. A figura "
              "ao lado é de outro paciente, no aumento em que a morfologia "
              "aparece.")
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

    pergunta("p6", "Pergunta 9 · leitura de um achado de tecido",
        "A imunofluorescência da biópsia renal não mostra depósito imune. O "
        "que ela afirma?",
        [
            alt("Padrão pauci-imune",
                "A imunofluorescência separa três mecanismos, e só três: "
                "depósito linear é anticorpo contra o colágeno tipo IV; "
                "granular é imunocomplexo; ausência é pauci-imune, das "
                "vasculites associadas ao ANCA.", certa=True),
            alt("Nada — é um exame negativo",
                "É o erro mais comum diante deste laudo, e vem de uma leitura "
                "razoável: a maioria dos exames negativos não afirma nada. "
                "Aqui a ausência é o achado."),
            alt("Afasta glomerulonefrite",
                "A glomerulonefrite está estabelecida pela microscopia óptica. "
                "A imunofluorescência não confirma que a lesão existe: ela "
                "separa mecanismos entre lesões que já existem."),
            alt("Nefrite lúpica de classe silenciosa",
                "A nefrite lúpica é doença por imunocomplexo, e a "
                "imunofluorescência dela é exuberante — o //full house//, com "
                "IgG, IgA, IgM, C3 e C1q."),
            alt("Doença anti-membrana basal em fase inicial",
                "A doença anti-MBG tem depósito linear e contínuo desde o "
                "começo — é o mecanismo, não a fase. Não existe anti-MBG com "
                "imunofluorescência limpa."),
        ],
        titulo_resposta="Exame sem depósito não é exame negativo",
        fundo=BIOPSIA,
    ),

    pagina("fenotipo", "Discussão", "Poliangeíte microscópica ou granulomatose",
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
            ["Neste paciente", "Compatível",
             "Improvável — mas não pela biópsia renal: pesam o anticorpo e a "
             "ausência de lesão destrutiva"],
        ]),
        quadro("A armadilha do tecido errado",
            p("A biópsia deste paciente é **renal**, e granuloma praticamente "
              "não aparece no rim — nem mesmo na granulomatose com "
              "poliangeíte. Bajema e cols., revendo biópsias renais de "
              "vasculite sistêmica //(Clin Nephrol. 1997;48:16-21)//, "
              "encontraram granuloma renal em 16 de 157 pacientes, cerca de "
              "10%. E nos critérios ACR/EULAR de 2022 o item é granuloma **em "
              "qualquer tecido**, somando pontos quando presente e zero quando "
              "ausente: a ausência jamais subtrai."),
            sistema="rim"),
        fundo=IF, segue="b1",
    ),

    # ─────────────── rota B: faltou prova, e o caso segue assim ─────────────

    pagina("sem_prova", "Discussão", "Conduzir sem a prova",
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
        quadro("O custo real da vaga que não foi gasta",
            p("A doença anti-membrana basal glomerular é o exemplo caro: faz "
              "exatamente esta síndrome, perde função renal em dias, e o "
              "tratamento dela **inclui troca plasmática**, que na vasculite "
              "ANCA é discutível. Ela se separa por um exame de sangue e por "
              "um padrão linear na imunofluorescência. Sem esses dois, tratar "
              "é apostar na doença mais provável — e a mais provável não é a "
              "única."),
            sistema="rim"),
        fundo=BIOPSIA,
    ),

    pergunta("p6b", "Pergunta 9 · o limite do que se pode afirmar",
        "Sem o tecido e sem o anticorpo, com creatinina de 4,6 e alvéolo "
        "sangrando. O que fazer hoje?",
        [
            alt("Aguardar a estabilização clínica",
                "Parece prudente e custa o rim. Crescente celular vira fibrosa "
                "ao longo de semanas, e fibrosa não responde a nada. Esperar "
                "aqui é escolher a alternativa irreversível."),
            alt("Ciclofosfamida empírica, pela gravidade",
                "A gravidade justifica a pressa, não a escolha da segunda "
                "droga sem diagnóstico. Se a explicação for infecciosa não "
                "cultivada, o desfecho não se recupera."),
            alt("Escalonar o antibiótico",
                "É a leitura já feita três vezes com este paciente — duas no "
                "ambulatório, uma na admissão — e não respondeu nenhuma. "
                "Repetir a hipótese que falhou é o viés que o caso descreve."),
            alt("Colher as duas provas e iniciar o glicocorticoide",
                "O glicocorticoide não apaga o padrão da imunofluorescência "
                "nem o título do anticorpo: colhido o material, ele pode "
                "entrar. O que não pode entrar antes das provas é a segunda "
                "droga.", certa=True),
            alt("Troca plasmática empírica",
                "Cobre a hipótese anti-MBG e, na vasculite ANCA, não reduziu "
                "morte nem doença renal terminal no PEXIVAS. E tem custo "
                "próprio: cateter, coagulopatia, depleção de imunoglobulina."),
        ],
        titulo_resposta="Colher e começar o corticoide não é imunossuprimir a fundo",
        fundo=BIOPSIA, segue="b1",
    ),

    # ═══════════ ATO IV — o tratamento, e a segunda virada ═══════════

    bifurcacao("b1", "Pergunta 10 · o limite de uma terapia",
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
        grade(
            p("**Rituximabe 375 mg/m² por via endovenosa, uma vez por semana, "
              "quatro doses.** Superfície corporal de 1,91 m² pela fórmula de "
              "Mosteller com 78 kg e 1,72 m: **716 mg** por dose. Sem correção "
              "para a função renal — o anticorpo monoclonal não é depurado "
              "pelo rim.")
            + quadro("O que este caminho pede de vigilância",
                p("Pré-medicação com anti-histamínico, paracetamol e o próprio "
                  "glicocorticoide, pela reação infusional da primeira dose. "
                  "Rastrear hepatite B **antes** — o anti-HBc isolado reativa "
                  "sob rituximabe, e a reativação é grave. Imunoglobulinas "
                  "séricas na linha de base, porque a hipogamaglobulinemia "
                  "tardia é o efeito dos ciclos seguintes, não deste."),
                sistema="sangue"),
            *_esquema_comum(), colunas=3,
        ),
        fundo=CENA, segue="dia3",
    ),

    pagina("t_cfx_ajustada", "A prescrição", "O que foi prescrito — caminho B",
        grade(
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
            *_esquema_comum(), colunas=3,
        ),
        fundo=CENA, segue="dia3",
    ),

    pagina("t_cfx_plena", "A prescrição", "O que foi prescrito — caminho C",
        grade(
            p("**Ciclofosfamida endovenosa em pulso, 15 mg/kg.** Com 78 kg, "
              "**1,17 g** por pulso. A dose de indução dos ensaios, sem as "
              "duas subtrações — nem a da idade entre 60 e 70 anos, nem a da "
              "creatinina entre 300 e 500 µmol/L.")
            + quadro("O que esta prescrição assume, sem dizer",
                p("Que a exposição depende só do peso. Ela depende também da "
                  "eliminação: os metabólitos ativos da ciclofosfamida saem "
                  "por via renal, e com filtração de 17 mL/min a área sob a "
                  "curva de 1,17 g não é a de 1,17 g — é maior. A conta do "
                  "CYCLOPS existe porque essa diferença foi medida, e o que "
                  "ela protege não é a eficácia: é a medula."),
                sistema="rim"),
            *_esquema_comum(), colunas=3,
        ),
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
        quadro("O que essa resposta prova, e o que não prova",
            p("Resposta rápida ao glicocorticoide é forte contra infecção não "
              "tratada e a favor de doença inflamatória — mas não é "
              "diagnóstica: linfoma, algumas vasculites secundárias e até "
              "pneumonia em organização respondem a corticoide. O que ela "
              "muda de concreto é o risco imediato: o alvéolo parou de "
              "sangrar, e a partir daqui a ameaça deixa de ser a doença e "
              "passa a ser o tratamento dela."),
            sistema="pulmao"),
        fundo=CENA,
    ),

    pagina("dia5", "Quinto dia de indução", "A madrugada do quinto dia",
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

    pergunta("p7", "Pergunta 11 · falha, complicação ou segunda doença",
        "Quinto dia de indução: febre com calafrio, procalcitonina de 0,4 para "
        "3,1, cateter com sítio inflamado. O que é?",
        [
            alt("Falha da indução",
                "É a leitura que o pânico sugere e a que mata. A hemoptise "
                "cessou, o infiltrado não piorou, e a procalcitonina subiu — "
                "ela separa razoavelmente inflamação estéril de infecção "
                "bacteriana."),
            alt("Infecção de corrente sanguínea pelo cateter",
                "**A causa de morte precoce na vasculite ANCA tratada é a "
                "infecção, não a vasculite.** Sítio inflamado, calafrio, "
                "procalcitonina em alta e órgão-alvo estável compõem "
                "bacteremia de cateter — e retirar o cateter faz parte do "
                "tratamento, não da investigação.", certa=True),
            alt("Febre do próprio glicocorticoide",
                "Corticoide em dose alta abaixa a temperatura e mascara febre; "
                "atribuir a ele um pico de 38,9 com calafrio e hipotensão é "
                "inverter a farmacologia."),
            alt("Pneumonia associada à ventilação",
                "Ele nunca foi intubado — está em cateter nasal — e o "
                "infiltrado não piorou. A porta de entrada está visível no "
                "pescoço dele."),
            alt("Recidiva da hemorragia alveolar",
                "Recidiva no quinto dia de corticoide em dose plena é rara, e "
                "ela viria com hemoptise e queda de hemoglobina. Nenhuma das "
                "duas aconteceu."),
        ],
        titulo_resposta="Nas primeiras semanas, o que mata é o tratamento",
        fundo=CENA,
    ),

    pagina("dia10", "Décimo dia de indução", "As hemoculturas e o cateter",
        p("As hemoculturas pareadas, do cateter e de veia periférica, vieram "
          "positivas para **//Staphylococcus aureus// sensível a oxacilina**, "
          "com tempo diferencial de positivação compatível com origem no "
          "cateter. O cateter foi retirado, a ponta cultivou o mesmo agente, e "
          "ele está em oxacilina. O ecocardiograma transesofágico não mostrou "
          "vegetação."),
        p("A febre cedeu em 48 horas. O que vem a seguir depende do esquema de "
          "indução que foi escolhido — e é aqui que os três caminhos deixam de "
          "ser o mesmo caso."),
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
        quadro("O que este caminho custou",
            p("A infecção aconteceu assim mesmo — porque metilprednisolona em "
              "pulso e prednisona em dose plena bastam para produzi-la. O que "
              "o rituximabe evitou foi **somar neutropenia** a um paciente já "
              "bacterêmico."),
            sistema="sangue"),
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
        quadro("O que este caminho custou",
            p("Uma bacteremia de cateter num paciente com 1.400 neutrófilos é "
              "um problema tratável. A mesma bacteremia com 200 neutrófilos é "
              "outro evento — e a única coisa que separa os dois cenários é a "
              "conta que foi feita antes de prescrever."),
            sistema="sangue"),
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
        quadro("O que este caminho custou",
            p("A mesma bacteremia de cateter, num paciente com 210 neutrófilos, "
              "virou choque séptico. A vasculite respondeu igual nos três "
              "caminhos — o que mudou não foi a doença, foi a medula."),
            sistema="sangue"),
        fundo=CENA, segue="d_cfx_plena",
    ),

    # ═══════════════════════ desfechos ═══════════════════════

    desfecho("d_rituximabe", "Alta no vigésimo primeiro dia, sem diálise",
        p("A creatinina, que havia chegado a 4,6 mg/dL, caiu de forma "
          "sustentada e estava em **1,9 mg/dL** na alta, com diurese "
          "recuperada e sem necessidade de diálise em nenhum momento. A "
          "saturação estava em 96% em ar ambiente."),
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

    desfecho("d_cfx_ajustada", "Alta no vigésimo sexto dia, sem diálise",
        p("A creatinina estabilizou em **2,3 mg/dL** e a diurese se recuperou. "
          "O hemograma foi vigiado duas vezes por semana durante a bacteremia "
          "e o nadir do segundo pulso foi de 1.600 neutrófilos."),
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

    desfecho("d_cfx_plena", "Alta no trigésimo quarto dia, após a terapia intensiva",
        p("A vasculite respondeu como nos outros dois caminhos: a hemoptise "
          "cessou no terceiro dia e a creatinina caiu para **2,6 mg/dL**. O "
          "que mudou foi o resto. Foram treze dias de terapia intensiva, "
          "noradrenalina por quatro deles, antibiótico de amplo espectro, "
          "antifúngico empírico e fator estimulador de colônias."),
        p("Saiu andando, com creatinina de 2,6 e uma internação de 34 dias. "
          "Nenhuma das três decisões que fizeram a diferença tinha a ver com "
          "o diagnóstico."),
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
        p("O caso ramificou em dois lugares. O primeiro foi silencioso: quem "
          "pediu a biópsia renal e o ANCA discutiu o mecanismo; quem não pediu "
          "discutiu como conduzir sem ele. O segundo foi a escolha da segunda "
          "droga — e a tabela compara os três, inclusive os que você não "
          "seguiu."),
        tabela(["Caminho", "A conta que ele exige",
                "Neutrófilos no 10º dia", "Desfecho"], [
            ["A · Rituximabe 375 mg/m² semanal",
             "Nenhuma correção para a filtração",
             "4.100", "Alta no 21º dia · creatinina 1,9"],
            ["B · Ciclofosfamida 10 mg/kg",
             "15 − 2,5 (idade) − 2,5 (creatinina)",
             "1.400", "Alta no 26º dia · creatinina 2,3"],
            ["C · Ciclofosfamida 15 mg/kg",
             "Nenhuma — e é esse o ponto",
             "210", "Alta no 34º dia · 13 dias de terapia intensiva"],
        ]),
        quadro("O que a comparação mostra",
            p("**A vasculite respondeu nos três.** A bacteremia de cateter "
              "aconteceu nos três, porque o glicocorticoide é o mesmo nos "
              "três. A diferença inteira está na profundidade da neutropenia "
              "quando essa infecção chegou — e ela foi decidida por uma "
              "subtração de duas parcelas, feita ou não feita antes de "
              "prescrever."),
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
        p("O diagnóstico foi feito no quinto dia de internação, com biópsia e "
          "sorologia. A pergunta útil é outra: em que momento, antes disso, a "
          "informação já estava disponível — e o que impediu que fosse usada."),
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

    pagina("procedencia", "Procedência e créditos", "De onde vem cada coisa",
        grade(
            quadro("O caso",
                p("**Autoral, curso simulado.** O paciente é ficcional e "
                  "nenhum ramo deste caso é o curso real de uma pessoa: cada "
                  "desfecho é inferência fisiológica escrita para ensino, e "
                  "não extração de artigo. Os números foram desenhados para "
                  "fechar entre si — gasometria por Henderson-Hasselbalch, "
                  "filtração por CKD-EPI 2021, relação PaO₂/FiO₂ calculada."),
                sistema="geral")
            + quadro("As cenas do paciente",
                p("**Ilustração gerada por inteligência artificial** a partir "
                  "da descrição clínica deste caso. Não retrata pessoa real."),
                sistema="geral"),
            quadro("As imagens médicas",
                p("Reais, ilustrativas, de repositórios de licença aberta, e "
                  "**não pertencem a este paciente**. Radiografia de tórax: "
                  "Samir, Wikimedia Commons, CC BY-SA 3.0. Tomografia: "
                  "Hellerhoff, Wikimedia Commons, CC BY-SA 4.0. Ultrassom "
                  "renal: Hansen, Nielsen e Ewertsen, CC BY 4.0. Sedimento "
                  "urinário: Rian Kabir, CC BY 2.0. Glomérulo e córtex renal: "
                  "Nephron, CC BY-SA 3.0. Imunofluorescência: Simon Caulton, "
                  "CC BY-SA 3.0. As setas sobre a fotomicrografia são leitura "
                  "editorial deste caso."),
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
            colunas=2,
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

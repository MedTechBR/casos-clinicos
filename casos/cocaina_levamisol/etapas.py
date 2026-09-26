"""Vasculopatia por cocaína adulterada com levamisol: púrpura retiforme,
agranulocitose e ANCA atípico.

Alíquota → pergunta, na gramática do //New England//. Paciente ficcional;
os desfechos são cenários didáticos, não probabilidades. O nome da causa só
aparece depois da entrevista privada, na toxicologia; antes disso, o caso
anda pela síndrome (púrpura retiforme com febre, neutropenia isolada, ANCA
com dois alvos).
"""
from pathlib import Path
from motor.desenhos import chave_corpusculo
from motor.estudo_imagem import ecg, estudo
from motor.etapas import (
    alt, bifurcacao, caminho, capa, desfecho, grupo, lamina, op, p,
    pagina, par, pareamento, pedido, pergunta, quadro, resultados, tabela,
    vitais, topicos,
)
from motor.etapas import painel as painel_resultados

TITULO = 'À flor da pele'
RODAPE = 'Caso ficcional · ensino para internos e residentes'
COR = '#7c3aed'
IMG = Path(__file__).parent / 'img'
BANCO = []
CENA = 'cena.png'
CENA_HISTORIA = lamina(CENA, 'Cena ilustrativa',
    'Pessoa ficcional em atendimento. Não interpretar a cena como fotografia '
    'de lesão.',
    'Ilustração gerada por IA para paciente ficcional; não documenta lesões.')


def painel(ident, kicker, titulo, enunciado, grupos):
    """Os exames que a equipe fez nesta rodada, todos, com o laudo no botão."""
    exames = [o for g in grupos for o in g['o']]
    laminas = {}
    if any(o['e'] == 'Radiografia de tórax' for o in exames):
        laminas['Radiografia de tórax'] = lamina('rx_torax_normal.jpg',
            'Radiografia de tórax',
            'Imagem ilustrativa de outro adulto. Não há opacidade focal '
            'evidente; isso não exclui infecção precoce.',
            'Mikael Häggström · Wikimedia Commons · CC0.')
    return painel_resultados(ident, kicker, titulo, exames, fundo=CENA,
                             introducao=enunciado, laminas=laminas)


def q(ident, n, enunciado, opcoes, titulo, segue=''):
    return pergunta(ident, f'Pergunta {n}', enunciado,
        [alt(t, j, certa=c) for t, j, c in opcoes],
        fundo=CENA, titulo_resposta=titulo, segue=segue)


ETAPAS = [
    capa(TITULO, fundo=CENA,
         kicker='Caso interativo · 8 perguntas · 3 decisões',
         procedencia='Roteiro autoral; fontes e limites no fecho.'),

    pagina('historia', 'Admissão', 'Apresentação',
        p('Marina, 34 anos, procura o pronto-socorro acompanhada da irmã por '
          'manchas dolorosas nas coxas e febre. Trabalha em uma loja de '
          'roupas e, nos últimos dois dias, faltou ao turno porque o tecido '
          'da calça doía ao tocar a pele. Uma das áreas escureceu naquela '
          'manhã.'),
        p('Diz que nunca teve uma lesão "desse tamanho". Não refere falta de '
          'ar, dor torácica ou sangramento aparente. Está lúcida e relata a '
          'sequência dos sintomas.'),
        fundo=CENA, lamina_=CENA_HISTORIA),

    pagina('hda', 'Antes da admissão', 'História da doença atual',
        p('Três dias antes, notou duas áreas avermelhadas e dolorosas na face '
          'externa das coxas. Pensou em atrito da roupa; não recordava '
          'exercício, queda ou picada. Nas horas seguintes surgiram outras '
          'manchas próximas, mais escuras e de contorno irregular. A dor '
          'passou de incômodo ao toque para dor em repouso.'),
        p('Há mal-estar e dor nos punhos e tornozelos, sem inchaço articular '
          'visível. A febre começou no dia da consulta, com calafrios. Tomou '
          'paracetamol e não usou antibiótico nem pomada.'),
        fundo=CENA),

    pagina('antecedentes', 'História pessoal', 'Antecedentes e hábitos',
        p('Sem hipertensão, diabetes, doença renal ou autoimune conhecida. '
          'Nunca teve trombose ou sangramento prolongado. Uma gestação a '
          'termo, sem perdas. Apendicectomia na adolescência. A mãe tem '
          'hipotireoidismo.'),
        p('Não usa medicação contínua nem anticoncepcional hormonal e nega '
          'medicamento novo, inclusive antibiótico, anti-inflamatório ou '
          'fórmula para emagrecer. Fuma cinco cigarros por dia e bebe nos '
          'fins de semana; nega uso de drogas ilícitas. Sem viagem recente. '
          'A entrevista foi feita com a irmã presente.'),
        fundo=CENA),

    pagina('exame', 'Admissão', 'Exame físico',
        vitais(('PA', '108/68 mmHg', False), ('FC', '112 bpm', True),
               ('FR', '18 irpm', False), ('Temperatura', '38,6 °C', True),
               ('SpO₂', '98% em ar ambiente', False)),
        topicos(('Estado geral', 'Lúcida e orientada, com dor nas coxas.'),
                ('Cardiovascular e pulmonar', 'Ritmo regular, sem sopro. '
                 'Ausculta pulmonar limpa.'),
                ('Abdome', 'Indolor, sem massas ou visceromegalias.'),
                ('Pele e membros', 'Placas violáceas dolorosas na face lateral '
                 'das coxas, que não desaparecem à pressão, de bordas '
                 'anguladas e ramificadas; duas têm centro escurecido. Sem '
                 'bolhas ou crepitação. Pulsos distais presentes. Face e '
                 'mucosas sem lesões.'),
                ('Neurológico', 'Força e sensibilidade preservadas.')),
        fundo=CENA),

    q('q1', 1,
      'Placas purpúricas dolorosas, que não clareiam à pressão, de contorno '
      'ramificado e centro escuro, com febre e taquicardia. **Quais cinco** '
      'diagnósticos devem entrar no diferencial?', [
      ('Púrpura fulminante ou êmbolo séptico',
       'Febre, taquicardia e necrose em horas: a causa infecciosa é a que '
       'não pode esperar.', True),
      ('Vasculite associada a ANCA',
       'Oclui vasos dérmicos e produz púrpura necrótica; febre e artralgia '
       'cabem no quadro.', True),
      ('Crioglobulinemia',
       'Púrpura de membros inferiores com artralgia; no tipo I, a oclusão '
       'necrosa a pele.', True),
      ('Síndrome antifosfolípide',
       'Trombose de pequeno vaso dérmico dá esse desenho, mesmo sem '
       'trombose prévia conhecida.', True),
      ('Vasculopatia por droga ou adulterante',
       'Várias exposições causam vasculite ou oclusão cutânea; pede '
       'história de exposição detalhada.', True),
      ('Embolia de colesterol após manipulação arterial',
       'Exige aterosclerose extensa e, em geral, cateterismo recente; ela '
       'não tem nenhum dos dois.', False),
      ('Calcifilaxia de forma não urêmica',
       'Necrose retiforme dolorosa, mas quase sempre com doença renal '
       'avançada ou varfarina.', False),
      ('Púrpura trombocitopênica imune com sangramento cutâneo',
       'Plaqueta baixa dá petéquia plana, sem contorno ramificado nem '
       'necrose.', False),
      ('Celulite bacteriana extensa das coxas',
       'Eritema quente, que clareia à pressão e tem bordas mal '
       'definidas.', False),
      ('Eritema nodoso com paniculite dolorosa',
       'Nódulos na face anterior das pernas, sem púrpura e sem '
       'necrose.', False),
     ], 'Púrpura retiforme: oclusão de pequeno vaso dérmico'),

    pagina('hda2', 'Admissão', 'Sintomas associados',
        p('Nega sangramento gengival, epistaxe recente ou aumento do fluxo '
          'menstrual. Não percebeu inchaço nas pernas nem mudança na '
          'quantidade ou na cor da urina. Sem tosse, dor abdominal, diarreia '
          'ou ardor ao urinar.'),
        p('Perguntada sobre episódios anteriores, recorda manchas pequenas '
          'que desapareceram sem consulta alguns meses antes. Não guardou '
          'fotografias e não sabe precisar a duração.'),
        fundo=CENA),

    pagina('imagem_pele', 'Discussão visual', 'Morfologia das lesões',
        p('Observe esta fotografia de outro paciente. Descreva a cor, a '
          'distribuição e as diferenças de tamanho. O que é possível afirmar '
          'apenas pela imagem?'),
        '<details class="leitura"><summary>Revelar pontos de discussão</summary>'
        '<p>A fotografia mostra lesões purpúricas. Imagem isolada não permite '
        'avaliar palpabilidade ou resposta à digitopressão e não distingue, '
        'por si, causa plaquetária, inflamatória ou oclusiva. Esta figura é '
        'comparativa; não documenta as placas de Marina.</p></details>',
        fundo=CENA,
        lamina_=lamina('purpura.jpg', 'Púrpura: imagem comparativa',
                       'Fotografia de outro paciente, utilizada apenas para '
                       'discutir morfologia.',
                       'Hektor · Wikimedia Commons · CC BY-SA 3.0 · sem alterações.')),

    *ecg('ecg_evolucao',
         'Uma hora depois do antitérmico, Marina segue com dor e o pulso '
         'continua acelerado. A equipe obtém um ECG. Qual é o ritmo e quais '
         'dados clínicos você revê antes de atribuir uma causa?', IMG,
         'Febre, dor e hipovolemia produzem esse ritmo. O ECG não esclarece '
         'a causa das lesões cutâneas.'),

    q('q3', 2,
      'Febre de 38,6 °C, frequência cardíaca de 112 e púrpura necrótica em '
      'progressão. **Quais quatro** exames são os mais apropriados agora?', [
      ('Hemograma com contagem diferencial',
       'A contagem de neutrófilos define o risco infeccioso e o esquema de '
       'antibiótico.', True),
      ('Hemoculturas, dois pares, antes do antibiótico',
       'Púrpura fulminante e êmbolo séptico seguem na lista; depois do '
       'antibiótico, a cultura rende menos.', True),
      ('Coagulograma com fibrinogênio',
       'INR, TTPa e fibrinogênio separam consumo de coagulação de oclusão '
       'sem consumo.', True),
      ('Creatinina e exame de urina',
       'Vasculites e crioglobulinemia acometem o rim sem sintoma; a urina '
       'mostra cedo.', True),
      ('Ecocardiograma transesofágico imediato',
       'Sem sopro e sem cultura, ainda não há pergunta para o '
       'transesofágico responder.', False),
      ('Tomografia computadorizada das coxas',
       'Sem crepitação, bolha ou dor fora da lesão, a imagem não muda as '
       'primeiras horas.', False),
      ('Dímero-D isolado como triagem',
       'Sobe em infecção, trombose e inflamação; sozinho, não separa as '
       'hipóteses.', False),
      ('Eletroforese de proteínas séricas',
       'Procura paraproteína de crioglobulina tipo I, mas o resultado não '
       'muda as primeiras horas.', False),
     ], 'Primeira rodada: gravidade, infecção e coagulação'),

    painel('p1', 'A investigação inicial', 'O que a equipe pediu',
        'Hemograma, culturas e coagulação antes do antibiótico; rim, perfusão '
        'e imagem para completar a rodada.', [
        grupo('Sangue', 'sangue', [
            op('Hemograma diferencial',
               resultado='Leucócitos 900/µL · Neutrófilos absolutos 180/µL · '
                         'Hemoglobina 12,1 g/dL · Plaquetas 238.000/µL',
               referencia='Neutrófilos 1.500–7.500/µL', alterado=True),
            op('Hemoculturas iniciais',
               resultado='Dois conjuntos coletados antes do antibiótico; '
                         'incubação em andamento.', referencia='Sem crescimento'),
            op('Coagulograma',
               resultado='INR 1,0 · TTPa 29 s · Fibrinogênio 410 mg/dL',
               referencia='INR 0,8–1,2; TTPa 25–35 s; fibrinogênio 200–400 mg/dL'),
            op('Esfregaço periférico', resultado='Sem blastos ou esquizócitos.',
               referencia='Ausentes'),
        ]),
        grupo('Órgãos e perfusão', 'geral', [
            op('Creatinina inicial', resultado='0,9 mg/dL', referencia='0,6–1,1 mg/dL'),
            op('Urina inicial',
               resultado='0–2 hemácias/campo · Sem cilindros · Proteína negativa',
               referencia='0–3 hemácias/campo; sem cilindros patológicos'),
            op('Lactato', resultado='1,7 mmol/L', referencia='0,5–2,0 mmol/L'),
        ]),
        grupo('Outras hipóteses', 'pele', [
            op('Proteína C reativa', resultado='96 mg/L', referencia='<5 mg/L',
               alterado=True),
            op('Doppler arterial de pernas',
               resultado='Fluxos arteriais preservados, sem oclusão de grandes '
                         'vasos.', referencia='Fluxos preservados'),
            op('Radiografia de tórax',
               resultado='Sem opacidades focais ou derrame.',
               referencia='Sem alterações agudas'),
        ]),
    ]),

    pagina('hemograma', 'Interpretação', 'Risco imediato',
        p('O hemograma mostra **180 neutrófilos por microlitro** numa mulher '
          'febril: agranulocitose. Hemoglobina e plaquetas normais, esfregaço '
          'sem blastos. A causa ainda está aberta; reconhecer a síndrome muda '
          'a urgência.'),
        fundo=CENA, segue='q4'),
    q('q4', 3,
      'Neutrófilos de 180/µL, hemoglobina e plaquetas normais, esfregaço sem '
      'blastos, em mulher de 34 anos previamente hígida e febril. **Quais '
      'quatro** causas são as mais prováveis?', [
      ('Reação a droga ou tóxico',
       'Dipirona, antitireoidianos, clozapina e sulfas lideram; início '
       'abrupto e linhagem única combinam.', True),
      ('Consumo periférico por sepse',
       'Infecção grave consome neutrófilos mais rápido do que a medula '
       'repõe; é sinal de gravidade.', True),
      ('Lúpus eritematoso sistêmico',
       'Neutropenia autoimune, artralgia, febre e lesão vascular de pele '
       'cabem no mesmo quadro.', True),
      ('Infecção viral aguda',
       'Soroconversão pelo HIV e outras viroses deprimem neutrófilos; a '
       'sorologia entra na investigação.', True),
      ('Leucemia aguda em fase inicial',
       'Com hemoglobina, plaquetas e esfregaço normais, fica menos provável; '
       'medula se não recuperar.', False),
      ('Neutropenia étnica benigna',
       'Contagens estáveis acima de 1.000, sem infecção associada; não '
       'explica 180 com febre.', False),
      ('Síndrome de Felty',
       'Exige artrite reumatoide de longa data e esplenomegalia; ela não '
       'tem nenhuma das duas.', False),
      ('Deficiência de vitamina B12',
       'Atinge as três linhagens, com macrocitose; aqui só os neutrófilos '
       'caíram.', False),
      ('Hiperesplenismo por sequestro',
       'Sequestra mais de uma linhagem e exige baço palpável; o abdome '
       'está normal.', False),
      ('Neutropenia cíclica hereditária',
       'Começa na infância, com ciclos de cerca de 21 dias e aftas; não '
       'surge aos 34.', False),
     ], 'Neutropenia grave e isolada: causas adquiridas'),

    bifurcacao('b1', 'Decisão', 'Primeiras horas',
        'Marina continua febril, com 180 neutrófilos. O que você faz?', [
        caminho('Internar, colher e iniciar antibiótico endovenoso de amplo '
                'espectro em até uma hora', 'protecao',
                'Neutropenia febril profunda é emergência: antibiótico '
                'antipseudomonas na primeira hora, depois se discute a causa.',
                rotulo_curto='Tratar'),
        caminho('Adiar a abordagem sistêmica e observar as lesões', 'b2',
                'A hipótese de dermatose não afasta deterioração. O atraso '
                'aumenta risco, mas não determina o desfecho.',
                rotulo_curto='Adiar'),
    ], fundo=CENA),

    pagina('protecao', 'Conduta', 'Neutropenia febril',
        p('A equipe interna, mantém as culturas e inicia cefepima em até uma '
          'hora, acrescentando vancomicina pela lesão de pele e partes '
          'moles. Hemograma diário. Dipirona é retirada da prescrição.'),
        p('Mesmo a conduta adequada não impede toda infecção ou perda '
          'tecidual.'),
        fundo=CENA, segue='q5'),

    bifurcacao('b2', 'Decisão', 'Reavaliação',
        'Antes de sair, Marina apresenta calafrios e maior prostração. Ainda '
        'está lúcida e sem hipotensão.', [
        caminho('Rever a hipótese e internar', 'resgate',
                'A mudança clínica é motivo para reavaliar; o resgate pode '
                'evitar dano, sem garantia.', rotulo_curto='Resgatar'),
        caminho('Manter espera por exames eletivos', 'atraso',
                'A espera prolonga a exposição ao risco infeccioso.',
                rotulo_curto='Esperar'),
    ], fundo=CENA),

    pagina('resgate', 'Reavaliação', 'Retorno ao cuidado',
        p('A equipe muda a conduta, interna e inicia cefepima com '
          'vancomicina, seis horas depois do primeiro hemograma. O atraso '
          'pode ter consequências, mas não é possível inferir dano apenas '
          'da escolha anterior.'),
        fundo=CENA, segue='q5'),
    pagina('atraso', 'Evolução possível', 'Persistência',
        p('Neste curso ficcional, a febre persiste e Marina retorna no mesmo '
          'dia, com pressão arterial de 92/58 mmHg. É admitida e a equipe '
          'inicia cefepima e vancomicina, doze horas depois do primeiro '
          'hemograma, com expansão volêmica. Não houve choque inevitável: '
          'outros cursos seriam possíveis.'),
        fundo=CENA, segue='q5'),

    q('q5', 4,
      'Febre com 180 neutrófilos e necrose cutânea em progressão. **Quais '
      'três** afirmações sobre o antibiótico estão corretas?', [
      ('A primeira dose entra em até 60 minutos, colhidas as culturas',
       'Atraso na neutropenia febril aumenta a mortalidade; a coleta não '
       'pode atrasar a dose.', True),
      ('Um betalactâmico antipseudomonas em monoterapia é a base',
       'Cefepima, piperacilina-tazobactam ou meropeném; a cobertura de '
       '//Pseudomonas// define o esquema.', True),
      ('A lesão de pele e partes moles justifica acrescentar vancomicina',
       'É um dos critérios de acréscimo do consenso, ao lado de '
       'instabilidade e cateter.', True),
      ('Vancomicina empírica entra em toda neutropenia febril',
       'Só com critério específico: instabilidade, cateter, pneumonia, MRSA '
       'ou pele e partes moles.', False),
      ('O escore MASCC de baixo risco permite antibiótico oral em casa',
       'O escore foi validado em câncer e não pesa necrose cutânea em '
       'progressão.', False),
      ('Um aminoglicosídeo deve ser associado de rotina',
       'Não reduz mortalidade e soma nefrotoxicidade; fica para '
       'instabilidade ou suspeita de resistência.', False),
      ('O fator estimulador de colônias substitui o antibiótico',
       'Pode encurtar a agranulocitose por droga, mas não trata a infecção '
       'presente.', False),
     ], 'Neutropenia febril: tempo e espectro'),

    pagina('evolucao', 'Segundo momento', 'Evolução',
        p('Na internação, Marina dorme após analgesia, mas sente dor na troca '
          'dos curativos. Algumas placas ficaram mais ramificadas e com centro '
          'mais escuro, sem crepitação. No reexame da manhã há uma placa '
          'purpúrica pequena e dolorosa na hélice da orelha esquerda, que não '
          'estava lá na admissão.'),
        p('Ao levantar para o banheiro, percebe a urina mais escura e avisa '
          'a enfermagem. A equipe registra "urina escura", sem convertê-la '
          'automaticamente em hematúria.'),
        fundo=CENA),

    painel('p2', 'Mecanismo e extensão', 'O que a equipe pediu',
        'As placas mudaram, surgiu lesão na orelha e a urina escureceu: '
        'tecido, anticorpos, rim e os diferenciais da oclusão.', [
        grupo('Tecido e marcadores', 'pele', [
            op('Biópsia cutânea',
               resultado='Trombos em pequenos vasos dérmicos · Necrose '
                         'epidérmica · Leucocitoclasia focal',
               referencia='Sem trombos ou necrose', alterado=True),
            op('ANCA por imunofluorescência',
               resultado='Padrão perinuclear 1:1.280', referencia='Negativo',
               alterado=True),
            op('Anti-MPO', resultado='128 U/mL',
               referencia='<20 U/mL neste ensaio', alterado=True),
            op('Anti-PR3', resultado='46 U/mL',
               referencia='<20 U/mL neste ensaio', alterado=True),
        ]),
        grupo('Rim', 'rim', [
            op('Creatinina de reavaliação', resultado='1,6 mg/dL',
               referencia='0,6–1,1 mg/dL', alterado=True),
            op('Sedimento urinário',
               resultado='50 hemácias/campo · Dismorfismo eritrocitário · '
                         'Cilindros hemáticos',
               referencia='0–3 hemácias/campo; sem cilindros hemáticos',
               alterado=True),
            op('Complemento C3', resultado='104 mg/dL', referencia='90–180 mg/dL'),
        ]),
        grupo('Diferenciais', 'geral', [
            op('Crioglobulinas',
               resultado='Não detectadas; amostra transportada aquecida.',
               referencia='Não detectadas'),
            op('Anticardiolipina IgG', resultado='8 GPL-U/mL',
               referencia='<20 GPL-U/mL'),
            op('Antígeno e anticorpos HIV', resultado='Não reagente',
               referencia='Não reagente'),
        ]),
    ]),

    pagina('tecido', 'Interpretação', 'Mecanismo',
        p('A biópsia sustenta lesão vascular com componente trombótico e '
          'leucocitoclasia focal. O tecido não identifica a substância '
          'causal e não define, sozinho, anticoagulação ou imunossupressão. '
          'A creatinina subiu de 0,9 para 1,6 mg/dL, com cilindros '
          'hemáticos.'),
        fundo=CENA, segue='q6'),
    q('q6', 5,
      'p-ANCA 1:1.280 com anti-MPO de 128 e anti-PR3 de 46 U/mL, C3 normal '
      'e crioglobulinas não detectadas em amostra transportada aquecida. '
      '**Quais duas** afirmações estão corretas?', [
      ('A dupla positividade é incomum nas vasculites primárias',
       'MPO e PR3 juntos aparecem em poucos por cento delas e são mais '
       'frequentes na forma induzida.', True),
      ('O padrão pede história de exposição a droga ou tóxico',
       'É a assinatura das vasculites induzidas; a história de exposição '
       'precisa ser refeita, a sós.', True),
      ('Confirma granulomatose com poliangeíte, pelo anti-PR3 positivo',
       'GPA costuma ter c-ANCA anti-PR3 isolado; anti-MPO junto foge do '
       'padrão.', False),
      ('Confirma poliangeíte microscópica, pelo anti-MPO alto',
       'PAM é anti-MPO sem anti-PR3; a dupla positividade não é o perfil '
       'dela.', False),
      ('O C3 normal exclui crioglobulinemia nesta paciente',
       'O consumo típico é de C4; quem afasta aqui é a crioglobulina colhida '
       'a 37 °C.', False),
      ('O título de 1:1.280 indica vasculite mais grave e extensa',
       'Título de ANCA não mede atividade nem extensão; o órgão acometido '
       'mede.', False),
     ], 'ANCA com dois alvos'),

    pagina('preparo_entrevista', 'Evolução', 'Entrevista individual',
        p('Com os anticorpos em mãos, a médica volta ao quarto para refazer a '
          'história de exposição. Marina pede para conversar sem a irmã. '
          'Parece receosa ao retomar o episódio anterior de manchas e '
          'pergunta quem terá acesso às informações.'),
        p('A equipe oferece privacidade e explica como os dados serão usados '
          'no cuidado. Sozinha com a médica, Marina conta que há um aspecto '
          'da história que preferiu não mencionar.'),
        fundo=CENA),

    pagina('entrevista', 'Terceiro momento', 'Entrevista privada',
        p('Marina relata **uso intranasal de cocaína** cerca de 72 horas antes '
          'da admissão e, reconstruindo a cronologia, associa o episódio '
          'anterior de manchas ao mesmo contexto. Não conhece a composição do '
          'produto. Nega uso injetável.'),
        p('O relato muda a probabilidade das hipóteses, mas não confirma '
          'adulteração. A urina escura persiste, sem dispneia ou hemoptise.'),
        fundo=CENA),

    estudo('us_evolucao', 'Ultrassonografia renal',
        'Como a urina permanece escura e a creatinina subiu, a equipe '
        'acrescenta ultrassonografia. Observe o corte longitudinal. O que '
        'esse método pode esclarecer e quais mecanismos continuariam '
        'possíveis?',
        IMG / 'us_rim.jpg',
        'Rim de outro adulto. Asteriscos da fonte: um, coluna de Bertin; '
        'dois, pirâmide; três, córtex; quatro, seio renal. Os cálipers também '
        'são da fonte e não representam medidas da paciente.',
        'Hansen, Nielsen e Ewertsen · Wikimedia Commons · CC BY 4.0. Recorte prévio e setas adicionadas.',
        [
         ((495, 288), (620, 105), '**Córtex** renal (três asteriscos), de espessura preservada.', 12),
         ((447, 400), (720, 550), '**Seio renal** (quatro asteriscos), ecogênico, sem dilatação do sistema coletor.', -12),
         ((462, 345), (330, 160), '**Pirâmide medular** (dois asteriscos), hipoecoica: a diferenciação entre córtex e medula está preservada.', 12),
        ],
        ['Rins de dimensões preservadas, sem dilatação pielocalicial (laudo ficcional do caso).', 'Afastar obstrução não exclui lesão glomerular.']),

    painel('p3', 'Exposição e gravidade', 'O que a equipe pediu',
        'Com o relato de exposição e a lesão renal: toxicologia, o rim por '
        'dentro e a vigilância da infecção.', [
        grupo('Toxicologia', 'geral', [
            op('Benzoilecgonina urinária',
               resultado='Detectada por método confirmatório.',
               referencia='Não detectada', alterado=True),
            op('Levamisol urinário por LC-MS/MS',
               resultado='Não detectado na amostra tardia, coletada cerca de '
                         '96 h após o último uso relatado.',
               referencia='Não detectado'),
        ]),
        grupo('Rim', 'rim', [
            op('Creatinina atual', resultado='2,6 mg/dL',
               referencia='0,6–1,1 mg/dL', alterado=True),
            op('Relação proteína/creatinina urinária', resultado='1,2 g/g',
               referencia='<0,2 g/g', alterado=True),
            op('Biópsia renal',
               resultado='Glomerulonefrite necrosante com crescentes celulares '
                         '· Imunofluorescência pauci-imune',
               referencia='Sem necrose ou crescentes', alterado=True),
            op('Anti-MBG', resultado='Não reagente', referencia='Não reagente'),
        ]),
        grupo('Infecção e sangue', 'sangue', [
            op('Hemograma de controle',
               resultado='Neutrófilos absolutos 420/µL · Hemoglobina 11,7 g/dL '
                         '· Plaquetas 226.000/µL',
               referencia='Neutrófilos 1.500–7.500/µL', alterado=True),
            op('Novas hemoculturas',
               resultado='Sem crescimento em 48 h; coleta sob antibiótico.',
               referencia='Sem crescimento'),
            op('Cultura de tecido cutâneo',
               resultado='Sem crescimento bacteriano em 48 h; coleta sob '
                         'antibiótico.', referencia='Sem crescimento'),
        ]),
    ]),

    pagina('toxicologia', 'Interpretação', 'Janela de detecção',
        p('Os testes documentam exposição à cocaína, mas não documentam '
          'levamisol. O resultado negativo tardio não exclui o adulterante: '
          'a detecção depende de tempo, método e limite analítico.'),
        fundo=CENA, segue='q9'),
    q('q9', 6,
      'Cocaína intranasal 72 horas antes da admissão, púrpura de orelha, 180 '
      'neutrófilos, anti-MPO e anti-PR3. Sobre a síndrome associada ao '
      'levamisol, **quais quatro** afirmações estão corretas?', [
      ('Urina negativa após 96 horas não exclui a exposição',
       'Meia-vida de cerca de 5,6 horas; a urina só é útil nas primeiras 48 '
       'horas.', True),
      ('A benzoilecgonina urinária positiva identifica também o adulterante',
       'Identifica cocaína; o adulterante exige cromatografia com '
       'espectrometria de massa.', False),
      ('A agranulocitose é idiossincrática e associada ao HLA-B27',
       'Foi descrita no uso terapêutico do levamisol, com HLA-B27 como '
       'fator de risco.', True),
      ('A orelha é sítio típico, mas não exclusivo',
       'Orelhas, bochechas, nariz e coxas; crioglobulinemia e antifosfolípide '
       'também atingem a orelha.', True),
      ('Regride com abstinência e volta com reexposição',
       'A pele melhora em duas a três semanas; o ANCA pode levar meses.',
       True),
      ('A neutropenia decorre de sequestro esplênico por hiperesplenismo',
       'Não há baço palpável; o mecanismo é toxicidade medular '
       'imunomediada.', False),
      ('Imunossupressão intensa é necessária em todos os casos',
       'Fica para órgão ameaçado; pele e neutropenia costumam responder à '
       'abstinência.', False),
      ('A síndrome só ocorre quando a cocaína é aspirada',
       'Fumada, aspirada ou injetada, a cocaína adulterada leva o levamisol '
       'do mesmo modo.', False),
     ], 'Levamisol: detecção curta e curso reversível'),

    pareamento('q10', 'Pergunta 7',
      'Exposições que produzem vasculite ou vasculopatia. Associe cada uma à '
      'síndrome que ela costuma produzir.', [
      par('Levamisol, adulterando cocaína',
          'Púrpura retiforme de orelhas, agranulocitose e ANCA duplo',
          'O quadro deste caso; a pele regride em semanas de abstinência, o '
          'anticorpo em meses.'),
      par('Cocaína inalada por anos',
          'Lesão destrutiva de linha média, com ANCA anti-elastase',
          'Destrói septo e palato e imita a granulomatose com poliangeíte.'),
      par('Propiltiouracila por meses',
          'Vasculite anti-MPO com glomerulonefrite',
          'É a droga que mais induz ANCA; suspender é a base do tratamento.'),
      par('Hidralazina por anos',
          'Lúpus induzido, com anti-histona',
          'Dose alta e acetilação lenta aumentam o risco; parte tem também '
          'ANCA anti-MPO.'),
      par('Anfetaminas e metanfetamina',
          'Vasculite necrosante de vaso médio, tipo poliarterite',
          'Descrita em usuários, sem ANCA, com acometimento cerebral e '
          'sistêmico.'),
      ], opcoes=[
      'Púrpura retiforme de orelhas, agranulocitose e ANCA duplo',
      'Lesão destrutiva de linha média, com ANCA anti-elastase',
      'Vasculite anti-MPO com glomerulonefrite',
      'Lúpus induzido, com anti-histona',
      'Vasculite necrosante de vaso médio, tipo poliarterite',
      'Arterite de células gigantes',
      ], titulo_resposta='Exposição, vaso e anticorpo',
      nota='A opção que sobrou, arterite de células gigantes, não se associa '
           'a essas exposições e é rara antes dos 50 anos.',
      fundo=CENA),

    bifurcacao('b3', 'Decisão', 'Plano integrado',
        'Creatinina de 2,6, neutrófilos de 420, culturas negativas, '
        'abstinência iniciada. Escolha com base no seu prontuário.', [
        caminho('Avaliar rim e infecção em paralelo, com biópsia quando '
                'viável, e discutir imunossupressão pela ameaça ao órgão',
                'imagem_rim',
                'Investigar rim e infecção simultaneamente permite '
                'individualizar a terapia; ausência de biópsia não impede '
                'avaliação urgente.', rotulo_curto='Investigar e proteger'),
        caminho('Manter apenas cuidados da pele e abstinência',
                'reavaliacao_suporte',
                'Suporte é central, mas pode ser insuficiente diante de '
                'sinais renais.', rotulo_curto='Só suporte'),
        caminho('Iniciar pulso de metilprednisolona sem reavaliar infecção',
                'vigilancia_infecciosa',
                'Aumenta risco infeccioso sem esclarecer benefício. O curso '
                'adverso apresentado é possível, não inevitável.',
                rotulo_curto='Pulso isolado'),
    ], fundo=CENA),

    pagina('imagem_rim', 'Discussão visual', 'Corpúsculo renal',
        p('Localize o tufo capilar e o espaço urinário. Em qual '
          'compartimento se inicia a filtração? Que observações urinárias '
          'sugerem lesão nessa barreira?'),
        '<details class="leitura"><summary>Revelar pontos de discussão</summary>'
        '<p>A barreira de filtração separa sangue e espaço urinário. '
        'Hematúria glomerular e proteinúria precisam ser demonstradas e '
        'interpretadas em conjunto. Este esquema normal não substitui o '
        'sedimento nem demonstra o padrão de uma biópsia.</p></details>',
        chave_corpusculo(), fundo=CENA,
        lamina_=lamina('corpusculo.svg', 'Corpúsculo renal',
                       'Anatomia normal. 2: camada parietal; 4: espaço '
                       'urinário; 10: capilares.',
                       'Michał Komorniczak · Wikimedia Commons · CC BY-SA 3.0 · '
                       'sem alterações.')),

    pagina('painel_lab', 'Evolução laboratorial', '',
        '<div class="painel-lab">'
        + p('Na visita, a equipe compara as coletas da internação antes de '
            'definir a intensidade do tratamento.')
        + tabela(['Exame', 'Admissão', 'Controle atual', 'Referência'], [
            ['Neutrófilos absolutos', '180/µL', '420/µL', '1.500–7.500/µL'],
            ['Hemoglobina', '12,1 g/dL', '11,7 g/dL', '12–16 g/dL'],
            ['Plaquetas', '238.000/µL', '226.000/µL', '150.000–450.000/µL'],
            ['Creatinina', '0,9 mg/dL', '2,6 mg/dL', '0,6–1,1 mg/dL'],
            ['Proteína/creatinina urinária', 'não dosada', '1,2 g/g', '<0,2 g/g'],
            ['Hemoculturas', 'Negativas', 'Negativas em 48 h', 'Negativas'],
        ]) + '</div>',
        fundo=CENA, so_kicker=True),

    q('q11', 8,
      'Glomerulonefrite crescêntica pauci-imune, creatinina de 2,6, '
      'neutrófilos de 420 em alta, culturas negativas, abstinência há cinco '
      'dias. **Quais três** afirmações orientam o tratamento?', [
      ('A abstinência é a base para pele e medula',
       'Nas séries, lesões e neutropenia regridem sem imunossupressor quando '
       'a exposição cessa.', True),
      ('Crescentes celulares justificam imunossupressão, com cobertura '
       'infecciosa',
       'A pele pode esperar; o glomérulo com crescente ativo, não.', True),
      ('O ANCA persiste por meses e não guia a duração',
       'O anticorpo persiste após a remissão; creatinina, sedimento e '
       'proteinúria guiam o seguimento.', True),
      ('Troca plasmática de rotina pela creatinina de 2,6',
       'Sem evidência nesta síndrome; na vasculite primária, o PEXIVAS não '
       'mostrou benefício de rotina.', False),
      ('Manutenção por dois anos, como na vasculite primária',
       'Na forma induzida, a recidiva vem da reexposição; manutenção longa '
       'não tem base.', False),
      ('Anticoagulação plena pela trombose de pequeno vaso',
       'Sem antifosfolípide comprovado não há indicação, e ela acabou de '
       'fazer biópsia renal.', False),
      ('Ciclofosfamida em dose plena, sem ajuste pelos leucócitos',
       'Os protocolos ajustam a dose pela contagem de leucócitos; ela ainda '
       'está neutropênica.', False),
     ], 'Tratamento guiado pelo órgão ameaçado'),

    pagina('plano_conjunto', 'Evolução', 'Avaliação conjunta',
        p('Nefrologia, infectologia e reumatologia discutem gravidade, '
          'segurança da imunossupressão e o antimicrobiano em curso. Marina '
          'pergunta se cuidar do rim significa diálise. A resposta é '
          'vinculada à evolução da creatinina, não ao aspecto da urina.'),
        fundo=CENA, segue='renal'),

    pagina('renal', 'Plano', 'Tratamento dirigido',
        p('Com biópsia renal disponível, a equipe define a imunossupressão '
          'pela lesão glomerular e mantém a cobertura infecciosa enquanto '
          'os neutrófilos sobem. Sem a biópsia, a decisão ficaria em aberto.'),
        fundo=CENA, segue='seguimento_recuperacao'),

    pagina('reavaliacao_suporte', 'Evolução', 'Reavaliação das lesões',
        p('Após analgesia e proteção das lesões, Marina tolera melhor a '
          'troca de roupa. Algumas áreas escuras permanecem bem delimitadas. '
          'A urina continua escura, e a creatinina, subindo.'),
        fundo=CENA, segue='suporte'),
    pagina('suporte', 'Plano', 'Extensão não resolvida',
        p('Curativos, analgesia e interrupção da exposição são mantidos. '
          'Urina escura com creatinina em ascensão requer avaliação além da '
          'pele. O grau de certeza sobre a extensão depende do que foi '
          'investigado.'),
        fundo=CENA, segue='fim_sequela'),

    pagina('seguimento_recuperacao', 'Evolução', 'Evolução na enfermaria',
        p('Depois do tratamento dirigido, o estado geral melhora e não '
          'surgem novas placas. As áreas já necrosadas persistem e exigem '
          'cuidados locais. Os neutrófilos passam de 1.000 no décimo dia, e '
          'a creatinina começa a cair.'),
        p('Marina participa das trocas de curativo e aprende a reconhecer '
          'sinais de piora. Os retornos renal, hematológico e cutâneo são '
          'articulados antes da alta.'),
        fundo=CENA, segue='fim_recuperacao'),

    desfecho('fim_recuperacao', 'Recuperação parcial',
        p('A biópsia permitiu tratar a lesão glomerular pauci-imune. Neste '
          'curso possível, após terapia individualizada e vigilância '
          'infecciosa, Marina melhora e mantém seguimento renal e de '
          'feridas. A recuperação completa da função renal permanece '
          'incerta.'),
        qualidade='melhor',
        porque='O manejo dirigido pode limitar dano ativo, mas não garante '
               'reversão de tecido já lesado.',
        fundo=CENA, fecho='incerteza'),
    desfecho('fim_sequela', 'Lesão persistente',
        p('Neste curso possível, a limitação ao cuidado cutâneo é revista '
          'após persistência dos sintomas. Marina necessita tratamento '
          'especializado e acompanhamento prolongado, com função renal '
          'residual menor do que teria com o tratamento precoce.'),
        qualidade='medio',
        porque='O atraso amplia o dano orgânico. A gravidade inicial também '
               'influencia a evolução.',
        fundo=CENA, fecho='incerteza'),
    pagina('vigilancia_infecciosa', 'Evolução', 'Reavaliação clínica',
        p('Após o pulso nesta rota, Marina volta a apresentar calafrios e '
          'responde mais lentamente. As extremidades esfriam, a frequência '
          'cardíaca sobe e a equipe é chamada para nova avaliação.'),
        p('É iniciada abordagem de deterioração, com revisão do suporte, '
          'pesquisa de foco e reavaliação dos antimicrobianos.'),
        fundo=CENA, segue='fim_infeccao'),
    desfecho('fim_infeccao', 'Complicação infecciosa',
        p('Neste curso possível, Marina desenvolve deterioração compatível '
          'com infecção e precisa de suporte intensivo. Sem cultura '
          'positiva, não se atribui um microrganismo. A evolução final '
          'permanece aberta.'),
        qualidade='pior',
        porque='Imunossupressão sem reavaliar infecção pode agravá-la; a '
               'associação não determina que todo paciente terá este curso.',
        fundo=CENA, fecho='incerteza'),
    pagina('incerteza', 'Fecho clínico', 'Diagnóstico provável',
        p('O conjunto clínico e a exposição relatada sustentam vasculopatia '
          'provavelmente associada à cocaína, com suspeita de participação '
          'do levamisol. O grau de sustentação depende dos exames '
          'escolhidos. A exposição ao adulterante não foi confirmada.'),
        p('Olhando para trás: púrpura retiforme com febre, agranulocitose '
          'isolada, lesão nova na orelha e ANCA com dois alvos já pediam a '
          'história de exposição refeita a sós, antes de a creatinina chegar a '
          '2,6 mg/dL.'),
        fundo=CENA),

    pagina('continuidade_cuidado', 'Evolução', 'Continuidade do cuidado',
        p('Marina manifesta preocupação com o trabalho, a filha e a '
          'exposição de informações pessoais. Autoriza a participação da '
          'irmã no planejamento e combina quem a acompanhará nos retornos.'),
        p('O plano registra a hipótese clínica, a situação das feridas e a '
          'avaliação renal, e oferece cuidado para interrupção da exposição '
          'sem condicionar o acolhimento à abstinência.'),
        fundo=CENA),

    pagina('fontes', 'Fontes e revisão', 'Evidência e limites',
        p('Fontes primárias abertas: '
          '<a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC2780984/" '
          'target="_blank" rel="noopener">Knowles 2009</a>; '
          '<a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC2802606/" '
          'target="_blank" rel="noopener">Wiens 2010</a>; '
          '<a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC3255368/" '
          'target="_blank" rel="noopener">McGrath 2011</a>; '
          '<a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC3573092/" '
          'target="_blank" rel="noopener">Vasculopatia com confirmação analítica</a>; '
          '<a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC4602417/" '
          'target="_blank" rel="noopener">Carlson 2014</a>; '
          '<a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC9154317/" '
          'target="_blank" rel="noopener">Ensaio de neutropenia febril 2022</a>.'),
        p('Neutropenia febril: IDSA 2010 (Freifeld e cols.) e ASCO/IDSA 2018 '
          '(Taplitz e cols.). Troca plasmática: PEXIVAS (Walsh e cols., 2020). '
          'Levamisol: meia-vida de cerca de 5,6 h; a pesquisa urinária é útil '
          'até cerca de 48 h após o uso. Séries e relatos não demonstram '
          'superioridade da imunossupressão ou do G-CSF nesta síndrome; o '
          'manejo antimicrobiano é extrapolado da neutropenia febril '
          'oncológica. Dados, cronologia e desfechos são ficcionais; a cena '
          'é ilustrativa.'),
        fundo=CENA),
]

REVISAO = []

"""Vasculopatia por cocaína adulterada com levamisol — púrpura retiforme,
agranulocitose e ANCA atípico.

Alíquota → pergunta, na gramática do //New England//. Paciente ficcional;
os desfechos são cenários didáticos, não probabilidades.
"""
from pathlib import Path
from motor.desenhos import chave_corpusculo
from motor.estudo_imagem import ecg, sequencia
from motor.etapas import (
    alt, bifurcacao, caminho, capa, desfecho, grupo, lamina, op, p,
    pagina, par, pareamento, pedido, pergunta, quadro, resultados, tabela,
    vitais, topicos,
)

TITULO = 'À flor da pele'
RODAPE = 'Caso ficcional · ensino para internos e residentes'
IMG = Path(__file__).parent / 'img'
BANCO = []
CENA = 'cena.png'
CENA_HISTORIA = lamina(CENA, 'Cena ilustrativa',
    'Pessoa ficcional em atendimento. Não interpretar a cena como fotografia '
    'de lesão.',
    'Ilustração gerada por IA para paciente ficcional; não documenta lesões.')


def painel(ident, kicker, titulo, enunciado, grupos):
    return pedido(ident, kicker, titulo, enunciado, grupos, fundo=CENA,
                  banco=BANCO, limite=4)


def q(ident, n, enunciado, opcoes, titulo, segue=''):
    return pergunta(ident, f'Pergunta {n}', enunciado,
        [alt(t, j, certa=c) for t, j, c in opcoes],
        fundo=CENA, titulo_resposta=titulo, segue=segue)


ETAPAS = [
    capa(TITULO, fundo=CENA,
         kicker='Caso interativo · 12 perguntas · 3 rodadas de exames · 3 decisões',
         procedencia='Roteiro autoral; fontes e limites no fecho.'),

    pagina('historia', 'Admissão', 'Apresentação',
        p('Marina, 34 anos, procura atendimento acompanhada da irmã por '
          'manchas dolorosas nas coxas e febre. Trabalha em uma loja de '
          'roupas e, nos últimos dois dias, deixou de cumprir o turno porque '
          'o tecido da calça incomodava ao tocar a pele. Está preocupada com '
          'uma área que escureceu naquela manhã.'),
        p('Diz que nunca teve uma lesão "desse tamanho". Não refere falta de '
          'ar, dor torácica ou sangramento aparente. Está lúcida e relata a '
          'sequência dos sintomas.'),
        fundo=CENA, lamina_=CENA_HISTORIA),

    pagina('hda', 'Antes da admissão', 'História da doença atual',
        p('Três dias antes, notou duas áreas avermelhadas dolorosas na face '
          'externa das coxas. Pensou em atrito da roupa, mas não recordava '
          'exercício, queda ou picada. Nas horas seguintes surgiram outras '
          'manchas próximas, de cor mais escura, **com bordas angulosas e '
          'ramificadas**. A dor passou de incômodo ao toque para dor em '
          'repouso.'),
        p('Havia mal-estar e dor nos punhos e tornozelos, sem articulação '
          'visivelmente inchada. A febre começou no dia da consulta, com '
          'calafrios. Tomou paracetamol depois do início dos sintomas e não '
          'usou antibiótico ou pomada.'),
        fundo=CENA),

    q('q1', 1,
      'Placas purpúricas dolorosas, de contorno ramificado, com centro '
      'escurecido, nas coxas de uma mulher de 34 anos com febre. **Quais '
      'quatro** diagnósticos considerar?', [
      ('Vasculopatia trombótica por cocaína adulterada com levamisol',
       'Púrpura retiforme dolorosa, em mulher jovem, com artralgia e febre: '
       'é a apresentação clássica — e as coxas são sítio comum, junto com '
       'orelhas, nariz e bochechas. Pergunte pela droga, a sós.', True),
      ('Eritema nodoso',
       'Nódulos eritematosos, não purpúricos, na face anterior das '
       'pernas. Não necrosa nem ramifica.', False),
      ('Púrpura fulminante por coagulação intravascular disseminada',
       'Febre com púrpura que necrosa em horas é meningococcemia até prova '
       'em contrário. Hemocultura e antibiótico antes de qualquer '
       'raciocínio elegante.', True),
      ('Celulite bacteriana',
       'Eritema quente, branqueável, de bordas mal definidas — não '
       'púrpura angulada com centro necrótico.', False),
      ('Crioglobulinemia mista',
       'Púrpura de membros inferiores com artralgia e, na tipo I, '
       'oclusão com necrose. Hepatite C e paraproteína na investigação.',
       True),
      ('Necrose cutânea por varfarina',
       'Necrose de coxa e mama nos primeiros dias de anticoagulante — ela '
       'não usa nenhum.', False),
      ('Síndrome antifosfolípide',
       'Livedo, púrpura retiforme e necrose por trombose de pequeno vaso. '
       'Anticoagulante lúpico e anticardiolipina entram na lista.', True),
      ('Urticária vasculite',
       'Placas urticariformes que duram mais de 24 horas e deixam '
       'pigmento — sem necrose ramificada.', False),
      ('Calcifilaxia',
       'Necrose retiforme dolorosa, sim — mas em doença renal terminal '
       'com hiperparatireoidismo. Ela tem 34 anos e creatinina normal.',
       False),
     ], 'Púrpura que ramifica é vaso ocluído, e quatro coisas ocluem'),

    pagina('hda2', 'Admissão', 'Sintomas associados',
        p('Nega sangramento gengival, epistaxe recente ou aumento do fluxo '
          'menstrual. Não percebeu inchaço nas pernas nem mudança na '
          'quantidade ou na cor da urina. Sem tosse, dor abdominal, diarreia '
          'ou ardor ao urinar.'),
        p('Perguntada sobre episódios anteriores, recorda manchas pequenas '
          'que desapareceram sem consulta alguns meses antes. Não guardou '
          'fotografias e não sabe precisar a duração.'),
        fundo=CENA),

    q('q2', 2,
      'Lesões purpúricas ramificadas, de bordas angulares, com centro '
      'necrótico. Qual termo descreve melhor essa morfologia — e o que ele '
      'implica?', [
      ('Púrpura retiforme: oclusão do vaso, mais que inflamação',
       'Retiforme é o desenho da rede vascular desenhado pela oclusão: '
       'trombo, êmbolo, crioglobulina, calcifilaxia, levamisol. A biópsia '
       'procura trombo antes de procurar vasculite.', True),
      ('Púrpura palpável: vasculite leucocitoclástica',
       'Palpável é arredondada, de 2 a 10 mm, sem ramificação. É '
       'inflamação de vênula — outra anatomia e outro diferencial.', False),
      ('Livedo reticular: vasoespasmo fisiológico',
       'Livedo é rendilhado violáceo **sem** púrpura nem necrose, e some '
       'ao aquecer. Quando fixo e com necrose, chama-se livedo racemosa e '
       'aproxima-se da retiforme.', False),
      ('Eritema multiforme: lesão em alvo',
       'Alvo tem três zonas concêntricas e não necrosa a pele em rede.',
       False),
      ('Petéquias: sangramento plaquetário',
       'Puntiformes, não palpáveis, em áreas de pressão. Não ramificam.',
       False),
     ], 'Retiforme é o mapa do vaso que fechou'),

    pagina('antecedentes', 'História pessoal', 'Antecedentes e hábitos',
        p('Sem hipertensão, diabetes, doença renal ou autoimune conhecida. '
          'Nunca teve trombose ou sangramento prolongado. Uma gestação a '
          'termo, sem perdas. Apendicectomia na adolescência. A mãe tem '
          'hipotireoidismo.'),
        p('Não usa medicação contínua nem anticoncepcional hormonal. Nega '
          'medicamento novo — antibiótico, anti-inflamatório, fórmula para '
          'emagrecer — e nega dipirona nas últimas semanas. Fuma cinco '
          'cigarros por dia; álcool nos fins de semana. Sem viagem recente. '
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
                ('Pele e membros', 'Placas violáceas dolorosas nas coxas, '
                 '**não desaparecem à pressão**, de bordas anguladas e '
                 'ramificadas, algumas com centro escurecido. Pulsos '
                 'presentes, sem crepitação. Orelhas e nariz sem lesão no '
                 'primeiro exame.'),
                ('Neurológico', 'Força e sensibilidade preservadas.')),
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

    q('q3', 3,
      'Febre de 38,6 °C, frequência cardíaca de 112, lesões dolorosas com '
      'necrose. **Quais três** medidas nas primeiras horas?', [
      ('Hemograma com diferencial, agora',
       'Púrpura necrótica com febre numa mulher jovem: o número que muda '
       'tudo é o de neutrófilos. Sem ele, não se sabe se a febre é de '
       'imunossuprimida.', True),
      ('Hemoculturas antes da primeira dose de antibiótico',
       'Meningococcemia e endocardite estão na lista, e a cultura só vale '
       'se for anterior ao antibiótico.', True),
      ('Corticoide empírico pela suspeita de vasculite',
       'Imunossuprimir uma febre sem hemograma e sem cultura é o erro que '
       'não se desfaz.', False),
      ('Delimitar as bordas e examinar a profundidade, com cirurgia à mão',
       'Dor desproporcional, necrose que avança em horas e crepitação são '
       'fasciite até prova em contrário. Marcar a borda com caneta custa '
       'nada e mostra a velocidade.', True),
      ('Anticoagulação plena empírica',
       'Trombo de pequeno vaso por levamisol ou crioglobulina não '
       'responde a heparina, e ela pode ter outra causa de sangrar.',
       False),
      ('Biópsia de pele antes de qualquer conduta',
       'Vem — mas depois de cultura e hemograma, e sem atrasar '
       'antibiótico.', False),
      ('Alta com analgésico e retorno em 48 horas',
       'Febre com necrose cutânea não sai do hospital sem hemograma.',
       False),
     ], 'Neutrófilos, cultura e a borda marcada com caneta'),

    *ecg('ecg_evolucao',
         'Na reavaliação, Marina mantém dor e febre; o pulso continua '
         'acelerado. A equipe obtém um ECG. Qual é o ritmo e quais dados '
         'clínicos você revê antes de atribuir uma causa?', IMG,
         'Febre, dor e outras causas de ativação simpática produzem esse '
         'ritmo. O ECG não identifica uma exposição nem estabelece a causa '
         'das lesões cutâneas.'),

    painel('p1', 'Exames · primeira rodada', 'Investigação inicial',
        'Febre e placas dolorosas não branqueáveis. Quatro exames para o '
        'risco sistêmico e os mecanismos da púrpura.', [
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

    resultados('r1', 'Primeira rodada', 'Resultados solicitados', 'p1',
        fundo=CENA,
        laminas={'Radiografia de tórax': lamina('rx_torax_normal.jpg',
                 'Radiografia de tórax',
                 'Imagem ilustrativa de outro adulto. Não há opacidade focal '
                 'evidente; isso não exclui infecção precoce.',
                 'Mikael Häggström · Wikimedia Commons · CC0.')},
        rota=dict(pediu=['Hemograma diferencial'], entao='hemograma',
                  senao='sem_hemograma')),

    pagina('hemograma', 'Interpretação', 'Risco imediato',
        p('O hemograma documenta **180 neutrófilos por microlitro** numa '
          'mulher febril: agranulocitose. Hemoglobina e plaquetas normais — '
          'a medula falhou numa linhagem só. A etiologia ainda está aberta; '
          'reconhecer a síndrome muda a urgência.'),
        fundo=CENA, segue='q4'),
    pagina('sem_hemograma', 'Interpretação', 'Reavaliação',
        p('Sem o diferencial, a febre e as lesões dolorosas continuam sem '
          'explicação suficiente. A enfermagem informa que o hemograma de '
          'rotina da admissão, colhido pelo protocolo, mostra **180 '
          'neutrófilos por microlitro**. A equipe recebe o número de quem '
          'não o pediu.'),
        fundo=CENA, segue='q4'),

    q('q4', 4,
      'Neutrófilos de 180/µL, com hemoglobina e plaquetas normais, em mulher '
      'de 34 anos previamente hígida e febril. **Quais quatro** causas devem '
      'ser consideradas?', [
      ('Agranulocitose induzida por droga ou tóxico',
       'Dipirona, propiltiouracila, clozapina, sulfa — e levamisol. Uma '
       'linhagem só, início abrupto, recuperação em uma a três semanas '
       'após retirar o agente. Pergunte por tudo, inclusive o que ela não '
       'chama de remédio.', True),
      ('Leucemia aguda',
       'Neutropenia isolada pode ser a primeira manifestação, e o '
       'esfregaço sem blasto não exclui. Se não recuperar em duas '
       'semanas, medula.', True),
      ('Neutropenia étnica benigna',
       'Contagens entre 1.000 e 1.500, estáveis, sem febre e sem '
       'infecção, em pessoa de ascendência africana ou do Oriente Médio. '
       '180 com febre não é isso.', False),
      ('Sepse com consumo medular',
       'Infecção grave pode consumir neutrófilos mais rápido do que a '
       'medula repõe — sobretudo com endotoxina. Neutropenia na sepse é '
       'sinal de gravidade.', True),
      ('Síndrome de Felty',
       'Exige artrite reumatoide de longa data com esplenomegalia. Ela não '
       'tem nenhuma das duas.', False),
      ('Lúpus eritematoso sistêmico',
       'Neutropenia autoimune, artralgia, febre e lesão cutânea vascular: '
       'o lúpus cabe nesta lista e pede FAN, complemento e '
       'antifosfolípide.', True),
      ('Deficiência de ferro',
       'Anemia, não neutropenia. Hemoglobina dela está normal.', False),
      ('Hipotireoidismo',
       'Não produz agranulocitose. A mãe tem, ela não.', False),
      ('Neutropenia cíclica',
       'Doença da infância, com ciclos de 21 dias e história de aftas '
       'recorrentes desde criança. Não começa aos 34.', False),
     ], 'Uma linhagem só, de repente: droga, tóxico, medula, sepse ou lúpus'),

    bifurcacao('b1', 'Decisão', 'Primeiras horas',
        'Marina continua febril, com 180 neutrófilos. O que você faz?', [
        caminho('Internar, colher e iniciar antibiótico endovenoso de amplo '
                'espectro em até uma hora', 'protecao',
                'Neutropenia febril profunda é emergência com relógio: '
                'antibiótico antipseudomonas na primeira hora, depois se '
                'discute a causa.', rotulo_curto='Tratar'),
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

    q('q5', 5,
      'Febre de 38,6 °C com 180 neutrófilos e lesão necrótica de pele. '
      '**Quais três** afirmações sobre o antibiótico estão corretas?', [
      ('A primeira dose deve entrar em até 60 minutos, depois das culturas',
       'Cada hora de atraso na neutropenia febril aumenta a mortalidade. '
       'Cultura sim, mas a cultura não pode atrasar a dose.', True),
      ('Um betalactâmico antipseudomonas em monoterapia é a base',
       'Cefepima, piperacilina-tazobactam ou meropeném: a cobertura de '
       '//Pseudomonas// é o que define o esquema da neutropenia febril.',
       True),
      ('Vancomicina empírica está indicada em toda neutropenia febril',
       'Não: só com instabilidade, cateter, pneumonia grave, colonização '
       'por MRSA ou **lesão de pele e partes moles** — que é o caso dela.',
       False),
      ('Vancomicina deve ser acrescentada pela lesão de pele e partes moles',
       'É exatamente o critério de acréscimo do consenso: infecção de '
       'pele e partes moles suspeita, com necrose.', True),
      ('É prudente aguardar o hemograma de controle antes da primeira dose',
       'O número já está na mão. Esperar outro é esperar a sepse.', False),
      ('Isolamento reverso e dieta neutropênica reduzem a infecção',
       'Sem evidência de benefício para os dois. Higiene de mãos, sim.',
       False),
      ('Fator estimulador de colônias substitui o antibiótico',
       'G-CSF pode encurtar a agranulocitose por droga; não trata a '
       'infecção que já está lá.', False),
     ], 'Uma hora, um betalactâmico antipseudomonas — e a pele pede vancomicina'),

    pagina('evolucao', 'Segundo momento', 'Evolução',
        p('Na internação, Marina dorme após analgesia, mas refere dor ao '
          'trocar os curativos. Algumas placas ganharam contornos mais '
          'ramificados e centro mais escuro, sem crepitação. Sem falta de ar.'),
        p('Ao levantar para o banheiro, percebe a **urina mais escura** pela '
          'primeira vez e avisa a enfermagem. Não sabe estimar o volume e '
          'não identifica sangue vivo. A equipe registra "urina escura", '
          'sem convertê-la automaticamente em hematúria.'),
        fundo=CENA),

    painel('p2', 'Exames · segunda rodada', 'Mecanismo e extensão',
        'As placas mudaram e apareceu urina escura. Quatro exames para o '
        'mecanismo cutâneo e para outro órgão acometido.', [
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

    resultados('r2', 'Segunda rodada', 'Resultados solicitados', 'p2',
        fundo=CENA,
        rota=dict(pediu=['Biópsia cutânea'], entao='tecido', senao='sem_tecido')),

    pagina('tecido', 'Interpretação', 'Mecanismo',
        p('A biópsia sustenta lesão vascular com componente trombótico e '
          'leucocitoclasia focal. O tecido não identifica a substância '
          'causal e não define, sozinho, anticoagulação ou imunossupressão.'),
        fundo=CENA,
        rota=dict(pediu=['Anti-MPO', 'Anti-PR3'], entao='q6', senao='q7')),
    pagina('sem_tecido', 'Interpretação', 'Hipóteses abertas',
        p('A aparência clínica permite mais de um mecanismo. Sem '
          'documentação tecidual, a linguagem continua de hipótese, e os '
          'próximos passos seguem a gravidade e o que realmente se tem.'),
        fundo=CENA,
        rota=dict(pediu=['Anti-MPO', 'Anti-PR3'], entao='q6', senao='q7')),

    q('q6', 6,
      'p-ANCA 1:1.280 com **anti-MPO 128 e anti-PR3 46 U/mL, os dois '
      'positivos**. Qual a interpretação mais adequada?', [
      ('Confirma granulomatose com poliangeíte',
       'GPA é anti-PR3 com padrão citoplasmático — e quase nunca com '
       'anti-MPO junto.', False),
      ('Confirma poliangeíte microscópica',
       'PAM é anti-MPO, sem anti-PR3. A dupla positividade não é o padrão '
       'dela.', False),
      ('Dupla positividade em título alto é atípica das vasculites '
       'primárias e aponta para exposição: levamisol, propiltiouracila, '
       'hidralazina',
       'Menos de 5% das vasculites primárias têm os dois anticorpos. '
       'Quando têm — sobretudo com anti-elastase —, a pergunta é "o que '
       'você usou", não "qual vasculite".', True),
      ('Indica doença anti-membrana basal concomitante',
       'Anti-MBG é outro anticorpo, contra outro alvo. Não está na frase.',
       False),
      ('Artefato de laboratório, a repetir',
       'Título de 1:1.280 com dois ELISA positivos não é artefato.', False),
     ], 'Dois alvos ao mesmo tempo é pergunta de exposição', segue='q7'),

    q('q7', 7,
      'Sobre a biópsia de pele na púrpura retiforme, **quais três** '
      'afirmações estão corretas?', [
      ('Trombo em vaso dérmico com leucocitoclasia focal é o padrão '
       'descrito na vasculopatia por levamisol',
       'Oclusão com pouca ou nenhuma inflamação, às vezes com vasculite '
       'leucocitoclástica ao lado: é a assinatura, embora não seja '
       'específica.', True),
      ('Leucocitoclasia focal confirma vasculite ANCA primária',
       'Leucocitoclasia é resto de neutrófilo. Aparece em vasculite por '
       'imunocomplexo, por droga, por infecção — não nomeia a causa.',
       False),
      ('Trombo sem vasculite exige procurar antifosfolípide, crioglobulina '
       'tipo I e coagulação intravascular',
       'A histologia da oclusão é a mesma; o que muda é o sangue. A '
       'biópsia manda de volta ao laboratório.', True),
      ('A imunofluorescência direta é dispensável',
       'É ela que mostra IgA (vasculite por IgA), imunocomplexo ou nada. '
       'Pele fresca, sem formol, em tubo próprio.', False),
      ('A biópsia deve ser da borda de uma lesão recente, profunda, '
       'incluindo tecido subcutâneo',
       'Retiforme é vaso de derme profunda e hipoderme: punch raso do '
       'centro necrótico mostra só necrose. Borda, recente, fundo.', True),
      ('A biópsia identifica o adulterante',
       'Nenhuma histologia identifica levamisol. Só a toxicologia — e só '
       'nas primeiras 48 horas.', False),
     ], 'Borda, recente, profunda — e com imunofluorescência'),

    pagina('evolucao_urinaria', 'Durante a internação', 'O rim entra em cena',
        p('A creatinina de controle da manhã, colhida na rotina, voltou '
          '**1,6 mg/dL** — era 0,9 três dias antes. A urina continua escura. '
          'Pressão arterial 122/78, sem edema.'),
        fundo=CENA),

    q('q8', 8,
      'Creatinina de 0,9 para 1,6 mg/dL em três dias, com urina escura. '
      '**Quais três** afirmações estão corretas?', [
      ('É lesão renal aguda KDIGO estágio 1',
       '1,6 ÷ 0,9 = 1,78 vezes a basal: estágio 1 vai de 1,5 a 1,9. '
       'Estágio 2 seria o dobro.', True),
      ('É lesão renal aguda KDIGO estágio 2',
       'Estágio 2 exige 2,0 a 2,9 vezes a basal. Ela está em 1,78.', False),
      ('Com sedimento ativo, é glomerulonefrite rapidamente progressiva '
       'até prova em contrário — e biópsia em dias, não em semanas',
       'Creatinina que sobe em dias com hemácia dismórfica e cilindro '
       'hemático é crescente até que a biópsia diga o contrário. A janela '
       'de tratamento é curta.', True),
      ('Necrose tubular por sepse é a explicação mais provável',
       'Sem hipotensão sustentada, sem nefrotóxico — e com púrpura '
       'retiforme e ANCA. O rim entrou pela mesma porta da pele.', False),
      ('A taxa de filtração por CKD-EPI é confiável agora',
       'CKD-EPI pressupõe creatinina em estado estável. Numa creatinina '
       'que sobe, a fórmula superestima a filtração — a real é menor.',
       False),
      ('Suspender anti-inflamatório e evitar contraste até esclarecer',
       'Nada de nefrotóxico enquanto o rim está sendo julgado. Se a '
       'tomografia for necessária, sem contraste.', True),
     ], 'Setenta e oito por cento acima da basal, em três dias'),

    pagina('preparo_entrevista', 'Evolução', 'Entrevista individual',
        p('No intervalo entre os cuidados, Marina pede para conversar sem a '
          'irmã. Parece receosa ao retomar o episódio anterior de manchas e '
          'pergunta quem terá acesso às informações.'),
        p('A equipe oferece privacidade e explica como os dados serão usados '
          'no cuidado. Quando fica sozinha com a médica, conta que há um '
          'aspecto da história que preferiu não mencionar.'),
        fundo=CENA),

    pagina('entrevista', 'Terceiro momento', 'Entrevista privada',
        p('Marina relata uso **intranasal de cocaína cerca de 72 horas antes '
          'da admissão** e, reconstruindo a cronologia, associa o episódio '
          'anterior de manchas ao mesmo contexto. Não conhece a composição '
          'do produto. No reexame, observa-se **pequena placa purpúrica no '
          'pavilhão da orelha esquerda**.'),
        p('O relato muda a probabilidade das hipóteses; não confirma '
          'adulteração. A urina escura persiste, sem dispneia ou hemoptise.'),
        fundo=CENA),

    *sequencia('us_evolucao', 'Ultrassonografia renal',
        'Como a urina permanece escura e a creatinina subiu, a equipe '
        'acrescenta ultrassonografia. Observe o corte longitudinal. O que '
        'esse método pode esclarecer e quais mecanismos continuariam '
        'possíveis?',
        IMG / 'us_rim.jpg',
        'Hansen, Nielsen e Ewertsen · Wikimedia Commons · CC BY 4.0. Recorte '
        'prévio e setas adicionadas na discussão.',
        'Rim de outro adulto. Asteriscos e cálipers são da fonte; não '
        'representam medidas da paciente.',
        [((524, 283), (620, 105)), ((447, 400), (720, 550))],
        ['1. A seta alcança o parênquima periférico, mais escuro que a '
         'região central.',
         '2. O seio renal é mais ecogênico. Neste corte, não há dilatação '
         'coletora evidente.',
         'O laudo ficcional descreve rins de dimensões preservadas, sem '
         'dilatação pielocalicial. A ausência de obstrução não exclui lesão '
         'glomerular.']),

    painel('p3', 'Exames · terceira rodada', 'Exposição e gravidade',
        'Com o relato de exposição e a lesão renal, quatro exames para '
        'esclarecer a associação e orientar o tratamento.', [
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
               referencia='Sem necrose ou crescentes', alterado=True,
               exige=['Sedimento urinário', 'Creatinina de reavaliação'],
               porque='a nefrologia punciona depois de documentar sedimento e '
                      'função renal'),
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

    resultados('r3', 'Terceira rodada', 'Resultados solicitados', 'p3',
        fundo=CENA,
        rota=dict(pediu=['Benzoilecgonina urinária',
                         'Levamisol urinário por LC-MS/MS'],
                  entao='toxicologia', senao='sem_toxicologia')),

    pagina('toxicologia', 'Interpretação', 'Janela de detecção',
        p('Os testes documentam exposição à cocaína, mas não documentam '
          'levamisol. O resultado negativo tardio não exclui o adulterante: '
          'a detecção depende de tempo, método e limite analítico.'),
        fundo=CENA, segue='q9'),
    pagina('sem_toxicologia', 'Interpretação', 'Limite da atribuição',
        p('O relato de uso sustenta a hipótese, mas não autoriza afirmar a '
          'composição do produto. Sem análise específica positiva, não se '
          'documenta confirmação de levamisol.'),
        fundo=CENA, segue='q9'),

    q('q9', 9,
      'Cocaína 72 horas antes, orelha com púrpura, 180 neutrófilos, '
      'anti-MPO e anti-PR3. Sobre a síndrome do levamisol, **quais quatro** '
      'afirmações estão corretas?', [
      ('O levamisol é detectável na urina por cerca de 48 horas; um exame '
       'negativo depois disso não exclui a exposição',
       'Meia-vida de 5,6 horas. A amostra de 96 horas era tarde demais — '
       'e é por isso que se pede no primeiro dia.', True),
      ('A benzoilecgonina identifica o adulterante',
       'Identifica cocaína. O que estava misturado a ela só a '
       'espectrometria de massa diz.', False),
      ('A tríade é púrpura retiforme (orelhas, nariz, bochechas), '
       'neutropenia e ANCA com anti-MPO e anti-PR3, muitas vezes com '
       'anti-elastase',
       'É a assinatura descrita desde 2009–2010, quando o levamisol '
       'passou a estar em mais de dois terços da cocaína apreendida nos '
       'Estados Unidos.', True),
      ('A lesão de orelha é patognomônica',
       'Crioglobulinemia, antifosfolípide, lúpus pérnio e congelamento '
       'também acometem orelha. Sugestiva, não exclusiva.', False),
      ('A agranulocitose é idiossincrática e associada ao HLA-B27',
       'Descrita desde o uso do levamisol como imunomodulador nos anos '
       '1970: agranulocitose em 2,5 a 13% dos tratados, com o HLA-B27 como '
       'fator de risco.', True),
      ('A neutropenia é por hiperesplenismo',
       'Não há esplenomegalia. É toxicidade medular, imunomediada.',
       False),
      ('As lesões e a neutropenia melhoram com a abstinência, e '
       'recorrem com a reexposição',
       'Duas a três semanas de abstinência resolvem a maioria das lesões '
       'cutâneas; o ANCA leva meses. Cada nova exposição reabre.', True),
      ('Imunossupressão intensa é sempre necessária',
       'Só quando há órgão ameaçado — rim, pulmão. Pele e neutropenia '
       'respondem à abstinência.', False),
      ('A síndrome só ocorre com uso intranasal',
       'Fumada, injetada ou aspirada: o levamisol chega do mesmo jeito.',
       False),
     ], 'Quarenta e oito horas para detectar; três semanas para melhorar'),

    pareamento('q10', 'Pergunta 10',
      'Substâncias que fabricam vasculite. Associe cada exposição à síndrome '
      'que ela produz.', [
      par('Levamisol, adulterando cocaína',
          'Púrpura retiforme de orelhas, agranulocitose e ANCA duplo',
          'A tríade deste caso. A pele fecha em semanas de abstinência; o '
          'anticorpo, em meses.'),
      par('Cocaína pura, inalada por anos',
          'Lesão destrutiva de linha média nasal, com anti-elastase',
          'A cocaína sem adulterante corrói septo e palato — a lesão '
          'destrutiva de linha média — e produz ANCA contra a elastase de '
          'neutrófilo, que imita a granulomatose com poliangeíte.'),
      par('Propiltiouracila por meses',
          'Vasculite ANCA anti-MPO induzida por droga',
          'A tionamida é a droga que mais produz ANCA: anti-MPO em título '
          'alto, glomerulonefrite e hemorragia alveolar. Suspender é o '
          'tratamento.'),
      par('Hidralazina por anos',
          'Lúpus induzido por droga, com anti-histona',
          'Lúpus com anti-histona e, numa parte, vasculite ANCA anti-MPO '
          'com glomerulonefrite. Dose e acetilação lenta pesam.'),
      par('Anfetaminas e metanfetamina',
          'Vasculite necrosante de vaso médio, tipo poliarterite nodosa',
          'Vasculite necrosante cerebral e sistêmica, de vaso médio, sem '
          'ANCA — a poliarterite das drogas simpaticomiméticas.'),
      ], opcoes=[
      'Púrpura retiforme de orelhas, agranulocitose e ANCA duplo',
      'Lesão destrutiva de linha média nasal, com anti-elastase',
      'Vasculite ANCA anti-MPO induzida por droga',
      'Lúpus induzido por droga, com anti-histona',
      'Vasculite necrosante de vaso médio, tipo poliarterite nodosa',
      'Síndrome serotoninérgica',
      ], titulo_resposta='Cada droga escolhe seu vaso e seu anticorpo',
      nota='A opção que sobrou, síndrome serotoninérgica, não é vasculite '
           'de espécie alguma.',
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
            ['Proteína/creatinina urinária', '—', '1,2 g/g', '<0,2 g/g'],
            ['Hemoculturas', 'Negativas', 'Negativas em 48 h', 'Negativas'],
        ]) + '</div>',
        fundo=CENA, so_kicker=True),

    q('q11', 11,
      'Glomerulonefrite crescêntica pauci-imune, neutrófilos de 420, '
      'culturas negativas, abstinência há cinco dias. **Quais três** '
      'afirmações orientam o tratamento?', [
      ('A abstinência é a medida com maior efeito documentado sobre a pele '
       'e a neutropenia',
       'Nas séries, a interrupção da exposição resolve as lesões em duas a '
       'três semanas sem imunossupressor. É o tratamento de base.', True),
      ('Rituximabe está contraindicado com neutrófilos abaixo de 500',
       'Não é contraindicação absoluta: com órgão ameaçado e infecção '
       'controlada, a depleção de células B pode entrar — com G-CSF e '
       'vigilância.', False),
      ('Com órgão ameaçado — rim crescêntico —, glicocorticoide com '
       'rituximabe ou ciclofosfamida é justificável, sob cobertura '
       'infecciosa',
       'A pele espera; o glomérulo não. Crescente celular é a única '
       'indicação consistente de imunossupressão nesta síndrome.', True),
      ('Troca plasmática é rotina',
       'Não há evidência para plasmaférese na vasculopatia por levamisol; '
       'entraria só com anti-MBG ou hemorragia alveolar grave.', False),
      ('G-CSF pode encurtar a agranulocitose enquanto há infecção ativa',
       'Séries da agranulocitose induzida por droga mostram recuperação '
       'mais rápida com fator estimulador. Não trata a causa; ganha '
       'tempo.', True),
      ('Manutenção por dois anos, como na granulomatose com poliangeíte',
       'Vasculite induzida por exposição não pede manutenção prolongada: '
       'retira-se a exposição e trata-se o órgão. A recidiva vem da '
       'droga, não do tempo.', False),
      ('Anticoagulação plena pela vasculopatia trombótica',
       'Trombo de pequeno vaso por levamisol não responde a heparina; a '
       'anticoagulação só entra se houver antifosfolípide comprovado.',
       False),
     ], 'Abstinência trata a pele; o glomérulo pede mais'),

    pagina('plano_conjunto', 'Evolução', 'Avaliação conjunta',
        p('Nefrologia, infectologia e reumatologia discutem gravidade, '
          'segurança da imunossupressão e o antimicrobiano em curso. Marina '
          'pergunta se cuidar do rim significa diálise. A resposta é '
          'vinculada à evolução da creatinina, não ao aspecto da urina.'),
        fundo=CENA, segue='renal'),

    pagina('renal', 'Plano', 'Tratamento dirigido',
        p('Com biópsia renal disponível, a equipe define a imunossupressão '
          'pela lesão glomerular e mantém a cobertura infecciosa enquanto '
          'os neutrófilos sobem. Sem a biópsia, a decisão permanece em '
          'aberto — e o caso segue assim.'),
        fundo=CENA,
        rota=dict(pediu=['Biópsia renal'], entao='seguimento_recuperacao',
                  senao='fim_incerteza')),

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
        fundo=CENA,
        rota=dict(pediu=['Sedimento urinário'], entao='fim_sequela',
                  senao='fim_incerteza')),

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
    desfecho('fim_incerteza', 'Investigação em continuidade',
        p('A hipótese associada à exposição permanece provável, sem '
          'caracterização completa da extensão. Marina segue em avaliação '
          'hospitalar. Não se declara rim normal, glomerulonefrite '
          'confirmada ou cura na ausência de documentação.'),
        qualidade='medio',
        porque='Falta de exame é falta de conhecimento, não proteção contra '
               'doença.',
        fundo=CENA, fecho='incerteza'),

    pagina('incerteza', 'Fecho clínico', 'Diagnóstico provável',
        p('O conjunto clínico e a exposição relatada sustentam vasculopatia '
          'provavelmente associada à cocaína, com suspeita de participação '
          'do levamisol. O grau de sustentação depende dos exames '
          'escolhidos. A exposição ao adulterante não foi confirmada.'),
        fundo=CENA, segue='q12'),

    q('q12', 12,
      'Na alta, **quais três** orientações e vigilâncias estão corretas?', [
      ('ANCA e neutrófilos tendem a normalizar em meses com abstinência; '
       'a reexposição reabre tudo',
       'Anticorpo negativa entre 2 e 14 meses; a lesão cutânea volta com o '
       'primeiro uso. A conversa sobre isso é o remédio.', True),
      ('Encaminhar para tratamento do transtorno por uso de substâncias, '
       'sem condicionar o cuidado à abstinência',
       'Acolher e tratar, com redução de danos. Quem é expulso do serviço '
       'por recair não volta — e volta a usar.', True),
      ('Manter antibiótico profilático por seis meses',
       'Não há indicação. A neutropenia se resolve; profilaxia só cria '
       'resistência.', False),
      ('Repetir toxicologia mensal como condição para o retorno',
       'Exame como vigilância punitiva afasta a paciente do seguimento. '
       'Toxicologia é ferramenta clínica, não de controle.', False),
      ('Vigiar creatinina e sedimento por meses, porque a glomerulonefrite '
       'pode persistir',
       'A pele fecha em semanas; o rim, quando acometido, pode não fechar. '
       'Retorno nefrológico com sedimento e proteinúria.', True),
      ('Vacinas inativadas estão contraindicadas pelo ANCA',
       'Não estão. Vacinar — sobretudo se houver imunossupressão.', False),
     ], 'A recaída é da droga; o cuidado não pode depender dela'),

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
        p('Neutropenia febril: IDSA 2010 (Freifeld e cols.). Séries e relatos '
          'não demonstram superioridade da imunossupressão ou do G-CSF nesta '
          'síndrome; o manejo antimicrobiano é extrapolado da neutropenia '
          'febril oncológica. Dados, cronologia e desfechos são ficcionais; '
          'a cena é ilustrativa.'),
        fundo=CENA),
]

REVISAO = [
    dict(rotulo='Hemograma diferencial', chave='Hemograma diferencial',
         porque='Febre com lesão necrótica exige saber o número de neutrófilos '
                'antes de qualquer outra coisa. A equipe recebeu o número da '
                'rotina; deveria tê-lo pedido.'),
    dict(rotulo='Culturas iniciais', chave='Hemoculturas iniciais',
         porque='Colher antes do antibiótico, sem atrasá-lo. Culturas '
                'negativas não excluem infecção, mas autorizam decisões.'),
    dict(rotulo='Sedimento urinário', chave='Sedimento urinário',
         porque='Localiza a lesão renal no glomérulo. Sem ele, urina escura '
                'com creatinina subindo ficou sem árbitro.'),
    dict(rotulo='Função renal atual', chave='Creatinina atual',
         porque='Quantifica a progressão; com o sedimento, define a urgência '
                'da biópsia.'),
    dict(rotulo='Mecanismo cutâneo', chave='Biópsia cutânea',
         porque='Separa oclusão de inflamação, sem identificar o agente.'),
    dict(rotulo='Toxicologia específica',
         chave='Levamisol urinário por LC-MS/MS',
         porque='Documenta a exposição se colhida cedo; a de 96 horas era '
                'tarde. Não é requisito para tratar a ameaça clínica.'),
]

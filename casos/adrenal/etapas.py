"""Choque depois de uma gastroenterite, em quem se cansava havia oito meses.

Refeito em 26/09/2026 no molde do //New England// (piloto: leptospirose;
gramática em Artifacts/nejm-casos-classicos/GRAMATICA_LIDA_2026-09-26.md).
O caso abre na emergência, no terceiro dia de vômitos e diarreia, e segue a
âncora que a equipe registrou: gastroenterite com choque hipovolêmico, lesão
renal pré-renal e hipercalemia. A primeira pergunta lê a gasometria; o sódio e
a urina viram páginas de leitura (revisão de 30/09: menos perguntas, mais
conteúdo, nada de doença específica no começo). A pressão que o volume não
segura, a conversa com o marido e o reexame da boca viram o caso, e o nome do
diagnóstico só aparece na decisão da madrugada, depois da metade. As decisões
de conduta mudam o desfecho, a pedido do Matheus.

Paciente ficcional. Doses e critérios: Endocrine Society 2016 (insuficiência
adrenal primária), Society for Endocrinology 2016 (crise adrenal), diretriz
europeia de hiponatremia 2014, UK Kidney Association 2023 (hipercalemia) e
Surviving Sepsis Campaign 2021.
"""
from pathlib import Path

from motor.estudo_imagem import estudo
from motor.etapas import (alt, bifurcacao, caminho, capa, desfecho, op, p,
                          pagina, painel, par, pareamento, pergunta, pontos,
                          topicos, vitais)

TITULO = 'Oito meses de cansaço'
RODAPE = 'Paciente ficcional · evoluções simuladas para ensino'
COR = '#ca8a04'
IMG = Path(__file__).parent / 'img'
BANCO = []
MOLDE = 'nejm'


def credito_meta(meta):
    import json
    m = json.loads(Path(meta).read_text())
    return m['autor'] + ' · Wikimedia Commons · ' + m['licenca'] + ' · setas adicionadas'


def pg(k, titulo, *textos, segue='', conforme=None):
    return pagina(k, titulo, '', *(p(t) for t in textos), so_kicker=True,
                  segue=segue, conforme=conforme)


def aula(k, titulo, *textos):
    """Página didática do NEJM, sem pergunta, entre as alíquotas."""
    return pagina(k, 'Discussão', titulo, *(p(t) for t in textos))


def Q(k, n, enunciado, opcoes, explicacao, segue=''):
    """Pergunta no molde do NEJM: alternativas curtas, sem comentário cada
    uma, e uma explicação só, em seções (subtítulo, texto)."""
    return pergunta(k, f'Pergunta {n}', enunciado,
                    [alt(t, certa=ok) for t, ok in opcoes],
                    explicacao=explicacao, segue=segue)


def ex(nome, valor, ref='—', alt_=False):
    return op(nome, resultado=valor, referencia=ref, alterado=alt_)


def fim(k, titulo, texto, porque, qualidade):
    return desfecho(k, titulo, p(texto), qualidade=qualidade, porque=porque,
                    fecho='retrospectiva')


ETAPAS = [
    capa(TITULO, fundo='cena.png', kicker='Caso interativo',
         selo='Paciente ficcional · procedência e créditos na última tela'),

    pg('historia', 'Apresentação',
       'Uma professora de 44 anos, moradora de Crateús, no sertão do Ceará, '
       'chega à emergência no sábado à noite, trazida pelo marido, no terceiro '
       'dia de vômitos e diarreia. Na quinta-feira ela e o filho de 9 anos '
       'comeram salpicão numa festa da escola; os dois adoeceram na mesma '
       'noite, e o menino melhorou em um dia.',
       'Ontem foi a uma unidade de pronto atendimento: soro, ondansetrona e '
       'alta. Hoje não consegue ficar de pé: "a vista escurece e as pernas '
       'somem". O marido conta que ela anda cansada e mais magra há meses.',
       'Nega sangue nas fezes, febre alta, dor torácica, viagem, antibiótico '
       'recente e uso de diurético ou laxante.'),

    pagina('ficha', 'Ficha do paciente', '',
           topicos(('Antecedentes', 'Cansaço e desânimo há oito meses, com perda '
                    'de 6 kg sem dieta. Há três meses a unidade básica '
                    'diagnosticou depressão, depois que a filha foi estudar em '
                    'Fortaleza. Vitiligo nas mãos desde os 34 anos. Menstruação '
                    'irregular no último ano. Dois partos, o último por cesárea.'),
                   ('Medicações', 'Fluoxetina 20 mg por dia há três meses. '
                    'Ondansetrona desde ontem. Nenhuma outra, nem chás.'),
                   ('Hábitos', 'Não fuma nem bebe. Parou as caminhadas há meses, '
                    'por cansaço.'),
                   ('Vida social', 'Professora do ensino fundamental, casada, dois '
                    'filhos. Sai pouco de casa além da escola.'),
                   ('Família', 'A mãe trata hipotireoidismo. O pai tratou '
                    'tuberculose pulmonar há vinte anos. Uma tia usa insulina '
                    'desde a juventude.')),
           so_kicker=True),

    pagina('exame', 'Exame físico', '',
           vitais(('Pressão arterial', '78/42 deitada', True),
                  ('Frequência cardíaca', '118', True),
                  ('Temperatura', '37,6 °C', False),
                  ('Frequência respiratória', '22', True),
                  ('SpO₂ em ar ambiente', '97%', False),
                  ('Glicemia capilar', '58 mg/dL', True),
                  ('Peso', '52 kg', False)),
           topicos(('Estado geral', 'Emagrecida, sonolenta, responde com '
                    'lentidão, orientada. Mucosas secas. Enchimento capilar de '
                    'quatro segundos.'),
                   ('Pele', 'Manchas acrômicas no dorso das mãos. Morena, sem '
                    'icterícia nem petéquias.'),
                   ('Pescoço', 'Jugulares planas. Tireoide discretamente '
                    'aumentada, fibroelástica, sem nódulos.'),
                   ('Coração e pulmões', 'Rítmico, taquicárdico, sem sopros. '
                    'Murmúrio presente, sem ruídos adventícios.'),
                   ('Abdome', 'Doloroso de forma difusa, sem defesa, ruídos '
                    'aumentados, sem visceromegalias.'),
                   ('Neurológico', 'Sem rigidez de nuca, sem déficit focal.')),
           so_kicker=True),

    painel('res1', 'Primeiros exames', 'Sangue', [
        ex('Hemoglobina / hematócrito', '13,4 g/dL / 40% {{(Hb 11,6 há três semanas)}}', 'Hb 12–16 g/dL'),
        ex('Leucócitos', '9.600/mm³ · neutrófilos 52% · eosinófilos 8% (770/mm³)', '4.000–11.000 · eosinófilos até 500', True),
        ex('Plaquetas', '262.000/mm³', '150.000–450.000/mm³'),
        ex('Ureia / creatinina', '88 / 1,8 mg/dL {{(creatinina 1,0 há três semanas)}}', 'até 40 / 0,6–1,1 mg/dL', True),
        ex('Sódio / potássio / cloro', '124 / 6,1 / 96 mmol/L {{(sódio 131 e potássio 5,0 há três semanas)}}', 'Na 135–145 · K 3,5–5,0 · Cl 98–107', True),
        ex('Glicose', '56 mg/dL', '70–99 mg/dL', True),
        ex('Albumina', '4,2 g/dL', '3,5–5,0 g/dL'),
        ex('AST / ALT / bilirrubina total', '32 / 28 U/L / 0,6 mg/dL', 'até 40 / 41 U/L / 1,2'),
        ex('Proteína C reativa', '1,2 mg/dL', 'até 0,5 mg/dL', True),
    ], introducao='Colhidos na chegada, antes do soro. Entre parênteses, os exames '
                  'da unidade básica de três semanas antes. Depois de 50 mL de '
                  'glicose a 50%, ela fica desperta e conversa.'),

    painel('res1b', 'Primeiros exames', 'Gasometria e urina', [
        ex('Gasometria arterial em ar ambiente', 'pH 7,31 · pCO₂ 33 mmHg · HCO₃ 16 mmol/L · pO₂ 92 mmHg · lactato 2,4 mmol/L', '—', True),
        ex('Osmolalidade sérica', '264 mOsm/kg', '275–295 mOsm/kg', True),
        ex('Urina', 'Densidade 1.022 · sem proteína, sangue ou leucócitos · raros cilindros hialinos', '—'),
        ex('Osmolalidade urinária', '418 mOsm/kg', '—'),
        ex('Sódio / potássio / cloro urinários', '62 / 14 / 58 mmol/L', '—'),
        ex('Creatinina urinária · FENa', '64 mg/dL · 1,4%', '—'),
    ]),

    Q('p1', 1,
      'Qual interpretação integra gasometria, eletrólitos e ânion gap urinário +18?', [
      ('Acidose metabólica sem aumento do gap, com componente renal além da diarreia', True),
      ('Acidose metabólica sem aumento do gap, explicada apenas por perda intestinal', False),
      ('Acidose láctica predominante com acidose respiratória associada', False),
      ('Acidose metabólica com alcalose respiratória adicional', False),
      ('Acidose respiratória primária com compensação metabólica', False),
    ], [('Contas', 'AG = 124 − (96 + 16) = 12, com albumina normal. Winter prevê pCO₂ 32 ± 2; 33 é compatível com compensação. Lactato 2,4 não explica a maior parte da acidose.'), ('Intestino e rim', 'Na perda intestinal de bicarbonato, espera-se aumento da excreção de amônio. Na urina, 62 + 14 − 58 = +18 sugere resposta de amônio insuficiente, se não houver ânions não medidos relevantes. É um marcador indireto: não mede o pH urinário nem prova falha de acidificar a urina. A hipercalemia reforça componente renal distal.')]),

    aula('sodio', 'Como ler este sódio',
       'A osmolalidade sérica de 264 confirma que a hiponatremia é hipotônica: '
       'há água demais para o sódio que existe. A urina, a 418 mOsm/kg, mostra '
       'que o ADH está agindo e que o rim não consegue eliminar essa água.',
       'O passo seguinte é o volume. Com mucosas secas, jugulares planas e '
       'pressão de 78, ela está hipovolêmica, e a hipovolemia é um estímulo '
       'para o ADH mais forte que a própria osmolalidade: a secreção é '
       'apropriada ao choque. A fluoxetina da ficha também pode baixar o sódio, '
       'mas por um mecanismo que pressupõe volume normal.',
       'O sódio era 131 há três semanas, e a hiponatremia é tratada como '
       'crônica. O cérebro já se adaptou, e subir o sódio depressa arrisca '
       'desmielinização osmótica, sobretudo na desnutrição: o limite é 8 mmol/L '
       'em 24 horas. Salina a 3% fica para convulsão ou coma, e restringir água '
       'em quem está em choque piora o choque.',
       'A equipe acompanha a diurese e a velocidade de mudança do sódio durante a reposição.'),

    estudo('ecg', 'Eletrocardiograma',
           'Feito à beira do leito pelo potássio de 6,1, com ela em taquicardia '
           'sinusal de 118. O traçado mostrado é de outro paciente, com o mesmo '
           'achado. Olhe a forma da onda T antes de abrir os achados.',
           IMG / 'ecg_hipercalemia.jpg',
           'Eletrocardiograma de outro paciente, com hipercalemia mais intensa · comparação didática.',
           credito_meta(IMG / 'ecg_hipercalemia.jpg.json'),
        [
         ((807, 316), (930, 250), '**Onda T** alta, pontiaguda e de base estreita em V4.', -12),
         ((129, 172), (60, 250), 'O mesmo formato da **onda T** em DII.', 12),
         ((396, 648), (300, 725), '**QRS estreito** na tira longa de DII.', 12),
        ],
        ['Ondas T altas, simétricas e de base estreita, mais evidentes de V3 a '
         'V5, com QRS estreito.',
         'É a primeira alteração da hipercalemia. Com potássio de 6,1 e '
         'alteração no traçado, o cálcio endovenoso protege a membrana '
         'cardíaca enquanto a causa é tratada.']),

    aula('urina', 'O que a urina diz',
       'A creatinina foi de 1,0 a 1,8 em três semanas, uma lesão renal aguda. '
       'Urina concentrada, a 418 mOsm/kg, raros cilindros hialinos e '
       'ureia de 88 alta para a creatinina são de hipoperfusão. Lesão do túbulo '
       'traria cilindros granulosos e urina com osmolalidade próxima à do '
       'plasma.',
       'O que não se encaixa é o sódio. Na hipovolemia da diarreia, a '
       'aldosterona sobe: o rim guarda sódio, com sódio urinário abaixo de 20 '
       'mmol/L e FENa abaixo de 1%, e perde potássio, que cai no sangue. Aqui o '
       'sódio urinário é 62, a FENa 1,4%, o potássio urinário 14 e o sérico '
       '6,1. No meio de um choque, o rim deixa sair sódio e segura potássio.',
       'É o mesmo néfron distal do ânion gap urinário positivo, que também não '
       'acidifica a urina. Hipovolemia com perda renal de sódio e potássio '
       'retido abre uma lista curta: diurético, remédio que bloqueia o eixo '
       'renina-aldosterona (espironolactona, inibidor da ECA, trimetoprim), '
       'nefropatia perdedora de sal e falta de ação da aldosterona.'),

    bifurcacao('b1', 'Decisão', 'As primeiras horas',
      'Depois de 1 litro de soro fisiológico e da glicose, a pressão é 92/58 e '
      'ela conversa. A hipótese registrada é gastroenterite aguda com choque '
      'hipovolêmico, lesão renal pré-renal e hipercalemia. A emergência está '
      'lotada. Como você conduz?', [
      caminho('Sala vermelha: soro com reavaliação, gluconato de cálcio, '
              'glicose contínua e monitor', 'internada',
              'Choque com potássio de 6,1 e onda T alterada pede monitor, cálcio '
              'para a membrana e volume guiado pela resposta.'),
      caminho('Insulina com glicose e bicarbonato para o potássio, e soro com '
              'cautela', 'insulina',
              'Trata o número do potássio com insulina numa glicemia que acabou '
              'de ser 56.'),
      caminho('Mais soro em observação por seis horas e alta com soro oral',
              'retorno',
              'Ela melhorou com o primeiro litro, e três dias de diarreia '
              'explicam a desidratação.'),
    ]),

    pg('insulina', 'Quarenta minutos depois',
       'Depois de 10 unidades de insulina regular com 25 g de glicose, a '
       'glicemia capilar cai para 34 e ela tem uma crise convulsiva. Recebe '
       'glicose a 50% e volta a responder. O potássio está em 5,6. A plantonista '
       'passa a glicose contínua, faz o gluconato de cálcio e a leva para a '
       'sala vermelha.',
       segue='internada'),

    pg('retorno', 'Seis horas depois',
       'Com pressão de 96/60 depois do segundo litro, ela recebe alta com soro '
       'oral. Na madrugada, o marido a encontra sem responder. O SAMU chega com '
       'ela em parada cardiorrespiratória; na gasometria da reanimação, '
       'glicemia de 31 e potássio de 7,4.',
       segue='f_obito'),

    pg('internada', 'Quatro horas depois, na sala vermelha',
       'Recebeu 3 litros de soro fisiológico, glicose a 10% contínua e 30 mL de '
       'gluconato de cálcio a 10%. A diurese é de 30 mL por hora. Mesmo assim, '
       'a pressão voltou a 80/46, e a glicemia caiu a 62 com a glicose correndo.',
       'Continua sem febre, sem crepitações, com jugulares planas. Antes de '
       'mais volume, a plantonista pede uma radiografia de tórax.'),

    estudo('rx', 'Radiografia de tórax',
           'Pedida na sala vermelha, antes de mais volume, para procurar '
           'congestão, derrame ou um foco de infecção que explique o choque.',
           IMG / 'rx_torax.jpg',
           'Radiografia de outra pessoa · comparação didática.',
           credito_meta(IMG / 'rx_torax.jpg.json'),
        [
         ((236, 500), (110, 420), '**Vasos pulmonares** de calibre normal: sem congestão.', 12),
         ((100, 955), (60, 1060), '**Seio costofrênico** direito livre: sem derrame.', 12),
         ((721, 786), (880, 700), '**Borda esquerda do coração**: área cardíaca sem aumento.', -12),
        ],
        ['Pulmões limpos, sem congestão nem consolidação. Seios costofrênicos '
         'livres. Área cardíaca normal.',
         'Nada no tórax explica o choque, e não há sinal de sobrecarga que '
         'impeça mais volume. A pressão que não se sustenta com 3 litros pede '
         'outra explicação.']),

    pg('marido', 'O marido volta',
       'Às duas da manhã, o marido volta com uma muda de roupa e conta o que '
       'ela não tinha dito à equipe: há meses Marta come sal puro na palma da '
       'mão e salga a comida já servida. "Achei que era mania."',
       'Diz também que ela escureceu desde o ano passado, "como quem pegou sol", '
       'embora quase não saia de casa. A residente volta ao leito.'),

    pagina('reexame', 'Reexame', '',
           topicos(('Boca', 'Manchas acastanhadas na gengiva e na face interna '
                    'das bochechas.'),
                   ('Mãos', 'Sulcos palmares escurecidos, em contraste com as '
                    'manchas acrômicas do dorso.'),
                   ('Pele', 'Cicatriz da cesárea mais escura que a pele em volta. '
                    'Cotovelos e joelhos escurecidos.'),
                   ('Hemodinâmica', 'Pressão 82/48, frequência 116. Não consegue '
                    'sentar sem tontura.')),
           so_kicker=True),

    estudo('foto_gengiva', 'A boca',
           'Com a lanterna, a residente afasta os lábios de Marta e encontra '
           'manchas acastanhadas na gengiva e na face interna das bochechas. A '
           'fotografia é de outra pessoa, com o mesmo tipo de pigmento na '
           'gengiva. Procure onde a cor muda antes de abrir os achados.',
           IMG / 'gengiva_pigmento.jpg',
           'Gengiva de outra pessoa, com pigmento acastanhado · comparação didática.',
           credito_meta(IMG / 'gengiva_pigmento.jpg.json'),
        [
         ((307, 150), (190, 50), '**Faixa acastanhada** na gengiva inserida acima '
          'dos dentes superiores, plana, sem relevo nem ferida.', 12),
         ((690, 395), (820, 475), 'O mesmo **pigmento** na gengiva inferior, dos '
          'dois lados da arcada.', -12),
         ((466, 118), (580, 40), '**Mucosa rósea** do freio labial, sem pigmento: '
          'o contraste que mostra a mancha.', -12),
        ],
        ['Máculas acastanhadas, planas, na gengiva superior e inferior, '
         'poupando o freio e a margem rósea.',
         'Em Marta há também manchas na face interna das bochechas, e o marido '
         'conta que ela escureceu desde o ano passado. O pigmento na boca, '
         'sozinho, pode ser constitucional; o que pesa é ele ter surgido em '
         'meses, junto do resto.']),

    estudo('foto_palmas', 'As mãos',
           'Marta abre as mãos: os sulcos palmares estão escurecidos, em '
           'contraste com as manchas acrômicas do dorso. A fotografia é de outra '
           'paciente, com o mesmo achado nas palmas. Olhe as linhas da mão, não '
           'a cor de fundo.',
           IMG / 'sulcos_palmares.jpg',
           'Palmas de outra paciente, com os sulcos escurecidos · comparação didática.',
           credito_meta(IMG / 'sulcos_palmares.jpg.json'),
        [
         ((283, 478), (90, 380), '**Sulco da eminência tenar** escurecido na mão '
          'esquerda da foto: uma linha mais escura que a pele ao lado.', 12),
         ((749, 473), (930, 380), 'Os **sulcos palmares** da outra mão, também '
          'marcados pelo pigmento.', -12),
         ((400, 540), (470, 400), '**Pele da palma** entre os sulcos, mais clara: o '
          'pigmento se concentra nas dobras.', -12),
        ],
        ['Sulcos palmares escurecidos nas duas mãos, com a pele entre eles mais '
         'clara.',
         'Pigmento que se acumula nas dobras das palmas, na cicatriz da '
         'cesárea e na gengiva não é bronzeado de sol: é pigmentação que vem de '
         'dentro, em quem quase não sai de casa.']),

    Q('p4', 2,
      'Choque após volume, hipoglicemia recorrente e pigmentação progressiva. Quais dois exames priorizar na amostra basal?', [
      ('Cortisol sérico', True),
      ('ACTH plasmático', True),
      ('Cortisol salivar noturno', False),
      ('Metanefrinas plasmáticas', False),
      ('Insulina e peptídeo C durante a infusão de glicose', False),
      ('Cortisol urinário de 24 horas', False),
    ], [('Amostra basal', 'Cortisol muito baixo durante choque sustenta deficiência; ACTH diferencia falência primária de deficiência central. A interpretação conjunta exige a amostra basal, anterior à hidrocortisona. Ambos têm resultados na sequência.'), ('Menor rendimento ou atraso', 'Cortisol salivar noturno avalia perda do ritmo no hipercortisolismo, não localiza esta deficiência. Metanefrinas investigam excesso catecolaminérgico e integram mal as perdas de sal e a pigmentação. Insulina/peptídeo C com glicose em infusão não são a prioridade para esta síndrome sistêmica. Cortisol urinário avalia sobretudo excesso e exige coleta demorada.')]),

    pg('hipotese', 'A hipótese muda',
       'A residente reescreve a evolução: a gastroenterite não fecha o quadro. '
       'Perda de sódio, potássio retido, hipoglicemia e pigmento de meses '
       'apontam para uma glândula que deixou de produzir os dois hormônios '
       'que seguram a pressão, a glicemia e o sal.',
       'A confirmação clássica é um teste de estímulo, feito de manhã. Ela '
       'chama o plantonista.'),

    bifurcacao('b2', 'Decisão', 'A madrugada',
      'São duas e meia. O plantonista da noite pergunta: "Não seria melhor '
      'confirmar antes de dar corticoide?" O teste de estímulo só pode ser '
      'feito às 7 horas. O que você faz?', [
      caminho('Colher cortisol e ACTH e dar hidrocortisona 100 mg EV agora',
              'tratado',
              'O tubo leva um minuto e não atrasa a dose; a crise não espera o '
              'teste.'),
      caminho('Manter soro e glicose e fazer o teste da cortrosina às 7 horas',
              'espera',
              'O teste sem corticoide é mais limpo. O preço é a noite em '
              'choque.'),
      caminho('Tratar como choque séptico: antibiótico, norepinefrina e UTI',
              'septico',
              'Choque que não responde a volume, com proteína C reativa alta, '
              'pode ser sepse de foco intestinal.'),
    ]),

    pg('espera', 'A noite',
       'Às 4 horas a pressão cai para 70/38 e ela fica confusa; começa '
       'norepinefrina. Às 5 horas o residente da UTI colhe cortisol e ACTH e dá '
       'hidrocortisona 100 mg sem esperar o teste. Às 8 horas, sem vasopressor, '
       'ela está acordada, com três horas a mais de choque na conta.',
       segue='tratado'),

    pg('septico', 'Na UTI',
       'Ceftriaxona e metronidazol, norepinefrina em dose crescente. Às 7 horas, '
       'com 0,3 µg/kg/min há quatro horas, o intensivista colhe cortisol e ACTH '
       'e inicia hidrocortisona 50 mg a cada 6 horas, como no choque séptico '
       'refratário. Em seis horas o vasopressor é desligado; as hemoculturas '
       'não crescem.',
       segue='tratado'),

    pg('tratado', 'Seis horas depois da hidrocortisona',
       'Pressão de 108/64 sem vasopressor, glicemia de 96 sem glicose, diurese '
       'boa. Ela pede água e pergunta onde está. Segue com hidrocortisona 50 mg '
       'a cada 6 horas.'),

    painel('res2', 'Resultados', 'A amostra basal da crise', [
        ex('Cortisol (antes da primeira dose)', '**2,1 µg/dL**', 'manhã: 5–25 µg/dL', True),
        ex('ACTH', '**480 pg/mL**', '7–63 pg/mL', True),
    ], introducao='Amostra colhida antes da primeira dose de hidrocortisona.'),

    Q('p6', 3,
      'Cortisol baixo e ACTH alto na amostra basal. Quais dois exames da investigação complementar definem mecanismo e necessidade de reposição?', [
      ('Renina e aldosterona em conjunto', True),
      ('Anticorpo anti-21-hidroxilase', True),
      ('Ressonância de hipófise como primeira imagem', False),
      ('Tomografia adrenal antes de interpretar os anticorpos', False),
      ('Novo cortisol durante hidrocortisona', False),
    ], [('Prioridades', 'Renina alta com aldosterona baixa sustenta deficiência mineralocorticoide, coerente com perda de sal e hipercalemia. Anti-21-hidroxilase pesquisa etiologia autoimune, favorecida pelo vitiligo. Os resultados foram colhidos na manhã seguinte e são apresentados após esta escolha.'), ('Alternativas', 'Ressonância hipofisária integra mal o ACTH muito alto e a deficiência mineralocorticoide. Tomografia pode pesquisar infiltração se anticorpo negativo ou quadro discordante, mas não precede a abordagem etiológica aqui. Novo cortisol sob hidrocortisona não recupera a informação da amostra basal e não orienta dose de reposição.')]),

    painel('res2_complemento', 'Resultados', 'Investigação complementar', [
        ex('Renina', '185 µUI/mL', '4–46 µUI/mL', True),
        ex('Aldosterona', '< 3 ng/dL', '3–16 ng/dL', True),
        ex('Anticorpo anti-21-hidroxilase', 'Reagente', 'não reagente', True),
        ex('TSH / T4 livre', '6,8 µUI/mL / 1,0 ng/dL', '0,4–4,0 / 0,9–1,7', True),
        ex('Anti-TPO', '340 UI/mL', 'até 35 UI/mL', True),
        ex('Hemoculturas e coprocultura', 'Sem crescimento em 48 horas', '—'),
    ], introducao='Exames da manhã seguinte à amostra basal.'),

    pg('virada', 'O diagnóstico',
       'Cortisol de **2,1 µg/dL** em choque, com ACTH de 480, renina alta e '
       'aldosterona indetectável: **insuficiência adrenal primária**, a doença '
       'de Addison, que se abriu como crise adrenal depois de uma '
       'gastroenterite. O anticorpo anti-21-hidroxilase indica a causa '
       'autoimune, hoje a mais comum.',
       'Quando mais de 90% do córtex está destruído, faltam os dois hormônios. '
       'Sem cortisol vêm a hipoglicemia, a eosinofilia, a hipotensão e a '
       'liberação de ADH que baixa o sódio. Sem aldosterona, o rim perde sódio, '
       'retém potássio e reduz a excreção de amônio. O ACTH alto, que nasce da mesma '
       'molécula precursora do hormônio estimulante do melanócito, escurece '
       'mucosas, dobras e cicatrizes.',
       'A doença se instala em meses e costuma passar por várias consultas '
       'antes do nome; infecção, sobretudo gastrointestinal, é o gatilho mais '
       'comum da crise. Com o vitiligo e a tireoidite (TSH de 6,8, anti-TPO '
       'reagente), o quadro completa uma síndrome poliglandular autoimune tipo 2.'),

    pg('noite', 'Doze horas depois da primeira dose',
       'A diurese passou a 350 mL por hora, de urina clara, com osmolalidade '
       'urinária de 90 mOsm/kg. O sódio, que era 124 na chegada, está em 132; o '
       'potássio, 4,6. Ela está lúcida e sem queixas, ainda com soro '
       'fisiológico a 150 mL por hora.'),

    Q('p5', 4,
      'Na 124 → 132 em 12 h, diurese 350 mL/h e urina a 90 mOsm/kg. Qual mecanismo exige mudar a prescrição agora?', [
      ('Perda de água livre após reposição de volume e cortisol, com risco de ultrapassar a correção planejada', True),
      ('Natriurese pela falta persistente de aldosterona, exigindo mais salina', False),
      ('Diurese osmótica por glicose, demonstrada pela osmolalidade urinária', False),
      ('Correção já concluída, pois o sódio se aproximou do normal', False),
      ('Excesso de mineralocorticoide, exigindo suspender toda reposição hormonal', False),
    ], [('Trajetória', 'Oito mmol/L em 12 horas já atinge uma meta conservadora diária neste contexto crônico. A urina muito diluída mostra eliminação de água livre após queda do estímulo de ADH; o ritmo pode acelerar, mesmo sem sintomas.'), ('Prescrição', 'Reavaliar e suspender salina após estabilização circulatória; repor água livre e considerar desmopressina para conter aquaresis, com Na frequente. Diurese osmótica teria mais solutos urinários. Não se suspende hidrocortisona para frear o sódio; falta de aldosterona não explica esta rápida perda de água diluída.')]),

    pg('evolucao', 'Terceiro dia',
       'Marta come, anda pelo corredor e passa à hidrocortisona oral em dose '
       'decrescente. O sódio é 134 e o potássio 4,4. A equipe planeja a '
       'reposição de longo prazo.'),

    bifurcacao('b3', 'Decisão', 'A reposição de longo prazo',
      'Qual esquema você prescreve para a alta?', [
      caminho('Hidrocortisona 15 a 25 mg por dia em duas ou três tomadas, '
              'fludrocortisona 0,1 mg, cartão e ampola de emergência',
              'manutencao',
              'Repõe o cortisol no ritmo do dia e a aldosterona, e prepara a '
              'paciente para a próxima crise.'),
      caminho('Prednisona 20 mg uma vez ao dia, sem fludrocortisona',
              'prednisona',
              'Uma tomada só é mais simples, e a prednisona tem algum efeito '
              'mineralocorticoide.'),
      caminho('Hidrocortisona 20 mg por dia, sem fludrocortisona', 'sem_fludro',
              'A hidrocortisona tem efeito mineralocorticoide; talvez baste.'),
    ]),

    pg('prednisona', 'Três meses depois',
       'Marta ganhou 9 kg, tem estrias novas e glicemia de jejum de 118. Ao '
       'mesmo tempo, sente tontura ao levantar, o potássio é 5,6 e a renina '
       'segue alta. Vinte miligramas de prednisona equivalem a cerca de 80 de '
       'hidrocortisona: excesso de glicocorticoide e falta de '
       'mineralocorticoide na mesma paciente.',
       'A endocrinologia troca para hidrocortisona fracionada com '
       'fludrocortisona.',
       segue='manutencao'),

    pg('sem_fludro', 'Seis semanas depois',
       'Tontura ao levantar, pressão de 96/60 em pé, vontade de comer sal de '
       'volta, potássio de 5,4 e renina ainda muito alta. Vinte miligramas de '
       'hidrocortisona não cobrem a aldosterona que falta.',
       'A endocrinologia acrescenta fludrocortisona 0,1 mg.',
       segue='manutencao'),

    pg('manutencao', 'O esquema da alta',
       'Hidrocortisona 10 mg ao acordar, 5 mg ao meio-dia e 5 mg às 16 horas; '
       'fludrocortisona 0,1 mg pela manhã. O ajuste se faz pela clínica, pela '
       'pressão em pé, pelo potássio e pela renina, não pelo cortisol nem pelo '
       'ACTH.'),

    Q('p7', 5,
      'Na alta, usa hidrocortisona 20 mg/dia. Se tiver febre de 38,5 °C, sem vômitos nem hipotensão e tolerando comprimidos, qual plano deve seguir?', [
      ('40 mg/dia em tomadas divididas enquanto durar a febre, em geral 2–3 dias', True),
      ('30 mg/dia, acrescentando 10 mg apenas à dose matinal enquanto durar a febre', False),
      ('40 mg no primeiro dia e 20 mg/dia a partir do segundo, mesmo se febril', False),
      ('20 mg/dia e aumento para 40 mg/dia se a febre persistir por 48 horas', False),
      ('20 mg/dia e aumento para 40 mg/dia se surgirem vômitos que impeçam os comprimidos', False),
    ], [('Dose e momento', 'Para febre acima de 38 °C com absorção preservada, a orientação da Endocrine Society é dobrar a dose diária: de 20 para 40 mg, divididos ao longo do dia. Acrescentar só 10 mg não alcança essa dose; esperar 48 horas deixa a demanda inicial descoberta.'), ('Duração e via', 'A dose de estresse acompanha a doença, em geral por 2–3 dias, não apenas o primeiro dia. Se surgirem vômitos persistentes, o problema muda para absorção: aumentar comprimidos deixa de ser estratégia confiável e o plano passa a hidrocortisona parenteral e atendimento urgente.')]),

    aula('ampola', 'A ampola de emergência',
       'A hidrocortisona injetável vem em pó, em frasco de 100 mg, com o '
       'diluente. Em casa, o marido dissolve o pó, aspira todo o conteúdo e '
       'aplica no músculo da face lateral da coxa, o local mais fácil para quem '
       'não é da saúde.',
       'A injeção não substitui a emergência. Depois dela, Marta vai ao '
       'hospital, onde a hidrocortisona segue endovenosa e o soro repõe o '
       'volume. Vômitos que impedem o comprimido, diarreia intensa, desmaio ou '
       'confusão são motivo para aplicar sem esperar a piora.',
       'O kit fica num lugar que a família conhece: frasco, diluente, seringa, '
       'agulha intramuscular e o cartão que diz que ela depende de '
       'glicocorticoide. A validade do frasco se confere a cada consulta.'),

    Q('p8', 6,
      'TSH 6,8, T4 livre normal e anti-TPO 340 na crise. Qual plano tireoidiano é mais adequado após estabilizar Marta?', [
      ('Repetir TSH e T4 livre em cerca de 8–12 semanas antes de decidir levotiroxina', True),
      ('Iniciar levotiroxina 25 µg/dia após 48 horas de hidrocortisona, pelo anti-TPO positivo', False),
      ('Repetir TSH em 7 dias e iniciar 25 µg/dia se continuar acima da referência', False),
      ('Repetir anti-TPO em 8–12 semanas e iniciar 25 µg/dia se o título permanecer elevado', False),
      ('Adiar a função tireoidiana por um ano, atribuindo a alteração à crise', False),
    ], [('Por que aguardar', 'T4 livre normal e TSH abaixo de 10 durante doença aguda não demonstram hipotireoidismo persistente. Reavaliar após recuperação e reposição de cortisol permite separar alteração transitória de tireoidopatia que requer tratamento. Uma semana ainda é cedo para essa distinção.'), ('Por que não as outras', 'Cobertura com hidrocortisona reduz o risco de iniciar hormônio tireoidiano, mas não cria indicação de levotiroxina em 48 horas. Anti-TPO positivo aumenta risco futuro; repetir seu título não decide reposição. Esperar um ano ignora uma alteração funcional já presente. Se a elevação persistir, sintomas e magnitude do TSH orientarão a decisão.')]),

    pg('alta', 'Preparando a alta',
       'Marta sai com o esquema de reposição, a ampola de hidrocortisona na '
       'bolsa e o marido treinado para aplicar.',
       conforme=('b3', ['alta_cedo', 'f2', 'f2'])),

    pg('alta_cedo', 'Na véspera da alta',
       'Ela conta que, pela primeira vez em meses, não sentiu vontade de comer '
       'sal. A gengiva e as cicatrizes vão clarear devagar, com a queda do ACTH.',
       conforme=('b2', ['alta_ok', 'f2', 'f2'])),

    pg('alta_ok', 'O resumo de alta',
       'A residente escreve no resumo o que abriu o caso: o potássio alto com '
       'diarreia e o sódio que saía pela urina, registrados já na primeira '
       'hora.',
       conforme=('b1', ['f1', 'f2', 'f2'])),

    fim('f1', 'Alta no quinto dia',
        'Marta volta à escola em três semanas. A pele clareia em quatro meses, '
        'e o TSH de controle é 3,1, sem levotiroxina.',
        'Monitor e cálcio na primeira hora, hidrocortisona assim que o quadro '
        'deixou de caber na gastroenterite, correção do sódio vigiada e '
        'reposição completa na alta.',
        'melhor'),

    fim('f2', 'Alta com um percurso mais longo',
        'Marta sai viva, mas com uma hipoglicemia convulsiva, horas a mais de '
        'choque ou meses de esquema errado até a correção.',
        'Insulina numa glicemia baixa, esperar o teste para dar corticoide ou '
        'repor só metade do que a glândula deixou de fazer cobraram em tempo e '
        'em dano.', 'medio'),

    fim('f_obito', 'Óbito em casa',
        'Marta morre na madrugada, em crise adrenal não reconhecida.',
        'Choque que só melhora em parte com volume, potássio alto com diarreia, '
        'sódio urinário alto e hipoglicemia são crise adrenal até prova em '
        'contrário. A alta interrompeu o volume, e a hidrocortisona 100 mg, que '
        'não custaria nada, nunca foi dada.', 'pior'),

    pagina('retrospectiva', 'Pontos de ensino', '',
        pontos(
            'Na diarreia com hipovolemia, o rim guarda sódio e perde potássio. '
            'Sódio urinário alto com potássio retido é falta de ação da '
            'aldosterona até prova em contrário.',
            'Acidose de ânion gap normal com ânion gap urinário positivo indica '
            'falha renal de acidificação, mesmo quando há diarreia.',
            'Hipoglicemia em jejum, eosinofilia no choque e pressão que o volume '
            'não segura apontam para falta de cortisol.',
            'Na suspeita de crise adrenal, colher cortisol e ACTH e dar '
            'hidrocortisona 100 mg endovenosa sem esperar o resultado nem o '
            'teste de estímulo.',
            'Com volume e cortisol repostos, o ADH cai e o sódio sobe depressa: '
            'vigiar a cada poucas horas e frear com glicose a 5% e desmopressina.',
            'Na alta: hidrocortisona fracionada, fludrocortisona, regras dos '
            'dias de doença com ampola de emergência, e rastreio das outras '
            'doenças da síndrome poliglandular tipo 2.'),
        so_kicker=True),

    pg('referencias', 'Fontes e limites',
       'Paciente, valores e percursos são ficcionais. A cena de abertura é uma ilustração autoral gerada por inteligência artificial para este caso; não é fotografia nem documentação clínica.',
       'Bornstein e cols. Diagnosis and Treatment of Primary Adrenal '
       'Insufficiency: An Endocrine Society Clinical Practice Guideline, J Clin '
       'Endocrinol Metab 2016. Arlt e cols. Society for Endocrinology Endocrine '
       'Emergency Guidance: acute adrenal insufficiency in adults, Endocr '
       'Connect 2016. Husebye e cols. Adrenal insufficiency, Lancet 2021. '
       'Spasovski e cols. Clinical practice guideline on diagnosis and '
       'treatment of hyponatraemia, Eur J Endocrinol 2014. UK Kidney '
       'Association, Clinical Practice Guideline: Management of Hyperkalaemia '
       'in Adults, 2023. Evans e cols. Surviving Sepsis Campaign 2021.',
       'Eletrocardiograma: Michael-Joseph F. Agbayani e Eddieson Gonzales, '
       'Wikimedia Commons, CC BY 4.0. Radiografia de tórax: Mikael Häggström, '
       'Wikimedia Commons, CC0. Gengiva pigmentada: Shaimaa Abdellatif, '
       'Wikimedia Commons, CC BY-SA 4.0, recortada '
       '(commons.wikimedia.org/wiki/File:Hyperpigmentation_of_the_gum.jpg). '
       'Sulcos palmares: Petros Perros, "A 69-Year-Old Female with Tiredness '
       'and a Persistent Tan", PLoS Medicine, via Wikimedia Commons, CC BY 2.5, '
       'recortada (commons.wikimedia.org/wiki/File:A_69-Year-Old_Female_with_'
       'Tiredness_and_a_Persistent_Tan_02.png). Todas de outras pessoas, com '
       'setas adicionadas.'),
]

REVISAO = []

# Revisão das perguntas: fontes consultadas em 22/10/2026.
# https://www.nbme.org/sites/default/files/2021-02/NBME_Item%20Writing%20Guide_R_6.pdf
# https://www.endocrine.org/clinical-practice-guidelines/primary-adrenal-insufficiency
# https://www.endocrinology.org/media/xhrhxhxm/emergency-management-of-severe-and-moderately-severely-symptomatic-hyponatraemia-in-adult-patients-2022.pdf
# https://www.nice.org.uk/guidance/NG145/chapter/recommendations
# https://pmc.ncbi.nlm.nih.gov/articles/PMC4880116/

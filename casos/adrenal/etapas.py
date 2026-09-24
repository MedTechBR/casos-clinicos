"""Crise adrenal em insuficiência adrenal primária autoimune (síndrome poliglandular tipo 2).

Alíquota → pergunta, no molde dos casos interativos do //New England//. Oito
perguntas, uma rodada de exames com gabarito e painel, um pareamento das
causas de insuficiência adrenal primária no Brasil e duas decisões de
conduta, uma delas com óbito. Paciente ficcional; doses segundo a diretriz
da Endocrine Society de 2016 e a orientação de emergência da Society for
Endocrinology.
"""
from pathlib import Path

from motor.etapas import (alt, bifurcacao, caminho, capa, desfecho, op, p,
                          pagina, painel, par, pareamento, pergunta, tabela,
                          topicos, vitais, lamina)

TITULO = 'Mais escura a cada verão'
RODAPE = 'Paciente ficcional · evoluções simuladas para ensino'
COR = '#ca8a04'
IMG = Path(__file__).parent / 'img'
BANCO = []
CREDITO_ECG = 'Ewingdo · Wikimedia Commons · CC BY-SA 4.0'


def pg(k, titulo, *textos, segue='', conforme=None):
    return pagina(k, titulo, '', *(p(t) for t in textos), so_kicker=True,
                  segue=segue, conforme=conforme)


def Q(k, n, enunciado, itens, titulo, segue=''):
    return pergunta(k, f'Pergunta {n}', enunciado,
                    [alt(t, c, certa=ok) for t, c, ok in itens],
                    titulo_resposta=titulo, segue=segue)


def ex(nome, valor, ref='—', alt_=False):
    return op(nome, resultado=valor, referencia=ref, alterado=alt_)


def fim(k, titulo, texto, porque, qualidade):
    return desfecho(k, titulo, p(texto), qualidade=qualidade, porque=porque,
                    fecho='retrospectiva')


ETAPAS = [
    capa(TITULO, fundo='cena.png', kicker='Caso interativo',
         selo='Paciente ficcional · procedência e créditos na última tela'),

    pg('historia', 'Apresentação',
       'Marta, 44 anos, professora em Crateús, chega à emergência levada pelo '
       'marido no terceiro dia de vômitos e diarreia. Hoje não conseguiu '
       'ficar de pé: "a vista escurece e as pernas somem".',
       'O marido conta que ela vem "murchando" há oito meses. Perdeu 7 kg, '
       'dorme à tarde, sente enjoo quase todo dia e passou a comer sal puro '
       'na palma da mão. As colegas da escola comentam que ela está "mais '
       'morena", e ela atribui ao sol.'),

    pg('antecedentes', 'Antecedentes',
       'Tem **vitiligo** há dez anos, nas mãos e em volta da boca. A mãe trata '
       'hipotireoidismo por tireoidite de Hashimoto. A menstruação ficou '
       'irregular no último ano.',
       'Nega uso de corticoide em comprimido, pomada, colírio ou injeção, '
       'inclusive as "injeções para dor nas costas" de farmácia. Nunca teve '
       'tuberculose, não trabalhou na roça e não tem feridas na boca.'),

    pagina('exame', 'Exame físico', '',
           vitais(('Pressão arterial', '78/42', True), ('Frequência cardíaca', '118', True),
                  ('Temperatura', '37,6 °C', False), ('Frequência respiratória', '22', False),
                  ('Glicemia capilar', '58 mg/dL', True)),
           topicos(('Estado geral', 'Sonolenta, responde com lentidão, mucosas secas.'),
                   ('Pele', '**Hiperpigmentação** dos sulcos palmares, dos cotovelos e de '
                    'uma cicatriz de cesárea antiga. Manchas de vitiligo nas mãos, que '
                    'contrastam com a pele escurecida.'),
                   ('Boca', '**Manchas acastanhadas na gengiva** e na mucosa jugal.'),
                   ('Abdome', 'Doloroso de forma difusa, sem defesa, ruídos aumentados.'),
                   ('Neurológico', 'Sem déficit focal, sem rigidez de nuca.')),
           so_kicker=True),

    Q('p1', 1,
      'Antes de qualquer exame: oito meses de cansaço, perda de peso, náusea, '
      'fissura por sal e pele escurecendo. **Quais quatro** hipóteses entram '
      'no diferencial desse quadro de base?', [
      ('Insuficiência adrenal primária',
       'Fissura por sal, hiperpigmentação e hipotensão formam a tríade que '
       'aponta para a adrenal.', True),
      ('Tuberculose disseminada',
       'Consome, dá náusea e, no Brasil, ainda é causa de destruição adrenal.',
       True),
      ('Neoplasia oculta',
       'Perda de peso e fadiga em oito meses obrigam a pensar nela, até pelas '
       'metástases adrenais.', True),
      ('Doença celíaca',
       'Emagrece, cansa e anda junto com outras doenças autoimunes, como o '
       'vitiligo dela.', True),
      ('Hiperaldosteronismo primário',
       'Faz hipertensão e fraqueza por potássio baixo, não hipotensão.', False),
      ('Feocromocitoma',
       'Crises de palpitação e hipertensão, não pele escura e sal na mão.',
       False),
      ('Síndrome do intestino irritável',
       'Não explica perda de peso, hipotensão nem hiperpigmentação.', False),
      ('Fibromialgia',
       'Cansaço sem perda de peso e sem sinal objetivo. Aqui os sinais sobram.',
       False),
     ], 'O sal na palma da mão'),

    pg('beira_leito', 'Na sala de emergência',
       'A gasometria venosa chega em dez minutos: sódio 124, potássio 6,1, '
       'bicarbonato 17. A glicemia é 58. O eletrocardiograma mostra '
       'taquicardia sinusal com ondas T apiculadas discretas em V2 a V4.',
       'Depois de 1 litro de soro fisiológico em 20 minutos, a pressão sobe '
       'para 84/50 e cai de novo.'),

    Q('p2', 2,
      'Suspeita de crise adrenal. **Quais quatro** medidas são as mais '
      'apropriadas agora?', [
      ('Hidrocortisona 100 mg endovenosa em bolo, seguida de 200 mg em 24 horas',
       'É o tratamento da crise. Nessa dose, a hidrocortisona também cobre a '
       'falta de aldosterona.', True),
      ('Colher cortisol e ACTH antes do corticoide, sem atrasar a dose',
       'Um tubo de sangue leva um minuto e vale o diagnóstico. Se não der '
       'para colher, trata-se assim mesmo.', True),
      ('Soro fisiológico, 1 litro na primeira hora, e depois conforme a resposta',
       'A crise adrenal é também choque hipovolêmico.', True),
      ('Glicose endovenosa para a hipoglicemia',
       'Glicemia de 58 com sonolência não espera.', True),
      ('Aguardar o teste de estímulo com cortrosina pela manhã',
       'O teste confirma depois. Esperar por ele com pressão de 78 mata.',
       False),
      ('Fludrocortisona oral já na emergência',
       'Com hidrocortisona acima de 50 mg por dia, o efeito '
       'mineralocorticoide já está coberto, e ela está vomitando.', False),
      ('Salina hipertônica para corrigir o sódio de 124',
       'Sem convulsão, não há indicação. Com hidrocortisona e volume, o sódio '
       'sobe sozinho, às vezes rápido demais: o risco é corrigir além de 8 a '
       '10 mEq/L em 24 horas.', False),
      ('Noradrenalina antes do volume',
       'Sem cortisol e sem volume, o vasopressor rende pouco. Entra se o '
       'choque persistir depois dos dois.', False),
      ('Insulina com glicose para o potássio de 6,1',
       'Com glicemia de 58, insulina é perigosa. O potássio cai com '
       'hidrocortisona e soro.', False),
     ], 'Corticoide, sal e açúcar, na primeira hora'),

    bifurcacao('b1', 'Decisão', 'A primeira hora',
      'O plantonista da noite hesita: "E se não for adrenal? Não seria melhor '
      'confirmar antes de dar corticoide?" O que você faz?', [
      caminho('Colhe cortisol e ACTH, dá hidrocortisona 100 mg agora e segue '
              'com o soro', 'tratado',
              'O corticoide não atrapalha a dosagem já colhida, e a crise não '
              'espera diagnóstico.'),
      caminho('Mantém soro e glicose, e deixa o teste de cortrosina para as 7 '
              'horas, antes do corticoide', 'espera',
              'O teste sem corticoide é mais limpo. O preço é passar a noite '
              'em choque.'),
      caminho('Trata como gastroenterite com desidratação: soro, antiemético e '
              'alta com retorno se piorar', 'retorno',
              'A pressão melhorou um pouco com o soro, e a história de '
              'diarreia explica a desidratação.'),
    ]),

    pg('retorno', 'Doze horas depois',
       'Marta é encontrada em casa pelo marido, na madrugada, sem responder. '
       'O SAMU chega com ela em parada cardiorrespiratória, glicemia de 31 e '
       'potássio de 7,4.',
       segue='f_obito'),

    pg('espera', 'A noite',
       'Às 2 horas, a pressão cai para 70/38 e ela fica confusa. Começa '
       'noradrenalina. Às 4 horas, o residente da UTI dá hidrocortisona 100 mg '
       'sem esperar o teste. Às 7 horas, já sem vasopressor, ela está '
       'acordada, com 12 horas a mais de choque na conta.',
       segue='tratado'),

    pg('tratado', 'Seis horas depois da hidrocortisona',
       'Pressão de 108/64, glicemia de 96, diurese boa. O sódio subiu de 124 '
       'para 128 e o potássio caiu para 5,0. Ela pede água e pergunta onde '
       'está.'),

    Q('ex1', 3,
      'Com Marta estável, **quais quatro** exames são os mais apropriados '
      'para confirmar e localizar a insuficiência adrenal?', [
      ('Cortisol e ACTH da amostra colhida antes da hidrocortisona',
       'O par confirma: cortisol baixo com ACTH alto é falência da glândula.',
       True),
      ('Renina e aldosterona',
       'Separam primária de secundária e dizem se ela vai precisar de '
       'fludrocortisona.', True),
      ('Anticorpo anti-21-hidroxilase',
       'Positivo, fecha a causa autoimune e dispensa imagem.', True),
      ('TSH e T4 livre',
       'Adrenalite autoimune anda com tireoidite, e o hormônio tireoidiano '
       'não pode vir antes do glicocorticoide.', True),
      ('Ressonância de sela túrcica',
       'Só entraria se o ACTH viesse baixo, apontando para a hipófise.',
       False),
      ('Cortisol salivar noturno',
       'Rastreia excesso de cortisol, o problema oposto.', False),
      ('Teste de supressão com dexametasona',
       'Também investiga Cushing, não insuficiência.', False),
      ('Tomografia de adrenais antes do anticorpo',
       'Fica para anticorpo negativo, quando se procuram tuberculose, fungo, '
       'hemorragia ou metástase.', False),
      ('Cortisol às 16 horas',
       'O cortisol da tarde é normalmente baixo e não informa nada.', False),
     ], 'Glândula, eixo e causa'),

    painel('res1', 'Resultados', 'O que a equipe pediu', [
        ex('Cortisol (antes da hidrocortisona)', '**2,1 µg/dL**', '> 18 µg/dL no estresse', True),
        ex('ACTH', '**480 pg/mL**', '7–63 pg/mL', True),
        ex('Renina ativa', '185 µUI/mL', '4–46 µUI/mL', True),
        ex('Aldosterona', '< 3 ng/dL', '3–16 ng/dL', True),
        ex('Anti-21-hidroxilase', '**Reagente**', 'não reagente', True),
        ex('TSH / T4 livre', '6,8 µUI/mL / 1,0 ng/dL', '0,4–4,0 / 0,9–1,7', True),
        ex('Anti-TPO', 'Reagente, 340 UI/mL', 'até 35 UI/mL', True),
        ex('Sódio / potássio (admissão)', '124 / 6,1 mEq/L', '135–145 / 3,5–5,0', True),
        ex('Ureia / creatinina (admissão)', '88 / 1,8 mg/dL', 'até 40 / 0,6–1,1', True),
        ex('Hemoglobina / eosinófilos', '11,4 g/dL / 9% (1.100 por mm³)', '12–16 / até 500', True),
        ex('Eletrocardiograma', 'Taquicardia sinusal, 118 bpm · T apiculada discreta em V2–V4', '—', True),
    ], introducao='O cortisol e o ACTH são da amostra colhida na chegada, antes da primeira dose.',
       laminas={'Eletrocardiograma': lamina('ecg_taquicardia.jpg', 'Eletrocardiograma',
                'Traçado ilustrativo de taquicardia sinusal de outra pessoa; não '
                'mostra as ondas T de Marta.', CREDITO_ECG)}),

    Q('p4', 4,
      'Cortisol de 2,1 no choque confirma a insuficiência. Hiponatremia aparece '
      'nos dois tipos, primária e secundária. **Quais quatro** achados indicam '
      'que a dela é primária?', [
      ('Hiperpigmentação de pele e mucosas',
       'O ACTH alto e seu precursor estimulam o melanócito. Na secundária, a '
       'pele empalidece.', True),
      ('Hipercalemia',
       'Falta de aldosterona, que só acontece quando a glândula é destruída.',
       True),
      ('Renina alta com aldosterona baixa',
       'O eixo renina-aldosterona não depende da hipófise.', True),
      ('ACTH elevado', 'A hipófise responde ao cortisol baixo.', True),
      ('Hiponatremia',
       'Nas duas: a falta de cortisol libera vasopressina e retém água.',
       False),
      ('Hipoglicemia', 'Nas duas: é falta de cortisol.', False),
      ('Eosinofilia', 'Nas duas: também é falta de cortisol.', False),
      ('Hipotensão ortostática',
       'Mais intensa na primária, mas presente nas duas.', False),
      ('Fadiga e perda de peso', 'Nas duas.', False),
     ], 'O que é do ACTH e o que é da aldosterona'),

    pareamento('p5', 'Pergunta 5',
      'A causa de Marta é autoimune. Associe cada cenário à causa mais '
      'provável de insuficiência adrenal primária.', [
      par('Mulher com vitiligo, tireoidite e anti-21-hidroxilase reagente',
          'Adrenalite autoimune',
          'É a causa mais comum no Brasil urbano e costuma vir acompanhada de '
          'outras doenças autoimunes.'),
      par('Homem de 62 anos, tuberculose tratada na juventude, adrenais '
          'pequenas e calcificadas na tomografia',
          'Infecção granulomatosa',
          'A tuberculose destrói as duas adrenais e deixa calcificação.'),
      par('Lavrador de 55 anos com úlceras orais de fundo granuloso e '
          'adrenais aumentadas',
          'Infecção fúngica endêmica',
          'Paracoccidioidomicose: no Brasil, as adrenais são acometidas com '
          'frequência na forma crônica.'),
      par('Jovem com púrpura fulminante e choque por meningococo',
          'Hemorragia adrenal bilateral',
          'Síndrome de Waterhouse-Friderichsen.'),
      par('Idoso anticoagulado, no quarto dia de artroplastia, com dor '
          'lombar e choque',
          'Hemorragia adrenal bilateral',
          'Anticoagulação e estresse pós-operatório são o cenário clássico.'),
      par('Menino de 9 anos com piora escolar, espasticidade e ácidos graxos '
          'de cadeia muito longa elevados',
          'Doença genética peroxissomal',
          'Adrenoleucodistrofia ligada ao X: pedir ácidos graxos de cadeia '
          'muito longa em todo menino com insuficiência adrenal primária.'),
    ], opcoes=['Adrenalite autoimune', 'Infecção granulomatosa',
               'Infecção fúngica endêmica', 'Hemorragia adrenal bilateral',
               'Doença genética peroxissomal',
               'Supressão do eixo por corticoide exógeno'],
    titulo_resposta='Autoimune, infecciosa, hemorrágica, genética',
    nota='A supressão por corticoide exógeno sobrou: ela é secundária, com '
         'ACTH baixo, e não entra na lista das primárias.'),

    pg('evolucao', 'Terceiro dia',
       'Marta come, anda pelo corredor e já recebe hidrocortisona oral em '
       'dose decrescente. O sódio é 134 e o potássio 4,6. A equipe planeja a '
       'reposição de longo prazo.'),

    bifurcacao('b2', 'Decisão', 'A reposição de longo prazo',
      'Qual esquema você prescreve para a alta?', [
      caminho('Hidrocortisona 15 a 20 mg por dia em duas ou três tomadas, '
              'fludrocortisona 0,1 mg, cartão de identificação e ampola de '
              'emergência', 'manutencao',
              'Repõe cortisol no ritmo do dia e aldosterona, e prepara a '
              'paciente para a próxima crise.'),
      caminho('Prednisona 20 mg uma vez ao dia, sem fludrocortisona', 'prednisona',
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
       'Tontura ao levantar, pressão de 96/60 em pé, fissura por sal de volta, '
       'potássio de 5,4 e renina ainda muito alta. Vinte miligramas de '
       'hidrocortisona não cobrem a aldosterona que falta.',
       'A endocrinologia acrescenta fludrocortisona 0,1 mg.',
       segue='manutencao'),

    pg('manutencao', 'O esquema da alta',
       'Hidrocortisona 10 mg ao acordar, 5 mg ao meio-dia e 5 mg às 16 horas; '
       'fludrocortisona 0,1 mg pela manhã. O ajuste se faz pela clínica, pela '
       'pressão em pé e pela renina, não pelo cortisol nem pelo ACTH.'),

    Q('p6', 6,
      'Antes da alta, a enfermagem ensina a Marta e ao marido as regras dos '
      'dias de doença. **Quais quatro** orientações estão corretas?', [
      ('Com febre acima de 38 °C, dobrar a dose de hidrocortisona; acima de 39 °C, triplicar',
       'Enquanto durar a febre, e voltar à dose habitual depois.', True),
      ('Com vômitos ou diarreia intensa, aplicar hidrocortisona 100 mg '
       'intramuscular e ir à emergência',
       'Foi a gastroenterite que abriu a crise dela. Comprimido vomitado não '
       'protege.', True),
      ('Em cirurgia de grande porte, hidrocortisona 100 mg na indução e 200 mg nas 24 horas seguintes',
       'O anestesista precisa saber. O cartão serve para isso.', True),
      ('Andar com cartão ou pulseira de identificação',
       'Inconsciente, ela não vai poder dizer que tem Addison.', True),
      ('Suspender a fludrocortisona quando tiver febre',
       'Não há motivo. A fludrocortisona não precisa de ajuste no estresse.',
       False),
      ('Dobrar a fludrocortisona no dia de estresse',
       'Quem sobe é a hidrocortisona.', False),
      ('Na gastroenterite leve, manter a dose habitual até ver se passa',
       'Foi exatamente assim que ela chegou em choque.', False),
      ('Reduzir a hidrocortisona por conta própria se ganhar peso',
       'O ajuste é com a equipe. Suspender por conta leva à crise.', False),
     ], 'Dobrar, injetar, avisar'),

    Q('p7', 7,
      'Adrenalite autoimune com tireoidite e vitiligo é síndrome poliglandular '
      'autoimune tipo 2. **Quais quatro** exames entram no seguimento dela?', [
      ('TSH e T4 livre periódicos',
       'A tireoidite é o componente mais frequente.', True),
      ('Glicemia de jejum e hemoglobina glicada',
       'Diabetes tipo 1 faz parte da síndrome.', True),
      ('Vitamina B12 e hemograma',
       'Gastrite atrófica autoimune e anemia perniciosa se associam.', True),
      ('Anticorpo antitransglutaminase IgA',
       'Doença celíaca também anda junto, e a irregularidade menstrual pede '
       'ainda avaliação de insuficiência ovariana.', True),
      ('Paratormônio e cálcio para hipoparatireoidismo',
       'Hipoparatireoidismo e candidíase mucocutânea são da síndrome tipo 1, '
       'da infância, por mutação no gene AIRE.', False),
      ('Pesquisa de mutação do gene AIRE',
       'É o exame da síndrome tipo 1, que ela não tem.', False),
      ('Anti-21-hidroxilase anual',
       'Já é positivo. Repetir não muda nada.', False),
      ('Cortisol sérico a cada consulta para ajustar a dose',
       'Com hidrocortisona, o cortisol oscila com a tomada e não guia a dose.',
       False),
     ], 'A tireoide primeiro, depois o pâncreas, o estômago e o intestino'),

    pergunta('p8', 'Pergunta 8',
      'TSH de 6,8 com T4 livre normal e anti-TPO reagente, colhidos em plena '
      'crise adrenal. Qual a conduta?', [
      alt('Repetir TSH e T4 livre seis a oito semanas depois de estabilizada a reposição de glicocorticoide',
          'A falta de cortisol eleva o TSH, que muitas vezes normaliza com a '
          'reposição. E levotiroxina antes do glicocorticoide pode precipitar '
          'crise adrenal.', certa=True),
      alt('Iniciar levotiroxina 50 µg hoje, pelo anticorpo positivo',
          'Hipotireoidismo subclínico com TSH abaixo de 10, dosado na crise, '
          'não justifica tratar já.'),
      alt('Ultrassonografia e punção da tireoide',
          'Não há nódulo. Tireoidite se vê no anticorpo.'),
      alt('Suspender a hidrocortisona por três dias para dosar o TSH sem interferência',
          'Suspender a hidrocortisona é arriscar outra crise.'),
      alt('Solicitar cintilografia de tireoide',
          'Ajuda em hipertireoidismo, não em TSH discretamente alto.'),
    ], titulo_resposta='O TSH da crise não é o TSH dela'),

    pg('alta', 'Preparando a alta',
       'Marta sai com o esquema corrigido, a ampola de hidrocortisona na bolsa '
       'e o marido treinado para aplicar.',
       conforme=('b2', ['alta_cedo', 'f2', 'f2'])),

    pg('alta_cedo', 'Na véspera da alta',
       'Ela conta que, pela primeira vez em meses, não sentiu vontade de comer '
       'sal. A cor da pele vai clarear devagar, com o ACTH.',
       conforme=('b1', ['f1', 'f2', 'f2'])),

    fim('f1', 'Alta no quinto dia',
        'Marta volta à escola em três semanas. A pele clareia em quatro meses, '
        'e o TSH de controle é 3,1, sem levotiroxina.',
        'Hidrocortisona na primeira hora, reposição completa desde a alta e '
        'uma paciente que sabe o que fazer na próxima gastroenterite.',
        'melhor'),

    fim('f2', 'Alta com um percurso mais longo',
        'Marta sai viva, mas com uma noite a mais de choque ou meses de '
        'esquema errado até a correção.',
        'Esperar o teste para dar corticoide, ou repor só metade do que a '
        'glândula deixou de fazer, cobrou em tempo e em dano.', 'medio'),

    fim('f_obito', 'Óbito em casa',
        'Marta morre na madrugada seguinte, em crise adrenal não reconhecida.',
        'Pele escura, fissura por sal, sódio baixo, potássio alto e '
        'hipoglicemia numa paciente hipotensa são crise adrenal até prova em '
        'contrário. Hidrocortisona 100 mg teria custado nada.', 'pior'),

    pagina('retrospectiva', 'Retrospectiva', '',
        tabela(['Momento', 'O dado', 'O que decidiu'], [
            ['Oito meses antes', 'Sal na palma da mão, pele mais escura, vitiligo',
             'A história já tinha o diagnóstico'],
            ['Emergência', 'Sódio 124, potássio 6,1, glicemia 58, pressão 78/42',
             'Crise adrenal: tratar antes de confirmar'],
            ['Primeira hora', 'Tubo de cortisol e ACTH antes da dose',
             'Diagnóstico sem atrasar o tratamento'],
            ['Resultados', 'ACTH 480, renina alta, anti-21-hidroxilase',
             'Primária, autoimune, com falta de aldosterona'],
            ['Alta', 'Regras dos dias de doença e ampola de emergência',
             'A prevenção da próxima crise'],
        ]),
        so_kicker=True),

    pg('referencias', 'Fontes e limites',
       'Paciente, valores e percursos são ficcionais. A cena de abertura é uma ilustração autoral gerada por inteligência artificial para este caso; não é fotografia nem documentação clínica.',
       'Bornstein e cols. Diagnosis and Treatment of Primary Adrenal '
       'Insufficiency: An Endocrine Society Clinical Practice Guideline, J Clin '
       'Endocrinol Metab 2016. Arlt e cols. Society for Endocrinology Endocrine '
       'Emergency Guidance: emergency management of acute adrenal '
       'insufficiency in adult patients, Endocr Connect 2016. Husebye e cols. '
       'Adrenal insufficiency, Lancet 2021. Eletrocardiograma: Ewingdo, '
       'Wikimedia Commons, CC BY-SA 4.0, traçado de outra pessoa.'),
]

REVISAO = []

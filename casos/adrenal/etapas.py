"""Crise adrenal em insuficiência adrenal primária autoimune (síndrome poliglandular tipo 2).

Alíquota → pergunta, no molde dos casos interativos do //New England//. O caso
abre no ambulatório, com meses de cansaço, perda de peso e sódio discretamente
baixo, e o diagnóstico só é nomeado na crise, depois de uma gastroenterite.
Oito perguntas, uma rodada de exames sindrômicos com gabarito e painel, um
painel de virada, um pareamento das causas de insuficiência adrenal primária
no Brasil e duas decisões de conduta, uma delas com óbito. Paciente
ficcional; doses segundo a diretriz da Endocrine Society de 2016 e a
orientação de emergência da Society for Endocrinology de 2016.
"""
from pathlib import Path

from motor.etapas import (alt, bifurcacao, caminho, capa, desfecho, op, p,
                          pagina, painel, par, pareamento, pergunta, tabela,
                          topicos, vitais, lamina)

TITULO = 'Oito meses de cansaço'
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

    # ───────────── ambulatório: dados inespecíficos ─────────────

    pg('historia', 'Apresentação',
       'Marta, 44 anos, professora em Crateús, chega ao ambulatório de clínica '
       'médica encaminhada pela unidade básica. Há oito meses acorda cansada, '
       'perdeu 6 kg sem dieta e tem enjoo quase todas as manhãs, às vezes com '
       'dor abdominal vaga. Na sala de aula, quando levanta depressa, "a vista '
       'escurece".',
       'Há três meses, depois que a filha foi estudar em Fortaleza, o médico da '
       'unidade atribuiu o quadro a depressão e iniciou fluoxetina 20 mg. O '
       'ânimo melhorou um pouco; o cansaço, nada. Queixa ainda dores '
       'musculares difusas e menstruação irregular no último ano.'),

    pg('antecedentes', 'Antecedentes',
       'Vitiligo desde os 34 anos, nas mãos e em volta da boca, sem '
       'tratamento. Dois partos, o último por cesárea. A mãe trata '
       'hipotireoidismo. O pai tratou uma "mancha no pulmão" há vinte anos.',
       'Não fuma nem bebe. Além da fluoxetina, nega outros remédios, chás ou '
       'fitoterápicos. Tem fezes amolecidas duas ou três vezes por semana e '
       'nunca fez restrição de glúten.'),

    pagina('exame', 'Exame físico', '',
           vitais(('Pressão deitada', '104/66', False), ('Pressão em pé', '86/54', True),
                  ('Frequência deitada', '84', False), ('Frequência em pé', '108', True),
                  ('Índice de massa corporal', '19,8 kg/m²', False)),
           topicos(('Estado geral', 'Emagrecida, colaborativa, humor um pouco '
                    'deprimido. Mucosas úmidas.'),
                   ('Pele', 'Manchas acrômicas de vitiligo no dorso das mãos e '
                    'em volta da boca. Sem icterícia.'),
                   ('Pescoço', 'Tireoide palpável, discretamente aumentada, '
                    'fibroelástica, sem nódulos. Sem linfonodos.'),
                   ('Abdome', 'Flácido, indolor, sem massas nem visceromegalias.'),
                   ('Neurológico', 'Sem déficit focal. Força preservada.')),
           so_kicker=True),

    pagina('exames_ubs', 'Os exames da unidade básica', '',
           tabela(['Exame', 'Resultado', 'Referência'], [
               ['Hemoglobina', '11,6 g/dL · VCM 88 fL', '12–16 g/dL'],
               ['Leucócitos', '5.900/mm³ · eosinófilos 7% (410/mm³)', 'eosinófilos até 500'],
               ['Sódio', '131 mEq/L', '135–145'],
               ['Potássio', '5,0 mEq/L', '3,5–5,0'],
               ['Ureia / creatinina', '44 / 1,0 mg/dL', 'até 40 / 0,6–1,1'],
               ['Glicemia de jejum', '71 mg/dL', '70–99'],
           ]),
           p('Colhidos há três semanas. O médico da unidade leu o sódio como '
             'efeito da fluoxetina e o restante como normal.'),
           so_kicker=True),

    Q('p1', 1,
      'Oito meses de cansaço, 6 kg a menos, náusea, queda de pressão ao ficar '
      'de pé e sódio de 131. **Quais cinco** hipóteses devem ficar no '
      'diferencial agora?', [
      ('Hipotireoidismo primário',
       'Mãe com hipotireoidismo, vitiligo e tireoide aumentada; se grave, baixa '
       'o sódio.', True),
      ('Doença celíaca',
       'Emagrece, cansa, dá anemia e fezes amolecidas, e anda junto com o '
       'vitiligo.', True),
      ('Neoplasia oculta',
       'Seis quilos em oito meses, aos 44 anos, obrigam a procurá-la.', True),
      ('Tuberculose',
       'Pai tratado de "mancha no pulmão" e consumo lento: no Brasil, entra '
       'sempre.', True),
      ('Insuficiência adrenal primária',
       'Queda postural da pressão, náusea e sódio baixo cabem nela; ainda sem '
       'dado que a separe.', True),
      ('Depressão como explicação suficiente',
       'Não explica a hipotensão postural nem o sódio baixo, que são achados '
       'objetivos.', False),
      ('SIADH pela fluoxetina',
       'O cansaço começou cinco meses antes do remédio, e SIADH não derruba a '
       'pressão em pé.', False),
      ('Anorexia nervosa',
       'Ela quer comer e o enjoo atrapalha; não há medo de engordar nem '
       'restrição.', False),
      ('Hiperaldosteronismo primário',
       'Faz hipertensão e potássio baixo, o contrário do que ela tem.', False),
     ], 'Os achados que a depressão não explica'),

    Q('ex1', 2,
      'A clínica decide investigar antes de rotular. **Quais cinco** exames '
      'são os mais apropriados nesta consulta?', [
      ('TSH e T4 livre',
       'Tireoide aumentada e mãe com hipotireoidismo; se grave, baixa o sódio.',
       True),
      ('Osmolalidade sérica e urinária, com sódio urinário',
       'Classificam a hiponatremia antes de culpar a fluoxetina.', True),
      ('Antitransglutaminase IgA com IgA total',
       'Rastreia doença celíaca; a IgA total evita o falso negativo da '
       'deficiência de IgA.', True),
      ('Radiografia de tórax',
       'Barata, procura tuberculose e massa pulmonar num emagrecimento sem '
       'causa.', True),
      ('Sorologia anti-HIV',
       'Emagrecimento sem causa aparente pede a sorologia; o resultado muda '
       'toda a investigação.', True),
      ('Tomografia de tórax, abdome e pelve',
       'Sem alvo, rende achado incidental; entra se os exames básicos não '
       'explicarem.', False),
      ('Marcadores tumorais: CEA, CA-125 e CA 19-9',
       'Não servem para rastrear neoplasia oculta; o falso positivo é '
       'frequente.', False),
      ('Ressonância de sela túrcica',
       'Sem cefaleia, alteração visual ou outro sinal hipofisário, não há '
       'indicação agora.', False),
      ('Vitamina D e ferritina',
       'Não explicam hipotensão postural nem sódio baixo.', False),
     ], 'Primeiro, classificar a hiponatremia'),

    painel('res1', 'Resultados', 'O que a equipe pediu', [
        ex('TSH / T4 livre', '4,6 µUI/mL / 1,0 ng/dL', '0,4–4,0 / 0,9–1,7', True),
        ex('Osmolalidade sérica', '268 mOsm/kg', '275–295', True),
        ex('Osmolalidade urinária', '412 mOsm/kg', 'varia com a ingestão'),
        ex('Sódio urinário', '64 mEq/L', 'varia com a ingestão'),
        ex('Sódio / potássio séricos', '130 / 5,4 mEq/L', '135–145 / 3,5–5,0', True),
        ex('Creatinina', '1,0 mg/dL', '0,6–1,1'),
        ex('Antitransglutaminase IgA / IgA total', 'Não reagente / 210 mg/dL', 'não reagente / 70–400'),
        ex('Sorologia anti-HIV', 'Não reagente', 'não reagente'),
        ex('Radiografia de tórax', 'Campos pulmonares limpos · silhueta cardíaca estreita', '—'),
    ], introducao='Colhidos pela manhã e trazidos ao retorno, duas semanas '
                  'depois. Ela seguia com a fluoxetina.'),

    Q('p3', 3,
      'Osmolalidade sérica de 268, urinária de 412, sódio urinário de 64 e '
      'potássio de 5,4, com queda de 18 mmHg na pressão sistólica ao ficar de '
      'pé. **Quais três** conclusões estão corretas?', [
      ('A hiponatremia é hipotônica e o ADH está ativo',
       'Osmolalidade abaixo de 275 com urina acima de 100 afasta pseudo-hiponatremia '
       'e polidipsia.', True),
      ('Há perda renal de sal, com hipovolemia',
       'Perda digestiva ou pouca ingestão reteriam sódio, com urinário abaixo '
       'de 30.', True),
      ('O potássio alto sugere falta de mineralocorticoide',
       'Sem insuficiência renal nem remédio que retenha potássio, falta ação '
       'da aldosterona.', True),
      ('O sódio urinário alto afasta hipovolemia',
       'Não afasta: perda renal de sal é hipovolemia com sódio urinário alto.',
       False),
      ('Os achados confirmam SIADH pela fluoxetina',
       'SIADH é euvolêmica, não sobe o potássio e exige excluir tireoide e '
       'glicocorticoide.', False),
      ('Hipotireoidismo explica o sódio e o potássio',
       'TSH de 4,6 com T4 livre normal não baixa o sódio nem sobe o potássio.',
       False),
      ('Restrição hídrica de 800 mL por dia é a conduta inicial',
       'Com hipovolemia e perda de sal, restringir água derruba mais a pressão.',
       False),
      ('Salina a 3% para corrigir o sódio de 130 no ambulatório',
       'Sem sintoma grave, não há indicação; corrigir rápido arrisca '
       'desmielinização osmótica.', False),
     ], 'Sódio que sai pela urina, potássio que fica'),

    pg('retorno_amb', 'No mesmo retorno',
       'O marido veio junto pela primeira vez. Conta o que ela não tinha dito: '
       'há meses Marta come sal puro na palma da mão e salga a comida já '
       'servida. "Achei que era mania", diz.',
       'Ao examinar a boca, a residente nota manchas acastanhadas na gengiva e '
       'na face interna da bochecha. A cicatriz da cesárea está mais escura que '
       'a pele em volta. A fluoxetina é suspensa, os exames da manhã ficam para '
       'segunda-feira e a endocrinologia é antecipada.'),

    pg('gastro', 'Cinco dias depois',
       'Na quinta-feira, Marta e o filho mais novo comem salpicão numa festa da '
       'escola. Os dois têm vômitos e diarreia na mesma noite. O menino melhora '
       'em um dia.',
       'Ela não. No terceiro dia, não consegue ficar de pé: "a vista escurece e '
       'as pernas somem". O marido a leva à emergência do hospital no sábado à '
       'noite, antes dos exames de segunda.'),

    pagina('emergencia', 'Na emergência', '',
           vitais(('Pressão arterial', '78/42', True), ('Frequência cardíaca', '118', True),
                  ('Temperatura', '37,6 °C', False), ('Frequência respiratória', '22', False),
                  ('Glicemia capilar', '58 mg/dL', True)),
           topicos(('Estado geral', 'Sonolenta, responde com lentidão, mucosas secas.'),
                   ('Pele', 'Sulcos palmares, cotovelos e cicatriz de cesárea '
                    'escurecidos. Vitiligo nas mãos.'),
                   ('Abdome', 'Doloroso de forma difusa, sem defesa, ruídos aumentados.'),
                   ('Neurológico', 'Sem déficit focal, sem rigidez de nuca.')),
           so_kicker=True),

    pg('beira_leito', 'Os primeiros vinte minutos',
       'Gasometria venosa: pH 7,29, bicarbonato 17, sódio 124, potássio 6,1, '
       'lactato 2,4. Ureia 88 e creatinina 1,8. O eletrocardiograma mostra '
       'taquicardia sinusal com ondas T apiculadas discretas em V2 a V4.',
       'Depois de 1 litro de soro fisiológico em 20 minutos, a pressão sobe '
       'para 84/50 e volta a cair. A residente abre no celular os exames do '
       'ambulatório.'),

    # ───────────── a virada: crise, tratar antes de confirmar ─────────────

    Q('p4', 4,
      'Choque que não responde a volume, glicemia de 58, sódio de 124 e '
      'potássio de 6,1 depois de três dias de diarreia. **Quais quatro** '
      'medidas são as mais apropriadas agora?', [
      ('Hidrocortisona 100 mg EV em bolo, e 200 mg nas 24 horas seguintes',
       'Choque, sódio baixo, potássio alto e hipoglicemia nessa paciente são '
       'crise adrenal até prova em contrário.', True),
      ('Colher cortisol e ACTH antes da dose, sem atrasá-la',
       'Um tubo leva um minuto e vale o diagnóstico; se não der, trata-se sem '
       'ele.', True),
      ('Soro fisiológico, 1 litro na primeira hora e depois pela resposta',
       'A crise é também choque hipovolêmico, por perda renal e digestiva de '
       'sal.', True),
      ('Glicose endovenosa para a glicemia de 58',
       'Sonolência com glicemia de 58 não espera o resto.', True),
      ('Aguardar a cortrosina das 7 horas antes de qualquer corticoide',
       'O teste confirma depois; esperar por ele com pressão de 78 custa horas '
       'de choque.', False),
      ('Fludrocortisona 0,1 mg oral já na emergência, junto com o soro',
       'Acima de 50 mg por dia, a hidrocortisona cobre o mineralocorticoide; e '
       'ela vomita.', False),
      ('Salina a 3% em bolo de 150 mL para o sódio de 124',
       'Sem convulsão, não entra; com volume e corticoide, o risco é corrigir '
       'rápido demais.', False),
      ('Noradrenalina em veia periférica antes de completar o volume',
       'Sem volume e sem cortisol, o vasopressor rende pouco; entra se o '
       'choque persistir.', False),
      ('Insulina regular com glicose para o potássio de 6,1',
       'Com glicemia de 58, insulina é perigosa; o potássio cai com soro e '
       'corticoide.', False),
     ], 'Tratar antes de confirmar'),

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
              'A pressão melhorou um pouco com o soro, e três dias de diarreia '
              'explicam a desidratação.'),
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
       'acordada, com horas a mais de choque na conta.',
       segue='tratado'),

    pg('tratado', 'Seis horas depois da hidrocortisona',
       'Pressão de 108/64, glicemia de 96, diurese boa. O sódio subiu de 124 '
       'para 128 e o potássio caiu para 5,0. Ela pede água e pergunta onde '
       'está.'),

    painel('res2', 'Resultados', 'O que a equipe pediu na crise', [
        ex('Cortisol (antes da hidrocortisona)', '**2,1 µg/dL**', '> 18 µg/dL no estresse', True),
        ex('ACTH', '**480 pg/mL**', '7–63 pg/mL', True),
        ex('Renina ativa', '185 µUI/mL', '4–46 µUI/mL', True),
        ex('Aldosterona', '< 3 ng/dL', '3–16 ng/dL', True),
        ex('Anti-21-hidroxilase', 'Reagente', 'não reagente', True),
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

    Q('p5', 5,
      'Cortisol de 2,1 no choque confirma a insuficiência. Hiponatremia aparece '
      'nos dois tipos, primária e secundária. **Quais quatro** achados indicam '
      'que a dela é primária?', [
      ('Hiperpigmentação de pele e gengiva',
       'O ACTH alto e seu precursor estimulam o melanócito; na secundária, a '
       'pele empalidece.', True),
      ('Potássio alto desde o ambulatório',
       'Falta de aldosterona, que só ocorre quando a glândula é destruída.',
       True),
      ('Renina alta com aldosterona baixa',
       'O eixo renina-aldosterona não depende da hipófise.', True),
      ('ACTH de 480',
       'A hipófise responde ao cortisol baixo.', True),
      ('Sódio de 124',
       'Nas duas: a falta de cortisol libera vasopressina e retém água.',
       False),
      ('Glicemia de 58', 'Nas duas: é falta de cortisol.', False),
      ('Eosinófilos de 1.100', 'Nas duas: também é falta de cortisol.', False),
      ('Queda da pressão ao ficar de pé',
       'Mais intensa na primária, mas presente nas duas.', False),
      ('Seis quilos a menos em oito meses',
       'Nas duas, e também em metade do diferencial inicial.', False),
     ], 'O que é do ACTH e o que é da aldosterona'),

    pareamento('p6', 'Pergunta 6',
      'A causa de Marta é autoimune. Associe cada cenário à causa mais '
      'provável de insuficiência adrenal primária.', [
      par('Mulher com vitiligo, tireoidite e anti-21-hidroxilase reagente',
          'Adrenalite autoimune',
          'Causa mais comum no Brasil urbano, em geral com outras doenças '
          'autoimunes.'),
      par('Homem de 62 anos, tuberculose tratada na juventude, adrenais '
          'pequenas e calcificadas na tomografia',
          'Infecção granulomatosa',
          'A tuberculose destrói as duas adrenais e deixa calcificação.'),
      par('Lavrador de 55 anos com úlceras orais de fundo granuloso e '
          'adrenais aumentadas',
          'Infecção fúngica endêmica',
          'Paracoccidioidomicose: na forma crônica, as adrenais são acometidas '
          'com frequência.'),
      par('Jovem com púrpura fulminante e choque por meningococo',
          'Hemorragia adrenal bilateral',
          'Síndrome de Waterhouse-Friderichsen.'),
      par('Idoso anticoagulado, no quarto dia de artroplastia, com dor '
          'lombar e choque',
          'Hemorragia adrenal bilateral',
          'Anticoagulação e estresse pós-operatório são o cenário típico.'),
      par('Menino de 9 anos com piora escolar, espasticidade e ácidos graxos '
          'de cadeia muito longa elevados',
          'Doença genética peroxissomal',
          'Adrenoleucodistrofia ligada ao X: dosar esses ácidos graxos em todo '
          'menino com a doença.'),
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
      caminho('Hidrocortisona 15 a 25 mg por dia em duas ou três tomadas, '
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

    Q('p7', 7,
      'Antes da alta, a enfermagem ensina a Marta e ao marido as regras dos '
      'dias de doença. **Quais quatro** orientações estão corretas?', [
      ('Febre acima de 38 °C: dobrar a hidrocortisona; acima de 39 °C, triplicar',
       'Enquanto durar a febre, em geral dois a três dias, e voltar à dose '
       'habitual.', True),
      ('Vômitos ou diarreia intensa: 100 mg intramuscular e emergência',
       'Foi a gastroenterite que abriu a crise dela; comprimido vomitado não '
       'protege.', True),
      ('Cirurgia de grande porte: 100 mg na indução e 200 mg em 24 horas',
       'O anestesista precisa saber, e o cartão serve para isso.', True),
      ('Andar com cartão ou pulseira de identificação',
       'Inconsciente, ela não vai poder dizer que tem Addison.', True),
      ('Suspender a fludrocortisona enquanto durar a febre, para não reter líquido',
       'Não há motivo; a fludrocortisona não precisa de ajuste no estresse.',
       False),
      ('Dobrar também a fludrocortisona nos dias de febre ou de estresse',
       'Quem sobe é a hidrocortisona.', False),
      ('Na gastroenterite leve, manter a dose habitual e observar por 48 horas',
       'Foi exatamente assim que ela chegou em choque.', False),
      ('Reduzir a hidrocortisona por conta própria se ganhar peso ou inchar',
       'O ajuste é com a equipe; reduzir por conta leva à crise.', False),
     ], 'Dobrar, injetar, avisar'),

    Q('p8', 8,
      'Adrenalite autoimune, tireoidite com anti-TPO e vitiligo: síndrome '
      'poliglandular autoimune tipo 2. O TSH foi 4,6 no ambulatório e 6,8 na '
      'crise, com T4 livre normal. **Quais quatro** condutas estão corretas?', [
      ('Repetir TSH e T4 livre após seis a oito semanas de reposição',
       'A falta de cortisol eleva o TSH, que muitas vezes normaliza com a '
       'hidrocortisona.', True),
      ('Glicemia de jejum e hemoglobina glicada periódicas',
       'Diabetes tipo 1 faz parte da síndrome.', True),
      ('Vitamina B12 e hemograma no seguimento',
       'Gastrite atrófica autoimune e anemia perniciosa se associam.', True),
      ('FSH e estradiol pela irregularidade menstrual',
       'Insuficiência ovariana autoimune também acompanha a síndrome.', True),
      ('Iniciar levotiroxina já, pelo TSH de 6,8 e o anti-TPO',
       'TSH abaixo de 10, dosado na crise, tende a cair; tratar agora é tratar '
       'um número.', False),
      ('Paratormônio e cálcio para hipoparatireoidismo',
       'Hipoparatireoidismo e candidíase são da síndrome tipo 1, da infância.',
       False),
      ('Pesquisa de mutação no gene AIRE, para a família',
       'É o exame da síndrome tipo 1, que ela não tem.', False),
      ('Cortisol sérico a cada consulta para ajustar a dose',
       'Com hidrocortisona, o cortisol oscila com a tomada e não guia a dose.',
       False),
      ('Anti-21-hidroxilase anual para acompanhar a atividade',
       'Já é reagente; repetir não muda nada.', False),
     ], 'O TSH da crise não é o TSH dela'),

    pg('alta', 'Preparando a alta',
       'Marta sai com o esquema da alta, a ampola de hidrocortisona na bolsa '
       'e o marido treinado para aplicar.',
       conforme=('b2', ['alta_cedo', 'f2', 'f2'])),

    pg('alta_cedo', 'Na véspera da alta',
       'Ela conta que, pela primeira vez em meses, não sentiu vontade de comer '
       'sal. A gengiva e as cicatrizes vão clarear devagar, com a queda do '
       'ACTH.',
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
        'Choque que não responde a volume, sódio baixo, potássio alto e '
        'hipoglicemia, numa paciente com gengiva escura e fissura por sal, são '
        'crise adrenal até prova em contrário. Hidrocortisona 100 mg teria '
        'custado nada.', 'pior'),

    pagina('retrospectiva', 'Retrospectiva', '',
        tabela(['Momento', 'O dado', 'O que decidiu'], [
            ['Ambulatório', 'Hipotensão postural e sódio de 131 atribuídos à fluoxetina',
             'Sinais objetivos que a depressão não explicava'],
            ['Retorno', 'Sódio urinário de 64 com potássio de 5,4',
             'Perda renal de sal: pensar na aldosterona'],
            ['Mesmo retorno', 'Sal na palma da mão, gengiva e cicatriz escurecidas',
             'O pigmento do ACTH alto'],
            ['Emergência', 'Pressão 78/42, glicemia 58, sódio 124, potássio 6,1',
             'Crise adrenal: tratar antes de confirmar'],
            ['Resultados', 'Cortisol 2,1, ACTH 480, renina alta, anti-21-hidroxilase',
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

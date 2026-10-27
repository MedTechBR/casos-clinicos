"""Revisão editorial de 23/10/2026: evolução clínica, decisões precoces e
urgências preservadas. Paciente e cronologia ficcionais; fontes na última tela.
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
 'Marta, professora de 44 anos de Crateús, chega no sábado à noite, no terceiro dia de vômitos e diarreia aquosa. Ela e o filho de 9 anos comeram salpicão numa festa da escola; ele melhorou em um dia. Ela foi à UPA ontem, recebeu soro e ondansetrona, voltou a beber água, mas nesta manhã os vômitos retornaram e passou a precisar de ajuda para ir ao banheiro.',
 'Há oito meses perde energia; há dois meses deixou as caminhadas e precisa sentar durante as aulas. Perdeu 6 kg sem dieta. Hoje escurece a vista ao levantar. Nega sangue nas fezes, febre alta, dor torácica, dispneia, viagem, antibiótico recente ou redução deliberada de alimentos.'),

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

    pg('socorro', 'Os primeiros minutos',
 'A sonolência melhora após 25 g de glicose endovenosa, mas ela continua incapaz de sentar por tontura. Iniciam monitorização, acesso venoso e solução salina isotônica, com reavaliação de perfusão e pulmões. A coleta não interrompe a ressuscitação.',
 'A história medicamentosa é conferida: não usa corticoide por nenhuma via, diurético, bloqueador do sistema renina–angiotensina ou suplemento de potássio. Não tem doença renal conhecida. Os resultados abaixo e o ECG da admissão são revistos em conjunto, sem uma espera clínica entre as telas.'),

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

    painel('res1b', 'Avaliação inicial do choque', 'Gasometria e urina', [
        ex('Gasometria arterial em ar ambiente', 'pH 7,31 · pCO₂ 33 mmHg · HCO₃ 16 mmol/L · pO₂ 92 mmHg · lactato 2,4 mmol/L', '—', True),
        ex('Urina', 'Densidade 1.022 · sem proteína, sangue ou leucócitos · raros cilindros hialinos', '—'),
    ], introducao='Gasometria e lactato pela hipoperfusão; urina na avaliação da função renal. Não se espera este painel para repor glicose e volume.'),

    estudo('ecg', 'Eletrocardiograma',
           'Feito à beira do leito pelo potássio de 6,1, com ela em taquicardia sinusal de 118. Olhe a forma da onda T antes de abrir os achados.',
           IMG / 'ecg_hipercalemia.jpg',
           'Eletrocardiograma.',
           credito_meta(IMG / 'ecg_hipercalemia.jpg.json'),
        [
         ((807, 316), (930, 250), '**Onda T** alta, pontiaguda e de base estreita em V4.', -12),
         ((129, 172), (60, 250), 'O mesmo formato da **onda T** em DII.', 12),
         ((396, 648), (300, 725), '**QRS estreito** na tira longa de DII.', 12),
        ],
        ['Ondas T altas, simétricas e de base estreita, mais evidentes de V3 a '
         'V5, com QRS estreito.',
         'O laudo descreve alterações de repolarização, com duração do QRS preservada.']),

    pg('primeira_resposta', 'Vinte minutos depois',
 'Após o primeiro litro de salina, a pressão chega a 92/58, a perfusão melhora e Marta conversa; ainda não consegue ficar em pé. O ECG da chegada motivou gluconato de cálcio a 10%, 30 mL EV em 10 minutos, com monitorização. A glicose segue em infusão.',
 'Para reduzir o potássio, recebe insulina regular com glicose após corrigir a hipoglicemia, conforme protocolo local. A glicemia é medida repetidamente por pelo menos seis horas, com reposição adicional de glicose pelo alto risco de nova queda. Insulina não é um erro por si: exige proteção e vigilância. O cálcio protege o coração, mas não remove potássio.',
 'A melhora circulatória foi parcial. O sódio baixo, a alteração do potássio e a função renal motivam agora estudos de osmolalidade e eletrólitos urinários, além do controle seriado dos valores sanguíneos. Não se presume que todo o distúrbio decorra da diarreia.'),

    painel('res_sodio', 'Investigação dirigida', 'Água e eletrólitos', [
        ex('Osmolalidade sérica', '264 mOsm/kg', '275–295 mOsm/kg', True),
        ex('Osmolalidade urinária', '418 mOsm/kg', '—'),
        ex('Sódio / potássio / cloro urinários', '62 / 14 / 58 mmol/L', '—'),
    ], introducao='Solicitados após Na 124, K 6,1 e a primeira reavaliação clínica. Para interpretar a perda renal de sal, o laboratório utiliza as amostras iniciais de sangue e urina, anteriores à salina. Estes resultados não condicionam a ressuscitação nem a coleta hormonal indicada na reavaliação seguinte.'),

    Q('p1', 1, 'Quais duas hipóteses você prioriza na admissão?', [
 ('Insuficiência adrenal primária', True), ('Sepse com foco gastrointestinal', True),
 ('Síndrome de secreção inapropriada de ADH isolada', False),
 ('Efeito isolado da fluoxetina', False), ('Insuficiência cardíaca descompensada', False)
 ], [('Hierarquia', 'Hipovolemia é real, mas hipercalemia, hipoglicemia e distúrbios prévios à diarreia exigem investigar insuficiência adrenal desde já. Infecção pode ser o gatilho e também causa concorrente de choque; colher culturas e avaliar antibiótico conforme suspeita, sem esperar exclusão de uma hipótese para tratar outra.'), ('Limites', 'Fluoxetina pode contribuir para hiponatremia, mas não explica este choque com retenção de potássio. Urina concentrada também ocorre por ADH estimulado pela hipovolemia; não basta para chamar SIADH. O gap urinário de +18 (62 + 14 − 58) sugere excreção de amônio inadequada, sem provar isoladamente acidose tubular.'), ('Como comparar as hipóteses', 'Diarreia e sepse podem produzir hipotensão e alteração renal. A combinação com sódio baixo, potássio alto e hipoglicemia pede considerar deficiência hormonal. Essa combinação aumenta a suspeita, mas a confirmação depende da avaliação hormonal e da evolução.')]),

    pg('recorrencia', 'Durante a primeira hora',
 'Os vômitos cessam com o antiemético e a pressão melhorou brevemente, mas cai outra vez a 82/48. Marta fica nauseada ao elevar a cabeceira; glicemia de 62 apesar da reposição. Não há nova evacuação, perda externa importante ou crepitações. A equipe percebe que cessar as perdas não restaurou a circulação.',
 'Já na primeira reavaliação são colhidos cortisol e ACTH antes do corticoide, sem esperar laudo ou estímulo. O marido acrescenta que ela passou a comer sal puro e escureceu em meses. Esses são dados antigos agora conhecidos, diferentes da recorrência observada no leito.'),

    pg('terapia', 'Tratamento sem esperar a confirmação',
 'Com suspeita de crise adrenal, recebe hidrocortisona 100 mg EV imediatamente, seguida de 200 mg em 24 horas, aqui como 50 mg a cada seis horas. A infusão de salina é ajustada ao exame e à perfusão; glicose e eletrólitos seguem monitorizados. Se persistisse choque, norepinefrina seria suporte, sem substituir o corticoide.',
 'Não se aguarda teste de cortrosina, manhã seguinte ou fotografia para iniciar. A sequência de imagens abaixo é revisão dos registros e achados examinados durante a ressuscitação, não tempo adicional sem tratamento.'),

    bifurcacao('b1', 'Reavaliação', 'Quanto volume ainda ajuda?',
 'A hidrocortisona já foi administrada e a reposição de volume continua em paralelo. Qual avaliação adicional você prioriza para orientar os próximos bolus?', [
 caminho('Ultrassonografia cardiopulmonar à beira do leito', 'volume_us', 'Pode avaliar congestão, função ventricular e causas alternativas de choque; integrar com resposta clínica.'),
 caminho('Elevação passiva das pernas com medida do volume sistólico', 'volume_dinamico', 'Avalia resposta dinâmica a volume, quando mensurada adequadamente; pressão isolada não basta.')]),

    pg('volume_us', 'Reavaliação à beira do leito',
 'A ultrassonografia mostra ventrículo esquerdo hiperdinâmico, sem derrame pericárdico ou linhas B difusas. A perfusão melhora durante um bolus de 250 mL, mas a pressão continua baixa. O achado permite reposição cautelosa; não autoriza litros sucessivos sem reexame.', segue='reexame'),

    pg('volume_dinamico', 'Resposta dinâmica',
 'Com elevação passiva das pernas, o volume sistólico estimado aumenta 13%. Um bolus de 250 mL melhora a perfusão; a pressão, entretanto, permanece em 84/50. Ser responsiva a volume não significa que toda a hipotensão decorra de perda de líquido.', segue='reexame'),

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

    estudo('rx', 'Radiografia de tórax',
           'Pedida na sala vermelha, antes de mais volume, para procurar '
           'congestão, derrame ou um foco de infecção que explique o choque.',
           IMG / 'rx_torax.jpg',
           'Radiografia.',
           credito_meta(IMG / 'rx_torax.jpg.json'),
        [
         ((236, 500), (110, 420), '**Vasos pulmonares** de calibre normal: sem congestão.', 12),
         ((100, 955), (60, 1060), '**Seio costofrênico** direito livre: sem derrame.', 12),
         ((721, 786), (880, 700), '**Borda esquerda do coração**: área cardíaca sem aumento.', -12),
        ],
        ['Pulmões limpos, sem congestão nem consolidação. Seios costofrênicos '
         'livres. Área cardíaca normal.',
         'Não há foco pulmonar evidente ou congestão radiográfica. A imagem isolada não decide tolerância a mais volume; perfusão, exame e medidas dinâmicas orientam a reposição. A resposta incompleta já motivou tratamento hormonal.']),

    estudo('foto_gengiva', 'A boca',
           'Com a lanterna, a residente afasta os lábios de Marta e encontra manchas acastanhadas na gengiva e na face interna das bochechas. Procure onde a cor muda antes de abrir os achados.',
           IMG / 'gengiva_pigmento.jpg',
           'Gengiva, com pigmento acastanhado.',
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
           'Marta abre as mãos: os sulcos palmares estão escurecidos, em contraste com as manchas acrômicas do dorso. Olhe as linhas da mão, não a cor de fundo.',
           IMG / 'sulcos_palmares.jpg',
           'Palmas, com os sulcos escurecidos.',
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

    pg('tratado', 'Seis horas depois',
 'Marta está orientada, pede comida e consegue sentar sem a sensação de desmaio. Pressão 108/64, sem vasopressor; a infusão de glicose pode ser reduzida. O abdome já não dói. A resposta favorece a hipótese, sem confirmar sozinha sua causa.',
 'A diurese começa a aumentar. A prioridade passa da restauração da perfusão para acompanhar água, sódio e potássio; a equipe não mantém automaticamente o mesmo volume de soro da chegada.'),

    painel('res2', 'Resultados', 'A amostra basal da crise', [
        ex('Cortisol (antes da primeira dose)', '**2,1 µg/dL**', 'manhã: 5–25 µg/dL', True),
        ex('ACTH', '**480 pg/mL**', '7–63 pg/mL', True),
    ], introducao='Amostra colhida antes da primeira dose de hidrocortisona.'),

    Q('p2', 2, 'Quais três dosagens você solicita após os primeiros resultados hormonais?', [
 ('Renina plasmática', True), ('Aldosterona plasmática', True), ('Anticorpo anti-21-hidroxilase', True),
 ('Prolactina', False), ('Metanefrinas livres plasmáticas', False), ('Novo cortisol sob hidrocortisona', False)
 ], [('Perguntas diferentes', 'Renina e aldosterona devem ser interpretadas em conjunto, considerando postura, potássio, volume, medicações e momento da coleta. O anticorpo pesquisa autoimunidade; vitiligo e história familiar a favorecem. As três dosagens aparecem na narrativa mesmo se não foram selecionadas.'), ('Confirmação', 'Cortisol muito baixo com ACTH marcadamente alto sustenta falência primária. Estímulo pode ser organizado quando seguro se persistir dúvida; não se interrompe cobertura necessária para obter um teste. Dosar cortisol durante hidrocortisona não recupera o basal.'), ('Localizar antes de procurar a causa', 'Cortisol baixo com ACTH muito elevado aponta para falha da adrenal. Deficiência central costuma preservar a aldosterona. Renina e aldosterona avaliam esse componente; o anticorpo investiga uma causa possível, sem substituir a avaliação funcional.')]),

    painel('res2_complemento', 'Investigação complementar', 'Etiologia e eixos associados', [
 ex('Renina plasmática', '185 µUI/mL', '4–46 µUI/mL', True),
 ex('Aldosterona', '< 3 ng/dL', '3–16 ng/dL', True),
 ex('Anticorpo anti-21-hidroxilase', 'Reagente', 'não reagente', True),
 ex('TSH / T4 livre', '6,8 µUI/mL / 1,0 ng/dL', '0,4–4,0 / 0,9–1,7', True),
 ex('Anti-TPO', '340 UI/mL', 'até 35 UI/mL', True)
 ], introducao='Resumo da causa com laudos liberados ao longo dos dias seguintes; depois retomaremos a evolução das primeiras 24 horas. Renina e aldosterona vieram de alíquotas colhidas antes da reposição hormonal, sem atrasá-la; a reavaliação longitudinal considerará o tratamento e o estado volêmico.'),

    pg('virada', 'Integração diagnóstica',
 'O conjunto estabelece insuficiência adrenal primária autoimune, doença de Addison, descompensada por provável gastroenterite. Sem cortisol, há menor resposta vascular, tendência à hipoglicemia e maior estímulo de ADH; sem aldosterona, perda renal de sal e dificuldade de eliminar potássio. O ACTH elevado ajuda a explicar pigmentação progressiva.',
 'Vitiligo e autoimunidade tireoidiana indicam avaliar associação poliglandular. O anti-TPO positivo com T4 livre normal durante a crise não comprova hipotireoidismo persistente nem exige levotiroxina imediata. A classificação da associação tireoidiana será revista após recuperação.'),

    pg('noite', 'Doze horas após a admissão',
 'Está lúcida, sem vômitos e com pressão sustentada. Nas últimas duas horas urinou 350 mL/h; a urina tem osmolalidade de 90 mOsm/kg. O sódio passou de 124 para 132 mmol/L e o potássio caiu para 4,6. A bolsa de salina ainda corre a 150 mL/h.',
 'A melhora circulatória veio acompanhada de nova perda de água livre. Ausência de sintomas não demonstra segurança para continuar corrigindo no mesmo ritmo.'),

    Q('p3', 3, 'Na reavaliação da hidratação, qual ajuste você faz?', [
 ('Suspender a infusão de salina a 150 mL/h', True), ('Suspender a hidrocortisona de estresse', False),
 ('Aumentar a infusão de salina para 250 mL/h', False), ('Reduzir o controle de sódio para uma vez ao dia', False)
 ], [('Prioridade', 'A reposição de salina nessa velocidade deve ser interrompida e revista. Aumento de 8 mmol/L em 12 horas com aquarese ameaça ultrapassar um limite diário conservador. Vigiar sódio e diurese permite considerar água livre e desmopressina com equipe experiente.'),
 ('Não trocar um risco por outro', 'Não se retira a cobertura de cortisol para controlar o sódio. Monitorização e reposição de glicose dependem da evolução, não do número do sódio isoladamente.')]),

    pg('freio', 'Controle da aquarese',
 'A salina é suspensa, o sódio passa a ser controlado a cada duas horas e a diurese, de hora em hora. Com a perda de água ainda intensa, a equipe utiliza desmopressina e glicose a 5% tituladas para conter a trajetória, sem suspender hidrocortisona. O sódio fica em 131–132 até completar 24 horas e chega a 134 em 48 horas.',
 'A hiponatremia já existia antes da diarreia. A meta é recuperação segura, não normalizar depressa. A necessidade de frear a correção é um evento desta simulação, não uma consequência obrigatória de toda reposição.'),

    pg('transicao', 'Terceiro dia',
 'Sem vômitos, Marta come e caminha alguns passos. Ao reduzir a dose de estresse e passar para via oral, volta a ter tontura ao levantar; pressão 112/70 deitada e 92/60 em pé, sem congestão. O potássio é 5,1. Não há nova diarreia.',
 'A equipe distingue absorção oral preservada de reposição mineralocorticoide ainda necessária. A hidrocortisona em dose alta tinha atividade mineralocorticoide suficiente para a fase aguda; isso muda ao chegar à manutenção.'),

    Q('p4', 4, 'Qual medicamento você acrescenta na transição para a manutenção?', [
 ('Fludrocortisona', True), ('Midodrina', False), ('Espironolactona', False), ('Levotiroxina', False)
 ], [('Reposição', 'Fludrocortisona repõe a deficiência de aldosterona, com ajuste por sintomas, pressão deitada/em pé, eletrólitos e renina. Midodrina pode elevar pressão, mas não corrige a deficiência. Espironolactona antagoniza o eixo já insuficiente; levotiroxina não trata esta hipotensão.')]),

    pg('manutencao', 'Antes da alta',
 'Com fludrocortisona 0,1 mg pela manhã e hidrocortisona 10 mg ao acordar, 5 mg ao meio-dia e 5 mg à tarde, consegue caminhar sem tontura. Potássio 4,4, sódio 136 e pressão em pé 108/68. As doses serão individualizadas; cortisol e ACTH não são alvos de titulação rotineira.',
 'Recebe cartão de emergência, prescrição e treinamento do kit intramuscular de hidrocortisona 100 mg. Marta e o marido ensaiam preparo e aplicação com a enfermagem. Vômitos que impedem comprimidos exigem via parenteral e atendimento urgente.'),

    Q('p5', 5, 'No episódio febril descrito, qual dose oral diária deve constar no plano domiciliar?', [
 ('Hidrocortisona 40 mg em tomadas divididas', True), ('Hidrocortisona 20 mg em tomadas divididas', False),
 ('Hidrocortisona 30 mg em tomadas divididas', False), ('Hidrocortisona 40 mg apenas no primeiro dia, mesmo permanecendo febril', False)
 ], [('Dia de doença', 'Neste esquema basal de 20 mg, 40 mg/dia divididos é a dose de estresse prevista enquanto durar a intercorrência, com revisão se não melhorar. Se não retiver a medicação, não basta aumentar comprimidos: usar o kit e procurar emergência. A orientação escrita deve ser adaptada pela equipe assistente.')]),

    pg('seguimento', 'Oito a doze semanas depois',
 'Marta voltou à escola gradualmente. Apetite e tolerância ao ortostatismo recuperaram antes da pigmentação, que clareia devagar. Não teve novas perdas digestivas. TSH de controle 3,1 µUI/mL com T4 livre normal, sem levotiroxina; mantém vigilância da autoimunidade tireoidiana.',
 'A avaliação periódica inclui peso, energia, pressão em pé, eletrólitos, renina e sinais de excesso de reposição; sintomas novos motivam rastreio dirigido de outras doenças autoimunes.'),

    fim('f1', 'Recuperação com plano de prevenção',
 'Marta retoma suas atividades com reposição dos dois eixos e um plano compreendido pela família.',
 'A resposta parcial ao volume levou à terapia precoce; a aquarese mudou a infusão; o ortostatismo na transição mudou a reposição. Nenhum resultado confirmatório foi usado como condição para tratar a crise.', 'melhor'),

    pagina('retrospectiva', 'Pontos de ensino', '', pontos(
 'Perdas intestinais podem precipitar uma deficiência hormonal anterior e não explicar toda a instabilidade.',
 'Hipercalemia com hipoglicemia e distúrbios prévios ao episódio agudo exige ampliar a hipótese desde a primeira avaliação.',
 'Suspeita de crise adrenal pede hidrocortisona imediata; coleta basal só quando não atrasa a dose.',
 'Insulina com glicose pode estar indicada na hipercalemia; prevenir hipoglicemia é parte do tratamento.',
 'Diurese e ritmo do sódio importam mesmo quando o paciente melhora.',
 'A dose de estresse não substitui a reposição mineralocorticoide de manutenção nem o ensino do kit de emergência.'), so_kicker=True),

    pg('referencias', 'Fontes e limites',
 'Paciente e cronologia ficcionais. A abertura é ilustração gerada por inteligência artificial. As ramificações comparam métodos de reavaliação; não associam erro a morte inevitável.',
 'Revisão em 23/10/2026: <a href="https://www.nice.org.uk/guidance/ng243">NICE NG243, 2024</a>; <a href="https://www.endocrinology.org/clinical-practice/clinical-guidance/adrenal-crisis/">Society for Endocrinology, crise adrenal</a>; <a href="https://www.endocrine.org/clinical-practice-guidelines/primary-adrenal-insufficiency">Endocrine Society, insuficiência primária, 2016</a>. UK Kidney Association, manejo da hipercalemia, 2023; Society for Endocrinology, orientação de hiponatremia sintomática, 2022. As fontes mais antigas permanecem identificadas por data, sem serem apresentadas como novas.',
 'Imagens de outras pessoas, com setas adicionadas: ECG, Michael-Joseph F. Agbayani e Eddieson Gonzales, Wikimedia Commons, CC BY 4.0; radiografia, Mikael Häggström, CC0; gengiva, Shaimaa Abdellatif, CC BY-SA 4.0, recortada (commons.wikimedia.org/wiki/File:Hyperpigmentation_of_the_gum.jpg); palmas, Petros Perros, PLoS Medicine via Wikimedia Commons, CC BY 2.5, recortada (commons.wikimedia.org/wiki/File:A_69-Year-Old_Female_with_Tiredness_and_a_Persistent_Tan_02.png). Créditos e coordenadas das figuras preservados.')
]

REVISAO = []

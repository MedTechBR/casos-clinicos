"""Doença neuroinvasiva pelo vírus do Nilo Ocidental — paralisia flácida aguda.

Alíquota → pergunta, na gramática do //New England//. Paciente ficcional;
evoluções autorais, sem pretensão de prognóstico individual.
"""
from pathlib import Path
from motor.estudo_imagem import ecg, sequencia
from motor.etapas import (alt, bifurcacao, caminho, capa, desfecho, grupo,
    lamina, op, p, pagina, par, pareamento, pedido, pergunta, resultados,
    tabela, topicos, vitais)

TITULO = 'O peso dos dias'
RODAPE = 'Caso ficcional · evoluções simuladas para ensino'
IMG = Path(__file__).parent / 'img'
BANCO = []
CENA = 'cena.png'
CREDITO = ('Ilustração gerada por IA para este paciente ficcional; não é '
           'documentação de achado clínico.')


def pg(k, titulo, *blocos, **kw):
    return pagina(k, titulo, '', *blocos, fundo=CENA, so_kicker=True, **kw)


def ex(n, r, ref='—', a=False):
    return op(n, resultado=r, referencia=ref, alterado=a)


def q(k, n, texto, itens, titulo, segue=''):
    return pergunta(k, f'Pergunta {n}', texto,
        [alt(t, c, certa=ok) for t, c, ok in itens],
        titulo_resposta=titulo, fundo=CENA, segue=segue)


def fim(k, titulo, texto, porque, qualidade='medio'):
    return desfecho(k, titulo, p(texto), qualidade=qualidade, porque=porque,
                    fundo=CENA, fecho='retrospectiva')


ETAPAS = [
    capa(TITULO, fundo=CENA,
         kicker='Caso interativo · 13 perguntas · 3 rodadas de exames · 4 decisões',
         procedencia='Paciente ficcional. Curso simulado.'),

    pg('historia', 'Apresentação',
       p('Antônio, 71 anos, é levado pela esposa ao pronto atendimento porque, '
         'naquela manhã, não conseguiu ir sozinho ao banheiro. Há quatro dias '
         'tem febre e cefaleia. Ao entrar no consultório, diz que está "sem '
         'firmeza nas pernas" e que deve ter se alimentado mal.'),
       p('Até a semana anterior caminhava até o mercado, cuidava das próprias '
         'contas e buscava o neto na escola. A esposa estranhou que ele '
         'precisasse se apoiar nos móveis e demorasse a responder a perguntas '
         'simples.'),
       lamina_=lamina(CENA, 'Antônio, na admissão',
                      'Ilustração do paciente ficcional.', CREDITO)),

    q('p1', 1,
      'Homem de 71 anos, quatro dias de febre e cefaleia, e hoje não '
      'consegue ir ao banheiro sozinho. **Quais quatro** hipóteses precisam '
      'ser consideradas de imediato?', [
      ('Meningoencefalite infecciosa',
       'Febre, cefaleia e mudança de comportamento em quatro dias. É a '
       'hipótese que não pode esperar exame: cada hora sem tratamento '
       'empírico custa.', True),
      ('Doença de Alzheimer',
       'Curso de anos, sem febre. Uma semana atrás ele cuidava das contas '
       'da casa.', False),
      ('Sepse de foco extraneural com delirium',
       'Pneumonia ou infecção urinária no idoso se apresentam assim: '
       'confusão e queda antes de qualquer sintoma local. Examine e '
       'culture.', True),
      ('Neuropatia diabética',
       'Sensitiva, distal, simétrica e crônica. Não explica a febre nem a '
       'lentificação de quatro dias.', False),
      ('Acidente vascular cerebral',
       'A perna que cedeu de manhã é um déficit focal até prova em '
       'contrário — e febre não exclui AVC. Imagem antes da punção.', True),
      ('Miastenia gravis',
       'Fatigabilidade sem febre e sem alteração cognitiva. Não é este '
       'padrão.', False),
      ('Hiponatremia ou hipoglicemia',
       'Diabético sem se alimentar, febril, com losartana: as causas '
       'metabólicas de confusão custam um minuto de bancada e são as '
       'primeiras a excluir.', True),
      ('Hipotensão postural pela losartana',
       'Explicaria uma queda, não quatro dias de febre com lentificação.',
       False),
     ], 'Infecção, foco, vaso e metabolismo — nessa ordem de pressa'),

    pg('hda', 'História da doença atual',
       p('Quatro dias antes, começou com indisposição e dor de cabeça difusa, '
         'de instalação gradual, com calafrios. A temperatura chegou a '
         '38,4 °C em casa. Tomou paracetamol, com alívio por algumas horas, '
         'mas ficou sem apetite. Sem tosse, coriza, dor torácica ou ardor '
         'para urinar.'),
       p('Na véspera da admissão, precisou interromper o banho para sentar-se. '
         'A esposa percebeu que ele derrubou um copo e perguntou duas vezes '
         'sobre um compromisso já cancelado. Pela manhã, ao tentar levantar, '
         'a perna direita cedeu. Não perdeu a consciência e não bateu a '
         'cabeça. Ela não observou convulsão, desvio da boca ou fala '
         'arrastada.')),

    q('p2', 2,
      'Perguntas repetidas, perda do fio da conversa quando duas pessoas '
      'falam, e piora ao entardecer. **Quais três** características '
      'distinguem delirium de demência?', [
      ('Início em horas ou dias',
       'Demência se instala em meses ou anos. Uma semana entre "cuidava '
       'das contas" e "não acha o banheiro" é delirium até prova em '
       'contrário.', True),
      ('Desorientação no tempo e no espaço',
       'Presente nos dois. Não distingue.', False),
      ('Flutuação ao longo do dia',
       'Pior à noite, melhor de manhã: é a marca do delirium, e o que faz '
       'o exame das 8h discordar do das 20h.', True),
      ('Déficit de atenção como núcleo do quadro',
       'Delirium é falha de atenção; demência é falha de memória com '
       'atenção preservada até tarde. Peça os meses do ano de trás para '
       'frente.', True),
      ('Alucinações visuais',
       'Mais frequentes no delirium, mas presentes na demência com corpos '
       'de Lewy. Não separam.', False),
      ('Prejuízo de memória recente',
       'Comum aos dois — no delirium, secundário à atenção que falha.',
       False),
      ('Alteração do ciclo sono-vigília',
       'Acontece em ambos. Sozinha, não decide.', False),
     ], 'Agudo, flutuante e desatento'),

    pg('antecedentes', 'Antecedentes e medicações',
       p('Hipertensão há catorze anos e diabetes tipo 2 há sete, acompanhados '
         'na unidade de saúde. Não conhece doença renal, retinopatia ou '
         'perda de sensibilidade nos pés. Nunca teve acidente vascular '
         'cerebral, crise convulsiva ou dificuldade semelhante para caminhar. '
         'Herniorrafia inguinal há vinte anos.'),
       p('Usa **losartana 50 mg** pela manhã e **metformina 850 mg** duas vezes '
         'ao dia. Durante a doença tomou apenas paracetamol e, nos últimos '
         'dois dias, quase não comeu nem bebeu. Aposentado, mora com a '
         'esposa. Parou de fumar há vinte anos; bebe cerveja ocasionalmente.')),

    q('p3', 3,
      'Diabético em metformina e losartana, febril, dois dias sem comer nem '
      'beber direito. **Quais três** riscos essa combinação impõe agora?', [
      ('Hipoglicemia pela metformina',
       'Metformina sozinha não causa hipoglicemia: não estimula insulina. '
       'É o erro clássico da lista.', False),
      ('Acidose láctica associada à metformina, se houver lesão renal',
       'A droga se acumula quando a filtração cai. Desidratação e sepse '
       'são o cenário em que a suspensão é obrigatória.', True),
      ('Lesão renal aguda pré-renal',
       'Febre, baixa ingestão e bloqueio do receptor de angiotensina: o '
       'rim perde a capacidade de manter a filtração com volume baixo.',
       True),
      ('Cetoacidose euglicêmica',
       'É efeito dos inibidores de SGLT2, que ele não usa.', False),
      ('Hipercalemia',
       'Losartana mais lesão renal aguda mais jejum. Potássio é o primeiro '
       'eletrólito a olhar no ECG e na bancada.', True),
      ('Síndrome serotoninérgica',
       'Nenhuma droga serotoninérgica em uso.', False),
      ('Hiponatremia pela losartana',
       'Não é efeito típico do bloqueador do receptor. Hiponatremia aqui, se '
       'vier, tem outra causa.', False),
     ], 'Metformina não baixa glicose demais; é o rim que ela cobra'),

    pg('exame', 'Exame físico',
       vitais(('PA', '146/84 mmHg', False), ('FC', '102 bpm', True),
              ('FR', '20 irpm', False), ('Temperatura', '38,7 °C', True),
              ('SpO₂', '96% em ar ambiente', False)),
       topicos(('Estado geral', 'Desperto, responde lentamente e erra o dia '
                'do mês. Mucosas discretamente secas.'),
               ('Cardiopulmonar', 'Ritmo regular, sem sopro; murmúrio '
                'vesicular presente, sem ruídos adventícios.'),
               ('Abdome e pele', 'Abdome indolor. Sem lesão cutânea ou '
                'edema.'),
               ('Neurológico', 'Sem rigidez de nuca evidente. Face simétrica '
                'e fala compreensível. Eleva os quatro membros contra a '
                'gravidade no leito, mas não se mantém em pé sem auxílio. '
                'Exame motor detalhado será repetido após analgesia.'))),

    q('p4', 4,
      'Sem rigidez de nuca evidente; eleva os quatro membros no leito, mas '
      'não fica em pé; frequência cardíaca de 102 com 38,7 °C. **Quais três** '
      'afirmações estão corretas?', [
      ('A ausência de rigidez de nuca não exclui meningite no idoso',
       'Em adultos com meningite, a rigidez de nuca tem sensibilidade em '
       'torno de 30%; Kernig e Brudzinski, de 5%. No idoso é ainda menor. '
       'Sinal meníngeo negativo não dispensa a punção.', True),
      ('Kernig e Brudzinski negativos tornam a punção lombar dispensável',
       'É o contrário: são específicos e pouco sensíveis. Servem quando '
       'presentes, não quando ausentes.', False),
      ('Elevar os quatro membros contra a gravidade não exclui paresia',
       'Força grau 3 é "vence a gravidade". Ele pode ter grau 3 na perna '
       'direita e grau 5 na esquerda e "elevar os quatro". É preciso '
       'graduar contra resistência, lado a lado.', True),
      ('A fala compreensível exclui encefalite',
       'Encefalite se apresenta com confusão, sonolência e crise — a '
       'afasia é achado de lesão focal, não requisito.', False),
      ('Não ficar em pé pode ser paresia, ataxia ou desatenção — o exame '
       'precisa separar',
       'Três mecanismos, três exames: força segmentar, prova '
       'índex-nariz e marcha, e o teste de atenção. A queixa é uma; a '
       'lesão, não necessariamente.', True),
      ('A frequência de 102 com 38,7 °C caracteriza dissociação '
       'pulso-temperatura',
       'Seria o sinal de Faget se o pulso estivesse **baixo** para a '
       'febre — febre tifoide, brucelose, legionelose. 102 para 38,7 é '
       'proporcional.', False),
     ], 'Sinal meníngeo negativo não é exame normal'),

    *ecg('ecg_evolucao',
         'Durante a observação, Antônio mantém febre e o pulso fica mais '
         'acelerado. A equipe registra um ECG. O ritmo ajuda a explicar a '
         'dificuldade para caminhar ou exige uma investigação em paralelo?',
         IMG,
         'A taquicardia pode acompanhar a febre e o estresse sistêmico. Isso '
         'não explica por si só o déficit motor e a alteração da atenção; a '
         'investigação neurológica continua.'),

    pedido('ex1', 'Exames · primeira rodada', 'Primeira rodada',
      'Febre, cefaleia e perda recente da autonomia com alteração cognitiva. '
      'Quatro exames para causas tratáveis e gravidade.', [
      grupo('Sangue', 'sangue', [
        ex('Hemograma', 'Hb 13,2 g/dL · leucócitos 10.900/mm³ · plaquetas 181.000/mm³',
           'Hb 13–17 · leucócitos 4.000–11.000 · plaquetas 150.000–450.000'),
        ex('Glicemia', '132 mg/dL', '70–140 (valor casual adotado no caso)'),
        ex('Eletrólitos e função renal', 'Na 131 mmol/L · K 4,1 mmol/L · creatinina 1,1 mg/dL',
           'Na 135–145 · K 3,5–5,0 · Cr 0,7–1,3', True),
        ex('Creatinoquinase', '124 U/L', '40–200'),
        ex('Transaminases', 'AST 39 U/L · ALT 35 U/L', 'Até 40'),
        ex('Proteína C reativa', '42 mg/L', 'Menor que 5', True)]),
      grupo('Avaliação complementar', 'geral', [
        ex('Urina tipo 1', '0–2 leucócitos/campo · nitrito negativo · sem sangue'),
        ex('Radiografia de tórax', 'Sem opacidade focal ou derrame pleural.'),
        ex('Hemoculturas iniciais', 'Coletadas; em processamento nesta etapa.'),
        ex('TSH', '2,4 mUI/L', '0,4–4,0'),
        ex('Vitamina B12', '410 pg/mL', '200–900')])],
      banco=BANCO, limite=4, fundo=CENA),

    resultados('res1', 'Resultados', 'Primeira rodada', 'ex1', fundo=CENA,
      laminas={'Radiografia de tórax': lamina('rx_torax_normal.jpg',
               'Radiografia de tórax',
               'Imagem comparativa de outro adulto. Ausência de opacidade '
               'focal evidente não exclui infecção precoce.',
               'Mikael Häggström · Wikimedia Commons · CC0. Imagem ilustrativa.')}),

    pg('bancada', 'Pronto atendimento',
       p('A bancada da chegada, que a equipe colheu de qualquer modo, voltou: '
         '**sódio 131 mmol/L**, potássio 4,1, creatinina 1,1 mg/dL, glicemia '
         '132 mg/dL, proteína C reativa 42 mg/L. Mucosas secas ao exame; '
         'sem edema; pressão arterial 146/84.'),
       p('A esposa conta que ele bebeu pouco nos últimos dois dias e que "o '
         'suor da febre molhava a cama".')),

    q('p5', 5,
      'Sódio de 131 mmol/L com glicemia de 132, mucosas secas, febre de '
      'quatro dias e doença do sistema nervoso em investigação. **Quais '
      'três** causas devem ser consideradas?', [
      ('Secreção inapropriada de hormônio antidiurético',
       'Qualquer doença do sistema nervoso central — meningite, encefalite, '
       'AVC — dispara ADH. É a causa mais comum de hiponatremia neste '
       'contexto, e exige sódio urinário e osmolalidade para se afirmar.',
       True),
      ('Hiponatremia translocacional por hiperglicemia',
       'Cada 100 mg/dL de glicose acima de 100 baixa o sódio 1,6 a 2,4 '
       'mEq/L. Com 132 de glicemia, a correção é de meio ponto. Não é '
       'isso.', False),
      ('Depleção de volume',
       'Sudorese, febre e dois dias sem beber, com mucosas secas. '
       'Hiponatremia hipovolêmica é a hipótese que a esposa acabou de '
       'sustentar — e a que muda a conduta: soro, não restrição.', True),
      ('Polidipsia primária',
       'Ele bebeu **menos**, não mais.', False),
      ('Insuficiência adrenal',
       'Hiponatremia com febre, hipotensão relativa e fraqueza num idoso: '
       'o cortisol da manhã custa pouco e a hipótese mata quando '
       'esquecida.', True),
      ('Efeito da losartana',
       'Bloqueador do receptor de angiotensina não produz hiponatremia '
       'clinicamente relevante. Tiazídico produziria — ele não usa.',
       False),
      ('Efeito da metformina',
       'Não altera o sódio.', False),
     ], 'Cérebro que segura água, corpo que perdeu água, adrenal que não responde'),

    pg('reexame', 'Reavaliação',
       p('Depois de analgesia e hidratação cautelosa, continua desorientado. '
         '**A perna direita não vence a gravidade; a esquerda vence '
         'resistência leve.** O braço direito está discretamente mais fraco '
         'que o esquerdo. A sensibilidade ao toque e à picada permanece '
         'simétrica.'),
       p('Os reflexos patelar e aquileu direitos estão **abolidos**; à '
         'esquerda, diminuídos. Não há nível sensitivo. Sem sinal de '
         'Babinski. Surge rigidez de nuca discreta. Tremor de ação nas '
         'mãos.')),

    q('p6', 6,
      'Paresia flácida assimétrica, arreflexia do lado mais fraco, '
      'sensibilidade preservada, sem nível sensitivo, sem Babinski. '
      '**Onde está a lesão?**', [
      ('Corno anterior da medula espinal',
       'Neurônio motor inferior, com sensibilidade poupada e assimetria: '
       'é a topografia da poliomielite — e dos vírus que a imitam. '
       'Flacidez, arreflexia e atrofia em semanas.', True),
      ('Raiz e nervo periférico, com desmielinização',
       'Guillain-Barré é simétrico e ascendente, com parestesias e '
       'dissociação no líquor. Assimetria tão marcada e febre em curso '
       'falam contra.', False),
      ('Cápsula interna',
       'Lesão de neurônio motor superior: hemiparesia com hiperreflexia e '
       'Babinski depois do choque inicial. Os reflexos dele estão '
       'abolidos, não exaltados.', False),
      ('Junção neuromuscular',
       'Miastenia e botulismo poupam reflexos e sensibilidade, e são '
       'simétricos. Arreflexia não é deles.', False),
      ('Medula transversa, na altura torácica',
       'Exigiria nível sensitivo e disfunção esfincteriana, com '
       'paraparesia simétrica. Não há nível.', False),
     ], 'Flácido, arreflexo, assimétrico, sensível: corno anterior'),

    q('p7', 7,
      'Paralisia flácida aguda assimétrica, com febre e rigidez de nuca. '
      '**Quais quatro** causas produzem esse quadro?', [
      ('Vírus do Nilo Ocidental',
       'A síndrome tipo poliomielite: mielite de corno anterior, '
       'assimétrica, em idoso, com encefalite junto. É a causa mais '
       'frequente de paralisia flácida arboviral nas Américas.', True),
      ('Enterovírus D68 e A71, e poliovírus',
       'Os enterovírus neurotrópicos fazem mielite flácida aguda com '
       'pródromo febril. O poliovírus segue circulando onde a vacinação '
       'falhou.', True),
      ('Botulismo',
       'Descendente, simétrico, com pupilas fixas e ptose, sem febre e com '
       'líquor normal. Não é este.', False),
      ('Raiva paralítica',
       'Um quinto a um terço das raivas humanas é "muda": paralisia flácida '
       'ascendente com febre, sem hidrofobia. Mordida de morcego passa '
       'despercebida. Pergunte.', True),
      ('Miastenia gravis',
       'Fatigável, sem febre, com reflexos e sensibilidade normais.',
       False),
      ('Guillain-Barré, variante axonal motora',
       'A variante AMAN pode ser assimétrica e rápida, e vem depois de '
       'diarreia por //Campylobacter//. Entra na lista, e o líquor e a '
       'eletroneuromiografia a separam.', True),
      ('Paralisia periódica hipocalêmica',
       'Simétrica, proximal, sem febre e sem meningismo, com potássio '
       'baixo. O dele é 4,1.', False),
      ('AVC de tronco encefálico',
       'Neurônio motor superior: hiperreflexia, Babinski, sinais de '
       'nervo craniano. Não faz flacidez com arreflexia.', False),
      ('Esclerose lateral amiotrófica',
       'Meses a anos, sem febre, com sinais de neurônio motor superior e '
       'inferior somados.', False),
     ], 'Poliomielite tem imitadores, e três deles são vírus'),

    pg('imagem_localizacao', 'Discussão de imagem',
       p('Observe o corte transversal da medula. Que estruturas você '
         'relacionaria à força, à sensibilidade e aos reflexos? Localize-as '
         'antes de abrir a discussão.'),
       '<details class="leitura"><summary>Revelar pontos de discussão</summary>'
       '<p>Os cornos anteriores abrigam corpos celulares motores; as raízes '
       'ventrais levam axônios motores para a periferia. O comprometimento '
       'dessas estruturas produz fraqueza e hiporreflexia sem o padrão '
       'sensitivo de uma lesão medular transversa. O esquema não identifica '
       'a etiologia.</p></details>',
       lamina_=lamina('medula.svg', 'Medula espinal',
                      'Esquema anatômico comparativo; não é exame do paciente. '
                      'Rótulos originais em inglês.',
                      'Polarlys · Wikimedia Commons · CC BY 2.5 · sem alterações.')),

    bifurcacao('b1', 'Decisão', 'Conduta inicial',
      'Qual caminho você escolhe diante da reavaliação?', [
      caminho('Internar, colher amostras e iniciar cobertura empírica para '
              'meningoencefalite.', 'r_interna',
              'A coleta é importante, mas não deve atrasar antimicrobianos '
              'quando a suspeita é relevante.'),
      caminho('Conduzir como polirradiculoneuropatia e priorizar '
              'imunoglobulina.', 'r_ig',
              'Guillain-Barré é um diferencial, mas febre ativa e '
              'encefalopatia tornam insuficiente essa hipótese isolada.'),
      caminho('Manter observação com hidratação antes de ampliar a '
              'investigação.', 'r_observa',
              'A observação sem investigação dirigida pode retardar o '
              'reconhecimento da progressão neurológica.')], fundo=CENA),

    pg('r_interna', 'Primeiro dia',
       p('Antônio é internado em leito monitorizado. São iniciados aciclovir '
         'e cobertura para meningite bacteriana, incluindo //Listeria// pela '
         'idade, com ajuste à função renal. A coleta de amostras e a '
         'avaliação de segurança da punção são organizadas sem atrasar o '
         'tratamento. A esposa fica para complementar a história.'),
       segue='reavaliacao_internacao'),
    pg('r_ig', 'Primeiro dia',
       p('A imunoglobulina é iniciada sob a hipótese de '
         'polirradiculoneuropatia. Ele mantém febre e confusão e o tremor de '
         'ação piora. Na revisão conjunta, a equipe amplia a abordagem para '
         'meningoencefalite e inicia cobertura empírica, doze horas depois '
         'do que poderia.'),
       segue='reavaliacao_internacao'),
    pg('r_observa', 'Primeiro dia',
       p('Durante a observação, a perna direita passa a apresentar apenas '
         'contração, sem movimento, e ele fica mais sonolento. É transferido '
         'para leito monitorizado, e a equipe inicia a abordagem empírica de '
         'meningoencefalite com um dia de atraso.'),
       segue='reavaliacao_internacao'),

    pg('reavaliacao_internacao', 'Reavaliação na internação',
       p('Na transferência para o leito, precisa de duas pessoas para se '
         'acomodar. Ao tentar ajustar o lençol, usa mais a mão esquerda. '
         'Mantém sensibilidade ao toque e responde quando chamado, mas '
         'alterna períodos de conversa com sonolência.'),
       p('A cefaleia permanece. A equipe revê a evolução da consciência e o '
         'déficit focal antes de definir a segurança da punção e a '
         'necessidade de imagem prévia.'),
       segue='tc_evolucao'),

    *sequencia('tc_evolucao', 'Tomografia de crânio',
        'Diante do déficit focal e da alteração da consciência, a equipe '
        'solicita TC de crânio antes de definir a segurança da punção. O '
        'tratamento empírico é mantido enquanto o exame é realizado.',
        IMG / 'tc_cranio.png',
        'Mikael Häggström · Wikimedia Commons · CC0. Setas adicionadas na '
        'discussão.',
        'Corte axial e localizador de outro adulto. Figura ilustrativa; não '
        'substitui a leitura do exame completo.',
        [((250, 400), (35, 340)), ((282, 210), (400, 100))],
        ['1. Os espaços liquóricos ventriculares aparecem escuros neste '
         'corte; não há dilatação grosseira evidente na figura.',
         '2. A fissura inter-hemisférica anterior oferece uma referência da '
         'linha média. Não se observa desvio grosseiro neste nível.',
         'O laudo ficcional do estudo completo não mostra hemorragia, '
         'hidrocefalia ou efeito de massa. Isso não exclui encefalite ou '
         'isquemia precoce.']),

    pedido('ex2', 'Exames · segunda rodada', 'Segunda rodada',
      'Paresia assimétrica com febre e confusão. Quatro investigações para '
      'distinguir os mecanismos.', [
      grupo('Sistema nervoso', 'nervo', [
        ex('Líquor: celularidade, proteína, glicose e Gram',
           '86 células/mm³ (58% neutrófilos) · proteína 92 mg/dL · glicose 68 '
           'mg/dL, sérica 120 · Gram sem bactérias',
           'Até 5 células · proteína 15–45 · relação glicose >0,4', True),
        ex('Cultura e PCR bacteriana do líquor',
           'Sem crescimento até o momento · painel bacteriano negativo.'),
        ex('PCR para HSV e VZV no líquor',
           'Não detectados em amostra obtida no sexto dia de sintomas.'),
        ex('Ressonância de encéfalo e medula',
           'Sem infarto, compressão medular ou lesão temporal. Ausência de '
           'alteração específica não exclui inflamação.'),
        ex('Eletroneuromiografia',
           'Respostas motoras reduzidas, assimétricas; respostas sensitivas '
           'preservadas. Sem critérios de desmielinização.', '—', True),
        ex('Eletroencefalograma',
           'Lentificação difusa, sem atividade epiléptica registrada.')]),
      grupo('Outras hipóteses', 'geral', [
        ex('HIV Ag/Ac', 'Não reagente.'),
        ex('Sífilis: teste treponêmico e VDRL', 'Não reagentes.'),
        ex('Dengue: NS1 e IgM', 'Não reagentes.'),
        ex('Leptospira: PCR', 'Não detectado.'),
        ex('Amônia', '28 µmol/L', '11–35'),
        ex('Cortisol matinal', '18 µg/dL', '5–25')])],
      banco=BANCO, limite=4, fundo=CENA),

    resultados('res2', 'Resultados', 'Segunda rodada', 'ex2', fundo=CENA,
      laminas={'Ressonância de encéfalo e medula': lamina('rm_encefalo.png',
               'RM do encéfalo',
               'A figura ilustra somente um corte axial T2 do encéfalo de '
               'outro adulto. Não mostra a medula nem todas as sequências do '
               'estudo.',
               'Sean Novak · Wikimedia Commons · CC BY-SA 4.0 · sem alterações.')},
      rota={'pediu': ['Líquor: celularidade, proteína, glicose e Gram'],
            'entao': 'p8', 'senao': 'sem_lcr'}),

    pareamento('p8', 'Pergunta 8',
      'O líquor dele: 86 células, 58% neutrófilos, proteína 92, glicose '
      '68 com sérica 120. Associe cada perfil de líquor ao diagnóstico que '
      'ele sugere.', [
      par('86 células, 58% neutrófilos, proteína 92, glicose 68/120, Gram '
          'negativo — o dele',
          'Meningoencefalite viral em fase inicial',
          'Pleocitose modesta, glicose preservada e Gram negativo. O '
          'predomínio neutrofílico engana: até metade das infecções pelo '
          'Nilo Ocidental começa assim, e vira linfocitário em dias.'),
      par('2.400 células, 95% neutrófilos, proteína 240, glicose 20/110',
          'Meningite bacteriana',
          'Milhares de neutrófilos, proteína alta e glicose consumida — '
          'relação abaixo de 0,4. Antibiótico já deveria estar correndo.'),
      par('180 células, 90% linfócitos, proteína 110, glicose 35/100, ADA '
          'elevada',
          'Meningite tuberculosa',
          'Linfocitário, proteína alta e **glicose baixa**: é a combinação '
          'que separa tuberculose e fungo dos vírus. ADA reforça.'),
      par('5 células, proteína 180, glicose normal',
          'Dissociação albuminocitológica — Guillain-Barré',
          'Proteína alta sem célula. Leva uma a duas semanas para '
          'aparecer; na primeira semana o líquor pode ser normal.'),
      par('60 células, linfócitos, proteína 80, glicose normal, 300 '
          'hemácias sem punção traumática',
          'Encefalite herpética',
          'Hemácias no líquor sem trauma de agulha: necrose hemorrágica '
          'do lobo temporal. Aciclovir até a PCR negativa em amostra '
          'adequada.'),
      ], opcoes=[
      'Meningoencefalite viral em fase inicial',
      'Meningite bacteriana',
      'Meningite tuberculosa',
      'Dissociação albuminocitológica — Guillain-Barré',
      'Encefalite herpética',
      'Meningite criptocócica',
      ], titulo_resposta='Célula, proteína e glicose — nessa ordem de leitura',
      nota='A opção que sobrou, criptococo, teria poucas células, pressão '
           'de abertura alta e tinta da China positiva.',
      fundo=CENA, segue='historia2'),

    pg('sem_lcr', 'Discussão',
       p('A equipe ainda não dispõe de caracterização do líquor neste '
         'percurso. O diagnóstico permanece sindrômico: doença febril com '
         'alteração do estado mental e paresia flácida assimétrica.'),
       p('As hipóteses infecciosas seguem cobertas empiricamente. A falta de '
         'definição não impede monitorização respiratória ou nova avaliação '
         'neurológica.'),
       segue='historia2'),

    pg('historia2', 'História complementar',
       p('Ao reconstruir o mês anterior com a esposa, a equipe descobre que '
         'voltaram de uma visita a familiares na Louisiana, no sul dos '
         'Estados Unidos, **doze dias antes da febre**. Ele passava o fim de '
         'tarde no quintal, perto de uma área alagada, e os dois tiveram '
         'várias picadas de mosquito. Não houve mordida de animal, contato '
         'com água de enchente ou leite cru. Ela permaneceu bem. Antônio já '
         'teve dengue anos antes.'),
       p('No segundo dia de internação, a tosse fica fraca. Ele engasga com '
         'água, embora mantenha saturação de 96% em ar ambiente. A '
         'capacidade vital caiu de 24 para **17 mL/kg** entre as duas '
         'medidas do dia, e a pressão inspiratória máxima piorou.')),

    q('p9', 9,
      'Doze dias entre as picadas num pântano da Louisiana e a febre. Sobre '
      'a infecção pelo vírus do Nilo Ocidental, **quais três** afirmações '
      'estão corretas?', [
      ('Cerca de 80% das infecções são assintomáticas, e menos de 1% '
       'evolui para doença neuroinvasiva',
       'A maioria nunca sabe que teve. Dos 20% sintomáticos, a doença '
       'febril autolimitada é a regra; a neuroinvasiva é a exceção.', True),
      ('O período de incubação é de quatro a seis semanas',
       'É de 2 a 14 dias. Os doze dias dele cabem exatamente.', False),
      ('Idade acima de 60 anos e imunossupressão são os principais fatores '
       'de risco para a forma neuroinvasiva',
       'O risco de encefalite e de paralisia é várias vezes maior acima dos '
       '60 anos, e a mortalidade da forma neuroinvasiva chega a 10%.', True),
      ('Existe vacina humana licenciada',
       'Só para cavalos. A prevenção humana é o repelente.', False),
      ('A transmissão é por mosquito //Culex//, com aves como reservatório; '
       'o humano é hospedeiro terminal',
       'Ave amplifica, //Culex// transmite. Humano e cavalo não fazem '
       'viremia suficiente para infectar o mosquito — mas transfusão e '
       'transplante transmitem.', True),
      ('A IgM no líquor confirma o diagnóstico sem reação cruzada',
       'Flavivírus reagem entre si: quem teve dengue pode ter IgM '
       'falsamente reagente. A neutralização em laboratório de referência '
       'é o que decide.', False),
      ('Há transmissão por contato direto entre pessoas',
       'Não há. Transfusão, transplante e via transplacentária, sim.',
       False),
     ], 'Dois a catorze dias, um em cem, e nenhuma vacina'),

    q('p10', 10,
      'Capacidade vital de 24 para 17 mL/kg, tosse fraca, engasgo com água, '
      'saturação de 96%. **Quais três** parâmetros indicam proteção '
      'eletiva da via aérea na fraqueza neuromuscular?', [
      ('Capacidade vital abaixo de 20 mL/kg',
       'A regra 20/30/40: capacidade vital abaixo de 20 mL/kg, pressão '
       'inspiratória máxima menos negativa que −30 cmH₂O, pressão '
       'expiratória abaixo de 40. Ele já cruzou a primeira.', True),
      ('Saturação abaixo de 90% em ar ambiente',
       'Sinal **tardio**. Na falência de bomba a saturação cai por último, '
       'quando a hipoventilação já é grave. Esperar por ela é esperar a '
       'parada.', False),
      ('Pressão inspiratória máxima menos negativa que −30 cmH₂O',
       'Mede a força do diafragma diretamente, à beira do leito, com um '
       'manovacuômetro. É o segundo número da regra.', True),
      ('pCO₂ acima de 45 mmHg na gasometria',
       'Também tardio: a hipercapnia aparece quando a reserva acabou. A '
       'gasometria confirma a falência; não a antecipa.', False),
      ('Incapacidade de proteger a via aérea: tosse ineficaz e disfagia',
       'Ele engasga com água e não tosse. Aspiração não espera número de '
       'espirometria.', True),
      ('Frequência respiratória acima de 30',
       'Inespecífica — febre e dor fazem o mesmo. Não decide sozinha.',
       False),
     ], 'Vinte, trinta, quarenta — e a tosse'),

    bifurcacao('b2', 'Decisão', 'Suporte respiratório',
      'Como você conduz essa mudança?', [
      caminho('Transferir para terapia intensiva e proteger a via aérea de '
              'forma planejada.', 'r_via',
              'A progressão bulbar e ventilatória permite antecipar uma via '
              'aérea difícil em vez de esperar o colapso.'),
      caminho('Tentar ventilação não invasiva com vigilância intensiva.',
              'r_vni',
              'Uma tentativa exige seleção e critérios precoces de falha; '
              'disfagia e secreções reduzem a margem de segurança.'),
      caminho('Manter oxigênio e vigilância na enfermaria enquanto '
              'investiga.', 'r_atraso',
              'A saturação não mede a reserva ventilatória nem a proteção '
              'contra aspiração.')], fundo=CENA),

    pg('r_via', 'Terceiro dia',
       p('É intubado de forma planejada por progressão da disfunção bulbar e '
         'fraqueza ventilatória. Não há aspiração. A febre começa a ceder, '
         'mas a paresia permanece. Ao reduzir a sedação, reconhece a esposa '
         'e segue comandos; movimenta menos o lado direito. A família '
         'pergunta se a melhora da febre significa que voltará a andar.'),
       segue='visita_dia4'),
    pg('r_vni', 'Reavaliação respiratória',
       p('Com ventilação não invasiva, acumula secreções e não consegue '
         'expectorar. Mantém episódios de engasgo. A oxigenação segue '
         'preservada, mas a proteção da via aérea piora.'),
       segue='b_resgate'),
    pg('r_atraso', 'Reavaliação respiratória',
       p('Na enfermaria, apresenta engasgo seguido de aumento do esforço '
         'respiratório. É levado à sala de emergência. O cenário agora exige '
         'decidir sobre proteção da via aérea e suporte intensivo.'),
       segue='b_resgate'),

    bifurcacao('b_resgate', 'Decisão', 'Reavaliação da conduta',
      'Diante da falha de eliminação de secreções, qual é a próxima conduta?', [
      caminho('Interromper a estratégia inicial e realizar intubação.',
              'r_resgate',
              'A mudança de plano é uma resposta à evolução, não precisa '
              'esperar falência completa.'),
      caminho('Prolongar o suporte não invasivo e reavaliar após a '
              'investigação.', 'f_obito',
              'A incapacidade de proteger a via aérea torna perigoso adiar o '
              'suporte invasivo.')], fundo=CENA),

    pg('r_resgate', 'Quarto dia',
       p('Após intubação de resgate, necessita de suporte ventilatório '
         'prolongado. Quando desperto, tenta comunicar-se por gestos e '
         'demonstra frustração por não conseguir elevar a perna direita. O '
         'episódio de aspiração motiva investigação e tratamento de '
         'pneumonia. A fraqueza assimétrica continua presente quando a '
         'sedação é reduzida.'),
       segue='visita_dia4'),

    pg('visita_dia4', 'Quarto dia',
       p('Quando a sedação é reduzida, acompanha a esposa com o olhar e '
         'responde por gestos. Consegue apertar a mão dela, mas não eleva a '
         'perna direita do leito. A família percebe que ele está mais '
         'presente na conversa, embora o movimento não tenha melhorado na '
         'mesma proporção.'),
       p('A equipe organiza a cronologia com os familiares: início da febre, '
         'a dificuldade para caminhar, a mudança do comportamento e a piora '
         'da tosse.'),
       segue='ex3'),

    pedido('ex3', 'Exames · terceira rodada', 'Terceira rodada',
      'Com a exposição esclarecida e a evolução neurológica, quatro exames '
      'para a etiologia e para as hipóteses concorrentes.', [
      grupo('Agentes e exposição', 'geral', [
        ex('IgM para vírus do Nilo Ocidental em soro e líquor',
           'Reagente nas duas amostras; resultado presuntivo, sujeito a '
           'reação cruzada.', 'Não reagente', True),
        ex('PCR para enterovírus no líquor', 'Não detectado.'),
        ex('Sorologia para encefalite de Saint Louis', 'IgM não reagente.'),
        ex('Chikungunya: IgM', 'Não reagente.'),
        ex('Pesquisa de malária', 'Gota espessa sem parasitas.'),
        ex('Pesquisa de vírus rábico em laboratório de referência',
           'Não detectado nas amostras do protocolo; interpretar com '
           'história de exposição.')]),
      grupo('Mecanismos alternativos', 'nervo', [
        ex('Anticorpos anti-GM1',
           'Não reagentes; resultado negativo não exclui neuropatia imune.'),
        ex('Anticorpos de encefalite autoimune',
           'Painel sem reatividade.'),
        ex('Porfobilinogênio urinário', 'Dentro do intervalo do método.'),
        ex('Nova eletroneuromiografia',
           'Denervação ativa assimétrica, respostas motoras reduzidas e '
           'sensitivas preservadas; sem desmielinização.', '—', True),
        ex('Nova PCR para HSV no líquor', 'Não detectado.'),
        ex('Cobre sérico', '102 µg/dL', '70–140')])],
      banco=BANCO, limite=4, fundo=CENA),

    resultados('res3', 'Resultados', 'Terceira rodada', 'ex3', fundo=CENA,
      rota={'pediu': ['IgM para vírus do Nilo Ocidental em soro e líquor'],
            'entao': 'p11', 'senao': 'indefinido'}),

    q('p11', 11,
      'A IgM reagente para Nilo Ocidental combina com o contexto, mas ele já '
      'teve dengue. Qual é a melhor forma de consolidar a atribuição '
      'etiológica?', [
      ('Interpretar qualquer IgM como confirmação definitiva',
       'Anticorpos contra flavivírus reagem entre si. Dengue prévia é a '
       'situação em que o falso reagente é mais provável.', False),
      ('Excluir a hipótese se a PCR sérica for negativa',
       'A viremia é curta e já passou quando a doença neurológica aparece. '
       'PCR negativa não exclui.', False),
      ('Substituir a IgM por uma IgG isolada',
       'IgG isolada pode ser da dengue de anos atrás.', False),
      ('Solicitar teste de neutralização por redução de placas em '
       'laboratório de referência',
       'O PRNT distingue o flavivírus responsável pela reatividade, e '
       'amostras pareadas mostram a soroconversão. É o que fecha.', True),
      ('Exigir biópsia cerebral antes de aceitar etiologia viral',
       'Não é investigação deste cenário.', False),
     ], 'Flavivírus cruzam; a neutralização separa', segue='b3'),

    bifurcacao('b3', 'Decisão', 'Definição etiológica',
      'Como você prossegue com a sorologia?', [
      caminho('Enviar confirmação por neutralização e manter suporte.',
              'confirmado',
              'A confirmação resolve uma limitação do método sem interromper '
              'o cuidado.'),
      caminho('Manter a classificação presuntiva e seguimento clínico.',
              'provavel',
              'É possível manejar a síndrome sem afirmar uma confirmação que '
              'não foi obtida.')], fundo=CENA),

    pg('confirmado', 'Resultado complementar',
       p('O laboratório de referência informa neutralização compatível com '
         'vírus do Nilo Ocidental, sem padrão cruzado que explique o '
         'resultado. A investigação sustenta doença neuroinvasiva com '
         'comprometimento motor.'),
       segue='p12'),
    pg('provavel', 'Avaliação etiológica',
       p('A associação clínica e sorológica sustenta doença neuroinvasiva '
         'provavelmente pelo vírus do Nilo Ocidental. Sem a confirmação '
         'complementar, permanece registrada a limitação de reação cruzada.'),
       segue='p12'),
    pg('indefinido', 'Avaliação etiológica',
       p('Neste percurso, a etiologia não foi estabelecida. A documentação '
         'permanece como meningoencefalite com paresia flácida assimétrica. '
         'O seguimento em neurologia e infectologia inclui reavaliar amostras '
         'e exposição, sem registrar um agente confirmado.'),
       segue='p12'),

    q('p12', 12,
      'Sexto dia de internação. Sobre o tratamento da doença neuroinvasiva '
      'pelo vírus do Nilo Ocidental, **quais três** afirmações estão '
      'corretas?', [
      ('Não há antiviral com benefício demonstrado',
       'Ribavirina e interferon foram testados sem sucesso. O tratamento '
       'é suporte.', True),
      ('Imunoglobulina endovenosa tem benefício comprovado',
       'O único ensaio randomizado — com imunoglobulina rica em anticorpo '
       'contra o vírus — foi inconclusivo. Não é tratamento estabelecido.',
       False),
      ('Suporte ventilatório, prevenção de complicações e reabilitação são '
       'o tratamento ativo',
       'Sem antiviral, o que muda o desfecho é não morrer de aspiração, '
       'trombose ou úlcera — e reabilitar o que sobrou.', True),
      ('Corticoide em altas doses acelera a recuperação motora',
       'Sem evidência; o dano é neuronal, não inflamatório reversível.',
       False),
      ('Os antibacterianos empíricos podem ser suspensos com cultura e PCR '
       'bacteriana do líquor negativas e quadro compatível',
       'Quarenta e oito a setenta e duas horas de cultura negativa, PCR '
       'negativa e evolução compatível: suspende. Manter "por via das '
       'dúvidas" só custa.', True),
      ('O aciclovir deve ser mantido por 14 dias mesmo com PCR para HSV '
       'negativa',
       'PCR negativa em amostra colhida depois do terceiro dia de sintomas '
       'autoriza suspender. Nos três primeiros dias pode ser falso '
       'negativo — a dele foi no sexto.', False),
     ], 'Sem antiviral, o tratamento é não perder o que sobrou'),

    q('p13', 13,
      'A família pergunta se ele voltará a andar. Sobre o prognóstico da '
      'paralisia flácida pelo vírus do Nilo Ocidental, **quais três** '
      'afirmações estão corretas?', [
      ('A recuperação motora costuma ser incompleta',
       'Lesão de corno anterior é perda neuronal, como na poliomielite. '
       'Metade recupera parcialmente; a força total volta em poucos.',
       True),
      ('A maioria recupera completamente em semanas',
       'É o curso da doença febril sem acometimento neurológico — não da '
       'mielite.', False),
      ('A mortalidade da forma neuroinvasiva fica em torno de 10%, maior '
       'na paralisia com insuficiência respiratória',
       'Quem precisa de ventilação mecânica morre mais e fica mais tempo. '
       'Idade avançada e imunossupressão pesam.', True),
      ('Fadiga e sintomas cognitivos podem persistir por meses',
       'Mesmo quem recupera a força relata fadiga, dificuldade de '
       'concentração e depressão por meses a um ano.', True),
      ('Recidiva é frequente',
       'Não há recidiva. A imunidade após a infecção é duradoura.',
       False),
      ('A imunidade não é duradoura, e reinfecção é comum',
       'É o contrário: infecção prévia protege por toda a vida.', False),
     ], 'O que o corno anterior perde, ele não devolve'),

    pg('tratamento', 'Tratamento e seguimento',
       p('O suporte inclui ventilação conforme necessidade, manejo de '
         'secreções, nutrição por via segura, prevenção de trombose e lesão '
         'por pressão e mobilização progressiva. Os antibacterianos '
         'empíricos são suspensos com cultura e PCR negativas; o aciclovir, '
         'com a PCR do sexto dia.'),
       p('Neurologia, fisioterapia e fonoaudiologia acompanham recuperação e '
         'limitações. A esposa nota que ele se cansa com visitas longas; são '
         'combinados períodos de descanso e participação gradual nos '
         'cuidados.'),
       segue='imagem_neuronio'),

    pg('imagem_neuronio', 'Discussão de imagem',
       p('Compare o corpo celular, o axônio e a bainha de mielina. Por que '
         'quadros com fraqueza semelhante podem ter tempos de recuperação '
         'diferentes?'),
       '<details class="leitura"><summary>Revelar pontos de discussão</summary>'
       '<p>Bloqueio de condução, perda de mielina e destruição do neurônio '
       'não são equivalentes. A desmielinização do Guillain-Barré se refaz '
       'em semanas; o corpo celular destruído pelo vírus, não. É por isso '
       'que a topografia da lesão — corno anterior — já continha o '
       'prognóstico.</p></details>',
       lamina_=lamina('neuronio.svg', 'Neurônio',
                      'Diagrama anatômico, sem achados específicos deste caso.',
                      'LadyofHats · Wikimedia Commons · domínio público · sem '
                      'alterações.'),
       conforme=('b2', ['pre_reabilitacao', 'pre_prolongada', 'pre_prolongada'])),

    pg('pre_reabilitacao', 'Terceira semana',
       p('Com a redução do suporte, Antônio volta a conversar sobre a casa e '
         'pergunta pelo neto. Senta-se na borda do leito com assistência. Ao '
         'tentar ficar em pé, a perna direita não sustenta o peso.'),
       p('A família recebe orientação sobre transferências e prevenção de '
         'quedas. A alta será articulada com um serviço capaz de continuar a '
         'reabilitação.'),
       segue='f_reabilita'),
    pg('pre_prolongada', 'Internação prolongada',
       p('A retirada do suporte progride mais lentamente. Antônio compreende '
         'as orientações nos períodos de vigília, mas precisa de ajuda para '
         'se posicionar e eliminar secreções. A pneumonia aspirativa custou '
         'dez dias de antibiótico e uma traqueostomia.'),
       p('A equipe conversa com a família sobre transferência para cuidados '
         'de continuidade.'),
       segue='f_longa'),

    fim('f_reabilita', 'Reabilitação',
        'Na terceira semana está desperto, sem suporte invasivo e com '
        'deglutição em recuperação. Continua sem caminhar sozinho. Segue '
        'para reabilitação; aos três meses usa auxílio para marcha e mantém '
        'fraqueza maior à direita.',
        'O suporte antecipado evitou a aspiração e a pneumonia, mas não '
        'devolve o neurônio motor. Este é um desfecho ficcional possível.',
        'melhor'),
    fim('f_longa', 'Internação prolongada',
        'A complicação respiratória prolonga a internação. Necessita de '
        'suporte ventilatório e reabilitação por mais tempo. Na '
        'transferência, mantém dependência para mobilidade e alimentação por '
        'via alternativa.',
        'Aspiração e falência ventilatória somaram morbidade à lesão '
        'neurológica. A duração e a recuperação deste roteiro não são '
        'previsões individuais.'),
    fim('f_obito', 'Evolução desfavorável',
        'A manutenção da estratégia apesar da piora bulbar é seguida, neste '
        'ramo simulado, de aspiração maciça e parada hipóxica. O paciente '
        'não sobrevive. A causa infecciosa não chegou a ser definida neste '
        'percurso.',
        'Este ramo ilustra o risco do atraso na proteção da via aérea quando '
        'a saturação ainda está normal — não uma consequência inevitável.',
        'pior'),

    pg('retrospectiva', 'Retrospectiva',
       tabela(['Quando', 'O que estava à mão', 'O que decidiu'], [
         ['Na chegada',
          'Uma perna que cedeu, num homem febril e confuso',
          'Prostração não é déficit focal. Graduar força lado a lado foi o '
          'que transformou "fraqueza" em corno anterior'],
         ['No reexame',
          'Flácido, arreflexo, assimétrico, com sensibilidade poupada',
          'A topografia já continha o prognóstico: neurônio destruído não '
          'volta'],
         ['No segundo dia',
          'Capacidade vital de 17 mL/kg com saturação de 96%',
          'A saturação é o último número a cair. Quem esperou por ela '
          'aspirou'],
         ['Na história complementar',
          'Doze dias entre um pântano e a febre',
          'A pergunta de viagem, feita no primeiro dia, teria posto o vírus '
          'na lista antes do líquor'],
       ]),
       p('O diagnóstico etiológico e o suporte respiratório correram em '
         'paralelo: é possível proteger o paciente antes de saber o nome do '
         'agente, e é possível nomear o agente sem recuperar a força.')),

    pg('fontes', 'Procedência e referências',
       p('Paciente, valores e evoluções são autorais e ficcionais. A cena é '
         'uma ilustração gerada por IA. Os diferentes finais não estimam o '
         'efeito causal ou a probabilidade de cada conduta.'),
       '<p><a href="https://www.cdc.gov/west-nile-virus/hcp/diagnosis-testing/index.html" '
       'target="_blank" rel="noopener">CDC — diagnóstico</a> · '
       '<a href="https://www.cdc.gov/west-nile-virus/hcp/treatment-prevention/index.html" '
       'target="_blank" rel="noopener">CDC — tratamento</a> · '
       '<a href="https://wwwnc.cdc.gov/eid/article/9/7/03-0129_article" '
       'target="_blank" rel="noopener">Sejvar et al., 2003 — paralisia flácida</a> · '
       '<a href="https://www.idsociety.org/practice-guideline/encephalitis" '
       'target="_blank" rel="noopener">IDSA — encefalite</a></p>',
       p('Regra 20/30/40 e sinais meníngeos no idoso: Lawn e Wijdicks, //Arch '
         'Neurol// 2001; Thomas e cols., //Clin Infect Dis// 2002. '
         'Imunoglobulina: Gnann e cols., //Clin Infect Dis// 2019.')),
]

REVISAO = [
    dict(chave='Líquor: celularidade, proteína, glicose e Gram',
         rotulo='Caracterização do líquor',
         porque='Sem o líquor, a diferença entre infecção e pós-infecção '
                'ficou sem árbitro — e a suspensão dos antibióticos, sem '
                'lastro.'),
    dict(chave='IgM para vírus do Nilo Ocidental em soro e líquor',
         rotulo='Atribuição etiológica',
         porque='A hipótese epidemiológica pede o teste dirigido; sem ele, o '
                'registro deve preservar a incerteza.'),
]

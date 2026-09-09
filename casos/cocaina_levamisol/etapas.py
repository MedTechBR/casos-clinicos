"""Caso ficcional; API de motor.etapas, sem alterar motor ou biblioteca.

Três momentos diagnósticos; painéis selecionáveis e exames trazidos pela equipe.
Os desfechos são cenários possíveis, não probabilidades nem punições causais.
A única imagem futura é ilustrativa e nunca constitui evidência clínica.
"""
from pathlib import Path
from motor.desenhos import chave_corpusculo
from motor.etapas import (
    alt, bifurcacao, caminho, capa, desfecho, grupo, lamina, op, p,
    pagina, pedido, pergunta, quadro, resultados, vitais, topicos,
)

TITULO = 'À flor da pele'
RODAPE = 'Caso ficcional · ensino para internos e residentes'
IMG = Path(__file__).parent / 'img'
BANCO = []
# Sem placeholder: o build funciona hoje e incorpora a cena no próximo build.
CENA_ARQUIVO = 'cena.png'
CENA = CENA_ARQUIVO if (IMG / CENA_ARQUIVO).is_file() else ''
CENA_HISTORIA = (lamina(CENA, 'Cena ilustrativa',
    'Pessoa ficcional em atendimento. Não interpretar a cena como fotografia de lesão.',
    'Ilustração gerada por IA para paciente ficcional; não documenta lesões.') if CENA else None)


def painel(ident, momento, titulo, grupos):
    return pedido(ident, momento, titulo,
        {
            'p1': 'Diante da febre e das placas dolorosas não branqueáveis, quais exames você pede agora para avaliar o risco sistêmico e os mecanismos da púrpura?',
            'p2': 'Com a mudança das placas e o aparecimento de urina escura, quais exames você pede para distinguir o mecanismo cutâneo e investigar possível acometimento de outro órgão?',
            'p3': 'Após o relato de exposição e com a queixa urinária persistente, quais exames você prioriza para esclarecer a associação e orientar a próxima decisão de tratamento?',
        }[ident],
        grupos, fundo=CENA, banco=BANCO, limite=4)


def questao(ident, enunciado, opcoes, titulo):
    return pergunta(ident, 'Pergunta '+ident[1:], enunciado,
        [alt(t, j, certa=c) for t, j, c in opcoes],
        fundo=CENA, titulo_resposta=titulo)


ETAPAS = [
    capa(TITULO, fundo=CENA,
         procedencia='Roteiro autoral; fontes e limites no fecho.'),
    pagina('historia', 'Admissão', 'Apresentação',
        p('Marina, 34 anos, procura atendimento acompanhada da irmã por manchas dolorosas nas coxas e febre. Trabalha em uma loja de roupas e, nos últimos dois dias, deixou de cumprir o turno porque o tecido da calça incomodava ao tocar a pele. Está preocupada com uma área que escureceu naquela manhã.'),
        p('Diz que nunca teve uma lesão “desse tamanho”. Não refere falta de ar, dor torácica ou sangramento aparente. Está lúcida, conversa sem dificuldade e relata a sequência dos sintomas.'),
        fundo=CENA, lamina_=CENA_HISTORIA),
    pagina('hda', 'Antes da admissão', 'História da doença atual',
        p('Três dias antes, notou duas áreas avermelhadas dolorosas na face externa das coxas. Pensou em atrito da roupa, mas não recordava exercício, queda ou picada naquele local. Nas horas seguintes surgiram outras manchas próximas, de cor mais escura. A dor passou de incômodo ao toque para dor em repouso.'),
        p('Havia também mal-estar e dor nos punhos e tornozelos, sem articulação visivelmente inchada. A febre começou no dia da consulta, com calafrios. Tomou paracetamol depois do início dos sintomas e não usou antibiótico ou pomada antes de procurar atendimento.'),fundo=CENA),
    pagina('hda2', 'Admissão', 'Sintomas associados',
        p('Nega sangramento gengival, epistaxe recente ou aumento do fluxo menstrual. Não percebeu inchaço nas pernas nem mudança na quantidade ou na cor da urina até aquela manhã. Não apresenta tosse, dor abdominal persistente, diarreia ou ardor ao urinar.'),
        p('Perguntada sobre episódios anteriores, recorda manchas pequenas que desapareceram sem consulta alguns meses antes. Não guardou fotografias e não sabe precisar a duração. Não atribui relação entre aquele episódio e o atual.'),fundo=CENA),
    pagina('antecedentes', 'História pessoal', 'Antecedentes',
        p('Não tem diagnóstico de hipertensão, diabetes, doença renal ou doença autoimune. Nunca teve trombose, embolia ou sangramento prolongado após procedimentos. Teve uma gestação a termo, sem perdas gestacionais. Não relata infecções graves recorrentes ou internações recentes.'),
        p('Foi submetida a apendicectomia na adolescência, sem complicações, e nega transfusões. Não conhece alergia medicamentosa. A mãe tem hipotireoidismo; não há história familiar conhecida de trombose em idade jovem ou doença hemorrágica.'),fundo=CENA),
    pagina('medicacoes', 'História pessoal', 'Medicações e hábitos',
        p('Não usa medicação contínua, anticoncepcional hormonal ou imunossupressor. Nega medicamento novo nas semanas anteriores, incluindo antibiótico, anti-inflamatório e fórmula para emagrecimento. O paracetamol foi tomado somente depois do aparecimento das manchas.'),
        p('Mora com a irmã e a filha, trabalha em pé durante boa parte do dia e relata sono irregular. Fuma cerca de cinco cigarros por dia e refere consumo de álcool nos fins de semana. Não houve viagem recente, contato com enchente ou mudança relevante no trabalho. A entrevista inicial foi feita com a irmã presente.'),fundo=CENA),
    pagina('exame', 'Admissão', 'Exame físico',
        vitais(('PA','108/68 mmHg',False),('FC','112 bpm',True),('FR','18 irpm',False),('Temperatura','38,6 °C',True),('SpO₂','98% em ar ambiente',False)),
        topicos(('Estado geral','Lúcida e orientada, com dor nas coxas.'),
                ('Cardiovascular e pulmonar','Ritmo regular, sem sopro. Ausculta pulmonar sem ruídos adventícios.'),
                ('Abdome','Indolor, sem massas ou visceromegalias palpáveis.'),
                ('Pele e membros','Placas violáceas dolorosas nas coxas, não desaparecendo à pressão, algumas com centro escurecido. Pulsos presentes, sem crepitação.'),
                ('Neurológico','Força e sensibilidade preservadas nos quatro membros.')),fundo=CENA),
    pagina('imagem_pele','Discussão visual','Morfologia das lesões',
        p('Observe esta fotografia de outro paciente. Descreva a cor, a distribuição e as diferenças de tamanho. O que é possível afirmar apenas pela imagem?'),
        '<details class="leitura"><summary>Revelar pontos de discussão</summary><p>A fotografia mostra lesões purpúricas. Imagem isolada não permite avaliar palpabilidade ou resposta à digitopressão e não distingue, por si, causa plaquetária, inflamatória ou oclusiva. Esta figura é comparativa; não documenta as placas de Marina.</p></details>',
        fundo=CENA,lamina_=lamina('purpura.jpg','Púrpura: imagem comparativa','Fotografia de outro paciente, utilizada apenas para discutir morfologia.','Hektor · Wikimedia Commons · CC BY-SA 3.0 · sem alterações.')),
    questao('q1', 'Febre acompanha placas dolorosas não branqueáveis, com pulsos distais presentes. Quais duas avaliações melhor distinguem os mecanismos iniciais?', [
        ('Contagem de plaquetas e coagulograma', 'Ajudam a avaliar distúrbios hemostáticos; púrpura não estabelece vasculite.', True),
        ('Angiografia dos grandes vasos como primeiro exame', 'Os pulsos e a distribuição tornam menos prioritária a pesquisa invasiva de oclusão proximal.', False),
        ('Exame da profundidade e velocidade de progressão', 'Dor, necrose e evolução podem exigir avaliação urgente de infecção profunda.', True),
        ('Teste terapêutico com anticoagulação', 'A resposta não substitui a identificação do mecanismo e pode acrescentar risco.', False),
        ('Rastreio de alergia alimentar', 'A morfologia e a evolução não favorecem uma reação alimentar imediata.', False),
    ], 'Discussão'),
    pagina('reavaliacao_inicial', 'Evolução', 'Reavaliação à beira do leito',
        p('Marina continua conversando, mas evita movimentar as pernas por causa da dor. Na nova avaliação, as extremidades estão aquecidas, os pulsos permanecem palpáveis e a sensibilidade distal está preservada. Não há crepitação ou secreção espontânea nas placas.'),
        p('As bordas das lesões são registradas para comparação. A equipe mantém vigilância sobre dor, velocidade de progressão e estado geral enquanto organiza os exames. A irmã permanece ao lado e ajuda a reconstruir a sequência dos sintomas.'), fundo=CENA),
    painel('p1', 'Primeiro momento', 'Investigação inicial', [
        grupo('Sangue', 'sangue', [
            op('Hemograma diferencial', resultado='Leucócitos 900/µL · Neutrófilos absolutos 180/µL · Hemoglobina 12,1 g/dL · Plaquetas 238.000/µL', referencia='Neutrófilos 1.500–7.500/µL', alterado=True),
            op('Hemoculturas iniciais', resultado='Dois conjuntos coletados antes do antibiótico, se isso não o atrasar; incubação em andamento.', referencia='Sem crescimento'),
            op('Coagulograma', resultado='INR 1,0 · TTPa 29 s · Fibrinogênio 410 mg/dL', referencia='INR 0,8–1,2; TTPa 25–35 s; fibrinogênio 200–400 mg/dL'),
            op('Esfregaço periférico', resultado='Sem blastos ou esquizócitos.', referencia='Ausentes'),
        ]),
        grupo('Órgãos e perfusão', 'geral', [
            op('Creatinina inicial', resultado='0,9 mg/dL', referencia='0,6–1,1 mg/dL'),
            op('Urina inicial', resultado='0–2 hemácias/campo · Sem cilindros · Proteína negativa', referencia='0–3 hemácias/campo; sem cilindros patológicos'),
            op('Lactato', resultado='1,7 mmol/L', referencia='0,5–2,0 mmol/L'),
        ]),
        grupo('Outras hipóteses', 'pele', [
            op('Proteína C reativa', resultado='96 mg/L', referencia='<5 mg/L', alterado=True),
            op('Doppler arterial de pernas', resultado='Fluxos arteriais preservados, sem oclusão de grandes vasos.', referencia='Fluxos preservados'),
            op('Radiografia de tórax', resultado='Sem opacidades focais ou derrame.', referencia='Sem alterações agudas'),
        ]),
    ]),
    resultados('r1', 'Primeiro momento', 'Resultados solicitados', 'p1', fundo=CENA,
        laminas={'Radiografia de tórax':lamina('rx_torax_normal.jpg','Radiografia de tórax','Imagem ilustrativa de outro adulto. Não há opacidade focal evidente; isso não exclui infecção precoce.','Mikael Häggström · Wikimedia Commons · CC0.')},
        rota=dict(pediu=['Hemograma diferencial'], entao='hemograma', senao='sem_hemograma')),
    pagina('hemograma', 'Interpretação', 'Risco imediato',
        p('O hemograma solicitado documenta neutropenia profunda em uma pessoa febril. '
          'A etiologia ainda está aberta; reconhecer a síndrome muda a urgência.'),
        fundo=CENA, segue='b1'),
    pagina('sem_hemograma', 'Interpretação', 'Reavaliação',
        p('A febre e as lesões dolorosas continuam sem explicação suficiente. '
          'A avaliação e a '
          'proteção contra deterioração podem avançar enquanto se completa a investigação.'),
        fundo=CENA, segue='b1'),
    bifurcacao('b1', 'Decisão 1', 'Primeiras horas',
        'Marina continua febril. Escolha a conduta com os dados que solicitou.', [
            caminho('Manter avaliação hospitalar', 'protecao',
                'Permite reavaliação rápida. Se há neutropenia febril documentada, iniciar antibiótico IV; '
                'se ainda não há diferencial, obtê-lo urgentemente e avaliar sepse.', rotulo_curto='Vigilância'),
            caminho('Adiar a abordagem sistêmica', 'b2',
                'A hipótese de dermatose não afasta deterioração. O atraso aumenta risco, mas não determina o desfecho.', rotulo_curto='Adiar'),
        ], fundo=CENA),
    pagina('protecao', 'Conduta', 'Conduta',
        p('A equipe mantém vigilância, coleta o que foi indicado sem atrasar terapia '
          'e trata a suspeita infecciosa conforme risco e protocolo local. '
          'Na neutropenia febril, utiliza cobertura IV antipseudomonas, ajustada '
          'a alergias, função renal e resistência local.'),
        p('Mesmo uma conduta adequada não impede toda infecção ou perda tecidual.'),
        fundo=CENA, rota=dict(pediu=['Hemograma diferencial'], entao='q2', senao='evolucao')),
    bifurcacao('b2', 'Decisão 2 · subramo de resgate', 'Reavaliação',
        'Antes de sair, Marina apresenta calafrios e maior prostração. Ainda está lúcida e sem hipotensão.', [
            caminho('Rever a hipótese e internar', 'resgate',
                'A mudança clínica é motivo para reavaliar; o resgate pode evitar dano, sem garantia.', rotulo_curto='Resgatar'),
            caminho('Manter espera por exames eletivos', 'atraso',
                'A espera prolonga a exposição ao risco infeccioso; melhora espontânea não validaria a decisão.', rotulo_curto='Esperar'),
        ], fundo=CENA),
    pagina('resgate', 'Reavaliação', 'Retorno ao cuidado',
        p('A equipe muda a conduta, mantém observação hospitalar e aborda a ameaça '
          'infecciosa com antibioticoterapia empírica IV, incluindo cobertura antipseudomonas se documentada neutropenia febril. O atraso pode ter consequências, mas não é possível '
          'inferir dano apenas da escolha anterior.'), fundo=CENA, rota=dict(pediu=['Hemograma diferencial'], entao='q2', senao='evolucao')),
    pagina('atraso', 'Evolução possível', 'Persistência',
        p('Neste curso ficcional, a febre persiste e Marina retorna no mesmo dia. '
          'É admitida e a equipe inicia antibioticoterapia empírica IV e vigilância, com cobertura antipseudomonas se documentada neutropenia febril. '
          'Não ocorreu choque inevitável: outros cursos seriam possíveis.'),
        fundo=CENA, rota=dict(pediu=['Hemograma diferencial'], entao='q2', senao='evolucao')),
    questao('q2', 'Em um cenário de febre de 38,6 °C e neutrófilos de 180/µL, quais duas medidas são prioritárias? '
        '', [
        ('Culturas sem atrasar terapia', 'A coleta é útil, mas não deve postergar o antimicrobiano.', True),
        ('Aguardar sorologias', 'Não é necessário fechar a etiologia para proteger contra infecção.', False),
        ('G-CSF como monoterapia', 'G-CSF não trata a ameaça infecciosa.', False),
        ('Antibiótico IV antipseudomonas', 'Neutropenia febril profunda exige terapia empírica e vigilância hospitalar.', True),
        ('Pulso isolado de corticoide', 'Não oferece cobertura infecciosa e pode agravar infecção.', False),
    ], 'Urgência antes da causa'),
    pagina('evolucao', 'Segundo momento', 'Evolução',
        p('Durante a internação, Marina consegue dormir após analgesia, mas refere dor ao trocar os curativos. Algumas placas passam a ter contornos ramificados e centro mais escuro, sem que isso seja acompanhado de crepitação. '
          'Não há falta de ar. Ao levantar para ir ao banheiro, percebe a urina mais escura pela primeira vez e avisa à enfermagem. Não refere ardor ao urinar. A lesão cutânea '
          'pode continuar evoluindo mesmo após o início do atendimento; isso '
          'não comprova falha do antibiótico ou necessidade de corticoide.'), fundo=CENA),
    pagina('evolucao_urinaria', 'Durante a internação', 'Uma nova queixa',
        p('Marina tenta lembrar se a urina já estava diferente em casa, mas não '
          'tem certeza. Não sabe estimar o volume eliminado e não identifica '
          'sangue vivo. A equipe registra a descrição como urina escura, sem '
          'convertê-la automaticamente em hematúria.'),
        p('A melhora do conforto após analgesia e a mudança da pele ocorreram '
          'no mesmo intervalo. Nenhuma delas, isoladamente, esclarece o que '
          'está acontecendo com a queixa urinária. Que hipótese conecta os '
          'achados e que alternativa ainda precisa permanecer em consideração?'), fundo=CENA),
    painel('p2', 'Segundo momento', 'Mecanismo e extensão', [
        grupo('Tecido e marcadores', 'pele', [
            op('Biópsia cutânea', resultado='Trombos em pequenos vasos dérmicos · Necrose epidérmica · Leucocitoclasia focal', referencia='Sem trombos ou necrose', alterado=True),
            op('ANCA por imunofluorescência', resultado='Padrão perinuclear 1:1.280', referencia='Negativo', alterado=True),
            op('Anti-MPO', resultado='128 U/mL', referencia='<20 U/mL neste ensaio', alterado=True),
            op('Anti-PR3', resultado='46 U/mL', referencia='<20 U/mL neste ensaio', alterado=True),
        ]),
        grupo('Rim', 'rim', [
            op('Creatinina de reavaliação', resultado='1,6 mg/dL', referencia='0,6–1,1 mg/dL', alterado=True),
            op('Sedimento urinário', resultado='50 hemácias/campo · Dismorfismo eritrocitário · Cilindros hemáticos', referencia='0–3 hemácias/campo; sem cilindros hemáticos', alterado=True),
            op('Complemento C3', resultado='104 mg/dL', referencia='90–180 mg/dL'),
        ]),
        grupo('Diferenciais', 'geral', [
            op('Crioglobulinas', resultado='Não detectadas; amostra transportada aquecida.', referencia='Não detectadas'),
            op('Anticardiolipina IgG', resultado='8 GPL-U/mL', referencia='<20 GPL-U/mL'),
            op('Antígeno e anticorpos HIV', resultado='Não reagente', referencia='Não reagente'),
        ]),
    ]),
    resultados('r2', 'Segundo momento', 'Resultados solicitados', 'p2', fundo=CENA,
        rota=dict(pediu=['Biópsia cutânea'], entao='tecido', senao='sem_tecido')),
    pagina('tecido', 'Interpretação', 'Mecanismo',
        p('A amostra solicitada sustenta lesão vascular com componente trombótico. '
          'O tecido não identifica a substância causal e não define, sozinho, '
          'anticoagulação ou imunossupressão sistêmica.'), fundo=CENA, rota=dict(pediu=['Anti-MPO','Anti-PR3'], entao='q3', senao='q4')),
    pagina('sem_tecido', 'Interpretação', 'Hipóteses abertas',
        p('A aparência clínica permite mais de um mecanismo. Sem documentação '
          'tecidual, mantenha linguagem de hipótese e escolha os próximos passos '
          'pela gravidade e pelas informações realmente disponíveis.'), fundo=CENA, rota=dict(pediu=['Anti-MPO','Anti-PR3'], entao='q3', senao='q4')),
    questao('q3', 'Se anti-MPO e anti-PR3 forem simultaneamente positivos, qual conclusão é válida? Selecione uma.', [
        ('Confirmam vasculite primária', 'Autoanticorpos não substituem avaliação etiológica.', False),
        ('Excluem infecção associada', 'Infecção pode coexistir e alguns contextos infecciosos produzem autoanticorpos.', False),
        ('Indicam pulso obrigatório', 'A indicação depende de lesão orgânica, mecanismo e risco infeccioso.', False),
        ('Identificam um adulterante', 'Nenhum desses anticorpos identifica uma substância.', False),
        ('Sugerem pesquisar exposições', 'Dupla positividade é uma pista de causa associada à exposição, sem ser específica.', True),
    ], 'Sorologia orienta, não confirma'),
    questao('q4', 'As lesões mudaram apesar da abordagem inicial e surgiu urina escura. Quais duas medidas ajudam a decidir se o tratamento deve mudar?', [
        ('Ampliar corticoide com base apenas na área de necrose', 'Necrose pode refletir dano já estabelecido ou oclusão, sem indicar inflamação reversível.', False),
        ('Reavaliar infecção e profundidade das lesões', 'O mecanismo e uma complicação infecciosa podem coexistir.', True),
        ('Caracterizar função renal e sedimento', 'A queixa urinária pode indicar extensão para além da pele, mas precisa ser investigada.', True),
        ('Trocar antibiótico apenas porque a cor se intensificou', 'Mudança da cor não demonstra falha microbiológica.', False),
        ('Aguardar cicatrização para investigar outros órgãos', 'A evolução sistêmica não deve depender da cicatrização cutânea.', False),
    ], 'Discussão'),
    pagina('preparo_entrevista', 'Evolução', 'Entrevista individual',
        p('No intervalo entre os cuidados, Marina pede para conversar sem a irmã. Parece receosa ao retomar o episódio anterior de manchas e pergunta quem terá acesso às informações.'),
        p('A equipe oferece privacidade e explica como os dados serão usados no cuidado. Quando fica sozinha com a médica, conta que há um aspecto da história que preferiu não mencionar durante o atendimento inicial.'), fundo=CENA),
    pagina('entrevista', 'Terceiro momento', 'Entrevista privada',
        p('Em nova conversa, desta vez sem acompanhantes, Marina explica que hesitou em falar sobre um hábito por receio da reação da irmã. A equipe esclarece a finalidade clínica da entrevista. Ela relata uso '
          'intranasal de cocaína cerca de 72 horas antes da admissão. Ao reconstruir a cronologia, associa o episódio anterior de manchas ao mesmo contexto de uso. Não conhece a composição '
          'do produto. No reexame, observa-se pequena placa purpúrica na orelha.'),
        p('O relato muda a probabilidade das hipóteses; não confirma adulteração. '
          'A urina escura persiste, sem dispneia ou hemoptise.'), fundo=CENA),
    pagina('plano_exposicao', 'Evolução', 'História complementar',
        p('Marina não dispõe de amostra do produto e não sabe sua composição. Nega nova exposição depois da internação. A irmã, que ajuda com a filha, ainda não conhece essa parte da história; Marina prefere escolher como será feita a conversa.'),
        p('A pequena lesão na orelha é registrada no exame seriado. Ela permanece sem falta de ar ou sangue no escarro. A urina continua descrita como escura, enquanto a equipe organiza a próxima etapa da investigação.'), fundo=CENA),
    painel('p3', 'Terceiro momento', 'Exposição e gravidade', [
        grupo('Toxicologia', 'geral', [
            op('Benzoilecgonina urinária', resultado='Detectada por método confirmatório.', referencia='Não detectada', alterado=True),
            op('Levamisol urinário por LC-MS/MS', resultado='Não detectado na amostra tardia, coletada cerca de 96 h após o último uso relatado.', referencia='Não detectado'),
        ]),
        grupo('Rim', 'rim', [
            op('Creatinina atual', resultado='2,6 mg/dL', referencia='0,6–1,1 mg/dL', alterado=True),
            op('Relação proteína/creatinina urinária', resultado='1,2 g/g', referencia='<0,2 g/g', alterado=True),
            op('Biópsia renal', resultado='Glomerulonefrite necrosante com crescentes celulares · Imunofluorescência pauci-imune', referencia='Sem necrose ou crescentes', alterado=True,
               exige=['Sedimento urinário', 'Creatinina de reavaliação'], porque='Solicitar após documentar indicação renal; avaliar segurança do procedimento'),
            op('Anti-MBG', resultado='Não reagente', referencia='Não reagente'),
        ]),
        grupo('Infecção e sangue', 'sangue', [
            op('Hemograma de controle', resultado='Neutrófilos absolutos 420/µL · Hemoglobina 11,7 g/dL · Plaquetas 226.000/µL', referencia='Neutrófilos 1.500–7.500/µL', alterado=True),
            op('Novas hemoculturas', resultado='Sem crescimento em 48 h; coleta sob antibiótico.', referencia='Sem crescimento'),
            op('Cultura de tecido cutâneo', resultado='Sem crescimento bacteriano em 48 h; coleta sob antibiótico.', referencia='Sem crescimento'),
        ]),
    ]),
    resultados('r3', 'Terceiro momento', 'Resultados solicitados', 'p3', fundo=CENA,
        rota=dict(pediu=['Benzoilecgonina urinária', 'Levamisol urinário por LC-MS/MS'], entao='toxicologia', senao='sem_toxicologia')),
    pagina('toxicologia', 'Interpretação', 'Janela de detecção',
        p('Os testes solicitados documentam exposição à cocaína, mas não documentam '
          'levamisol. O resultado negativo tardio não exclui esse adulterante. '
          'A detecção depende de tempo, método e limite analítico.'), fundo=CENA, segue='q5'),
    pagina('sem_toxicologia', 'Interpretação', 'Limite da atribuição',
        p('Integre somente os testes que solicitou. O relato de uso continua '
          'válido para formular uma hipótese, mas não autoriza afirmar a '
          'composição do produto. Sem análise específica positiva, não documente '
          'confirmação de levamisol.'), fundo=CENA, segue='q5'),
    questao('q5', 'Sobre toxicologia, quais duas afirmações são corretas?', [
        ('Negativo tardio não exclui', 'Levamisol tem janela curta e a sensibilidade depende do ensaio.', True),
        ('48 horas é corte absoluto', 'É uma referência prática de coleta precoce, não limite universal.', False),
        ('Triagem sempre inclui levamisol', 'Em geral é necessário solicitar método específico.', False),
        ('Metabólito prova causalidade', 'Detectar exposição à cocaína não identifica a causa da lesão.', False),
        ('Benzoilecgonina não identifica adulterante', 'Benzoilecgonina indica exposição à cocaína, não a composição do produto.', True),
    ], 'Exposição não equivale a causalidade'),
    bifurcacao('b3', 'Decisão 3', 'Plano integrado',
        'Escolha com base no seu prontuário. Se faltam exames, mantenha a incerteza explícita.', [
            caminho('Avaliar ameaça orgânica em paralelo', 'imagem_rim',
                'Investigar rim e infecção simultaneamente permite individualizar terapia; ausência de biópsia não impede avaliação urgente.', rotulo_curto='Investigar e proteger'),
            caminho('Manter apenas cuidados da pele', 'reavaliacao_suporte',
                'Suporte é central, mas pode ser insuficiente diante de sinais renais. Um resultado favorável não validaria ignorar esses sinais.', rotulo_curto='Só suporte'),
            caminho('Iniciar pulso sem avaliar infecção', 'vigilancia_infecciosa',
                'Aumenta risco infeccioso sem esclarecer benefício. O curso adverso apresentado é possível, não inevitável.', rotulo_curto='Pulso isolado'),
        ], fundo=CENA),
    pagina('imagem_rim','Discussão visual','Corpúsculo renal',
        p('Localize o tufo capilar e o espaço urinário. Em qual compartimento se inicia a filtração? Que observações urinárias poderiam sugerir lesão nessa barreira?'),
        '<details class="leitura"><summary>Revelar pontos de discussão</summary><p>A barreira de filtração separa sangue e espaço urinário. Hematúria glomerular e proteinúria precisam ser demonstradas e interpretadas em conjunto. Este esquema normal não substitui o sedimento nem demonstra o padrão de uma biópsia.</p></details>',
        chave_corpusculo(), fundo=CENA,lamina_=lamina('corpusculo.svg','Corpúsculo renal','Anatomia normal. 2: camada parietal; 4: espaço urinário; 10: capilares. Não é biópsia da paciente.','Michał Komorniczak · Wikimedia Commons · CC BY-SA 3.0 · sem alterações.')),
    questao('q6', 'Qual princípio orienta a condução simultânea de suspeita de lesão orgânica e possível infecção? Selecione uma.', [
        ('Esperar toxicologia positiva', 'A confirmação do agente não é requisito para abordar ameaça renal.', False),
        ('Avaliar rim e infecção em paralelo', 'Buscar biópsia quando viável e discutir imunossupressão se houver ameaça orgânica; tratar infecção concomitante.', True),
        ('Tratar apenas com curativos', 'O cuidado de pele não substitui a avaliação sistêmica.', False),
        ('Proibir toda imunossupressão', 'Neutropenia aumenta risco, mas não é veto absoluto diante de ameaça orgânica.', False),
        ('Pulsar só pelo ANCA', 'Sorologia isolada não estabelece o mecanismo da lesão renal.', False),
    ], 'Órgão ameaçado muda a decisão'),
    pagina('plano_conjunto', 'Evolução', 'Avaliação conjunta',
        p('Durante a visita conjunta, Marina está lúcida, alimenta-se e relata dor ao trocar os curativos. A pele adjacente às placas não apresenta crepitação; a inspeção e a avaliação da profundidade continuam sendo feitas em cada troca.'),
        p('A equipe revê o risco infeccioso e os resultados disponíveis antes de definir a intensidade do tratamento. Marina pergunta se a necessidade de cuidar do rim significa que precisará de diálise. A resposta é vinculada à avaliação clínica e funcional, sem concluir apenas pelo aspecto da urina.'), fundo=CENA),
    pagina('renal', 'Plano', 'Avaliação conjunta',
        p('Nefrologia, infectologia e reumatologia discutem gravidade, possibilidade '
          'de biópsia e segurança da imunossupressão. Antimicrobianos e controle '
          'de foco continuam conforme indicação. Não é preciso esperar uma '
          'cultura negativa para sempre, nem ignorar infecção para tratar o rim.'),
        fundo=CENA, rota=dict(pediu=['Biópsia renal'], entao='seguimento_recuperacao', senao='fim_incerteza')),
    pagina('reavaliacao_suporte', 'Evolução', 'Reavaliação das lesões',
        p('Após analgesia e proteção das lesões, Marina tolera melhor a troca de roupa. Algumas áreas escuras permanecem bem delimitadas. Não há resolução imediata da dor e a urina continua escura.'),
        p('Consegue ir ao banheiro com ajuda da irmã, mas sente receio de voltar ao trabalho em pé. A equipe reavalia o plano, porque a melhora do conforto não esclareceu a queixa urinária.'), fundo=CENA, segue='suporte'),
    pagina('suporte', 'Plano', 'Extensão não resolvida',
        p('Curativos, analgesia e interrupção da exposição são mantidos. '
          'Urina escura requer avaliação além da pele. O grau de certeza sobre '
          'a extensão depende do que foi investigado.'),
        fundo=CENA, rota=dict(pediu=['Sedimento urinário'], entao='fim_sequela', senao='fim_incerteza')),
    pagina('seguimento_recuperacao', 'Evolução', 'Evolução na enfermaria',
        p('Depois do tratamento individualizado, o estado geral melhora e deixa de apresentar novas placas durante a observação. As áreas já necrosadas, porém, persistem e continuam exigindo cuidados locais. A recuperação da pele não é imediata.'),
        p('Marina participa das trocas de curativo e aprende a reconhecer sinais de piora. Os retornos renal, hematológico e cutâneo são articulados antes de encerrar a internação; ela ainda não se sente pronta para cumprir um turno inteiro na loja.'), fundo=CENA, segue='fim_recuperacao'),
    desfecho('fim_recuperacao', 'Recuperação parcial',
        p('A biópsia solicitada permite discutir tratamento da lesão glomerular '
          'pauci-imune. Neste curso possível, após terapia individualizada e '
          'vigilância infecciosa, Marina melhora clinicamente e mantém seguimento '
          'renal e de feridas. A recuperação completa permanece incerta.'),
        qualidade='melhor', porque='O manejo dirigido pode limitar dano ativo, mas não garante reversão de tecido já lesado.',
        fundo=CENA, fecho='incerteza'),
    desfecho('fim_sequela', 'Lesão persistente',
        p('Neste curso possível, a limitação ao cuidado cutâneo é revista após '
          'persistência de sintomas. Marina necessita tratamento especializado '
          'e acompanhamento prolongado. Não há dado suficiente nesta rota para '
          'quantificar função renal residual ou afirmar dependência de diálise.'),
        qualidade='medio', porque='O atraso pode ampliar dano orgânico. A gravidade inicial também influencia a evolução; não há penalidade numérica automática.',
        fundo=CENA, fecho='incerteza'),
    pagina('vigilancia_infecciosa', 'Evolução', 'Reavaliação clínica',
        p('Após a decisão de pulso nesta rota, Marina volta a apresentar calafrios e passa a responder mais lentamente. As extremidades estão frias, a frequência cardíaca aumenta e a equipe é chamada para nova avaliação.'),
        p('É iniciada abordagem de deterioração com revisão do suporte, pesquisa de foco e reavaliação dos antimicrobianos. Não há identificação de agente nesta página. A equipe discute a imunossupressão novamente diante da mudança do quadro.'), fundo=CENA, segue='fim_infeccao'),
    desfecho('fim_infeccao', 'Complicação infecciosa possível',
        p('Neste curso possível, Marina desenvolve deterioração clínica compatível '
          'com infecção e precisa de suporte intensivo e revisão do plano. '
          'Sem cultura solicitada e positiva, não se atribui um microrganismo. '
          'A evolução final permanece aberta.'),
        qualidade='pior', porque='Imunossupressão sem avaliação infecciosa pode agravar uma infecção; essa associação não determina que todo paciente terá este curso.',
        fundo=CENA, fecho='incerteza'),
    desfecho('fim_incerteza', 'Investigação em continuidade',
        p('A hipótese associada à exposição permanece provável, sem caracterização '
          'completa da extensão. Marina segue em avaliação hospitalar ou transferência '
          'para equipe especializada. Não se declara rim normal, glomerulonefrite '
          'confirmada ou cura na ausência de documentação.'),
        qualidade='medio', porque='Falta de exame é falta de conhecimento, não proteção contra doença. Esta rota permite continuar cuidando sem fabricar confirmação.',
        fundo=CENA, fecho='incerteza'),
    pagina('incerteza', 'Fecho clínico', 'Diagnóstico provável',
        p('O conjunto clínico e a exposição relatada sustentam vasculopatia/vasculite '
          'provavelmente associada à cocaína, com suspeita de participação do '
          'levamisol. O grau de sustentação depende dos exames escolhidos. '
          'A exposição ao adulterante não foi confirmada neste caso.'),
        p('Manter interrupção da exposição, acolhimento e oferta de cuidado em '
          'adicções, seguimento hematológico, renal e cutâneo. Nenhum lote ou '
          'via de uso pode ser apresentado como seguro. Reexposição pode causar '
          'recorrência. Os desfechos são exemplos, não probabilidades clínicas.'),
        fundo=CENA),
    pagina('continuidade_cuidado', 'Evolução', 'Continuidade do cuidado',
        p('Na conversa sobre continuidade, Marina manifesta preocupação com o trabalho, a filha e a exposição de informações pessoais. Autoriza a participação da irmã no planejamento e combina quem poderá acompanhá-la nos retornos.'),
        p('O destino depende do curso percorrido: alguns caminhos ainda exigem internação ou transferência. O plano registra a hipótese clínica, a situação das feridas e a avaliação renal pendente, além de oferecer cuidado para interrupção da exposição sem condicionar o acolhimento à abstinência.'), fundo=CENA),
    pagina('fontes', 'Fontes e revisão', 'Evidência e limites',
        p('Fontes primárias abertas: '
          '<a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC2780984/" target="_blank" rel="noopener">Knowles 2009</a>; '
          '<a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC2802606/" target="_blank" rel="noopener">Wiens 2010</a>; '
          '<a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC3255368/" target="_blank" rel="noopener">McGrath 2011</a>; '
          '<a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC3573092/" target="_blank" rel="noopener">Vasculopatia com confirmação analítica</a>; '
          '<a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC4602417/" target="_blank" rel="noopener">Carlson 2014</a>; '
          '<a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC9154317/" target="_blank" rel="noopener">Ensaio de neutropenia febril 2022</a>.'),
        p('Séries e relatos não demonstram superioridade da imunossupressão ou '
          'do G-CSF nesta síndrome. O manejo antimicrobiano é extrapolado da '
          'neutropenia febril, sobretudo oncológica. Dados, cronologia e '
          'desfechos são ficcionais; a cena é apenas ilustrativa.'),
        p('Avance para a revisão dos pedidos e respostas. Avalie a decisão '
          'pelas informações disponíveis, não apenas pelo resultado final.'), fundo=CENA),
]

REVISAO = [
    dict(rotulo='Hemograma diferencial', chave='Hemograma diferencial',
         porque='Permite reconhecer neutropenia febril. Febre com lesões dolorosas exige avaliar risco sistêmico.'),
    dict(rotulo='Culturas iniciais', chave='Hemoculturas iniciais',
         porque='Coletar antes do antibiótico quando isso não atrasa tratamento. Culturas negativas não excluem infecção.'),
    dict(rotulo='Avaliação renal', chave='Sedimento urinário',
         porque='Ajuda a localizar lesão glomerular. Sem ele, a urina escura ainda merece investigação; não se presume normalidade.'),
    dict(rotulo='Função renal atual', chave='Creatinina atual',
         porque='Quantifica disfunção; interpretar com evolução e sedimento, sem confundir ausência de medida com ausência de doença.'),
    dict(rotulo='Mecanismo cutâneo', chave='Biópsia cutânea',
         porque='Pode distinguir padrões trombóticos e inflamatórios, sem identificar sozinho o agente causal.'),
    dict(rotulo='Toxicologia específica', chave='Levamisol urinário por LC-MS/MS',
         porque='Pode documentar exposição se positiva; coleta tardia reduz rendimento. Não é requisito para tratar ameaça clínica.'),
]

from motor.estudo_imagem import ecg, sequencia, inserir_antes
inserir_antes(ETAPAS, 'p1', ecg('ecg_evolucao',
    'Na reavaliação, Marina mantém dor e febre; o pulso continua acelerado. A equipe obtém um ECG. Qual é o ritmo e quais dados clínicos você revê antes de atribuir uma causa?', IMG,
    'Febre, dor e outras causas de ativação simpática podem produzir esse ritmo. O ECG não identifica uma exposição nem estabelece a causa das lesões cutâneas.'))
inserir_antes(ETAPAS, 'p3', sequencia('us_evolucao', 'Ultrassonografia renal',
    'Como a urina permanece escura, a equipe acrescenta ultrassonografia à investigação urinária. Observe o corte longitudinal apresentado. O que esse método pode esclarecer e quais mecanismos continuariam possíveis?',
    IMG / 'us_rim.jpg',
    'Hansen, Nielsen e Ewertsen · Wikimedia Commons · CC BY 4.0. Recorte prévio e setas adicionadas na discussão.',
    'Rim de outro adulto. Asteriscos e cálipers são da fonte; não representam medidas da paciente.',
    [((524, 283), (620, 105)), ((447, 400), (720, 550))],
    ['1. A seta alcança o parênquima periférico, mais escuro que a região central.',
     '2. O seio renal é mais ecogênico. Neste corte, não há dilatação coletora evidente.',
     'O laudo ficcional descreve rins de dimensões preservadas, sem dilatação pielocalicial. A ausência de obstrução não exclui lesão glomerular: urina e função renal continuam fundamentais.']))

from casos.investigacoes import aplicar, ESPECIFICACOES
aplicar(ETAPAS, ESPECIFICACOES["cocaina_levamisol"])

from casos.paineis_evolucao import aplicar as paineis_equipe
paineis_equipe(ETAPAS, "cocaina_levamisol")

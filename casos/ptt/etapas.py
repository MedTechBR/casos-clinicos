"""Revisão editorial de 23/10/2026: evolução clínica, decisões precoces e
urgências preservadas. Paciente e cronologia ficcionais; fontes na última tela.
"""
import json
from pathlib import Path

from motor.estudo_imagem import estudo
from motor.etapas import (alt, bifurcacao, caminho, capa, desfecho, op, p,
                          pagina, painel, par, pareamento, pergunta, pontos,
                          topicos, vitais)

TITULO = 'Do outro lado do plantão'
RODAPE = 'Paciente ficcional · evoluções simuladas para ensino'
COR = '#7c3aed'
IMG = Path(__file__).parent / 'img'
BANCO = []
MOLDE = 'nejm'


def credito_meta(meta):
    m = json.loads(Path(meta).read_text())
    return m['autor'] + ' · Wikimedia Commons · ' + m['licenca'] + ' · setas adicionadas'


def pg(k, titulo, *textos, segue='', conforme=None):
    return pagina(k, titulo, '', *(p(t) for t in textos), so_kicker=True,
                  segue=segue, conforme=conforme)


def disc(k, titulo, *textos, segue=''):
    return pagina(k, 'Discussão', titulo, *(p(t) for t in textos), segue=segue)


def Q(k, n, enunciado, opcoes, explicacao, segue=''):
    """Pergunta no molde do NEJM: alternativas curtas e uma explicação só,
    em seções (subtítulo, texto)."""
    return pergunta(k, f'Pergunta {n}', enunciado,
                    [alt(t, certa=ok) for t, ok in opcoes],
                    explicacao=explicacao, segue=segue)


def ex(nome, valor, ref='—', alt_=False):
    return op(nome, resultado=valor, referencia=ref, alterado=alt_)


def fim(k, titulo, texto, porque, qualidade):
    return desfecho(k, titulo, p(texto), qualidade=qualidade, porque=porque,
                    fecho='retrospectiva')


ETAPAS = [

    capa(TITULO, fundo='cena-paciente.png', kicker='Caso interativo',
         selo='Paciente ficcional · procedência e créditos na última tela'),

    pg('historia', 'Apresentação',
       'Sandra, técnica de enfermagem de 36 anos, moradora de Quixadá, no '
       'sertão central do Ceará, é trazida à emergência do hospital regional '
       'pelo marido no quarto dia de dor de cabeça, cansaço e febre baixa, '
       'entre 37,6 e 38 °C. Há três dias apareceram pintas vermelhas nas '
       'pernas e a gengiva sangra ao escovar os dentes. Desde ontem a urina '
       'está "cor de café".',
       'O marido conta que duas vezes, ontem e hoje, ela "trocou as palavras" '
       'e repetiu a mesma pergunta por alguns minutos, e depois voltou ao '
       'normal. No segundo dia, numa unidade de pronto atendimento, o teste '
       'NS1 para dengue foi negativo e as plaquetas eram 38.000/mm³; saiu com '
       'soro oral e orientação de voltar se piorasse.',
       'Nega diarreia, vômitos, tosse, rigidez no pescoço, convulsão, viagem '
       'recente, picada de carrapato, contato com água de enchente e uso de '
       'anti-inflamatório. Tem dor lombar leve desde ontem.'),

    pagina('ficha', 'Ficha do paciente', '',
           topicos(('Antecedentes', 'Hipotireoidismo por tireoidite de Hashimoto '
                    'há cinco anos. Duas gestações: a primeira sem intercorrências; '
                    'na segunda, aos 29 anos, cesárea de urgência com 34 semanas '
                    'por "pré-eclâmpsia grave com síndrome HELLP", nove dias de '
                    'UTI, transfusão de plaquetas e de plasma. O bebê nasceu bem.'),
                   ('Medicações', 'Levotiroxina 75 µg ao dia. Anticoncepcional '
                    'oral combinado, etinilestradiol e levonorgestrel, há um '
                    'ano. Dipirona para a dor de cabeça nestes quatro dias.'),
                   ('Hábitos', 'Não fuma. Cerveja em festas. Nega drogas.'),
                   ('Trabalho', 'Plantões noturnos na emergência do hospital '
                    'municipal. Na semana passada o setor atendeu um rapaz com '
                    'meningite; ela não participou da intubação e não recebeu '
                    'profilaxia. Acidente com agulha há dois anos, com '
                    'seguimento sorológico negativo.'),
                   ('Família', 'Mãe hipertensa, viva. Uma irmã com hipotireoidismo. '
                    'Sem doença do sangue conhecida na família.')),
           so_kicker=True),

    pagina('exame', 'Exame físico', '',
           vitais(('Temperatura', '37,9 °C', True),
                  ('Pressão arterial', '148/92', True),
                  ('Frequência cardíaca', '104', True),
                  ('Frequência respiratória', '20', False),
                  ('SpO₂ em ar ambiente', '97%', False),
                  ('Glasgow', '14', True)),
           topicos(('Estado geral', 'Descorada, com icterícia leve nas escleras. '
                    'Sonolenta, desorientada no tempo, obedece a comandos.'),
                   ('Pele e mucosas', 'Petéquias nas pernas e nos antebraços, '
                    'algumas confluentes. Sangramento discreto na gengiva.'),
                   ('Neurológico', 'Sem rigidez de nuca, sem déficit motor, '
                    'pupilas simétricas. Fala fluente no momento do exame.'),
                   ('Coração e pulmões', 'Taquicárdica, sem sopros. Pulmões '
                    'limpos.'),
                   ('Abdome', 'Doloroso à palpação profunda no flanco esquerdo. '
                    'Fígado e baço não palpáveis.'),
                   ('Linfonodos', 'Sem adenomegalias.')),
           so_kicker=True),

    pg('primeiros_minutos', 'O quadro muda durante a admissão',
 'Enquanto se obtém acesso venoso, Sandra deixa de nomear o relógio e o celular. Obedece a comandos, não tem fraqueza ou hipoglicemia; oito minutos depois volta a falar normalmente. A melhora é documentada, sem encerrar a avaliação de isquemia ou infecção.',
 'É levada para área monitorizada. Glicemia à beira do leito, hemograma, função renal e urina compõem a avaliação inicial. A TC de crânio é solicitada desde já pela alteração neurológica focal transitória; a investigação será ampliada assim que os primeiros achados forem revistos, ainda na primeira hora. Não há câncer, transplante, prótese valvar, uso de quinina ou medicamento novo associado a microangiopatia; a gestação atual será excluída.'),

    estudo('pele', 'As pintas das pernas',
           'Observe as lesões nas pernas. Observe o tamanho, o relevo e o que acontece onde as lesões se juntam.',
           IMG / 'pele_perna.jpg',
           'Fotografia.',
           credito_meta(IMG / 'pele_perna.jpg.json'),
        [
         ((361, 474), (205, 560), '**Petéquia**: ponto vermelho-escuro de 1 a 2 mm, plano, '
          'que não some à pressão.', 12),
         ((389, 392), (250, 330), '**Lesão maior**, de vários milímetros, onde petéquias '
          'confluíram: púrpura.', -12),
         ((529, 478), (660, 560), 'Outra **petéquia**, isolada, na pele de cor normal: as '
          'lesões se espalham sem relevo.', 12),
        ],
        ['No exame de Sandra: petéquias nas pernas e nos antebraços, algumas '
         'confluentes, e sangramento discreto da gengiva.',
         'Lesões planas, puntiformes, não desaparecendo à pressão; algumas são confluentes.']),

    painel('res1', 'Primeiros exames', 'Sangue', [
        ex('Hemoglobina / hematócrito', '7,8 g/dL / 23%', 'Hb 12–16 g/dL', True),
        ex('VCM / RDW', '88 fL / 18,6%', '80–100 fL / 11,5–14,5%', True),
        ex('Leucócitos', '9.800/mm³ · neutrófilos 72%', '4.000–11.000/mm³'),
        ex('Plaquetas', '14.000/mm³ {{(38.000 na UPA, dois dias antes)}}', '150.000–450.000/mm³', True),
        ex('Volume plaquetário médio', '12,4 fL', '7–11 fL', True),
        ex('Ureia / creatinina', '62 / 1,4 mg/dL {{(TFG 50, CKD-EPI 2021)}}', 'até 42 / 0,6–1,1', True),
        ex('Proteína C reativa', '24 mg/L', 'até 5 mg/L', True),
        ex('Urina', 'Marrom-escura · sangue +++ · 0 a 2 hemácias por campo · 8 leucócitos por campo · nitrito negativo · proteína +', '—', True),
    ], introducao='Colhidos na chegada. Dois pares de hemoculturas foram colhidos '
                  'antes de qualquer antibiótico.'),

    pg('reavaliacao_inicial', 'Reexame após os primeiros resultados',
 'Sandra voltou a nomear os objetos, mas continua cansada e com a urina escura. A hemoglobina de 7,8 e a queda das plaquetas para 14.000 não se explicam pelo pequeno sangramento gengival. A fita marca sangue sem número proporcional de hemácias no sedimento.',
 'A equipe associa esses achados à icterícia e solicita marcadores de hemólise, reticulócitos e revisão do esfregaço, além de antiglobulina direta. As coletas são urgentes; recuperar a fala entre episódios não autoriza adiar a investigação.'),

    Q('p1', 1, 'Quais três exames você prioriza na admissão?', [
 ('Esfregaço periférico com quantificação de esquizócitos', True),
 ('Haptoglobina sérica', True), ('Teste de antiglobulina direto', True),
 ('Mielograma', False), ('Ultrassonografia do baço', False), ('Pesquisa de sangue oculto fecal', False)
 ], [('Prioridade', 'Fragmentação, consumo de haptoglobina e antiglobulina direta ajudam a distinguir microangiopatia, hemólise e mecanismo imune. DHL, bilirrubinas, reticulócitos e coagulação também são obtidos pela equipe; esta é uma seleção limitada entre opções, não um painel completo de prescrição.'), ('Menor prioridade', 'Mielograma, ultrassom e pesquisa de sangramento não explicam tão bem a associação de anemia importante, icterícia e disfunção neurológica. Púrpura plana pode acompanhar trombocitopenia; lesões palpáveis ou necróticas mudariam a avaliação de parede vascular e oclusão, sem definir causa pela aparência isolada. Os resultados indicados chegam independentemente da resposta.'), ('Como organizar as citopenias', 'Anemia com plaquetas baixas pode decorrer de baixa produção, destruição imune, consumo ou fragmentação das hemácias. Esfregaço e marcadores de hemólise testam esses mecanismos. Esquizócitos indicam fragmentação, mas ainda é necessário diferenciar suas causas.')]),

    painel('res1b', 'Após hemograma e urina', 'Investigação da anemia', [
        ex('Bilirrubina total / indireta', '3,2 / 2,7 mg/dL', 'até 1,2 / 0,9 mg/dL', True),
        ex('Desidrogenase lática (DHL)', '1.480 U/L', '120–246 U/L', True),
        ex('Haptoglobina', 'menor que 10 mg/dL', '30–200 mg/dL', True),
        ex('Teste de antiglobulina direto', 'Negativo', 'negativo'),
        ex('AST / ALT', '58 / 31 U/L', 'até 32 / 33 U/L', True),
        ex('Creatinoquinase', '110 U/L', 'até 170 U/L'),
        ex('Beta-hCG sérico', 'Negativo', 'negativo'),
        ex('Reticulócitos', '7,8%', '0,5–2,5%', True),
        ex('Lâmina revista pelo laboratório', 'Plaquetopenia confirmada, sem agregados · anisocitose e policromasia', '—', True),
    ]),

    pg('reavaliacao', 'Quarenta minutos depois',
 'A temperatura chega a 38,1 °C e ela fica mais sonolenta, ainda sem rigidez de nuca ou déficit fixo. A urina permanece escura e o sangramento gengival é discreto. Não há hipotensão ou oligúria importante.',
 'Doença meningocócica precisa de cobertura empírica enquanto é avaliada; ceftriaxona em dose meníngea começa após hemoculturas, sem aguardar líquor. A exposição ocupacional isolada é fraca evidência de causa. Hemólise com plaquetopenia e manifestações neurológicas exige avaliar consumo de fatores e lesão de órgãos: a equipe solicita coagulação, fibrinogênio, lactato e avaliação cardíaca, em paralelo à revisão urgente do esfregaço. ADAMTS13 será colhida antes de qualquer plasma se a suspeita se sustentar, sem aguardar todos os resultados. NS1 negativo isolado não exclui dengue.'),

    painel('res1c', 'Avaliação dirigida na primeira hora', 'Coagulação e lesão de órgãos', [
        ex('Tempo de protrombina / INR', '13,1 s / 1,08', 'INR até 1,2'),
        ex('TTPa (relação)', '29 s (1,0)', 'até 1,25'),
        ex('Fibrinogênio', '340 mg/dL', '200–400 mg/dL'),
        ex('D-dímero', '1.200 ng/mL', 'até 500 ng/mL', True),
        ex('Lactato arterial', '1,6 mmol/L', 'até 2,0 mmol/L'),
        ex('Troponina I', '0,09 ng/mL', 'até 0,04 ng/mL', True),
        ex('Eletrocardiograma', 'Taquicardia sinusal, 104 bpm · sem alterações de ST', '—'),
    ]),

    estudo('tc', 'Tomografia de crânio sem contraste',
           'Feita na primeira hora, pela confusão que vai e volta, antes de '
           'decidir se é seguro puncionar o líquor. Corte axial na altura dos '
           'ventrículos laterais.',
           IMG / 'tc_cranio.jpg',
           'Tomografia.',
           credito_meta(IMG / 'tc_cranio.jpg.json'),
        [
         ((508, 522), (120, 300), '**Corno frontal** do ventrículo lateral, de tamanho normal '
          'e simétrico ao do outro lado.', 12),
         ((430, 780), (120, 980), '**Corno occipital**: sem sangue no ventrículo e sem '
          'desvio da linha média.', -12),
         ((632, 375), (880, 180), '**Substância branca frontal** sem hipodensidade: '
          'nenhum sinal de infarto estabelecido.', -12),
        ],
        ['Sem hemorragia, sem hipodensidade, sem efeito de massa. Ventrículos '
         'e sulcos normais para a idade.',
         'Não foram identificadas alterações estruturais agudas neste estudo sem contraste.']),

    bifurcacao('b1', 'Investigação em paralelo', 'Uma amostra adicional',
 'O esfregaço está em revisão urgente e a avaliação da microangiopatia já foi acionada. Para a hipótese infecciosa ainda aberta, qual exame você prioriza entre estes?', [
 caminho('Urocultura', 'via_urina', 'Dor lombar e leucócitos urinários permitem avaliar foco urinário, sem assumir que explica a hemólise.'),
 caminho('PCR para meningococo em sangue', 'via_sangue', 'Quando disponível, pode acrescentar evidência sem punção lombar; resultado negativo não exclui toda infecção do SNC.')]),

    pg('via_urina', 'O trato urinário',
 'A amostra urinária é enviada e o laboratório fará cultura. A fita com sangue +++ e apenas 0–2 hemácias por campo favorece pigmentúria; CK normal e haptoglobina muito baixa apontam para hemoglobina. A dor lombar não basta para chamar pielonefrite. A cultura não será usada para adiar a hematologia.', segue='amostra'),

    pg('via_sangue', 'Investigação sem líquor imediato',
 'É enviada amostra sanguínea para PCR de meningococo. A urocultura também é colhida pela equipe pela queixa lombar, independentemente da prioridade escolhida. O resultado fica pendente. A punção lombar é adiada pela trombocitopenia e pela mudança de prioridade diagnóstica; a ceftriaxona já cobre a hipótese urgente. Não se transfundem plaquetas de rotina para viabilizar esse procedimento.', segue='amostra'),

    pg('amostra', 'Amostra antes do plasma',
 'Ainda na primeira hora, pela combinação de hemólise não imune provável, plaquetas muito baixas e manifestações neurológicas, colhe-se atividade de ADAMTS13, uma enzima que ajuda a controlar a formação de pequenos coágulos. A amostra será enviada ao centro de referência; o resultado não é necessário para iniciar o tratamento de uma suspeita forte. Inibidor funcional e anticorpo anti-ADAMTS13 são solicitados separadamente, usando alíquotas pré-plasma.',
 'Hematologia e centro de aférese são contatados já nessa fase. A transfusão ou infusão de plasma não deve preceder a coleta quando esta pode ser feita de imediato; tampouco a dificuldade de colher justificaria retardar terapia necessária.'),

    pg('manha', 'Revisão urgente do esfregaço',
 'Na primeira hora, a hematologista revê a lâmina de admissão: 4,2% de esquizócitos, plaquetas raras e policromasia. O laboratório complementa o laudo inicial que descrevia apenas anisocitose. Não se espera o dia seguinte para essa revisão.',
 'Os achados conectam a anemia e a queda plaquetária à síndrome de microangiopatia trombótica. A imagem didática abaixo explica o achado, sem pedir que se adivinhe sua causa apenas pela morfologia.'),

    estudo('esfregaco', 'Esfregaço de sangue periférico',
           'Esfregaço de sangue periférico. Compare o contorno das células marcadas com o de uma hemácia íntegra.',
           IMG / 'esfregaco.jpg',
           'Lâmina · região recortada.',
           credito_meta(IMG / 'esfregaco.jpg.json'),
        [
         ((336, 653), (175, 760), '**Hemácia em capacete**: perdeu um pedaço e ficou com '
          'uma borda reta e duas pontas.', 12),
         ((354, 731), (470, 805), '**Fragmento irregular**, menor que uma hemácia, sem '
          'halo central.', -12),
         ((361, 354), (285, 450), '**Hemácia íntegra**, redonda, com o halo central claro: '
          'a referência.', 12),
        ],
        ['No esfregaço de Sandra: 4,2% de esquizócitos (hemácias em capacete, '
         'triângulos e fragmentos), policromasia e plaquetas raras, sem '
         'agregados.',
         'Acima de 1%, num adulto com hemólise e plaquetopenia, a contagem apoia a suspeita de microangiopatia pela recomendação do ICSH de 2021.']),

    pg('plasmic', 'Probabilidade e decisão urgente',
 'PLASMIC 7: plaquetas <30.000, hemólise, ausência de câncer ativo, ausência de transplante, VCM <90, INR <1,5 e creatinina <2. O escore estima probabilidade de deficiência grave de ADAMTS13, sem substituir julgamento ou confirmação.',
 'PTT é a hipótese prioritária. Microangiopatia por complemento, infecção com CIVD inicial e outras causas permanecem possíveis; INR e fibrinogênio preservados pesam contra CIVD manifesta. A amostra pré-plasma está guardada, e não se espera seu resultado para tratar.'),

    Q('p2', 2, 'Qual procedimento você solicita neste momento?', [
 ('Troca plasmática terapêutica', True), ('Punção lombar', False),
 ('Biópsia renal', False), ('Mielograma', False)
 ], [('Urgência', 'A probabilidade alta de PTT com lesão neurológica exige troca plasmática urgente e corticoide. Transferência e preparo são imediatos; o objetivo não é consumir uma janela de espera. Plasma infundido pode ser ponte se houver atraso inevitável, sob controle de volume, e não substitui a troca na PTT imune. A TC sem alterações não afasta isquemia pequena, transitória ou recente, nem encefalite; seu resultado não encerra a avaliação da fala flutuante.')]),

    pg('transferencia', 'Durante a transferência',
 'Corticoide é iniciado após discussão com hematologia. O transporte monitorizado sai sem esperar ADAMTS13. Diante do tempo necessário até a aférese, recebe plasma como ponte, com vigilância respiratória e circulatória. Não há sangramento grave que justifique transfusão profilática de plaquetas.',
 'Já perto do centro, volta a trocar palavras por seis minutos; permanece hemodinamicamente estável e depois recupera a fala. A aparente normalidade entre os episódios não mudou a urgência nem permite substituir troca por observação.'),

    pg('troca', 'Ainda no primeiro dia',
 'A primeira troca plasmática começa no centro aproximadamente cinco horas após reconhecer a microangiopatia. Usa-se plasma como reposição, com volume e frequência definidos pela equipe. O corticoide é mantido e o acesso venoso é realizado por equipe experiente, guiado por ultrassom, sem transfusão rotineira de plaquetas.',
 'Caplacizumabe é discutido precocemente pela alta probabilidade de PTT imune, considerando sangramento, acesso e prazo do ensaio de ADAMTS13; neste hospital ficcional não há disponibilidade imediata. Isso não atrasa troca e corticoide. Rituximabe é planejado precocemente após avaliação infecciosa e rastreio de hepatite B.'),

    pg('resposta_inicial', 'Primeiras 48 horas',
 'A fala não volta a falhar após iniciar a troca; Sandra fica desperta e orientada. A urina clareia e a gengiva para de sangrar. Plaquetas sobem de 14.000 para 31.000 e depois 58.000/mm³, enquanto DHL cai para 820 U/L. Creatinina 1,1 mg/dL.',
 'Apesar da melhora, ainda sente palpitação ao caminhar ao banheiro, e a troponina segue discretamente elevada. A equipe mantém telemetria e avaliação cardíaca, sem atribuir tudo à ansiedade nem exigir dor torácica para vigiar o coração.'),

    bifurcacao('b2', 'Reavaliação', 'Palpitação durante a recuperação',
 'Sandra já está em telemetria e a troca continua. A palpitação recorrente ao caminhar ocorre com troponina ainda discretamente elevada. Qual exame adicional você prioriza nesta avaliação?', [
 caminho('Eletrocardiograma de 12 derivações durante o sintoma', 'tendencia_plaquetas', 'Pode documentar o ritmo e alterações isquêmicas dinâmicas que precisam ser comparadas com a admissão.'),
 caminho('Ecocardiograma transtorácico', 'tendencia_dhl', 'Avalia disfunção e alterações segmentares; não substitui monitorização do ritmo e avaliação isquêmica.')]),

    pg('tendencia_plaquetas', 'O ritmo durante a palpitação',
 'O ECG obtido durante o sintoma mostra taquicardia sinusal a 112 bpm, sem nova alteração de ST; a telemetria não registra arritmia sustentada. A troponina permanece em queda. Não há indicação de betabloqueador só pelo número da frequência; anemia, esforço e lesão aguda ainda importam.',
 'O ecocardiograma complementar mostra FE 60%, sem alteração segmentar ou derrame. A equipe mantém vigilância e reavaliaria imediatamente dor, síncope ou piora dos marcadores.', segue='p3'),

    pg('tendencia_dhl', 'Função cardíaca preservada',
 'O ecocardiograma mostra FE 60%, sem alteração segmentar ou derrame. O resultado não exclui lesão microvascular. Durante nova palpitação breve, ECG mostra taquicardia sinusal a 112 bpm sem alteração nova de ST, e a troponina permanece em queda.',
 'Sem arritmia sustentada na telemetria, a equipe mantém vigilância e reavaliaria imediatamente dor, síncope ou piora dos marcadores.', segue='p3'),

    Q('p3', 3, 'Na reavaliação, quais duas medidas você mantém?', [
 ('Manter troca plasmática diária', True), ('Manter monitorização cardíaca', True),
 ('Suspender troca após desaparecer a confusão', False), ('Iniciar anticoagulação plena sem outra indicação', False),
 ('Transfundir plaquetas para normalizar a contagem', False)
 ], [('Resposta ainda incompleta', 'A resolução dos sintomas neurológicos pode anteceder a resposta hematológica. Troca diária e vigilância de órgãos permanecem indicadas; a troponina exige contexto e tendência. Anticoagulação plena não é tratamento rotineiro da microtrombose da PTT. Plaquetas são reservadas a situações excepcionais, como sangramento ameaçador, com avaliação especializada.'), ('Resposta de um órgão não é resposta completa', 'Melhora neurológica e recuperação hematológica podem ocorrer em momentos diferentes. A decisão precisa reunir plaquetas, hemólise e órgãos afetados. Um único parâmetro em melhora não substitui a comparação de toda a trajetória.')]),

    pg('resultado', 'Terceiro dia',
 'Atividade de ADAMTS13 <5%, IgG anti-ADAMTS13 presente e inibidor de 1,8 unidade Bethesda na amostra pré-plasma: confirma PTT imune. Não é preciso esperar a pêntade completa. Rituximabe 375 mg/m² semanal por quatro doses é iniciado pelo centro, com cuidados de infusão e prevenção conforme risco.',
 'O prontuário obstétrico recuperado descreve plaquetopenia e hemólise persistentes após o parto, com melhora após plasma. Isso levanta a possibilidade de episódio anterior; sem ADAMTS13 daquela internação, não permite reclassificá-lo com certeza. AST de 90 U/L isolada não exclui HELLP.'),

    pg('recuperacao', 'Quinto dia',
 'Sem palpitação ou déficit neurológico, caminha pelo corredor. Plaquetas 162.000/mm³, DHL 290 U/L (limite 246), creatinina 0,9 e troponina normal. Hemoculturas e urocultura finais negativas; no ramo em que se solicitou PCR, também foi negativa. A investigação clínica permite suspender a ceftriaxona.',
 'É a primeira contagem normal, não garantia de resposta sustentada. A avaliação conjunta inclui ausência de nova isquemia e tendência da hemólise antes de interromper a troca.'),

    pg('remissao', 'Encerramento da fase aguda',
 'Nos dias seis e sete, plaquetas 188.000 e 215.000/mm³, DHL 240 e 215 U/L, sem nova isquemia. Após essa resposta sustentada, o centro encerra a troca no oitavo dia. Não exige normalização da ADAMTS13 para interrompê-la. Sandra recebe alta no 12.º dia e completa as doses semanais de rituximabe em acompanhamento.',
 'Aos 30 dias da última troca, sem caplacizumabe neste percurso, mantém resposta clínica; plaquetas 245.000/mm³ e ADAMTS13 34%. A atividade enzimática se recupera em ritmo diferente do hemograma. Remissão clínica e remissão da ADAMTS13 são dimensões distintas.'),

    Q('p4', 4, 'Qual resultado do seguimento exige reavaliação precoce?', [
 ('Queda confirmada da ADAMTS13 para menos de 20%', True),
 ('VCM de 91 fL', False), ('D-dímero discretamente elevado', False),
 ('Anti-TPO ainda positivo', False)
 ], [('Prevenir recaída', 'Queda confirmada da enzima pode anteceder recaída clínica e levar à avaliação de imunossupressão preventiva, frequentemente rituximabe. Não equivale automaticamente a indicação de nova troca sem microangiopatia clínica. Consideram-se tendência, método, contexto e decisão especializada.')]),

    pg('seguimento', 'Três meses depois',
 'ADAMTS13 68%, hemograma normal e nenhum déficit focal. Sandra voltou primeiro a atividades leves; cansaço e receio de novo episódio são discutidos antes de retomar plantões noturnos. Orienta-se vigilância prolongada da enzima e procura urgente por pontos vermelhos na pele, urina escura, confusão ou dor torácica.',
 'Contracepção sem estrogênio e eventual gestação são planejadas com hematologia e ginecologia. O DIU de levonorgestrel é uma opção escolhida após avaliação, não uma prescrição obrigatória para toda pessoa com PTT.'),

    fim('f1', 'Remissão com seguimento organizado',
 'Sandra recupera função neurológica, renal e cardíaca e mantém vigilância após a alta.',
 'A flutuação da fala não foi confundida com resolução; a melhora com troca não levou a encerrá-la antes da resposta sustentada. A confirmação enzimática caracterizou o mecanismo sem atrasar terapia.', 'melhor'),

    pagina('retrospectiva', 'Pontos de ensino', '', pontos(
 'Anemia hemolítica e trombocitopenia com lesão de órgão exigem investigação urgente de microangiopatia.',
 'Esquizócitos apoiam a síndrome; não identificam sozinhos a causa rara.',
 'Colher ADAMTS13 antes do plasma quando possível e tratar alta suspeita de PTT sem aguardar resultado.',
 'Troca plasmática e corticoide são urgentes; discutir cedo caplacizumabe e rituximabe conforme contexto.',
 'Transfusão de plaquetas não é rotina; avaliar exceções sem afirmar que uma transfusão causa inevitavelmente AVC.',
 'Recuperação de sintomas, hemograma e ADAMTS13 pode ocorrer em ritmos diferentes.'), so_kicker=True),

    pg('referencias', 'Fontes e limites',
 'Paciente, cronologia e percursos ficcionais. A indisponibilidade imediata de caplacizumabe é condição deste cenário, não afirmação sobre incorporação ou acesso atuais em todo o SUS. As escolhas de investigação infecciosa e cardíaca preservam tratamento e dados essenciais em todos os percursos.',
 'Revisão: <a href="https://pubmed.ncbi.nlm.nih.gov/40533296/">ISTH, atualização focada de 2025</a>, que mantém recomendações para PTT imune; <a href="https://pubmed.ncbi.nlm.nih.gov/37586700/">BSH, 2023</a>; ISTH, diagnóstico e tratamento, 2020; Cuker et al., definições de resposta, Blood 2021; Bendapudi et al., PLASMIC, 2017; Zini et al., ICSH, esquizócitos, 2021. Não se extrapola reposição de ADAMTS13 da doença congênita para esta apresentação imune.',
 'Imagens, setas preservadas, Wikimedia Commons: petéquias, James Heilman, CC BY-SA 4.0 (File:Petechia_lower_leg.jpg); TC, Mikael Häggström, CC0, recortada (File:CT_of_a_normal_brain,_axial_17.png); esfregaço, Osaro Erhabor, CC0, recortado (File:Schistocytes.jpg). Abertura: ilustração original da paciente ficcional, gerada com OpenAI imagegen para o projeto em 24/10/2026; não é fotografia clínica.')
]

REVISAO = []

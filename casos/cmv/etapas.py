"""Doença gastrointestinal por citomegalovírus após transplante renal.

Alíquota → pergunta, no molde dos casos interativos do //New England//. Oito
perguntas no percurso, uma rodada de exames com gabarito e painel, um
pareamento de histologia e três decisões de conduta, uma delas com
perfuração. Paciente ficcional; sem doses numéricas de antiviral — a
prescrição depende de depuração renal e protocolo do serviço.
"""
from pathlib import Path

from motor.etapas import (alt, bifurcacao, caminho, capa, desfecho, op, p,
                          pagina, painel, par, pareamento, pergunta, tabela,
                          topicos, vitais, lamina)
from casos.novos import imagem, referencia_imagem

TITULO = 'Depois da travessia'
RODAPE = 'Paciente ficcional · evoluções simuladas para ensino'
COR = '#ca8a04'
IMG = Path(__file__).parent / 'img'
BANCO = []
CENA = 'cena.png'


def pg(k, titulo, *textos, segue=''):
    return pagina(k, titulo, '', *(p(t) for t in textos), so_kicker=True, segue=segue)


def Q(k, n, enunciado, itens, titulo, segue=''):
    return pergunta(k, f'Pergunta {n}', enunciado,
                    [alt(t, c, certa=ok) for t, c, ok in itens],
                    titulo_resposta=titulo, segue=segue)


def ex(nome, valor, ref='—', alt_=False):
    return op(nome, resultado=valor, referencia=ref, alterado=alt_)


def fim(k, titulo, texto, porque, qualidade):
    return desfecho(k, titulo, p(texto), qualidade=qualidade, porque=porque,
                    fecho='retrospectiva')


def sem_setas(meta):
    return referencia_imagem(meta).replace('Setas editoriais sob a mesma licença; ', 'Sem setas; ')


ETAPAS = [
    capa(TITULO, fundo=CENA, kicker='Caso interativo',
         selo='Paciente ficcional · procedência e créditos na última tela'),

    pg('historia', 'Apresentação',
       'Helena, 58 anos, volta ao hospital por seis dias de diarreia e '
       'cansaço. Recebeu um transplante renal há quatro meses e vinha '
       'retomando as tarefas da casa. Há dois dias tem febre de até 38,4 °C e '
       'não consegue terminar as refeições.',
       'São seis a oito evacuações aquosas por dia, inclusive à noite, com '
       'cólica. Não viu sangue. A família acha que "algum remédio está '
       'irritando o intestino".'),

    pg('hda', 'História da doença atual',
       'No começo a diarreia vinha depois das refeições; agora persiste em '
       'jejum. Sem vômitos, sem dor sobre o enxerto, sem disúria, tosse ou '
       'falta de ar. Perdeu 2 kg na semana e notou que urina menos.',
       'Ninguém em casa está doente. Nega viagens, água não tratada ou '
       'comida suspeita. Recebeu **amoxicilina-clavulanato** por uma sinusite '
       'cinco semanas antes.'),

    pg('antecedentes', 'O transplante e as medicações',
       'Doença renal por diabetes e hipertensão, três anos de hemodiálise e '
       'transplante de doador falecido. Creatinina basal depois do '
       'transplante: 1,2 mg/dL. Sem rejeição documentada. **Doadora e '
       'receptora eram soropositivas para CMV.**',
       'Usa **tacrolimo, micofenolato mofetil e prednisona**, além de '
       'insulina, anlodipino e **sulfametoxazol-trimetoprima** como profilaxia '
       'de pneumocistose. O **valganciclovir profilático foi encerrado há '
       'quatro semanas**, no fim dos três meses previstos.'),

    pagina('exame', 'Exame físico', '',
           vitais(('Pressão arterial', '100/62', True), ('Frequência cardíaca', '108', True),
                  ('Frequência respiratória', '18', False), ('Temperatura', '38,2 °C', True),
                  ('SpO₂ em ar ambiente', '97%', False)),
           topicos(('Estado geral', 'Alerta, **mucosas secas**, enchimento capilar preservado.'),
                   ('Cardiopulmonar', 'Taquicardia regular, sem sopros; ausculta pulmonar normal.'),
                   ('Abdome', 'Dor difusa leve, **sem defesa ou descompressão**. Ruídos aumentados. '
                    'Enxerto na fossa ilíaca direita indolor.'),
                   ('Pele e neurologia', 'Sem exantema, sem déficit focal. Sem edema.')),
           so_kicker=True),

    Q('p1', 1,
      'Diarreia febril quatro meses depois de um transplante renal, quatro '
      'semanas após o fim da profilaxia antiviral. **Quais cinco** causas '
      'precisam ser consideradas?', [
      ('Doença gastrointestinal por CMV',
       'O fim da profilaxia é a hora do CMV: a doença de início tardio '
       'aparece nos meses seguintes à suspensão.', True),
      ('Rejeição aguda do enxerto',
       'Rejeição sobe a creatinina, mas não causa diarreia febril.', False),
      ('Colite por //Clostridioides difficile//',
       'Antibiótico há cinco semanas, imunossupressão e internações '
       'prévias: o risco é alto.', True),
      ('Síndrome do intestino irritável',
       'Não faz febre, nem diarreia noturna, nem perda de peso.', False),
      ('Toxicidade do micofenolato',
       'É a causa medicamentosa mais comum de diarreia no transplantado, e '
       'pode coexistir com infecção.', True),
      ('Norovírus crônico',
       'No imunossuprimido, o norovírus pode durar meses. O painel '
       'molecular o encontra.', True),
      ('Doença celíaca de início tardio',
       'Possível em qualquer idade, mas não explica febre e citopenias '
       'agudas.', False),
      ('Doença linfoproliferativa pós-transplante',
       'O linfoma associado ao EBV acomete o intestino e faz febre. Entra '
       'na lista até a endoscopia.', True),
      ('Insuficiência pancreática exócrina',
       'Esteatorreia crônica, sem febre.', False),
      ('Hipertireoidismo',
       'Diarreia sim, febre de 38 °C e citopenia, não.', False),
     ], 'Vírus, bactéria, droga — e o linfoma que o transplante permite'),

    Q('ex1', 2,
      'Na admissão, **quais cinco** exames são os mais apropriados?', [
      ('PCR quantitativa de CMV no plasma',
       'Replicação viral medida no mesmo ensaio, em unidades '
       'internacionais: é a base para diagnosticar e para acompanhar.',
       True),
      ('Sorologia IgM para CMV',
       'No transplantado, IgM não diagnostica doença ativa: falha em quem é '
       'soropositivo e aparece em reativações que não importam.', False),
      ('Teste para //C. difficile// nas fezes',
       'Obrigatório com antibiótico recente e diarreia de três ou mais '
       'evacuações por dia.', True),
      ('Biópsia do enxerto renal',
       'A creatinina subiu com desidratação. Primeiro corrige-se o volume; '
       'rejeição só se a disfunção persistir.', False),
      ('Nível sérico de tacrolimo',
       'Diarreia aumenta a absorção do tacrolimo, e o nível alto soma '
       'nefrotoxicidade à desidratação.', True),
      ('Colonoscopia antes de hidratar',
       'Preparo intestinal numa paciente depletada piora o rim. A endoscopia '
       'vem depois da estabilização.', False),
      ('Painel molecular gastrointestinal',
       'Norovírus, adenovírus, //Cryptosporidium//, //Giardia//: um só '
       'exame para os agentes que duram meses no imunossuprimido.', True),
      ('Hemograma e função renal',
       'Citopenia orienta mielotoxicidade e CMV; creatinina e potássio '
       'orientam volume e doses.', True),
      ('Tomografia de abdome com contraste iodado',
       'Sem peritonismo, não se expõe o enxerto a contraste na chegada.',
       False),
      ('Pesquisa de sangue oculto nas fezes',
       'Não muda nada numa diarreia febril aguda.', False),
     ], 'A equipe pede os cinco, e hemoculturas'),

    painel('res1', 'Na admissão', 'O que a equipe pediu', [
        ex('Hemoglobina', '10,1 g/dL', '12–16 g/dL', True),
        ex('Leucócitos', '2.100/mm³ · neutrófilos 1.200/mm³', '4.000–11.000/mm³', True),
        ex('Plaquetas', '112.000/mm³', '150.000–400.000/mm³', True),
        ex('Creatinina', '2,1 mg/dL {{(basal 1,2)}}', '0,6–1,1 mg/dL', True),
        ex('Potássio', '4,6 mmol/L', '3,5–5,0 mmol/L'),
        ex('AST / ALT', '62 / 71 U/L', 'até 35 / 35 U/L', True),
        ex('Tacrolimo, nível de vale', '14 ng/mL', 'alvo individual 5–8 ng/mL', True),
        ex('PCR de CMV no plasma', '18.600 UI/mL', 'não detectado', True),
        ex('//C. difficile//, toxina e PCR', 'Negativos', 'negativos'),
        ex('Painel molecular gastrointestinal', 'Nenhum agente detectado', 'negativo'),
        ex('Hemoculturas', 'Sem crescimento em 48 horas', 'negativas'),
    ], introducao='A equipe hidrata, ajusta o tacrolimo pelo nível e revê as medicações.'),

    Q('p3', 3,
      'PCR de CMV no plasma de **18.600 UI/mL**. Qual a interpretação mais '
      'adequada?', [
      ('Confirma doença gastrointestinal por CMV e dispensa endoscopia',
       'Mostra replicação no sangue, não localiza a doença. Colite por '
       'outra causa pode coexistir com viremia.', False),
      ('Replicação ativa; a doença intestinal exige tecido',
       'Doença gastrointestinal "comprovada" exige biópsia com efeito '
       'citopático ou imuno-histoquímica — e a viremia pode ser baixa ou '
       'ausente nela.', True),
      ('É latência, sem significado clínico',
       'Latência não produz DNA circulante nesse nível.', False),
      ('Carga abaixo de 50.000 UI/mL exclui doença invasiva',
       'Não existe limiar que exclua doença gastrointestinal: ela pode '
       'ocorrer com viremia baixa ou indetectável.', False),
      ('Deve ser repetida em outro laboratório antes de qualquer decisão',
       'O acompanhamento é feito no mesmo ensaio. Trocar de laboratório '
       'quebra a série.', False),
     ], 'Sangue mostra o vírus; tecido mostra a doença'),

    Q('p4', 4,
      'Leucopenia, neutropenia e plaquetopenia neste contexto. **Quais três** '
      'causas contribuem?', [
      ('O próprio CMV', 'Mielossupressão viral é parte da síndrome do CMV.',
       True),
      ('Micofenolato mofetil', 'Antiproliferativo: deprime a medula e é o '
       'primeiro a ser reduzido na infecção.', True),
      ('Sulfametoxazol-trimetoprima', 'O antifolato soma mielotoxicidade, '
       'sobretudo com o micofenolato.', True),
      ('Anlodipino em dose plena', 'Não é mielotóxico.', False),
      ('Prednisona de manutenção', 'Corticoide causa leucocitose por desmarginação, não '
       'leucopenia.', False),
      ('Insulina basal-bolus', 'Sem efeito medular.', False),
      ('Hiperesplenismo', 'Sem esplenomegalia nem hepatopatia.', False),
     ], 'Vírus, antiproliferativo e antifolato: a medula paga três contas'),

    pg('evolucao1', 'Depois da hidratação',
       'A pressão melhora e a creatinina cai para 1,6 mg/dL. O ultrassom do '
       'enxerto não mostra obstrução nem alteração vascular. O micofenolato '
       'é reduzido pela metade.',
       'A febre e a diarreia continuam: sete evacuações por dia, ingestão '
       'precária.'),

    bifurcacao('b1', 'Decisão', 'Febre, diarreia e viremia',
      'O que você faz agora?', [
      caminho('Ganciclovir endovenoso já, com endoscopia e biópsias após a '
              'estabilização', 'inicio_antiviral',
              'Absorção oral incerta com diarreia; a biópsia não precisa '
              'atrasar a primeira dose.'),
      caminho('Observar a resposta à redução do micofenolato antes do '
              'antiviral', 'atraso',
              'A toxicidade é possível, mas febre, viremia e fim da '
              'profilaxia apontam para CMV.'),
      caminho('Pulso de corticoide por possível rejeição', 'imunossupressao',
              'A creatinina subiu com desidratação e caiu com volume. '
              'Rejeição não foi demonstrada, e a infecção está ativa.'),
    ]),

    pg('atraso', 'Quatro dias de observação',
       'Oito evacuações por dia, agora com **estrias de sangue**. Creatinina '
       '2,3 mg/dL, albumina 2,7 g/dL. Sem defesa abdominal. A persistência '
       'depois da redução do micofenolato fala contra toxicidade isolada.',
       segue='resgate_atraso'),

    bifurcacao('resgate_atraso', 'Decisão', 'O que muda agora',
      'Qual a conduta?', [
      caminho('Iniciar ganciclovir e seguir com a endoscopia', 'inicio_antiviral',
              'Trata a hipótese de maior risco sem abandonar o diagnóstico.'),
      caminho('Esperar o laudo da biópsia antes do antiviral', 'piora_atraso',
              'O diagnóstico não exige manter a infecção sem tratamento.'),
    ]),

    pg('piora_atraso', 'Mais 48 horas',
       'Helena precisa de reposição venosa contínua e nutrição. Hemoglobina '
       '8,8 g/dL; a tomografia mostra colite extensa, sem ar livre. A equipe '
       'do transplante inicia o ganciclovir.',
       segue='inicio_antiviral'),

    pg('imunossupressao', '48 horas de pulso',
       'A febre chega a 39 °C, a diarreia aumenta e aparece sangue. A '
       'creatinina não cai. A tomografia mostra espessamento colônico, sem '
       'perfuração.',
       segue='resgate_corticoide'),

    bifurcacao('resgate_corticoide', 'Decisão', 'A piora sob corticoide',
      'Como prosseguir?', [
      caminho('Parar o pulso, iniciar ganciclovir e reavaliar o enxerto com a '
              'nefrologia', 'inicio_antiviral',
              'Tira a prioridade de uma rejeição não demonstrada sem suspender '
              'a imunossupressão de base.'),
      caminho('Completar o pulso e deixar o antiviral para depois da biópsia',
              'insistencia',
              'Mais imunossupressão sobre uma infecção invasiva em curso.'),
    ]),

    pg('insistencia', '72 horas depois',
       'Dor intensa no flanco esquerdo, defesa abdominal, pressão de 82/50 e '
       'lactato de 3,8 mmol/L. A tomografia mostra **ar extraluminal** junto '
       'ao cólon descendente.',
       'Ressuscitação, antibiótico para sepse abdominal, ganciclovir e '
       'cirurgia de urgência. A peça mostra colite ulcerada com perfuração e '
       'imuno-histoquímica positiva para CMV.',
       segue='f3'),

    pg('inicio_antiviral', 'Tratar enquanto se investiga',
       '**Ganciclovir endovenoso** começa hoje, com dose ajustada à '
       'depuração de creatinina e revista a cada mudança da função renal. A '
       'data da primeira dose passa a ser o D0.',
       'Transplante e infectologia mantêm o micofenolato reduzido, conferem '
       'o tacrolimo e o hemograma duas vezes por semana.'),

    pg('endoscopia', 'A colonoscopia',
       'Já estável e sem sinais peritoneais, Helena faz colonoscopia: '
       '**úlceras rasas, bem delimitadas, em cólon transverso e descendente**, '
       'com mucosa intermediária pouco alterada. São colhidas biópsias da '
       'borda e do fundo das úlceras.'),

    imagem('histologia_baixo', 'Biópsia do cólon: aumento intermediário',
           'Esta lâmina é de outro paciente com a mesma doença. Descreva a '
           'mucosa antes de procurar a célula que decide.',
           IMG / 'colon_baixo.jpg',
           'Mucosa colônica em hematoxilina-eosina · outro paciente.',
           sem_setas(IMG / 'colon_baixo.jpg.json'),
           ['Inflamação intensa da lâmina própria, com distorção e perda de '
            'criptas. Nesse aumento, procuram-se células grandes no estroma e '
            'no endotélio.',
            'A imagem não é imuno-histoquímica nem é de Helena.']),

    imagem('histologia_alto', 'Biópsia do cólon: grande aumento',
           'O mesmo diagnóstico em grande aumento. Que alteração celular '
           'aparece?',
           IMG / 'colon_alto.jpg',
           'Hematoxilina-eosina, grande aumento · outro paciente.',
           sem_setas(IMG / 'colon_alto.jpg.json'),
           ['Células muito aumentadas — citomegalia — com inclusão '
            'intranuclear grande e halo claro: o "olho de coruja". Pode '
            'haver inclusões citoplasmáticas menores.',
            'É o efeito citopático do CMV. A imuno-histoquímica, em outro '
            'preparo, confirma o antígeno.']),

    pareamento('p5', 'Pergunta 5',
      'Cada agente deixa uma marca na lâmina. Associe cada achado '
      'histológico ao diagnóstico.', [
      par('Células gigantes com inclusão intranuclear em "olho de coruja"',
          'Citomegalovírus',
          'Citomegalia no endotélio e no estroma, com inclusão rodeada de '
          'halo. É o laudo de Helena.'),
      par('Pseudomembranas com exsudato em "vulcão" saindo das criptas',
          '//Clostridioides difficile//',
          'Fibrina, neutrófilos e muco em jato. O teste de fezes dela foi '
          'negativo.'),
      par('Apoptose de criptas sem inclusões, em uso de micofenolato',
          'Colite pelo micofenolato',
          'Lembra doença enxerto-contra-hospedeiro. Pode coexistir com o '
          'CMV, e por isso a dose foi reduzida.'),
      par('Células multinucleadas com núcleos em vidro fosco e moldagem',
          'Herpes-simples',
          'Os três M: multinucleação, moldagem, marginação da cromatina. '
          'Mais no esôfago que no cólon.'),
      par('Infiltrado linfoide atípico com EBER positivo',
          'Doença linfoproliferativa pós-transplante',
          'Linfócitos B transformados pelo EBV. Muda tudo: redução da '
          'imunossupressão e rituximabe.'),
    ], opcoes=['Citomegalovírus', '//Clostridioides difficile//',
               'Colite pelo micofenolato', 'Herpes-simples',
               'Doença linfoproliferativa pós-transplante', 'Colite isquêmica'],
    titulo_resposta='Na lâmina, cada agente assina de um jeito',
    nota='A opção que sobrou, colite isquêmica, teria atrofia de criptas e '
         'hialinização da lâmina própria, sem inclusões.'),

    pg('confirmacao', 'O laudo de Helena',
       'Colite ulcerada com células citomegálicas e **imuno-histoquímica '
       'positiva para CMV**. Clínica e tecido fecham **doença '
       'gastrointestinal por CMV comprovada**.',
       'Todas as medidas seguintes usam plasma e o mesmo ensaio. O limite '
       'inferior de quantificação do laboratório é 137 UI/mL.'),

    painel('semana1', 'D7', 'A primeira semana', [
        ex('PCR de CMV no plasma, D0', '18.600 UI/mL', 'mesmo ensaio', True),
        ex('PCR de CMV no plasma, D7', '3.200 UI/mL', 'limite de quantificação 137 UI/mL', True),
        ex('Neutrófilos', '700/mm³', '1.500–7.500/mm³', True),
        ex('Creatinina', '1,4 mg/dL', 'basal 1,2 mg/dL'),
        ex('Evacuações', 'Quatro por dia, sem sangue · febre em resolução', '—'),
    ], introducao='A carga viral caiu mais de cinco vezes em uma semana.'),

    Q('p6', 6,
      'Quais **três** achados, se presentes, levantariam suspeita de '
      'resistência do CMV ao ganciclovir e justificariam genotipagem?', [
      ('Mais de seis semanas de ganciclovir',
       'A mutação em UL97 é selecionada por exposição prolongada, sobretudo '
       'com viremia persistente.', True),
      ('Carga viral inicial acima de 10.000 UI/mL',
       'Carga alta pede tratamento, não sugere resistência.', False),
      ('Carga que não cai após duas semanas',
       'Na primeira semana a carga pode subir por cinética; depois de duas '
       'semanas de dose e absorção adequadas, não deveria.', True),
      ('Neutropenia surgindo durante o tratamento',
       'É toxicidade, não resistência.', False),
      ('Doadora soropositiva e receptora soronegativa',
       'Ausência de imunidade prévia é o principal fator de risco para '
       'resistência.', True),
      ('Recorrência depois de parar o tratamento antes do limiar',
       'Isso é interrupção precoce, não resistência. Reinicia-se o mesmo '
       'fármaco.', False),
      ('Diarreia persistente na primeira semana',
       'O intestino cicatriza mais devagar que a carga cai.', False),
     ], 'Exposição longa, resposta ruim depois de duas semanas, e receptor sem imunidade'),

    pergunta('p7', 'Pergunta 7',
      'Neutrófilos de 700/mm³ no D7, com clínica e carga viral melhorando. '
      'Qual o próximo passo?', [
      alt('Reduzir a dose do ganciclovir para poupar a medula',
          'Subdose seleciona resistência. Ajusta-se a dose à função renal, '
          'não à contagem.'),
      alt('Trocar imediatamente para foscarnet',
          'Nefrotóxico e com distúrbio eletrolítico. É a alternativa quando '
          'a mielotoxicidade é grave e refratária ou há resistência.'),
      alt('Tirar mielotóxicos e manter o antiviral',
          'Suspender o micofenolato temporariamente e trocar a profilaxia de '
          'pneumocistose por atovaquona mantém o antiviral eficaz.',
          certa=True),
      alt('Pausar o antiviral até os neutrófilos normalizarem',
          'Resposta parcial não autoriza interrupção: a doença invasiva está '
          'no meio do tratamento.'),
      alt('Iniciar letermovir em dose de tratamento',
          'O letermovir é aprovado para profilaxia, não para tratar doença '
          'estabelecida.'),
    ], titulo_resposta='Proteger a medula sem enfraquecer o antiviral'),

    pg('evolucao2', 'D14',
       'Sem o micofenolato e com a profilaxia trocada, os neutrófilos sobem '
       'para 1.400/mm³. Creatinina 1,3 mg/dL. Afebril, uma a duas evacuações '
       'formadas por dia, comendo bem.',
       'A PCR de CMV do D14 é **620 UI/mL** — ainda quantificável.'),

    pergunta('p8', 'Pergunta 8',
      'Clínica resolvida, absorção confiável e carga de 620 UI/mL no D14. '
      'Qual a conduta sobre o antiviral?', [
      alt('Valganciclovir oral em dose de tratamento',
          'Melhora clínica e absorção confiável permitem a via oral. A dose '
          'continua sendo de tratamento.', certa=True),
      alt('Manter endovenoso até a carga ficar indetectável',
          'Indetectável não é requisito para trocar a via; a internação '
          'prolongada tem riscos próprios.'),
      alt('Trocar para valganciclovir em dose de profilaxia',
          'Via e intensidade são decisões diferentes. A carga ainda está '
          'acima do limiar de término.'),
      alt('Encerrar hoje: completou os 14 dias mínimos',
          'O término exige três coisas juntas: clínica resolvida, duas '
          'semanas no mínimo e carga abaixo do limite de quantificação.'),
      alt('Trocar para maribavir, pela carga persistente',
          'Reservado para doença refratária ou resistente — o que a queda '
          'contínua da carga desmente.'),
    ], titulo_resposta='Via oral sim; dose de profilaxia, não'),

    bifurcacao('b2', 'Decisão', 'O fim do tratamento',
      'D14, sintomas resolvidos e carga de 620 UI/mL. Como seguir?', [
      caminho('Valganciclovir oral em dose de tratamento, com nova carga em '
              'uma semana', 'resposta',
              'Cumpre as duas semanas mínimas e espera o limiar virológico.'),
      caminho('Encerrar agora e manter só vigilância', 'recaida',
              'O mínimo de duração não basta com a carga acima do limiar.'),
    ]),

    pg('resposta', 'D21',
       'Série semanal: 18.600 → 3.200 → 620 → **abaixo de 137 UI/mL**. '
       'Assintomática, comendo, hemograma em recuperação.',
       'Encerra-se o tratamento com clínica resolvida, mais de duas semanas '
       'de terapia e uma amostra abaixo do limite de quantificação de um '
       'ensaio altamente sensível. A vigilância semanal segue por oito '
       'semanas.',
       segue='f1'),

    pg('recaida', 'D28',
       'Duas semanas depois de parar, voltam a febre e seis evacuações '
       'líquidas por dia. Carga de CMV **9.800 UI/mL**, creatinina 1,8 mg/dL.',
       'O tratamento foi interrompido com 620 UI/mL. A queda foi contínua '
       'enquanto ele durou — o padrão é de interrupção precoce, não de '
       'resistência.',
       segue='resgate_recaida'),

    bifurcacao('resgate_recaida', 'Decisão', 'A recorrência',
      'Como abordar?', [
      caminho('Reiniciar ganciclovir e revisar dose, absorção e outras causas',
              'retratamento', 'A interrupção precoce explica a volta.'),
      caminho('Trocar para foscarnet e pedir genotipagem por suspeita de '
              'resistência', 'revisao_resistencia',
              'Resistência é hipótese, mas a curva durante o tratamento não '
              'a sustenta.'),
    ]),

    pg('revisao_resistencia', 'Antes da troca',
       'A infectologia revê a série: queda contínua sob tratamento e '
       'interrupção acima do limiar. Menos de seis semanas de exposição. A '
       'troca reflexa para foscarnet é suspensa pelo risco renal.',
       segue='retratamento'),

    pg('retratamento', 'Novo curso',
       'Ganciclovir endovenoso, depois valganciclovir em dose de tratamento. '
       'Carga semanal: 9.800 → 1.700 → 280 → abaixo de 137 UI/mL. Encerra-se '
       'no D21 do novo curso.',
       segue='f2'),

    fim('f1', 'Retorno ao ambulatório',
        'Helena mantém alimentação, função do enxerto próxima da basal e '
        'hemograma em recuperação. O micofenolato volta em dose menor.',
        'Tratar sem esperar a biópsia, proteger a medula sem subdose e '
        'encerrar só no limiar virológico foram as três decisões que '
        'contaram.', 'melhor'),

    fim('f2', 'Recuperação depois da reinternação',
        'A infecção é controlada e a função renal volta perto da basal, '
        'com uma reinternação de três semanas.',
        'O término no mínimo de dias, com a carga ainda quantificável, deu '
        'a recorrência. O resgate funcionou sem presumir resistência.',
        'medio'),

    fim('f3', 'Perfuração e diálise',
        'Depois da colectomia parcial e do controle da sepse, Helena segue '
        'internada, dependente de diálise por lesão renal aguda. A '
        'recuperação do enxerto é incerta.',
        'O corticoide dado para uma rejeição não demonstrada, sobre uma '
        'colite por CMV sem tratamento, contribuiu para um desfecho grave '
        'que o antiviral precoce provavelmente teria evitado.', 'pior'),

    pagina('retrospectiva', 'Retrospectiva', '',
        tabela(['Momento', 'O dado', 'O que decidiu'], [
            ['Admissão', 'Diarreia febril um mês depois do fim da profilaxia',
             'CMV, //C. difficile//, micofenolato, norovírus e linfoma na mesma lista'],
            ['Laboratório', 'Carga de 18.600 UI/mL, citopenias, tacrolimo alto',
             'Replicação ativa; o tecido é que comprova doença intestinal'],
            ['Decisão', 'Febre e ingestão precária', 'Antiviral antes da biópsia, não depois'],
            ['D7', 'Neutrófilos de 700', 'Tirar os mielotóxicos, não baixar o antiviral'],
            ['D14', 'Carga de 620 UI/mL', 'Via oral em dose de tratamento até o limiar'],
        ]),
        so_kicker=True),

    pg('referencias', 'Fontes e limites',
       'Paciente, séries laboratoriais e percursos são ficcionais. Não há '
       'doses numéricas: a prescrição depende de depuração renal e do '
       'protocolo do serviço.',
       'Kotton e cols. Fourth International Consensus Guidelines on the '
       'Management of Cytomegalovirus in Solid Organ Transplantation, 2025. '
       'Histologia de outros pacientes: Nephron, Wikimedia Commons, CC BY-SA '
       '3.0. Cena: ilustração gerada por IA.'),
]

REVISAO = []

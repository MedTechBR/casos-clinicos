"""Painéis da visita clínica: consolidação de resultados já obtidos pela equipe."""
from motor.etapas import pagina, p, tabela
from motor.estudo_imagem import inserir_antes

def aplicar(etapas, caso):
    dados={
      'pulmao_rim':('p5', 'Evolução laboratorial',
        'Na reavaliação, a equipe coloca lado a lado os resultados do ambulatório e da admissão. A comparação antecede a discussão dos mecanismos possíveis.',
        ['Exame','Ambulatório','Admissão','Referência'],[
          ['Hemoglobina','11,2 g/dL','7,8 g/dL','13,5–17,5 g/dL'],
          ['Leucócitos','9.800/mm³','14.200/mm³','4.000–11.000/mm³'],
          ['Plaquetas','431.000/mm³','468.000/mm³','150.000–400.000/mm³'],
          ['Creatinina','1,4 mg/dL','3,8 mg/dL','Até 1,3 mg/dL'],
          ['Proteína C reativa','62 mg/L','186 mg/L','Até 5 mg/L'],
        ]),
      'west_nile':('b2', 'Exames durante a internação',
        'Antes de discutir o suporte respiratório, a equipe revê os resultados já obtidos. Os dados do sangue e do líquor são considerados junto do exame motor e da capacidade de proteger a via aérea.',
        ['Exame','Resultado','Referência'],[
          ['Sódio sérico','131 mmol/L','135–145 mmol/L'],
          ['Potássio sérico','4,1 mmol/L','3,5–5,0 mmol/L'],
          ['Creatinina sérica','1,1 mg/dL','0,7–1,3 mg/dL'],
          ['Células no líquor','86/mm³; 58% neutrófilos','Até 5/mm³'],
          ['Proteína no líquor','92 mg/dL','15–45 mg/dL'],
          ['Glicose no líquor / sangue pareado','68 / 120 mg/dL','Relação >0,4'],
        ]),
      'cocaina_levamisol':('q6', 'Evolução laboratorial',
        'Na visita, a equipe compara as coletas da internação. Esses resultados acompanham a reavaliação das lesões, da urina e do risco infeccioso antes de definir o tratamento.',
        ['Exame','Inicial','Controle atual','Referência'],[
          ['Neutrófilos absolutos','180/µL','420/µL','1.500–7.500/µL'],
          ['Hemoglobina','12,1 g/dL','11,7 g/dL','12–16 g/dL'],
          ['Plaquetas','238.000/µL','226.000/µL','150.000–450.000/µL'],
          ['Creatinina','0,9 mg/dL','2,6 mg/dL','0,6–1,1 mg/dL'],
          ['Proteína/creatinina urinária','Não quantificada','1,2 g/g','<0,2 g/g'],
        ]),
    }
    destino,titulo,contexto,colunas,linhas=dados[caso]
    nova=pagina('painel_evolucao_equipe',titulo,'','<div class="painel-lab">'+p(contexto)+tabela(colunas,linhas)+'</div>',so_kicker=True,segue=destino)
    inserir_antes(etapas,destino,[nova])

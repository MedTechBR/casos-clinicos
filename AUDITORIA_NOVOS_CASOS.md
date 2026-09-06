# Dois casos — 6 de setembro de 2026

## Imagens

As capas de **À flor da pele** e **O peso dos dias** foram inspecionadas de forma independente por Avicenna e Bacon. Os dois aceitaram ambas: aparência plausível para as idades propostas, ausência de erros anatômicos grosseiros e de sinais diagnósticos inequívocos. O martelo de reflexos na cena masculina sugere exame neurológico, sem identificar etiologia. As imagens não documentam achados clínicos e são creditadas como geradas por IA.

## Narrativa

A auditoria de O peso dos dias identificou resultado final precoce de hemocultura, uma descrição redundante de perda de força e antecipação da resposta de uma bifurcação pela questão anterior. Corrigidos: cultura em processamento, progressão para contração sem movimento e explicação respiratória posterior à escolha de suporte.

As perguntas de À flor da pele que interpretam hemograma e dupla positividade de anticorpos passam apenas pelos percursos em que os respectivos exames foram solicitados. As decisões permitem resgate e investigação incompleta. A suspeita de participação do levamisol não é apresentada como confirmação.

## Verificação reproduzível

`python3 ferramentas/testar_novos_casos.py` verifica destinos, percorre combinações de conduta com painéis completos e mínimos, testa teto de quatro exames, número de resultados retornados, ausência de erros de JavaScript e legibilidade das alternativas a 1600 × 900. Resultados locais são gravados em `saida/revisao/novos-casos-qa.json`.

Os ramos são cenários didáticos ficcionais. Não representam prognóstico individual ou estimativas de efeito causal das condutas.

A revisão final de À flor da pele encontrou início de antibiótico pouco explícito nos ramos de resgate e referente ambíguo em uma alternativa de toxicologia. Ambos corrigidos.

Teste completo: 72 percursos de O peso dos dias e 24 de À flor da pele, cobrindo os sete desfechos; nenhum erro JS ou corte de alternativas a 1600 × 900. Todas as perguntas também verificadas a 1366 × 768. Biblioteca com três links funcionais; ampliação das duas cenas verificada por clique e fechamento com Escape.

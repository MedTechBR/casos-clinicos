# Investigação por etapas e coerência da amostragem — 24/10/2026

## Escopo

Revisados os 13 casos. Alterada a sequência de investigação de 12, preservando layout, imagens, personagens e tratamentos urgentes. O caso de cocaína manteve o painel inicial: hemograma diferencial, coagulação e culturas são pertinentes já na entrada com febre e lesões necróticas. A regra não é proibir exames específicos precoces quando a apresentação já os justifica.

Os resultados de rotina precedem a reavaliação que justifica exames dirigidos. Exemplos: citopenias justificam avaliação hematológica/autoimune em Bianca; hiponatremia justifica estudos urinários no caso neurológico; hipercalcemia justifica cálcio ionizado e PTH em Rafael; dor torácica e congestão justificam avaliação cardíaca imediata. A separação editorial não impõe espera clínica. Antibióticos, estabilização, coleta urgente e investigação de condições graves continuam em paralelo.

Retiradas interpretações que antecipavam hipóteses nos laudos iniciais. As descrições permanecem nos exames; o raciocínio e os limites diagnósticos ficam nas explicações após as respostas. A revisão não pretende eliminar todo indício clínico: achados reais devem permitir inferências pelos residentes.

## Rafael: procedimentos diferentes

- Mediastinoscopia direta: biópsia de linfonodo paratraqueal, arquitetura preservada e resultado do material cirúrgico; não passa por EBUS.
- EBUS inicialmente insuficiente: exige nova decisão de coleta, mantendo acompanhamento clínico da hipercalcemia.
- Nova EBUS: melhora técnica com avaliação da adequação e material representativo.
- Alternativa após EBUS insuficiente: mediastinoscopia com seu próprio resultado.

Os percursos convergem após obtenção adequada de tecido. Não se afirma que possuem finais diferentes: a diferença aqui é o procedimento, a suficiência da amostra e a necessidade de nova decisão. A insuficiência do primeiro material é um evento deste paciente ficcional, não uma punição inevitável pela escolha de EBUS, que é uma via inicial geralmente preferida. Cultura pendente e resultados negativos não excluem automaticamente todas as infecções; granuloma não determina sozinho a etiologia.

## Referências consultadas

- [Endotext — Approach to Hypercalcemia](https://www.ncbi.nlm.nih.gov/books/NBK279129/): PTH orienta a classificação etiológica após confirmação de hipercalcemia; tratamento depende também de sintomas e repercussões.
- [ATS 2020 — Diagnosis and Detection of Sarcoidosis](https://pmc.ncbi.nlm.nih.gov/articles/PMC7159433/): EBUS versus mediastinoscopia, limites de rendimento e integração de clínica, histologia e exclusão de alternativas.

Auditoria independente de Rafael: aprovada, 37 nós e três percursos de amostragem válidos, sem destinos ausentes ou ciclos. Nenhum bloqueador clínico identificado no escopo da revisão.

## Verificação

Build individual dos 13 casos e reconstrução da biblioteca. Teste dedicado de regressão em `ferramentas/testar_sarco_rotas.py` verifica os destinos reais das três rotas. A suíte de todas as telas inclui desktop e celular, resultados revelados e respostas; a suíte de perguntas verifica limite de seleção e explicações. Resultados consolidados registrados após a execução abaixo.

- Todas as telas: **4.028 páginas/estados**, sem transbordamento, em 1366×768, 1600×900 e 375×812.
- Perguntas: **296 estados de seleção/resposta**, 148 instâncias em dois tamanhos de tela, incluindo 92 de multisseleção; sem falhas de limite ou explicação.
- Regressão da amostragem: as três rotas retornam o procedimento escolhido, com convergência apenas após material adequado.

A primeira passagem completa de navegação dos 13 casos terminou com todos os nós alcançados, sem falhas de JavaScript, destinos, imagens ou layout. Após essa passagem, o pedido adicional de linguagem simples e exames acessíveis motivou uma segunda rodada de alterações e nova verificação, descritas em `linguagem-e-acesso-2026-10-24.md`.

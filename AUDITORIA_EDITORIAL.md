# Revisão editorial e visual — três casos

## Alterações

- Biblioteca redesenhada com busca, três casos ativos e catálogo futuro recolhido.
- Estilo compartilhado das apresentações: tipografia maior, contraste, imagens sem sobreposição ao texto, perguntas inteiras nas telas de desktop verificadas e retorno à biblioteca.
- HDA, antecedentes, medicamentos e contexto social ampliados nos dois casos novos. Exame do primeiro caso dividido em duas páginas para preservar a legibilidade.
- Cinco novas figuras abertas, em seis páginas de discussão: medula, neurônio, alvéolo, corpúsculo renal (dois casos) e púrpura comparativa. Comentários revelados por clique e ampliação disponíveis. Créditos nos arquivos de cada caso.

## Auditorias independentes

Os dois revisores de imagens aprovaram todas as cinco figuras para os usos delimitados nas seis discussões. Os esquemas representam anatomia normal; a fotografia de púrpura pertence a outro paciente. Nenhuma figura foi apresentada como exame do paciente ficcional.

A revisão narrativa encontrou antecipação da resposta pela discussão medular. Corrigido e reconferido: reexame → pergunta p2 → discussão anatômica → decisão b1. Nenhum bloqueador adicional nas narrativas novas.

A revisão visual aprovou biblioteca, história, exame e três telas de perguntas em 1366×768, limitada aos estados capturados. Sem sobreposição ou corte nos screenshots examinados.

## Verificações executadas

- Dois casos novos: 96 combinações de decisões e seleção ampla/mínima de exames, sem erros JS ou perguntas cortadas; smoke de oito percursos após mudar a posição da discussão medular.
- Caso original: 54 percursos, 59 etapas visitadas e quatro desfechos, sem erros JS ou perguntas cortadas. Total: 150 percursos entre os três casos.
- Biblioteca: busca, ausência de resultados, três links ativos e retorno a partir das apresentações.
- Todas as páginas: imagens carregadas; seis discussões inicialmente fechadas, abertura por clique e ampliação com fechamento por Escape.
- 1600×900, 1366×768 e 375×812: navegação e confirmação acessíveis. Em desktop as alternativas cabem sem rolar; em celular listas longas permitem rolagem.
- Conteúdo fechado das páginas em 1600×900: sem transbordamento dos painéis principais.

Os testes não representam validação clínica externa de cada decisão ou prognóstico simulado. Os desfechos permanecem autorais para ensino.

## Ampliação dos casos e exames contextualizados

- Conteúdo passou de 59/44/43 para 67/51/52 etapas autoradas (pulmão-rim/West Nile/cocaína), acrescentando 24 páginas. Cada percurso visita apenas suas páginas; a contagem não corresponde a uma sessão única.
- Todas as nove rodadas de pedidos agora apresentam um problema clínico interrogativo, com os mesmos limites de seleção.
- Sete novas inserções radiológicas: RX nos dois casos novos, TC de crânio e RM de encéfalo no painel neurológico, ultrassom no painel renal, RX e TC comparativos no caso original. Quatro arquivos inéditos no acervo e três reutilizações de figuras existentes.
- Laudos permanecem optativos, agora com estado separado por rodada: ler um RX anterior não abre o seguinte. Painéis com uma ou duas imagens aproveitam melhor a largura disponível.
- Dois auditores independentes aceitaram as seis figuras distintas para os usos delimitados. Figuras são de outros pacientes; cortes de TC/RM e US não representam estudos completos. As fontes e licenças estão nos CREDITOS.md de cada caso.
- Auditoria estática de narrativa e transições: sem bloqueador novo; sedação, intubação e pré-altas compatíveis com os percursos que as alcançam. Não equivale à revisão de todo o conteúdo clínico preexistente.
- 150 percursos novamente executados: 54 no original, 72 West Nile e 24 cocaína, sem erro JS ou perguntas cortadas. A questão condicional de dupla positividade na cocaína também foi renderizada diretamente, embora não apareça nas combinações padrão.
- Teste específico de imagens: somente pedidos selecionados retornam; laudos inicialmente ocultos; revelação e lupa funcionam, inclusive RX repetido em rodadas distintas.
- Interface verificada em 1600×900, 1366×768 e 375×812. Catálogos longos usam rolagem; alternativas das perguntas em desktop permanecem inteiras.

## 7 de setembro — exames na evolução e respostas

- Doze páginas novas, em seis pares: observação sem interpretação, depois leitura com setas. Um par de ECG por caso; adicionalmente RX na piora respiratória, TC após déficit focal e US na investigação urinária. O mesmo ECG aberto é comparativo nos três roteiros, com identificação explícita de outro paciente.
- A equipe pode solicitar esses exames na narrativa, conforme nova orientação do autor. TC e US migrados para a evolução foram retirados dos respectivos catálogos para não consumir uma escolha redundante. Os painéis continuam exibindo somente os exames selecionados.
- Dois auditores independentes (Godel e Carver) aceitaram RX, TC e US. Houve divergência na seta inicialmente atribuída à onda P; essa marcação foi substituída por dois QRS consecutivos, sem nomear P nas setas. Ambos aceitaram o ECG revisado. Originais, SVGs, capturas e grade de coordenadas conferidos. Licenças e limites em `casos/*/img/CREDITOS.md`.
- Marcadores de alternativa não usam mais pseudo-rótulos “certa/sua”; o resultado aparece junto ao comentário. Ampliação de SVG corrigida: a figura ocupa a lupa em vez de encolher ao tamanho intrínseco.
- Testes: 54 percursos principais + 72 West + 24 cocaína, todos com finais alcançados e zero erro JavaScript. 19 perguntas confirmadas em 1600×900, 1366×768 e 375×812 sem sobreposição do marcador/comentário. Seis pares testados para ordem, ausência de setas iniciais, leitura seguinte, voltar, lupa e ganho de tamanho. Questões extensas podem rolar após a confirmação; alternativas antes de confirmar continuam sem corte nos desktops testados.
- Totais autorais: 71/55/56 páginas, incluindo ramos alternativos. Nenhum percurso individual contém necessariamente todas elas.

## 8 de setembro — conferência das setas e fim da rolagem

Reabertura das imagens originais, exame da ponta efetiva dos SVGs e revisão independente de Carver. As tentativas adicionais de revisão tiveram erro de limite do serviço e não produziram novos pareceres; não são contadas como aprovação.

- Removido o quarto marcador da histologia, anteriormente chamado de “glomérulo esclerosado”, por identificação não sustentada. Três estruturas mantidas e novamente conferidas: tufo, cápsula e crescente. Numeração curta na imagem e explicação ao lado; contagem de glomérulos e imunofluorescência ficcionais em página separada. Retiradas afirmações absolutas de reversibilidade.
- ECG, RX, TC e US: alvos mantidos após reconferência. Corrigida a legenda dos asteriscos no US antigo, adicionada chave completa do corpúsculo renal, retirado o esquema alveolar com rótulo anatômico inadequado e usado fundo branco para os diagramas na lupa.
- Novo paginador mede os blocos reais e distribui conteúdo excedente entre páginas, sem zoom tipográfico ou exclusão de informação. Seleção de exames e limite persistem. Resultados abertos levam à página do laudo; comentários, tabelas, exame físico e revisão final também são paginados quando necessário. Fontes mantidas. A biblioteca aponta explicitamente para esta versão dos arquivos.
- Verificação automatizada de 1.411 páginas/estados em 1366×768, 1600×900 e 375×812: nenhum transbordamento vertical/horizontal das áreas de leitura. Catálogos conservam todas as opções, cada bloco pertence a uma página, navegação preserva marcações e discussão pode abrir/fechar. A paginação usa os botões Avançar/Voltar e mostra “Página X de Y”.

Validação complementar: 54 percursos principais e 96 percursos dos outros casos na revisão de navegação; verificação final de quatro percursos principais após incluir a paginação da revisão de encerramento. Testes de biblioteca, lupa, perguntas, laudos optativos e interface passaram nos três viewports. Corrigida também a repaginação síncrona ao abrir discussão, evitando que uma atualização tardia devolvesse o usuário à primeira página.

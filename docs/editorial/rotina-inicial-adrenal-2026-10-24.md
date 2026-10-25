# Rotina inicial — adrenal, PTT e feocromocitoma

24/10/2026. Ajuste pontual dos primeiros painéis e da ligação achado → reavaliação → exame dirigido. Sem reformulação integral, mudança de motor/layout, capas ou discussão diagnóstica final. IDs anteriores de nós e bifurcações preservados. Dados da história continuam disponíveis desde a apresentação, sem nomes dos diagnósticos raros na abertura.

## Adrenal

- Primeiro painel mantém hemograma, glicemia, função renal, eletrólitos e bioquímica geral. Gasometria/lactato permanecem precoces pela hipoperfusão; urina integra a avaliação renal.
- Osmolalidades e eletrólitos urinários saem do painel inicial. A resposta incompleta ao primeiro litro, com Na 124 e K 6,1, justifica a solicitação e antecede o painel novo `res_sodio`. Os valores anteriores à salina vêm de amostras iniciais já disponíveis no laboratório; não se espera nova coleta para ressuscitar.
- Removida FENa, sem dependências posteriores. Mantidos os eletrólitos urinários usados no cálculo do gap da explicação, agora explícito.
- Cortisol/ACTH pré-hidrocortisona e tratamento imediato continuam na primeira hora, sem depender da conclusão dos estudos urinários.
- Comentário antecipado do ECG ficou descritivo; a interpretação com consequência terapêutica continua em `primeira_resposta`.

## PTT

- Primeiro painel passa a reunir hemograma, função renal, PCR e urina pela pigmentúria. Reticulócitos e revisão inicial da lâmina passam para o painel dirigido de anemia.
- Após os resultados básicos, `reavaliacao_inicial` mostra recuperação transitória da fala, cansaço persistente e pigmentúria; anemia, queda plaquetária e discrepância fita/sedimento justificam investigar hemólise. A pergunta mantém seleção limitada e resultados independentes de acerto.
- A reavaliação com febre/sonolência antecede coagulação e avaliação de órgãos. Ceftriaxona empírica não espera líquor. TC segue indicada precocemente pelo déficit transitório; ADAMTS13 continua pré-plasma e troca/corticoide não aguardam confirmação.
- Explicações de mecanismo da púrpura e limites da TC saem dos laudos anteriores às perguntas e permanecem nas explicações de `p1`/`p2`. Descrições e achados das imagens foram preservados.

## Feocromocitoma

- Hemograma, glicemia, eletrólitos e função renal/bioquímica ficam no painel básico. Novo painel `res1b` separa troponina/gasometria, cuja indicação já existe na chegada pela dor torácica e congestão.
- `reavaliacao_inicial` explicita essa indicação e a persistência clínica durante o controle da pressão. A separação editorial não cria espera: ECG e primeira troponina são imediatos, em paralelo à rotina; a troponina seriada conclui-se em três horas.
- O traçado ilustrado continua sendo o controle da segunda hora, e a síntese agora ocorre após a série de três horas. A discussão de sobrecarga anterior foi deslocada do comentário da imagem para a reavaliação clínica.
- Investigação metabólica/endócrina do segundo dia tem justificativas explícitas após estabilização. Removido NT-proBNP, sem uso posterior. Metanefrinas continuam após a apresentação e recorrência que as justificam; não foram antecipadas à abertura.

## Fontes e verificação

Não foram alteradas doses ou regimes terapêuticos. Rechecadas as exceções de urgência em fontes primárias/institucionais:

- [Society for Endocrinology — crise adrenal](https://www.endocrinology.org/clinical-practice/clinical-guidance/adrenal-crisis/): investigação não atrasa hidrocortisona.
- [ISTH — diagnóstico da PTT, 2020](https://pmc.ncbi.nlm.nih.gov/articles/PMC8146131/) e [atualização 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC13470878/): amostra pré-terapia e tratamento urgente na alta suspeita; a atualização mantém as recomendações da doença imune.
- [ESC — síndromes coronarianas agudas, 2023](https://academic.oup.com/eurheartj/article/44/38/3720/7243210): ECG imediato e troponina inicial/seriada, sem esperar pela rotina geral.

Compilação em memória e importação individual aprovadas: 111 nós (36 adrenal, 36 PTT, 39 feocromocitoma), 10 percursos (2/4/4). Sem IDs duplicados, destino ausente, ciclo ou nó inacessível. Tetos e gabaritos preservados; nenhum pedido livre introduzido. Todos os percursos recebem os painéis necessários e chegam às referências; conferida a ordem das coletas urgentes e tratamentos. FENa e NT-proBNP não têm referências residuais nos casos.

Sem build global, comandos Git ou teste grande de UI. Pendência concreta: conferir a paginação dos novos trechos no teste visual consolidado. SAR não foi examinado nem alterado nesta frente.

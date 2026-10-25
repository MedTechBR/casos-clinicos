# Rotina inicial e investigação dirigida — 24/10/2026

Revisão pontual de `casos/kikuchi/etapas.py`, `casos/leptospirose/etapas.py` e `casos/paracoco/etapas.py`. Preservados personagens, capas, imagens, marcações, diagnósticos e IDs das decisões existentes. Sem alteração de layout/motor, build global ou operações Git.

## O que mudou

| Caso | Entrada | Reavaliação e complementação |
|---|---|---|
| Bianca | Hemograma, PCR, creatinina e urina | Novo `reexame_inicial`: febre e desconforto persistem, sem instabilidade; anemia e leucopenia justificam esfregaço, LDH, transaminases e investigação infecciosa/autoimune. `complemento_hematologico` entrega os resultados antes das etapas que os utilizam. FAN/C3/C4 e investigação de hemólise continuam precoces, na mesma etapa de atendimento, com resultados no retorno já previsto. |
| Paciente de O sexto dia | Hemograma, glicemia, função renal, eletrólitos e urina; gasometria/lactato precoces pela hipoxemia/hipotensão | O suporte não é adiado. Após melhora inicial da pressão, persistem icterícia, oligúria e mialgia: justificam bilirrubinas/enzimas hepáticas, CK e eletrólitos urinários. Novo `investigacao_dirigida` entrega tudo nas primeiras horas, antes da interpretação renal. Culturas pré-antibiótico, amostra de sangue precoce, investigação etiológica e antibiótico mantidos. |
| Valdir | Hemograma, PCR, glicemia, renal, eletrólitos e urina | Novo `reavaliacao_basica`: limitação ao caminhar e saturação repetida de 93% justificam gasometria/radiografia; emagrecimento, doença respiratória e mucosas justificam HIV e complementação sistêmica/nutricional. `avaliacao_dirigida` contém gasometria, HIV, proteínas e enzimas hepáticas. Avaliação adrenal continua antecipada quando surgem ortostatismo e alterações eletrolíticas, sem esperar confirmar a micose. |

VHS redundante retirado dos dois casos em que aparecia junto à PCR; fosfatase alcalina/GGT normais e VDRL sem pergunta clínica explícita retirados de Bianca; ECG normal sem dependência posterior retirado de Valdir. Não foram removidos dados necessários a perguntas ou explicações posteriores. Não se inseriu uma espera artificial entre exames urgentes: separação editorial não significa coleta obrigatoriamente em dias diferentes.

## Laudos iniciais sem antecipar o diferencial

- Bianca: ultrassom e radiografia descrevem forma, hilo, fluxo e dimensões/contornos visíveis. A interpretação de aspecto reacional e os limites para excluir doença ficam nos comentários após a decisão `b_inicial`.
- O sexto dia: radiografia inicial descreve a consolidação; associação com pneumonia e necessidade de ampliar a hipótese ficam na explicação de `p_etiologias`. Ultrassom descreve estruturas e ausência de dilatação/cálculos, sem declarar a etiologia hepática ou renal; interpretação contextual permanece na discussão e na questão renal.
- Valdir: laudos de radiografia e lesões já eram descritivos, portanto foram mantidos. O diferencial permanece nas explicações, sem apagar diagnóstico ou discussão posteriores.

## Fontes e limites

Não houve mudança de esquema terapêutico. Conferidos em 24/10/2026: [CDC Yellow Book 2026, leptospirose, atualização de 2025](https://www.cdc.gov/yellow-book/hcp/travel-associated-infections-diseases/leptospirosis.html), para tratamento sem aguardar confirmação e escolha da amostra por fase; [Endocrine Society, insuficiência adrenal primária, diretriz de 2016](https://www.endocrine.org/clinical-practice-guidelines/primary-adrenal-insufficiency), para investigação dirigida e tratamento imediato da crise, sem esperar teste; [ARUP — LES](https://arupconsult.com/content/systemic-lupus-erythematosus) e [ARUP — hemólise](https://arupconsult.com/content/hemolytic-anemias), para manter avaliação paralela das citopenias e não equiparar LDH isolada a hemólise. A diretriz endócrina é identificada pela data original, não apresentada como publicação nova. Fontes primárias e diretrizes das reformulações anteriores permanecem nos casos e no documento de expansão.

Os novos textos descrevem reavaliações com os dados já conhecidos, sem criar choque, novo órgão acometido ou demora necessária para justificar um exame. A escolha e o ritmo dos exames dependem da apresentação; os painéis não são um pacote obrigatório para todo paciente com febre.

## Verificação

Sintaxe/importação e grafo individual verificados; resultados dirigidos precedem as questões que os interpretam, e todos os caminhos chegam às referências. Não foram executados build global ou testes de UI. A separação em mais páginas de conteúdo ainda depende da conferência visual na consolidação.

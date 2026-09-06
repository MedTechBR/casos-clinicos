# À flor da pele — referências e notas de autoria

Pesquisa verificada em 06/09/2026. Fontes primárias com texto aberto no PMC;
algumas aberturas diretas apresentaram captcha, mas os textos indexados foram
consultados e os identificadores conferidos. Não se usaram revisões narrativas
como evidência primária nem prevalências históricas como estimativa brasileira atual.

| Fonte aberta | Tipo e contribuição | Limite |
|---|---|---|
| [Knowles et al., 2009 — Levamisole tainted cocaine causing severe neutropenia in Alberta and British Columbia](https://pmc.ncbi.nlm.nih.gov/articles/PMC2780984/) | Investigação observacional; neutropenia, infecções, recorrência e dificuldade de confirmação tardia. | Notificação e seleção; não estima risco individual nem compara tratamentos. |
| [Wiens et al., 2010 — Cocaine adulterant linked to neutropenia](https://pmc.ncbi.nlm.nih.gov/articles/PMC2802606/) | Relatos clínicos; abordagem antimicrobiana e recuperação com e sem filgrastim. | Não prova benefício nem ausência de benefício do G-CSF. |
| [McGrath et al., 2011 — Contaminated Cocaine and Antineutrophil Cytoplasmic Antibody-Associated Disease](https://pmc.ncbi.nlm.nih.gov/articles/PMC3255368/) | Série de 30 casos; dupla positividade MPO/PR3 e manifestações sistêmicas. | Seleção por laboratório de ANCA; perfil não é patognomônico. |
| [Cutaneous Vasculopathy Associated with Levamisole-Adulterated Cocaine](https://pmc.ncbi.nlm.nih.gov/articles/PMC3573092/) | Relato primário com GC-MS positiva; trombose cutânea sem vasculite franca. | O caso publicado confirmou exposição; Marina NÃO herda essa confirmação. |
| [Carlson et al., 2014 — Pauci-Immune Glomerulonephritis… A Series of 4 Cases](https://pmc.ncbi.nlm.nih.gov/articles/PMC4602417/) | Série renal com biópsias e cursos heterogêneos; justifica avaliar ameaça orgânica. | Não define esquema imunossupressor ideal nem probabilidades de diálise. |
| [A Prospective Randomized Study Comparing Ceftolozane/Tazobactam to Standard of Care… (2022)](https://pmc.ncbi.nlm.nih.gov/articles/PMC9154317/) | Ensaio de neutropenia febril em neoplasias hematológicas; contextualiza cobertura empírica antipseudomonas. | Extrapolação de outra população; não recomenda ceftolozana/tazobactam rotineira nesta síndrome. |

## Contrato clínico/editorial

- Paciente, valores laboratoriais, cronologia e desfechos são ficcionais.
- Primeira etapa: febre e pele, sem exposição, orelha ou ANCA na abertura.
- Segunda: mecanismo e extensão; terceira: entrevista privada e toxicologia.
- Resultado de exame aparece apenas no pedido correspondente. Discussões
  subsequentes usam portas `rota` ou hipóteses explicitamente condicionais.
- Diagnóstico sempre provável; mesmo com biópsia renal, agente causal não é
  identificado histologicamente. Levamisol nunca é documentado como confirmado.
- Neutropenia febril: culturas sem atrasar antibiótico IV antipseudomonas,
  avaliação de foco e vigilância. Escolha/dose conforme protocolo local,
  alergias, função renal e resistência. G-CSF individualizado, nunca substituto.
- Lesão cutânea e ANCA isolados não indicam pulso. Ameaça renal pode justificar
  imunossupressão individualizada com especialistas, tratando simultaneamente
  infecção quando indicada. Cultura negativa não constitui autorização automática.
- Janela toxicológica depende de ensaio e tempo. Coleta precoce é preferível;
  48 h não é corte absoluto. Negativo tardio não exclui; benzoilecgonina não
  identifica adulterante nem estabelece causalidade.
- Quatro finais são cenários possíveis. O motor navega por escolhas e pedidos,
  não sorteia eventos; não foram acrescentadas probabilidades ou penalidades
  fisiológicas fictícias. A presença de exame determina certeza da narrativa,
  não a biologia. Erro pode ser resgatado; boa conduta não garante recuperação.
- As perguntas 2–6 são condicionais e não acrescentam laudos ao prontuário.
- Limite de quatro opções por painel é recurso pedagógico, não racionamento clínico.
- Links HTML locais no fecho atendem ao requisito explícito de fontes clicáveis
  sem exigir alteração do helper compartilhado de texto.

## Estrutura e execução

```text
casos/cocaina_levamisol/
  etapas.py
  REFERENCIAS.md
  img/cena.png          # cena gerada por IA e auditada
```

`TITULO = 'À flor da pele'`, `BANCO = []`, `IMG = Path(__file__).parent / 'img'`.
Sem a imagem, o build usa o fundo do motor e omite a lâmina. Ao copiar a cena,
refazer o build: ela será usada somente como fundo e lâmina em História.
Não deve ser fotografia diagnóstica nem evidência de lesão. Nenhuma imagem
foi gerada ou copiada por este trabalho.

Build local: `PYTHONDONTWRITEBYTECODE=1 python3 build_etapas.py cocaina_levamisol`.
Saída esperada: `saida/cocaina-levamisol-etapas.html`. Não publicar.
O build pode ser validado em memória com `motor.etapas.montar(caso)` para
preservar o escopo de somente dois arquivos escritos. O fecho segue para a
revisão nativa (`REVISAO`). Motor, biblioteca e west_nile ficam fora deste escopo.

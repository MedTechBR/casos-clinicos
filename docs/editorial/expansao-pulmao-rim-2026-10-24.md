# Revisão focada — pulmão-rim — 24/10/2026

Escopo exclusivo: `casos/pulmao_rim/etapas.py` e este registro. Imagens, atores, layout e motor preservados. Não foram criados novos episódios de choque nem novos finais.

## Correções

- `r_corticoide` e `b_dia2`: hemoculturas pré-antibiótico permanecem interpretáveis. Corticoide não invalida retrospectivamente a coleta. Retirada a consequência que atribuía dias e perda renal ao corticoide urgente por esse motivo falso; isso corrige o balanço, sem alterar os destinos dos desfechos.
- `dia2` e três ramos: cuidado intensivo, suporte respiratório, avaliação de via aérea e transfusão com reavaliação. Duas unidades distribuídas ao longo da piora; Hb posterior 8,6, sem a antiga estabilização em 6,8 após duas unidades.
- `r_escalona`, `virada`, `res_mec`, `if_anca`, `b1`: deterioração reavaliada em horas no segundo dia; sorologias urgentes retornam no terceiro. Corticoide urgente no segundo dia e decisão da indução após ANCA positivo não aguardam biópsia ou culturas finais. O painel histológico é retrospectivo; a ordem didática das telas não implica espera terapêutica. A biópsia ocorre após estabilização e análise do risco hemorrágico.
- `exame`/`reexame`: força distal e sensibilidade documentadas no basal; déficit multifocal novo nas últimas horas da internação. Sem marcha provocada em paciente hipoxêmico.
- `p5`: quatro exames selecionáveis, anti-MPO e anti-PR3 separados; repetição de C3 isolada como distrator.
- `b_dia2`/`b_febre`: títulos sóbrios e alternativas de uma ação. Culturas e antibiótico empírico imediato são cuidados comuns na nova suspeita infecciosa; a decisão testa controle de foco versus mudança da imunossupressão. Procalcitonina não confirma nem exclui infecção. Próximos pulsos são revistos durante bacteremia; suspensão abrupta de todo corticoide não é apresentada como regra de segurança.
- Profilaxias e rastreios em paralelo ao tratamento urgente, incluindo anti-HBc retornado; sem exigir espera de dois dias de ivermectina para tratar ameaça vital.

## Fontes primárias/oficiais consultadas

- [KDIGO 2024 ANCA](https://kdigo.org/wp-content/uploads/2024/05/KDIGO-2024-ANCA-Vasculitis-Guideline-Update.pdf), PP 9.1.1: apresentação compatível e MPO/PR3 positivo permitem tratar sem aguardar biópsia, sobretudo na deterioração. PP 9.3.1.9: considerar troca plasmática na disfunção renal grave/progressiva ou hemorragia alveolar hipoxêmica; o roteiro mantém discussão individualizada.
- [Surviving Sepsis Campaign 2026 — SCCM](https://www.sccm.org/clinical-resources/guidelines/guidelines/surviving-sepsis-campaign-international-guidelines-for-management-of-sepsis-and-septic-shock-2026): suspeita clínica orienta antibiótico, sem depender de procalcitonina.
- [SSC 2021 — SCCM](https://www.sccm.org/clinical-resources/guidelines/guidelines/surviving-sepsis-guidelines-2021): retirada rápida de acesso suspeito após obtenção de outro acesso; culturas não devem atrasar antimicrobianos.

## Verificação e limites

Importação com Python 3 e bytecode desabilitado. Grafo básico: 62 IDs únicos, referências válidas, todas as etapas alcançáveis, nenhum ciclo; `p5` exige quatro escolhas corretas. Sem build global, Git ou alteração de arquivos compartilhados. Não foi feita verificação visual em navegador.

Os finais e números de dias/TFG continuam simulações autorais, não estimativas causais ou resultados garantidos. As formulações determinísticas dos finais antigos foram corrigidas na complementação abaixo. Classificação MPA/GPA depende do fenótipo e não apenas do alvo MPO/PR3. Decisões de ventilação, transfusão, biópsia e imunossupressão em infecção concomitante exigem julgamento à beira do leito.

## Complementação final — formulações dos percursos

- Corrigidos `fi_obito`, `d10_rituximabe`, `d10_cfx_ajustada`, `d10_cfx_plena`, os três finais de alta e as explicações do balanço: contagens, dias e recuperação renal são observações simuladas, sem nadir universal nem superioridade causal de esquema. Dose ajustada não garante ausência de neutropenia; dose não ajustada aumenta risco, sem explicar sozinha a gravidade.
- Bacteremia já recebe antibiótico empírico em todos os ramos; o risco narrado é atraso no controle do foco e intensificação da imunossupressão. Não há afirmação de bacteremia sem tratamento nesses finais.
- Próximo pulso reprogramado após controle infeccioso e revisão clínica/laboratorial; duração de antibiótico individualizada, sem apresentar 28 dias como regra universal. Corrigida a duplicação textual “ANCA no assim que”.
- Preservados 62 IDs, rotas, quantidade de telas, imagens e layout. Importação e grafo básico revalidados: todas as etapas alcançáveis, sem ciclos ou destinos ausentes. Sem build ou teste UI; o snapshot anterior precisa de rebuild/reteste do pulmão-rim.

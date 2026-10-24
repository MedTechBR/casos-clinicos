# Capas dos pacientes — 24/10/2026

Quatro ilustrações originais geradas com a ferramenta integrada OpenAI imagegen. Não são fotografias clínicas nem exames. Os arquivos anteriores, com fotografias de objetos/paisagens e suas licenças, foram preservados no disco; deixaram de ser usados como capa. Layout mantido.

## Arquivos integrados

- `casos/encefalite_nmda/img/cena-paciente.png`: Camila na admissão, com a mãe.
- `casos/ptt/img/cena-paciente.png`: Sandra como paciente, com familiar e profissional.
- `casos/paracoco/img/cena-paciente.png`: Valdir em consulta, com pequena alteração labial.
- `casos/feocromocitoma/img/cena-paciente.png`: Patrícia com desconforto torácico, durante aferição de pressão.

Usados na abertura de cada caso e no cartão da biblioteca. Metadados locais e créditos no encerramento identificam procedência ficcional. Nenhum resultado diagnóstico aparece na imagem.

## Auditoria independente

Gibbs e Ptolemy abriram individualmente as quatro imagens e compararam-nas com os personagens e a admissão. Ambos aprovaram as quatro, sem deformidades grosseiras impeditivas nem revelação da etiologia. Ressalvas: detalhes discretos como petéquias e icterícia não são demonstrados pela capa; não se usa a ilustração como prova desses achados. O recorte deve preservar rosto e postura.

`ferramentas/testar_capas.py` verifica as 13 capas embutidas na biblioteca, a imagem carregada de cada abertura em modo offline e a ausência de tabelas, alternativas e exames na capa. A aceitação visual das quatro ilustrações é humana/por auditoria visual, não inferida apenas desse teste.

## Prompts utilizados

Prefixo comum, seguido do texto específico de cada paciente:

> Use case: illustration-story. Asset: wide 3:2 cover painting for a Brazilian interactive internal medicine teaching case. Original editorial medical illustration with subtle oil/gouache brushwork, convincing adult anatomy, restrained warm daylight, deep desaturated teal hospital walls, cream bedding, warm skin tones. Natural human expression, not smiling stock photography, not glossy 3D, no decorative icons. Medium-wide hospital encounter with one fictional patient framed center-right, some calm darker negative space on the left for title overlay. No text, no letters, no logos, no diagnoses or visible test results, no labels. This is a fictional person, not a medical diagnostic photograph.

### Camila

> Camila, Brazilian woman age 24, architecture student, medium brown skin, dark wavy shoulder length hair, wearing casual muted blue blouse and trousers, sitting uneasily upright on an emergency department examination bed, tired from several nights of insomnia, alert with a worried distracted expression. Her middle-aged mother sits quietly beside the bed, conveying concern without dramatic behavior. Calm respectful clinical scene; no restraints, no hallucination imagery.

### Sandra

> Sandra, Brazilian woman age 36, a nursing technician arriving as a patient, medium brown skin, dark hair in a loose ponytail, wearing ordinary burgundy casual shirt and trousers, seated on emergency department bed. She looks exhausted and mildly distracted, pale at lips, eyes attentive toward off-frame clinician. Husband partially visible seated nearby. Subtle realistic everyday presentation, no exaggerated lesions, no blood, no dramatic illness imagery.

### Valdir

> Valdir, Brazilian rural worker age 52 from Rondônia, lean build, weathered medium brown face, short dark hair with some gray, faded beige work shirt with sleeves rolled and dark trousers, seated in a public hospital outpatient examination room with a worn straw hat resting beside him. A small discreet crusted area on lower lip, closed mouth, no grotesque or magnified lesion. Thoughtful tired expression, natural light through clinic window. Patient at ordinary consultation, no respiratory devices.

### Patrícia

> Patrícia, Brazilian woman age 41, accountant, medium-light brown skin, shoulder-length dark brown hair, wearing mustard colored office blouse, seated semi-upright on emergency department examination bed. Worried alert expression, one hand lightly at upper chest, other hand resting on bedding. A clinician's hand adjusting a standard blood pressure cuff on her arm, no readable numbers or monitors. No dramatic collapse, no diagnostic imagery.

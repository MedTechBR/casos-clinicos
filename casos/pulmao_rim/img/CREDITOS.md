# Imagens — origem, autor e licença

| Arquivo | Conteúdo | Autor | Fonte | Licença |
|---|---|---|---|---|
| `tc_torax_vidro_fosco.jpg` | Tomografia de tórax, opacidades em vidro fosco difusas | Hellerhoff | Wikimedia Commons | CC BY-SA 4.0 |
| `panca_imunofluorescencia.jpg` | Imunofluorescência indireta, padrão p-ANCA | Simon Caulton | Wikimedia Commons | CC BY-SA 3.0 |
| `biopsia_renal_cortex.jpg` | Córtex renal, glomérulos e tubulointerstício | Nephron | Wikimedia Commons | CC BY-SA 3.0 |
| `glomerulo_crescente.jpg` | Glomérulo com crescente celular, PAS, grande aumento | Nephron | Wikimedia Commons | CC BY-SA 3.0 |
| `rx_torax_alveolar.jpg` | Radiografia de tórax, opacidades alveolares bilaterais | Samir | Wikimedia Commons | CC BY-SA 3.0 |
| `us_rim.jpg` | Ultrassonografia de rim adulto normal | Hansen, Nielsen e Ewertsen | Wikimedia Commons | CC BY 4.0 |
| `sedimento_cilindro.jpg` | Cilindro celular em sedimento urinário | Rian Kabir | Wikimedia Commons | CC BY 2.0 |

> **Correção de 03/09/2026, sobre `biopsia_renal_cortex.jpg`.** A legenda dela
> afirmava "hematoxilina-eosina, crescente celular". A coloração é de padrão
> PAS, não H&E, e não é possível identificar com segurança uma crescente
> naquele plano, de menor aumento. As duas afirmações saíram: a foto passou a
> mostrar o que dá para nomear — glomérulos, túbulos, interstício. A morfologia
> da crescente ficou primeiro num esquema autoral e, desde 05/09/2026, em
> `glomerulo_crescente.jpg`, que é de grande aumento e sustenta a afirmação.

Todas ilustrativas. Nenhuma pertence ao paciente do caso, que é ficcional.
O crédito e a licença aparecem na legenda de cada figura e no slide final.

## cena_admissao.jpg

Ilustração **gerada por inteligência artificial** (Higgsfield / nano-banana),
04/09/2026, a partir da descrição clínica deste caso. Não retrata pessoa real:
o paciente é ficcional.

Aceita pela auditoria de duas vias em 04/09/2026 — os dois auditores
independentes confirmaram que a distribuição da púrpura (face anterior das
pernas e dorso dos pés), o cateter nasal e a idade aparente correspondem ao que
o caso afirma.

## biopsia_renal_cortex.jpg

Renomeada em 04/09/2026, **de `biopsia_renal_crescente.jpg`**. O nome antigo
afirmava um achado que a foto não sustenta, e reintroduzia a afirmação errada
em todo lugar onde o caminho do arquivo aparecia. Os dois auditores rejeitaram
o vínculo entre esta foto e o laudo das crescentes. Hoje ela é só o fundo das
páginas de discussão do rim.


## As quatro imagens novas de 05/09/2026

`glomerulo_crescente.jpg` entrou para **substituir o esquema autoral** da
crescente, a pedido: onde existe fotografia real de licença aberta, o esquema
ensina a forma idealizada — que é justamente a que não aparece na lâmina do
hospital. As três setas sobre ela (cápsula de Bowman, tufo capilar, crescente)
são **leitura editorial deste caso**, não do autor da foto, e a legenda diz
isso na tela.

`rx_torax_alveolar.jpg` é a radiografia de um paciente com SDRA. Entra como
ilustração de **opacidade alveolar bilateral**, e a legenda diz explicitamente
que esse padrão não distingue sangue de água ou de pus — que é a lição, não
uma ressalva.

`us_rim.jpg` foi **recortada**: a imagem original traz gravada a medida
"1 L 13,36 cm", e o laudo do caso diz 11,2 e 11,0 cm. Número gravado na
imagem não pode discutir com o dado do paciente. Os asteriscos que restam são
do autor da fonte e estão decodificados na legenda.

`sedimento_cilindro.jpg` está identificada **na fonte** como cilindro hemático.
Ampliada ao máximo, não se resolvem hemácias individuais, e por isso a legenda
do caso diz apenas "cilindro urinário" — o piso que a fotografia sustenta sem
depender do título do arquivo. Pelo mesmo motivo o arquivo foi renomeado em
05/09/2026, de `sedimento_cilindro_hematico.jpg`: nome de arquivo é uma
afirmação que viaja em todo caminho, log e commit.


## O que a auditoria de duas vias decidiu em 05/09/2026

Os dois auditores independentes **rejeitaram** `rx_torax_alveolar.jpg` pelo
mesmo motivo, encontrado separadamente: havia texto de interface gravado dentro
do arquivo — um `?` na tarja superior e o resto de um `Comments:` no rodapé,
sobras da página de onde a imagem foi capturada. O arquivo foi rebaixado da
fonte e recortado em 5% no topo e 8,5% na base. As demais foram aceitas pelos
dois.

Sobre as setas da fotomicrografia, os dois calcularam a ponta real de cada
seta pela curva de Bézier — e não pelo alvo declarado — e confirmaram cápsula e
crescente. Os dois pediram o mesmo conserto na seta do tufo, que caía sobre
matriz sem alça capilar reconhecível, e um deles apontou o glomérulo
globalmente esclerosado do canto inferior esquerdo como distrator. As duas
coisas foram feitas: a seta do tufo mudou de alvo e o esclerosado ganhou seta
própria, dizendo que não é crescente.

## Imagens para discussão — revisão editorial

- **Alvéolo**: LadyofHats. Domínio público. [Fonte e licença](https://commons.wikimedia.org/wiki/File:Alveolus_diagram.svg). Arquivo sem alterações. Uso comparativo; não é exame do paciente ficcional.
- **Corpúsculo renal**: Michał Komorniczak. CC BY-SA 3.0. [Fonte e licença](https://commons.wikimedia.org/wiki/File:Renal_corpuscle.svg). Arquivo sem alterações. Uso comparativo; não é exame do paciente ficcional.

## Ampliação radiológica

- `rx_consolidacao.jpg` — Mikael Häggström. [Fonte](https://commons.wikimedia.org/wiki/File:X-ray_of_lobar_pneumonia.jpg) · [CC0](https://creativecommons.org/publicdomain/zero/1.0/). sem alterações. Imagem de outro paciente para uso ilustrativo/comparativo.
- `tc_cavidade.jpg` — Yale Rosen. [Fonte](https://commons.wikimedia.org/wiki/File:Lung_abscess_-_CT_scan_(7471756882).jpg) · [CC BY-SA 2.0](https://creativecommons.org/licenses/by-sa/2.0/). sem alterações. Imagem de outro paciente para uso ilustrativo/comparativo.

Os dois revisores independentes aceitaram os usos delimitados. Cortes de TC/RM não representam séries completas nem excluem doença no restante do estudo. O laudo simulado e o crédito da figura são apresentados separadamente.

## ECG e leitura em duas páginas — 7 de setembro de 2026

- `ecg_taquicardia.jpg`: Ewingdo, [arquivo original](https://commons.wikimedia.org/wiki/File:ECG_Sinus_Tachycardia_125_bpm.jpg), [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Traçado de outra pessoa, 125 bpm, sem alteração do arquivo. As setas da segunda página são uma adaptação sob CC BY-SA 4.0. O mesmo traçado comparativo é usado nos três casos; não representa três registros independentes nem os ECGs dos pacientes ficcionais.
- Discussão de ritmo e causas sistêmicas: [ESC, diretriz de taquicardias supraventriculares, seção de taquicardia sinusal](https://academic.oup.com/eurheartj/article/41/5/655/5556821). Não se atribui causa ou diagnóstico etiológico pelo traçado isolado.
- As figuras de radiologia/ultrassom nesta sequência mantêm seus arquivos e créditos prévios. Setas sobrepostas por SVG na página seguinte são adições editoriais; em obras BY-SA, a adaptação conserva a licença original.

## Revisão das marcações — 8 de setembro de 2026

A chave numérica de `Renal corpuscle.svg` foi traduzida da [fonte original](https://commons.wikimedia.org/wiki/File:Renal_corpuscle.svg) e incluída como legenda revelável. A figura permanece sem alterações. Os diagramas transparentes usam fundo branco também na lupa.

Na microfotografia `glomerulo_crescente.jpg`, foi **revogada a interpretação anterior do quarto marcador como glomérulo esclerosado**. Essa estrutura não sustenta a identificação; a seta e o nome foram removidos. Restam três pontos numerados (tufo, cápsula, proliferação extracapilar), conferidos sobre a imagem e pela ponta real do SVG. O laudo simulado agora ocupa uma página separada e não é apresentado como conclusão extraída de uma única fotografia.

O esquema `alveolo.svg` foi retirado da apresentação por conter uma indicação de glândula mucosa na via distal que não é adequada ao ensino dessa anatomia. A página usa agora a TC comparativa previamente conferida. O arquivo original permanece no acervo, sem modificações e sem uso no produto construído.

A legenda de `us_rim.jpg` escreve por extenso a quantidade de asteriscos, evitando que o processador de texto transforme as marcações em negrito.

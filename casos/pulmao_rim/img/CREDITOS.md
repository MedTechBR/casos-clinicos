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

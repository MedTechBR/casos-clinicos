# Casos clínicos interativos

**No ar:** <https://medtechbr.github.io/casos-clinicos/>

Casos no modelo dos *Interactive Medical Cases* do *New England Journal of
Medicine*, para sessão clínica com internos e residentes. A unidade do caso é o
par **alíquota → pergunta**: uma página curta com um dado novo do paciente, e a
pergunta que aquele dado abre — o diferencial de um sintoma, a interpretação de
um resultado, o mecanismo de um achado, um pareamento, a conduta. A proporção
dos tipos segue a medida nas 333 perguntas dos 71 casos da série.

Os três casos no ar (`casos/pulmao_rim`, `casos/west_nile`,
`casos/cocaina_levamisol`) usam o motor em etapas (`motor/etapas.py`):
`pagina`, `pergunta`, `pareamento`, `pedido`/`resultados` (com teto por rodada e
pré-requisito), `bifurcacao`, `desfecho`, `balanco`. Montagem com
`python3 build_etapas.py <caso>`; teste com
`python3 ferramentas/percorrer_casos.py` (todas as combinações de bifurcação,
painel completo e mínimo, em 1600×900 e 1366×768).

A apresentação é **um arquivo `.html` único**: abre com duplo clique, roda em
`file://`, sem servidor, sem internet, sem dependência externa. CSS, JavaScript,
conteúdo, banco de exames e imagens moram dentro dele.

## Estrutura

```
motor/            o motor, comum a todos os casos
  conteudo.py     helpers de prosa, caixas, tabelas, figuras
  slides.py       tipos de slide
  perguntas.py    pergunta -> par (escolha, resposta comentada)
  exames.py       entrada do banco
  estilo.css      folha de estilo
  runtime.js      navegação, revelação, gaveta, edição
  engine.py       montagem do arquivo final
casos/
  _modelo/        ponto de partida para um caso novo
  pulmao_rim/     caso.py (slides) · perguntas.py · banco.py · img/
motor/
  arvore.py       nós, ramos, estado do paciente e desfechos
  ramificacao.js  caminho percorrido, volta ao nó e mapa
ferramentas/
  verificar.py    linter: 12 verificações (ver abaixo)
  autoteste.py    envenena o arquivo e exige que cada verificação acuse
  testar.py       teste de fumaça da interatividade (Playwright)
  densidade.py    mede e escolhe a densidade tipográfica de cada slide
  tirar.py        capturas + folha de contato dos slides
  grade.py        grade de coordenadas sobre as imagens, para anotar
  publicar.py     HTML -> PDF
  comparar.py     compara duas versões, slide a slide
```

Toda ferramenta recebe o nome do caso: `python3 ferramentas/verificar.py
pulmao_rim`. Sem isso, no segundo caso a ferramenta mediria um arquivo e
escreveria em outro, em silêncio.

## Caso novo

```bash
cp -r casos/_modelo casos/<nome>
python3 build.py <nome>
python3 ferramentas/densidade.py <nome> --aplicar
python3 ferramentas/verificar.py <nome>
```

## Uso

```bash
python3 build.py                  # monta saida/pulmao-rim.html
python3 ferramentas/verificar.py  # linter
python3 ferramentas/testar.py     # interatividade
python3 ferramentas/densidade.py --aplicar
python3 ferramentas/publicar.py   # PDF
```

Playwright é a dependência única, e só das ferramentas. A apresentação não tem
nenhuma.

## Teclas, na sala

| tecla | o que faz |
|---|---|
| `→` `espaço` | revela o próximo passo; no fim do slide, avança |
| `←` | volta um passo; no início, volta um slide |
| `A` / `Z` | revela tudo / esconde tudo do slide |
| `1` a `5` | conta os votos da turma na alternativa · `Shift`+número tira um |
| `C` | zera a votação |
| `Q` | pula para a próxima pergunta · `Shift+Q` volta para a anterior |
| `T` | cronômetro da sessão |
| `X` | gaveta de exames — **cada exame pedido adianta o relógio do caso** |
| `M` | mapa da árvore: onde estou, por onde passei, o que não escolhi |
| `V` | volta ao nó anterior **desfazendo o estado** — é o contrafactual |
| `O` | visão geral em miniaturas |
| `E` | modo de edição · `Ctrl+S` baixa o HTML editado |
| `F` | tela cheia |

A votação é por levantamento de mão: você conta e digita. Não precisa de
servidor, de celular nem de internet. O resultado acompanha para o slide de
resposta, e a barra da alternativa certa fica verde-escura — a turma vê no que
apostou antes de saber a resposta.

## Ramificação

O caso não corre em linha reta. A conduta escolhida e os exames pedidos levam
o paciente por caminhos que **não reconvergem** e terminam em desfechos
distintos. No pulmão-rim: 3 momentos de decisão, 2 ramos cada, **8 desfechos**.

Quatro coisas alimentam o estado, que persiste entre os slides e aparece numa
barra de prontuário — sem pontuação, sem estrela, sem barra de vida:

1. a conduta escolhida em cada nó;
2. os exames pedidos na gaveta, e os que se deixou de pedir;
3. o tempo gasto, que a função renal sente;
4. a reavaliação clínica, que libera informação nova.

**Erro é recuperável, com custo.** Nenhum ramo termina no nó: a escolha ruim
produz piora imediata e visível, o caso continua, e dentro do ramo ruim ainda
existe uma decisão de resgate. Mas o melhor final do ramo ruim é pior que o
pior final do ramo certo. O aluno nunca fica travado; ele paga.

Cada ramo mostra a **justificativa fisiológica** depois da escolha — as duas,
para o contrafactual. `V` volta ao nó desfazendo o estado, que é o gesto de
"e se tivéssemos feito o outro?".

`v_cobertura da árvore` recusa destino sem bloco, nó inalcançável, ramo sem
justificativa e desfecho não escrito.

```python
no("n1", "Decisão · primeira hora", "O que você faz na próxima hora",
   "O paciente está no pronto-socorro há quarenta minutos…",
   [
     ramo("colher_e_tratar", "Colher tudo e iniciar pulso hoje",
          vai_para="b_cedo",
          efeito_=efeito(horas=+4, creatinina=+0.1, liga=["imunossupressao"]),
          porque="O pulso é reversível e cobre as três hipóteses…"),
     ramo("esperar_sorologia", "Aguardar as sorologias",
          vai_para="b_espera",
          efeito_=efeito(horas=+38, creatinina=+1.6, spo2=-4, hb=-0.9),
          porque="A glomerulonefrite rapidamente progressiva perde função…"),
   ])
```

## Regras que não se discutem

**Prosa.** História e exame físico em parágrafos corridos, nunca em tópicos.
Marcos temporais dentro da frase. Sinais vitais narrados.

**Títulos.** Substantivo simples: "Exame físico", "Biópsia renal". Nunca
"Quando o pulmão acusa o rim". O linter recusa.

**Banco de exames.** Entrega o valor encontrado e o valor de referência. Nada de
interpretação, comentário didático ou selo de relevância. O grupo interpreta; o
sistema informa. Um analito por entrada.

**Imagens.** Só licença aberta verificável, com crédito e licença no slide e em
`casos/*/img/CREDITOS.md`. Nunca figura do NEJM.

**O caso se abre aos poucos.** O diagnóstico é o destino, não o ponto de
partida. O grupo levanta o diferencial, cada dado novo poda uma linha do
quadro de hipóteses com o motivo ao lado, e o nome da doença só aparece
quando o percurso terminou. `v_sem_spoiler` recusa alternativa correta que já
esteja impressa nos dois slides anteriores à pergunta.

**O formato não pode entregar a resposta.** `v_gabarito` mede a distribuição
das letras corretas, o viés de tamanho da correta e o par repetido nas
perguntas de dupla resposta — as três assinaturas de banco gerado
automaticamente.

**As contas são conferidas.** `v_contas` refaz Henderson-Hasselbalch, a
compensação por Winters, a relação PaO₂/FiO₂ e o CKD-EPI 2021 sobre os
próprios números do banco.

**O slide é canônico.** Se o slide mostra creatinina 3,8, a gaveta não mostra
outra coisa. `verificar.py` confere.

**A régua decide o corpo da fonte, não o autor.** `densidade.py` mede a ocupação
da área útil com tudo revelado e trabalha nos dois sentidos: slide que
transborda aperta, slide que ocupa menos de 58% folga. Slide após slide
preenchido pela metade, sempre com o mesmo corpo, é o que faz um baralho
parecer template.

**Rótulo é voz editorial, não versalete espaçado.** O baralho tinha 19
seletores em maiúscula com entreletra — o delator mais forte de template.
Ficaram três, todos de cromo do sistema (ajuda, gaveta, botão). Etiqueta de
seção, rótulo de caixa e legenda são serifadas em itálico, caixa de frase.

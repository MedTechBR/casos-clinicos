# Casos clínicos interativos

Casos no modelo dos *Case Records of the Massachusetts General Hospital*, para
sessão clínica com internos e residentes. O caso avança em blocos de informação
nova, o grupo discute, e o diagnóstico só aparece depois do raciocínio.

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
  pulmao_rim/     caso.py (slides) · perguntas.py · banco.py · img/
ferramentas/
  verificar.py    linter: transbordo, alternativas, títulos, coerência
  testar.py       teste de fumaça da interatividade (Playwright)
  densidade.py    mede e escolhe a densidade tipográfica de cada slide
  tirar.py        capturas de tela para revisão visual
  publicar.py     HTML -> PDF
  comparar.py     compara duas versões, slide a slide
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
| `X` | gaveta de exames |
| `O` | visão geral em miniaturas |
| `E` | modo de edição · `Ctrl+S` baixa o HTML editado |
| `F` | tela cheia |

A votação é por levantamento de mão: você conta e digita. Não precisa de
servidor, de celular nem de internet. O resultado acompanha para o slide de
resposta, e a barra da alternativa certa fica verde-escura — a turma vê no que
apostou antes de saber a resposta.

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

**O slide é canônico.** Se o slide mostra creatinina 3,8, a gaveta não mostra
outra coisa. `verificar.py` confere.

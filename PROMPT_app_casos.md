# Prompt — aplicativo de casos clínicos interativos

> Cole isto inteiro. É autossuficiente: não depende de nenhuma conversa anterior.

---

## Quem pede e para quê

Sou médico, coordenador do Internato de uma faculdade de medicina no interior do
Ceará. Quero um **aplicativo com vários casos clínicos interativos** para usar
com internos e residentes — tanto projetado numa sala, conduzido por mim ao
vivo, quanto acessado por eles sozinhos.

Tudo em **português do Brasil**.

## O que existe hoje, e que o app precisa respeitar

Tenho um ecossistema de aplicativos médicos hospedados em GitHub Pages, com um
portal que é um lançador de ícones arredondados coloridos sobre papel claro.
O novo app precisa parecer parte dessa família, não um corpo estranho.

## As duas telas

### 1. Biblioteca — clara, polida

Grade de casos. Cada cartão traz a ilustração do caso, o título, a
especialidade, a duração estimada e o progresso de quem já começou.

- Fundo papel claro. Tipografia limpa. Ícones arredondados e bem desenhados.
- **Sem** gradiente decorativo, **sem** emoji, **sem** cartão flutuante com
  sombra difusa, **sem** espaçamento uniforme de template.
- Deve caber ao lado de aplicativos comerciais bem feitos, não parecer gerado.

### 2. O caso — escuro, cinematográfico

Um caso aberto ocupa a tela inteira, com outra linguagem: fundo escuro, a
**imagem médica ocupando a tela inteira** como chão — desfocada, dessaturada e
recuada no eixo Z — e o conteúdo flutuando acima dela com profundidade real
(perspectiva CSS, não sombra).

Como um aplicativo de streaming: biblioteca clara, reprodutor escuro.

## Como o caso funciona

**Página a página.** Cada etapa ocupa uma tela inteira. Nada rola. Passar de
etapa é virar a folha. Botões Voltar/Avançar e setas do teclado.

**Sem relógio.** Nada de esperar resultado de exame, nada de tempo correndo.
O resultado está na virada da página.

A sequência de um caso:

1. **Capa** — título, uma frase de abertura, três números grandes do paciente,
   e os territórios acometidos com marcadores coloridos.
2. **Apresentação** — a história em duas ou três páginas, em prosa corrida.
3. **Exame físico** — uma página.
4. **Seis perguntas**, intercaladas com páginas de discussão e de resultado.
5. **Desfecho** — três finais possíveis, decididos pela última pergunta.
6. **Revisão** — a única página em que o caso comenta o que ficou de fora.

### O tipo de pergunta que carrega o caso

**"Que exames você pede agora?"** — uma tela com os exames organizados em
grupos (bancada imediata, imagem, imunologia, microbiologia…), cada grupo com
a sua cor, todos com caixa de seleção. O grupo marca quantos quiser.

**Na página seguinte volta só o que foi marcado.** O que não foi pedido não
aparece — nem ali, nem depois. Nada é obrigatório e nada é sugerido.

O caso deve ter **duas rodadas** desse tipo de pergunta, em momentos
diferentes.

### As outras perguntas

Escolha com 4 ou 5 alternativas, 1 ou 2 corretas, coluna única.

- O enunciado **começa pelo dado e termina pelo pedido**.
- **Toda alternativa é comentada, inclusive as erradas** — é onde mora a
  discussão. O comentário da errada explica por que ela é tentadora, não só que
  está errada.
- O comentário aparece **depois** da escolha, nunca antes.
- A primeira pergunta **nunca** lista as hipóteses diagnósticas.

### A ramificação

A última pergunta é uma **bifurcação**: dois ou três caminhos concretos de
conduta, e cada um leva a um desfecho diferente. Depois da escolha, aparece a
justificativa fisiológica de todos os caminhos — inclusive dos não escolhidos —
para que se possa discutir o contrafactual em sala.

Cada desfecho traz um bloco **"Por quê"** com a explicação fisiológica do
resultado. Sem pontuação, sem estrela, sem troféu, sem barra de vida. É um
prontuário, não um jogo.

## Regras editoriais que não podem ser quebradas

**Título:** nomeia o achado, **nunca** o diagnóstico. "O sangue dos dois lados",
não "Vasculite associada ao ANCA". Curto e evocativo.

**Prosa:** a história e o exame físico em parágrafos corridos, nunca em
tópicos. Marcadores temporais dentro da frase — "Oito semanas antes…",
"Nos últimos três dias…" — e não como etiqueta.

**Sem pistas.** Durante o caso, a tela nunca aponta o que o grupo deixou de
fazer, e nunca antecipa a resposta da pergunta seguinte. Apontar o erro no meio
da condução é decidir pelo grupo.

**A revisão do fim** é o único lugar em que o caso diz o que faltou pedir, e
por que aquilo teria mudado a condução.

**Negrito é raro.** Só onde o olho precisa parar.

**Tipografia:** serifa para prosa clínica longa, sem serifa para dado
laboratorial e para o que é sistema. Contraste real entre os níveis de título.
Densidade generosa: texto corrido é o formato.

**Cor é sistema, não enfeite.** Cada território do corpo tem a sua cor — via
aérea, pulmão, rim, pele, nervo — e ela reaparece em todo lugar onde aquele
território é citado: no marcador, na borda do grupo de exames, no número do
painel, na barra do desfecho. Nada de verde e vermelho saturados de quiz.

Precisa funcionar num **datashow ruim de sala de aula**.

## As imagens

Duas naturezas, e elas não se misturam:

1. **Cenas do paciente** — ilustração editorial, no estilo da série interativa
   do *New England Journal of Medicine* dos anos recentes: linha de contorno
   escura, preenchimento chapado, fundo desfocado, paleta discreta. Uma cena de
   admissão por caso, no mínimo.
2. **Imagens médicas reais** — tomografia, anatomia patológica,
   imunofluorescência. **Somente de licença aberta verificável** (Wikimedia
   Commons, PHIL/CDC, Europe PMC CC-BY), sempre com crédito e licença ao pé da
   figura. **Nunca** reproduzir figura de periódico fechado.

Toda imagem médica aparece sobre fundo escuro, como se lê num negatoscópio.

## Honestidade clínica

- O paciente é **ficcional**, e isso é dito na capa.
- Nenhuma afirmação clínica sem lastro. Diretriz citada com sociedade e ano.
- Os números têm de fechar entre si: gasometria que obedece a
  Henderson-Hasselbalch, filtração glomerular por CKD-EPI 2021, relação
  PaO₂/FiO₂ calculada e não estimada.
- Onde as sociedades divergem, dizer que divergem, e onde.

## Como quero que seja construído

- **Um arquivo HTML por caso**, autossuficiente, que abra por duplo clique, sem
  servidor, sem internet e sem dependência externa. As imagens viajam
  embutidas.
- O conteúdo de cada caso deve ser **declarativo e separado do motor** — uma
  estrutura de dados legível, para que escrever o próximo caso não seja mexer
  em código.
- O motor não pode saber nada de medicina: ele lê a estrutura do caso.

## O que eu não quero

- Rolagem infinita, tudo descendo numa coluna só.
- Menu lateral com todas as condutas à vista — é prova de múltipla escolha com
  vinte alternativas, e o grupo escolhe pela lista em vez de pensar.
- Relógio correndo e espera por resultado de exame.
- Cara de coisa gerada por IA: gradiente decorativo, emoji, ícone genérico,
  cartão flutuante com sombra difusa, título de manchete ("Quando o pulmão
  acusa o rim" — o certo é "Exame físico").

## Primeira entrega

A tela da biblioteca e **um caso completo** funcionando de ponta a ponta.
Depois disso, mais casos.

Antes de escrever tudo, me mostre **uma tela renderizada** de cada decisão
visual importante. Eu decido vendo, não lendo.

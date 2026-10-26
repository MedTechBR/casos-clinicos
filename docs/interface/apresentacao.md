# Apresentação em tela cheia

Na biblioteca e nos 13 casos, o botão **Apresentar** no cabeçalho abre a tela cheia nativa do navegador. Durante a apresentação, o botão passa a **Sair da tela cheia**. Em telas pequenas, aparece apenas o ícone, com nome acessível.

- **F** alterna o modo; não captura digitação em campos nem as teclas da lupa.
- **Esc** usa a saída nativa do navegador.
- Avançar, voltar e revisar o caso mantêm o modo e as respostas.
- A lupa de imagens continua independente. Seu botão Fechar mantém a apresentação.
- Trocar de documento (por exemplo, abrir um caso a partir da biblioteca) pode encerrar a tela cheia conforme o navegador. O botão está disponível na página de destino.
- Se o navegador não disponibilizar ou bloquear a API, aparece uma orientação, sem simular um modo ativo.

Implementação compartilhada em `motor/apresentacao.js` e `motor/apresentacao.css`, embutida em cada HTML para funcionar também offline. Verificação: `python3 ferramentas/testar_apresentacao.py`.

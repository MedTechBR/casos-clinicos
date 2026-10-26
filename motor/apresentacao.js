/* Tela cheia nativa, compartilhada pela biblioteca e pelos casos. */
(() => {
  const root = document.documentElement;
  const host = document.querySelector('#trilho') || document.querySelector('#topo .barra');
  if (!host) return;
  const ativo = () => !!(document.fullscreenElement || document.webkitFullscreenElement);
  const entrar = root.requestFullscreen || root.webkitRequestFullscreen;
  const sair = document.exitFullscreen || document.webkitExitFullscreen;
  const icone = on => '<svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">' + (on
    ? '<path d="M9 3v6H3m18 0h-6V3M3 15h6v6m6 0v-6h6"/>'
    : '<path d="M9 3H3v6m12-6h6v6M3 15v6h6m12-6v6h-6"/>') + '</svg>';
  let pendente = false;
  let aviso;
  function avisar(texto) {
    if (!aviso) {
      aviso = document.createElement('div');
      aviso.className = 'aviso-apresentacao';
      aviso.setAttribute('role', 'status');
      document.body.append(aviso);
    }
    aviso.textContent = texto;
  }
  function sincronizar() {
    let b = host.querySelector('[data-apresentacao]');
    if (!b) {
      b = document.createElement('button');
      b.type = 'button';
      b.className = 'bt-apresentacao';
      b.dataset.apresentacao = '';
      b.addEventListener('click', alternar);
      host.append(b);
    }
    const on = ativo();
    const titulo = on ? 'Sair da tela cheia' : 'Apresentar em tela cheia';
    b.setAttribute('aria-label', titulo);
    b.setAttribute('aria-pressed', String(on));
    b.title = titulo + ' (F) · Esc para sair';
    b.disabled = pendente;
    const conteudo = icone(on) + '<span>' + (on ? 'Sair da tela cheia' : 'Apresentar') + '</span>';
    if (b.innerHTML !== conteudo) b.innerHTML = conteudo;
  }
  async function alternar() {
    if (pendente) return;
    if (!entrar || !sair) {
      avisar('Este navegador não oferece tela cheia nesta página. Use a opção Tela cheia do menu do navegador.');
      return;
    }
    pendente = true;
    sincronizar();
    if (aviso) aviso.textContent = '';
    try {
      if (ativo()) await sair.call(document);
      else await entrar.call(root);
    } catch (_) {
      avisar('Não foi possível abrir a tela cheia. Tente novamente pelo botão ou pelo menu do navegador.');
    } finally {
      pendente = false;
      sincronizar();
    }
  }
  // O cabeçalho é refeito ao avançar e na revisão; o controle acompanha essas telas.
  new MutationObserver(sincronizar).observe(host, {childList: true});
  document.addEventListener('fullscreenchange', sincronizar);
  document.addEventListener('webkitfullscreenchange', sincronizar);
  document.addEventListener('keydown', ev => {
    if (ev.defaultPrevented || ev.repeat || ev.ctrlKey || ev.metaKey || ev.altKey) return;
    if (ev.target.closest('input,textarea,select,[contenteditable="true"],[role="textbox"]')) return;
    if (document.querySelector('.lupa')) return;
    if (ev.key.toLowerCase() === 'f') { ev.preventDefault(); alternar(); }
  });
  sincronizar();
})();

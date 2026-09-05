/* A biblioteca: monta a prateleira a partir do JSON embutido.

   Sem framework e sem dependência — a mesma regra do caso. Os ícones são
   desenhados aqui, em traço, e não vêm de nenhuma fonte de ícones: é o que
   evita o ar de template. */

const D = JSON.parse(document.getElementById('dados').textContent);

const ICONE = {
  relogio: '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3.2 2"/>',
  bifurca: '<path d="M7 20V9a4 4 0 0 1 4-4h6"/><path d="M14 2l3 3-3 3"/>'
         + '<circle cx="7" cy="21" r="1.4"/>',
  camada:  '<path d="M12 3l8 4.5-8 4.5-8-4.5L12 3z"/><path d="M4 12.5l8 4.5 8-4.5"/>',
};
const ico = n => '<svg viewBox="0 0 24 24" aria-hidden="true">' + ICONE[n] + '</svg>';

document.getElementById('topo').innerHTML =
  '<div class="chapeu"><i></i><span>Casos clínicos interativos</span></div>'
  + '<h1>' + D.titulo + '</h1><p>' + D.subtitulo + '</p>';

document.getElementById('grade').innerHTML = D.casos.map(c => {
  const miolo =
    '<div class="capa" style="' + (c.capa ? 'background-image:url(' + c.capa + ')' : '') + '">'
    + (c.pronto ? '' : '<span class="faixa">Em preparo</span>') + '</div>'
    + '<div class="corpo"><div class="esp">' + c.esp + '</div>'
    + '<h2>' + c.tt + '</h2>'
    + '<p class="sub">' + c.sub + '</p>'
    + '<div class="pe">'
    + '<span>' + ico('relogio') + '<b>' + c.min + '</b> min</span>'
    + '<span>' + ico('bifurca') + '<b>' + c.dec + '</b> decisões</span>'
    + '<span>' + ico('camada') + '<b>' + c.des + '</b> desfechos</span>'
    + '</div></div>';
  return c.pronto
    ? '<a class="cs" style="--cor:' + c.cor + '" href="' + c.arq + '">' + miolo + '</a>'
    : '<div class="cs preparo" style="--cor:' + c.cor + '">' + miolo + '</div>';
}).join('');

document.getElementById('rodape').innerHTML = D.rodape;

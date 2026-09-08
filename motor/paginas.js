/* Paginação por blocos medidos. Nenhum bloco é descartado ou reduzido por zoom. */
let partesTela = [], parteTela = 0, areaTela = null;
const detalhesAbertos = new Set();
const temProximaParte = () => parteTela + 1 < partesTela.length;
function aplicarParte(){
  if (!areaTela) return;
  parteTela = Math.min(Math.max(parteTela, 0), Math.max(0, partesTela.length - 1));
  const ativos = new Set(partesTela[parteTela] || []);
  [...areaTela.children].forEach(el => el.toggleAttribute('data-fora', !ativos.has(el)));
  areaTela.scrollTop = 0; areaTela.scrollLeft = 0;
}
function virarParte(delta){
  parteTela += delta; aplicarParte(); pintarPe();
}
function montarFolhas(){
  partesTela = []; areaTela = null;
  const root = document.querySelector('#palco .plano,#palco .folha,#palco .fim .caixa');
  if (!root) return;
  const mobile = innerWidth <= 900;
  if (mobile && root.classList.contains('plano')){
    const figura = document.querySelector('#palco .lamina');
    if (figura) root.append(figura);
  }
  let area = root.querySelector(':scope > .alts,:scope > .grupos,:scope > .res,:scope > .cams');
  if (!area){
    root.classList.add('paginavel');
    area = document.createElement('div'); area.className = 'conteudo-paginado';
    const filhos = [...root.children];
    // Conserva o título como referência em todas as páginas de continuação.
    filhos.filter(el => !el.matches('.marca,h1,h2')).forEach(el => area.append(el));
    root.append(area);
  }
  if(area.classList.contains('cams')){const aviso=root.querySelector(':scope>.forca');if(aviso)area.append(aviso);}
  if(mobile)root.querySelectorAll('table').forEach(t=>{const nomes=[...t.querySelectorAll('thead th')].map(x=>x.textContent);t.querySelectorAll('tbody tr').forEach(tr=>[...tr.children].forEach((td,n)=>td.dataset.col=nomes[n]||''));});
  area.classList.add('area-paginada'); areaTela = area;
  // Respostas e resultados permanecem inteiros: a densidade se adapta à tela.
  if(area.matches('.alts,.res,.cams')){
    root.classList.add('tela-unica');
    const cabe=()=>area.scrollHeight<=area.clientHeight+1&&area.scrollWidth<=area.clientWidth+1;
    let fator=1;
    root.style.setProperty('--compacto',fator);
    while(!cabe()&&fator>0.25){fator=Math.max(0.25,fator-0.015);root.style.setProperty('--compacto',fator.toFixed(3));}
    partesTela=[[...area.children]];parteTela=0;aplicarParte();return;
  }

  // O flex precisa reservar espaço aos cabeçalhos e aos botões antes da medição.
  const capacidade = () => area.clientHeight;
  function grande(el){ const st=getComputedStyle(el);return el.getBoundingClientRect().height+parseFloat(st.marginTop||0)+parseFloat(st.marginBottom||0) > capacidade() - 3; }
  function dividir(el){
    if (!grande(el)) return false;
    if(mobile && el.matches('.grade,.bal,div:not([class])')){el.replaceWith(...el.children);return true;}
    let filhos = [], criar;
    if (el.matches('.gr')){
      filhos = [...el.querySelectorAll(':scope > .it')];
      criar = () => { const c=el.cloneNode(false);c.append(el.querySelector('b').cloneNode(true));return c; };
    } else if (el.matches('.tops,.grade,.vit,.corpo .lg,aside,.cons,.rev')){
      filhos = [...el.children]; criar=()=>el.cloneNode(false);
    } else if (el.matches('.estudo-imagem') && mobile){
      filhos=[...el.children];criar=()=>el.cloneNode(false);
    } else if (el.matches('.corpo') && mobile){
      filhos=[...el.children];criar=()=>el.cloneNode(false);
    } else if (el.matches('table')){
      filhos=[...el.querySelectorAll('tbody tr')];
      criar=()=>{const c=el.cloneNode(false);if(el.tHead)c.append(el.tHead.cloneNode(true));c.append(document.createElement('tbody'));return c;};
    } else if (el.matches('details[open]')){
      filhos=[...el.children].filter(x=>x.tagName!=='SUMMARY');
      criar=()=>{const c=document.createElement('div');c.className='leitura continuacao-leitura';return c;};
    } else if (el.matches('.rc') && el.querySelector('figure')){
      filhos=[...el.children].filter(x=>x.tagName!=='B');
      criar=()=>{const c=el.cloneNode(false);c.append(el.querySelector('b').cloneNode(true));return c;};
    }
    if (filhos.length > 1){
      if(el.matches('.gr')){
        // Conserva o máximo de opções por grupo que a altura comporta.
        const blocos=[];let atual=criar();el.before(atual);
        for(const f of filhos){atual.append(f);if(grande(atual)&&atual.querySelectorAll('.it').length>1){f.remove();blocos.push(atual);atual=criar();el.before(atual);atual.append(f);}}
        el.remove();return true;
      }
      // Blocos inteiros, com cabeçalhos repetidos onde necessários.
      const novos=filhos.map(f=>{const c=criar();(c.tBodies?.[0]||c).append(f);return c;});
      el.replaceWith(...novos);return true;
    }
    if(el.matches('.cam') && el.querySelector('.c')?.textContent && !el.dataset.discussao){
      const comentario=el.querySelector('.c'),c=el.cloneNode(false);c.dataset.discussao='1';
      c.append(el.querySelector('.l').cloneNode(true));const rot=document.createElement('span');rot.className='r';rot.textContent='Discussão do caminho '+el.querySelector('.l').textContent;c.append(rot,comentario);el.after(c);return true;
    }
    const seletor=el.matches('p')?null:'.c,.cm,:scope>p';
    const alvo=seletor?el.querySelector(seletor):el;
    if(alvo && alvo.textContent.length>120){
      const walker=document.createTreeWalker(alvo,NodeFilter.SHOW_TEXT),nodes=[];
      while(walker.nextNode())nodes.push(walker.currentNode);
      const txt=alvo.textContent,mid=txt.indexOf(' ',Math.floor(txt.length/2));
      if(mid<0)return false;
      let used=0,cut;
      for(const n of nodes){if(used+n.length>=mid){cut=[n,mid-used];break;}used+=n.length;}
      if(!cut)return false;
      const a=document.createRange();a.selectNodeContents(alvo);a.setEnd(...cut);
      const b=document.createRange();b.selectNodeContents(alvo);b.setStart(...cut);
      const left=el.cloneNode(true),right=el.cloneNode(true);
      (seletor?left.querySelector(seletor):left).replaceChildren(a.cloneContents());
      (seletor?right.querySelector(seletor):right).replaceChildren(b.cloneContents());
      el.replaceWith(left,right);return true;
    }
    return false;
  }
  // Une novamente apenas na próxima renderização; os originais continuam nos dados do caso.
  for(let pass=0;pass<8;pass++){
    let mudou=false;
    for(const el of [...area.children])if(dividir(el))mudou=true;
    if(!mudou)break;
  }
  const itens=[...area.children];
  itens.forEach(el=>el.setAttribute('data-fora',''));
  let folha=[];
  for(const el of itens){
    el.removeAttribute('data-fora');
    const excedeu = area.scrollHeight>area.clientHeight+2 || area.scrollWidth>area.clientWidth+2;
    if(excedeu && folha.length){
      partesTela.push(folha);folha.forEach(n=>n.setAttribute('data-fora',''));folha=[];
    }
    folha.push(el);
  }
  if(folha.length)partesTela.push(folha);
  aplicarParte();
}

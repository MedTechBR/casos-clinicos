"""Navega pelos mesmos botões usados em aula para alcançar um bloco paginado."""
def mostrar(page, selector, index=0):
    loc=page.locator(selector).nth(index)
    if not loc.is_visible():
        destino=loc.evaluate('(el)=>partesTela.findIndex(p=>p.some(n=>n===el||n.contains(el)))')
        assert destino>=0,(page.evaluate('etapa().k'),selector,index,'elemento sem página',loc.evaluate('(e)=>e.parentElement.outerHTML.slice(0,200)'))
        while page.evaluate('parteTela')<destino:page.locator('#seguir').click()
        while page.evaluate('parteTela')>destino:page.locator('#voltar').click()
    return loc

def ultima(page):
    while page.evaluate('temProximaParte()'):page.locator('#seguir').click()

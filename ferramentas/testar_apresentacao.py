"""Tela cheia nativa nas 14 páginas, preservação do caso e falhas da API."""
import sys
from pathlib import Path
from playwright.sync_api import sync_playwright
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from nomes_publicos import PUBLICO

with sync_playwright() as pw:
    browser = pw.chromium.launch()
    page = browser.new_page(viewport={"width": 1366, "height": 768})
    errors = []
    page.on('pageerror', lambda e: errors.append(str(e)))
    for name in ['index', *PUBLICO.values()]:
        page.goto((ROOT / (name + '.html')).as_uri())
        for script in page.locator('script:not([type="application/json"])').all_text_contents():
            page.evaluate('(s)=>{new Function(s)}', script)
        button = page.locator('[data-apresentacao]')
        assert button.count() == 1
        button.click()
        page.wait_for_function('!!document.fullscreenElement')
        page.wait_for_timeout(180)
        assert button.get_attribute('aria-pressed') == 'true'
        if name != 'index':
            page.locator('#seguir').click()
            page.wait_for_timeout(180)
            assert page.evaluate('!!document.fullscreenElement && i > 0')
            page.evaluate('''()=>{const e=ETAPAS.find(e=>e.t==='pergunta');ir(porId(e.k));respostas[e.k]={feita:true,marcadas:e.alts.map((a,n)=>a.ok?n:-1).filter(n=>n>=0)};pintar()}''')
            before = page.evaluate('JSON.stringify([i,respostas,escolhas])')
        button.click()
        page.wait_for_function('!document.fullscreenElement')
        page.wait_for_timeout(180)
        assert button.get_attribute('aria-pressed') == 'false'
        if name != 'index':
            assert page.evaluate('JSON.stringify([i,respostas,escolhas])') == before
            page.evaluate('mostrarRevisao()')
            assert button.count() == 1
        for width, height in [(1366,768),(375,812)]:
            page.set_viewport_size({'width': width, 'height': height})
            page.wait_for_timeout(180)
            assert page.evaluate('''()=>{const b=document.querySelector('[data-apresentacao]').getBoundingClientRect();return b.left>=0 && b.right<=innerWidth && b.top>=0 && b.bottom<=innerHeight && document.documentElement.scrollWidth<=innerWidth}'''), (name, width)
            assert button.evaluate('(el)=>{let r=el.getBoundingClientRect();return el.contains(document.elementFromPoint(r.x+r.width/2,r.y+r.height/2))}'), (name, 'botão encoberto')
        page.set_viewport_size({'width':1366,'height':768})
        print('OK', name, flush=True)
    page.goto((ROOT / 'index.html').as_uri())
    page.locator('#busca').fill('f')
    page.locator('#busca').press('f')
    assert not page.evaluate('!!document.fullscreenElement')
    page.locator('#busca').blur()
    page.keyboard.press('f')
    page.wait_for_function('!!document.fullscreenElement')
    page.keyboard.press('f')
    page.wait_for_function('!document.fullscreenElement')
    # Ampliação da figura não encerra o modo de apresentação.
    page.goto((ROOT / 'o-sangue-que-nao-saiu.html').as_uri())
    page.evaluate('ir(porId("crescente"))')
    page.locator('[data-apresentacao]').click()
    page.wait_for_function('!!document.fullscreenElement')
    page.wait_for_timeout(180)
    page.locator('figure.amplia').first.click()
    page.locator('.lupa .fechar').click()
    assert page.evaluate('!!document.fullscreenElement')
    page.screenshot(path='/tmp/casos-apresentacao.png')
    # O evento nativo também atualiza o controle ao sair pelo navegador.
    page.evaluate('document.exitFullscreen()')
    page.wait_for_function('document.querySelector("[data-apresentacao]").getAttribute("aria-pressed")==="false"')
    # Rejeição e ausência da API: sem falso estado nem erro JS.
    denied = browser.new_context()
    denied.add_init_script('Element.prototype.requestFullscreen=()=>Promise.reject(new Error("Teste"))')
    other = denied.new_page()
    other.on('pageerror', lambda e: errors.append(str(e)))
    other.goto((ROOT / 'index.html').as_uri())
    other.locator('[data-apresentacao]').click()
    other.wait_for_function('document.querySelector(".aviso-apresentacao")?.textContent.includes("Não foi possível")')
    assert other.locator('[data-apresentacao]').get_attribute('aria-pressed') == 'false'
    denied.close()
    unsupported = browser.new_context()
    unsupported.add_init_script('Element.prototype.requestFullscreen=undefined;Element.prototype.webkitRequestFullscreen=undefined')
    other = unsupported.new_page()
    other.on('pageerror', lambda e: errors.append(str(e)))
    other.goto((ROOT / 'index.html').as_uri())
    other.locator('[data-apresentacao]').click()
    other.wait_for_function('document.querySelector(".aviso-apresentacao")?.textContent.includes("não oferece")')
    assert other.locator('[data-apresentacao]').get_attribute('aria-pressed') == 'false'
    unsupported.close()
    assert not errors, errors
    browser.close()
    print('14 páginas: tela cheia real, navegação, estado, revisão, desktop/mobile, atalho, lupa e falhas da API OK')

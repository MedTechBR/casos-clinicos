"""Confere capas embutidas na biblioteca e na abertura, inclusive sem internet.

Uso: python3 ferramentas/testar_capas.py [--prints]
"""
import importlib
import json
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from build_biblioteca import CASOS
from nomes_publicos import PUBLICO

with sync_playwright() as pw:
    browser = pw.chromium.launch()
    page = browser.new_page(viewport={"width": 1366, "height": 768}, offline=True)
    errors = []
    page.on("pageerror", lambda e: errors.append(str(e)))
    page.goto((ROOT / "saida/biblioteca.html").as_uri())
    covers = page.evaluate("D.casos.map(c=>({titulo:c.tt,capa:c.capa}))")
    assert len(covers) == len(CASOS)
    for c in covers:
        assert c["capa"].startswith("data:image/"), (c["titulo"], "sem imagem embutida")
    result = []
    for slug in PUBLICO:
        module = importlib.import_module(f"casos.{slug}.etapas")
        cover = module.ETAPAS[0]
        assert cover["t"] == "capa" and (module.IMG / cover["fundo"]).is_file()
        page.goto((ROOT / "saida" / f'{slug.replace("_", "-")}-etapas.html').as_uri())
        page.wait_for_function("document.querySelector('.capa-fundo')")
        ok = page.evaluate("""async () => {
            const bg = getComputedStyle(document.querySelector('.capa-fundo')).backgroundImage;
            if (!bg.startsWith('url("data:image/')) return false;
            const img = new Image(); img.src = bg.slice(5, -2);
            await img.decode(); return img.naturalWidth >= 600 && img.naturalHeight >= 300;
        }""")
        assert ok, (slug, "imagem da abertura não carregou")
        assert page.locator(".abertura h1").inner_text() == module.TITULO
        assert not page.locator(".rc, .vitais, .alts, table").count(), (slug, "dados clínicos na capa")
        if "--prints" in sys.argv and slug in ("ptt", "encefalite_nmda", "paracoco", "feocromocitoma"):
            page.wait_for_timeout(1200)  # aguardar a animação de entrada antes da prova visual
            page.screenshot(path=f"/tmp/capa-{slug}.png")
        result.append({"caso": slug, "imagem": cover["fundo"], "abertura": "OK"})
    assert not errors, errors
    browser.close()
print(json.dumps({"biblioteca": len(covers), "aberturas": result}, ensure_ascii=False, indent=2))

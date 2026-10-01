"""Folha de conferência das setas: para cada tela de imagem, a figura inteira com
a ponta de cada seta marcada e um zoom em volta de cada ponta, com o texto do achado.

Uso:  python3 ferramentas/auditar_setas.py <pasta-de-saída> [slug ...]
Serve para OLHAR se a ponta cai dentro da estrutura descrita (não na borda vizinha).
"""
import importlib, re, sys, textwrap
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
ROOT = Path(__file__).resolve().parents[1]; sys.path.insert(0, str(ROOT))
from nomes_publicos import PUBLICO
TAG = re.compile(r'<[^>]+>')
try: FONTE = ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial.ttf', 22)
except Exception: FONTE = ImageFont.load_default()

def telas(slug):
    m = importlib.import_module('casos.' + slug + '.etapas')
    for e in m.ETAPAS:
        s = str(e)
        if 'vv-estudo' not in s: continue
        html = next(v for v in e.values() if isinstance(v, str) and 'vv-estudo' in v) if any(isinstance(v, str) and 'vv-estudo' in v for v in e.values()) else s
        img = re.search(r'data-img="([^"]+)"', html).group(1)
        vb = re.search(r'viewBox="0 0 1000 ([\d.]+)"', html)
        pontas = [(int(n), float(x), float(y)) for n, x, y in
                  re.findall(r'<g class="sa" data-n="(\d+)".*?translate\(([\d.\-]+) ([\d.\-]+)\)', html)]
        alvos = re.findall(r'<li data-n="(\d+)"[^>]*>.*?<div>(.*?)</div></li>', html)
        textos = {int(n): TAG.sub('', t).replace('\\n', ' ') for n, t in alvos}
        yield e['k'], ROOT / 'casos' / slug / 'img' / img, pontas, textos

def folha(slug, k, arq, pontas, textos, out):
    im = Image.open(arq).convert('RGB'); W, H = im.size; esc = W / 1000
    Z, R = 300, int(70 * esc)  # zoom: janela de 140‰ da largura
    full = im.copy(); d = ImageDraw.Draw(full)
    for n, x, y in pontas:
        X, Y = x * esc, y * esc; r = max(6, W // 120)
        d.ellipse((X - r, Y - r, X + r, Y + r), outline=(255, 0, 0), width=max(2, W // 400))
        d.text((X + r + 2, Y - r - 2), str(n), fill=(255, 0, 0), font=FONTE)
    fw = 900; full = full.resize((fw, int(H * fw / W)))
    linhas = max(len(pontas), 1)
    sheet = Image.new('RGB', (fw + Z + 520, max(full.height, linhas * (Z + 10)) + 40), 'white')
    sheet.paste(full, (0, 40)); sd = ImageDraw.Draw(sheet)
    sd.text((5, 5), f'{slug} · {k} · {arq.name}', fill=(0, 0, 0), font=FONTE)
    for i, (n, x, y) in enumerate(pontas):
        X, Y = int(x * esc), int(y * esc)
        c = im.crop((X - R, Y - R, X + R, Y + R)).resize((Z, Z)); cd = ImageDraw.Draw(c)
        cd.line((Z / 2 - 14, Z / 2, Z / 2 + 14, Z / 2), fill=(255, 0, 0), width=2)
        cd.line((Z / 2, Z / 2 - 14, Z / 2, Z / 2 + 14), fill=(255, 0, 0), width=2)
        oy = 40 + i * (Z + 10); sheet.paste(c, (fw + 10, oy))
        t = f'{n}: ' + textos.get(n, '?')
        sd.multiline_text((fw + Z + 20, oy + 5), '\n'.join(textwrap.wrap(t, 38)), fill=(0, 0, 0), font=FONTE)
    sheet.save(out)

if __name__ == '__main__':
    saida = Path(sys.argv[1]); saida.mkdir(parents=True, exist_ok=True)
    slugs = sys.argv[2:] or [s for s in PUBLICO if (ROOT / 'casos' / s / 'etapas.py').exists()]
    n = 0
    for s in slugs:
        for k, arq, pontas, textos in telas(s):
            folha(s, k, arq, pontas, textos, saida / f'{s}__{k}.jpg'); n += 1
            print(s, k, arq.name, len(pontas), 'setas')
    print(n, 'folhas')

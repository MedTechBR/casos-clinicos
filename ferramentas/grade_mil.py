"""Grade de coordenadas em milésimos da largura, para posicionar setas.

As setas de `estudo(...)` usam (x, y) em milésimos da LARGURA da imagem nos
dois eixos. Esta grade desenha essas coordenadas sobre a imagem para que a
seta seja escolhida olhando, nunca chutando.

Uso:  python3 ferramentas/grade_mil.py <imagem> <saida.jpg> [passo=50]
"""
import sys
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
src=Path(sys.argv[1]); out=Path(sys.argv[2]); passo=int(sys.argv[3]) if len(sys.argv)>3 else 50
im=Image.open(src).convert('RGB'); W,H=im.size
esc=1400/W if W<1400 else 1
im=im.resize((int(W*esc),int(H*esc))); W,H=im.size
d=ImageDraw.Draw(im); u=W/1000
try: f=ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc',int(14))
except: f=None
hmax=1000*H/W
v=0
while v<=1000:
  x=v*u; c=(0,255,255) if v%100==0 else (255,255,0)
  d.line([(x,0),(x,H)],fill=c,width=1)
  if v%100==0: d.text((x+2,2),str(v),fill=(0,255,255),font=f)
  v+=passo
v=0
while v<=hmax:
  y=v*u; c=(0,255,255) if v%100==0 else (255,255,0)
  d.line([(0,y),(W,y)],fill=c,width=1)
  if v%100==0: d.text((2,y+2),str(v),fill=(0,255,255),font=f)
  v+=passo
im.save(out,quality=85)
print(W,H,round(hmax))

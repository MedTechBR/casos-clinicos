"""Cálipers vetoriais sobre a imagem de referência, sem alterar seus pixels.

Original: 650 × 560 px. Profundidade D=4 cm; primeira marca lateral
em y=78, última em y=550: 472 px / 40 mm = 11,8 px/mm.
Estimativa didática em imagem rasterizada, não medição DICOM.
"""
from math import hypot

PX_POR_MM = (550 - 78) / 40
LONGO = ((105, 208), (516, 189))
CURTO = ((310, 121), (316, 248))


def medida_cm(pontos):
    (x1, y1), (x2, y2) = pontos
    return hypot(x2-x1, y2-y1) / PX_POR_MM / 10


def sobreposicao():
    partes = ['<g class="medidas-us" transform="scale(1.5384615385)" '
              'aria-label="Medida aproximada: 3,5 por 1,1 centímetros">']
    for nome, pontos, texto, label in (
        ('A', LONGO, 'A ≈ 3,5 cm', (239, 277)),
        ('B', CURTO, 'B ≈ 1,1 cm', (520, 263)),
    ):
        (x1,y1),(x2,y2) = pontos
        partes.append(f'<g fill="none" stroke="#67e8f9" stroke-width="1.8">'
                      f'<path d="M{x1} {y1} L{x2} {y2}" stroke-dasharray="5 4"/>')
        for x,y in pontos:
            partes.append(f'<path d="M{x-5} {y}h10 M{x} {y-5}v10" '
                          'stroke="#0a0c10" stroke-width="4"/>'
                          f'<path d="M{x-5} {y}h10 M{x} {y-5}v10"/>')
        partes.append('</g>')
        x,y = label
        partes.append(f'<text x="{x}" y="{y}" fill="#67e8f9" font-size="14" '
                      'font-family="Arial,sans-serif" font-weight="bold" '
                      'stroke="#0a0c10" stroke-width="3" paint-order="stroke">'
                      f'{texto}</text>')
    # Régua de 10 mm, subdivisões de 1 mm; a régua lateral original é preservada.
    partes.append('<g stroke="#67e8f9" stroke-width="1.8"><path d="M85 478h118"/>')
    for n in range(11):
        x=85+n*PX_POR_MM
        partes.append(f'<path d="M{x:.1f} 478v{-10 if n in (0,5,10) else -5}"/>')
    partes.append('</g><text x="144" y="499" text-anchor="middle" '
                  'font-family="Arial,sans-serif" font-size="14" fill="#67e8f9" '
                  'stroke="#0a0c10" stroke-width="3" paint-order="stroke">1 cm</text></g>')
    return ''.join(partes)

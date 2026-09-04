"""Dimensões intrínsecas de uma imagem, sem dependência externa.

A anotação em SVG precisa saber o tamanho real do arquivo: é o que permite a
sobreposição casar exatamente com a imagem renderizada em `object-fit: contain`.
"""

from __future__ import annotations

import struct
from pathlib import Path

# marcadores JPEG que carregam altura e largura
_SOF = {0xC0, 0xC1, 0xC2, 0xC3, 0xC5, 0xC6, 0xC7,
        0xC9, 0xCA, 0xCB, 0xCD, 0xCE, 0xCF}


def dimensoes(caminho: Path) -> tuple[int, int]:
    d = Path(caminho).read_bytes()
    if d[:8] == b"\x89PNG\r\n\x1a\n":
        w, h = struct.unpack(">II", d[16:24])
        return w, h
    if d[:2] == b"\xff\xd8":
        i = 2
        while i < len(d) - 9:
            if d[i] != 0xFF:
                i += 1
                continue
            m = d[i + 1]
            if m in _SOF:
                h, w = struct.unpack(">HH", d[i + 5 : i + 9])
                return w, h
            if m in (0xD8, 0xD9) or 0xD0 <= m <= 0xD7:
                i += 2
                continue
            i += 2 + struct.unpack(">H", d[i + 2 : i + 4])[0]
    raise ValueError(f"não sei ler as dimensões de {caminho}")

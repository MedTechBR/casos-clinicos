"""Desenhos autorais em SVG.

Não são imagens de licença aberta: são esquemas desenhados aqui, o que resolve
a licença de vez e permite anotar exatamente o que o caso precisa. É como o
periódico faz as figuras explicativas — traço único, sem sombra, sem volume.

Todo desenho é vetorial e escala com o palco. Os que têm partes reveladas usam
as mesmas classes de revelação do motor, então o `→` e o clique já funcionam.
"""

from __future__ import annotations

from .conteudo import texto

TRACO = "#2a2620"
FINO = "#8d8474"
FUNDO = "#e6dfd0"
MARCA = "#8e2b1b"


# ═══════════════════════════ corpo do paciente ═══════════════════════════


def _suave(pts, fechado=True) -> str:
    """Catmull-Rom -> Bézier: transforma uma lista de pontos em curva contínua.

    Desenhar silhueta humana com segmentos de reta denuncia o desenho. Com a
    curva passando pelos pontos, o contorno fica orgânico e o autor controla
    só os marcos anatômicos.
    """
    n = len(pts)
    d = [f"M{pts[0][0]:.1f} {pts[0][1]:.1f}"]
    for i in range(n if fechado else n - 1):
        p0 = pts[(i - 1) % n]
        p1, p2 = pts[i % n], pts[(i + 1) % n]
        p3 = pts[(i + 2) % n]
        c1 = (p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6)
        c2 = (p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6)
        d.append(f"C{c1[0]:.1f} {c1[1]:.1f} {c2[0]:.1f} {c2[1]:.1f} "
                 f"{p2[0]:.1f} {p2[1]:.1f}")
    if fechado:
        d.append("Z")
    return " ".join(d)


# Meia silhueta anterior, em deslocamento a partir do eixo (x=150).
# Só marcos anatômicos: crânio, mandíbula, pescoço, deltoide, cotovelo,
# punho, cintura, quadril, joelho, tornozelo, pé. O resto é a curva.
_MEIA = [
    (0, 6), (15, 11), (25, 30), (24, 50), (17, 66), (11, 74),      # crânio e face
    (11, 86),                                                       # pescoço
    (32, 92), (52, 100), (62, 112),                                 # trapézio e deltoide
    (70, 136), (80, 176), (90, 216), (98, 252),                     # braço, lado de fora
    (103, 274), (104, 287), (95, 289), (90, 278),                   # mão
    (86, 252), (78, 216), (68, 176), (60, 140),                     # braço, lado de dentro
    (52, 124),                                                      # axila
    (45, 150), (38, 180), (39, 202),                                # tronco e cintura
    (45, 224), (43, 246),                                           # quadril
    (41, 290), (37, 330), (32, 370), (30, 398),                     # coxa e perna
    (33, 410), (46, 417), (47, 422), (28, 422), (17, 415), (16, 400),  # pé
    (18, 362), (16, 320), (11, 278),                                # perna, lado de dentro
    (5, 244), (0, 236),                                             # virilha
]


def _silhueta() -> str:
    dir_ = [(150 + dx, y) for dx, y in _MEIA]
    esq = [(150 - dx, y) for dx, y in reversed(_MEIA[1:-1])]
    return _suave(dir_ + esq)


# Cada território: o realce anatômico e onde fica o número.
TERRITORIOS = {
    "via_aerea": dict(
        nome="Via aérea superior",
        marca=(
            # região médio-facial: seios e fossas nasais, sem virar rosto
            '<path d="M150 30 C138 30 133 40 134 51 C135 60 141 68 150 68 '
            'C159 68 165 60 166 51 C167 40 162 30 150 30 Z"/>'
            '<path d="M150 44 L150 62" stroke-width="1.2" fill="none"/>'
        ),
        num=(190, 40),
    ),
    "pulmao": dict(
        nome="Pulmão",
        marca=(
            '<path d="M141 106 C130 114 126 140 129 162 C131 176 141 178 143 166 '
            'C146 146 145 118 141 106 Z"/>'
            '<path d="M159 106 C170 114 174 140 171 162 C169 176 159 178 157 166 '
            'C154 146 155 118 159 106 Z"/>'
            '<path d="M150 96 L150 108 M150 108 L142 116 M150 108 L158 116"/>'
        ),
        num=(190, 130),
    ),
    "rim": dict(
        nome="Rim",
        marca=(
            '<path d="M133 186 C124 186 120 196 121 206 C122 217 128 223 134 220 '
            'C139 218 138 210 136 204 C134 198 137 190 133 186 Z"/>'
            '<path d="M167 186 C176 186 180 196 179 206 C178 217 172 223 166 220 '
            'C161 218 162 210 164 204 C166 198 163 190 167 186 Z"/>'
        ),
        num=(190, 204),
    ),
    "pele": dict(
        nome="Pele",
        marca=(
            '<circle cx="128" cy="332" r="3"/><circle cx="134" cy="350" r="2.4"/>'
            '<circle cx="126" cy="364" r="3.2"/><circle cx="132" cy="380" r="2.4"/>'
            '<circle cx="127" cy="396" r="2.8"/><circle cx="124" cy="412" r="2.4"/>'
            '<circle cx="172" cy="336" r="2.6"/><circle cx="167" cy="354" r="3.2"/>'
            '<circle cx="174" cy="372" r="2.4"/><circle cx="169" cy="388" r="2.8"/>'
            '<circle cx="175" cy="404" r="2.4"/><circle cx="177" cy="416" r="2.6"/>'
        ),
        num=(210, 356),
    ),
    "nervo": dict(
        nome="Nervo periférico",
        marca=(
            # pé caído à direita do paciente e território ulnar à esquerda dele
            # pé caído à direita do paciente
            '<path d="M181 392 L185 414 L206 424" stroke-width="3.6" fill="none" '
            'stroke-linecap="round" stroke-linejoin="round"/>'
            # território ulnar na mão esquerda
            '<path d="M52 258 L48 280" stroke-width="3" fill="none" '
            'stroke-linecap="round"/>'
            '<circle cx="47" cy="285" r="6"/>'
        ),
        num=(218, 424),
    ),
}


def mapa_do_corpo(territorios, altura: int = 350, passo_a_passo: bool = True) -> str:
    """Figura do paciente com os territórios acometidos.

    `territorios` é uma lista de (chave, descrição). Cada território acende no
    desenho e na legenda ao mesmo tempo, e clicar em qualquer um dos dois liga
    os dois — em sala, dá para apontar pelo desenho ou pela lista.
    """
    marcas, legenda = [], []
    for k, (chave, desc) in enumerate(territorios):
        if chave not in TERRITORIOS:
            raise ValueError(f"território desconhecido: {chave!r}; "
                             f"use {sorted(TERRITORIOS)}")
        t = TERRITORIOS[chave]
        nx, ny = t["num"]
        cls = "terr pv" if passo_a_passo else "terr on"
        marcas.append(
            f'<g class="{cls}" data-terr="{chave}">'
            f'<g class="marca" fill="{MARCA}" fill-opacity=".2" stroke="{MARCA}" '
            f'stroke-width="1.7" stroke-linejoin="round">{t["marca"]}</g>'
            f'<g class="marca">'
            f'<circle cx="{nx}" cy="{ny}" r="9" fill="{MARCA}"/>'
            f'<text x="{nx}" y="{ny + 3.8}" text-anchor="middle" fill="#fff" '
            f'font-size="11" font-weight="700" '
            f'font-family="Helvetica Neue,Arial,sans-serif">{k + 1}</text>'
            f"</g></g>"
        )
        legenda.append(
            f'<div class="lt" data-terr="{chave}">'
            f'<div class="nm">{k + 1} · {texto(t["nome"])}</div>'
            f'<div class="ds">{texto(desc)}</div></div>'
        )

    svg = (
        f'<svg viewBox="0 0 310 438" xmlns="http://www.w3.org/2000/svg">'
        f'<path d="{_silhueta()}" fill="#fff" stroke="{TRACO}" stroke-width="1.7" '
        f'stroke-linejoin="round"/>'
        f'{"".join(marcas)}</svg>'
    )
    return (
        f'<div class="mapa" style="--mh:{altura}px">'
        f'<div class="fig">{svg}</div>'
        f'<div class="legenda">{"".join(legenda)}</div></div>'
    )


# ═══════════════════════ capilar glomerular × alveolar ═══════════════════════


def capilar_compartilhado(altura: int = 300) -> str:
    """Por que pulmão e rim caem juntos: a mesma parede, nos dois órgãos.

    À esquerda o tufo glomerular dentro da cápsula de Bowman; à direita o
    alvéolo com o capilar correndo na parede. O traço vermelho é a estrutura
    que os dois compartilham, e é o que a doença agride.
    """
    def rot(x, y, t, cor=None, tam=12, peso=600):
        return (
            f'<text x="{x}" y="{y}" text-anchor="middle" font-size="{tam}" '
            f'font-family="Helvetica Neue,Arial,sans-serif" font-weight="{peso}" '
            f'letter-spacing=".3" fill="{cor or TRACO}">{t}</text>'
        )

    svg = f"""<svg viewBox="0 0 640 310" xmlns="http://www.w3.org/2000/svg">
  <!-- glomérulo -->
  <g fill="none" stroke="{TRACO}" stroke-width="1.5">
    <circle cx="160" cy="168" r="86"/>
    <ellipse cx="137.8" cy="134.4" rx="37" ry="14" transform="rotate(-62 137.8 134.4)"/><ellipse cx="152.6" cy="148.4" rx="37" ry="14" transform="rotate(-31 152.6 148.4)"/><ellipse cx="158.0" cy="168.0" rx="37" ry="14" transform="rotate(0 158.0 168.0)"/><ellipse cx="152.6" cy="187.6" rx="37" ry="14" transform="rotate(31 152.6 187.6)"/><ellipse cx="137.8" cy="201.6" rx="37" ry="14" transform="rotate(62 137.8 201.6)"/>
    <path d="M40 152 L120 168 M40 190 L120 168"/>
    <circle cx="120" cy="168" r="3" fill="{TRACO}"/>
  </g>

  <!-- alvéolo -->
  <g fill="none" stroke="{TRACO}" stroke-width="1.5">
    <circle cx="480" cy="168" r="86"/>
    <path d="M480 82 L480 40 M480 40 L452 22 M480 40 L508 22"/>
    <path d="M404 122 C444 148 516 148 556 122"/>
    <path d="M404 138 C444 164 516 164 556 138"/>
  </g>

  <!-- a parede que os dois compartilham -->
  <g stroke="{MARCA}" stroke-width="4" fill="none" stroke-linecap="round">
    <path d="M121.0 168 A37 14 0 0 1 195.0 168"/>
    <path d="M404 130 C444 156 516 156 556 130"/>
  </g>

  <!-- chave entre os dois -->
  <g fill="none" stroke="{MARCA}" stroke-width="1.1" stroke-dasharray="4 4">
    <path d="M150 104 C210 66 380 66 428 104"/>
  </g>
  {rot(300, 48, "a mesma parede", MARCA, 13.5, 700)}
  {rot(300, 64, "endotélio sobre membrana basal, sob pressão", FINO, 11, 500)}

  {rot(46, 142, "aferente", FINO, 10, 500)}
  {rot(46, 204, "eferente", FINO, 10, 500)}
  {rot(160, 286, "Capilar glomerular", None, 12.5)}
  {rot(160, 302, "dentro da cápsula de Bowman", FINO, 11, 400)}
  {rot(480, 286, "Capilar alveolar", None, 12.5)}
  {rot(480, 302, "na parede do espaço aéreo", FINO, 11, 400)}
</svg>"""
    return _fig_desenho(
        svg,
        "O capilar glomerular e o capilar alveolar têm a mesma arquitetura: "
        "endotélio fino sobre membrana basal, submetido a pressão. Uma agressão "
        "a esse compartimento aparece nos dois órgãos ao mesmo tempo.",
        altura,
    )


# ═══════════════════════════ crescente glomerular ═══════════════════════════


def crescente_glomerular(altura: int = 280) -> str:
    """Glomérulo normal ao lado de glomérulo com crescente celular."""
    def rotulo(x, y, t, cor=None, tam=11.5, peso=600):
        return (
            f'<text x="{x}" y="{y}" text-anchor="middle" font-size="{tam}" '
            f'font-family="Helvetica Neue,Arial,sans-serif" font-weight="{peso}" '
            f'fill="{cor or TRACO}">{t}</text>'
        )

    tufo = ('<path d="M-34 0 C-34 -26 -12 -38 4 -26 C20 -14 16 8 -2 14 '
            'C-20 20 -34 16 -34 0 Z"/>'
            '<path d="M36 -2 C36 -26 14 -38 -2 -26"/>'
            '<path d="M-18 26 C4 38 30 32 40 16"/>')
    svg = f"""<svg viewBox="0 0 560 280" xmlns="http://www.w3.org/2000/svg">
  <g transform="translate(140,124)">
    <circle r="86" fill="none" stroke="{TRACO}" stroke-width="1.5"/>
    <g fill="none" stroke="{TRACO}" stroke-width="1.5">{tufo}</g>
    <path d="M-118 0 L-86 0" fill="none" stroke="{TRACO}" stroke-width="1.5"/>
  </g>
  <g transform="translate(420,124)">
    <circle r="86" fill="none" stroke="{TRACO}" stroke-width="1.5"/>
    <!-- tufo comprimido -->
    <g fill="none" stroke="{TRACO}" stroke-width="1.5" transform="translate(6,16) scale(.82)">
      {tufo}
    </g>
    <!-- a crescente: proliferação no espaço de Bowman -->
    <path d="M-86 0 A86 86 0 0 1 62 -60 L44 -40 A62 62 0 0 0 -62 0 Z"
          fill="{MARCA}" opacity=".82"/>
    <path d="M-118 0 L-86 0" fill="none" stroke="{TRACO}" stroke-width="1.5"/>
  </g>
  {rotulo(140, 240, "Glomérulo normal")}
  {rotulo(140, 256, "tufo livre no espaço de Bowman", FINO, 11, 400)}
  {rotulo(420, 240, "Crescente celular")}
  {rotulo(420, 256, "proliferação que comprime o tufo", FINO, 11, 400)}
</svg>"""
    return _fig_desenho(
        svg,
        "A crescente ocupa o espaço de Bowman e comprime o tufo. É a lesão que "
        "explica a queda rápida de função renal; não diz, sozinha, qual é a causa.",
        altura,
    )


# ═══════════════════════════ padrão de imunofluorescência ═══════════════════


def padroes_imunofluorescencia(altura: int = 250) -> str:
    """Os três padrões que a imunofluorescência separa."""
    def glom(cx, tipo):
        base = (f'<circle cx="{cx}" cy="104" r="62" fill="none" '
                f'stroke="{TRACO}" stroke-width="1.4"/>')
        alcas = (f'<g fill="none" stroke="{FINO}" stroke-width="1.2">'
                 f'<path d="M{cx-38} 104 C{cx-38} 78 {cx-14} 68 {cx-2} 80 '
                 f'C{cx+10} 92 {cx+6} 112 {cx-8} 118 C{cx-24} 124 {cx-38} 120 {cx-38} 104 Z"/>'
                 f'<path d="M{cx+34} 100 C{cx+34} 76 {cx+12} 66 {cx-2} 78"/></g>')
        if tipo == "linear":
            dep = (f'<path d="M{cx-38} 104 C{cx-38} 78 {cx-14} 68 {cx-2} 80 '
                   f'C{cx+10} 92 {cx+6} 112 {cx-8} 118 C{cx-24} 124 {cx-38} 120 {cx-38} 104 Z" '
                   f'fill="none" stroke="{MARCA}" stroke-width="3.6"/>')
        elif tipo == "granular":
            pontos = "".join(
                f'<circle cx="{cx - 34 + (k * 13) % 68}" '
                f'cy="{78 + (k * 19) % 44}" r="3.2" fill="{MARCA}"/>'
                for k in range(14)
            )
            dep = pontos
        else:
            dep = ""
        return base + alcas + dep

    def rotulo(x, y, t, cor=None, tam=11.5, peso=600):
        return (
            f'<text x="{x}" y="{y}" text-anchor="middle" font-size="{tam}" '
            f'font-family="Helvetica Neue,Arial,sans-serif" font-weight="{peso}" '
            f'fill="{cor or TRACO}">{t}</text>'
        )

    svg = f"""<svg viewBox="0 0 620 250" xmlns="http://www.w3.org/2000/svg">
  {glom(108, 'linear')}
  {glom(310, 'granular')}
  {glom(512, 'nenhum')}
  {rotulo(108, 196, "Linear")}
  {rotulo(108, 212, "anti-membrana basal", FINO, 11, 400)}
  {rotulo(310, 196, "Granular")}
  {rotulo(310, 212, "imunocomplexos", FINO, 11, 400)}
  {rotulo(512, 196, "Pauci-imune")}
  {rotulo(512, 212, "vasculite associada ao ANCA", FINO, 11, 400)}
  <g stroke="{MARCA}" stroke-width="2.2" fill="none">
    <path d="M446 234 L578 234"/>
  </g>
  {rotulo(512, 232, "", FINO, 11, 400)}
</svg>"""
    return _fig_desenho(
        svg,
        "A imunofluorescência não gradua a lesão: ela separa três mecanismos. "
        "Ausência de depósito é achado, não falha de técnica.",
        altura,
    )


# ═══════════════════════════ linha do tempo ═══════════════════════════


def marco(quando: str, oque: str, agora: bool = False) -> dict:
    return {"quando": quando, "oque": oque, "agora": agora}


def linha_do_tempo(marcos, passo_a_passo: bool = True) -> str:
    """As oito semanas, em régua. Cada marco entra como um passo da revelação."""
    cols = " ".join("1fr" for _ in marcos)
    itens = []
    for m in marcos:
        cls = ["m"]
        if passo_a_passo:
            cls.append("pv")
        else:
            cls.append("on")
        if m["agora"]:
            cls.append("agora")
        itens.append(
            f'<div class="{" ".join(cls)}">'
            f'<div class="qd">{texto(m["quando"])}</div>'
            f'<div class="oq">{texto(m["oque"])}</div></div>'
        )
    return (
        f'<div class="tl"><div class="marcos" '
        f'style="grid-template-columns:{cols}">{"".join(itens)}</div></div>'
    )


# ═══════════════════════════ comparação ═══════════════════════════


def comparacao(titulo_a: str, blocos_a, titulo_b: str, blocos_b) -> str:
    """Duas colunas confrontadas por uma régua. Para 'o que fala a favor / contra'."""
    return (
        '<div class="comp">'
        f'<div><div class="ct">{texto(titulo_a)}</div>{"".join(blocos_a)}</div>'
        f'<div><div class="ct">{texto(titulo_b)}</div>{"".join(blocos_b)}</div>'
        "</div>"
    )


# ═══════════════════════════ util ═══════════════════════════


def _fig_desenho(svg: str, legenda: str, altura: int) -> str:
    return (
        f'<figure class="dz" style="--fh:{altura}px">{svg}'
        f"<figcaption>{texto(legenda)}"
        f'<span class="cred">Esquema autoral, desenhado para este caso.</span>'
        f"</figcaption></figure>"
    )

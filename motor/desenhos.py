"""Desenhos autorais em SVG.

Não são imagens de licença aberta: são esquemas desenhados aqui, o que resolve
a licença de vez e permite anotar exatamente o que o caso precisa. É como o
periódico faz as figuras explicativas — traço único, sem sombra, sem volume.

Todo desenho é vetorial e escala com o palco. Os que têm partes reveladas usam
as mesmas classes de revelação do motor, então o `→` e o clique já funcionam.
"""

from __future__ import annotations

import math

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


def _tufo(escala: float = 1.0, angulos=(-62, -31, 0, 31, 62)) -> str:
    """Alças capilares em roseta, radiando do polo vascular na origem (0,0).

    Desenhar o tufo como emaranhado de curvas vira borrão projetado. Alças
    distintas, radiando de um ponto, é como o glomérulo é esquematizado — e
    deixa claro o que a crescente comprime.
    """
    partes = []
    for a in angulos:
        r = math.radians(a)
        d, rx, ry = 38 * escala, 37 * escala, 14 * escala
        cx, cy = d * math.cos(r), d * math.sin(r)
        partes.append(
            f'<ellipse cx="{cx:.1f}" cy="{cy:.1f}" rx="{rx:.1f}" ry="{ry:.1f}" '
            f'transform="rotate({a} {cx:.1f} {cy:.1f})"/>'
        )
    return "".join(partes)


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
    <g transform="translate(120,168)">{_tufo()}</g>
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
    def rot(x, y, t, cor=None, tam=12, peso=600):
        return (
            f'<text x="{x}" y="{y}" text-anchor="middle" font-size="{tam}" '
            f'font-family="Helvetica Neue,Arial,sans-serif" font-weight="{peso}" '
            f'fill="{cor or TRACO}">{t}</text>'
        )

    svg = f"""<svg viewBox="0 0 580 300" xmlns="http://www.w3.org/2000/svg">
  <g transform="translate(146,140)">
    <circle r="88" fill="none" stroke="{TRACO}" stroke-width="1.5"/>
    <g transform="translate(-46,0)" fill="none" stroke="{TRACO}" stroke-width="1.4">
      {_tufo(1.05)}
    </g>
    <path d="M-122 0 L-88 0" fill="none" stroke="{TRACO}" stroke-width="1.5"/>
    <circle cx="-46" cy="0" r="3" fill="{TRACO}"/>
  </g>

  <g transform="translate(434,140)">
    <circle r="88" fill="none" stroke="{TRACO}" stroke-width="1.5"/>
    <!-- a crescente ocupa o espaço de Bowman, longe do polo vascular -->
    <path d="M-88 0 A88 88 0 0 1 62 -62 L40 -40 A57 57 0 0 0 -57 0 Z"
          fill="{MARCA}" fill-opacity=".85"/>
    <!-- o tufo, comprimido, sobra menor e empurrado para baixo -->
    <g transform="translate(-44,18)" fill="none" stroke="{TRACO}" stroke-width="1.4">
      {_tufo(0.74, (-38, -12, 15, 42))}
    </g>
    <path d="M-122 0 L-88 0" fill="none" stroke="{TRACO}" stroke-width="1.5"/>
    <circle cx="-44" cy="18" r="3" fill="{TRACO}"/>
  </g>

  {rot(146, 262, "Glomérulo normal", None, 12.5)}
  {rot(146, 280, "tufo livre no espaço de Bowman", FINO, 11, 400)}
  {rot(434, 262, "Crescente celular", None, 12.5)}
  {rot(434, 280, "proliferação que comprime o tufo", FINO, 11, 400)}
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


# ═══════════════════════════ quadro de hipóteses ═══════════════════════════

# O caso do NEJM não entrega o diagnóstico: entrega dados, e o discussant vai
# derrubando candidatos até sobrar um. O quadro é esse movimento, visível.
# Ele reaparece ao longo do caso, e cada dado novo derruba ou enfraquece uma
# linha — com o motivo escrito ao lado. O nome da doença só sobra no fim.

ESTADOS = {
    "de_pe": ("", "de pé"),
    "enfraquecida": ("fraca", "enfraquecida"),
    "derrubada": ("fora", "derrubada"),
    "confirmada": ("dentro", "confirmada"),
}


def hip(chave: str, nome: str, exige: str) -> dict:
    """Um candidato do diferencial.

    `exige` é o que teria de ser verdade para ele ser o diagnóstico — não o que
    este paciente tem. A diferença é o caso inteiro: escrever "púrpura palpável
    e mononeurite múltipla" na linha da vasculite ANCA é apontar o dedo para o
    paciente antes de qualquer exame.
    """
    return {"chave": chave, "nome": nome, "exige": exige}


def quadro(hipoteses, estado=None, passo_a_passo: bool = True,
           titulo: str = "", novos=None) -> str:
    """O diferencial e o que já aconteceu com cada linha.

    `estado` mapeia chave -> (situação, motivo). Quem não aparece segue de pé.
    Cada mudança de situação entra como um passo de revelação, para que o
    professor derrube uma por vez enquanto a turma discute.

    `novos` são as chaves podadas NESTE passo: só elas mostram o motivo por
    extenso. As que já tinham caído aparecem riscadas e mudas — repetir todos
    os motivos a cada reaparição enche a tela e apaga o que acabou de mudar.
    """
    estado = estado or {}
    novos = set(novos) if novos is not None else set(estado)
    linhas = []
    for h in hipoteses:
        sit, motivo = estado.get(h["chave"], ("de_pe", ""))
        if sit not in ESTADOS:
            raise ValueError(f"situação desconhecida: {sit!r}; use {sorted(ESTADOS)}")
        cls, rotulo = ESTADOS[sit]
        muda = sit != "de_pe"
        passo = " pv" if (muda and passo_a_passo and h["chave"] in novos) else ""
        linhas.append(
            f'<div class="hp {cls}{passo}" data-hip="{h["chave"]}">'
            f'<div class="hn">{texto(h["nome"])}</div>'
            f'<div class="hx">{texto(h["exige"])}</div>'
            + (f'<div class="hm"><b>{texto(rotulo)}</b> {texto(motivo)}</div>'
               if muda and h["chave"] in novos
               else (f'<div class="hm mudo">{texto(rotulo)}</div>' if muda
                     else '<div class="hm"></div>'))
            + "</div>"
        )
    cab = f'<div class="qt">{texto(titulo)}</div>' if titulo else ""
    return f'<div class="quadro">{cab}{"".join(linhas)}</div>'


# ═══════════════ figuras da direção Atlas (fundo escuro) ═══════════════

# Os desenhos acima nasceram para papel claro: silhueta branca, traço quase
# preto. No chão escuro do caso em etapas eles somem. O que vem abaixo é a
# mesma anatomia repintada para o escuro — e, principalmente, a ferramenta que
# põe seta e rótulo sobre FOTOGRAFIA de licença aberta, que é o que ensina
# melhor que esquema autoral quando a imagem real existe.

# do vocabulário de sistemas do motor de etapas para as chaves daqui
_DE_SISTEMA = {"via": "via_aerea", "pulmao": "pulmao", "rim": "rim",
               "pele": "pele", "nervo": "nervo"}


def corpo(territorios, *, altura: int = 340) -> str:
    """O boneco do paciente, com os territórios acometidos acesos.

    `territorios` é uma lista de (sistema, achado). O número no desenho e o
    número na legenda são o mesmo, e cada um herda a cor do seu sistema — a
    mesma cor que aquele território tem em toda a peça.
    """
    marcas, legenda = [], []
    for k, (sis, achado) in enumerate(territorios):
        chave = _DE_SISTEMA.get(sis)
        if chave is None:
            raise ValueError(f"sistema sem desenho no corpo: {sis!r}")
        t = TERRITORIOS[chave]
        nx, ny = t["num"]
        cor = f"var(--{sis})"
        marcas.append(
            f'<g class="tr t-{sis}">'
            f'<g fill="{cor}" fill-opacity=".26" stroke="{cor}" '
            f'stroke-width="1.9" stroke-linejoin="round">{t["marca"]}</g>'
            f'<circle cx="{nx}" cy="{ny}" r="9.5" fill="{cor}"/>'
            f'<text x="{nx}" y="{ny + 3.9}" text-anchor="middle" fill="#0b0e12" '
            f'font-size="11.5" font-weight="700" '
            f'font-family="-apple-system,Helvetica Neue,Arial,sans-serif">'
            f"{k + 1}</text></g>"
        )
        legenda.append(
            f'<div class="lt t-{sis}"><b>{k + 1}</b><div>'
            f'<span class="nm">{texto(t["nome"])}</span>'
            f'<span class="ds">{texto(achado)}</span></div></div>'
        )
    svg = (
        '<svg viewBox="0 0 310 438" xmlns="http://www.w3.org/2000/svg">'
        f'<path d="{_silhueta()}" fill="#161b22" stroke="#5b6672" '
        f'stroke-width="1.6" stroke-linejoin="round"/>'
        f'{"".join(marcas)}</svg>'
    )
    return (f'<div class="corpo" style="--ch:{altura}px">{svg}'
            f'<div class="lg">{"".join(legenda)}</div></div>')


# ─────────────────── fotografia com seta e rótulo ───────────────────


def seta(alvo, rotulo, texto_, *, curva: float = 0) -> dict:
    """Uma seta: parte do rótulo e aponta para o alvo.

    Coordenadas em milésimos da largura da imagem — x de 0 a 1000, y de 0 até
    a altura proporcional. Pensar em ‰ da largura deixa a anotação
    independente do tamanho do arquivo: trocar a foto por uma maior não move
    as setas.
    """
    return {"a": alvo, "r": rotulo, "t": texto(texto_), "c": curva}


def anotada(arquivo, largura, altura, *setas, legenda="", credito="",
            titulo="", moldura: int = 0) -> str:
    """A foto de licença aberta com as setas que explicam o que olhar.

    Substitui o esquema autoral onde existe imagem real: o esquema ensina a
    forma idealizada, e a forma idealizada é justamente a que não aparece na
    lâmina do hospital. A seta resolve o problema que fazia o esquema
    necessário — dizer QUAL das estruturas da foto é a que interessa.
    """
    h = round(1000 * altura / largura, 1)
    partes = []
    for s in setas:
        (ax, ay), (rx, ry) = s["a"], s["r"]
        # ponto de controle deslocado na perpendicular: seta reta sobre
        # textura biológica some, seta curva se lê como anotação
        mx, my = (ax + rx) / 2, (ay + ry) / 2
        dx, dy = ax - rx, ay - ry
        n = max((dx * dx + dy * dy) ** 0.5, 1e-6)
        cx, cy = mx - dy / n * s["c"], my + dx / n * s["c"]
        # a ponta para pouco antes do alvo: o suficiente para não cobrir a
        # estrutura, não tanto que aponte para o vizinho dela
        t = 0.965
        px = (1 - t) ** 2 * rx + 2 * (1 - t) * t * cx + t * t * ax
        py = (1 - t) ** 2 * ry + 2 * (1 - t) * t * cy + t * t * ay
        ang = math.degrees(math.atan2(ay - py, ax - px))
        d = f"M{rx:.1f} {ry:.1f} Q{cx:.1f} {cy:.1f} {px:.1f} {py:.1f}"
        anc = "start" if rx <= ax else "end"
        partes.append(
            # dois traços sobre o mesmo caminho: o escuro largo abre espaço na
            # textura, o claro fino é a seta que se lê
            f'<path class="fio halo" d="{d}"/><path class="fio luz" d="{d}"/>'
            f'<path class="ponta" d="M0 0 L-19 8 L-19 -8 Z" '
            f'transform="translate({px:.1f} {py:.1f}) rotate({ang:.1f})"/>'
            f'<text class="rot" x="{rx:.1f}" y="{ry:.1f}" text-anchor="{anc}" '
            f'dy="-7">{s["t"]}</text>'
        )
    fig = (
        f'<figure class="anot{" mold" if moldura else ""}">'
        f'<svg viewBox="0 0 1000 {h}" xmlns="http://www.w3.org/2000/svg">'
        f'<image data-img="{arquivo}" x="0" y="0" width="1000" height="{h}" '
        f'preserveAspectRatio="xMidYMid slice"/>'
        f'<g class="an">{"".join(partes)}</g></svg>'
    )
    if titulo or legenda or credito:
        fig += ('<figcaption>'
                + (f"<b>{texto(titulo)}</b>" if titulo else "")
                + texto(legenda)
                + (f'<span class="cr">{texto(credito)}</span>' if credito else "")
                + "</figcaption>")
    return fig + "</figure>"

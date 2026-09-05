"""O caso em etapas — direção Atlas.

Uma página de cada vez. O caso se apresenta, faz uma pergunta, e a resposta
decide a página seguinte. Sem relógio e sem espera: o resultado está na virada
da folha.

A pergunta que carrega o caso é a de exames — grupos com caixas de seleção, e
só o que foi marcado volta na página de resultados. O que não foi pedido não
aparece; a revisão do fim é o único lugar em que o caso comenta o que faltou, e
ela vem quando não há mais o que decidir.

Cada tela tem um chão: a imagem médica ocupa a tela inteira, escurecida e
recuada no espaço, e o conteúdo flutua acima dela. A cor não é enfeite — cada
sistema tem a sua, e ela reaparece em todo lugar onde aquele sistema é citado.

    capa()          abertura
    pagina()        prosa, painel, figura
    pedido()        "que exames você pede?", em grupos, marcação múltipla
    resultados()    devolve só o que foi marcado
    pergunta()      escolha comentada, com o comentário de cada alternativa
    bifurcacao()    a escolha que muda a página seguinte
    desfecho()      o fim, e por quê
"""

from __future__ import annotations

import base64
import json
import mimetypes
import re
from pathlib import Path

from .conteudo import texto

# Um sistema, uma cor. A mesma em toda a peça: no marcador do território, na
# borda do grupo de exames, no número do painel, na barra do desfecho.
SISTEMAS = {
    "via": "via aérea superior",
    "pulmao": "pulmão",
    "rim": "rim",
    "pele": "pele",
    "nervo": "nervo periférico",
    "sangue": "sangue",
    "geral": "sistêmico",
}


def _s(nome):
    if nome not in SISTEMAS:
        raise ValueError(f"sistema desconhecido: {nome!r}; use {sorted(SISTEMAS)}")
    return nome


# ─────────────────────────── blocos de conteúdo ───────────────────────────


def p(*partes) -> str:
    return f"<p>{texto(' '.join(partes))}</p>"


def lead(*partes) -> str:
    return f'<p class="lede">{texto(" ".join(partes))}</p>'


def lista(itens, ordenada=False) -> str:
    tag = "ol" if ordenada else "ul"
    return f"<{tag}>" + "".join(f"<li>{texto(i)}</li>" for i in itens) + f"</{tag}>"


def numeros(*trios) -> str:
    """Três a quatro números grandes, cada um na cor do sistema a que pertence."""
    return '<div class="nums">' + "".join(
        f'<div class="n-{_s(sis)}"><b>{texto(valor)}</b>'
        f"<span>{texto(rotulo)}</span></div>"
        for valor, rotulo, sis in trios) + "</div>"


def territorios(*itens, colunas=1) -> str:
    """Marcadores de território: cor, nome e o achado.

    O nome e o achado moram num mesmo filho: com três filhos diretos numa grade
    de duas colunas, o achado caía para a linha de baixo, na coluna estreita do
    marcador, e a prosa saía uma palavra por linha.
    """
    return f'<div class="terrs c{colunas}">' + "".join(
        f'<div class="terr t-{_s(sis)}"><i></i><div>'
        f"<b>{texto(nome)}</b><span>{texto(achado)}</span></div></div>"
        for sis, nome, achado in itens) + "</div>"


def grade(*blocos, colunas=2) -> str:
    """Põe blocos lado a lado em vez de empilhados.

    Numa peça que não rola, altura é o recurso escasso. Quatro quadros de
    prescrição empilhados passavam 400 px da tela; em duas colunas, cabem —
    e passam a ser comparáveis com o olho, que é como se lê uma prescrição.
    """
    return (f'<div class="grade c{colunas}">'
            + "".join(f"<div>{b}</div>" for b in blocos) + "</div>")


def quadro(titulo, *blocos, sistema="geral") -> str:
    return (f'<div class="qd q-{_s(sistema)}"><b>{texto(titulo)}</b>'
            f'{"".join(blocos)}</div>')


def tabela(cabecalho, linhas) -> str:
    th = "".join(f"<th>{texto(c)}</th>" for c in cabecalho)
    tr = "".join("<tr>" + "".join(f"<td>{texto(c)}</td>" for c in l) + "</tr>"
                 for l in linhas)
    return (f'<table class="tb"><thead><tr>{th}</tr></thead>'
            f"<tbody>{tr}</tbody></table>")


def lamina(arquivo, titulo, legenda, credito) -> dict:
    """A imagem em destaque, inclinada no espaço, ao lado do conteúdo."""
    return {"img": arquivo, "tt": texto(titulo), "lg": texto(legenda),
            "cr": texto(credito)}


# ─────────────────────────── páginas ───────────────────────────


def _pag(tipo, ident, **extra):
    return dict({"t": tipo, "k": ident}, **extra)


def capa(titulo, *, fundo, kicker="", selo="", procedencia="") -> dict:
    """A capa é título e imagem. Só.

    Ela trazia três números grandes — creatinina, saturação, hemoglobina — e a
    lista dos territórios acometidos. Isso é o resumo do caso impresso na porta
    de entrada: entrega de graça, na primeira tela, dados que o caso depois vai
    cobrar uma das seis vagas do painel de exames para devolver. E ninguém
    conduz um paciente lendo o desfecho da triagem antes de entrar no quarto.

    A procedência não some: ela vai inteira para a última tela, onde não
    atrapalha o raciocínio de ninguém.
    """
    return _pag("capa", "capa", tt=texto(titulo), fundo=fundo,
                kicker=texto(kicker), selo=texto(selo),
                proc=texto(procedencia))


def _rota(rota):
    """A ramificação pelo que foi PEDIDO, validada no build."""
    if rota is None:
        return None
    if set(rota) != {"pediu", "entao", "senao"}:
        raise ValueError("rota: use pediu=[...], entao=..., senao=...")
    if not rota["pediu"]:
        raise ValueError("rota sem exame exigido não ramifica nada")
    return rota


def pagina(ident, kicker, titulo, *blocos, fundo="", lamina_=None,
           nota="", sistema="geral", so_kicker=False, segue="",
           conforme=None, rota=None) -> dict:
    """`so_kicker` promove o rótulo a título e descarta a manchete.

    `conforme=("b1", ["a", "b", "c"])` faz a página seguinte depender do
    caminho escolhido numa bifurcação anterior. É o que permite ter uma
    evolução compartilhada — a febre do quinto dia é a mesma nos três — e um
    hemograma que só depois se separa, sem triplicar a página inteira.

    Serve às telas em que o rótulo longo diz mais que o título curto — "onde
    dava para ter chegado antes" contra "a retrospectiva". Ter os dois é o que
    faz onze telas parecerem a mesma máquina de quatro compartimentos.
    """
    if conforme is not None:
        de, para = conforme
        if not isinstance(para, (list, tuple)) or len(para) < 2:
            raise ValueError("conforme: (ident_da_bifurcacao, [destinos])")
        conforme = {"de": de, "para": list(para)}
    return _pag("pagina", ident, kicker=texto(kicker), tt=texto(titulo),
                corpo="".join(blocos), fundo=fundo, lamina=lamina_,
                nota=texto(nota), sis=_s(sistema),
                so_kicker=1 if so_kicker else 0, segue=segue,
                conforme=conforme, rota=_rota(rota))


# ─────────────────────────── o pedido de exames ───────────────────────────


def op(exame, detalhe="", *, resultado=None, referencia=None,
       alterado=None, exige=None, porque="") -> dict:
    """Uma linha marcável. `exame` é o nome exato no banco do caso.

    `resultado` sobrepõe o valor do banco. É necessário porque o banco foi
    escrito para um formato com relógio, em que a hemocultura vira positiva no
    quinto dia: aqui, sem relógio, ela precisa devolver o resultado da coleta
    daquela etapa, e não o desfecho de uma complicação futura.
    """
    o = {"e": exame, "d": texto(detalhe)}
    if exige:
        # A biópsia renal aparecia no painel antes de existir um sedimento.
        # Nenhum nefrologista punciona um rim assim, e oferecer o exame
        # decisivo cedo demais encerra o caso antes da hora: o grupo pula o
        # raciocínio e vai direto ao tecido. Com `exige`, a linha continua
        # visível — para que se veja o que existe — mas só destrava quando o
        # que a justifica já foi pedido.
        o["ex"] = list(exige)
        o["pq"] = texto(porque or "depende de exame que ainda não foi pedido")
    if resultado is not None:
        o["r"] = texto(resultado)
        o["ref"] = texto(referencia) if referencia is not None else "—"
        o["a"] = 1 if alterado else 0
    return o


def grupo(nome, sistema, opcoes) -> dict:
    return {"n": texto(nome), "s": _s(sistema), "o": opcoes}


def pedido(ident, kicker, titulo, enunciado, grupos, *, fundo="",
           nota="", banco=None, limite=0) -> dict:
    """Marcação múltipla, sem sugestão — e com teto.

    O teto não é economia: é o que transforma a tela numa decisão. Sem ele a
    jogada dominante é marcar tudo, e quem marca tudo recebe o diagnóstico
    pronto na virada da folha sem ter escolhido nada. Com teto, deixar um exame
    de fora passa a custar — que é exatamente o custo da beira do leito.
    """
    vistos = set()
    for g in grupos:
        for o in g["o"]:
            if o["e"] in vistos:
                raise ValueError(f"exame repetido no pedido {ident!r}: {o['e']}")
            vistos.add(o["e"])
    sobre = {o["e"]: {"n": o["e"], "r": o["r"], "ref": o["ref"], "a": o["a"]}
             for g in grupos for o in g["o"] if "r" in o}
    # Um rótulo que não existe no banco e não traz resultado próprio é marcável,
    # soma no contador, e devolve NADA na página seguinte — sem erro e sem
    # aviso. O caso chegava a dizer "você não pediu nenhum exame" para quem
    # tinha marcado quatro. Isso passa a explodir no build.
    if banco is not None:
        nomes = {e["n"] for e in banco}
        orfaos = sorted(o["e"] for g in grupos for o in g["o"]
                        if o["e"] not in nomes and "r" not in o)
        if orfaos:
            raise ValueError(
                f"pedido {ident!r}: rótulo sem entrada no banco e sem "
                f"resultado próprio — devolveria nada: {', '.join(orfaos)}")
        # Oferecer um exame que devolve "não realizada" é pior do que não
        # oferecer: o grupo gasta uma das suas vagas para receber a informação
        # de que a vaga foi desperdiçada. Ou o exame tem resultado, ou não é
        # marcável.
        por_nome = {e["n"]: e for e in banco}
        vazios = sorted(o["e"] for g in grupos for o in g["o"]
                        if "r" not in o
                        and "não realiza" in por_nome.get(o["e"], {})
                        .get("r", "").lower())
        if vazios:
            raise ValueError(
                f"pedido {ident!r}: exame marcável que devolve 'não realizada' "
                f"— tire do painel ou dê um resultado: {', '.join(vazios)}")
    if limite and limite > sum(len(g["o"]) for g in grupos):
        raise ValueError(f"pedido {ident!r}: teto maior que o próprio painel")
    return _pag("pedido", ident, kicker=texto(kicker), tt=texto(titulo),
                enunciado=texto(enunciado), grupos=grupos, fundo=fundo,
                nota=texto(nota), sobre=sobre, limite=limite)


def resultados(ident, kicker, titulo, de, *, fundo="", introducao="",
               nota="", laminas=None, rota=None) -> dict:
    """Devolve os exames marcados no pedido `de` — e só eles.

    `laminas` associa nome de exame à imagem que ele devolve: quem pede a
    tomografia recebe a tomografia, e quem não pede não vê nada.

    `rota` leva a promessa até o fim: se as provas que a etapa exigia não foram
    pedidas, o caso não segue para a página que as discute — segue para outra,
    que trata de conduzir sem elas. É a única ramificação do caso que não é
    escolha de conduta, e é a que mais ensina.
    """
    return _pag("resultados", ident, kicker=texto(kicker), tt=texto(titulo),
                de=de, fundo=fundo, intro=texto(introducao), nota=texto(nota),
                laminas=laminas or {}, rota=_rota(rota))


# ─────────────────────────── perguntas ───────────────────────────


def alt(txt, porque, *, certa=False) -> dict:
    if not porque.strip():
        raise ValueError(f"alternativa sem comentário: {txt!r}")
    return {"t": texto(txt), "c": texto(porque), "ok": 1 if certa else 0}


def pergunta(ident, kicker, enunciado, alternativas, *, fundo="",
             titulo_resposta="", nota="", segue="") -> dict:
    """A pergunta do //New England// é, na maioria das vezes, de MÚLTIPLA
    seleção a partir de uma lista longa: "quais três são as causas mais
    prováveis", "quais sete diagnósticos considerar". Ler as 333 perguntas dos
    71 casos interativos deixou isso claro — 104 delas começam com "Quais".

    A diferença não é cosmética. Numa lista de nove diagnósticos plausíveis,
    dos quais quatro contam, não existe a alternativa obviamente sensata que
    denuncia a resposta: é preciso incluir E excluir, e o distrator é sempre
    uma doença que um bom clínico consideraria."""
    certas = [a for a in alternativas if a["ok"]]
    if not 1 <= len(certas) <= 5:
        raise ValueError(f"pergunta {ident!r}: use de 1 a 5 corretas")
    if not 4 <= len(alternativas) <= 10:
        raise ValueError(f"pergunta {ident!r}: use de 4 a 10 alternativas")
    if len(certas) == len(alternativas):
        raise ValueError(f"pergunta {ident!r}: todas corretas não é pergunta")
    if not titulo_resposta.strip():
        raise ValueError(f"pergunta {ident!r}: sem título de resposta")
    return _pag("pergunta", ident, kicker=texto(kicker),
                enunciado=texto(enunciado), alts=alternativas,
                escolhas=len(certas), fundo=fundo,
                tr=texto(titulo_resposta), nota=texto(nota), segue=segue)


def caminho(rotulo, vai_para, porque, *, rotulo_curto="") -> dict:
    if not porque.strip():
        raise ValueError(f"caminho {rotulo!r} sem justificativa")
    return {"r": texto(rotulo), "vai": vai_para, "c": texto(porque),
            "rc": texto(rotulo_curto)}


def bifurcacao(ident, kicker, titulo, enunciado, caminhos, *, fundo="",
               nota="") -> dict:
    if not 2 <= len(caminhos) <= 3:
        raise ValueError(f"bifurcação {ident!r}: use 2 ou 3 caminhos")
    return _pag("bifurcacao", ident, kicker=texto(kicker), tt=texto(titulo),
                enunciado=texto(enunciado), caminhos=caminhos, fundo=fundo,
                nota=texto(nota))


# ─────────────────── o que cada decisão custou ───────────────────


def consequencia(*, chave, titulo, quando, porque, dias=0, tfg=0) -> dict:
    """Uma consequência rastreável de uma decisão — não um comentário.

    Conduzir o caso ao vivo mostrou que o que ensina não é o desfecho: é a
    **distância entre o desfecho que se teve e o que se teria**. Antibiótico
    antes da cultura não faz mal no dia em que é dado; faz mal no oitavo, e
    numa peça de botão isso nunca chega ao aluno porque o desfecho é o mesmo
    para todo mundo.

    `quando` é declarativo e só tem duas formas, de propósito:

        {"sem": ["Hemocultura"]}      dispara se NENHUM da lista foi pedido
        {"escolheu": ["b1", 2]}       dispara se a bifurcação foi por ali

    `dias` e `tfg` são o preço: dias a mais de internação e mililitros a menos
    de filtração na alta. São inferência autoral, como todo o resto do caso —
    e é por isso que cada um vem com o `porque` que o sustenta.
    """
    if set(quando) - {"sem", "escolheu"}:
        raise ValueError("quando: use {'sem': [...]} ou {'escolheu': [id, n]}")
    if dias == 0 and tfg == 0:
        raise ValueError(f"consequência {chave!r} sem preço não é consequência")
    return {"k": chave, "tt": texto(titulo), "q": quando, "pq": texto(porque),
            "d": dias, "t": tfg}


def balanco(ident, kicker, titulo, *blocos, base_dias, base_tfg,
            base_creatinina, consequencias, fundo="", nota="") -> dict:
    """A última tela: o que aconteceu, o que teria acontecido, e a diferença."""
    return _pag("balanco", ident, kicker=texto(kicker), tt=texto(titulo),
                corpo="".join(blocos), bd=base_dias, bt=base_tfg,
                bc=texto(base_creatinina), cons=consequencias, fundo=fundo,
                nota=texto(nota))


def desfecho(ident, titulo, *blocos, qualidade, porque, fundo="",
             kicker="Desfecho", fecho="") -> dict:
    """`fecho` é a página para onde o caso vai depois do desfecho.

    Os passos que o documento de referência chama de INCERTEZA e RETROSPECTIVA
    — o que ficou sem explicação, e onde dava para ter chegado antes — são os
    dois que quase toda imitação esquece, e são justamente os que transformam o
    material em ensino de raciocínio. Eles vêm depois do desfecho, iguais para
    os três ramos, porque a lição não muda com a escolha."""
    if qualidade not in ("melhor", "medio", "pior"):
        raise ValueError("qualidade: 'melhor', 'medio' ou 'pior'")
    if not porque.strip():
        raise ValueError(f"desfecho {ident!r} sem explicação fisiológica")
    return _pag("desfecho", ident, kicker=texto(kicker), tt=texto(titulo),
                corpo="".join(blocos), q=qualidade, porque=texto(porque),
                fundo=fundo, fecho=fecho)


# ─────────────────────────── montagem ───────────────────────────


def montar(caso) -> str:
    raiz = Path(__file__).parent
    css = (raiz / "etapas.css").read_text(encoding="utf-8")
    js = (raiz / "etapas.js").read_text(encoding="utf-8")

    cache: dict[str, str] = {}

    def embutir(nome: str) -> str:
        if nome not in cache:
            caminho_img = caso.IMG / nome
            if not caminho_img.exists():
                raise FileNotFoundError(f"imagem não encontrada: {caminho_img}")
            tipo = mimetypes.guess_type(nome)[0] or "image/jpeg"
            cache[nome] = ("data:" + tipo + ";base64,"
                           + base64.b64encode(caminho_img.read_bytes()).decode())
        return cache[nome]

    def resolver(v):
        """Anota que a imagem é usada, mas deixa o NOME no lugar do arquivo.

        Inlinear o data: URI aqui custava caro: a cena de admissão é o fundo de
        quase todas as etapas, e cada ocorrência carregava uma cópia inteira do
        base64 — o mesmo quarto de megabyte, vinte vezes. O arquivo saía com
        8 MB de imagem repetida. Agora cada imagem viaja uma vez, numa tabela,
        e a etapa guarda só a chave.
        """
        if isinstance(v, dict):
            for k, x in v.items():
                if k in ("fundo", "img") and x:
                    embutir(x)
            return {k: (x if k in ("fundo", "img") and x else resolver(x))
                    for k, x in v.items()}
        if isinstance(v, list):
            return [resolver(x) for x in v]
        return v

    dados = {
        "caso": {"titulo": caso.TITULO, "rodape": caso.RODAPE,
                 "sistemas": SISTEMAS},
        "etapas": resolver(caso.ETAPAS),
        "banco": {e["n"]: e for e in caso.BANCO},
        "revisao": [dict(r, rotulo=texto(r["rotulo"]), porque=texto(r["porque"]))
                    for r in getattr(caso, "REVISAO", [])],
    }
    # Figura anotada e boneco chegam como HTML pronto, e o nome do arquivo
    # viaja dentro do atributo `data-img` — fora do alcance do `resolver`, que
    # só olha as chaves "fundo" e "img". Sem esta varredura a foto da crescente
    # saía do build sem endereço nenhum e a página abria com um vazio.
    def _varrer(v):
        if isinstance(v, str):
            for nome in re.findall(r'data-img="([^"]+)"', v):
                embutir(nome)
        elif isinstance(v, dict):
            for x in v.values():
                _varrer(x)
        elif isinstance(v, (list, tuple)):
            for x in v:
                _varrer(x)

    _varrer(dados)
    dados["imgs"] = cache          # cada imagem uma vez só, no fim

    return (
        '<!doctype html>\n<html lang="pt-BR">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width,initial-scale=1">\n'
        f"<title>{caso.TITULO}</title>\n<style>\n{css}\n</style>\n</head>\n"
        '<body>\n<div id="trilho"></div>\n<div id="palco"></div>\n'
        '<div id="pe"></div>\n'
        '<script type="application/json" id="dados">'
        + json.dumps(dados, ensure_ascii=False).replace("</", "<\\/")
        + f"</script>\n<script>\n{js}\n</script>\n</body>\n</html>\n"
    )

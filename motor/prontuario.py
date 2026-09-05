"""Modo prontuário: o caso deixa de ser um baralho e vira uma condução.

O baralho, por mais que ramifique, empurra. O grupo pede um exame e duas telas
depois aparece outro, que ninguém pediu, porque a tela seguinte já estava
escrita. Aqui não existe tela seguinte: existe um paciente, um relógio e uma
lista de coisas que se pode fazer. O que entra no prontuário é o que foi feito.

    · o relógio só anda quando alguém faz alguma coisa, ou espera;
    · exame pedido entra na hora; o resultado entra quando fica pronto;
    · a doença progride sozinha enquanto não é tratada, e o número mostra;
    · o desfecho é calculado do estado final, não escolhido de uma lista.

O que o autor escreve aqui é declarativo e sem código: quem se pode perguntar,
o que se pode examinar, o que se pode prescrever, a que velocidade a doença
anda e que condição define cada desfecho. O motor em JavaScript não sabe nada
de vasculite — ele lê estas tabelas.
"""

from __future__ import annotations

import json

from .conteudo import texto

# ─────────────────────────── o paciente ───────────────────────────

# Os campos que o cabeçalho mostra e que a evolução move. `passo` é a menor
# variação que vale exibir; abaixo dela o número não pisca à toa.
CAMPOS = {
    "creatinina": dict(rotulo="Creatinina", unidade=" mg/dL", casas=1,
                       sobe_e_piora=True, passo=0.1),
    "spo2": dict(rotulo="SpO₂", unidade="%", casas=0, sobe_e_piora=False, passo=1),
    "hb": dict(rotulo="Hemoglobina", unidade=" g/dL", casas=1,
               sobe_e_piora=False, passo=0.1),
    "potassio": dict(rotulo="Potássio", unidade=" mEq/L", casas=1,
                     sobe_e_piora=True, passo=0.1),
    "diurese": dict(rotulo="Diurese", unidade=" mL/h", casas=0,
                    sobe_e_piora=False, passo=5),
}

SINAIS = {
    "imunossupressao": "imunossupressão em curso",
    "dialise": "em diálise",
    "vm": "em ventilação mecânica",
    "plasmaferese": "plasmaférese em curso",
    "antibiotico": "antibiótico de amplo espectro",
    "culturas_colhidas": "culturas colhidas",
    "culturas_prejudicadas": "culturas colhidas após o corticoide",
    "fibrose": "crescentes em fibrose",
    "neutropenia": "neutropenia febril",
    "infeccao": "infecção em curso",
    "diagnostico": "diagnóstico estabelecido",
    "o2": "oxigênio suplementar",
    "cfx_plena": "ciclofosfamida em dose plena",
    "cfx_ajustada": "ciclofosfamida com dose ajustada",
    "rituximabe": "rituximabe",
    "pjp": "profilaxia para Pneumocystis",
    "transfundido": "transfundido",
    "medicacoes_revisadas": "lista de medicamentos revisada",
    "sedimento_visto": "sedimento urinário examinado",
    "hemorragia_macica": "hemorragia alveolar em progressão",
}


def paciente(*, identificacao, leito, admissao, queixa, estado, resumo) -> dict:
    """A abertura: é tudo o que se sabe antes de perguntar qualquer coisa."""
    desconhecidos = set(estado) - set(CAMPOS)
    if desconhecidos:
        raise ValueError(f"campo de estado desconhecido: {sorted(desconhecidos)}")
    faltando = set(CAMPOS) - set(estado)
    if faltando:
        raise ValueError(f"estado inicial incompleto: falta {sorted(faltando)}")
    return {"id": identificacao, "leito": leito, "admissao": admissao,
            "queixa": queixa, "estado": estado, "resumo": texto(resumo)}


# ─────────────────────────── as ações ───────────────────────────


def _acao(tipo, chave, rotulo, *, minutos, texto_, grupo="", exige=(), liga=(),
          uma_vez=True, detalhe="", perigo="", sin=()) -> dict:
    """Uma coisa que se pode fazer. `texto_` é o que ela escreve no prontuário.

    `exige` são sinalizadores que precisam estar ligados para a ação existir —
    é como a conduta de resgate só aparece depois de o paciente piorar, sem que
    o caso precise anunciá-la antes.
    """
    return {"t": tipo, "k": chave, "r": texto(rotulo), "min": minutos,
            "x": texto(texto_), "g": texto(grupo), "exige": list(exige),
            "liga": list(liga), "uma": 1 if uma_vez else 0,
            "d": texto(detalhe), "p": texto(perigo), "s": list(sin)}


def perguntar(chave, rotulo, resposta, *, minutos=4, grupo="Anamnese",
              liga=(), detalhe="", sin=()) -> dict:
    """Uma pergunta da anamnese. A resposta só existe se alguém perguntar.

    É aqui que mora metade da lição: a revisão da lista de medicamentos, a
    epidemiologia, a exposição ocupacional. No baralho isso vinha impresso; aqui
    quem não pergunta não sabe, e o prontuário registra que não perguntou.
    """
    return _acao("anamnese", chave, rotulo, minutos=minutos, texto_=resposta,
                 grupo=grupo, liga=liga, detalhe=detalhe, sin=sin)


def examinar(chave, rotulo, achado, *, minutos=3, grupo="Exame físico",
             liga=(), detalhe="", sin=()) -> dict:
    """Uma manobra do exame físico, com o que ela mostra."""
    return _acao("exame", chave, rotulo, minutos=minutos, texto_=achado,
                 grupo=grupo, liga=liga, detalhe=detalhe, sin=sin)


def prescrever(chave, rotulo, registro, *, minutos=20, grupo="Conduta",
               efeito=None, exige=(), liga=(), uma_vez=True, detalhe="",
               perigo="", perigo_sem=(), perigo_liga=(), sin=(),
               pede=()) -> dict:
    """Uma conduta. `efeito` é a mudança imediata no estado; a mudança lenta
    vem da tabela de evolução, que passa a valer pelos sinalizadores ligados.

    `perigo` é o que a conduta cobra quando é feita fora de hora — texto que
    entra no prontuário, não um aviso antes do clique. Avisar antes seria
    decidir pelo grupo.
    """
    if perigo and not perigo_sem:
        raise ValueError(f"conduta {chave!r}: perigo sem a condição que o dispara")
    a = _acao("conduta", chave, rotulo, minutos=minutos, texto_=registro,
              grupo=grupo, exige=exige, liga=liga, uma_vez=uma_vez,
              detalhe=detalhe, perigo=perigo, sin=sin)
    a["ef"] = efeito or {}
    # o preço de fazer fora de hora: só cobra se o sinalizador que protegeria
    # a conduta não estiver ligado, e o texto entra no prontuário depois do
    # fato — avisar antes do clique seria decidir pelo grupo
    a["ps"] = list(perigo_sem)
    a["pl"] = list(perigo_liga)
    # exames que a própria conduta solicita: "colher três pares de hemocultura"
    # tem de colocar a hemocultura na fila, não só acender um sinalizador
    a["pede"] = list(pede)
    return a


def efeito(**campos) -> dict:
    desconhecidos = set(campos) - set(CAMPOS)
    if desconhecidos:
        raise ValueError(f"efeito sobre campo desconhecido: {sorted(desconhecidos)}")
    return campos


# ─────────────────────────── exames complementares ───────────────────────────

# Quanto cada categoria do banco leva para ficar pronta, em minutos. É o número
# que faz o caso ter física: pedir sorologia e esperar por ela custa dois dias
# de rim, e é por isso que a conduta não pode depender dela.
ESPERA = {
    "Urina": 40,
    "Gasometria": 20,
    "Hemograma": 45,
    "Bioquímica": 60,
    "Coagulação": 60,
    "Inflamação": 90,
    "Imagem": 180,
    "Procedimento": 240,
    "Microbiologia": 2880,
    "Sorologia": 1440,
    "Imunologia": 2880,
    "Anatomia patológica": 4320,
    "Neurofisiologia": 720,
}


# ─────────────────────────── a abertura, em alíquotas ───────────────────────
#
# A história não é um menu de perguntas. Ela é contada — em pedaços, no ritmo
# de quem escuta, como no //Case Records//. O que continua sendo pergunta é o
# que o paciente não conta espontaneamente: os medicamentos que ele não
# considera medicamento, a exposição que ele não relaciona com nada.


def aliquota(titulo, *paragrafos, minutos=0) -> dict:
    return {"tt": texto(titulo), "p": [texto(x) for x in paragrafos],
            "min": minutos}


# ─────────────────────────── pontos de decisão ───────────────────────────
#
# Não são todas as condutas listadas o tempo todo numa lateral — isso é prova
# de múltipla escolha com doze alternativas à vista. São dois ou três caminhos
# concretos, oferecidos no momento em que o caso realmente exige uma decisão, e
# a linha de comando continua aberta para quem quiser fazer outra coisa.


def caminho(rotulo, *, faz=(), espera=0, porque="") -> dict:
    """Um caminho é um atalho por dentro da mesma máquina: ele executa ações
    que já existem. Não há regra escondida atrás dele."""
    if not faz and not espera:
        raise ValueError(f"caminho {rotulo!r} não faz nada")
    return {"r": texto(rotulo), "faz": list(faz), "esp": espera,
            "porque": texto(porque)}


def decisao(chave, pergunta, caminhos, *, quando, contexto="",
            volta_em=None) -> dict:
    """Aparece quando as condições passam a valer.

    `volta_em` são as horas depois das quais a mesma decisão pode reaparecer se
    a situação persistir. Uma saturação que segue caindo depois de "reavaliar em
    uma hora" tem de voltar a perguntar; uma escolha de indução, não.
    """
    if not 2 <= len(caminhos) <= 4:
        raise ValueError(f"decisão {chave!r}: use de 2 a 4 caminhos")
    return {"k": chave, "q": texto(pergunta), "c": texto(contexto),
            "quando": list(quando), "caminhos": caminhos,
            "volta": volta_em}


# ─────────────────────────── a evolução ───────────────────────────


def taxa(**campos) -> dict:
    """Variação por hora. Somam-se as taxas de todos os sinalizadores ligados."""
    desconhecidos = set(campos) - set(CAMPOS)
    if desconhecidos:
        raise ValueError(f"taxa sobre campo desconhecido: {sorted(desconhecidos)}")
    return campos


def marco(horas, registro, *, liga=(), desliga=(), exige=(), impede=()) -> dict:
    """Algo que acontece sozinho, na hora certa, se as condições valerem.

    A fibrose das crescentes é o exemplo: às 72 horas sem tratamento, o que era
    reversível deixa de ser, e o prontuário registra isso sem que ninguém tenha
    clicado em nada.
    """
    return {"h": horas, "x": texto(registro), "liga": list(liga),
            "desliga": list(desliga), "exige": list(exige),
            "impede": list(impede)}


def rumo(**campos) -> dict:
    """Para onde o campo caminha, e em quanto tempo anda metade do caminho.

        rumo(creatinina=(1.6, 40))   alvo 1,6 mg/dL, meia-vida de 40 horas

    Taxa linear serve para a doença que piora: ela não tem para onde ir. Não
    serve para a que melhora — somada por tempo suficiente ela leva a
    creatinina a zero e a saturação a 100, que é caricatura, não fisiologia. A
    recuperação tem patamar, e chega nele desacelerando.
    """
    for c, v in campos.items():
        if c not in CAMPOS:
            raise ValueError(f"rumo sobre campo desconhecido: {c!r}")
        if not (isinstance(v, tuple) and len(v) == 2 and v[1] > 0):
            raise ValueError(f"rumo de {c!r}: use (alvo, meia_vida_em_horas)")
    return {c: list(v) for c, v in campos.items()}


def evolucao(*, base, quando=None, alvos=None, marcos=()) -> dict:
    """`alvos` sobrepõe a taxa base do campo; a ordem de declaração decide quem
    ganha quando dois sinalizadores miram o mesmo campo — o último vence."""
    return {"base": base, "quando": quando or {}, "alvos": alvos or {},
            "marcos": list(marcos)}


# ─────────────────────────── os desfechos ───────────────────────────


def campo(nome, op, valor) -> dict:
    if nome not in CAMPOS and nome != "horas":
        raise ValueError(f"condição sobre campo desconhecido: {nome!r}")
    if op not in ("<", "<=", ">", ">=", "=="):
        raise ValueError(f"operador inválido: {op!r}")
    return {"c": nome, "op": op, "v": valor}


def sinal(nome, presente=True) -> dict:
    if nome not in SINAIS:
        raise ValueError(f"sinalizador desconhecido: {nome!r}")
    return {"s": nome, "v": bool(presente)}


def desfecho(chave, titulo, *paragrafos, quando, qualidade="medio",
             porque="", automatico=False) -> dict:
    """Um final. `quando` é uma lista de condições, todas verdadeiras.

    A ordem da lista de desfechos importa: vence o primeiro que casar. O último
    deve ser incondicional, para que nunca exista um estado sem desfecho.
    """
    if qualidade not in ("melhor", "medio", "pior"):
        raise ValueError("qualidade deve ser 'melhor', 'medio' ou 'pior'")
    if not porque.strip():
        raise ValueError(f"desfecho {chave!r} sem explicação fisiológica")
    return {"k": chave, "t": texto(titulo), "q": qualidade,
            "p": [texto(x) for x in paragrafos], "quando": list(quando),
            "porque": texto(porque), "auto": 1 if automatico else 0}


# ─────────────────────────── montagem ───────────────────────────


def _imagens(caso) -> dict:
    import base64
    import mimetypes
    saida = {}
    for nome, spec in getattr(caso, "IMAGENS", {}).items():
        caminho = caso.IMG / spec["arquivo"]
        if not caminho.exists():
            raise FileNotFoundError(f"imagem não encontrada: {caminho}")
        tipo = mimetypes.guess_type(caminho.name)[0] or "image/jpeg"
        b64 = base64.b64encode(caminho.read_bytes()).decode()
        saida[nome] = {"src": f"data:{tipo};base64,{b64}",
                       "legenda": texto(spec["legenda"]),
                       "credito": texto(spec["credito"])}
    return saida


def dados_do_caso(caso) -> str:
    """Serializa tudo o que o motor precisa saber sobre este caso."""
    blocos = {
        "paciente": caso.PACIENTE,
        "abertura": getattr(caso, "ABERTURA", []),
        "decisoes": getattr(caso, "DECISOES", []),
        "campos": CAMPOS,
        "sinais": SINAIS,
        "acoes": caso.ACOES,
        "espera": ESPERA,
        "evolucao": caso.EVOLUCAO,
        "desfechos": caso.DESFECHOS,
        "banco": caso.BANCO,
        "revisao": [dict(r, rotulo=texto(r["rotulo"]),
                         porque=texto(r["porque"]))
                    for r in getattr(caso, "REVISAO", [])],
        # exame cujo resultado, ao chegar, muda o estado do paciente: é assim
        # que o painel imunológico "fecha o diagnóstico" sem que nenhum slide
        # precise anunciá-lo
        "gatilhos": getattr(caso, "GATILHOS", {}),
        # a imagem viaja embutida: o arquivo tem de abrir por duplo clique,
        # sem servidor e sem rede
        "imagens": _imagens(caso),
    }
    return "".join(
        f'<script type="application/json" id="d-{k}">'
        f"{json.dumps(v, ensure_ascii=False)}</script>"
        for k, v in blocos.items()
    )


def montar(caso) -> str:
    """A página inteira, num arquivo só, sem dependência externa."""
    from pathlib import Path
    raiz = Path(__file__).parent
    css = (raiz / "prontuario.css").read_text(encoding="utf-8")
    js = (raiz / "prontuario.js").read_text(encoding="utf-8")
    return (
        "<!doctype html>\n<html lang=\"pt-BR\">\n<head>\n"
        "<meta charset=\"utf-8\">\n"
        "<meta name=\"viewport\" content=\"width=device-width,initial-scale=1\">\n"
        f"<title>{caso.TITULO}</title>\n"
        f"<style>\n{css}\n</style>\n</head>\n<body>\n"
        "<header id=\"topo\">"
        "<div id=\"pac\"></div><div id=\"hora\"></div>"
        "<div id=\"vitais\"></div></header>\n"
        "<div id=\"flags\"></div>\n"
        "<main id=\"reg\"></main>\n"
        "<div id=\"barra\"><div id=\"resp\"></div>"
        "<div class=\"cmd-linha\">"
        "<label for=\"cmd\">O que você faz agora?</label>"
        "<input id=\"cmd\" autocomplete=\"off\" spellcheck=\"false\" "
        "placeholder=\"peço o sedimento · ausculto o tórax · aguardo seis horas\">"
        "<button id=\"ajuda\" title=\"exemplos\">?</button>"
        "<button id=\"encerrar\">encerrar</button>"
        "</div></div>\n"
        "<div id=\"modal\"></div>\n"
        f"{dados_do_caso(caso)}\n"
        f"<script>\n{js}\n</script>\n</body>\n</html>\n"
    )

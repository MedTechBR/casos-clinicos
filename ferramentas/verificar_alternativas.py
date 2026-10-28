"""Impede pistas editoriais nas alternativas visíveis de todos os casos públicos.

A justificativa pode explicar que um achado não basta. O rótulo da opção não
pode denunciar o distrator com 'única', 'isolada', 'principal' ou equivalentes.
Uso: python3 ferramentas/verificar_alternativas.py
"""
import importlib
import re
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from nomes_publicos import PUBLICO
PISTAS=re.compile(r'\b(?:principa(?:l|is)|[úu]nic[oa]s?|isolad[oa](?:s|mente)?|exclusiv[oa](?:s|mente)?|apenas|somente|s[oó]|sozinh[oa]s?)\b|explica[çc][ãa]o suficiente|explicad[oa] suficientemente',re.I)
falhas=[];n=0
for slug in PUBLICO:
 m=importlib.import_module('casos.'+slug+'.etapas')
 for e in m.ETAPAS:
  alts=[a['t'] for a in e.get('alts',[])]+[a['r']for a in e.get('caminhos',[])]+[a['rc']for a in e.get('caminhos',[]) if a.get('rc')]
  for t in alts:
   n+=1
   if PISTAS.search(t):falhas.append((slug,e['k'],t))
  if e.get('alts'):
   assert len({a['t']for a in e['alts']})==len(e['alts']),(slug,e['k'],'alternativas repetidas')
   assert sum(bool(a['ok'])for a in e['alts'])==e['escolhas'],(slug,e['k'],'gabarito inconsistente')
for f in falhas:print('REVISAR',*f)
assert not falhas,f'{len(falhas)} alternativas com pistas editoriais'
print(f'{len(PUBLICO)} casos · {n} rótulos de alternativas e caminhos conferidos · nenhuma pista editorial')

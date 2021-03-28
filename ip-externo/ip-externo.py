# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 21:01:15 2021

@author: Clauber

Ferramente Verificador de um ip externo.
A biblioteca re permite operações com expressões regulares 
A biblioteca json fornece operação de codificação e decodificação JSON
A bilioteca urllib.request import urlopen fornece funções e classes que ajudam 
a abrir URLs
Site https://ipinfo.io/json para verificar o ip externo

"""
import re
import json
from urllib.request import urlopen

url = 'https://ipinfo.io/json'

resposta = urlopen(url)
dados = json.load(resposta)

ip = dados['ip']
org   = dados['org']
cid = dados['city']
pais = dados['country']
regiao = dados['region']
hostname = dados['hostname']

print ('Detalhes do IP externo\n')
print ('IP: {4}\nHostName: {5}\nRegião: {1}\nPais: {2}\nCidade: {3}\nOrg.: {0}'.format(org,
                                                                        regiao,pais,cid,ip,hostname))

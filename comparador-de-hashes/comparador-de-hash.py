# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 15:26:50 2021

@author: Clauber
"""

import hashlib

arquivo_1 = 'arquivo-1.txt'
arquivo_2 = 'arquivo-2.txt'
#oj hash_1 recebe o construtor new da biblioteca hashlib informando o alg de hash será utilizado
#ripemd160 alg de 160 bits
hash_1 = hashlib.new('ripemd160')
#passando a informação para o arquivo o método de leitura binário
hash_1.update(open(arquivo_1, 'rb').read())

hash_2 = hashlib.new('ripemd160')

hash_2.update(open(arquivo_2, 'rb').read())

if hash_1.digest() != hash_2.digest():
    print(f'O arquivo: {arquivo_1} é diferente do arquivo: {arquivo_2}')
    print('O hash do arquivo arquivo-1.txt é: ', hash_1.hexdigest())
    print('O hash do arquivo arquivo-2.txt é: ', hash_2.hexdigest())
else:
    print(f'O arquivo: {arquivo_1} é igual ao arquivo: {arquivo_2}')
    print('O hash do arquivo arquivo-1.txt é: ', hash_1.hexdigest())
    print('O hash do arquivo arquivo-2.txt é: ', hash_2.hexdigest())


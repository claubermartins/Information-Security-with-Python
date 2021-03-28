# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 13:28:45 2021

@author: Clauber
"""
#Wordlists são arquivos contendo uma palavra por linha e são utilizados para ataque
#de força bruta como quebra de autenticação
#A biblioteca intertools fornece a condição para permutação e combinação
import itertools

string = input("String a ser permutada: ")

resultado = itertools.permutations(string, len(string))

for i in resultado:
    print(''.join(i))


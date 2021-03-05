# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 02:30:29 2021

@author: Clauber
"""

import random, string

tamanho = 20
#tamanho = int(input('Digite o tamanho de sua senha: '))
#maiusculas e minusculas
chars = string.ascii_letters + string.digits +'!@#$%¨&*()-ç'
#minusculas
#chars = string.ascii_lowercase + string.digits +'!@#$%¨&*()-Çç'
#maiuscula
#chars = string.ascii_lowercase + string.digits +'!@#$%¨&*()-Çç'
rnd = random.SystemRandom()
#retorna uma lista com caracteres random
print(''.join(rnd.choice(chars) for i in range(tamanho)))
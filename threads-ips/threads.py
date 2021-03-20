# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 17:58:47 2021

@author: Clauber
"""
#Com este exemplo, podemos criar um teste de stress, scan simultaneo, ou seja,
#envio de requisições 
#biblioteca para fazer o multiThread
from threading import Thread
import time
#função para colocar dois carros de corrida que competirão entre si.
def carro(velocidade, piloto):
    trajeto = 0
    while trajeto <= 100:
        trajeto += velocidade
        time.sleep(0.5)
        print('Piloto: {} km: {} \n '.format(piloto, trajeto))

t_carro1 = Thread(target = carro, args = [1, 'Clauber'])
t_carro2 = Thread(target = carro, args = [2, 'Bot'])

t_carro1.start()
t_carro2.start()

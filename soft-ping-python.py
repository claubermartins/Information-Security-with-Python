# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 20:04:30 2021

@author: Clauber
"""
#requisição ICMP
#importando a biblioteca os para integrar os programas e resursos do S.O
import os
#print ("#" *50)
#var recebe o ip do usuário
ip_host = input("Digite o endereço de ip a ser verificado: ")
#print ("-" *50)
#chamando system da biblioteca os -comando ping com 10 pacotes
os.system('ping -n 10 {}'.format(ip_host))
#print ("-" *50)

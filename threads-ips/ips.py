# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 18:57:26 2021

@author: Clauber
"""
#biblioteca para manipular ips, cálculos de ips,
import ipaddress
#indentificando a rede
'''ip = "192.168.0.100/24"

rede = ipaddress.ip_network(ip, strict=False) 
print(rede)
'''
#imprimindo todos os endereços ips de uma rede
ip = "192.168.0.0/24"

rede = ipaddress.ip_network(ip, strict=False) 
print(rede)
for ip in rede:
    print(ip)
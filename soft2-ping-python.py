# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 14:20:05 2021

@author: Clauber
"""

import os
import time

with open('hosts.txt') as file:
    dump = file.read()
    dump = dump.splitlines()
    
    for ip in dump:
#        print (ip)
        print('Verificando o ip utilizando o protocolo ICMP: ', ip)
        print('-'*50)
        os.system('ping -n 5 {}'.format(ip))
        print('-'*50)
        time.sleep(5)
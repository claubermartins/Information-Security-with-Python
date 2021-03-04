# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 01:25:43 2021

@author: Clauber
"""

#Desenvolvimento de um cliente UDP, onde o cliente se conectarar com o serv e o
#servidor enviará dados para o cliente
import socket
#AF_INET(protocolo ip);SOCK_DGRAM(protocolo UDP); s (obj de conexão)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print('Cliente Socket criado com socesso!')

host = 'localhost'
porta = 5433
mensagem = 'Oi, tudo bem?'
#enviando a mensagem
try:
    print('Cliente: ' + mensagem)
    #enviando a mensagem empacotada com pacotes UDP para o servidor
    s.sendto(mensagem.encode(), (host, 5432))
    #var que recebe os dados de tamanho x bytes do serv e desempacota
    dados, servidor = s.recvfrom(4096)
    dados = dados.decode()
    print("Cliente: " + dados)
finally: 
    print("Cliente: fechando a conexão" )
    s.close()
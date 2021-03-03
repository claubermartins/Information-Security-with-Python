# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 01:56:34 2021

@author: Clauber
"""
import socket
#obj de conexão
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("Socket criado com socesso!")

host = 'localhost'
port = 5432
#fazendo a ligação a partir do host e da porta do host
s.bind((host, port))
mensagem = '\n Servidor: Oi cliente, estou bem.'
#enquanto for verdadeiro a conexão, o serv vai receber 4096 bytes atraves do obj conexão
while 1:
    dados, end = s.recvfrom(4096)
    if dados:
        print('Servidor enviando mensagem...')
#enviando a mensagem empacotada com pacotes UDP para o cliente
        s.sendto(dados + (mensagem.encode()), end)


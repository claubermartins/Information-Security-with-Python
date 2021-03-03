# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 15:11:23 2021

@author: Clauber
"""
#biblioteca para fazer o relacionamento da placa de rede com o S.O
import socket
#biblioteca que fornece o acesso à algumas var e funções que tem interação com o Python
import sys
#função para fazer a conexão TCP/IP
def main():
    try:
        #AF_INET(protocolo ip); SOCK_STREAM(protocolo tcp)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as e:
        print("A conexão falhou!")
        print("Error: {}".fortmat(e))
        sys.exit()
    print("Socket criado com sucesso.")
    
    hostAlvo = input("Digite o host a ser conectado: ")
    portaAlvo = input("Digite a porta a ser conectada: ")
    
    try:
        s.connect((hostAlvo, int(portaAlvo)))
        print("Cliente TCP conectado com sucesso no host: " + hostAlvo + "e na porta: " + portaAlvo)
        s.shutdown(2)
    except socket.error as e:
        print("A conexão falhou no host: " + hostAlvo + "e na porta: " + portaAlvo)
        print("Error: {}".format(e))
        sys.exit()
#Indentação 
if __name__ == "__main__":
    main()
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 20:39:24 2021

@author: Clauber

Biblioteca ctypes fornece tipos de dados compatíveis com C e funções de chamada
em DLLs ou bibliotecas compartilhadas

"""
import ctypes 

pasta = input("Digite o caminho da pasta a ser ocultada: ")

atributo_ocultar = 0x02

#retorno = ctypes.windll.kernel32.SetFileAttributesW('ocultar.txt', atributo_ocultar)
retorno = ctypes.windll.kernel32.SetFileAttributesW(pasta, atributo_ocultar)

if retorno:
    print("Arquivo foi ocultado")
else:
    print("Arquivo não foi ocultado")


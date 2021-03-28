# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 17:44:39 2021

@author: Clauber

Biblioteca phonenumbers fornece vários recursos, como informações básicas de um
telefone, validação de um número de telefone, etc.

"""
import phonenumbers
#usada para informar a localização do número de teleffone
from phonenumbers import geocoder

telefone = input('Digite o telefone no formato +551140028922: ')

telefone_numero = phonenumbers.parse(telefone)

print(geocoder.description_for_number(telefone_numero, 'pt'))


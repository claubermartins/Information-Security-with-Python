# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 13:36:51 2021

@author: Clauber

Web scraper é uma ferramenta  de mineração de coleta de dados web, uma forma de
mineração que permite a extração de dados de sites da web convertendo-os em 
informação estruturada para análise.

"""
from bs4 import BeautifulSoup
import requests

#obj site recebendo o conteúdo da requisição http do site
#site = requests.get("http://www.exemplo.com/projeto/index.html").content
site = requests.get("https://web.facebook.com/?_rdc=1&_rdr").content
#objeto soup baixando do site o html
soup = BeautifulSoup(site, 'html.parser')
#tranforma html em string e o print vai exibir o html da página
#print(soup.prettify())
#pegando a tag e a classe 
informacao  = soup.find("span", class_="_55pe")
print(informacao.string) 
#imprimindo a estrutura html no formato string
print(soup.title.string)
#tentando captar informação relacionada a admin da página
print(soup.find('admin'))

                      
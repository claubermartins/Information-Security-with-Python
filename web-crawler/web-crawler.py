# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 16:22:14 2021

@author: Clauber

Web Crawler é uma ferramenta usada para encontrar, ler e indexar páginas de um
site. É como um robo que captura informações de cada um dos links que encontra
pela frente, cadastra e compreende o que é mais relevante.
É muito utilizado em levantamento de informações em processo de Pentest

"""
#biblioteca operator exporta um conjunto de funções eficientes correspondentes
#aos operadores intrísecos do Python (+ - * / not and, etc)
#biblioteca collections nos ajuda a preencher e manipular eficientemente as es
#trutura de dados como tuplas, dicionários e lista.
import requests
from bs4 import BeautifulSoup
import operator
from collections import Counter

#função para armazenar o conteudo do site 
def start(url):
    wordlist = []
    source_code = requests.get(url).text
    #achando o conteúdo html, se cria um for para tudo com div e class e trans
    #formar em texto
    soup = BeautifulSoup(source_code, 'html.parser')

    for each_text in soup.findAll('div', {'class': 'entry-content'}):
        content = each_text.text
        #transformando o conteúdo em letras minúsculas em uma linha
        words = content.lower().split()
        
        for each_word in words:
            wordlist.append(each_word)
        clean_wordlist(wordlist)
#função para remover simbolos indesejados do word list e substituir por nada('')
def clean_wordlist(wordlist):
    clean_list = []
    for word in wordlist:
        symbols = '!@#$%^&*()_-+={[}]|\;:"<>,.'
        for i in range (0, len(symbols)):
            word = word.replace(symbols[i], '')
        if len(word) > 0:
            clean_list.append(word)
    create_dictionary(clean_list)
#função que cria um dicionário fazendo contagem das palavras mostrando as 
#palavras mais ocorrencia no site    
def create_dictionary(clean_list):
    word_count = {}
    
    for word in clean_list:
        if word in word_count:
           word_count[word] += 1
        else:
            word_count[word] = 1
            
    for key, value in sorted(word_count.items(),
                             key = operator.itemgetter(1)):
        print("% s : % s" % (key,value))
    c = Counter(word_count)
    
    top = c.most_common(10)
    print (top)
#chama a função main(start)
if __name__ == '__main__':
    start("https://www.geeksforgeeks.org/python-programming-language/?ref=leftbar")

        
        


# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 21:51:29 2021

@author: Clauber
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 21:44:41 2021

@author: Clauber

Ferramenta gráfica para abrir o navegador 
A biblioteca webbrower fornece uma interface de alto nível para permitir a exi
bição de documentos Web aos usuários.
A biblioteca tkinter fornece interface gráfica padrão do python para kit de 
ferramentas gráficas Tk  
"""
import webbrowser
from tkinter import *

root = Tk()

root.title('Abrir Browser')
root.geometry('400x300')

def google():
    webbrowser.open('www.google.com')
mygoogle = Button(root, text='Abrir o Google', command=google).pack(pady=20)

root.mainloop()
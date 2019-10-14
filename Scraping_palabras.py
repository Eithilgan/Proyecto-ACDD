# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 21:51:44 2019

@author: Ezxiio
"""

from bs4 import BeautifulSoup
import requests

def llamar():
    busca_palabra()
def busca_palabra():
    palabra = input("Ingresa palabra: ")
    URL = "https://www.wordreference.com/sinonimos/"+palabra

    req = requests.get(URL)

    status_code = req.status_code
    if status_code == 200:

        html = BeautifulSoup(req.text, "html.parser")

        entradas = html.find_all('div', {'class': 'trans clickable'})
        texto = str(entradas)
        index     = texto.find("<li>")
        end       = texto.find("</li>")
        sinonimos = texto[index:end]
        if sinonimos == "":
            print("-------------------------------------------------------------")
            print("No tengo sinonimos para esa palabra")
            print("-------------------------------------------------------------")
            llamar()
        else:
            print("-------------------------------------------------------------")
            print(sinonimos[4:len(sinonimos)].replace("  ",""))
            print("-------------------------------------------------------------")
            llamar()

llamar()
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 02:48:25 2019

@author: Ezxiio
"""
from sklearn.feature_extraction.text import CountVectorizer
import os

def leer_documentos(root):
    diccionario = dict()
    labels = [] #tema
    docs = []   #
    for r, dirs, files in os.walk(root):
        for file in files:
            with open(os.path.join(r, file), "r",encoding="latin-1") as f:
                #r es el directorio, y file son los archivos txt dentro, lo que hace
                #esta linea es unir la ruta de forma inteligente
                docs.append(f.read()) #todo el contenido de cada txt
            label = r.replace(root, '') #guarda nombre de cada carpeta y quita el nombre del path principal
            labels.append(label.replace('\\',''))
    for x in range(len(labels)):
        diccionario.setdefault(labels[x], docs[x])
    return diccionario
    #devuelve diccionario con el texto y los nombres de cada carpeta 

contar = leer_documentos('Sesiones')
print (contar)

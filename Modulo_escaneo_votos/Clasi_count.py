# -*- coding: utf-8 -*-
from sklearn.feature_extraction.text import CountVectorizer
from insertaDato import *
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
keys = []
boletines = []
for key in leer_documentos('../Temas'):
    keys.append(key)
for key in leer_documentos('Boletines'):
    boletines.append(key)
data = leer_documentos('../Temas')
contar = leer_documentos('Boletines')

#____________________Palabras descartadas________________#
prepositions =['a','del','ante','bajo','cabe','cada','con','contra','de','desde','en','entre','hacia','hasta','para','por','según','sin','so','sobre','tras']
prep_alike = ['durante','mediante','excepto','salvo','incluso','más','menos']
adverbs = ['no','si','sí']
articles = ['el','la','los','las','un','una','unos','unas','este','esta','estos','estas','aquel','aquella','aquellos','aquellas','su','sus']
aux_verbs = ['he','has','ha','hemos','habéis','han','había','habías','habíamos','habíais','habían']

#(list.tema||||list.boletines||||,diccionario||||Discusiones||||TEMA recorrido for)
def obtener_score(llaves,documentos,data,boletines,palabras):
    vectorizer = CountVectorizer(stop_words=prepositions+prep_alike+adverbs+articles+aux_verbs)

    #____________________Conteo de palabras__________________#
    # lista de documentos de texto
    # crear la transformación
    # tokenizar y construir el vocabulario
    cadena = [data[palabras]]
    documentos = [documentos[boletines]]
    vectorizer.fit(cadena)
    # resumen
    vocabulario = vectorizer.get_feature_names()
    # codificador de documentos
    vector = vectorizer.transform(documentos)
    
    datos = vector.toarray()
    suma = 0
    for x in range(len(vocabulario)):
        suma = suma + datos[0][x]
    print (palabras," = ",suma)
    return boletines,palabras,suma

def obtener_top(boletin):
    tema=[]    #recibe cada tema, score, y boletin y los separa en los arreglos
    score=[]   #pero cada correspondiente en la misma posicion.
    boletines=[]
    total = 0
    for y in keys: #keys son los temas
        resultados = (obtener_score(keys,contar,data,boletin,y)) # resultado de obtener_score
        boletines.append(resultados[0]) #posicion 0 de resultados
        tema.append(resultados[1])     #posicion 1 de resultados
        score.append(resultados[2])   #posicion 2 de resultados
            
    #print(tema)
    #print(score)
    #print(max(score))
    #print(score.index(max(score)))
    temadef = (tema[score.index(max(score))]) #recojo la posicion del valor mas alto en score
    boletindef = (boletines[score.index(max(score))]) #busco la posicion del boletin al cual corresponde el valor mas alto
    print("la clasificacion para el boletin",boletindef,"es =",temadef)
    print("-----------------------------------------------------------------")
    for i in range(len(score)):
        total = total+score[i]
    totalpalabras=max(score),'de',total
    updatePrediccion(boletindef,temadef)
    updateScore(boletindef,str(totalpalabras))
    
def clasificar():
    for y in boletines: #realizar el proceso de clasificacion y almaccenado
        obtener_top(y) #por cada boletin existente en la carpeta
clasificar()      
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 11:37:58 2019

@author: Ezxiio
"""
import os
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import KNeighborsClassifier

preposiciones =['a','ante','bajo','cabe','con','contra','de','desde','en','entre','hacia','hasta','para','por','según','sin','so','sobre','tras']
prep_aux = ['durante','mediante','excepto','salvo','incluso','más','menos']
adverbios = ['no','si','sí']
personales = ['el','la','los','las','un','una','unos','unas','este','esta','estos','estas','aquel','aquella','aquellos','aquellas']
verbos_aux = ['he','has','ha','hemos','habéis','han','había','habías','habíamos','habíais','habían']
pronombres = ['yo', 'tú', 'él', 'nosotros', 'ustedes', 'ellos', 'que', 'quien', 'me', 'mi', 'su','niños','niñas','adolecentes','niño','niña','diputado','diputada','diputados','diputadas','intervencion','interviene']

#TfidfVectorizer crea una matriz de tipo frecuencia de término – frecuencia inversa de documento 
#(o sea, la frecuencia de ocurrencia del término en la colección de documentos)
#como en este caso le estamos indicando "stop_words", esto quiere decir que 
#las palabras pertenecientes a la matriz TF-IDF si bien se repetiran 
# una gran cantidad de veces, estas no seran de mucha importancia.
tfid = TfidfVectorizer(stop_words=preposiciones+prep_aux+adverbios+personales+verbos_aux+pronombres)


def leer_documentos(root):
    labels = [] #tema
    docs = []   #
    for r, dirs, files in os.walk(root):
        print(os.walk(root))
        for file in files:
            with open(os.path.join(r, file), "r",encoding="latin-1") as f:
                #r es el directorio, y file son los archivos txt dentro, lo que hace
                #esta linea es unir la ruta de forma inteligente
                docs.append(f.read()) #todo el contenido de cada txt
            labels.append(r.replace(root, '')) #guarda nombre de cada carpeta y quita el nombre del path principal
    return dict([('docs', docs), ('labels', labels)])
    #devuelve diccionario con el texto y los nombres de cada carpeta 
#____________________________________________________________#
#data se transforma en un diccionario con los temas y texto correspondiente para cada tema
data = leer_documentos('Palabras_claves')
#se separan el texto y los temas: Documents = texto Labels = temas
documentos = data['docs']
etiquetas = data['labels']
#____________________________________________________________#
X_train = tfid.fit_transform(documentos)
X_train2 = tfid.get_feature_names()
print (X_train2)
y_train = etiquetas
#____________________________________________________________#
#KNeighborsClassifier(n_neighbors=3) es un metodo de clasificacion que asigna
#una clase dependiendo de la cantidad de representantes mas cercanos que este posea
#en n_neighbors indicamos la cantidad de vecinos bases para realizar la aproximacion
clf = KNeighborsClassifier(n_neighbors=3)
clf.fit(X_train, y_train)


#____________________________________________________________#
test = leer_documentos('Documento')
X_test = tfid.transform(test['docs'])
y_test = test['labels']
pred = clf.predict(X_test)
for i in range(len(test['labels'])):
    print("Sesion N°"+str(i))
    print (test['labels'][i])
    print(pred[i])
    print("----------------------------")


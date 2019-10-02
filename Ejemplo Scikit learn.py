# -*- coding: utf-8 -*-
"""
@author: Ezxiio
"""
from sklearn.neighbors import KNeighborsClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
import os

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
        for file in files:
            with open(os.path.join(r, file), "r",encoding="latin-1") as f:
                #r es el directorio, y file son los archivos txt dentro, lo que hace
                #esta linea es unir la ruta de forma inteligente
                docs.append(f.read()) #todo el contenido de cada txt
            labels.append(r.replace(root, '')) #guarda nombre de cada carpeta y quita el nombre del path principal
    return dict([('docs', docs), ('labels', labels)])

data = leer_documentos("Aprendizaje")
documentos = data['docs']
print (documentos)
print (data['docs'])
etiquetas = data['labels']
#____________________________________________________________#
X_train = tfid.fit_transform(documentos)
print(X_train)
y_train = etiquetas

Aprendizaje = KNeighborsClassifier(n_neighbors=1)
Aprendizaje.fit(X_train,y_train)

test = leer_documentos("Predecir")
X_test = tfid.transform(test['docs'])
y_test = test['labels']
pred = Aprendizaje.predict(X_test)
print (pred)
print('accuracy score %0.3f' % Aprendizaje.score(X_train, y_train))
print('accuracy score %0.3f' % Aprendizaje.score(X_test, y_test))
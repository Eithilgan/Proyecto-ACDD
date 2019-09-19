# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 11:37:58 2019

@author: Ezxiio
"""
import os
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import KNeighborsClassifier

prepositions =['a','ante','bajo','cabe','con','contra','de','desde','en','entre','hacia','hasta','para','por','según','sin','so','sobre','tras']
prep_alike = ['durante','mediante','excepto','salvo','incluso','más','menos']
adverbs = ['no','si','sí']
articles = ['el','la','los','las','un','una','unos','unas','este','esta','estos','estas','aquel','aquella','aquellos','aquellas']
aux_verbs = ['he','has','ha','hemos','habéis','han','había','habías','habíamos','habíais','habían']
pronouns = ['yo', 'tú', 'él', 'nosotros', 'ustedes', 'ellos', 'que', 'quien', 'me', 'mi', 'su']

#TfidfVectorizer crea una matriz de tipo frecuencia de término – frecuencia inversa de documento 
#(o sea, la frecuencia de ocurrencia del término en la colección de documentos)
#como en este caso le estamos indicando "stop_words", esto quiere decir que 
#las palabras pertenecientes a la matriz TF-IDF si bien se repetiran 
# una gran cantidad de veces, estas no seran de mucha importancia.
tfid = TfidfVectorizer(stop_words=prepositions+prep_alike+adverbs+articles+aux_verbs+pronouns)


def read_all_documents(root):
    labels = []
    docs = []
    for r, dirs, files in os.walk(root):
        for file in files:
            with open(os.path.join(r, file), "r",encoding="latin-1") as f:
                docs.append(f.read())
            labels.append(r.replace(root, ''))
    return dict([('docs', docs), ('labels', labels)])

#____________________________________________________________#
#data se transforma en un diccionario con los temas y texto correspondiente para cada tema
data = read_all_documents('Palabras_claves')
#se separan el texto y los temas: Documents = texto Labels = temas
documents = data['docs']
labels = data['labels']
#____________________________________________________________#
X_train = tfid.fit_transform(documents)
print (X_train)
y_train = labels
#____________________________________________________________#
#KNeighborsClassifier(n_neighbors=3) es un metodo de clasificacion que asigna
#una clase dependiendo de la cantidad de representantes mas cercanos que este posea
#en n_neighbors indicamos la cantidad de vecinos bases para realizar la aproximacion
clf = KNeighborsClassifier(n_neighbors=3)
clf.fit(X_train, y_train)

#____________________________________________________________#
test = read_all_documents('Documento')
X_test = tfid.transform(test['docs'])
print ("X_test")
print (X_test)
y_test = test['labels']
pred = clf.predict(X_test)
for i in range(len(test['labels'])):
    print("Sesion N°"+str(i))
    print (test['labels'][i])
    print(pred[i])
    print("----------------------------")
    


print('accuracy score %0.3f' % clf.score(X_test, y_test))

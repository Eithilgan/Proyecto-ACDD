# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 11:37:58 2019

@author: Ezxiio
"""
import os
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer

prepositions =['a','ante','bajo','cabe','con','contra','de','desde','en','entre','hacia','hasta','para','por','según','sin','so','sobre','tras']
prep_alike = ['durante','mediante','excepto','salvo','incluso','más','menos']
adverbs = ['no','si','sí']
articles = ['el','la','los','las','un','una','unos','unas','este','esta','estos','estas','aquel','aquella','aquellos','aquellas']
aux_verbs = ['he','has','ha','hemos','habéis','han','había','habías','habíamos','habíais','habían']


tfid = TfidfVectorizer(stop_words=prepositions+prep_alike+adverbs+articles+aux_verbs)


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
data = read_all_documents('C:\\xampp\htdocs\\Proyecto ACDD\\Proyecto-ACDD\\Palabras_claves')
documents = data['docs']
labels = data['labels']
#____________________________________________________________#

from sklearn.feature_extraction.text import TfidfVectorizer
X_train = tfid.fit_transform(documents)
y_train = labels
#____________________________________________________________#
from sklearn.neighbors import KNeighborsClassifier

clf = KNeighborsClassifier(n_neighbors=3)
clf.fit(X_train, y_train)

#____________________________________________________________#
test = read_all_documents('C:\\xampp\\htdocs\\Proyecto ACDD\\Proyecto-ACDD\\Documento')
X_test = tfid.transform(test['docs'])
y_test = test['labels']
pred = clf.predict(X_test)
for i in range(len(test['labels'])):
    print("Sesion N°"+str(i))
    print (test['labels'][i])
    print(pred[i])
    print("----------------------------")
    


print('accuracy score %0.3f' % clf.score(X_test, y_test))

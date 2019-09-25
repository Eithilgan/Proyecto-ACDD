# -*- coding: utf-8 -*-
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer




#____________________Palabras descartadas________________#
prepositions =['a','del','ante','bajo','cabe','con','contra','de','desde','en','entre','hacia','hasta','para','por','según','sin','so','sobre','tras']
prep_alike = ['durante','mediante','excepto','salvo','incluso','más','menos']
adverbs = ['no','si','sí']
articles = ['el','la','los','las','un','una','unos','unas','este','esta','estos','estas','aquel','aquella','aquellos','aquellas']
aux_verbs = ['he','has','ha','hemos','habéis','han','había','habías','habíamos','habíais','habían']

tfid = TfidfVectorizer(stop_words=prepositions+prep_alike+adverbs+articles+aux_verbs)

#____________________Conteo de palabras__________________#
# lista de documentos de texto
text = ["Cada estudiante puede seleccionar libremente los ejercicios de su interés y escribir periódicamente durante las clases de Lenguaje.Los docentes recibirán recomendaciones escritas para retroalimentar las entradas de los cuadernillos y para implementar en sus aulas una comunidad de escritores.Esta primera etapa del Plan Nacional de Escritura consiste en la entrega de cuadernillos de escritura, a través de los cuales los estudiantes desarrollarán de forma libre la escritura desde diversos temas y formatos. Irán destinados por tramos de edad: 1° y 2° básico; 3° a 6° básico, 7° y 8° básico; 1° a 4° medio."]
# crear la transformación
vectorizer = CountVectorizer()
# tokenizar y construir el vocabulario
vectorizer.fit(text)
# resumen
print(vectorizer.vocabulary_)
# codificador de documentos
vector = vectorizer.transform(text)
# resumir vector codificado
print(vector.shape)
print(type(vector))
print(vector.toarray())



#___________________Estructura Json_____________________#
JsonData = '{"Legistalura":{"idLegislatura":,"numeroLegislatura":,"fecha_inicio":,"fecha_termino":,"tipo":,"sesion":{"idLegislatura":,"idSesion":,"numero":,"fecha_inicio":,"fecha_termino":,"tipo":,"Boletin":{"idDiputado":,"nombre":,"comentario":,"boletin":},"Asistencia":{"idSesion":,"nombre":,"partido":,"asistencia":,"asistencia":,"hora_ingreso":,"observacion":},Votaciones:{"boletin":,"resultado":,"a_favor":,"en_contra":,"abstencion":,"dispensados":}}}'
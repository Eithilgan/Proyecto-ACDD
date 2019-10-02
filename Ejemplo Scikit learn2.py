# -*- coding: utf-8 -*-
"""
@author: Ezxiio
"""

from sklearn.feature_extraction.text import CountVectorizer
# lista de documentos de texto
text = ["Profesor alumno aula aprender enseñar escuela colegio liceo universidad aprendizaje curso beca materia privada publica instruccion instituto examen prueba rector municipal matricula estudiante notas numeros cualitativo preparacion evaluacion apoderado establecimiento tarea prueba control presentacion evaluacion admision gratuidad basica media superior doctorado bachiller titulo tecnico profesional docente postular biblioteca libro escribir directores","establecimientos"]

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

text2 = ["El Presidente de la República, Sebastián Piñera, acompañado por la ministra de Educación, Marcela Cubillos, firmaron esta mañana el proyecto de ley “Aula Segura”, el cual busca fortalecer las facultades de los directores de establecimientos educacionales, permitiéndoles expulsar de manera inmediata a alumnos que se vean involucrados en hechos graves de violencia. Sobre esto, el Presidente Sebastián Piñera sostuvo que ”el mensaje es muy claro; les decimos a todos nuestros compatriotas, nuestro Gobierno está comprometido con la calidad de la educación de todos y cada uno de nuestros niños y jóvenes, con la dignidad e integridad que merece toda la comunidad escolar, pero va a perseguir con toda la fuerza de la ley a aquellos delincuentes y violentistas que, disfrazados de estudiantes, sin respetar a nada ni a nadie, pretenden causar un clima de terror al interior de nuestros establecimientos educacionales”. Por su parte, la ministra de Educación, Marcela Cubillos, señaló que, “esperamos contar con el apoyo de los parlamentarios para aprobar rápido esta ley que significa un fuerte apoyo a la educación pública. Debemos enfrentar con rigor la cobardía y la violencia que hemos visto en el actuar de estos jóvenes lanzando bombas Molotov al interior de los liceos o rociando con bencina a los docentes. Son ellos los que están poniendo en riesgo a sus compañeros y profesores, afectando el derecho a la educación de todo el resto de la comunidad educativa”."]
vector = vectorizer.transform(text2)
print(vector.toarray())

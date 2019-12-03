import pymongo
from pymongo import MongoClient # El cliente de MongoDB
from bson.objectid import ObjectId # Para crear ObjectId, porque _id como cadena no funciona

#Clase que define el objeto alumno, y sus caracteristicas y metodos
class Legislatura:
				def __init__(self,idlegislatura,numerolegislatura,fecha_inicio,fecha_termino,tipo):
					self.idlegislatura = idlegislatura
					self.numerolegislatura = numerolegislatura
					self.fecha_inicio = fecha_inicio
					self.fecha_termino = fecha_termino
					self.tipo = tipo

				def addColeccion(self):
					return {
						"idlegislatura":self.idlegislatura,
						"numerolegislatura":self.numerolegislatura,
						"fecha_inicio":self.fecha_inicio
						"fecha_termino":self.fecha_termino
						"tipo":self.tipo
					}

print("  ")

print("  ")

print("  ")

def InsertaEnDatabase(idlegislatura,numerolegislatura,fecha_inicio,fecha_termino,tipo):
    legislaturas = [
        Legislatura(idlegislatura,numerolegislatura,fecha_inicio,fecha_termino,tipo);
    ]
    cliente = MongoClient("localhost",27017)
    database = cliente["Camara"]
    coleccion = database["Legislatura"]

    for leg in legislaturas:
        coleccion.insert(Legislatura.addColeccion())


import pymongo
from pymongo import MongoClient # El cliente de MongoDB
from bson.objectid import ObjectId # Para crear ObjectId, porque _id como cadena no funciona

#Clase que define el objeto alumno, y sus caracteristicas y metodos
class Alumno:
				def __init__(self,nombre,apellido,edad):
					self.nombre = nombre
					self.apellido = apellido
					self.edad = edad

				def addColeccion(self):
					return {
						"nombre":self.nombre,
						"apellido":self.apellido,
						"edad":self.edad
					}



print("  ")

print("  ")

print("  ")
#Arreglo con varios objetos de tipo Alumno
alumnos = [
		Alumno("Perico","Perez",30),
		Alumno("Angélica","Gonzalez",28),
		Alumno("Roberto","Gómez",23),
		Alumno("Loreto","Moya",22),
]

#*******Conección a la base de datos***********
cliente = MongoClient("localhost",27017)
cliente.drop_database('Escuela')
db = cliente.Escuela #Nombre de la base de datos
curso = db.Escuela #Nombre de la coleccion

#**********************************************

#*Inserción de elementos en la colección curso*
for alumno in alumnos:
	curso.insert(alumno.addColeccion())
#**********************************************

#**Función que lee los datos de la colección**
reader = curso.find()
#**Recorre la lectura imprimiendo los datos**
for alu in reader:
	print(alu["nombre"],str(" - "),alu["apellido"],str(" - "),alu["edad"])

#Actualización de la edad, cuando el nombre sea perico, actualiza la edad a 18
curso.update({
	"nombre":"Perico"
	},{
	"$set":{
		"edad":18
		}
	})
print("\nImpresión luego de la 1a update\n")

#**Función que lee los datos de la colección**
reader = curso.find()
#**Recorre la lectura imprimiendo los datos**
for alu in reader:
	print(alu["nombre"],str(" - "),alu["apellido"],str(" - "),alu["edad"])


#Actualizacion cuando la edad sea mayor a 10, la incrementa en 5 unidades.
curso.update({
	"edad":{
		"$gt":10
		}
	},
	{"$inc":{
		"edad":5
		}
	}, multi = True)
print("\nImpresión luego de la 2a update\n")

#**Función que lee los datos de la colección**
reader = curso.find()
#**Recorre la lectura imprimiendo los datos**
for alu in reader:
	print(alu["nombre"],str(" - "),alu["apellido"],str(" - "),alu["edad"])


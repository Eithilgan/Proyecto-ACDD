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
			"fecha_inicio":self.fecha_inicio,
			"fecha_termino":self.fecha_termino,					
			"tipo":self.tipo
		}
class Sesion:
	def __init__(self,idlegislatura,idsesion,numero,fecha_inicio,fecha_termino,tipo):
		self.idlegislatura = idlegislatura
		self.idsesion = idsesion
		self.numero = numero
		self.fecha_inicio = fecha_inicio
		self.fecha_termino = fecha_termino
		self.tipo = tipo

	def addColeccion(self):
		return {
			"idlegislatura":self.idlegislatura,
			"idsesion":self.idsesion,
			"numero":self.numero,
			"fecha_inicio":self.fecha_inicio,	
			"fecha_termino":self.fecha_termino,					
			"tipo":self.tipo
		}
class Boletin:
	def __init__(self,idboletin,nombre,prediccion,contenido,score):
		self.idboletin = idboletin
		self.nombre = nombre
		self.prediccion = prediccion
		self.contenido = contenido
		self.score = score

	def addColeccion(self):
		return {
			"idboletin":self.idboletin,
			"nombre":self.nombre,
			"prediccion":self.prediccion,
			"contenido":self.contenido,
			"score":self.score
		}
class Votaciones:
	def __init__(self,idvotaciones,boletin,resultado,a_favor,en_contra,abstencion,dispensado):
		self.idvotaciones = idvotaciones
		self.boletin = boletin
		self.resultado = resultado
		self.a_favor = a_favor
		self.en_contra = en_contra
		self.abstencion = abstencion
		self.dispensado = dispensado

	def addColeccion(self):
		return {
			"idvotaciones":self.idvotaciones,
			"boletin":self.boletin,
			"resultado":self.resultado,
			"a_favor":self.a_favor,
			"en_contra":self.en_contra,
			"abstencion":self.abstencion,
			"dispensado":self.dispensado
		}
class Proyecto_ley:
	def __init__(self,idboletin,idproyecto_ley,nombre_proyecto,a_favor,en_contra,abstencion,dispensado):
		self.idboletin = idboletin
		self.boletin = boletin
		self.nombre_proyecto = nombre_proyecto


	def addColeccion(self):
		return {
			"idboletin":self.idboletin,
			"idproyecto_ley":self.idproyecto_ley,
			"nombre_proyecto":self.nombre_proyecto
		}




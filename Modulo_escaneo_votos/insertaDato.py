import pymongo
from pymongo import MongoClient # El cliente de MongoDB
from bson.objectid import ObjectId # Para crear ObjectId, porque _id como cadena no funciona
def insertarRegistro(NombreColeccion,dato):
    cliente = MongoClient("localhost", 27017)
    database = cliente["Camara"]
    coleccion = database[str(NombreColeccion)]
    x = coleccion.insert_one(dato.__dict__)

def DeleteDatabase():
    cliente = MongoClient("localhost", 27017)
    cliente.drop_database('Camara')


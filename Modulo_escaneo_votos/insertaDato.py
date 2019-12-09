import pymongo
from pymongo import MongoClient # El cliente de MongoDB
from bson.objectid import ObjectId # Para crear ObjectId, porque _id como cadena no funciona
def insertarRegistro(NombreColeccion,dato):
    DbName="Camara1"
    cliente = MongoClient("localhost", 27017)
    database = cliente[str(DbName)]
    coleccion = database[str(NombreColeccion)]
    x = coleccion.insert_one(dato.__dict__)

def DeleteDatabase():
    DbName="Camara1"
    cliente = MongoClient("localhost", 27017)
    cliente.drop_database(str(DbName))

def IsDuplicate(NombreColeccion,campo,dato):
    DbName="Camara1"
    cliente = MongoClient("localhost", 27017)
    db = cliente[str(DbName)]
    cursor = db[str(NombreColeccion)].find({str(campo):str(dato)})
    cont=0
    for document in cursor:
        cont=cont+1
    if(cont>1):
        flag=True
    else:
        flag=False
    return flag


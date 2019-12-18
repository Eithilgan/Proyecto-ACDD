import pymongo
from pymongo import MongoClient # El cliente de MongoDB
from bson.objectid import ObjectId # Para crear ObjectId, porque _id como cadena no funciona
global DbName
DbName = "Camara1"
def insertarRegistro(NombreColeccion,dato):
    #DbName="Camara1"
    cliente = MongoClient("localhost", 27017)
    database = cliente[str(DbName)]
    coleccion = database[str(NombreColeccion)]
    x = coleccion.insert_one(dato.__dict__)

def updatePrediccion(idboletin,prediccion):
    #DbName="Camara1"
    cliente = MongoClient("localhost", 27017)
    database = cliente[str(DbName)]
    columna = database[str("Boletin")]
    query = {"idboletin":str(idboletin)}
    value = {"$set":{"prediccion":str(prediccion)}}
    columna.update_many(query,value,upsert=False)

def updateScore(idboletin,score):
    #DbName="Camara1"
    cliente = MongoClient("localhost", 27017)
    database = cliente[str(DbName)]
    columna = database[str("Boletin")]
    query = {"idboletin":str(idboletin)}
    value = {"$set":{"score":str(score)}}
    columna.update_many(query,value,upsert=False)

def updateNombre(idboletin,nombreBoletin):
    #DbName="Camara1"
    cliente = MongoClient("localhost", 27017)
    database = cliente[str(DbName)]
    columna = database[str("Boletin")]
    query = {"idboletin":str(idboletin)}
    value = {"$set":{"nombre":str(nombreBoletin)}}
    columna.update_many(query,value,upsert=False)

def DeleteDatabase():
    #DbName="Camara1"
    cliente = MongoClient("localhost", 27017)
    cliente.drop_database(str(DbName))
    print("Database '",DbName,"' Eliminada\n")

def IsDuplicate(NombreColeccion,campo,dato):
    #DbName="Camara1"
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

#DeleteDatabase()
#updateScore("11256-12","  ")
#updatePrediccion("11256-12","El proyecto trata de salud")
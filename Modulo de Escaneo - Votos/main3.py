from includes import *
from sopa import *
from legislatura import *
from sesiones import *
from proyecto import *
from boletin import *
from votaciones import *
from detalle import *
from fromBoletinGetproyecto import *

LegID    = getLegislaturaActual()
a_sesion = getSesiones(LegID)

#Primero, Se crean arreglos vacios para las etiquetas XML de proyectos y para los ID de boletines de esos proyectos
#Despues, se pide ingresar un numero de sesion
#En caso de que este incorrecto preguntara de nuevo, hasta que se ingrese de manera correcta
#Luego, obtendra las etiquetas XML de los proyectos de ley asociados a la sesion y se los pasara a la funcion getBoletin
#Una vez que tenga el ID de boletin lo añadira al arreglo de Boletines (los cuales estan asociados a una sesion en particular)

#Despues, preguntará por un ID de boletin y validará que ese boletin exista o este bien ingresado
#Luego llamará a la funcion creaFile() del script fromBoletinGetproyecto.py
# Esta funcion es para obtener el XML del proyecto de ley a partir del id de boletin
# Lo que hace es crear el archivo que contiene la discusion parlamentaria de ese boletin
# Cabe destacar que si en una sesion cualquiera, se discute un proyecto de ley asociado a ese id de boletin
# y no hay votacion, entonces no tomará en cuenta esa sesion, porque nos interesan las sesiones donde haya votacion

#Luego, imprime los id de votaciones que hay en el boletin anteriormente ingresado
#Finalmente, obtiene el resultado de la votacion, preguntando el ID de votacion y validandolo
aProyecto=[]; aBoletin=[]
while(True):
    print("\n########################### SESIONES DE LA LEGISLATURA ACTUAL ###");print(a_sesion);print("#################################################################\n")

    sesion = input("\n-Obtener boletines a partir de ID de sesion: ")
    while(getProyecto(str(sesion))==None):
        sesion = input("# Error! No hay boletines para este ID o está mal ingresado\n Ingrese ID de sesion nuevamente: ")    
    aProyecto=getProyecto(str(sesion))

    for i in range(0,len(aProyecto),1):
        if(getBoletin(aProyecto[i])!=""):
            aBoletin.append(getBoletin(aProyecto[i]))
        
    print("****BOLETINES EN SESION ",sesion,":",aBoletin,"****")
    
    boletin=input("\n-Generar .TXT de la discusion parlamentaria a partir de ID de boletin: ")
    while(getVotaciones(str(boletin))==""):
        boletin=input("# Error! No hay datos para este boletin o está mal ingresado\n Ingrese ID de boletin nuevamente: ")    
    
    creaFile(boletin)
    
    print("\n****VOTACIONES EN BOLETIN ",boletin,":",getVotaciones(str(boletin)),"****")
    votacion=input("\n-Obtener resultado a partir de ID de votacion: ")
    while(getDetalle(str(votacion))==None):
        votacion=input("# Error, ingrese de ID de votacion nuevamente: ")

    
    print("\n****RESULTADO:",getDetalle(str(votacion)),"****")
    input("Ingrese ENTER para continuar")
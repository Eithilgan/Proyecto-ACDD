from includes import * ; from sopa import    * ; from legislatura import * ; from sesiones import *
from proyecto import * ; from boletin import * ; from votaciones import  *
from detalle  import * ; from archivo import * ; from dialogo import     *

LegID    = getLegislaturaActual()
aSesion  = getSesiones(LegID)

# Este es un script, que interactua con el usuario, pidiendo que ingrese datos y a través de funciones que están en otros scripts
# entrega una respuesta con la información correspondiente a los datos ingresados por el usuario.

#Primero, Se crean arreglos vacios para las etiquetas XML de proyectos y para los ID de boletines de esos proyectos 
#Despues, se pide ingresar un numero de sesion 
#En caso de que este incorrecto preguntara de nuevo, hasta que se ingrese de manera correcta 
#Luego, obtendra las etiquetas XML de los proyectos de ley asociados a la sesion. 
#Estos se guardarán en el arreglo aProyectos creado al comienzo. 
#Despues, recorrera el arreglo de aProyectos, y le pasará cada proyecto a la funcion getBoletin
# (siempre y cuando ese boletin no esté vacío)
#Una vez que tenga el ID de boletin lo añadira al arreglo de Boletines (los cuales estan asociados a una sesion en particular) 
#Después imprime los boletines que se obtuvieron, para que el usuario elija uno y así busque información respecto a ese boletin 

#Despues, preguntará por un ID de boletin y validará que ese boletin exista o este bien ingresado 
#Luego llamará a la funcion creaFile() del script fromBoletinGetproyecto.py  
# Esta funcion es para obtener el XML del proyecto de ley a partir del id de boletin 
# Lo que hace es crear el archivo que contiene la discusion parlamentaria de ese boletin
# Cabe destacar que si en una sesion cualquiera, se discute un proyecto de ley asociado a ese id de boletin
# y no hay votacion, entonces no tomará en cuenta esa sesion, porque nos interesan las sesiones donde haya votacion

#Luego, al arreglo aVotaciones le asigna la lista de id de votaciones que retorna de la función getVotaciones() que está en el script votaciones.py
#Posterior a ello, imprime los id de votaciones que hay en el boletin que le pasó como parámetro a getVotaciones()
#Finalmente, obtiene el resultado de la votacion, preguntando el ID de votacion del cual se desea saber el resultado
#Para esto llama a la función getDetalle() , la cual retorna APROBADO/RECHAZADO, pasándo como parámetro un ID de votación
#Posteriormente, imprime el resultado de la votación 
aProyecto=[]; aBoletin=[]; aVotaciones=[]
while(True):
    print("\n########################### SESIONES DE LA LEGISLATURA ACTUAL ###");print(aSesion);print("#################################################################\n")

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
        boletin = input("# Error! No hay datos para este boletin o está mal ingresado\n Ingrese ID de boletin nuevamente: ")    
    
    creaFile(boletin)
    aVotaciones = getVotaciones(str(boletin))

    print("\n****VOTACIONES EN BOLETIN ",boletin,":",aVotaciones,"****")

    votacion = input("\n-Obtener resultado a partir de ID de votacion: ")
    while(getDetalle(str(votacion))==None):
        votacion = input("# Error, No hay datos o el ingreso fue incorrecto\n Ingrese de ID de votacion nuevamente: ")

    resultado = getDetalle(str(votacion))
    print("\n****RESULTADO:",resultado,"****")
    input("Ingrese ENTER para continuar")
from includes import *
from sopa import *
from legislatura import *
from sesiones import *
from proyecto import *
from boletin import *
from votaciones import *
from detalle import *

LegID    = getLegislaturaActual()
a_sesion = getSesiones(LegID)

print("########################### SESIONES DE LA LEGISLATURA ACTUAL ###");print(a_sesion);print("#################################################################")

#--------------------------------Codigo principal------------------------------------------------------------------------------
#Primero crea un arreglo vacio para almacenar los proyectos de ley que existen para cada sesion
#Recorre cada una de las sesiones y extrae los proyectos de ley tratados en dicha sesion
#Entonces el arreglo aProyecto contiene arreglos con proyectos de ley
#Ejemplo: [  [p1,p2,p3], [p1,p1,p1],... ]
#Se valida con un if, que realmente ese proyecto exista y no sea un campo vacio

#Despues, se crea un arreglo vacio para guardar arreglos con los boletines, pues cada proyecto de ley esta asociado a un ID de boletin (los cuales pueden ser + de uno)
#Ejemplo: [  [Boletin1,Boletin2,Boletin3], [Boletin1,Boletin2,Boletin3],...]
#El primer ciclo for, recorre el arreglo grande, el que contiene arreglos mas pequeños con los boletines, el segundo ciclo for recorre los elementos de esos arreglos pequeños
#Se valida con un if, que realmente ese boletin exista y no sea un campo vacio

#Luego, se crea un arreglo vacio para almacenar los ID de las votaciones, ya que dentro de cada boletin, pueden existir varias instancias de votacion
#Ejemplo: [ [IdVotacion1,IdVotacion2,IdVotacion3], [IdVotacion1,IdVotacion2,IdVotacion3],... ]
#Se valida con un if, que realmente esa votacion exista y no sea un campo vacio

#Finalmente, se crea un arreglo llamado aDetalle, el cual guardara el resultado de la votacion (APROBADO o RECHAZADO)

aProyecto=[]                                   
for p in range(0,len(a_sesion),1):
    print(p,":Leyendo ",a_sesion[p])
    if(getProyecto(a_sesion[p]) is None):
        b=9
    else:
        aProyecto.append(getProyecto(a_sesion[p]))

aBoletin=[]
for lista in range(0,len(aProyecto),1):
    for proyecto in range(0,len(aProyecto[lista]),1):
        if(getBoletin(aProyecto[lista][proyecto])!=""):
            print("Leyendo del arreglo de proyectos",lista," , El proyecto:",proyecto)
            aBoletin.append(getBoletin(aProyecto[lista][proyecto]))
aVotacion=[]
for v in range(0,len(aBoletin),1):
    if(getVotaciones(aBoletin[v])!=None):
       print(v,":Leyendo ",aBoletin[v])
       aVotacion.append(getVotaciones(aBoletin[v]))
aDetalle=[]
for d in range(0,len(aVotacion),1):
    for d2 in range(0,len(aVotacion[d]),1):
        print("-Leyendo de la lista de votaciones ",d," El detalle de la votacion:",d2)
        aDetalle.append(getDetalle(aVotacion[d][d2]))

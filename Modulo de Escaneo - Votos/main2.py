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
#Una vez obtenidas las sesiones existentes en la legislatura actual
#Recorrera el arreglo que contiene cada una de estas sesiones
#Despues creará un arreglo para almacenar el contenido de las etiquetas <PROYECTO_LEY> 
# Si se da el caso de que en una determinada sesion no exista etiqueta <PROYECTO_LEY>, continua con la siguiente sesion del arreglo
# En caso de que si existan etiquetas <PROYECTO_LEY>
#  Primero crea un arreglo vacio y temporal llamado boletin, el cual guardará los boletines que se extraigan del proyecto de ley
#  Entonces, para cada etiqueta <PROYECTO_LEY> buscara cual es su ID de Boletin, para esto llama a la funcion getBoletin()
#   Si el ID de boletin NO ES VACIO, entonces lo añade al arreglo temporal creado anteriormente.
#   Despues, usando el ID de boletin, consultará cuales son las votaciones correspondientes a ese boletin y las guardara en un arreglo
#    Validará si esas votaciones existen (ya que hay boletines en los que la discusion queda pendiente y finalmente no hay votacion) 
#    En caso de que si hayan votaciones, recorrera el arreglo que contiene los ID de las votaciones correspondientes al boletin en cuestion 
#    Y llamara a la funcion getDetalle() para saber si el resultado de esa votacion fue APROBADO o RECHAZADO

for i in range(0,len(a_sesion),1):
    tagProyecto = getProyecto(a_sesion[i])
    if(tagProyecto is None):
        b=8
    else:
        aBoletin = [];                                                           print("\n###########################-SESION: ",a_sesion[i],"\n")
        for j in range(0,len(tagProyecto),1):
            idBoletin = getBoletin(tagProyecto[j])
            if(idBoletin!=""):
                aBoletin.append(idBoletin);                                      print("\n************************-Boletin:",aBoletin[j],"\n")
                idVotaciones=getVotaciones(aBoletin[j])
                if(idVotaciones!=None):
                    for g in range(0,len(idVotaciones),1):
                        print("-",idVotaciones[g],":",getDetalle(idVotaciones[g]))     

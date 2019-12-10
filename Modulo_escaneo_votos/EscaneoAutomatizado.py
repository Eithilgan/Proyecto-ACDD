from sopa       import * ; from legislatura import *
from sesiones   import * ; from proyecto    import *; from boletin             import *
from votaciones import * ; from detalle     import *; from archivo             import * 
from clases import *; from insertaDato import *

# Este es un script que no interactua con el usuario, extrae información por si solo.
# Es un poco más eficiente que el script main.py
####################################################################################

# Lo primero que hace es obtener la legislatura actual, a través de la página de opendata
# lo hace, con la función getLegislaturaActual(), esa función se encuentra en el script legislatura.py

# Después obtiene todas las sesiones que se han realizado dentro de esa legislatura.
# Esta función (getSesiones), recibe como parámetro un id de legislatura y se encuetra en el script sesiones.py

DataOfLeg    = getDataOfLegislaturaActual()

insertarRegistro("Legislatura",Legislatura(DataOfLeg[0],DataOfLeg[1],DataOfLeg[2],DataOfLeg[3],DataOfLeg[4]))

a_sesion = getSesiones(DataOfLeg[0])


print("########################### SESIONES DE LA LEGISLATURA ACTUAL ###");print(a_sesion);print("#################################################################")



#Una vez obtenidas las sesiones existentes en la legislatura actual
#Recorrera el arreglo que contiene cada una de estas sesiones (el arreglo llamado a_sesion creado anteriormente)
#Despues, creará un arreglo para almacenar el contenido de las etiquetas <PROYECTO_LEY>, ese arreglo se llamará tagProyecto
 
# Si se da el caso de que en una determinada sesion no exista etiqueta <PROYECTO_LEY>, continua con la siguiente sesion del arreglo
# En caso de que si existan etiquetas <PROYECTO_LEY> Lo que hace esto lo siguiente:
#   Primero crea un arreglo vacio y temporal llamado aBoletin, el cual guardará los boletines que se extraigan de cada proyecto de ley que se encuentra dentro del arreglo tagProyecto
#   Entonces, para cada etiqueta <PROYECTO_LEY> guardará en una variable llamada idBoletin cual es su ID de Boletin
#    para esto llama a la funcion getBoletin() la que se encuentra en el script boletin.py
#    En caso de que el idBoletin sea vacío continuará extrayendo el idBoletin de la siguiente etiqueta <PROYECTO_LEY>
#    Si el ID de boletin NO ES VACIO, entonces lo añade al arreglo tempporal aBoletin creado anteriormente.
#       Despues, usando el ID de boletin, consultará cuales son las votaciones correspondientes a ese boletin y las guardara en un arreglo (ese arreglo se llamará idVotaciones)
#       Validará si esas votaciones existen (ya que hay boletines en los que la discusion queda pendiente y finalmente no hay votacion) 
#          Si NO hay votaciones para ese id de Boletin, entonces continua con la siguiente etiqueta <PROYECTO_LEY>
#          En caso de que SI hayan votaciones, recorrerá el arreglo que contiene los ID de las votaciones correspondientes al boletín en cuestion 
#          Y llamara a la funcion getDetalle() para saber si el resultado de esa votacion fue APROBADO o RECHAZADO
#          Además llama a la función creaFile, la cual crea un archivo con la discusión parlamentaria del boletin que reciba como parámetro

#particular = a_sesion.index("3769")-1
for i in range(0,len(a_sesion),1):
    insertarRegistro("Sesion",Sesion(DataOfLeg[0],a_sesion[i],"None","None","None","None")) #BD
    tagProyecto = getProyecto(a_sesion[i])
    if(tagProyecto is None):
        flag = False
    else:
        aBoletin = []
        print("\n###########################-SESION: ",a_sesion[i],"\n")
        for j in range(0,len(tagProyecto),1):
            idBoletin = getBoletin(tagProyecto[j])
            if(idBoletin!="" and idBoletin!=None):
                
                aBoletin.append(idBoletin)
                print("\n************************-Boletin:",aBoletin[j],"\n")
                idVotaciones = getVotaciones(aBoletin[j])
                if(idVotaciones!=None):
                    contenido = creaFile(idBoletin)
                    insertarRegistro("Boletin",Boletin(str(idBoletin),"None",contenido))
                    for g in range(0,len(idVotaciones),1):
                        resultadoVotacion = getDetalle(idVotaciones[g])
                        print("- Resultado de la votación ",idVotaciones[g],":",resultadoVotacion)  
                        insertarRegistro("Votaciones",Votaciones(idVotaciones[g],str(idBoletin),resultadoVotacion,"None","None","None","None"))

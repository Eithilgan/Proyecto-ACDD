from includes import *
from sopa import *
from legislatura import *
from sesiones import *
from proyecto import *
from boletin import *
from votaciones import *
from detalle import *

# Este es un script que no interactua con el usuario, extrae información por si solo.
# Es el más ineficiente de los tres scirpts main.
####################################################################################

# Lo primero que hace es obtener la legislatura actual, a través de la página de opendata
# lo hace, con la función getLegislaturaActual(), esa función se encuentra en el script legislatura.py

# Después obtiene todas las sesiones que se han realizado dentro de esa legislatura.
# Esta función (getSesiones), recibe como parámetro un id de legislatura y se encuetra en el script sesiones.py

LegID    = getLegislaturaActual()
a_sesion = getSesiones(LegID)

print("########################### SESIONES DE LA LEGISLATURA ACTUAL ###");print(a_sesion);print("#################################################################")

# Una vez obtenidas las sesiones existentes en la legislatura actual
# Recorrera el arreglo que contiene cada una de estas sesiones (el arreglo llamado a_sesion creado anteriormente)

# Primero crea un arreglo vacio para almacenar los proyectos de ley que existen para cada sesion, ese arreglo se llamará aProyecto
# Después, recorrerá cada una de las sesiones.
# En caso de que en una sesión NO EXISTA etiqueta <PROYECTO_LEY> , continúa con la próxima sesión
# Y en caso de que sí exista etiqueta <PROYECTO_LEY> en esa sesión, agrega al arreglo aProyecto esa etiqueta <PROYECTO_LEY>
# Esto lo hace gracias a la función getProyecto, la cual está en el script proyecto.py
# Entonces el arreglo aProyecto contiene arreglos con proyectos de ley
# Ejemplo: [  [p1,p2,p3], [p1,p1,p1],... ]

# Despues, se crea un arreglo vacio para guardar arreglos con los boletines, pues cada proyecto de ley esta asociado a un ID de boletin
# (los cuales pueden ser + de uno). Este arreglo se llamará aBoletin.
# Después a través de dos ciclos for recorrerá los elementos del arreglo aProyecto
# recordar, que dicho arreglo contiene arreglos en su interior (Ver ejemplo anterior), por esto son dos ciclos for. 
# El primer ciclo for, recorre el arreglo grande, el que contiene arreglos mas pequeños con los boletines,
# El segundo ciclo for recorre los elementos de esos arreglos pequeños
# Se valida con un if, que realmente ese boletin exista y no sea un campo vacio. Si existe, entonces lo añade al arreglo aBoletin
# Ahora el arreglo aBoletin se ve así: [  [Boletin1,Boletin2,Boletin3], [Boletin1,Boletin2,Boletin3],...]

# Luego, se crea un arreglo vacio para almacenar los ID de las votaciones, ya que dentro de cada boletin
# pueden existir varias instancias de votacion. Este arreglo se llamará aVotacion y se verá así:
# Ejemplo: [ [IdVotacion1,IdVotacion2,IdVotacion3], [IdVotacion1,IdVotacion2,IdVotacion3],... ]
# Se valida con un if, que realmente esa votacion exista y no sea un campo vacio. esto lo hace mediante la función getVotaciones()
# La que se encuentra en el script votaciones.py

# Finalmente, se crea un arreglo vacío llamado aDetalle, el cual guardará el resultado de la votación (APROBADO o RECHAZADO)
# Esto lo hace recorriendo el arreglo aVotaciones, el cual contiene arreglos con id de votaciones.

aProyecto=[]                                   
for p in range(0,len(a_sesion),1):
    print(p,":Guardando en aProyecto etiquetas XML de los proyectos tratados en la sesion",a_sesion[p])
    if(getProyecto(a_sesion[p]) is None):
        flag=False
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
       print(v,":Extrayendo la(s) votacion(es) del boletin:",aBoletin[v])
       aVotacion.append(getVotaciones(aBoletin[v]))
aDetalle=[]
for d in range(0,len(aVotacion),1):
    for d2 in range(0,len(aVotacion[d]),1):
        print("-Leyendo de la lista de votaciones ",d," El detalle de la votacion:",d2)
        aDetalle.append(getDetalle(aVotacion[d][d2]))

from includes import *
from sopa import *
from legislatura import *
from sesiones import *
from proyecto import *
from boletin import *
from votaciones import *
from detalle import *
from bs4 import BeautifulSoup

#######################################################################################################################
#  ESTE SCRIPT CONTIENE TRES IMPORTANTES FUNCIONES QUE SE UTILIZAN PARA EXTRAER EL TEXTO DE UNA DISCUSIÓN PARLAMENTARIA
#######################################################################################################################

# Esta funcion retorna un arreglo con IDs de sesiones que están asociadas con un ID de boletin en partiuclar
# Recibe como parametro un id de boletin, por ejemplo "11571-21"
# ------------------------------------------ EXPLICACION ------------------------------------------
# Lo primero que hace es concatenar el id de boletin con la página de la cámara
# para porder acceder a dicha página. Ésta página contiene IDs de votaciones y de sesiones (Solo necesitamos las sesiones)
# Luego, convierte esa URL en un objeto BeautifulSoup.
# una vez convertida la URL buscará si existe la etiqueta 'Votacion' (ya que a veces no existe votacion)
# En caso de que si exista buscará todas las etiquetas de sesion y las guardará en un arreglo llamado aSesiones
#                     Ejemplo: aSesiones = ['<id>3731</id>','<id>3732</id>']
# Después, recorre ese arreglo de sesiones y guarda en una variable el atributo ID de dicha sesion, y también 
# lo convierte en un objeto de tipo string, ya que era objeto de tipo BeautifulSoup.
# le quita las etiquetas, y después lo guarda en el mismo arreglo. Entonces quedaría algo asi:
#                     Ejemplo: aSesiones = ['3731','3732']

def getSesionesById(idboletin):
    url="http://opendata.camara.cl/wscamaradiputados.asmx/getVotaciones_Boletin?prmBoletin="+idboletin
    bs_resultado = soup(url)
    if(bs_resultado.find("votacion")!=None):
        aSesiones   = bs_resultado.findAll("sesion") 
        for i in range(0,len(aSesiones),1):
            elemento      = str(aSesiones[i].id)
            elemento      = elemento.replace("<id>","")
            elemento      = elemento.replace("</id>","")
            aSesiones[i] = elemento
    return list(set(aSesiones))

# ------------------------------------------ EXPLICACION ------------------------------------------
# Esta funcion retorna una etiqueta con el dialogo que se da dentro de la etiqueta proyecto de ley
# Es decir, lo que hay justo después de la etiqueta <PROYECTO_LEY> y antes de la etiqueta <VOTACION>
# 
# En primer lugar, la funcion recibe como parametro la etiqueta de un proyecto de ley
# Por ejemplo:
#                 <proyecto_ley boletin="11571-21">AUTORIZACIÓN DE CAPTURA DE ESPECIES SALMONÍDEAS...
#                 <br/><br/>...<intervencion_diputado iddiputado="">...etc...
#                 </proyecto_ley>
#Lo primero que hace es transformar esa etiqueta a tipo String
#Después va a crear un arreglo, donde los elementos estaran separarados cuando exista un <br/>
# (Solo lo transforma a arreglo para poder elminiar los <br/>, luego lo volveremos a string)
#Por ejemplo:
#    tagProyecto = ["<proyecto_ley boletin...etc..","<intervencion_diputado...etc","Tiene la palabra el diputado..etc.."]
#Luego, lo transformamos nuevamente a string con la funcion join
#Despues va a cortar el string en la posicion donde esté "<votacion", ya que cuando comienza esta etiqueta
#termina la discusion parlamentaria e inician los resultados de la votacion
#
#Luego, Entra en un ciclo While que se encarga de eliminar lo que haya dentro de <     > 
#Finalmente retorna el string.
def getDialogo(tagProyecto):
    tagProyecto    = str(tagProyecto)
    tagProyecto    = tagProyecto.split("<br/>")
    tagProyecto    = "".join(tagProyecto)
    tagProyecto    = tagProyecto[:tagProyecto.index("<votacion")]
    flag = True
    while(flag==True):
        try:
            flag = True
            inicio = tagProyecto.index("<")
            final  = tagProyecto.index(">")
            tagProyecto = tagProyecto[:inicio]+tagProyecto[final:][1:]
        except:
            flag = False
    return tagProyecto
    

# ------------------------------------------ EXPLICACION ------------------------------------------
# Esta función no retorna cosa alguna. Se encarga de crear un archivo con la discusion parlamentaria asociada a un id de Boletin
# Esta función recibe como parámetro el id de un boletin por ejemplo: "11571-21"
# En primer lugar, llama a la función getSesionesById, la cual retorna un arreglo con todas las sesiones (Esta función está al comienzo de este script)
# en las que se discute sobre el proyecto de ley al cual esta asociado ese id de boletin
# Por ejemplo: ['3731','3763']

# Despues, va a recorrer ese arreglo y va a llamar a la funcion getProyecto() que está en el script proyecto.py la cual
# retorna un arreglo, donde sus elementos son etiquetas XML con cada proyecto de ley tratado en una determinada sesion
# Por ejemplo: ['<proyecto_ley boletin=11571-21...','<proyecto_ley boletin=11324-65...']

# Luego, recorrera ese arreglo de etiquetas XML.    
# Guardará en una variable el proyecto que esté recorriendo y lo transformará en un string.
# y preguntará si el id de boletin se encuentra en ese string

# Por ejemplo: if('3731' está en '<proyecto_ley boletin=11571-21...')
# En caso de que no esté, no pasará nada. En caso de que sí esté,  llamará a la funcion getDialogo()
# la cual retornará un string con la discusion del proyecto que se le pase como parámentro.
# (Esta función está justo arriba, en este mismo script).
# Después creará un archivo de texto con el string de la discusion parlamentaria
# Ese archivo txt tendrá el nombre del id de boletin y el id de la sesion.

def creaFile(idboletin):
    aSesion = getSesionesById(idboletin)
    #print("\nEn el boletin ",idboletin," Existen las sesiones:",aSesion)
    for i in range(0,len(aSesion),1):
        #print("\n******* Analizando la sesion:",aSesion[i]," *******\n")
        aProyectos = getProyecto(aSesion[i])
        for j in range(0,len(aProyectos),1):
            string=str(aProyectos[j])
            if(idboletin in string):
                cadena = getDialogo(aProyectos[j])
                namefile = "boletin "+idboletin+" discutido en la sesion "+aSesion[i]
                nfh = open(namefile+".txt","w")
                nfh.write(cadena)
                print("- El archivo ",namefile+".txt"," fue creado exitosamente")
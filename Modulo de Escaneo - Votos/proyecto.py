from includes import *
from sopa import *
#Funcion que obtiene los proyectos de ley de una sesion - Recibe como parametro el ID de la sesion
#------------------------------EXPLICACION-----------------------------------------
#Primero, concatena la URL de la pagina opendata con el ID de la sesion, y esta URL resultante la convierte en un objeto BeautifulSoup
#En caso de que no existan etiquetas de proyecto de ley, no retorna nada.
#En caso de que si existan etiquetas de proyecto de ley, las almacena en un arreglo de etiquetas
#Cabe destacar que este arreglo contiene las etiquetas proyecto de ley y con ellas todo su contenido (intervenciones, votaciones, etc)
#Finalmente, retorna ese arreglo
#----------------------------------------------------------------------------------
def getProyecto(IDSesion):
    bs_boletin       = soup("http://opendata.camara.cl/wscamaradiputados.asmx/getSesionBoletinXML?prmSesionID="+IDSesion)
    if not bs_boletin.select("PROYECTO_LEY"):
        #print("-Sesion ",IDSesion, "es OBJETO_SESION\n-La votacion no tiene ID\n")
        k=8
    else:
        tagsProyecto = bs_boletin.select("PROYECTO_LEY")
        #print(tagsProyecto)
        return(tagsProyecto)

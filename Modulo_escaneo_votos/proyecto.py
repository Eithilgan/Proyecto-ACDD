from includes import *
from sopa     import *

# Funcion que retorna el contenido existente en las etiquetas <PROYECTO_LEY> de una sesion
# Esta función recibe como parametro el ID de la sesion.

#------------------------------EXPLICACION-----------------------------------------
# Primero, concatena la URL de la pagina opendata con el ID de la sesion, y esta URL resultante la convierte en un objeto BeautifulSoup
# En caso de que no existan etiquetas de proyecto de ley, no retorna nada.
# En caso de que si existan etiquetas de proyecto de ley, las almacena en un arreglo de etiquetas llamado tagsProyecto
# Cabe destacar que este arreglo contiene las etiquetas proyecto de ley y con ellas todo su contenido (intervenciones, votaciones, etc)
# Finalmente, retorna ese arreglo
#----------------------------------------------------------------------------------
def getProyecto(IDSesion):
    bs_boletin       = soup("http://opendata.camara.cl/wscamaradiputados.asmx/getSesionBoletinXML?prmSesionID="+IDSesion)
    etiquetaProyecto = bs_boletin.select("PROYECTO_LEY")
    if not etiquetaProyecto:
        #print("-Sesion ",IDSesion, "es OBJETO_SESION\n-La votacion no tiene ID\n")
        return None
    else:
        tagsProyecto = etiquetaProyecto
        #print(tagsProyecto)
        return(tagsProyecto)

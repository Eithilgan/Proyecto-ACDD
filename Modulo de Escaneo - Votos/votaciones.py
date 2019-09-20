from includes import *
from sopa import *

# Esta funcion retorna los ID de cada una de las votaciones que se hicieron en un boletin - Recibe como parametro el ID un boletin
# ------------------------------ EXPLICACION -----------------------------------------
# Primero, concatena el ID de boletin con la URL de la pagina de opendata.
# Después, transforma esa URL en un objeto BeautifulSoup con la función soup, la cual está en el script sopa.py
# Luego, crea una variable vacía llamada idVotacion, la cual almacenará el ID de una votación
#  Si NO HAY votacion, entonces retorna la variable vacía
#  En caso de que SÍ HAYA votacion, entonces elimina todas las etiquetas de sesion
#  (Hace esto, porque las etiquetas de sesion también tienen ID, y solo queremos buscar los ID de la etiqueta votación)
#    Una vez eliminadas las etiquetas de sesion, guarda en idVotacion, la ID de las votaciones pertenecientes al boletin en cuestion
#    Posteriormente, para cada una de esas ID de votaciones va a eliminar la etiqueta, dejando solo el contenido, ya que viene de esta forma: "[<id>valor</id>]"
#    Finalmente retorna las ID de votaciones.
#------------------------------------------------------------------------------------
def getVotaciones(IdBoletin):
    pagina       = "http://opendata.camara.cl/wscamaradiputados.asmx/getVotaciones_Boletin?prmBoletin="+IdBoletin
    bs_resultado = soup(pagina)
    idVotacion   = ""

    if(bs_resultado.find("votacion")!=None):
        sesion   = bs_resultado.votacion.findAll("sesion") 

        while(bs_resultado.sesion!=None):
            bs_resultado.sesion.decompose()
        idVotacion = bs_resultado.find_all("id")

        for i in range(0,len(idVotacion),1):
            elemento      = str(idVotacion[i])
            elemento      = elemento.replace("<id>","")
            elemento      = elemento.replace("</id>","")
            idVotacion[i] = elemento
    
    return idVotacion

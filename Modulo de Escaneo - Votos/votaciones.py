from includes import *
from sopa import *
#Funcion que obtiene los ID de cada una de las votaciones que se hicieron en un boletin -  Recibe como parametro el ID del boletin
#------------------------------EXPLICACION-----------------------------------------
#Primero, concatena el ID de boletin con la URL de la pagina de opendata.
#Despues, transforma esa URL en un objeto BeautifulSoup
#Luego, crea una variable vacia, la cual almacenará el ID de una votacion
# Si no hay votacion, entonces retorna la variable vacia
# Si hay votacion, entonces elimina todas las etiquetas de sesion (Hace esto, porque las etiquetas de sesion también tienen ID, y solo queremos buscar los ID de la etiqueta votacion)
# Una vez eliminadas las etiquetas de sesion, guarda en idVotacion, la ID de las votaciones pertenecientes al boletin en cuestion
#  Posteriormente, para cada una de esas ID de votaciones va a eliminar la etiqueta, dejando solo el contenido, ya que viene de esta forma: "[<id>valor</id>]"
#  Finalmente retorna las ID de votaciones.
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

from includes import *
from sopa import *
#Funcion que obtiene el resultado de una votacion - Recibe como parametro el ID de la votacion
#Primero, concatena el ID de la votacion recibida con la URL de la pagina de opendata
#Despues, transforma esa URL en un objeto BeautifulSoup
#Luego, busca la etiqueta resultado, la cual obtiene el estado del proyecto, es decir, si fue APROBADO o RECHAZADO
def getDetalle(idVotacion):
    pagina     = "http://opendata.congreso.cl/wscamaradiputados.asmx/getVotacion_Detalle?prmVotacionID="+idVotacion
    bs_detalle = soup(pagina)
    resultado  = bs_detalle.find("resultado")
    if(resultado!=None):
        return resultado.text

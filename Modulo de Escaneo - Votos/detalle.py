from includes import *
from sopa import *

# Esta función retorna el resultado (APROBADO o RECHAZADO) de una votación - Recibe como parámetro un id de votación
# ---------------------------------------------- EXPLICACIÓN ----------------------------------------------
# Primero, concatena el ID de la votacion recibida con la URL de la pagina de opendata
# Despues, transforma esa URL en un objeto BeautifulSoup con la función soup, la cual está en el script sopa.py
# Luego, busca la etiqueta resultado, la cual obtiene el estado del proyecto, es decir, si fue APROBADO o RECHAZADO
# En caso de que no haya etiqueta votación, no retorna nada. (Recordar que solo nos sirven las votaciones que tienen ID)

def getDetalle(idVotacion):
    pagina     = "http://opendata.congreso.cl/wscamaradiputados.asmx/getVotacion_Detalle?prmVotacionID="+idVotacion
    bs_detalle = soup(pagina)
    resultado  = bs_detalle.find("resultado")
    if(resultado!=None):
        return resultado.text

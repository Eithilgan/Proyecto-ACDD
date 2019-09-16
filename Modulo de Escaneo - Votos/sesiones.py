from includes import *
from sopa import *
def getSesiones(IDLegis):
    #-Obtener datos de sesion
    url_sesion = "http://opendata.camara.cl/wscamaradiputados.asmx/getSesiones?prmLegislaturaID="+IDLegis
    bs_sesion  = soup(url_sesion)
    aSesion   = [Texto.text.strip() for Texto in bs_sesion.select('id')]
    return aSesion

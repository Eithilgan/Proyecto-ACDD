from includes import *
from sopa import *
def getLegislaturaActual():
    #-Obtener datos de legislatura
    url_legislatura = "http://opendata.camara.cl/wscamaradiputados.asmx/getLegislaturaActual"
    bs_legislatura  = soup("http://opendata.camara.cl/wscamaradiputados.asmx/getLegislaturaActual")
    label_id        = bs_legislatura.find_all("id")                                ## Busca todas las etiquetas "ID" y retorna una lista con ellas
    IDLegis         = [Texto.text.strip() for Texto in bs_legislatura.select('id')][0]       
    NumeroLegis     = [Texto.text.strip() for Texto in bs_legislatura.select('numero')][0]
    return IDLegis

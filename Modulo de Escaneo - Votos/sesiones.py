from includes import *
from sopa import *
# ----------------------------- EXPLICACIÓN ------------------------------------
# Esta función retorna las sesiones que se han tratado dentro de una legislatura
# Recibe como parámetro el ID de una legislatura. 
# Primero, concatena la URL de la página opendata que obtiene las sesiones con el ID de legislatura
# Después, a través de la función soup, la cual está en el script sopa.py transformará la URL anterior
# En un objeto BeautifulSoup.

# Luego, para cada elemento llamado "Texto" que esté dentro de una lista de IDs de sesiones  
# extraerá su atributo texto. El cual contiene el valor de la etiqueta ID. ( Esto lo hace la función .text.strip() )
# Por ejemplo:  Texto = <ID>34</ID>  Texto.text.strip() --> 34

def getSesiones(IDLegis):
    url_sesion = "http://opendata.camara.cl/wscamaradiputados.asmx/getSesiones?prmLegislaturaID="+IDLegis
    bs_sesion  = soup(url_sesion)
    aSesion   = [Texto.text.strip() for Texto in bs_sesion.select('id')]
    return aSesion

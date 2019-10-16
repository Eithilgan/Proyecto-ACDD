from includes import *
from sopa     import *

# Esta función retorna el ID de la legislatura que está vigente en la actualidad - No recibe parámetro
# ------------------------------------------- EXPLICACIÓN ---------------------------------------------
# Primero crea una variable que tiene una URL, cual contiene un XML con la legislatura actual de la cámara
# Después, con la función soup (que está en el script sopa.py) convierte la URL en un objeto BeautifulSoup
# Luego, busca las etiquetas llamadas "ID", solo habrá una, porque no puede haber más de una legislatura vigente
# Entonces, en una variable llamada IDLegis guardará el ID de la legislatura y en otra variable el Numero de la legislatura

# Después, para cada elemento llamado "Texto" que esté dentro de una lista de ID de Legislatura (Solo habrá un elemento porque no puede haber más de una legislatura actual)
# extraerá su atributo texto. El cual contiene el valor de la etiqueta ID. ( Esto lo hace la función .text.strip() )
# Por ejemplo:  Texto = <ID>34</ID>  Texto.text.strip() --> 34

# Posteriormente, repite este proceso con el Numero de legislatura

# Finalmente, retorna el ID de legislatura que es el que se va a utilizar.

def getLegislaturaActual():
    #-Obtener datos de legislatura
    url_legislatura = "http://opendata.camara.cl/wscamaradiputados.asmx/getLegislaturaActual"
    bs_legislatura  = soup("http://opendata.camara.cl/wscamaradiputados.asmx/getLegislaturaActual")
    label_id        = bs_legislatura.find_all("id")                                ## Busca todas las etiquetas "ID" y retorna una lista con ellas
    IDLegis         = [Texto.text.strip() for Texto in bs_legislatura.select('id')][0]       
    NumeroLegis     = [Texto.text.strip() for Texto in bs_legislatura.select('numero')][0]
    return IDLegis

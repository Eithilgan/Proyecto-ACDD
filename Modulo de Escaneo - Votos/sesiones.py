from includes import *
from sopa     import *
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
    aSesion    = [Texto.text.strip() for Texto in bs_sesion.select('id')]
    return aSesion

#######################################################################################################################
#  ESTE SCRIPT CONTIENE TRES IMPORTANTES FUNCIONES QUE SE UTILIZAN PARA EXTRAER EL TEXTO DE UNA DISCUSIÓN PARLAMENTARIA
#######################################################################################################################

# Esta funcion retorna un arreglo con IDs de sesiones que están asociadas con un ID de boletin en partiuclar
# Recibe como parametro un id de boletin, por ejemplo "11571-21"
# ------------------------------------------ EXPLICACION ------------------------------------------
# Lo primero que hace es concatenar el id de boletin con la página de la cámara
# para porder acceder a dicha página. Ésta página contiene IDs de votaciones y de sesiones (Solo necesitamos las sesiones)
# Luego, convierte esa URL en un objeto BeautifulSoup.
# una vez convertida la URL buscará si existe la etiqueta 'Votacion' (ya que a veces no existe votacion)
# En caso de que si exista buscará todas las etiquetas de sesion y las guardará en un arreglo llamado aSesiones
#                     Ejemplo: aSesiones = ['<id>3731</id>','<id>3732</id>']
# Después, recorre ese arreglo de sesiones y guarda en una variable el atributo ID de dicha sesion, y también 
# lo convierte en un objeto de tipo string, ya que era objeto de tipo BeautifulSoup.
# le quita las etiquetas, y después lo guarda en el mismo arreglo. Entonces quedaría algo asi:
#                     Ejemplo: aSesiones = ['3731','3732']

def getSesionesById(idboletin):
    aSesiones = []
    url = "http://opendata.camara.cl/wscamaradiputados.asmx/getVotaciones_Boletin?prmBoletin="+idboletin
    bs_resultado = soup(url)
    if(bs_resultado.find("votacion")!=None):
        aSesiones   = bs_resultado.findAll("sesion") 
        for i in range(0,len(aSesiones),1):
            elemento      = str(aSesiones[i].id)
            elemento      = elemento.replace("<id>","")
            elemento      = elemento.replace("</id>","")
            aSesiones[i] = elemento
    print(aSesiones)
    return list(set(aSesiones))
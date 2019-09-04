#Librerías para hacer scraping
from bs4 import BeautifulSoup
import urllib; import urllib.request;import urllib.parse
import lxml; import requests

#**************************************************************************************************************************************************
#**************************************************************************************************************************************************
#**************************************************************************************************************************************************

#Funcion que obtiene el id del boletin
def getBoletin(proyecto):
    proyecto  = str(proyecto)
    index     = proyecto.find("<")
    end       = proyecto.find(">")
    idBoletin = proyecto[index:end]
    idBoletin = idBoletin.split(chr(34))
    idBoletin = idBoletin[1]
    return idBoletin

#Funcion que convierte una URL en un objeto BeautifulSoup
def soup(url):
    obj = urllib.request.urlopen(url)          ## Retorna a una variable un objeto http.response 
    xml = obj.read()                           ## Lee el contenido de ese objeto y lo almacena en una variable
    objSoup = BeautifulSoup(xml,"lxml")        ## Convierte el XML en un objeto BeautifulSoup
    return objSoup

#Funcion que manipula el string, separa las etiquetas <br>
def manipula_string(aVotacion):
    aResultado=str(aVotacion[0]).split("<br/>")
    aResultado=[elemento for elemento in aResultado if len(elemento)>0]
    aResultado=aResultado[:-1]
    aResultado=aResultado[1:]
    return aResultado

#Funcion que recopila las votaciones por categorias y diputados
def recopilar_votaciones(IDSesion,bandera):
    bs_boletin   = soup("http://opendata.camara.cl/wscamaradiputados.asmx/getSesionBoletinXML?prmSesionID="+IDSesion)
    tagsProyecto = bs_boletin.select("PROYECTO_LEY")

    favor      = tagsProyecto[1].select('A_FAVOR')
    contra     = tagsProyecto[1].select('EN_CONTRA')
    abstencion = tagsProyecto[1].select('ABSTENCION')
    dispensado = tagsProyecto[1].select('DISPENSADO')
    aEstados   = [favor,contra,abstencion,dispensado]

    idBol1                             = getBoletin(tagsProyecto[1])
    astring                            = ["A FAVOR","EN CONTRA", "ABSTENCION", "DISPENSADO"]
    
    print("***** RESULTADOS DE LA SESION: ",IDSesion," ****  BOLETIN: ",print(idBol1)," *******");print("\n\n")

    #Recorre el arreglo aEstados, el cual contiene arreglos de los diputados que votaron en cada categoria
    for j in range(0,len(aEstados),1):
        print("######## ",astring[j]," ########")
        aVotaciones = []
        aVotaciones = aEstados[j]
        if not aVotaciones:
            print("Votación vacia")
        else:
            aFavor = manipula_string(aVotaciones)
            aEstados[j] = aFavor
        print(aEstados[j])
            
 
        

#**************************************************************************************************************************************************
#**************************************************************************************************************************************************
#**************************************************************************************************************************************************
#**************************************************************************************************************************************************




#Pagina a escanear - esta página contiene los datos de la legislatura actual
url_legislatura = "http://opendata.camara.cl/wscamaradiputados.asmx/getLegislaturaActual"

#********************   Escaneo de la pagina legislaturas  *****************************************************************
obj_legislatura = urllib.request.urlopen(url_legislatura)                      ## Retorna a una variable un objeto http.response 
xml_legislatura = obj_legislatura.read()                                       ## Lee el contenido de ese objeto y lo almacena en una variable
bs_legislatura = BeautifulSoup(xml_legislatura,"lxml")                         ## Convierte el XML en un objeto BeautifulSoup
label_id = bs_legislatura.find_all("id")                                       ## Busca todas las etiquetas "ID" y retorna una lista con ellas
print("\n\n")

#Recorre a través de "Texto" el contenido del xml, seleccionando solo el primer elemento de la busqueda de contenido de las etiquetas "id"
#Recorre a través de "Texto" el contenido del xml, seleccionando solo el primer elemento de la busqueda de contenido de las etiquetas "numero"
LegislaturaID     = [Texto.text.strip() for Texto in bs_legislatura.select('id')][0]       
LegislaturaNumero = [Texto.text.strip() for Texto in bs_legislatura.select('numero')][0]


#********************   Escaneo de la pagina sesiones      *****************************************************************
url_sesion = "http://opendata.camara.cl/wscamaradiputados.asmx/getSesiones?prmLegislaturaID="+LegislaturaID
obj_sesion = urllib.request.urlopen(url_sesion)     ## Retorna a una variable un objeto http.response 
xml_sesion = obj_sesion.read()              ## Lee el contenido de ese objeto y lo almacena en una variable
bs_sesion = BeautifulSoup(xml_sesion,"lxml")    ## Convierte el XML en un objeto BeautifulSoup
a_sesion = [Texto.text.strip() for Texto in bs_sesion.select('id')]

print("*************** SESIONES CORRESPONDIENTES A LA LEGISLATURA ",LegislaturaID," ****************\n\n")
print("\n\n")
#************************************************************************************

#LegislaturaID
#LegislaturaNumero
#a_sesion

for i in range(0,len(a_sesion),1):
    recopilar_votaciones(a_sesion[i],0)
    break

#*************************************************************************************


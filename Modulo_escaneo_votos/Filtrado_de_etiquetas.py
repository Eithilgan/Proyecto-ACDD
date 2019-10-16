#importado de librerias pora hacer scraping
import requests
from bs4 import BeautifulSoup


#scraping de boletin, guardando el contenido en variable "contenido"
fuente = requests.get("http://opendata.congreso.cl/wscamaradiputados.asmx/getSesionBoletinXML?prmSesionID=3747")
contenido = fuente.content
#print (contenido)

#creamos objeto "Soup"
soup = BeautifulSoup(contenido, "lxml")

#encontramos TODAS las etiquetas y las guardamos en arreglos "alltags"
#alltags contiene el nombre de las etiquetas y alltagscontent su contenido
allTagsID = [tag.name for tag in soup.find_all()]
allTagsContent = [tag.text for tag in soup.find_all()]

#imprimir todas las etiquetas excepto "br", la cual se usa solo para hacer salto de linea
def lista_etiquetas():
    etiquetas = []
    for i in range(len(allTagsID)):
        if allTagsID[i]!="br":   
            print (allTagsID[i])
            etiquetas.append(allTagsID[i])

#funcion para encontrar una etiqueta en específico
def buscar_etiqueta(etiqueta):
    for i in range(len(allTagsContent)):
        if allTagsID[i]==etiqueta:  
            return (allTagsContent[i])
        

#imprime TODO el contenido de TODAS LAS INSTANCIAS de una etiqueta
#enumeradas y ordenadas
def buscar_contenido_etiquetas(etiqueta):
    cont = 1
    for i in range(len(allTagsContent)):
        if allTagsID[i]==etiqueta:  
            print (etiqueta + " NUMERO: " + str(cont) + "\n" + (allTagsContent[i]))
            cont = cont+1

#-----------------------------------------------------------------------------------------
from proyecto import *
from dialogo import *
from GeneraDialogo import *
import json

def datos_boletin():
    nombre = buscar_etiqueta('titulo')
    proyecto = getProyecto('3747')
    boletin = getBoletin(proyecto)
    texto = generaDialogo(str(boletin))
    return boletin,nombre,texto

def ToJson():
   info_boletin = datos_boletin()
   boletin = {
                  "boletin": str(info_boletin[0]),
                  "nombre" : str(info_boletin[1]),
                  "texto"  : str(info_boletin[2])
                  
             }
   Json = json.dumps(boletin)
   print (Json)
print("------------------------------SEPARADO--------------------------------")
ToJson()





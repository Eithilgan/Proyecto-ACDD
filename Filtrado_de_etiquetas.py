#importado de librerias pora hacer scraping
import requests
from bs4 import BeautifulSoup


#scraping de boletin, guardando el contenido en variable "contenido"
fuente = requests.get("http://opendata.congreso.cl/wscamaradiputados.asmx/getSesionBoletinXML?prmSesionID=32")
contenido = fuente.content
#print (contenido)

#creamos objeto "Soup"
soup = BeautifulSoup(contenido, "lxml")

#encontramos TODAS las etiquetas y las guardamos en arreglos "alltags"
#alltags contiene el nombre de las etiquetas y alltagscontent su contenido
alltags = [tag.name for tag in soup.find_all()]
alltagscontent = [tag.text for tag in soup.find_all()]

#imprimir todas las etiquetas excepto "br", la cual se usa solo para hacer salto de linea
def lista_etiquetas():
    for i in range(len(alltags)):
        if alltags[i]!="br":   
            print (alltags[i])

#funcion para encontrar una etiqueta en específico
def buscar_etiqueta(etiqueta):
    for i in range(len(alltagscontent)):
        if alltags[i]==etiqueta:  
            return (alltagscontent[i])
            break

#imprime TODO el contenido de TODAS LAS INSTANCIAS de una etiqueta
#enumeradas y ordenadas
def buscar_contenido_etiquetas(etiqueta):
    cont = 1
    for i in range(len(alltagscontent)):
        if alltags[i]==etiqueta:  
            print (etiqueta + " NUMERO: " + str(cont) + "\n" + (alltagscontent[i]))
            cont = cont+1






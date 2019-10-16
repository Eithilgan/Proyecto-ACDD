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
eti_pref = ['titulo','asistencia','intervencion_diputado']
lista_etiquetas()
for x in eti_pref:
    print(buscar_etiqueta(x))
    






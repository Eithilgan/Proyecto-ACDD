#importado de librerias pora hacer scraping
import requests
from bs4 import BeautifulSoup


#scraping de boletin, guardando el contenido en variable "contenido"
fuente = requests.get("http://opendata.congreso.cl/wscamaradiputados.asmx/getSesionBoletinXML?prmSesionID=3747")
legislatura_actual = requests.get("http://opendata.congreso.cl/wscamaradiputados.asmx/getLegislaturaActual")
contenido = fuente.content
contenido_leg_actual = legislatura_actual.content
#print(contenido_leg_actual)

#creamos objeto "Soup"
soup = BeautifulSoup(contenido, "lxml")
soup_leg_actual = BeautifulSoup(contenido_leg_actual, "lxml")

#encontramos TODAS las etiquetas y las guardamos en arreglos "alltags"
#alltags contiene el nombre de las etiquetas y alltagscontent su contenido
allTagsID = [tag.name for tag in soup.find_all()]
allTagsContent = [tag.text for tag in soup.find_all()]

leg_actual_nombre = [tag.name for tag in soup_leg_actual.find_all()]
leg_actual_content = [tag.text for tag in soup_leg_actual.find_all()]

print (leg_actual_content[3])

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
#---------------------------------------------------------------------------------------
def obtener_etiquetas():
    for i in range(len(leg_actual_nombre)):
        print (leg_actual_nombre[i])
    for i in range(1):
        print (leg_actual_content[i])
    
            


#--------------------------------------------------------------------------------------
#from proyecto import*
#from legislatura import*

#import json
#from GeneraFecha import*



def datos_legislatura():
    numero = buscar_etiqueta('sesion')
    return numero

#print (datos_legislatura())
    
    
   


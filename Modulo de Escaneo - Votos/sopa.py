import lxml;   import requests
from   bs4     import BeautifulSoup
import urllib; import urllib.request; import urllib.parse

#-Funcion que convierte URL en objeto BeautifulSoup
#------------------------------EXPLICACION-----------------------------------------
#Primero recibe una URL, la que a traves de la libreria URLLIB la abrirá
#Despues Leera el contenido de ese objeto URLLIB
#Luego, transforma ese objeto URLLIB en uno BeautifulSoup, indicando que estamos leyendo un XML
#Finalmente, retorna ese objeto BeautifulSoup
def soup(url):
    obj     = urllib.request.urlopen(url)      ## Retorna a una variable un objeto http.response 
    xml     = obj.read()                       ## Lee el contenido de ese objeto y lo almacena en una variable
    objSoup = BeautifulSoup(xml,"lxml")        ## Convierte el XML en un objeto BeautifulSoup
    return objSoup

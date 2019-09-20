import lxml;   import requests
from   bs4     import BeautifulSoup
import urllib; import urllib.request; import urllib.parse

# Esta funcion convierte una URL en objeto BeautifulSoup - Recibe como parámetro el string de una URL
# ----------------------------------------------- EXPLICACION -------------------------------------------------
# Primero recibe una URL, la que a través de la librería URLLIB la abrirá
# Después Leerá el contenido de ese objeto URLLIB a través de .obj.read()
# Luego, transforma ese objeto URLLIB en un objeto BeautifulSoup, indicandole que estamos leyendo un XML
# Finalmente, retorna ese objeto BeautifulSoup
def soup(url):
    obj     = urllib.request.urlopen(url)      ## Retorna a una variable un objeto http.response 
    xml     = obj.read()                       ## Lee el contenido de ese objeto y lo almacena en una variable
    objSoup = BeautifulSoup(xml,"lxml")        ## Convierte el XML en un objeto BeautifulSoup
    return objSoup

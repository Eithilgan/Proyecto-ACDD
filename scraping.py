#Librerías para hacer scraping
from bs4 import BeautifulSoup
import urllib.request
import re

#Pagina a escanear
url = "https://en.wikipedia.org/wiki/Artificial_intelligence"
page = urllib.request.urlopen(url)

try:
	page = urllib.request.urlopen(url)
except:
	print("Error")
soup = BeautifulSoup(page,"html.parser")

# Variable que guarda un filtro para el valor "tocsection-"
regex = re.compile('^tocsection-')

#Busca todas las "li" y aplica el filtro guardado en regex
#Es decir, va a buscar todas las "li" con clase "tocsection"
listas = soup.find_all("li",attrs={'class':regex})
print(listas)
print(" \n\n **************** \n\n")




'''Crea una arreglo llamado "contenido" donde inserta
el atributo "texto" de cada "li", luego imprime ese arreglo
'''
contenido = []
for li in listas:
	contenido.append(li.getText().split("\n")[0])

for i in range(0,len(contenido),1):
	print(contenido[i])

#*************************************************************
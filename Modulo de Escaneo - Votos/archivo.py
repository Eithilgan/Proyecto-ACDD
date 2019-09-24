from includes import * ; from sopa import    * ; from legislatura import * ; from sesiones import *
from proyecto import * ; from boletin import * ; from votaciones import  * ; from detalle import  *
from dialogo import  * ; from bs4 import BeautifulSoup 

# ------------------------------------------ EXPLICACION ------------------------------------------
# Esta función no retorna cosa alguna. Se encarga de crear un archivo con la discusion parlamentaria asociada a un id de Boletin
# Esta función recibe como parámetro el id de un boletin por ejemplo: "11571-21"
# En primer lugar, llama a la función getSesionesById, la cual retorna un arreglo con todas las sesiones (Esta función está al comienzo de este script)
# en las que se discute sobre el proyecto de ley al cual esta asociado ese id de boletin
# Por ejemplo: ['3731','3763']

# Despues, va a recorrer ese arreglo y va a llamar a la funcion getProyecto() que está en el script proyecto.py la cual
# retorna un arreglo, donde sus elementos son etiquetas XML con cada proyecto de ley tratado en una determinada sesion
# Por ejemplo: ['<proyecto_ley boletin=11571-21...','<proyecto_ley boletin=11324-65...']

# Luego, recorrera ese arreglo de etiquetas XML.    
# Guardará en una variable el proyecto que esté recorriendo y lo transformará en un string.
# y preguntará si el id de boletin se encuentra en ese string

# Por ejemplo: if('3731' está en '<proyecto_ley boletin=11571-21...')
# En caso de que no esté, no pasará nada. En caso de que sí esté,  llamará a la funcion getDialogo()
# la cual retornará un string con la discusion del proyecto que se le pase como parámentro.
# (Esta función está justo arriba, en este mismo script).
# Después creará un archivo de texto con el string de la discusion parlamentaria
# Ese archivo txt tendrá el nombre del id de boletin y el id de la sesion.

def creaFile(idboletin):
    aSesion = getSesionesById(idboletin)
    #print("\nEn el boletin ",idboletin," Existen las sesiones:",aSesion)
    for i in range(0,len(aSesion),1):
        #print("\n******* Analizando la sesion:",aSesion[i]," *******\n")
        aProyectos = getProyecto(aSesion[i])
        for j in range(0,len(aProyectos),1):
            string = str(aProyectos[j])
            if(idboletin in string):
                cadena   = getDialogo(aProyectos[j])
                namefile = "boletin "+idboletin+" discutido en la sesion "+aSesion[i]
                nfh      = open(namefile+".txt","w")
                nfh.write(cadena)
                print("- El archivo ",namefile+".txt"," fue creado exitosamente")
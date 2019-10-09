from includes import * ; from sopa import    * ; from legislatura import * ; from sesiones import *
from proyecto import * ; from boletin import * ; from votaciones import  * ; from detalle import  *
from dialogo import  * ; from bs4 import BeautifulSoup 

# ------------------------------------------ EXPLICACION ------------------------------------------
# Esta función retorna un string con la discusión parlamentaria de un boleti
# Esta función recibe como parámetro el id de un boletin por ejemplo: "11571-21"


def generaDialogo(idboletin): #Recibe como parámetro un id de boletin por ej: "11571-21"
    aSesion = getSesionesById(idboletin) #Llama a las funcion getSesionesById para guardar en un arreglo las sesiones en las que fue discutido el boletin que se le pase como parámetro
    for i in range(0,len(aSesion),1):    #Recorre ese arreglo de sesiones
        aProyectos = getProyecto(aSesion[i]) #Llama a la función getProyecto que retorna un arreglo con todas las etiquetas de los proyectos que se trataron en la sesión que reciba como parámetro. El arreglo queda así: ['<proyecto_ley boletin=11571-21...','<proyecto_ley boletin=11324-65...']
        if(aProyectos!=None): #Valida que el arreglo no esté vacío
            aDiscusion = []  #Crea un arreglo para guardar las discusiones del boletin, cada posición corresponde a una sesión donde ese boletín fue discutido
            for j in range(0,len(aProyectos),1): #Recorre todas esas etiquetas de proyectos
                string = str(aProyectos[j])      #Convierte esas etiquetas de proyectos en string, ya que viene como formato BeautifulSoup
                if(idboletin in string):         #Valida que el Boletin en cuestión esté en esa etiqueta de proyecto de ley
                    cadena   = getDialogo(aProyectos[j]) # Llama a la función getDialogo, la que retorna un string con la discusión parlamentaria, recibe como parámetro una etiqueta de proyecto de ley 
                    if(cadena==None):  #Si no hay discusión, no retorna nada
                        return
                    else:
                        aDiscusion.append(cadena) #Si hay discusión, añade esa discusión al arreglo aDiscusión
            return aDiscusion # Finalmente retorna el arreglo aDiscusión

from includes import * ; from sopa    import * ; from legislatura import * ; from sesiones import *
from proyecto import * ; from boletin import * ; from votaciones  import * ; from detalle  import *
from bs4      import BeautifulSoup 

# ------------------------------------------ EXPLICACION ------------------------------------------
# Esta funcion retorna una etiqueta con el dialogo que se da dentro de la etiqueta proyecto de ley
# Es decir, lo que hay justo después de la etiqueta <PROYECTO_LEY> y antes de la etiqueta <VOTACION>
# 
# En primer lugar, la funcion recibe como parametro la etiqueta de un proyecto de ley
# Por ejemplo:
#                 <proyecto_ley boletin="11571-21">AUTORIZACIÓN DE CAPTURA DE ESPECIES SALMONÍDEAS...
#                 <br/><br/>...<intervencion_diputado iddiputado="">...etc...
#                 </proyecto_ley>
#Lo primero que hace es transformar esa etiqueta a tipo String
#Después va a crear un arreglo, donde los elementos estaran separarados cuando exista un <br/>
# (Solo lo transforma a arreglo para poder elminiar los <br/>, luego lo volveremos a string)
#Por ejemplo:
#    tagProyecto = ["<proyecto_ley boletin...etc..","<intervencion_diputado...etc","Tiene la palabra el diputado..etc.."]
#Luego, lo transformamos nuevamente a string con la funcion join
#Despues va a cortar el string en la posicion donde esté "<votacion", ya que cuando comienza esta etiqueta
#termina la discusion parlamentaria e inician los resultados de la votacion
#
#Luego, Entra en un ciclo While que se encarga de eliminar lo que haya dentro de <     > 
#Finalmente retorna el string.
def getDialogo(tagProyecto):
    print
    flag2 = True
    try:
        tagProyecto    = str(tagProyecto)
        tagProyecto    = tagProyecto.split("<br/>")
        tagProyecto    = "".join(tagProyecto)
        tagProyecto    = tagProyecto[:tagProyecto.index("<votacion")]
        flag = True
        while(flag==True):
            try:
                flag        = True
                inicio      = tagProyecto.index("<")
                final       = tagProyecto.index(">")
                tagProyecto = tagProyecto[:inicio]+tagProyecto[final:][1:]
            except:
                flag = False
    except:
        return None
    return tagProyecto
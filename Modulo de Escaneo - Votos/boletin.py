#-Funcion para obtener el ID-BOLETIN
#------------------------------EXPLICACION-----------------------------------------
#Primero convierte el proyecto de ley que en tipo String
#Como lo que recibe es (por ejemplo): <11490-24> ó <11490-24, 12426-06 9119-18>
#Lo que hace es ubicar en que posicion están los signos mayor que y menor que
#Una vez que tiene estas posiciones, se las quita
#En caso de que halla más de un ID de boletin, hará de la variable boletin un arreglo, de tal manera que separa los elementos cuando encuentre el caracter 34 (que son las comillas)
#Una vez creado este arreglo con los ID de boletin, seleccionará solo el primer ID de boletin y lo guardara, ya que cualquiera de los ID nos conducirá a la misma pagina de votaciones.
# Si existiera un espacio en blanco, lo quita
# Finalmente retorna un ID de Boletin
#----------------------------------------------------------------------------------
def getBoletin(proyecto):
    proyecto  = str(proyecto)
    index     = proyecto.find("<")
    end       = proyecto.find(">")
    idBoletin = proyecto[index:end]
    idBoletin = idBoletin.split(chr(34)) #Separa cuando hay comillas
    idBoletin = idBoletin[1]

    if(idBoletin.find(" ")!=-1):
        idBoletin = idBoletin.split(" ")
        idBoletin = idBoletin[0]
    return idBoletin

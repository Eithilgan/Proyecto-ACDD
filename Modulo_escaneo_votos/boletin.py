#-Funcion para obtener el ID de un BOLETIN - Recibe como parámetro el contenido de una etiqueta <PROYECTO_LEY>
#------------------------------EXPLICACION-----------------------------------------
#Ejemplo de lo que recíbe como parámetro: <PROYECTO_LEY BOLETIN="11571-21"> .... </PROYECTO_LEY>
#Primero convierte la etiqueta <PROYECTO_LEY> en tipo String (ya que es un objeto BeautifulSoup).

#Después lo que hace es ubicar en que posicion están los signos "mayor que y menor que", sin lugar a duda
#Hay muchos de estos signos en el string. Pero siempre los primeros "mayor que y menor que" tienen el ó los ID de boletín

#Una vez que tiene estas posiciones, corta el string en esas posiciones
#Si el string era así: 
#               <PROYECTO_LEY BOLETIN="11571-21">....<INTERVENCIÓN>....</INTERVENCIÓN>....
#Entonces quedaría así :
#               <PROYECTO_LEY BOLETIN="11571-21">


#En caso de que halla más de un ID de boletin, hará de la variable boletin un arreglo, de tal manera que separa los elementos cuando encuentre el caracter 34 (que son las comillas)
#Si el string era así:
#              <PROYECTO_LEY BOLETIN="11571-21">
#              Entonces el arreglo quedaría así: [   <PROYECTO_LEY BOLETIN=,  11571-21,    > ]

#Si el string era así:
#              <PROYECTO_LEY BOLETIN="11571-21, 12333-34">
#              Entonces el arreglo quedaría así: [   <PROYECTO_LEY BOLETIN=,  11571-21,  12333-34  ,  > ]



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

from sopa    import * ; from legislatura import * ;  from sesiones   import * ; from proyecto import *;
from boletin import * ; from votaciones  import * ;  from detalle    import * ; from archivo  import *; 
from clases  import * ; from insertaDato import * ;  import os

#Esta función borra la base de datos llamada: "Camara"
#DeleteDatabase()

#DataOfLeg es una variable, que llama a la función getDataOfLegislaturaActual(), esta función está en el archivo
#legislatura,py y lo que hace es extraer todos los datos de la legislatura actual es decir:
#ID, Numero, Fecha_Inicio, Fecha_Termino y Tipo. Esta función retorna un arreglo.
#Ahora en DataOfLeg se va a guardar un arreglo con todos los datos de la legislatura actual
DataOfLeg    = getDataOfLegislaturaActual()

#InsertarRegistro() es una función que está en el archivo insertarDato.py y se encarga de insertar registros a la
#Base de datos, esta función recibe dos parametros: Uno es un string que le indica a que colección va a ingresar
#El dato, en este caso queremos insertar los datos en la colección de la base de datos llamada "Legislatura".
#El segundo parametro que recibe es: El metodo constructor de un objeto "Legislatura", el objeto legislatura
#Tiene atributos ID, Numero, Fecha_Inicio, Fecha_Termino y Tipo. 

duplicado = IsDuplicate("Legislatura","idlegislatura",DataOfLeg[0])
if(duplicado==False):
    insertarRegistro("Legislatura",Legislatura(DataOfLeg[0],DataOfLeg[1],DataOfLeg[2],DataOfLeg[3],DataOfLeg[4]))


directorioSesiones = "Sesiones2"
#a_sesion es una variable que guarda un arreglo con todas las sesiones pertenecientes a la legislatura actual
a_sesion = getSesiones(DataOfLeg[0])
#Aquí se guardan las carpetas de las sesiones ya analizadas, básicamente para que no las vuelva a analizar
folderSesiones = [dI for dI in os.listdir(os.getcwd()+"\\"+directorioSesiones) if os.path.isdir(os.path.join(os.getcwd()+"\\"+directorioSesiones,dI))] 
print("#####\nLas sesiones de la legislatura actual son:\n",a_sesion,"#####\n")
print("\n  -- Largo :",len(a_sesion),"\n")
#Borrar del arreglo a_sesion aquellas sesiones que ya están hechas (esto a partir del arreglo folderSesiones)
#que tiene las sesiones ya hechas.
for a in range(0,len(folderSesiones),1):
    if(folderSesiones[a] in a_sesion):
        print("[ - Saqué a:",folderSesiones[a]," - ]")
        a_sesion.pop(a_sesion.index(folderSesiones[a]))
print("Las sesiones que analizaré son:\n",a_sesion,"##############")
print("\n  -- Largo (Sacadas las sesiones hechas):",len(a_sesion),"\n")


################################################################################################################
################################################################################################################



#Probar que pasa con una sesión en particular
#a_sesion=["3813"] 3737, 11934-15 30748-30736



#Este es un ciclo for que va a recorrer todas las sesiones del arreglo a_sesion
for i in range(0, len(a_sesion), 1):
    
    #datosSesion es una variable que llama a la función getDataOfSesion() está función recibe como parámetro el id de
    #una sesión y retorna un arreglo con varios datos de dicha sesión, por ej así: [ID,Numero,Fecha,Termino,Tipo,Estado]
    #InsertarRegistro() es una función que está en el archivo insertarDato.py y se encarga de insertar registros a la
    #Base de datos, esta función recibe dos parametros: Uno es un string que le indica a que colección va a ingresar
    #El dato, en este caso queremos insertar los datos en la colección de la base de datos llamada "Sesion".
    #El segundo parametro que recibe es: El metodo constructor de un objeto "Sesion", el objeto Sesion
    #Tiene atributos: IdLegislatura, idSesion, numero, fecha_inicio, fecha_termino y tipo. 
    datosSesion = getDataOfSesion(a_sesion[i])
    duplicado = IsDuplicate("Sesion","idsesion",datosSesion[0])
    if(duplicado==False):
        insertarRegistro("Sesion",Sesion(DataOfLeg[0],datosSesion[0],datosSesion[1],datosSesion[2],datosSesion[3],datosSesion[4]))
 

    #etiquetasProyecto es una variable que llama a la función getProyecto, esta funcion recibe como parametro el ID de una
    #sola sesion, y retorna las etiquetas <PROYECTO_LEY> que existan en esa sesion. Ahora etiquetasProyecto es una variable
    #que contiene un arreglo, y cada posicion de ese arreglo es una etiqueta PROYECTO_LEY, pueden ser muchas, como puede
    #ser solo una, eso depende de cuantos proyectos de ley se hayan discutido en esa sesion que se le pasó como parametro
    etiquetasProyecto = getProyecto(a_sesion[i])
    
    #En caso de que no exista proyecto de ley discutido en esa sesión, no pasa nada.
    if(etiquetasProyecto is None):
        flag = False
    #En caso de que sí exista proyecto de ley discutido en esa sesión, hará lo que hay a continuación
    else:
        #Primero se crea un arreglo vacío para guardar los boletines que más adelante recibirá
        aBoletin = []

        #Se inicia un ciclo for para recorrer las etiquetas PROYECTO_LEY del arreglo etiquetasProyecto
        for j in range(0, len(etiquetasProyecto), 1):

            #idBoletin es una variable que llama a la función getBoletin, esta función recibe como parámetro una
            #etiqueta PROYECTO_LEY. Esta función retorna un ID de boletin, por ejemplo: "4321-123"
            idBoletin   = getBoletin(etiquetasProyecto[j])
            #nameBoletin = getNameBoletin(etiquetasProyecto[j])

            #En caso de que el boletín no esté vacío continúa
            if(idBoletin!="" and idBoletin!=None):
   
                #Añade el idBoletin al arreglo aBoletin creado anteriormente 
                aBoletin.append(idBoletin)
                #print("\n-Sesion:",a_sesion[i],"-Boletin: ",idBoletin)
  
                #idVotaciones es una variable que llama a la función getVotaciones, esta función recibe como parametro
                #Un id de boletín y retorna un arreglo con varios id de votaciones que hubieron en ese boletín en particular.
                idVotaciones = getVotaciones(idBoletin)

                #Continúa en caso de que SI haya votación en ese boletin 
                if(idVotaciones!=None):
                    #contenido es una variable que llama a la función creaFile, esta función recibe como parametro el
                    #id de un boletín y retorna todo el contenido de la discusión parlamentaria asociada a ese boletín.
                    #Además de esto, la función crea un archivo de texto con ese contenido.
                    contenido = creaFile(idBoletin)
                    if(contenido==None):
                        flag = False
                    else:
                        #InsertarRegistro() es una función que está en el archivo insertarDato.py y se encarga de insertar registros a la
                        #Base de datos, esta función recibe dos parametros: Uno es un string que le indica a que colección va a ingresar
                        #El dato, en este caso queremos insertar los datos en la colección de la base de datos llamada "Boletin".
                        #El segundo parametro que recibe es: El metodo constructor de un objeto "Boletin", el objeto Boletin
                        #Tiene atributos: IdBoletin, Nombre y contenido. 
                        duplicado = IsDuplicate("Boletin","idboletin",str(idBoletin))
                        if(duplicado==False):
                            insertarRegistro("Boletin",Boletin(str(idBoletin)," ","Prediccion",contenido,"score"))

                        
                        #Este es un ciclo for que recorre el arreglo de las votaciones que hubieron en un boletin particular
                        for g in range(0, len(idVotaciones), 1):
                            
                            #resultadoVotacion es una variable que llama a la función getDetalle, esta función recibe como
                            #parámetro un id de votación y retorna su resultado (aprobado o rechazado)
                            resultadoVotacion = getDetalle(idVotaciones[g])
                            
                            #print("- Resultado de la votación ",idVotaciones[g],":",resultadoVotacion)  
                            
                            #InsertarRegistro() es una función que está en el archivo insertarDato.py y se encarga de insertar registros a la
                            #Base de datos, esta función recibe dos parametros: Uno es un string que le indica a que colección va a ingresar
                            #El dato, en este caso queremos insertar los datos en la colección de la base de datos llamada "Votaciones".
                            #El segundo parametro que recibe es: El metodo constructor de un objeto "Votaciones", el objeto Votaciones
                            #Tiene atributos: IdVotaciones, boletin, resultado, a_favor, en_contra y abstención
                            datosVotacion = getDataOfVotacion(idVotaciones[g])
                            duplicado = IsDuplicate("Votaciones","idvotaciones",str(idVotaciones[g]))
                            if(duplicado==False):
                                insertarRegistro("Votaciones",Votaciones(idVotaciones[g],str(idBoletin),resultadoVotacion,datosVotacion[0],datosVotacion[1],datosVotacion[2],datosVotacion[3]))
                            
                            
                            
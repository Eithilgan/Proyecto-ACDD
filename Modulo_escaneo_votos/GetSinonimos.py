from includes import * ; from sopa import * 
import requests
from bs4 import BeautifulSoup
def normalize(s):
    if("," in s):
        s.replace(",","")
    if(")" in s):
        s.replace(")","")
    if("(" in s):
        s.replace("(","")
    if("." in s):
        s.replace(".","")
    if("-" in s):
        s.replace("-","")
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in replacements:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s

cosa = "REGULACIÓN DE ACCESO A REGISTROS DE ENTREVISTAS INVESTIGATIVAS VIDEOGRABADAS Y DE DECLARACIONES JUDICIALES ESTABLECIDAS EN LEY N° 21.057 (Primer trámite constitucional. Boletín N° 12637-07)El señor FLORES, don Iván (Presidente).- En el Orden del Día, corresponde tratar el proyecto de ley, iniciado en mensaje, que regula el acceso a los registros de entrevistas investigativas videograbadas y de declaraciones judiciales de la ley N° 21.057, para los fines que indica.Diputado informante de la Comisión de Constitución, Legislación, Justicia y Reglamento es el señor Luciano Cruz-Coke Carvallo.Antecedentes:-Moción, sesión 28ª de la presente legislatura, en jueves 16 de mayo de 2019. Documentos de la Cuenta N° 1.-Informe de la Comisión de Constitución, Legislación, Justicia y Reglamento, sesión 48ª de la presente legislatura, en jueves 4 de julio de 2019. Documentos de la Cuenta N° 2.El señor FLORES, don Iván (Presidente).- Tiene la palabra el diputado informante.El señor CRUZ-COKE (de pie).- Señor Presidente, honorables diputadas y diputados, en representación de la Comisión de Constitución, Legislación, Justicia y Reglamento, vengo en informar, en primer trámite constitucional y reglamentario, el proyecto de ley regula el acceso a los registros de entrevistas investigativas videograbadas y de declaraciones judiciales de la ley N° 21.057, para los fines que indica, iniciado en mensaje de su excelencia el Presidente de la República.La idea matriz o fundamental de esta iniciativa consiste en modificar la ley N° 21.057, que regula entrevistas grabadas en video y otras medidas de resguardo a menores de edad víctimas de delitos sexuales, con el propósito de permitir el acceso a los registros de entrevistas investigativas videograbadas y declaraciones judiciales exclusivamente para los efectos del cumplimento del proceso de formación del artículo 28, como para los efectos del artículo 18, letra d), ambos artículos de la ley mencionada anteriormente.Durante la discusión de esta iniciativa, asistieron el señor Hernán Larraín Fernández, ministro de Justicia y Derechos Humanos; la señora Nora Rosati, magistrada del Segundo Tribunal de Juicio Oral en lo Penal de Santiago; la señora Erika Maira Bravo, gerenta de la División de Atención a las Víctimas y Testigos del Ministerio Público; la señora Karin Hein, representante de la Fundación Amparo y Justicia; la general de Carabineros señora Berta Robles Fernández, jefa de Zona de Prevención y Protección de la Familia; el señor Héctor González, prefecto inspector y jefe nacional de Delitos Sexuales de la PDI. La mayoría de ellos es representante de instituciones públicas que trabajaron en forma mancomunada en la Subcomisión Técnica de la Comisión Nacional de Coordinación del Sistema de Justicia Penal, la cual observó la necesidad de una modificación legal referente al acceso a los registros de las entrevistas investigativas videograbadas y declaraciones judiciales. Estas entrevistas, dada su naturaleza tan sensible, están sujetas a un deber de reserva por el artículo 23 de la ley N° 21.057, que hace muy restrictivo su acceso. El propósito de este proyecto es dar acceso a estas entrevistas en dos casos.Primero, para dar cumplimiento al artículo 28 de la ley N° 21.057, sobre entrevistas videograbadas, que establece un proceso de formación y capacitación continua de los entrevistadores encargados de la delicada misión de entrevistar a menores que han sido víctimas de delitos sexuales, que, como se puede advertir, es una situación compleja que requiere de un conocimiento especializado para evitar revictimizar al menor. La idea es que los entrevistadores de las instituciones autorizadas, esto es Poder Judicial, Ministerio del Interior y Seguridad Pública, Ministerio Público, Carabineros de Chile y la Policía de Investigaciones, puedan tener acceso a estas entrevistas (previa adopción de medidas para evitar la identificación del menor que aparece en la entrevista, como mediante deformación de imagen) para su proceso de aprendizaje.El segundo propósito del proyecto es solucionar un problema originado"
aCosa = cosa.split()


for i in range(0,len(aCosa),1):
    if(len(aCosa[i])>2):
        try:

            url = "https://www.wordreference.com/sinonimos/"+str(normalize(aCosa[i].lower()))
            r = requests.get(url)
            sopita = BeautifulSoup(r.text,"html.parser")
            result = sopita.find("div",{"id":"article"})
            print("** Sinonimos de ",aCosa[i],"**")
            aSinonimos = result.ul.li.text.split(",")
            
            for j in range(0,len(aSinonimos),1):
                print("- ",aSinonimos[j])
            print("\n")
        except:
            flag=False
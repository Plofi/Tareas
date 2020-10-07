"""
Ej.5.12 - Escribir una función que dada la cantidad de ejercicios de 
un examen, y el porcentaje necesario de ejercicios bien resueltos
necesario para aprobar dicho examen, revise un grupo de exámenes.
Para ello, en cada paso debe preguntar la cantidad de ejercicios 
resueltos por el alumno, indicando con un valor centinela que no hay 
más exámenes a revisar. Debe mostrar por pantalla el porcentaje
correspondiente a la cantidad de ejercicios resueltos respecto a la
cantidad de ejercicios del examen y una leyenda que indique si aprobó o no.

"""
def correccion_examen(cant_ej):
    """
    Devuelve la cantidad de respuestas correctas de un examen.

            Parameters:
                    (int) Cantidad total de ejercicios del examen.
                    (str) Hay que ir indicando si cada ejecicio fue resuelto correctamente.

            Returns:
                    Cantidad de respuestas correctas.

    """
    correctas = 0
    for i in range(1,cant_ej+1):
        ok = input(f"Indique si el ejercicio {i} fue resuelto correctamente: Si/No: ")
        if ok == "Si":
            correctas += 1
    return correctas


def alumno_resultado_examen():
    """
    Devuelve si el examen fue aprobado o no y el porcentaje de respuestas correctas.

            Parameters:
                    (int) Cantidad total de ejercicios del examen.
                    (int) Cantidad de ejercicios necesarios para aprobar.
                    Cantidad de respuestas correctas del alumno.
            
            Returns:
                    El resultado del examen: No aprobado o aprobado con % / 100.

    """
    cant_ej = int(input("Indique la cantidad de ejercicios que tiene su examen:"))
    aprobar = int(input("Indique la cantidad de ejercicios que deben estar correctos para aprobar su examen:"))
            
    centinela = input("Desea ingresar como le fue en cada ejercicio a su alumno (-No- para terminar):")
    while not centinela == "No":
        correctas = correccion_examen(cant_ej)
    
        if not correctas >= aprobar:
            resultado = "Examen no aprobado."
            return resultado
        else:
            porcentaje = (correctas * 100) / cant_ej
            resultado = (f"Examen aprobado con: {porcentaje}/100")
            return resultado
        
   
def resultados_examenes():
    """
    Devuelve el número de examen, el nombre del alumno y el resultado del examen:
    si fue aprobado o no y el porcentaje de respuestas correctas. 
    Devuelve la cantidad de alumnos, cuantos aprobaron y el porcentaje de aprobados.

            Parameters:
                    (str) Nombre del alumno.
                    (int) Cantidad total de ejercicios del examen.
                    (int) Cantidad de ejercicios necesarios para aprobar.
                    Cantidad de respuestas correctas del alumno.
            
            Returns:
                    (str) El número de examen, el nombre del alumno y el resultado del examen:
                    "Examen no aprobado o aprobado con % / 100".
                    Devuelve la cantidad de alumnos, cuantos aprobaron y el porcentaje de aprobados.

    """
    centinela = input("Desea ingresar un alumno y su examen (-No- para terminar): ")
    alumno = {}
    numero_examen = 1
    aprobados = 0
    while not centinela == "No":
        alumno["Examen número"]= numero_examen
        print("Examen número:", numero_examen)
        nombre = input("Ingrese el nombre del alumno: ")
        alumno["Nombre alumno"]= nombre
        resultado = alumno_resultado_examen()
        alumno["Resultado examen"]= resultado
        if resultado != "Examen no aprobado.":
            aprobados += 1
        print(alumno)
        centinela = input("Desea ingresar otro alumno y su examen (-No- para terminar):")
        numero_examen += 1

    porcentaje_examenes = (aprobados * 100) / numero_examen-1
    return print(f"De {numero_examen-1} alumnos, aprobaron: {aprobados}, un {porcentaje_examenes}% de aprobados.")

resultados_examenes()

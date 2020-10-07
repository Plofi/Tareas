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

def resultados_examenes():
    """
    Devuelve si el examen está aprobado o no, y el porcentaje 
    correspondiente a la cantidad de ejercicios resueltos correctamente,
    respecto de la cantidad de ejercicios del examen.
            
            Parameters:
                    (int,float) Para los datos numéricos.
                    (str) El valor centinela es (*)
            
            Returns: 
                    print("Examen aprobado con: % / 100 o Examen no aprobado.")
    
    """
    ejercicios = int(input("Indique la cantidad de ejercicios que tiene su examen:"))
    aprobar = float(input("Indique la cantidad de ejercicios que deben estar correctos para aprobar su examen:"))
        
    ej_correctos = input("¿Cuántos ejercicios resolvió correctamente este alumno? (* para terminar):")
    while not ej_correctos == "*":
        ej_correctos = float(ej_correctos)
        if not ej_correctos >= aprobar:
            print("Examen no aprobado.")
        else:
            porcentaje = (ej_correctos * 100) / ejercicios
            print(f"Examen aprobado con: {porcentaje}/100")
        ej_correctos = input("¿Quiere ingresar otro examen? ¿Cuántos ejercicios resolvió correctamente este alumno? (* para terminar):")
   

resultados_examenes()
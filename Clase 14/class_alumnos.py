#from examenes_alumnos import correccion_examen, alumno_resultado_examen,resultados_examenes

class Alumno:
                
    def __init__(self,nombre,correctas,resultado):
        self.nombre = nombre
        self.correctas = correctas
        self.resultado = resultado
        
    def get_nombre(self):
        return self.nombre
    
    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_correctas(self):
        return self.correctas
    
    def set_correctas(self, correctas):
        self.correctas = correctas

    def get_resultado(self):
        return self.resultado
    """
    def set_resultado(self, resultado):
        self.resultado = resultado

    def respuestas_correctas(self, cant_ej):
        return correccion_examen
    
    def resultado_examen(self):
        return alumno_resultado_examen
    """      

alumno1 = Alumno("Plofi",8,"Aprobado")
alumno2 = Alumno("Gato", 7,"Aprobado")
alumnos = [alumno1,alumno2]

def imprimir(alumnos):
    print(alumnos)

imprimir(alumnos)


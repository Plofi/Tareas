class Alumno:
                
    def __init__(self, nombre, nota, resultado):
        self.nombre = nombre
        self.nota = nota
        self.resultado = resultado
        self.examenes = []
        
    def agregar_examen(self, examen):
        self.examenes.append(examen)

    def get_examen(self):
        return self.examenes.append

    def get_nombre(self):
        return self.nombre
    
    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_nota(self):
        return self.nota
    
    def set_nota(self, nota):
        self.nota = nota

    def get_resultado(self):
        return self.resultado

    def set_resultado(self, resultado):
        self.resultado = resultado

    def imprimir_alumno(self):
        print(f"Alumno: {self.nombre}, Nota: {self.nota}, Resultado examen: {self.resultado}")


alumno1 = Alumno("Plofi","8","Aprobado")
alumno2 = Alumno("Gato","7","Aprobado")
alumnos = [alumno1,alumno2]

def imprimir_alumnos(alumnos):
    for alumno in alumnos:
        alumno.imprimir_alumno()  

imprimir_alumnos(alumnos)


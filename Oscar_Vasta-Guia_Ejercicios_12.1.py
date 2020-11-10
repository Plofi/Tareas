"""
Oscar_Vasta-Guia_Ejercicios_12.1.

a) Implementar la clase Intervalo(desde, hasta) que representa un intervalo entre dos
instantes de tiempo (números enteros expresados en segundos), con la condición desde
< hasta. (la funcion valid_desde_menor_hasta valida que el tiempo asta sea mayor que el
    tiempo desde y si esta invertido devuelve un string con mensaje de error)
b) Implementar el método duracion que devuelve la duración en segundos del intervalo.
    (en caso que el período de teiempo este invertido , calcula la amplitud del período
     a la inversa para que el resultado de la amplitud del tiempo de un resultado absoluto)
c) Implementar el método interseccion que recibe otro intervalo y devuelve un nuevo intervalo
    resultante de la intersección entre ambos, o lanzar una excepción si la intersección
    es nula.(el método interseccion devuelve 2 parámetros , el 1º es el intervalode tiempo de
    intersección y el 2º es un string de aviso si el período se encuentra fuera del entorno o
    es nulo si los entornos se interceptan)
d) Implementar el método union que recibe otro intervalo. Si los intervalos no son adyacentes
    ni intersectan, debe lanzar una excepción. En caso contrario devuelve un nuevo
    intervalo resultante de la unión entre ambos. (el método union devuelve 2 parámetros , el 1º es
    la suma de los tiempos de los 2 períodos y el 2º es un string de aviso si el período se
    encuentra fuera del entorno)
"""
# a)
class intervalo:
    # constructor
    def __init__(self, desde, hasta):
        # atributos de instancia
        self.desde = desde
        self.hasta = hasta

    def valid_desde_menor_hasta(self):
        if self.desde < self.hasta:
            return ''
        else:
            return ' ERROR: El intervalo de tiempo esta invertido '
# b)
    def intervalo(self):
        if self.desde < self.hasta:
            return self.hasta-self.desde
        else:
            return self.desde-self.hasta
# c)
    def interseccion(self, desde2, hasta2):
        # 1º verifica si existe intersexión
        if hasta2 < self.desde or desde2 > self.hasta:
            return 0, 'el 2º periodo se encuentra fuera del entorno del 1º período'
        # 2º verifica si la interseccion es posterior o anterior al 1º intervalo
        if self.hasta > desde2 and hasta2 > self.hasta:
            return desde2 - self.hasta
        if desde2 < self.desde and hasta2 < self.hasta:
            return hasta2 - self.desde, ''
        # 3º verifica si unintervalo esta dentro del otro
        if self.desde < desde2 and self.hasta > hasta2:
            return hasta2 - desde2, ''
        if desde2 < self.desde and hasta2 > self.hasta:
            return self.hasta - self.desde, ''
# d)
    def union(self, desde2, hasta3):
        # 1º verifica si existe continuidad
        if hasta2 < self.desde or desde2 > self.hasta:
            return 0, 'el 2º periodo se encuentra fuera del entorno del 1º período'
        # 2º verifica si la interseccion es posterior o anterior al 1º intervalo
        if self.hasta => desde3 and hasta3 > self.hasta:
            return hasta3  - self.desde, ''
        if desde3 < self.desde and hasta3 d=> self.hasta:
            return hasta2 - self.desde, ''
        # 3º verifica si unintervalo esta dentro del otro
        if self.desde < desde2 and self.hasta > hasta2:
            return hasta2 - desde2,''
        if desde2 < self.desde and hasta2 > self.hasta:
            return self.hasta - self.desde, ''
#------------------ E.O.F. ------------------------------------------------------

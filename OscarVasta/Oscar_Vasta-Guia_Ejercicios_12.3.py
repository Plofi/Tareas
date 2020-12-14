
"""
Oscar_Vasta-Guia_Ejercicios_12.3.

a) Crear una clase Vector, que en su constructor reciba una lista de elementos que serán
    sus coordenadas. En el método __str__ se imprime su contenido con el formato [x,y,z]
b) Implementar el método __add__ que reciba otro vector, verifique si tienen la misma
    cantidad de elementos y devuelva un nuevo vector con la suma de ambos. Si no tienen la
    misma cantidad de elementos debe levantar una excepción.
c) Implementar el método __mul__ que reciba un número y devuelva un nuevo vector, con
    los elementos multiplicados por ese número.
"""
class Vector:
    def __init__(self, vec):
        self.vec = vec


    def __str__(self):
        if len(self.vec) > 2:
            return "[ %+ 0.3f , %+0.3f , %+0.3f ]" % ( self.vec[0], self.vec[1], self.vec[2])
        else:
            if len(self.vec) > 1:
                return "[ %+ 0.3f , %+0.3f ]" % ( self.vec[0], self.vec[1] )
            else:
                if len(self.vec) > 0:
                    return "[ %+ 0.3f  ]" % ( self.vec[0] )
                else:
                    return " "

    def __add__(self, otrovector):
        try:
            if len(otrovector) == len(self.vec):
                nuevovector=list()
                for i in range(len(self.vec)):
                    nuevovector.append(self.vec[i] + otrovector[i])
                return Vector(nuevovector)
            else:
                raise ValueError("!! Los vectores no tienen la misma cantidad de elementos no se pueden sumar !!")
        except  ValueError as e:
                return(e)

    def __mul__(self, multiplicador):
            nuevovector=list()
            for i in range(len(self.vec)):
                nuevovector.append(self.vec[i] * multiplicador)
            return Vector(nuevovector)
#------------------- PRUEBA ----------------------------------------
vector1 = (5, 6, 7)
a = Vector(vector1)
print('a) ', a)
print('_'* 80,'\n')
vector2 = (3, 6, -9)
b = vector2
c = a + b
print('b) suma ',a,' + ', Vector(b),'=', c )
print('_'*80,'\n')
vector3 = (17, -48)
g = vector3
h = a + g
print('b) suma ',a,' + ', Vector(g),'=', h )
print('_'* 80,'\n')
d = 12
f = a * d
print('C) multiplicación ', a,' x ', d, '=', f )
print('_'* 80)
#---------------------E.O.F.----------------------------------------

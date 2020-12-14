
"""
Oscar_Vasta-Guia_Ejercicios_12.2.

a) Crear una clase Fraccion, que cuente con dos atributos: dividendo y divisor, que se
asignan en el constructor, y se imprimen como X/Y en el método __str__.

b) Implementar el método __add__ que recibe otra fracción y devuelve una nueva fracción
con la suma de ambas.

c) Implementar el método __mul__ que recibe otra fracción y devuelve una nueva fracción
con el producto de ambas.

d) Crear un método simplificar que modifica la fracción actual de forma que los valores
del dividendo y divisor sean los menores posibles.
"""
class Fraccion:

    def __init__(self, dividendo, divisor, entero=0):
        self.dividendo = dividendo
        self.divisor = divisor
        self.entero = entero

    def __str__(self):
        if self.dividendo == 0 and self.divisor == 0 and self.entero == 0:
            return " "
        if self.dividendo == 0 and self.divisor == 0:
            return "(%i)" % (self.entero)
        if self.dividendo == 0 and self.entero == 0:
            return "0"
        if abs(self.entero) > 1:
            return "(%i %i/%i)" % (self.entero, self.dividendo, self.divisor)
        else:
            return "(%i/%i)" % ( self.dividendo, self.divisor)


    def __add__(self, otra):
        suma_dividendo = (self.dividendo * otra.divisor) + (otra.dividendo * self.divisor)
        suma_divisor = self.divisor * otra.divisor
        return Fraccion(suma_dividendo, suma_divisor)

    def __sub__(self, otra):
        resta_dividendo = (self.dividendo * otra.divisor) - (otra.dividendo * self.divisor)
        resta_divisor = self.divisor * otra.divisor
        return Fraccion(resta_dividendo, resta_divisor)

    def __mul__(self, otra):
        multiplica_dividendo = self.dividendo * otra.dividendo
        multiplica_divisor = self.divisor * otra.divisor
        return Fraccion(multiplica_dividendo, multiplica_divisor)

    def simplificar(self):
        if abs(self.divisor) > abs(self.dividendo):
            test = abs(self.dividendo)
        else:
            test = abs(self.divisor)
        for i in range(1, (test+1)):
            if self.dividendo % i == 0 and self.divisor % i == 0:
                mcd = i
            else:
                if self.dividendo % (i + 1) == 0 and self.divisor % (i + 1) == 0:
                    mcd = (i + 1)
                else:
                    entero = mcd
                    nuevodivisor = self.divisor / mcd
                    nuevodividendo = self.dividendo / mcd
                    if nuevodivisor == nuevodividendo:
                        nuevodivisor = 0
                        nuevodividendo = 0
                    if nuevodividendo < 0:
                        entero = mcd * (-1)
                    return Fraccion(nuevodividendo, nuevodivisor, entero)



#---------------------------------------------------------
cociente = Fraccion(5, 6)
print('a) ',cociente)
a = Fraccion(3, 6)
b = Fraccion(20, 8)
c = a + b
print('b) suma ',a,'+',b,'=', c, '=', Fraccion.simplificar(c))

d = a - b
print ('c) resta',a,'-',b,'=', d, '=', Fraccion.simplificar(d))
e = a * b
print ('d) multiplica',a,'x',b,'=', e, '=', Fraccion.simplificar(e))
#---------------------E.O.F.----------------------------------------

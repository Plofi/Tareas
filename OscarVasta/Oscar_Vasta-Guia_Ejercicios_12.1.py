"""
Oscar_Vasta-Guia_Ejercicios_12.1.

a) Implementar la clase Intervalo(desde, hasta) que representa un intervalo entre dos
instantes de tiempo (números enteros expresados en segundos), con la condición desde
< hasta.
    **Si el intervalo enviado tubiera un tiempo desde mayor devuelve un assertError alertándolo.**

b) Implementar el método duracion que devuelve la duración en segundos del intervalo.

c) Implementar el método interseccion que recibe otro intervalo y devuelve un nuevo intervalo
    resultante de la intersección entre ambos, o lanzar una excepción si la intersección
    es nula.
        **Si el período enviado no tiene continuidad con el 1º períod la funcion interseccion() devuelve un ValueError alertándolo.**

d) Implementar el método union que recibe otro intervalo. Si los intervalos no son adyacentes
    ni intersectan, debe lanzar una excepción. En caso contrario devuelve un nuevo
    intervalo resultante de la unión entre ambos.
        **Si el período enviado no tiene continuidad con el 1º períod la funcion union() devuelve un ValueError alertándolo.**
"""

# a)
class Intervalo:
    # Atributos o propiedades
    desde = 0
    hasta = 0
    #interpreto que al poner los atributos en 0 , le estoy indicando que es un número entero, no ?

    # constructor
    def __init__(self, desde, hasta):
        # atributos de instancia
        try:
            assert desde < hasta, "desde debe ser menor que hasta"
        except AssertionError as e:
            print(e)
        self.desde = desde
        self.hasta = hasta
# b)
    def duracion(self):
        return self.hasta - self.desde
# c)
    def interseccion(self, desde2, hasta2):
        # [] ()
        # [(])
        # ([)]
        try:
            if self.hasta > desde2 and self.hasta <= hasta2:
                # [()] o ([)]
                if self.desde <= desde2:
                # ([)]
                    return desde2, self.hasta
                else:
                    # [()]
                    return self.desde, self.hasta
            else:
                # [] ()
                # [(])
                if self.desde > desde2 and self.desde <= hasta2:
                    # [(])
                    return self.desde, hasta2
                else:
                    raise ValueError("No hay interseccion entre intervalos")
        except ValueError as e:
            print(e)
# d)
    def union(self, desde2, hasta2):
        # [] ()
        # [(])
        # ([)]
        try:
            if self.hasta > desde2 and self.hasta <= hasta2:
                # [()] o ([)]
                if self.desde <= desde2:
                # ([)]
                    return self.desde, hasta2
                else:
                    # [()]
                    return desde2, hasta2
            else:
                # [] ()
                # [(])
                if self.desde > desde2 and self.desde <= hasta2:
                    # [(])
                    return desde2, self.hasta
                else:
                    raise ValueError("No hay interseccion entre intervalos")
        except ValueError as e:
            print(e)

#----------------------------------------------------------------
print("Carga y validacion de Intervalos")
intervalo1=Intervalo(23654, 23789)
intervalo2=Intervalo(0, 112)
intervalo3=Intervalo(480, 498)
intervalo4=Intervalo(500, 498)
intervalos=[intervalo1, intervalo2, intervalo3, intervalo4]
print('_'*80)
# prueba b
print("Duración:")
for interv in intervalos:
        print(interv.duracion())
print('_'*80)
#prueba c)
print("Intersección:")
print('(23500, 23700)', intervalo1.interseccion(23500, 23700))
print('(-1, 120)', intervalo2.interseccion(-1, 120))
print('(490, 500)', intervalo3.interseccion(490, 500))
print('(499, 600)', intervalo3.interseccion(499, 600))
print('_'*80)
#prueba d)
print("Union:")
print('(23500, 23700)', intervalo1.union(23500, 23700))
print('(-1, 120)', intervalo2.union(-1, 120))
print('(490, 500)', intervalo3.union(490, 500))
print('(499, 600)', intervalo3.union(499, 600))
print('_'*80)




#------------------------ E.O.F. --------------------------------

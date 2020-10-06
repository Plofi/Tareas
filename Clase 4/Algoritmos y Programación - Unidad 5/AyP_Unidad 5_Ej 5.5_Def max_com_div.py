"""
Ej. 5.5 - Algoritmo de Euclides: Implementar el algoritmo de Euclides
para calcular el máximo común divisor de dos números n y m, 
dado por los siguientes pasos:
1. Teniendo n y m, se obtiene r, el resto de la división entera de m/n.
2. Si r es cero, n es el mcd de los valores iniciales.
3. Se reemplaza m --n, n -- r, y se vuelve al primer paso.
Hacer un seguimiento del algoritmo implementado para los siguientes
pares de números: (15,9); (9,15); (10,8);(12/6)

"""

def max_com_div(m,n):
    """
    Calcula el máximo divisor entre dos números enteros.

        Parameters: 
                int(m,n) Dos números enteros.

        Returns: 
                (int) El máximo común divisor.

    """
    assert isinstance(m, int), "Su número ingresado debe ser entero."
    assert isinstance(n, int), "Su número ingresado debe ser entero."

    r = m % n
    if r == 0:
       return n
    else:
        while not r == 0:
            m = n
            n = r
            r = m % n
            if r == 0:
                return n

#Ej.
m = int(input("Ingrese su 1er número:"))
n = int(input("Ingrese su 2do número, le diremos el máximo común divisor entre ambos:"))

print("El máximo común divisor es:", max_com_div(m,n))

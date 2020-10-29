"""
Ejercicio 7.1. Escribir una función que reciba una tupla de elementos e
indique si se encuentran ordenados de menor a mayor o no.
"""
def ordenada(tupla): 
    """
    Indica si una tupla de números o strings está oredenada de menor a mayor o alfabeticamente.

        Parameters:
                (tuple) Sólo formada por (int) o (str).

        Returns:
                (str) Cadena que indica si está ordenada o no.

    """
    tupla = list(tupla)
    ordenada = sorted(tupla)
    if tupla == ordenada:
        return "Su tupla está ordenada."
    else:
        return "Su tupla está desordenada."
    
#Ejemplo:
herramientas_solas = ('alicate','martillo','sierra','cuter','destornillador phillips')
numeros = (1,2,3,4,5)

print(ordenada(herramientas_solas))
print(ordenada(numeros))


# Otra opción si incluye ambos tipos int y str:
def orden_tupla(tupla):
    """
    Indica si una tupla de números y strings, está oredenada de menor a mayor o alfabeticamente.
    El orden debe corresponder a 1ro los números y luego los strings.

        Parameters:
                (tuple de int y/o str) Para que de por resultado que está ordenada,
                se considera que 1ro haya números de menor a mayor y luego strings en orden alfabético.

        Returns:
                (str) Cadena que indica si está ordenada o no.
                
    """
    numeros = [0,1,2,3,4,5,6,7,8,9,-1,-2,-3,-4,-5,-6,-7,-8,-9]
    lista_numeros = []
    lista_strings = []

    for item in tupla:
        if item not in numeros:
            lista_strings.append(item)
        else:
            lista_numeros.append(item)

    ordenar_numeros = sorted(lista_numeros)
    ordenar_strings = sorted(lista_strings)
    orden_final = (ordenar_numeros+ordenar_strings)
    orden_final = tuple(orden_final)

    if tupla == orden_final:
        return "Su tupla está ordenada."
    else:
        return "Su tupla está desordenada."

#Ejemplo:
herramientas = (2,'alicate',1,'martillo',3,'sierra',4,'cuter',5,'destornillador phillips')
herramientas_ordenadas = (1,2,3,"alicate","cuter","martillo")

print(orden_tupla(herramientas))
print(orden_tupla(herramientas_ordenadas))
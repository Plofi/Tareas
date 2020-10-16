"""
Ejercicio 6.1. Escribir funciones que dada una cadena de caracteres:
a) Imprima los dos primeros caracteres.

"""
def dos_prim_car(x):
    """
    Imprime los dos primeros caracteres de una cadena de caracteres.

        Parameters:
                (str) Cadena de caracteres.
        
        Return:
                (str) Dos primeros caracteres de una cadena.

    """
    assert isinstance(x,str), "Debe ingresar una cadena de caracteres."

    dpc = x[0:2]
    print(dpc)

#Ej.
dos_prim_car("Casa")
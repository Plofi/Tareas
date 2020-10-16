"""
Ejercicio 6.1. Escribir funciones que dada una cadena de caracteres:
b) Imprima los tres últimos caracteres.

"""
def tres_ult_car(x):
    """
    Imprime los tres últimos caracteres de una cadena de caracteres.

        Parameters:
                (str) Cadena de caracteres.
        
        Return:
                (str) Tres últimos caracteres de una cadena.

    """
    assert isinstance(x,str), "Debe ingresar una cadena de caracteres."

    tuc = x[-3:]
    print(tuc)

#Ej.
tres_ult_car("Caminos")
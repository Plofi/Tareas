"""
Ejercicio 6.1. Escribir funciones que dada una cadena de caracteres:
d) Dicha cadena en sentido inverso. Ej.: 'hola mundo!' debe imprimir '!odnum aloh'

"""
def invertir_car(cadena):
    """
    Imprime una cadena dada en sentido inverso.

        Parameters:
                (str) Cadena de caracteres.
        
        Return:
                (str) Imprime una cadena dada al revés (en sentido inverso).

    """
    assert isinstance(cadena,str), "Debe ingresar una cadena de caracteres."
    
    cadena_invertida = ""
    ult_letra = 1    
    for caracter in cadena:
        caracter = cadena[-ult_letra]
        cadena_invertida += caracter
        ult_letra = ult_letra + 1
    print(cadena_invertida)
    
#Ej.
invertir_car("hola mundo!")
"""
Ejercicio 6.1. Escribir funciones que dada una cadena de caracteres:
e) Imprima la cadena en un sentido y en sentido inverso. Ej: 'reflejo' imprime
'reflejoojelfer'.

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
    return(cadena_invertida)


def reflejo(cadena):
    """
    Imprime una cadena dada y a continuación la misma en sentido inverso.

        Parameters:
                (str) Cadena de caracteres.
        
        Return:
                (str) Imprime una cadena y a continuación al revés (en sentido inverso).

    """
    print(cadena+invertir_car(cadena))

#Ej.
reflejo("reflejo")
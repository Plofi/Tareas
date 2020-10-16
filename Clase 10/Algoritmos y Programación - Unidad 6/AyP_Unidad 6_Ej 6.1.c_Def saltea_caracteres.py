"""
Ejercicio 6.1. Escribir funciones que dada una cadena de caracteres:
c) Imprima dicha cadena cada dos caracteres. Ej.: 'recta' debería imprimir 'rca'

"""
def saltea_car(cadena):
    """
    Imprime un caracter cada dos de una cadena dada, empezando por el primero 
    (los espacios y puntuación cuentan como caracter).

        Parameters:
                (str) Cadena de caracteres.
        
        Return:
                (str) Imprime un caracter y se saltea el siguiente de una cadena dada.

    """
    assert isinstance(cadena,str), "Debe ingresar una cadena de caracteres."
    
    cadena_final = ""
    for i in range(0,len(cadena)):
        if i % 2 == 0:
            cadena_final += cadena[i]
    print(cadena_final)

#Ej.
saltea_car("Recta")

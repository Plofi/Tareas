"""
Ejercicio 6.7. Escribir funciones que dadas dos cadenas de caracteres:
a) Indique si la segunda cadena es una subcadena de la primera.
Por ejemplo, 'cadena' es una subcadena de 'subcadena'.

"""

def subcadena(cadena1,cadena2):
    """
    Devuelve si una cadena es una subcadena de la primera ingresada.
                
        Parameters:
                (str) Dos cadenas.

        Returns:
                (str) Una cadena que indica si la la 2da cadena ingresada,
                está contenida en la 1ra.
    
    """
    if cadena2 in cadena1:
        return("Su 2da cadena ingresada es una subcadena de la 1ra.")
    else:    
        return("Su 2da cadena ingresada no es una subcadena de la 1ra.")


#Ej.
print(subcadena("subcadena","cadena"))
"""
Ejercicio 6.5. Escribir una función que dada una cadena de caracteres, devuelva:
b) Dicha cadena con la primera letra de cada palabra en mayúsculas.
Por ejemplo, si recibe 'república argentina' debe devolver 'República Argentina'.

"""
def primera_mayuscula(cadena):
    """
    Devuelve una cadena donde la primera letra de cada palabra es mayúscula.

        Parameters:
                (str) Una cadena.

        Returns:
                (str) La cadena resultante de la misma cadena, 
                pero donde ahora cada palabra comienza con mayúscula.

    """
    cadena_final = ""
    
    cadena = cadena.split() # Separa las palabras
    for i in cadena:
        primer_letra = ""
        primer_letra += i[0] #Separa la 1ra letra
        primer_letra = primer_letra.upper() # La convierte a mayúscula
        cadena_final += primer_letra # La agrega a la cadena final
        cadena_final += i[1:]+ " " # Reconstruye el resto de la palabra más el espacio
    cadena_final = cadena_final[:-1] #Quita el último espacio
    return(cadena_final)

#Ej.
print(primera_mayuscula("república argentina"))
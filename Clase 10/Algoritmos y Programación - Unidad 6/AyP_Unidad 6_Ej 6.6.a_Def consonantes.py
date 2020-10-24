"""
Ejercicio 6.6. Escribir funciones que dada una cadena de caracteres:
a) Devuelva solamente las letras consonantes. Por ejemplo, si recibe 'algoritmos' o
'logaritmos' debe devolver 'lgrtms'.

"""
def consonantes(cadena):
    """
    Devuelve una cadena formada únicamente por las letras consonantes que la componen.

        Parameters:
                (str) Una cadena.
                
        Returns:
                (str) La cadena formada únicamente por las letras consonantes que la componen.
                Respeta si son mayúscúlas o minúsculas de origen.
                
    """
    cadena_final = ""
    vocales = ["a","e","i","o","u","A","E","I","O","U"]

    for caracter in cadena:
        if caracter not in vocales:
            cadena_final += caracter
    return(cadena_final)

#Ej.
print(consonantes("Algoritmos y Logaritmos"))

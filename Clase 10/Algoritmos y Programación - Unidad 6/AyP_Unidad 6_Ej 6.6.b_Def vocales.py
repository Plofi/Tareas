"""
Ejercicio 6.6. Escribir funciones que dada una cadena de caracteres:
b) Devuelva solamente las letras vocales. Por ejemplo, 
si recibe 'sin consonantes' debe devolver 'i ooae'.

"""

def vocales(cadena):
    """
    Devuelve una cadena formada únicamente por las letras vocales que la componen.

        Parameters:
                (str) Una cadena.
                
        Returns:
                (str) La cadena formada únicamente por las letras vocales que la componen.
                Respeta si son mayúscúlas o minúsculas de origen.

    """
    cadena_final = ""
    cadena = cadena.split()
    vocales = ["a","e","i","o","u","A","E","I","O","U"]

    for palabra in cadena:
        for caracter in palabra:
            if caracter in vocales:
                cadena_final += caracter
        cadena_final += " "
    print(cadena_final)

#Ej.
print(vocales("Sin consonantes"))

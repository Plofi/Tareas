"""
Ejercicio 6.6. Escribir funciones que dada una cadena de caracteres:
c) Reemplace cada vocal por su siguiente vocal. Por ejemplo, 
si recibe 'vestuario' debe devolver 'vistaerou'.

"""
def siguiente_vocal(cadena):
    """
    Devuelve una cadena donde las letras vocales que la componían originalmente,
    han sido reemplazadas por la siguiente. Respeta mayúscúlas y/o minúsculas de origen.
                
        Parameters:
                (str) Una cadena.

        Returns:
                (str) La cadena resultante de reemplazar las letras vocales originales,
                por su inmediata siguiente. Respeta mayúscúlas y/o minúsculas de origen.
                
    """
    cadena_final = ""
    cadena = cadena.split()
    vocales = ["a","e","i","o","u","A","E","I","O","U"]

    for palabra in cadena:
        for caracter in palabra:
            if caracter not in vocales:
                cadena_final += caracter
            else:
                if caracter in vocales:
                    posicion = vocales.index(caracter)
                    if posicion == 4:
                        cadena_final += vocales[0]
                    elif posicion == 9:
                        cadena_final += vocales[5]
                    else:
                        cadena_final += vocales[posicion+1]
        cadena_final += " "
    return(cadena_final[:-1])

#Ej.
print(siguiente_vocal("vestuario"))
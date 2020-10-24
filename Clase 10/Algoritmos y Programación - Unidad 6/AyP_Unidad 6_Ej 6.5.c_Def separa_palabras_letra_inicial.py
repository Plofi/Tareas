"""
Ejercicio 6.5. Escribir una función que dada una cadena de caracteres, devuelva:
c) Las palabras que comiencen con la letra ‘A’. Por ejemplo, si recibe 'Antes de ayer'
debe devolver 'Antes ayer'.

"""
def separa_palabras_letra_inicial(cadena,caracter):
    """
    Devuelve una cadena formada únicamente por las palabras que comienzan con la letra dada.

        Parameters:
                (str) Una cadena.
                (str) Un caracter o letra para que seleccione las palabras que comienzan con ella.

        Returns:
                (str) La cadena formada con palabras que sólo empiezan con el caracter dado.

    """
    cadena_final = ""
    cadena = cadena.split() 
    
    for palabra in cadena:
        primer_letra = ""
        primer_letra += palabra[0] 
        primer_letra = primer_letra.lower() 
        caracter = caracter.lower()
        if primer_letra == caracter:
            cadena_final += palabra + " "
    cadena_final = cadena_final[:-1] 
    return(cadena_final)

#Ej.
print(separa_palabras_letra_inicial("Antes de ayer","A"))
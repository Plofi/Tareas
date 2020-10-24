"""
Ejercicio 6.6. Escribir funciones que dada una cadena de caracteres:
d) Indique si se trata de un palíndromo. Por ejemplo, 'anita lava la tina'
es un palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda).

"""
def palindromo(cadena):
    """
    Devuelve una cadena que indica si la cadena o frase ingresada,
    es o no un palíndromo (se lee igual al derecho y al revés).
                
        Parameters:
                (str) Una cadena.

        Returns:
                (str) Una cadena que indica si la cadena ingresada,
                es o no un palíndromo (se lee igual de izq a der y su inverso).
                
    """
    cadena_original = ""
    for caracter in cadena:
        if caracter != " ":
            cadena_original += caracter

    cadena_invertida = ""
    ult_letra = 1    
    for caracter in cadena:
        caracter = cadena[-ult_letra]
        if caracter != " ":
            cadena_invertida += caracter
        ult_letra = ult_letra + 1
    
    if cadena_original == cadena_invertida:
        return("Su cadena es un palíndromo.")
    else:
        return("Su cadena no es un palíndromo.")

#Ej.
print(palindromo("anita lava la tina"))
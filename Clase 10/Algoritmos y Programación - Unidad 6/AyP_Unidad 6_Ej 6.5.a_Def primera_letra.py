"""
Ejercicio 6.5. Escribir una función que dada una cadena de caracteres, devuelva:
a) La primera letra de cada palabra. Por ejemplo, si recibe 'Universal Serial Bus' 
debe devolver 'USB'.

"""
def primera_letra(cadena):
    """
    Devuelve la primera letra de cada palabra de una cadena dada.

        Parameters:
                (str) Una cadena.

        Returns:
                (str) La cadena resultante de la primera letra 
                de cada palabra de la cadena dada.

    """
    cadena_final = ""

    cadena = cadena.split()
    for i in cadena:
        cadena_final += i[0]
    print(cadena_final)

#Ej.
print(primera_letra("Universal Serial Bus"))
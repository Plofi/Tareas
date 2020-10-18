"""
Ejercicio 6.2. Escribir funciones que dada una cadena y un caracter:
a) Inserte el caracter entre cada letra de la cadena. Ej: 'separar' y ',' debería devolver
's,e,p,a,r,a,r'

"""

def separador_caracteres(cadena,separador):
    """
    Inserta un caracter dado entre los caracteres de una cadena.

        Parameters:
                (str) Cadena de caracteres.
                ("") Caracter o signo de puntuación de separador.

        Returns:
                (str) Cadena resultante de insertar un caracter/separador entre cada caracter de la cadena dada.
    """
    assert isinstance(cadena, str), "Debe ingresar una cadena de caracteres."

    cadena_final = ""
    for caracter in cadena:
        cadena_final += caracter
        separado = separador.join(cadena_final)
    return separado

#Ej.
print(separador_caracteres("separar",","))


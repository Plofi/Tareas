"""
Ejercicio 6.2. Escribir funciones que dada una cadena y un caracter:
a) Inserte el caracter entre cada letra de la cadena. Ej: 'separar' y ',' debería devolver
's,e,p,a,r,a,r'

"""

def separar_comas(cadena):
    """
    Inserta una "coma" entre los caracteres de una cadena.

        Parameters:
                (str) Cadena de caracteres.

        Returns:
                (str) Cadena resultante de insertar una coma(,) entre cada caracter de la cadena dada.
    """
    assert isinstance(cadena, str), "Debe ingresar una cadena de caracteres."

    resultado = ""
    for caracter in cadena:
        resultado += caracter
        separado = ",".join(resultado)
    return separado

#Ej.
print(separar_comas("separar"))


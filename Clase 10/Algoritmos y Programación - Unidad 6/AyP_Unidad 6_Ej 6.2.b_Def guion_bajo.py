"""
Ejercicio 6.2. Escribir funciones que dada una cadena y un caracter:
b) Reemplace todos los espacios por el caracter. Ej: 'mi archivo de texto.txt' y '_'
debería devolver 'mi_archivo_de_texto.txt'

"""

def reemplazo_guion_bajo(cadena):
    """
    Inserta un "guión bajo" entre los caracteres de una cadena donde había espacios.

        Parameters:
                (str) Cadena de caracteres.

        Returns:
                (str) Cadena resultante de insertar un guión bajo(_) 
                entre cada caracter de la cadena dada, donde antes había un espacio.
                
    """
    assert isinstance(cadena, str), "Debe ingresar una cadena de caracteres."

    resultado = ""
    for caracter in cadena:
        if caracter != " ":
            resultado += caracter
        else:
            resultado += "_"
    return resultado

#Ej.
print(reemplazo_guion_bajo("mi archivo de texto.txt"))

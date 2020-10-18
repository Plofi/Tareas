"""
Ejercicio 6.2. Escribir funciones que dada una cadena y un caracter:
b) Reemplace todos los espacios por el caracter. Ej: 'mi archivo de texto.txt' y '_'
debería devolver 'mi_archivo_de_texto.txt'

"""

def reemplazo_espacio(cadena,reemplazo):
    """
    Inserta un caracter dado, donde antes había espacios.

        Parameters:
                (str) Cadena de caracteres.
                ("") Un caracter o una cadena, para ingresar como reemplazo.

        Returns:
                (str) Cadena resultante de insertar un caracter dado
                donde antes había un espacio.
                
    """
    assert isinstance(cadena, str), "Debe ingresar una cadena de caracteres."

    resultado = ""
    for caracter in cadena:
        if caracter != " ":
            resultado += caracter
        else:
            resultado += reemplazo
    return resultado

#Ej.
print(reemplazo_espacio("mi archivo de texto.txt", "_"))

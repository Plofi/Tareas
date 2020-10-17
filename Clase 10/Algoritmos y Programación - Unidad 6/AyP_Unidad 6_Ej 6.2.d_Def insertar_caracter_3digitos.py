"""
Ejercicio 6.2. Escribir funciones que dada una cadena y un caracter:
d) Inserte el caracter cada 3 dígitos en la cadena. Ej. '2552552550' y '.' debería devolver
'255.255.255.0'
"""

def insertar_caracter(cadena):
    """
    Inserta el caracter dado cada 3 dígitos en la cadena dada.

        Parameters:
                (str or int) Cadena de caracteres y/o números.

        Returns:
                (str) Cadena resultante que se obtiene de insertar un caracter dado cada 3 dígitos.
                
    """
    resultado = ""
    x = 3
    for caracter in range(x):
        while caracter <= len(cadena):
            resultado = resultado + cadena[caracter]
            x += 3
    resultado += "."
    return resultado

#Ej.
print(insertar_caracter('2552552550'))
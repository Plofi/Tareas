"""
Ejercicio 6.2. Escribir funciones que dada una cadena y un caracter:
c) Reemplace todos los dígitos en la cadena por el caracter. Ej: 'su clave es: 1540' y
'X' debería devolver 'su clave es: XXXX'

"""

def reemplazo_X(cadena):
    """
    Reemplaza todos los dígitos en una tupla o cadena por el caracter "X".

        Parameters:
                (tuple) or (str) Tupla o cadena de caracteres y/o números.

        Returns:
                (str) Cadena resultante que se obtiene de reemplazar 
                todos los dígitos de una tupla dada por "X" en su lugar.
                
    """
    cadena = tuple(cadena)
    resultado = ""
    for caracter in cadena:
        resultado += "X"
    return resultado

#Ej.
cadena = input("Ingrese su clave:")
print("Su clave es:", reemplazo_X(cadena))
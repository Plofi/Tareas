"""
Ej.4.5.a. Escribir una función que dado un año indicar si es bisiesto.
Nota: un año es bisiesto si es un número divisible por 4,
pero no es divisible por 100, excepto que también sea divisible por 400.

"""

def bisiesto(n):
    """
    Devuelve si un año es bisiesto.

        Parameters:
                int (n) Año ingresado en números enteros.
        
        Returns:
                (str) Cadena de texto que indica "Su año es o no es bisiesto."
    """
    assert isinstance(n, int),"Su año debe ser ingresado en números enteros."
    
    if n % 4 == 0 and not n % 100 == 0 or n % 400 == 0:
        return "Su año es bisiesto."
    else:
        return "Su año no es bisiesto."        

#ej.
print(bisiesto(1990))

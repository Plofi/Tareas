"""
Ejercicio 4.1.a. Escribir una función que resuelva el siguiente problema:
a) Dado un número entero n, indicar si es par o no.

"""

def numero_par(n):
    """
    Devuelve si un número es par o impar.

        Parameters: 
                int(n): Numero entero.
        
        Returns:
                (str) Cadena de texto que indica "Su número es par o impar"
    """
    assert isinstance(n,int),"Su número ingresado debe ser un entero."

    if n % 2 == 0:
        return ("Su número es par.")
    else:
        return ("Su número es impar.")

# ej.
print(numero_par(-8))
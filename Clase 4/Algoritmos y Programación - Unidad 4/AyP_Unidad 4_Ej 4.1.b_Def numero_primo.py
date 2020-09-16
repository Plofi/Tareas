"""
Ej.4.1.b. Escribir una función que dado un número entero n, indicar si es primo o no.
"""

def numero_primo (n):
    """
    Devuelve si un numero entero es primo o no.

        Parameters:
                (n) Número entero mayor a 0.

        Returns:
                (str) Cadena de texto que indica "Su número es primo o no es primo."

    """

    if n<2:
        return "Su número no es primo."
    for i in range (2,n):
        if n % i == 0:
            return "Su número no es primo."
    else:
        return "Su número es primo."

#ej.
print(numero_primo(41))
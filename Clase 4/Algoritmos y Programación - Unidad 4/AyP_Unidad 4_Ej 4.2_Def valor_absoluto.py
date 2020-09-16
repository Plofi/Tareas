"""
Ej.4.2. Escribir una implementación propia de la función abs, que devuelva el valor absoluto de cualquier valor que reciba.

"""
print(abs(-30.33)) # Si esto es lo que pedía el enunciado
# o una función pero para números enteros o flotantes:

def abs(n):
    """
    Devuelve el valor absoluto de un número entero o flotante.

        Parameters:
                int (n) or float(n): Número entero o flotante.

        Returns:
                Devuelve el valor absoluto de ese número.
    """
    if n >= 0:
        return n
    else:
        return -n

#Ej.
print(abs(-35))

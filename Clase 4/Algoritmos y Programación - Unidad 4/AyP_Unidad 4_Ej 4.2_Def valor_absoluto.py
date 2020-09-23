"""
Ej.4.2. Escribir una implementación propia de la función abs, que devuelva el valor absoluto de cualquier valor que reciba.

"""
print(abs(-30.33)) # Si esto es lo que pedía el enunciado
# o una función pero para números enteros o flotantes:

def absoluto(n):
    """
    Devuelve el valor absoluto de un número entero o flotante.

        Parameters:
                int(n) or float(n): Número entero o flotante.

        Returns:
                (int) Devuelve el valor absoluto de ese número.
    """
    assert isinstance(n,int) or (n,float), "Su número debe ser un número entero o flotante."
    
    if n >= 0:
        return n
    else:
        return -n

#Ej.
print(absoluto(-39))

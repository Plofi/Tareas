"""
Ejercicio 6.8. Escribir una función que reciba una cadena de unos y ceros
(es decir, un número en representación binaria) y devuelva el valor decimal correspondiente.

"""
def decimal(cadena):
    """
    Devuelve el valor decimal correspondiente dea una cadena en representación binaria.

        Parameters:
                (str o int) Una cadena de números en representación binaria 
                o un número binario .

        Returns:
                (str) Una cadena con el valor decimal correspondiente.
    """
    decimal = cadena[-2:]
    return decimal

#Ej.
print(decimal("101010101000100010"))
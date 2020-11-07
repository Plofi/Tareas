"""
Ejercicio 7.2. Dominó.
a) Escribir una función que indique si dos fichas de dominó encajan o no. 
Las fichas son recibidas en dos tuplas, por ejemplo: (3,4) y (5,4)

"""

def domino_tuplas(tupla1,tupla2):
    """
    Indica si dos fichas de dominó encajan o no, al recibirlas como 2 tuplas.

        Parameters: (int, tuple) Recibe dos tuplas de números enteros.

        Returns: (str) Cadena que indica si las fichas encajan o no.

    """
    if tupla1[0] == tupla2[0] or tupla1[0] == tupla2[1]:
        return "Sus fichas encajan."
    elif tupla1[1] == tupla2[0] or tupla1[1] == tupla2[1]:
        return "Sus fichas encajan."
    else:
        return "Sus fichas no encajan."


print(domino_tuplas((3,4),(5,4)))
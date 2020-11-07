"""
Ejercicio 7.2. Dominó.
b) Escribir una función que indique si dos fichas de dominó encajan o no. 
Las fichas son recibidas en una cadena, por ejemplo: 3-4  2-5. 
Nota: utilizar la función split de las cadenas.

"""

def domino_cadenas(a,b):
    """
    Indica si dos fichas de dominó encajan o no, al recibirlas como dos cadenas,
    cada numero debe estar separado por un guión (ej:"2-5").

        Parameters: (int,str) Recibe dos cadenas de números enteros, 
        dentro de ellas los números deben estar separados por un guión.

        Returns: (str) Cadena que indica si las fichas encajan o no.

    """
    ficha1 = a.split("-")
    ficha2 = b.split("-")
    

    if ficha1[0] == ficha2[0] or ficha1[0] == ficha2[1]:
        return "Sus fichas encajan."
    elif ficha1[1] == ficha2[0] or ficha1[1] == ficha2[1]:
        return "Sus fichas encajan."
    else:
        return "Sus fichas no encajan."


print(domino_cadenas("3-4","2-5"))
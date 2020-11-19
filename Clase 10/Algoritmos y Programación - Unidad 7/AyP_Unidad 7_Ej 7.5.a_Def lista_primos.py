"""
Ejercicio 7.5. Dada una lista de números enteros, escribir una función que:
a) Devuelva una lista con todos los que sean primos.
"""

def numero_primo(n):
    """
    Devuelve verdadero o falso si un número entero es primo o no.

        Parameters:
                (n) Número entero mayor a 0.

        Returns:
                (bool) Verdadero o Falso si el número es primo o no.

    """
    assert n> 0,"Su número ingresado debe ser mayor a 0."
    assert isinstance(n,int),"Su número debe ser un número entero."

    if n<2:
        return False
    for i in range (2,n):
        if n % i == 0:
            return False
    else:
        return True


def lista_primos(lista_num):
    """
    Devuelve todos los números primos que hay en la lista ingresada.

        Parameters:
                int(n) Lista de números enteros mayor a 1.

        Returns: 
                (int) Lista de números primos de la lista ingresada.
    
    """
    lista_primos = []

    for i in lista_num:
        primo = numero_primo(i)
        if primo == True:
            lista_primos.append(i)
    return lista_primos 


#Ej:
lista_num = [3,5,25,67,190,5983]

print(lista_primos(lista_num))
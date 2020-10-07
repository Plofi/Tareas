"""
Ej.5.10. Escribir una función que reciba un número natural
e imprima todos los números primos que hay hasta ese número.

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


def primos(n):
    """
    Devuelve todos los números primos que hay entre 1 y el número ingresado inclusive.

        Parameters:
                int(n) Número entero mayor a 1.

        Returns: 
                (int) Números primos entre 1 y el número ingresado inclusive.
    
    """
    assert n> 1,"Su número debe ser mayor a 1."
    assert isinstance(n,int),"Su número debe ser un número entero."

    num_primos = []
    for i in range(2,n+1):
        primo = numero_primo(i)
        if primo == True:
            num_primos.append(i)
    return num_primos 

#Ej.
n = int(input("Ingrese un número, le diremos los números primos hasta el ingresado inclusive:"))

print(f"Los números primos hasta {n} son:", primos(n))


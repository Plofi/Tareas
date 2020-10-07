"""
Ejercicio 5.9.a. Escribir una función que reciba dos números como parámetros, 
y devuelva cuántos múltiplos del primero hay, que sean menores que el segundo.

a) Implementarla utilizando un ciclo for, desde el primer número hasta el segundo.

"""

def multiplos_for(n1,n2):
    """
    Devuelve la cantidad de múltiplos que hay desde el 1er número 
    hasta llegar al segundo exclusive; los cuenta siempre y cuando su
    valor sea menor que el 2do número.

            Parameters:
                    int(n1,n2) Dos números enteros.
            
            Returns:
                    (int) Cantidad de múltiplos desde el 1er número, hasta llegar al 2do número exclusive.
                    Los cuenta siempre su valor sea menor que el 2do número.

    """
    assert isinstance(n1, int), "Su número ingresado debe ser entero."
    assert isinstance(n2, int), "Su número ingresado debe ser entero."

    multiplos = []  
    m = 0
    for i in range(n1, n2):
        m = n1 * i
        if m < n2:
            multiplos.append(m)
        else:    
            return (len(multiplos))

#Ej.
n1 = int(input("Introduzca su 1er número:"))
n2 = int(input("Introduzca su 2do número, le diremos cuantos múltiplos del 1er número hay entre ellos:"))

print(f"Entre {n1} y {n2}, hay {multiplos_for(n1,n2)} múltiplos de {n1}.")


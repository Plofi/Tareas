"""
Ejercicio 5.9.b. Escribir una función que reciba dos números como parámetros, 
y devuelva cuántos múltiplos del primero hay, que sean menores que el segundo.

b) Implementarla utilizando un ciclo while, que multiplique el primer número hasta que
sea mayor que el segundo.

"""

def multiplos_while(n1,n2):
    """
    Devuelve la cantidad de múltiplos que hay del 1er número 
    hasta llegar al segundo exclusive; los cuenta siempre y cuando su
    valor sea menor que el 2do número.

            Parameters:
                    int(n1,n2) Dos números enteros.
            
            Returns:
                    (int) Cantidad de múltiplos del 1er número, hasta llegar al 2do número.
                    Los cuenta siempre su valor sea menor que el 2do número.

    """
    assert isinstance(n1, int), "Su número ingresado debe ser entero."
    assert isinstance(n2, int), "Su número ingresado debe ser entero."

    multiplos = []  
    m = 0
    numerador = 1
    while m < n2:
        m = n1 * numerador
        numerador += 1
        if m < n2:
            multiplos.append(m)
    else:    
        return (len(multiplos))

#Ej.
n1 = int(input("Introduzca su 1er número:"))
n2 = int(input("Introduzca su 2do número, le diremos cuantos múltiplos del 1er número hay hasta el 2do número exclusive:"))

print(f"Hay {multiplos_while(n1,n2)} múltiplos de {n1}, hasta {n2} exclusive.")

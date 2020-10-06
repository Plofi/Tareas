"""
Ej. 5.8 - Escribir un programa que le pida al usuario que ingrese una
sucesión de números ( 1ro uno, luego otro, y así hasta que el usuario
ingrese "-1" como condición de salida).
Al final, el programa debe imprimir cuantos números fueron ingresados,
la suma total de los valores y el promedio.

"""

def num_centinela(n):
    """
    Devuelve cuantos números fueron ingresados, la suma total
    y el promedio entre ellos.

        Parameters:
                int or float(n): Números ingresados en números enteros o float.
                No puede utilizar el -1, ya que es el valor centinela para salir del programa.
        
        Returns:
                (str) Imprime una cadena de texto que indica "La cantidad de números
                ingresados, la suma total de los mismos y el promedio."
    
    """
    assert isinstance(n,int) or (n,float), "Su número ingresado debe ser un número entero o float."
        
    num_ingresados = []
    num_ingresados.append(n)
    suma_total = 0
    centinela = float(input("Ingrese un número, (""-1"" para terminar):"))

    while centinela != "-1":
        centinela = float(centinela)
        num_ingresados.append(centinela)
        centinela = input("¿Quiere ingresar otro número? (""-1"" para terminar):")

    for item in range(len(num_ingresados)):
        suma_total += num_ingresados[item]
    
    promedio = suma_total / len(num_ingresados)
    return print(f"La cantidad de números ingresados es: {len(num_ingresados)}, la suma total de ellos es: {suma_total} y su promedio es: {promedio}")

num_centinela(9)
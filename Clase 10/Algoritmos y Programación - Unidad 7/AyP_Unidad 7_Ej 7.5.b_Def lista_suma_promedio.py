"""
Ejercicio 7.5. Dada una lista de números enteros, escribir una función que:

b) Devuelva la sumatoria y el promedio de los valores.

"""

def lista_suma_promedio(lista_num):
    """
    Devuelve la sumatoria y el promedio de los números ingresados en una lista.

        Parameters:
                (int) Lista de números enteros.

        Returns: 
                (int) La sumatoria y el promedio de los valores ingresados.
    
    """
    suma = 0   

    for i in lista_num:
        suma = suma + i
    
    promedio = suma // len(lista_num)

    return suma, promedio


#Ej:
lista_num = [3,5,25,67,190,5983]

print(lista_suma_promedio(lista_num))

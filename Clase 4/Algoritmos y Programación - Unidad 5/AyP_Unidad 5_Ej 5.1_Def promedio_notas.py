"""
Ej.5.1 - Escribir un programa que permita al usuario ingresar un 
conjunto de notas, preguntando a cada paso si desea ingresar más notas,
e imprimiendo el promedio correspondiente.

"""
def promedio_notas(n):
    """
    Devuelve el promedio de las notas ingresadas.

        Parameters:
                int or float(n): Notas ingresadas en números enteros o float.
        
        Returns:
                (str) Imprime una cadena de texto que indica "El promedio de las notas ingresadas es:"
    
    """
    assert isinstance(n,int) or (n,float), "Su número ingresado debe ser un número entero o float."
    assert n > 0 and n <= 10, "Su nota debe estar entre 0 y 10."

    notas_ingresadas = []
    notas_ingresadas.append(n)
    mas_notas = "Si"
    suma_notas = 0

    while mas_notas == "Si":
        n = float(input("Ingrese otra nota, expresada en números, le diremos su promdedio:"))
        notas_ingresadas.append(n)
        mas_notas = input("¿Quiere ingresar más notas? Si/No.")

    for item in range(len(notas_ingresadas)):
        suma_notas += notas_ingresadas[item]
    
    promedio = suma_notas / len(notas_ingresadas)
    return print(f"El promedio de las notas {notas_ingresadas} es:{promedio}")

#Ej.
promedio_notas(5)
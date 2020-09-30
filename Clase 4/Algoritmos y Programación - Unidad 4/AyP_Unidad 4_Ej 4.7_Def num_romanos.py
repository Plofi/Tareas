"""
Ej.4.7 - Escribir un programa que reciba como entrada un entero representando un año 
(por ejemplo 751, 1999, o 2158), y muestre por pantalla el mismo año escrito en números romanos.

"""

def num_romano(a):
    """
    Devuelve el año ingresado convertido a números romanos.

        Parameters:
                int (a) Año ingresado en números enteros.
        
        Returns:
                (str) Cadena que indica "Su año ingresado, expresado en números romanos es igual a:".
    
    """
    assert isinstance(a,int),"Su año debe ser ingresado en números enteros."
    
    num_enteros = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    numeros_romanos = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    convertido = ""
    
    for i in range(len(num_enteros)):
        while (num_enteros[i] <= a):
            convertido = convertido + numeros_romanos[i]
            a = a - num_enteros[i]
    return f"Su año ingresado, expresado en números romanos es igual a: {convertido}."

#Ej.
a = int(input("Ingrese el año que quiere convertir a números romanos:"))

print(num_romano(a))
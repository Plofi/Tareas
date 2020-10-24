"""
Ejercicio 6.7. Escribir funciones que dadas dos cadenas de caracteres:
b) Devuelva la que sea anterior en orden alfábetico. 
Por ejemplo, si recibe 'kde' y 'gnome' debe devolver 'gnome'.

"""
def ordenada(cadena1,cadena2):
    """
    Devuelve la cadena que sea anterior en el orden alfabético.
                
        Parameters:
                (str) Dos cadenas.

        Returns:
                (str) La cadena de las dos ingresadas,
                que esté antes en el orden alfabético.
    
    """
    cadenas_ingresadas = []
    cadenas_ingresadas.append(cadena1)
    cadenas_ingresadas.append(cadena2)
    ordenada = sorted(cadenas_ingresadas)
    return(ordenada[0])

#Ej.
print(ordenada("kde","gnome"))
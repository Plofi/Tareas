"""
Ejercicio 6.4. Escribir una función que reciba una cadena que contiene 
un largo número entero y devuelva una cadena con el número 
y las separaciones de miles. Por ejemplo, si recibe
'1234567890', debe devolver '1.234.567.890'.
"""

def insertar_punto(numero):
    """
    Inserta el caracter (.) cada 3 dígitos en la cadena dada,
    siempre que la longitud de la cadena sea divisible por 3.

        Parameters:
                (str or int) Cadena de caracteres y/o números.
                   
        Returns:
                (str) Cadena resultante que se obtiene de insertar un punto cada 3 dígitos.
                    
    """           
    cadena = str(numero)
        
    cadena_final = ""
    p = 0 #posicion hasta la que selecciono dentro de la cadena inicial, para que copie los valores
    maximo = ((len(numero)-1)//3) #para que no agregue puntos demás al final, saber cuantos debe tener como máximo
        
    for i in range(len(numero)):
        cadena_final += cadena[p:p+3] #suma a lo que contiene la cadena entre los parémetros[i:j]
        if i == maximo:
            break
        else:
            cadena_final += "."
            p += 3 #va aumentando de 3 en 3, para limitar el rango de arriba y agregar el punto luego
    return(cadena_final)


def inserta_punto_miles(numero):
    """
    Inserta el un punto(.) cada 3 dígitos en el número o cadena dada.
    
        Parameters:
                (str or int) Cadena de caracteres y/o números.
                
        Returns:
                (str) Cadena resultante que se obtiene de insertar un punto(.) cada 3 dígitos.
                
    """
    numero = str(numero)
    total_numeros = len(numero)
    sumo_ceros = ""

    if total_numeros % 3 == 0:
        return print(insertar_punto(numero))
    elif total_numeros % 3 == 2:
        sumo_ceros += "0000" + numero
        sumo_ceros = insertar_punto(sumo_ceros)
        num_final = sumo_ceros[5:]
        return print(num_final)
    else:
        if total_numeros % 3 == 1:
            sumo_ceros += "00" + numero
            sumo_ceros = insertar_punto(sumo_ceros)
            num_final = sumo_ceros[2:]
        return print(num_final)

#Ej.
print(inserta_punto_miles(1234567890))
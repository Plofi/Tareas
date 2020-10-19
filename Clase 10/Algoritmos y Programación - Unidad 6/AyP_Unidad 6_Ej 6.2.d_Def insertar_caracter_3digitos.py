"""
Ejercicio 6.2. Escribir funciones que dada una cadena y un caracter:
d) Inserte el caracter cada 3 dígitos en la cadena. Ej. '2552552550' y '.' debería devolver
'255.255.255.0'
Ejercicio 6.3. Modificar la función anterior, para que reciban un parámetro que indique la
cantidad máxima de reemplazos o inserciones a realizar.

"""

def insertar_caracter(cadena,caracter):
    """
    Inserta el caracter dado cada 3 dígitos en la cadena dada,
    con un máximo del resultado de la longitud de la cadena menos uno dividida por 3.

        Parameters:
                (str or int) Cadena de caracteres y/o números.
                ("") Cadena con el caracter a insertar.

        Returns:
                (str) Cadena resultante que se obtiene de insertar un caracter dado cada 3 dígitos.
                Con un máximo de repeticiones del multiplo de 3 en base a la longitud de la cadena.
    """
    cadena = str(cadena)
    
    cadena_final = ""
    p = 0 #posicion hasta la que selecciono dentro de la cadena inicial, para que copie los valores
    maximo = ((len(cadena)-1)//3) #para que no agregue puntos demás al final, saber cuantos debe tener como máximo
    
    for i in range(len(cadena)):
        cadena_final += cadena[p:p+3] #suma a lo que contiene la cadena entre los parémetros[i:j]
        if i == maximo:
            break
        else:
            cadena_final += caracter
            p += 3 #va aumentando de 3 en 3, para limitar el rango de arriba y agregar el punto luego
    return(cadena_final)

#Ej.
print(insertar_caracter("2552552550","."))
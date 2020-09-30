"""
Ej.4.5.b. Escribir una función que dado un mes y un año,
devuelva la cantidad de días correspondientes.

"""

def dias(m,a):
    """
    Devuelve la cantidad de días correspondientes a un mes y año/s previamente dados.

        Parameters:
                int (m,a) Mes y año ingresados como números enteros.
        
        Returns:
                (str) Cadena de texto que indica "La cantidad de (d) día/s es el equivalente al año y mes que ingresó".
                
    """
    assert isinstance(m,int), "Su mes debe ser ingresado en números enteros."
    assert isinstance(a,int), "Su año debe ser ingresado en números enteros."

    a = a * 365 + (a // 4) # Le sumo un día cada 4 años x bisiesto.
    a = a
    d_meses = [0,31,28,31,30,31,30,31,31,30,31,30,31] # Para que sea más exacto recorro la duración de los meses hasta el dado y sumo su cantidad de días.
    suma_meses = 0
    for i in range(1,m+1):
        i = d_meses[i] # i va a ir tomando el valor del array en la posición del mes.
        suma_meses = suma_meses + i
        m = suma_meses 
    
    d = a + m # días = años + meses convertidos
    return f"La cantidad de {d} día/s es el equivalente al año y mes que ingresó."

#Ej.
m = int(input("Ingrese la cantidad de meses que quiere pasar a días:"))
a = int(input("Ingrese la cantidad de años que quiere pasar a días:"))

print(dias(m,a))

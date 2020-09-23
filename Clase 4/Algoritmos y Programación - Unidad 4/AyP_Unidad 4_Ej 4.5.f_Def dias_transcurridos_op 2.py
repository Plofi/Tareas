"""
Ej.4.5.f. Escribir una función que dada una fecha,
indique la cantidad de días transcurridos en ese año hasta la fecha.

"""
def bisiesto(a):
    """
    Devuelve si un año es bisiesto.

        Parameters:
                (n) Año.
        
        Returns:
                (bool) Verdadero o falso.
    """

    if a % 4 == 0 and not a % 100 == 0 or a % 400 == 0:
        return True 
    else:
        return False  

def fecha(d,m,a):
    """
    Devuelve si una fecha es válida tras recibirla previamente como día, mes y año en forma numérica.

        Parameters:
                int (d,m,a) Día, mes y año (se toma como válido hasta el año 2020).
        
        Returns:
                (bool) Verdadero o Falso.
                
    """
    assert isinstance(d,int), "Su día/s debe ser un número entero."
    assert isinstance(m,int), "Su mes/es debe ser un número entero."
    assert isinstance(a,int), "Su año/s debe ser un número entero."

    ano = bisiesto(a)
    if ano == True and d >= 1 and d <= 31 and m >= 1 and m <=12 and a <= 2020:
        return True
        
    elif ano == False:
        if d >= 29 and m == 2:
            return False
        elif d >= 1 and d <= 31 and m >= 1 and m <=12 and a <= 2020: #Puse el año en curso pero podría ser mayor, ej. 10000
            return True
        else:
            return False
    
    else:  
        return False


def total_d_transcurridos(d,m,a):
    """
    Devuelve la cantidad de días trascurridos del año previamente dado hasta la fecha.

        Parameters:
                int (d,m,a) Día, mes y año.
        
        Returns:
                (str) Cadena de texto que indica "Han transcurrido (d) día/s desde que inició el año".
                
    """
    f_correcta = fecha(d,m,a)
    if f_correcta == True:
        d_meses = [0,31,28,31,30,31,30,31,31,30,31,30,31] 
        a = bisiesto(a)
        if a == True:
            d_meses[2]= 29
        suma_meses = 0
        d_desde_inicio_ano = 0
    
        for i in range(1,m): # Recorro la duración de los meses sin incluir al mes dado y sumo su cantidad de días.
            i = d_meses[i] # i va a ir tomando el valor del array de cada mes hasta el anterior al dado.
            suma_meses = suma_meses + i
            d_desde_inicio_ano = suma_meses
    
        total_d_transcurridos = d + d_desde_inicio_ano
        return f"Han transcurrido {total_d_transcurridos} día/s desde que inició el año."
    
    else:
        return "Fecha ingresada inválida."

#Ej.
d = int(input("Ingrese la cantidad de día/s de su fecha, le diremos cuantos días transcurrieron del año:"))
m = int(input("Ingrese la cantidad de meses de su fecha:"))
a = int(input("Ingrese la cantidad de años de su fecha:"))

print(total_d_transcurridos(d,m,a))
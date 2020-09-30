"""
Ej.4.5.g. Escribir una función que dadas dos fechas,
indique el tiempo transcurrido entre ambas, en días, meses y años.

"""
def bisiesto(a):
    """
    Devuelve si un año es bisiesto.

        Parameters:
                int (a) Año ingresado en números enteros.
        
        Returns:
                (bool) Indica si su año es bisiesto devolviendo: Verdadero o Falso. 
    """
    assert isinstance(a, int),"Su año debe ser ingresado en números enteros."

    if a % 4 == 0 and not a % 100 == 0 or a % 400 == 0:
        return True 
    else:
        return False  


def fecha(d,m,a):
    """
    Devuelve si una fecha es válida tras recibirla previamente como día, mes y año en forma numérica.

        Parameters:
                int (d,m,a) Día, mes y año ingresados en números enteros (se toma como válido hasta el año 2020).
        
        Returns:
                (bool) Verdadero o Falso de si su fecha es válida o no.
                
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

def dma_entre_fechas(d1,m1,a1,d2,m2,a2):
    """
    Devuelve la cantidad de días,meses y años que hay entre dos fechas.

        Parameters:
                int (d,m,a) Día, mes y año de dos fechas distintas entre sí, ingresadas en números enteros.
        
        Returns:
                (str) Cadena que indica que la cantidad de día/s, mes/es y año/s entre las fechas ingresadas.
                
    """
    assert isinstance(d1,int), "Su día/s debe ser un número entero."
    assert isinstance(m1,int), "Su mes/es debe ser un número entero."
    assert isinstance(a1,int), "Su año/s debe ser un número entero."
    assert isinstance(d2,int), "Su día/s debe ser un número entero."
    assert isinstance(m2,int), "Su mes/es debe ser un número entero."
    assert isinstance(a2,int), "Su año/s debe ser un número entero."
    
    f_valida1 = fecha(d1,m1,a1)
    f_valida2 = fecha(d2,m2,a2)
    if f_valida1 and f_valida2 == True:
        if a2 >= a1:
            total_anos = a2 - a1
        else:
            total_anos = a1 - a2

        if m2 >= m1:
            total_meses = m2 - m1
        else:    
            total_meses = m1 - m2
    
        if d2 >= d1:
            total_dias = d2 - d1
        else:    
            total_dias = d1 - d2
    
    return f"La cantidad de días entre sus fechas ingresadas es: {total_dias} día/s, de {total_meses} mes/es y {total_anos} año/s es."  


#Ej.
d1 = int(input("Ingrese la cantidad de día/s de su fecha 1, le diremos cuantos días hay entre ambas fechas:"))
m1 = int(input("Ingrese la cantidad de mes/es de su fecha 1:"))
a1 = int(input("Ingrese la cantidad de años de su fecha 1:"))
d2 = int(input("Ingrese la cantidad de día/s de su fecha 2:"))
m2 = int(input("Ingrese la cantidad de mes/es de su fecha 2:"))
a2 = int(input("Ingrese la cantidad de años de su fecha 2:"))

print(dma_entre_fechas(d1,m1,a1,d2,m2,a2))


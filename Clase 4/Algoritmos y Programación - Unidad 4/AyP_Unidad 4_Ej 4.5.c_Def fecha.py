"""
Ej.4.5.c. Escribir una función que dada una fecha (día, mes,año),
indica si es válida o no.

"""
def bisiesto(n):
    """
    Devuelve si un año es bisiesto.

        Parameters:
                (n) Año.
        
        Returns:
                (bool) Verdadero o Falso.
    """

    if n % 4 == 0 and not n % 100 == 0 or n % 400 == 0:
        return True
    else:
        return False  


def fecha(d,m,a):
    """
    Devuelve si una fecha es válida tras recibirla previamente como día, mes y año en forma numérica.

        Parameters:
                int (d,m,a) Día, mes y año (se toma como válido hasta el año 2020).
        
        Returns:
                (str) Cadena de texto que indica "Su fecha (d,m,a) es válida o inválida".
                
    """
    assert isinstance(d,int), "Su día/s debe ser un número entero."
    assert isinstance(m,int), "Su mes/es debe ser un número entero."
    assert isinstance(a,int), "Su año/s debe ser un número entero."

    ano = bisiesto(a)
    if ano == True and d >= 1 and d <= 31 and m >= 1 and m <=12 and a <= 2020:
        return f"Su fecha {d,m,a} es válida."
        
    elif ano == False:
        if d >= 29 and m == 2:
            return f"Su fecha {d,m,a} es inválida."
        elif d >= 1 and d <= 31 and m >= 1 and m <=12 and a <= 2020: #Puse el año en curso pero podría ser mayor, ej. 10000
            return f"Su fecha {d,m,a} es válida."
        else:
            return f"Su fecha {d,m,a} es inválida."
    
    else:  
        return f"Su fecha {d,m,a} es inválida."

#Ej:
print(fecha(29,2,2020))

"""
Ej. 4.8 - Programa de astrología: el usuario debe ingresar el día y mes de su cumpleaños
y el programa le debe decir a qué signo corresponde. 
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

def signos(d,m,a):
    """
        Devuelve el signo del zodíaco al que perteneces al ingresar una fecha de cumpleaños en números(día, mes y año).

            Parameters:
                    (int) Día, mes y año de nacimiento, ingresada en números enteros.

            Returns: 
                    (str) El nombre del signo candrespondiente a la fecha ingresada.

    """
    assert isinstance(d,int),"Su día ingresado no es un número entero."
    assert isinstance(m,int),"Su mes ingresado no es un número entero."
    assert isinstance(a,int),"Su año ingresado no es un número entero."
    
    f_ingresada = fecha(d,m,a)
    if f_ingresada == True:
        if d >= 21 and m == 3 or d <= 20 and m == 4:
            return "Aries"
        elif d >= 21 and m == 4 or d <= 20 and m == 5:
            return "Tauro"
        elif d >= 21 and m == 5 or d <= 21 and m == 6:
            return "Géminis"
        elif d >= 22 and m == 6 or d <= 23 and m == 7:
            return "Cáncer"
        elif d >= 24 and m == 7 or d == 23 and m == 8:
            return "Leo"
        elif d >= 24 and m == 8 or d <= 23 and m == 9:
            return "Virgo"
        elif d >= 24 and m == 9 or d <= 22 and m == 10:
            return "Libra"
        elif d >= 23 and m == 10 or d <= 22 and m == 11:
            return "Escorpio"
        elif d >= 23 and m == 11 or d <= 21 and m == 12:
            return "Sagitario"
        elif d >= 22 and m == 12 or d <= 20 and m == 1:
            return "Capricornio"
        elif d >= 21 and m == 1 or d <= 19 and m == 2:
            return "Acuario"
        elif d >= 20 and m == 2 or d <= 20 and m == 3:
            return "Piscis"
        
    else:
        return "ERROR: Fecha inválida o ingrese los datos con números."

#Ej.
d = int(input("Ingrese la el día de su cumpleaños(en números):"))
m = int(input("Ingrese el mes de su cumpleaños (en números):"))
a = int(input("Ingrese el año de su cumpleaños (en números), le diremos su signo:"))

print("Su signo es:",(signos(d,m,a)))
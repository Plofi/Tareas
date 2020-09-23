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

def d_ano(a):
        """
        Devuelve la cantidad de días de un año bisiesto o no.
            
            Parameters:
                    int (a) Año.
        
            Returns:
                    (int) La cantiad de días de un año bisiesto o no.
            
        """
        a_bisiesto = bisiesto(a) # Llama a esa función.
        if a_bisiesto == True:
            return 366
        else:
            return 365

def d_fin_mes(d,m,a):
    """
    Devuelve la cantidad de días que falan hasta fin de mes, partiendo de una fecha previamente dada.

        Parameters:
                int (d,m,a) Días, mes y año.
        
        Returns:
                (int) Cantidad de días que faltan hasta fin de mes.
                
    """
    def feb (a):
        """
        Devuelve la cantidad de días que tiene Febrero, dependiendo de si el año es o no bisiesto.
            
            Parameters:
                    int (a) Año.
        
            Returns:
                    int (feb) La cantiad de días que tiene Febrero en ese año.
                
        """
        a_bisiesto = bisiesto(a) # Llama a esa función.
        if a_bisiesto == True:
            feb = 29
            return feb
        else:
            feb = 28
            return feb
    
    m_31d = [1,3,5,7,8,10,12] # Meses con 31 días.
    m_30d = [4,6,9,11] # Meses con 30 días. 
    feb = feb(a) # Varia si es bisiesto, llama a esa función.

    for i in range(len(m_31d)):
        i = m_31d[i] # i adopta el valor del array para compararlo luego con el mes dado.
        if i == m:
            d_restantes = 31 - d
            return d_restantes
    for i in range(len(m_30d)):
        i = m_30d[i]
        if i == m:
            d_restantes = 30 - d
            return d_restantes
    else:
        d_restantes = feb - d #Llamo a febero que va a ser 28 o 29 según sea o no bisiesto.
        return d_restantes

def d_fin_ano(m):
        """
        Devuelve la cantidad de días que faltan para terminar el año (sin tener en cuenta los días de ese mes ni si el año es bisiesto).

            Parameters:
                    int (m) Mes.
        
            Returns:
                    Cantidad de días de los meses restantes para terminar el año, no toma en cuenta los días del mes ingresado o el año bisiesto.
                
        """
        d_meses = [0,31,28,31,30,31,30,31,31,30,31,30,31] 
        suma_meses = 0
        for i in range(m+1,13): # Recorro la duración de los meses a partir del siguiente al mes dado y sumo su cantidad de días.
            i = d_meses[i] # i va a ir tomando el valor del array desde la posición del mes siguiente al dado.
            suma_meses = suma_meses + i
            d_hasta_fin_ano = suma_meses
        return d_hasta_fin_ano

def total_d_transcurridos(d,m,a):
    """
    Devuelve la cantidad de días trascurridos del año previamente dado hasta la fecha.

        Parameters:
                int (d,m,a) Día, mes y año.
        
        Returns:
                (str) Cadena de texto que indica "Han transcurrido (d) día/s desde que inició el año".
                
    """
    f_correcta = fecha(d,m,a) # Corroboro que la fecha ingresada sea válida.
    if f_correcta == True:
        ano = d_ano(a) # Llamo a esta función para tener la cantidad de días total del año ingresado.
        d_hasta_fin_mes = d_fin_mes(d,m,a) # Llamo a esta función para calcular los días que faltan del mes dado.
        d_hasta_fin_ano = d_fin_ano(m) # Llamo a esta función para saber cuantos días faltan de los meses restantes.
        total_d_transcurridos = ano - (d_hasta_fin_mes + d_hasta_fin_ano)  
        return f"Han transcurrido {total_d_transcurridos} día/s desde que inició el año."
    else:
        return "Su fecha es inválida."

#Ej.
d = int(input("Ingrese la cantidad de día/s de su fecha, le diremos cuantos días transcurrieron del año:"))
m = int(input("Ingrese la cantidad de meses de su fecha:"))
a = int(input("Ingrese la cantidad de años de su fecha:"))

print(total_d_transcurridos(d,m,a))
"""
Ej.4.5.h. Escribir una función que dadas dos fechas,
indique la cantidad de día/s transcurridos entre ambas.

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


def total_d_transcurridos(d,m,a):
    """
    Devuelve la cantidad de días trascurridos del año previamente dado hasta la fecha.

        Parameters:
                int (d,m,a) Día, mes y año ingresados en números enteros.
        
        Returns:
                (int) Total de día/s transcurridos desde que inició el año expresado en números enteros.
                
    """
    assert isinstance(d,int), "Su día/s debe ser un número entero."
    assert isinstance(m,int), "Su mes/es debe ser un número entero."
    assert isinstance(a,int), "Su año/s debe ser un número entero."
    
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
        return total_d_transcurridos
    else:
        return "Fecha ingresada inválida."


def d_fin_mes(d,m,a):
    """
    Devuelve la cantidad de días que falan hasta fin de mes, partiendo de una fecha previamente dada.

        Parameters:
                int (d,m,a) Días, mes y año ingresado en números enteros.
        
        Returns:
                (int) Cantidad de días que faltan hasta fin de mes.
                
    """
    def feb (a):
        """
        Devuelve la cantidad de días que tiene Febrero, dependiendo de si el año es o no bisiesto.
            
            Parameters:
                    int (a) Año ingresados en números enteros.
        
            Returns:
                    int (feb) La cantiad de días que tiene Febrero en ese año.
                
        """
        assert isinstance(a, int),"Su año debe ser ingresado en números enteros."

        a_bisiesto = bisiesto(a) # Llama a esa función.
        if a_bisiesto == True:
            feb = 29
            return feb
        else:
            feb = 28
            return feb

    assert isinstance(d,int), "Su día/s debe ser ingresado en números enteros."
    assert isinstance(m,int), "Su mes/es debe ser ingresado en números enteros."
    assert isinstance(a,int), "Su año/s debe ser ingresado en números enteros."

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
        d_restantes = feb - d #Llamo a febrero que va a ser 28 o 29 según sea o no bisiesto.
        return d_restantes


def d_fin_ano(m):
        """
        Devuelve la cantidad de días que faltan para terminar el año (sin tener en cuenta los días de ese mes ni si el año es bisiesto).

            Parameters:
                    int (m) Mes ingresado en números enteros.
        
            Returns:
                    (int) Cantidad de días de los meses restantes para terminar el año, no toma en cuenta los días del mes ingresado o el año bisiesto.
                
        """
        assert isinstance(m,int), "Su mes/es debe ser ingresado en números enteros."

        d_meses = [0,31,28,31,30,31,30,31,31,30,31,30,31] # Recorro la duración de los meses a partir del siguiente el dado y sumo su cantidad de días.
        suma_meses = 0
        for i in range(m+1,13):
            i = d_meses[i] # i va a ir tomando el valor del array desde la posición del mes siguiente al dado.
            suma_meses = suma_meses + i
            d_hasta_fin_ano = suma_meses
        return d_hasta_fin_ano


def total_d_fin_ano(d,m,a):
    """
    Devuelve la cantidad de días que faltan para terminar el año previamente dado.

        Parameters:
                int (d,m,a) Día, mes y año ingresados en números enteros.
        
        Returns:
                (str) Cadena de texto que indica "Faltan (d) día/s para terminar el año que ingresó".
                
    """
    assert isinstance(d,int), "Su día/s debe ser ingresado en números enteros."
    assert isinstance(m,int), "Su mes/es debe ser ingresado en números enteros."
    assert isinstance(a,int), "Su año/s debe ser ingresado en números enteros."

    f_correcta = fecha(d,m,a) # Chequeo que ingresen una fecha correcta, llamando a la función.
    if f_correcta == True:
        d_hasta_fin_mes = d_fin_mes(d,m,a) # Llamo a esta función para calcular los días que faltan del mes dado.
        d_hasta_fin_ano = d_fin_ano(m) # Llamo a esta función para saber cuantos días falta de los meses restantes.
        total_d_fin_ano = d_hasta_fin_mes + d_hasta_fin_ano 
        return f"Faltan {total_d_fin_ano} día/s para terminar el año que ingresó."
    else:
        return "Su fecha es inválida."


def d_entre_fechas(d1,m1,a1,d2,m2,a2):
    """
    Devuelve la cantidad de días que hay entre dos fechas.

        Parameters:
                int (d,m,a) Día, mes y año de dos fechas distintas entre sí, ingresadas en números enteros.
        
        Returns:
                (str) Cadena que indica que la cantidad de día/s equivalentes entre sus fechas ingresadas.
                
    """
    assert isinstance(d1,int), "Su día/s debe ser un número entero."
    assert isinstance(m1,int), "Su mes/es debe ser un número entero."
    assert isinstance(a1,int), "Su año/s debe ser un número entero."
    assert isinstance(d2,int), "Su día/s debe ser un número entero."
    assert isinstance(m2,int), "Su mes/es debe ser un número entero."
    assert isinstance(a2,int), "Su año/s debe ser un número entero."
        
    if a1 == a2:
        if m1 == m2:
            d_entre_f = d2 - d1
            return f"La cantidad de días entre sus fechas ingresadas es equivalente a:{d_entre_f} día/s"
        
        elif m2 >= m1:
            d_m1 = total_d_transcurridos(d1,m1,a1)
            d_m2 = total_d_transcurridos(d2,m2,a2)
            d_entre_f = d_m2 - d_m1 
        else:
            if m1 >= m2:
                d_m1 = total_d_transcurridos(d1,m1,a1)
                d_m2 = total_d_transcurridos(d2,m2,a2)
                d_entre_f = d_m1 - d_m2
        return f"La cantidad de días entre sus fechas ingresadas es equivalente a:{d_entre_f} día/s"     
       
    elif a2 > a1:
        a2 = total_d_transcurridos(d2,m2,a2)
        a1 = total_d_fin_ano (d1,m1,a1)
        d_entre_f = a1 + a2
        return f"La cantidad de días entre sus fechas ingresadas es equivalente a:{d_entre_f} día/s"  

    elif a1 > a2:
        a1 = total_d_transcurridos(d1,m1,a1)
        a2 = total_d_fin_ano (d2,m2,a2)
        d_entre_f = a1 + a2
        return f"La cantidad de días entre sus fechas ingresadas es equivalente a:{d_entre_f} día/s"

    else:
        return "Sus fechas son inválidas."

#Ej.
d1 = int(input("Ingrese la cantidad de día/s de su fecha 1, le diremos cuantos días hay entre ambas fechas:"))
m1 = int(input("Ingrese la cantidad de mes/es de su fecha 1:"))
a1 = int(input("Ingrese la cantidad de años de su fecha 1:"))
d2 = int(input("Ingrese la cantidad de día/s de su fecha 2:"))
m2 = int(input("Ingrese la cantidad de mes/es de su fecha 2:"))
a2 = int(input("Ingrese la cantidad de años de su fecha 2:"))

print(d_entre_fechas(d1,m1,a1,d2,m2,a2))


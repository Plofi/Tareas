"""
Ej.4.5.d. Escribir una función que dada una fecha,
indique los días que faltan hasta fin de mes.

"""
def bisiesto(a):
    """
    Devuelve si un año es bisiesto.

        Parameters:
                int (n) Año.
        
        Returns:
                (bool) Verdadero o falso.
    """

    if a % 4 == 0 and not a % 100 == 0 or a % 400 == 0:
        return True 
    else:
        return False  


def d_fin_mes(d,m,a):
    """
    Devuelve la cantidad de días que falan hasta fin de mes, partiendo de una fecha previamente dada.

        Parameters:
                int (d,m,a) Días, mes y año.
        
        Returns:
                (str) Cadena de texto que indica "Faltan (d) día/s para llegar a fin de mes." 
                
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
            return f"Faltan {d_restantes} día/s para llegar al fin de mes que ingresó."
    for i in range(len(m_30d)):
        i = m_30d[i]
        if i == m:
            d_restantes = 30 - d
            return f"Faltan {d_restantes} día/s para llegar al fin de mes que ingresó."
    else:
        d_restantes = feb - d #Llamo a febero que va a ser 28 o 29 según sea o no bisiesto.
        return f"Faltan {d_restantes} día/s para llegar al fin de mes que ingresó."
    
    
#Ej.

d = int(input("Ingrese la cantidad de día/s de su fecha, le diremos cuantos días faltan para fin de mes:"))
m = int(input("Ingrese la cantidad de meses de su fecha:"))
a = int(input("Ingrese la cantidad de años de su fecha:"))

print(d_fin_mes(d,m,a))

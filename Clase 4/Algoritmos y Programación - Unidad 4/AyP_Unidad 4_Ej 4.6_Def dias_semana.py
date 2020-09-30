"""
Ej.4.6 - Suponiendo que el primer día del año fue lunes, 
escribir una función que reciba un número con el día del año (de 1 a 366) 
y devuelva el día de la semana que le toca. Por ejemplo: si recibe '3' debe devolver 'miércoles', 
si recibe '9' debe devolver 'martes'.

"""

def d_semana(d):
    """
        Devuelve el nombre del día de la semana equivalente al número de día ingresado."
            
            Parameters:
                    int(d) Número de día (entre 1 y 366), ingresado en números enteros.
                    Inicia en Lunes como día equivalente a 1.
                    
            Return:
                    (str) "Su día corresponde a: Nombre del día equivalente al número de día ingresado".

    """
    assert isinstance (d,int), "Sus días deben ingresarse en números enteros."
    assert d >= 1 and d <= 366, "Su número de día ingresado, debe estar entre 1 y 366."
    
    d_semana = (0,"Lunes","Martes","Miércoles","Jueves","Viernes","Sábado", "Domingo")
    
    d = d % 7 # Divido los días por la cantidad de semanas y me quedo con su resto
    if d == 0: # Si el resto da cero va a corresponder a Domingo por eso convierto su valor a 7.
        d = 7
    i = d # i = posición tupla
    return f"Su día corresponde a un {d_semana[i]}."

# Ej.
d = int(input("Ingrese el día del año, le diremos a que día de la semana corresponde:"))

print(d_semana(d))
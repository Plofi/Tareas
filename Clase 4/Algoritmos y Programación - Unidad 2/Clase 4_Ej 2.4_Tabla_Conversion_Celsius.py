F = None #Grados Fahrenheit

def conversion_Celsius(F):
    conversion_Celsius = (F-32)*5/9
    return conversion_Celsius

for t in range(0,130,+10): # t = temperatura en la tabla
    F = t
    print(t, "°F expresado en Celsius es igual a:",conversion_Celsius(F))
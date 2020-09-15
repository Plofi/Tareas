# Ej. 3.1.b. Escribir una función que calcule la duración en hs, min y seg de un intervalo dado en segundos:
#En programa sería:

def calculo_hms (s):
    h = 0
    m = 0
    while s>=3600:
        hora = s-3600
        s = hora
        h = h+1
    else: 
        while s>=60:
            minutos = s-60
            s = minutos
            m = m+1
    return (f"son: {h} hora/s, {m} minutos, {s} segundo/s.")

s = int(input("Ingrese el intervalo en segundos, le diremos cuantas hs,min y seg son:"))

print("Su intervalo de", s, "segundos,", calculo_hms(s))

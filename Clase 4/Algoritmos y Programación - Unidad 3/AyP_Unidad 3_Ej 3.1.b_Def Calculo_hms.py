# Ej. 3.1.b. Escribir una función que calcule la duración en hs, min y seg de un intervalo dado en segundos:
#En programa sería:

def calculo_hms(segundos):
    h = 0
    m = 0
    while segundos>=3600:
        hora = segundos -3600
        segundos = hora
        h = h+1
       
        while segundos>=60:
            minutos = segundos-60
            segundos = minutos
            m = m+1
        return (h,":", m,":",segundos)

calculo_hms(segundos)

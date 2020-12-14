#Escribir un programa que pida al usuario 2 intervalos en (h,m,s),
# sume sus duraciones y muestre el resultado en h,m,s

#@OscarVasta : este programa funciona correctamente

def calculo_seg(h,m,s):
    return (h*3600+m*60+s)


def calculo_hms(s):
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
    s = int(s)
    return ((print("La suma de sus intervalos expresados en horas, minutos y segundos es:",h,":",m,":",s)))

h1=int(input("Introduzca la hora del intervalo 1:"))
m1=int(input("Introduzca los minutos del intervalo 1:"))
s1=int(input("Introduzca los segundos del intervalo 1:"))

h2=int(input("Introduzca la hora del intervalo 2:"))
m2=int(input("Introduzca los minutos del intervalo 2:"))
s2=int(input("Introduzca los segundos del intervalo 2:"))

intervalo1 = calculo_seg(h1,m1,s1)
intervalo2 = calculo_seg(h2,m2,s2)
suma_intervalos = int(intervalo1+intervalo2)#Esta línea tal vez se podría obviar y sumar directamente abajo
print(calculo_hms(suma_intervalos))

# Ej.3.1.a = Escribir una función que permita calcular la duración en segundos de un intervalo dado en hs,min y seg.
# En programa sería:

def calculo_seg(h,m,s):
    return h * 3600 + m * 60 + s

h= int(input("Ingrese la hora:")) 
m= int(input("Ingrese los minutos:")) 
s= int(input("E ingrese los segundos del intervalo:")) 

print("Le devolveremos la duración de su intervalo en segundos, es:", calculo_seg(h,m,s))
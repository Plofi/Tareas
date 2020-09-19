"""
Oscar_Vasta-Guia_Ejercicios_7.1.py
Ejercicio 7.1. Escribir una función que reciba una tupla de elementos e indique si se encuentran
ordenados de menor a mayor o no.
"""
# - definicion de funcion --------------------
def ordesor3(listaor3):
    rorden = 0
    control = 0
    sigueordenado = 0
    for i in range(0,len(listaor3),3):
        control +=1
        if listaor3[i]>rorden:
            sigueordenado += 1
        rorden=listaor3[i]
    if sigueordenado == control:
        return 'ordenadas'
    else:
        return 'desordenadas'
# ---------------------------------------------------
# - programa de prueba
herramientas=(2,'alicate',True,1,'martillo',False,3,'sierra',True,4,'cuter',True,5,'destornillador phillips',True)
for i in range(0,len(herramientas),3):
    print(herramientas[i],'|',herramientas[i+1],'|',herramientas[i+2])
print('** ',ordesor3(herramientas),' ** ')
# E.O.F.

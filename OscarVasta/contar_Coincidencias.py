"""
Escribir una función que reciba una lista desordenada y un elemento, que:
a) Busque todos los elementos coincidan con el pasado por parámetro y devuelva la cantidad
de coincidencias encontradas.

version original:

def contar_Coincidencias(listax,elementox)
for i in range(0,len(listax)+1):
    if listax(i)=elementox:
      cont_coinc+=1
return cont_coinc
------------------------------------------------------------------
para que funcione es necesario que:
    1º las instrucciones por debajo del def() deben estar indentadas
    2º antes de usar cont_coinc se debe definir la variable dentro del area local
version corregida:
"""
def contar_Coincidencias(listax,elementox)
    cont_coinc=0
    for i in range(0,len(listax)+1):
        if listax(i)=elementox:
            cont_coinc+=1
    return cont_coinc
"""
Oscar Vasta
"""

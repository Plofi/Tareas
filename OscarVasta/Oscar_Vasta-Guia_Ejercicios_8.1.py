"""
Oscar_Vasta-Guia_Ejercicios_8.1
Escribir una función que reciba una lista desordenada y un elemento, que:
a) Busque todos los elementos coincidan con el pasado por parámetro y devuelva la can-
tidad de coincidencias encontradas.
b) Busque la primera coincidencia del elemento en la lista y devuelva su posición.
c) Utilizando la función anterior, busque todos los elementos que coincidan con el pasado
por parámetro y devuelva una lista con las posiciones.
"""
#-- a)
def cuentaocur(a,buscado):
    contar=a.count(buscado)
    return contar
posit=list()
# -- b)
def donde1(a,buscado):
    encontrado=a.index('Terrero',0)
    return encontrado
# -- c)
def dondeocur(a,buscado):
    posit=list()
    encontrado=0
    apartir=0
    rango=a.count(buscado)
    for i in range(0,rango):
        encontrado=a.index('Terrero',apartir,len(a))
        posit.append(encontrado)
        apartir=encontrado+1
    return posit
# -- programa de prueba
listado=('Terrero','borgoña','aresenico','plomo','Ernesto','Terrero','Fererico','Loperfido')
print('     *** Ejercicio_8.1 - busquedas ***')
print()
print('_ a) Cantidad de ocurrencias de la palabra <Terrero> : ',cuentaocur(listado,'Terrero'))
print()
print('_ b) Posicion de la 1º ocurrencia de la palabra <Terrero> : ',donde1(listado,'Terrero'))
print()
print('_ c) Posiciones de todas las ocurrencias de la palabra <Terrero> : ',dondeocur(listado,'Terrero'))
print('_'*80)
# E.O.F.

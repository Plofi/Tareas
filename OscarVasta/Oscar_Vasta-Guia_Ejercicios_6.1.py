"""
Oscar_Vasta-Guia_Ejercicios_6.1.py
Ejercicio 6.1. Escribir funciones que dada una cadena de caracteres:
a) Imprima los dos primeros caracteres.
b) Imprima los tres últimos caracteres.
c) Imprima dicha cadena cada dos caracteres. Ej.: 'recta' debería imprimir 'rca'
d) Dicha cadena en sentido inverso. Ej.: 'hola mundo!' debe imprimir '!odnum aloh'
e) Imprima la cadena en un sentido y en sentido inverso. Ej: 'reflejo' imprime
'reflejoojelfer'.
"""
cadena=""
#- definiciones de funciones -#
def dp(ca):
    return ca[:2]
def tu(ca):
    return ca[(len(ca)-3):]
def cada2(ca):
    ca2=""
    for i in range(0,(len(ca)-1),2):
        ca2 += ca[i]
    return ca2
def rcada2(ca):
    rca2=""
    for i in range((len(ca)-2),-2,-2):
        rca2+=ca[i]
    return rca2
def espejo(ca):
    rca=""
    for i in range((len(ca)-1),-1,-1):
        rca+=ca[i]
    return ca+rca
#- programa - #
cadena = input("ingrese cadena de caracteres :")
print('los 2 primeros caracteres son : ',dp(cadena))
print('los 3 ultimos caracteres son : ',tu(cadena))
print('la cadena salteando 1 caracter de por medio es : ',cada2(cadena))
print('la reversa de la cadena salteando 1 caracter de por medio es : ',rcada2(cadena))
print('la cadena mas el reflejo de si misma es :', espejo(cadena))
# EOF #

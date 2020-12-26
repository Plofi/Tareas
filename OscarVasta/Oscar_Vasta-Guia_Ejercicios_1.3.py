# Oscar Vasta Guia de Ejercicios 1.3 
# UN PROGRAMA QUE HACE VARIOS CALCULOS GEOMÉTRICOS MEDIANTE EL USO DE FUNCIONES
def rectdim(b, a):
    perec = (abs(b) * 2) + (abs(a) * 2)
    suprec = (abs(a) * abs(b))
    return perec, suprec
""" lo de los valores absolutos es por que seria muy facil ingrasar valores negativos, 
    sobre todo por que los puntos de los ejes podrian estan en los cuadrantes 2, 3 o 4 
    pero los perímetros y las superficies siempre son magnitudes positivas """
def receje(u, v, w, x):
    ejeab = abs(v - u)
    ejeor = abs(x - w)
    perec = (ejeab * 2) + (ejeor * 2)
    suprec = ejeab * ejeor
    return perec, suprec
# carga el valor del numero pi en la variable pi desde la libreria math
from math import pi 
def circulo(s):
    circun= abs(s) * pi
    supcir= pi * (abs(s)**2)
    return circun, supcir
def esfera(s):
    volesf= 3/4 * (abs(s)**3) * pi
    return volesf
def hipotenusa(ady,opu):
    hipo = (( abs(ady)**2 ) + ( abs(opu)**2 )) **0.5
    return hipo
print('_'*105)
print()
print(' a y b) calcula el perimetro y superficie de un rectangulo en base a dimensiones base y altura :')
print('( Nota: si ingresa valores decimales use punto < . > decimal ) ' )
print()
xx = input("ingrese base del rectangulo [m] : ")
x=float(xx)
yy = input("ingrese altura del rectángulo [m] : ")
y=float(yy)
print()
print('El perímetro y la superficie del rectángulo son : ', rectdim(x,y), '[m] y [m2] respectivamente')
print()
print('_'*105)
print()
print(' c) Calcula el perimetro y superficie de un rectangulo en base a los puntos inicial') 
print('     y final del eje de absisas y los puntos inicial y final del eje de ordenadas :')
print()
x1 = float(input("ingrese el punto x1 (o punto inicial del eje de absisas)   [cm]: "))
x2 = float(input("ingrese el punto x2 (o punto final del eje de absisas)     [cm]: "))
y1 = float(input("ingrese el punto y1 (o punto inicial del eje de ordenadas) [cm]: "))
y2 = float(input("ingrese el punto y2 (o punto final del eje de ordenadas)   [cm]: "))
print()
print('El perímetro y la superficie del rectángulo son : ', receje(x1,x2,y1,y2), ' [cm] y [cm2] respectivamente')
print()
print('_'*105)
print(' d y e ) Calcula la circunferencia y la superfície de un círculo en base a su radio : ') 
print()
radio = float(input("ingrese el radio del círculo en [km]: "))
print()
print('La circunferencia y la superficie del círculo son : ', circulo(radio), ' [km] y [km2] respectivamente')
print()
print('_'*105)
print(' f ) Calcula el volumen de una esfera en base a su radio : ') 
print()
radio = float(input("ingrese el radio de la esfera en [cm]: "))
print()
print('El volumen de la esfera es de  : ', esfera(radio), ' [miliLitros]')
print()
print('_'*105)
print(' g ) Calcula la hipotenusa de un triángulo en base a sus catetos : ') 
print()
adyacente = float(input("ingrese la longitud del cateto adyacente [m]: "))
opuesto  = float(input("ingrese la longitud del cateto opuesto [m]: "))
print()
print('El la hipotenusa del triángulo mide : ', hipotenusa(adyacente, opuesto),' [m]')
print()
print('_'*105)
# - END OF FILE -






"""
Oscar_Vasta-Guia_Ejercicios_7.2.py
Dominó :
a) Escribir una función que indique si dos fichas de dominó encajan o no. Las fichas son
recibidas en dos tuplas, por ejemplo: (3,4) y (5,4)
b) Escribir una función que indique si dos fichas de dominó encajan o no. Las fichas son
recibidas en una cadena, por ejemplo: 3-4 2-5. Nota: utilizar la función split de las
cadenas.
"""
# - definicion de funcion a)--------------------
def domino_a(ficha1,ficha2):
    coinciden = 0
    for i1 in ficha1:
        for i2 in ficha2:
            print(i1,'-',i2, end=' ; ')
            if i1 == i2:
                coinciden = 1
    if coinciden == 1 :
        return "encajan"
    else:
        return "no encajan"
# - definicion de funcion b)--------------------
def domino_b(fichas):
    fichasg1=()
    fichasg2=()
   
    fichase=fichas.split(' ')
    fichasg1=fichase[0].split('-')
    fichasg2=fichase[1].split('-')
    coinciden=0
    for i1 in fichasg1:
        for i2 in fichasg2:
            print(i1,'-',i2, end=' ; ')
            if i1 == i2:
                coinciden = 1
    if coinciden == 1 :
        return "encajan"
    else:
        return "no encajan"
# ---------------------------------------------------
# - programa de prueba
fic1=(3,4)
fic2=(5,4)
print('** ',domino_a(fic1,fic2),' ** ')
ficsplit='3-4 2-5'
print('## ',domino_b(ficsplit),' ##')
# E.O.F.

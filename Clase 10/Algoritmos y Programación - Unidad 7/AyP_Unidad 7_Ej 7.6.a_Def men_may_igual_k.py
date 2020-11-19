"""
Ejercicio 7.6. Dada una lista de números enteros y un entero k, 
escribir una función que:
a) Devuelva tres listas, una con los menores, otra con los mayores 
y otra con los iguales a k.

"""
def menores(lista_num,k):
    lista_menores = []
    for i in lista_num:
        if i < k:
            lista_menores.append(i)
    return lista_menores

def mayores(lista_num,k):
    lista_mayores = []
    for i in lista_num:
        if i > k:
            lista_mayores.append(i)
    return lista_mayores

def iguales(lista_num,k):
    lista_iguales = []
    for i in lista_num:
        if i == k:
            lista_iguales.append(i)
    return lista_iguales

def men_may_igual_k(lista_num,k):
    """
    Dada una lista de números enteros y un entero k; devuelva una tupla con tres listas, 
    una con los menores, otra con los mayores y otra con los iguales a k.

        Parameters:
                (list,int) Recibe una lista de numeros enteros y un número para comparalo.

        Returns: 
                (tuple,list) Devuelve una tupla con 3 listas: una con los menores, 
                otra con los mayores y otra con los iguales a k.

    """
    return menores(lista_num,k), mayores(lista_num,k), iguales(lista_num,k)


#Ej. 
menores, mayores, iguales = men_may_igual_k([6,8,7,5,3,6,4],6)
print(menores, mayores, iguales)
print(menores)
print(mayores)
print(iguales)
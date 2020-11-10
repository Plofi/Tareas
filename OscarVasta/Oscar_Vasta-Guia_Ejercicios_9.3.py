# --  Oscar Vasta -- Curso Python -- Guia de ejercicios -- Ejercicio 9.3--- #
"""
Escribir un programa que vaya solicitando al usuario que ingrese nombres.
a) Si el nombre se encuentra en la agenda (implementada con un diccionario), debe mostrar
el teléfono y, opcionalmente, permitir modificarlo si no es correcto.
b) Si el nombre no se encuentra, debe permitir ingresar el teléfono correspondiente.
El usuario puede utilizar la cadena ”*”, para salir del programa.
"""
#
# a)_______________________________________

salida=''
nombreºTe={}
while salida != '*':
    nombre=input("ingrese el nombre del que desea el teléfono : ")
    if nombre in nombreºTe:
        print('Te : ',nombreºTe[nombre])
        edita=input('desea modificarlo [S/N] ?')
        if edita.lower()=='s':
            nombreºTe[nombre]=input('Ingrese el nuevo Te : ')
    else:
        agrega=input('Desea agregar este nombre a la lista con su Te [S/N] ?')
        if agrega.lower()=='s':
            nombreºTe[nombre]=input('Ingrese el Te de ese nombre : ')
    salida=input('Desea continuar ? [ * ] para salir o cualquier otra letra para continuar')

#-------------------- E.O.F. -----------------------------

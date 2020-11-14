
"""
Oscar Vasta

Ejercicio 11.2. Escribir una función, llamada cp, que copie todo el contenido de un archivo (sea
de texto o binario) a otro, de modo que quede exactamente igual.
Nota: utilizar archivo.read(bytes) para leer como máximo una cantidad de bytes.
"""
dirname=''
import os
directorio=os.path.dirname(__file__)
archivoI="Principios_Python.txt"
archivoO="Zen_de_Python.txt"
with open(os.path.join(directorio, archivoO),'w', encoding='UTF-8') as o:
    with open(os.path.join(directorio, archivoI),'r', encoding='UTF-8') as i:
        for l in i.readlines():
            print (l, end='')
            o.writelines(l)
#filename_salida="Zen_de_Python.txt"
#linea=" "

#    for linea in f:
#        print(linea, end=" ")

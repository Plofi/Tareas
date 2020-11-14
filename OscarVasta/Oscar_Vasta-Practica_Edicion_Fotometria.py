
"""
Oscar Vasta

Ejercicio de practica que le un archivo .IES y lo vuelca a otro con la mitad de la irradiacion luminica pero manteniendo la misma distriucion fotometrica y cambia tamien la cantidad de placas de 4 a 2 en el encabezado del archivo.
"""
dirname = ''
record = list()
orecord = list()
nuevovalor=float()
import os # Carga los parametros del sistema operativo en ue este corriendo
directorio = os.path.dirname(__file__)
import csv # Carga el conjunto e herramientas de manejo de archivos con campos separados por comas
nrecord = 0
listo =''
"""
funcion que controla que el nombre de archivo se encuentre presente en el
diretorio conde se encuentra corriendo el programa ingresa el parametro archivo
y devuelve la palabra listo so el nombreexiste o un mensaje de error si no existe
"""
def control_Open(archivoI):
    i=''
    try:
        f = open(os.path.join(directorio, archivoI),'r')
    except IOError as err:
        print('=======',"IO error: {}".format(err),'=======')
        f.close()
        return "IO error: {}".format(err)
    except FileExistsError as err:
        print('=======',"IO error: {}".format(err),'=======')
        f.close()
        return "FileExistsError: {}".format(err)
    except FileNotFoundError as err:
        print('=======',"IO error: {}".format(err),'=======')
        f.close()
        return "FileNotFoundError: {}".format(err)
    else:
        f.close()
        return "Listo"
# -----------------------------------------------------------------
print('***** ESTE PROGRAMA MODIFICA LOS VALORES FOTOMETRICOAS DE UN ARCHIVO FOTOMETRICO .ies *****')
print()
print('Tenga en cuenta qu el erchivo de entrada dee estar presente en el directorio en el cual se ejecuta este programa')
#ingresa el nombre de archivo de entrada y lo prueba
while listo != 'Listo':
    archivoI = input('INGRESE EL NOMRE DEL ARCHIVO DE ENTRADA :')
    listo = control_Open(archivoI)
    print(listo)

archivoO = input('InadaelpNGRESE EL NOMRE DEL ARCHIVO DE SALIDA : ')
str_factor = input('INGRESE EL FACTOR POR EL CUAL DESEA MULTIPLICAR LOS VALORES FOTOMETRICOS :')
factor = float(str_factor)
nreg = 0
with open(os.path.join(directorio, archivoO),'w', encoding='UTF-8') as o:
    with open(os.path.join(directorio, archivoI),'r', encoding='UTF-8') as i:
        for reg in i.readlines():
            camposI =[]
            if nreg < 13:
                o.writelines(reg) #graba e registro igual sin modificarlo
                nreg += 1
                continue
            camposI = reg.split('  ')
            print(nreg, reg, end='')
            O=''
            for campo in range(0,len(camposI)):
                print(camposI[campo], end='  ')
                aa=int(camposI[campo])
                bb=aa*factor
                O += str(int(bb))+'  '
            PRINT()
            O += '\n' #trmina el registro con un salto de carro
            o.writelines(O) #graa el registro con los nuevos valore
            print(nreg,O)
            nreg += 1


#  E.O.F.

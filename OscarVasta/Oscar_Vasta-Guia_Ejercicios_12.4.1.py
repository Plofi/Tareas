
"""
Oscar_Vasta-Guia_Ejercicios_12.4.

Escribir una clase Caja para representar cuánto dinero hay en una caja de un
negocio, desglosado por tipo de billete (por ejemplo, en el quiosco de la esquina hay 6 billetes
de 500 pesos, 7 de 100 pesos y 4 monedas de 2 pesos). Las denominaciones permitidas son 1, 2,
5, 10, 20, 50, 100, 200, 500 y 1000 pesos. Debe comportarse según el siguiente ejemplo:
>>> c = Caja({500: 6, 300: 7, 2: 4})
ValueError: Denominación "300" no permitida
16
>>> c = Caja({500: 6, 100: 7, 2: 4})
>>> str(c)
'Caja {500: 6, 100: 7, 2: 4} total: 3708 pesos'
>>> c.agregar({250: 2})
ValueError: Denominación "250" no permitida
>>> c.agregar({50: 2, 2: 1})
>>> str(c)
'Caja {500: 6, 100: 7, 50: 2, 2: 5} total: 3810 pesos'
>>> c.quitar({50: 3, 100: 1})
ValueError: No hay suficientes billetes de denominación "50"
>>> c.quitar({50: 2, 100: 1})
200
>>> str(c)
'Caja {500: 6, 100: 6, 2: 5} total: 3610 pesos'

"""
                                                    #define un diccionario con las denominaciones válidas solo para
                                                    # validar de forma indexada , el 2º término del diccionario se deja en 0 por qu e no se usa
denominaciones={1: 0, 2: 0, 5: 0, 10: 0, 20: 0, 50: 0, 100: 0, 200: 0, 500: 0, 1000: 0}
class Caja:
    def __init__(self, arqueo):                     #arqueo es un diccionario que contiene denominaciones y cantidad de billetes existentes en la caja
        self.arqueo = arqueo
    def __str__(self):
        totalcaja = 0
        for i in self.arqueo:
            try:
                if i in denominaciones:             # verifica que la denominacion buscada este entre las denominaciones permitidas
                    totalcaja +=  i * self.arqueo[i]# si esta suma la cantidad de billetes por la denominacion al total de caja
                else:                               # si en la lista hay una denominacion no permitida la borra para que no la
                    valor = self.arqueo.pop(i)      # sume y no la siga rechazando en póximas consultas y esto debe hacerlo
                                                    # antes de lanzar el ValueError por que si no ,no lo hace
                    raise ValueError('denominación '+'"'+str(i)+'"'+' no permitida')
            except ValueError as e:
                return str(e)
        return 'Caja '+str(self.arqueo)+' total: '+str(totalcaja)+' pesos'

    def agregar(self,otro):
        for i in otro:
            if self.arqueo.get(i) != None:
                self.arqueo[i] += otro[i]           #si existe le suma la cantidad de blilletes agregados
            else:
                valor = self.arqueo.setdefault(i, otro[i]) #si no esta se lo agrega, aunque podria ser una denominacion no
        return Caja(self.arqueo)                           #permitida, pero al pasrlo por el __str__Caja, se ocupara de quitarlo 




#------------------- PRUEBA ----------------------------------------
xx={500: 6, 100: 7, 2: 4}
c = Caja({500: 6, 100: 7, 2: 4})
print(c)
print('_'* 80,'\n')
d = c.agregar({250: 2})
print(d)
print('_'* 80,'\n')
d= c.agregar({50: 2, 2: 1})
print(d)
print('_'* 80,'\n')
#---------------------E.O.F.----------------------------------------
#for i in masbilletes:
#    print('buscando:',i, masbilletes[i])
#    if xx.get(i) != None:
#        print('existe:', i, xx[i], masbilletes[i])
#        xx[i]+=masbilletes[i]
#        print('ahora:',i, xx[i])
#    else:
#        print('no hay:', i, masbilletes[i])
#        valor = xx.setdefault(i, masbilletes[i])
#        print('alta:', i, xx[i])
#print(xx)

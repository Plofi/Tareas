"""
Oscar_Vasta-Guia_Ejercicios_13.1 revisión 1
Implementar el método __str__ de ListaEnlazada, para que se genere una
salida legible de lo que contiene la lista, similar a las listas de python.
** En esta nueva version perfeccione un poco el formato del método __str__
aunque todavía no logre lo que quiero con la representacion de los puntos
separadores de miles , los ejemplos que encuentro sobre este tema estan con
el viejo formato {:,} .format() y los métodos para remmplazar la , por el .
me parecen demasiado rebuscados , tiene que haber algo mas simple con el
nuevo formato % f() **
"""
class Nodo:
    def __init__(self, nombre=None, DNI=None, sig=None):
        self.nombre = nombre
        self.DNI = DNI
        self.sig = sig
    def __str__(self):
        return "%012s : %8d" %(self.nombre, self.DNI)

class listasimple:
    def __init__(self):
        self.cabeza = None
        self.cola = None
    def agregar(self, elemento):
        if self.cabeza == None:
            self.cabeza = elemento

        if self.cola != None:
            self.cola.sig = elemento
            self.cola = elemento

        self.cola = elemento

    def show(self):
        aux = self.cabeza
        while aux != None:
            print (aux)
            aux = aux.sig
#creamos 2 array con datos iniciales
nombres = ['Oscar', 'Graciela', 'Mecedes', 'Sara', 'Gise', 'Matias', 'Alexis', 'Ezequiel','Estanislao']
documentos =[12602584, 12856585, 34569876, 41876543, 29887021, 40987656, 93567876, 39876656, 6986501]
#Cargamos un array en la lista enlazada
ls = listasimple()
for i in range(len(nombres)):
    #print(nombres[i], documentos[i])
    nod = Nodo(nombres[i], documentos[i])
    ls.agregar(nod)
#listamos lo que cargamos
ls.show()
# ----------------------------- E.O.F. ---------------------------------

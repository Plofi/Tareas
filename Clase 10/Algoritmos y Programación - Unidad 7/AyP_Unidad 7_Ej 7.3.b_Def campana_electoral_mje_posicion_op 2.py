"""
Ejercicio 7.3. Campaña electoral

b) Escribir una función que reciba una tupla con nombres,
una posición de origen p y una cantidad n, e imprima el mensaje 
"Estimado <nombre>, vote por mí." para los n nombres que se encuentran a 
partir de la posición p.

"""

def campana_electoral_mje_posicion(nombres,p,n):
    """
    Recibe una tupla con nombres, una posición de origen y una cantidad n,
    e imprime el mensaje "Estimado <nombre>, vote por mí." para los n
    nombres que se encuentran a partir de la posición p.

        Parameters:
                (tuple) De nombres.
                (int) Posición de origen en la tupla de nombres,
                      (de cual se quiere partir). Debe ser menor a la longitud
                      de la cantidad de nombres dados o dará error.
                (int) Una cantidad de nombres que se quieren imprimir,
                      a partir de la posición dada. Debo tener en cuenta,
                      la longitud de la tupla o dará error si el número es mayor.

        Ouput: 
                Imprime la cadena con el mje. para la cantidad de
                nombres ingresados que se encuentran a partir de la posición dada.

    """
    assert p < len(nombres), "Variable p excede la longitud de la lista de nombres."
    assert p+n < len(nombres), "La cantidad de nombres que desea imprimir excede la longitud de la lista"
    
    m = min(p+n, len(nombres))
    for i in range(p,m): # p+n = Le sumo a la posición de la cual parto la cantidad de nombres que quiero imprimir
        print(f"Estimado {nombres[i]}, vote por mí.")
    
    
campana_electoral_mje_posicion(("Plofi", "Gato", "Agus", "Connie", "Sabri", "Palo", "Martin"),1,8)
"""
Ejercicio 7.3. Campaña electoral
a) Escribir una función que reciba una tupla con nombres, 
y para cada nombre imprima el mensaje "Estimado <nombre>, vote por mí."

"""

def campana_electoral_mje(nombres):
    """
    Recibe una tupla con nombres, y para cada nombre imprime
    el mensaje "Estimado <nombre>, vote por mí."

        Parameters:
                (tuple) De nombres.

        Output: 
                Imprime una cadena con el mje.

    """
    for i in nombres:
        print(f"Estimado {i}, vote por mí.")


campana_electoral_mje(("Plofi","Gato","Agus"))
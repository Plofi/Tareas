"""
Ejercicio 7.3. Campaña electoral

c) Modificar las funciones anteriores para que tengan en cuenta el género
del destinatario, para ello, deberán recibir una tupla de tuplas,
conteniendo el nombre y el género.
"""

def campana_electoral_mje_genero(nombres):
    """
    Recibe una tupla con nombres y su género, y para cada nombre imprime
    el mensaje "Estimado/a <nombre>, vote por mí."; según lo que corresponda
    con el género cargado previamente.

        Parameters:
                (tuple(tuple)) De nombres y género, ej.("Flor","fem").

        Output: 
                Imprime una cadena con el mje modificado según el género ingresado.

    """
    for i in range(len(nombres)):
        votante = nombres[i]
        if votante[1] == "fem":
            print(f"Estimada {votante[0]}, vote por mí.")
        else:
            print(f"Estimado {votante[0]}, vote por mí.")
       

destinatarios = (("Gato","masc"),("Plofi","fem"),("Agus","masc"),("Connie","fem"))

campana_electoral_mje_genero(destinatarios)

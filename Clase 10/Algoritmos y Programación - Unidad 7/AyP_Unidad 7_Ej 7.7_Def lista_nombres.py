"""
Ejercicio 7.7. Escribir una función que reciba una lista de tuplas 
(Apellido, Nombre, Inicial_segundo_nombre) y devuelva una lista de 
cadenas donde cada una contenga primero el nombre, luego la inicial 
con un punto, y luego el apellido.

"""
def lista_nombres(nombres):
    """
    Recibe una lista de tuplas (Apellido, Nombre, Inicial_segundo_nombre) 
    y devuelva una lista de cadenas donde cada una contenga primero el nombre, 
    luego la inicial con un punto, y luego el apellido.

        Parameters:
                (list(tuple)) Lista de tuplas, ej.[(Apellido, Nombre, Inicial_segundo_nombre)]

        Returns:
                (list(str)) Una lista de cadenas donde cada una contenga primero el nombre, 
                luego la inicial con un punto, y luego el apellido.

    """
    lista_nombres_final = []
    for i in nombres:
        persona = i
        lista_nombres_final.append(persona[1]+" "+persona[2]+"."+" "+persona[0])
    return lista_nombres_final


#Ej.
nombres = [("La Torre", "Gabriel", "A"),("Bussola", "Florencia", "C")]

print(lista_nombres(nombres))
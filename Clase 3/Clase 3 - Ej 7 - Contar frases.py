cantidad_frases = 0
mas_frases = "si"

while mas_frases == "si":
    print("Introduzca una frase:")
    arreglo_frases = [input()]
    print("Quiere introducir más frases? (si/no)")
    mas_frases = input()
    for numero in arreglo_frases:
        cantidad_frases = cantidad_frases+1
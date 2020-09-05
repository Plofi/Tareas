cantidad_frases = 0
mas_frases = "si"
arreglo_frases = []

while mas_frases == "si":
    print("Introduzca una frase")
    arreglo_frases.append(input())
    print("Quiere introducir más frases? (si/no)")
    mas_frases = input()
    cantidad_frases = cantidad_frases+1


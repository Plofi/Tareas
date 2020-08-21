contador_multiplos = 0
numero = 1
while numero <= 100:
    if numero % 2 == 0 or numero % 3 == 0:
        contador_multiplos = contador_multiplos+1
        print(numero)
    numero = numero+1
contador_par = 0
contador_impar = 0
numero = 1
while numero <= 100:
    print(numero)
    if numero % 2 == 0:
        contador_par = contador_par+numero
    else:
        contador_impar = contador_impar+numero
    numero = numero+1
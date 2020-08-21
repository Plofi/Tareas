print("Ingrese un número mayor a 1 e imprimiremos los múltiplos de 3 hasta ese número inclusive")
contador_multiplos = 0
numero = 1
ingreso = int(input())
while numero <= ingreso:
    if numero % 3 == 0:
        print(numero)
        contador_multiplos = contador_multiplos+1 
    numero = numero+1    
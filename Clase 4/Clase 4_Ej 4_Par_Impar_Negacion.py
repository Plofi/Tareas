numero = input("Ingrese un número par")
numero = int(numero)
if numero % 2 == 0:
    print(numero)
else:
    print("El número no es par")
numero2 = int(input("Ingrese un número impar"))
if not numero2 % 2 == 0:
    print(numero2)
else:
    print("El número ingresado no es impar")
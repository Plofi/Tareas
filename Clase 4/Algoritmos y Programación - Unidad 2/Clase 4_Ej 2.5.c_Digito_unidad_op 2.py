numero = input("Ingrese un número, le diremos el dígito de las unidades:")
while int(numero)>10:
    numero = int(numero) % 10
print(str(numero))

numero_mayor = None
numero_menor = None

for numero in range(1,6):
    numero_ingresado = int(input("Ingrese un número, imprimiremos el mayor y el menor de su serie de 5 números"))
    if numero_mayor is None or numero_ingresado > numero_mayor:
        numero_mayor = numero_ingresado        
    if numero_menor is None or numero_ingresado < numero_menor:
        numero_menor = numero_ingresado 

print("El número mayor es:")
print(numero_mayor)
print("El número menor es:")
print(numero_menor)
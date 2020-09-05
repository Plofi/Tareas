numero_mayor = 0
numero_menor = 99999
arreglo = []

for numero2 in range(1,6):
    numeros_ingresados = int(input("Ingrese un número, imprimiremos el mayor y el menor de su serie de 5 números"))
    arreglo.append(numeros_ingresados)
    
for n in arreglo:
    if n > numero_mayor:
        numero_mayor = n
        
for n in arreglo:
    if n < numero_menor:
        numero_menor = n 

print("El número mayor es:")
print(numero_mayor)
print("El número menor es:")
print(numero_menor)

numero = 1
numero_mayor = 0
numero_menor = 99999

while numero <= 5:
    print("Ingrese un número, imprimiremos el mayor y el menor de su serie de 5 números")
    numeros_ingresados = int(input())
    arreglo = ([numeros_ingresados])
    
    for n in arreglo:
        if n > numero_mayor:
            numero_mayor = n
        
    for n in arreglo:
        if n < numero_menor:
            numero_menor = n 

    numero = numero+1

print("El número mayor es:")
print(numero_mayor)
print("El número menor es:")
print(numero_menor)
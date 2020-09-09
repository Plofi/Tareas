def num_triangulares(num):
    suma = 0
    for n in range(1,num+1):
        suma = suma+n
        print(n, "-", suma)

num_triangulares(int(input("Ingrese un número, imprimiremos los numéros triangulares hasta ese número: ")))
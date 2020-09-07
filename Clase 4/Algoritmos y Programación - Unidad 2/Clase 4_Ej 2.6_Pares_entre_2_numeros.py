def numeros_pares_entre():
    numero1 = int(input("Ingrese un número:"))
    numero2  = int(input("Ingrese un segundo número, imprimiremos los números pares entre ellos:"))
    if numero1 < numero2:
        for n in range(numero1+1,numero2):
            if n % 2 == 0:
                print(n)
    if numero1 > numero2:
        for n in range(numero2+1,numero1):
            if n % 2 == 0:
                print(n)

numeros_pares_entre()
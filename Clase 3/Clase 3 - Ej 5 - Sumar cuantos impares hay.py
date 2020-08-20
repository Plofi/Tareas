numero = 1
suma_impares = 0
while numero <= 100:
    if numero % 2 != 0:
        print(numero)    
    suma_impares = suma_impares +1
    numero = numero +2
print("La cantidad de números impares que hay es...")
print(suma_impares)
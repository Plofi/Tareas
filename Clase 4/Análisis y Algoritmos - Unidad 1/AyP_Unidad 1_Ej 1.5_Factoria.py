n = int(input("Ingrese un número le diremos su factorial:"))#número dado
m = 1 #multiplicador
f = 1*m #factorial

while m <= n:
    f = f * m
    m = m+1

print("El factorial del número ingresado es:",f)
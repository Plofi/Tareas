n = int(input("Ingrese un número entero del cual quiera su factorial"))
m = 1 #multiplicador
f = 1*m

for m in range(1,n+1):
    f = f * m

print("El factorial de su número es:", f)
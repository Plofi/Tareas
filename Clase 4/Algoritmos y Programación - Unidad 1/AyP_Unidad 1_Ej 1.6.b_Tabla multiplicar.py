n = int(input("Ingrese un número entero del cual quiera su tabla hasta el 10:"))
m = 0 #multiplicador
print("La tabla del", n, "es:")

for m in range(0,11):
    resultado_tabla = n * m
    print(n, "x", m,"=",resultado_tabla)
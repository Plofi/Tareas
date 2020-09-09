n = int(input("Ingrese un número y le diremos su factorial:"))
numero_ingresado = [n]
agregar_numero = (input("Si desea ingresar otro número, ingrese si, sino ingrese no:"))
while agregar_numero == "si":
    n = int(input("Ingrese otro número:"))
    numero_ingresado.append(n)
    agregar_numero = (input("Desea agregar otro número, si o no:"))
    

def factorial(n):   #número dado x item
    f = 1         #factorial
    for m in range(1,n+1):    # m = multiplicador en el rango 
        f = f*m
    return print("El factorial de", n, "es:", f)

for item in numero_ingresado:
    factorial(item)
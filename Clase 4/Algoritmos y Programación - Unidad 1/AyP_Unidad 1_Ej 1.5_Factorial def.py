def factorial(n):   #número dado
    f = 1         #factorial
    for m in range(1,n+1):    # m = multiplicador en el rango 
        f = f*m
    return f
   
n = int(input("Ingrese un número, le diremos su factorial:"))
print("El factorial de su número es:", factorial(n))
def resultado_hipotenusa(cat1, cat2):
    h = (cat1**2) + (cat2*2) 
    return h**2

cat1 = int(input("Ingrese el 1er cateto de su trángulo rectángulo:"))
cat2 = int(input("Ingrese el 2do cateto de su trángulo rectángulo:"))
print("La hipotenusa de su triángulo es:", resultado_hipotenusa(cat1, cat2))
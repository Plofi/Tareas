def volumen_esfera(r):
    return 4/3 * 3.14 * r**3

r = int(input("Ingrese el radio de su esfera:"))
print("El volumen de su esfera es:", volumen_esfera(r))
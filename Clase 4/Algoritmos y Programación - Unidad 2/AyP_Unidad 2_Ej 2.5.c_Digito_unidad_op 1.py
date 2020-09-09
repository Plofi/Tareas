def digito_unidad(numero):
    return int(repr(numero)[-1])  

print(digito_unidad(int(input("Ingrese un número, le diremos el dígito de la unidad:"))))

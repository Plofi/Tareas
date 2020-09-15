#Ej. 3.3 = Escribir una función, que dado 4 números, devuelva el mayor producto:

def mayor_producto(a,b,c,d):
    producto = [a, b, c, d]
    maximo = None
    for i, numero in enumerate(producto): #numero toma el valor del array de producto en la posicion i, que va subiendo
        actual = i + 1
        while actual< len(producto):
            resultado = numero * producto [actual] # lo multiplica por producto [actual=posición en el array que va subiendo al sumarle uno al final]
            if maximo is None or resultado > maximo:
                maximo = resultado
            actual = actual + 1    
    return maximo

#Ej:
print("El mayor producto de estos 4 números es:",mayor_producto(1,5,-2,-4))
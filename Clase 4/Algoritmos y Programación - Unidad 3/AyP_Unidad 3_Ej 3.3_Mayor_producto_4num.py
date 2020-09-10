#Ej. 3.3 = Escribir una función, que dado 4 números, devuelva el mayor producto:

def mayor_producto(a,b,c,d):
    producto = []
    producto.append(a*b)
    producto.append(a*c)
    producto.append(a*d)
    producto.append(b*c)
    producto.append(b*d)
    producto.append(c*d)
    return max(producto)

#Ej:
print("El mayor producto de estos 4 números es:",mayor_producto(1,5,-2,-4))
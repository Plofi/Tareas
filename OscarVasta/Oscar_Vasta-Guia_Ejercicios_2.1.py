# Oscar Vasta Guia de Ejercicios 2.1 
def Cn(D,y,o): return D * ((1+(y / 100)) **o )
print('/'*120)
print('$$ CALCULA EL MONTO TOTAL A DEVOLVER EN BASE AL CAPITAL A FINANCIAR , LA TASA DE INTERES ANUAL Y EL NÚMERO DE AÑOS $$')
print('mediante el método del interes compuesto, " LA FUERZA MAS PODEROSA DEL UNIVERSO " segun Albert Einstein')
print()
C=float(input("Ingrese el capital inicial en $ :"))
x=float(input('Ingrese la tasa de interes anual en % :'))
n=int(input('Ingreseel número de años de plazo (entero) :'))
print('El monto total de la financiacion (Capital + intereses) es : $' , Cn(C,x,n))
print()
print('_'*120)
# - END OF FILE -






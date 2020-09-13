# Oscar Vasta Guia de Ejercicios 2.1
def Cn(D,y,o):
    #1º controlamos que los datos sean numericos para que no nos de error al pasarlos a Int() o float()
    if D.isdigit() and y.isdigit() and o.isdigit():
        return D * ((1+(y / 100)) **o )
    else:
        return "<ERROR> uno de los 3 datos no es numérico, vuelva a ingresarlos"

continua = 'S'
# lazo principal de ejecucion del programa
while continua == 'S' or continua == 's':
    print('/'*120)
    print('$$ CALCULA EL MONTO TOTAL A DEVOLVER EN BASE AL CAPITAL A FINANCIAR , LA TASA DE INTERES ANUAL Y EL NÚMERO DE AÑOS $$')
    print('mediante el método del interes compuesto, " LA FUERZA MAS PODEROSA DEL UNIVERSO " segun Albert Einstein')
    print()
    C=input("Ingrese el capital inicial en $ :")
    x=input('Ingrese la tasa de interes anual en % :')
    n=input('Ingreseel número de años de plazo (entero) :')
    print('El monto total de la financiacion (Capital + intereses) es : $' , Cn(C,x,n))
    print()
    print('_'*120)
    continua=input('quiere hacer otro cálculo: [S] o [N]')
for i in range(20):
    print()
# - END OF FILE -

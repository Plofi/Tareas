# Oscar Vasta Guia de Ejercicios 2.3
"""
Escribir una función que convierta un valor dado en grados Fahrenheit a grados
Celsius. Recordar que la fórmula para la conversión es: 𝐹 = 9/5
𝐶 + 32
"""
c=float()
def F2C(G):
    g=float(G)
    return 5 / 9 * (g - 32)
continua = 'S'
# lazo principal de ejecucion del programa
while continua == 'S' or continua == 's':
    c=input("Ingrese la temperatura en grados Fahrenheit : ")
    print('La temperatura en ºC es : ','{:>-10.6}'.format(F2C(c)))
    print('_'*80)
    continua=input('quiere hacer otro cálculo: [S] o [N]')
for i in range(20):
    print()
# - END OF FILE -

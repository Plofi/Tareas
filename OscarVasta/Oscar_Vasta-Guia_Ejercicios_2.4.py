# Oscar Vasta Guia de Ejercicios 2.4
"""
Escribir un programa que utilice la función anterior para generar una tabla de
conversión de temperaturas, desde 0 °F hasta 120 °F, de 10 en 10.
"""
c=float()
#
def F2C(G):
    g=float(G)
    return 5 / 9 * (g - 32)
#
print(' ','_'*26)
print('  | Fahrenheit |  Celcius  |')
# lazo principal de ejecucion del programa
for c in range(0, 120 + 10, 10):
    print('  | ','{:>-6}'.format(c),'   =','{:>-7.3}'.format(F2C(c)),'  |')
#
print(' ','_'*26)
print()
# - END OF FILE -

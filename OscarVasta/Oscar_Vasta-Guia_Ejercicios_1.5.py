# ejercicio 1.5 de Oscar Vasta 
# calculo del factorial de un número !n 
import math
I=int(1)
F=int()
print('_'*80)
print('<'*20,' CALCULO DEL FACTORIAL DE UN NÚMERO !Nº','>'*20)
print()
n=int(input('ingrese en número del que desea obtener el factorial :'))
print()
for i in range(n):
    I = I*(i+1)
#
print('1º El factorial mediante la instruccion for es :',I)
F = math.factorial(n)
print('2º El factorial mediante la funcion "math.factorial()" es :',F)
print()
print('_'*80)
#
# END OF FILE






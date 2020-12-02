# ejercicio 1.6 de Oscar Vasta 
# Dados 2 números calcular, mediante funciones, las cuatro operaciones básicas entre ambos
def suma(m1, m2): return m1 + m2
def resta(m1, m2): return m1 - m2
def producto(m1, m2): return m1 * m2
def cociente(m1, m2): return m1 / m2
print('_'*80)
print('>'*10,' CALCULO DE CUATRO OPERACIONES BÁSICAS ENTRE 2 NÚMEROS','<'*10)
print()
n1=float(input('ingrese el 1º número :'))
n2=float(input('ingrese el 2º número :'))
print()
print('La suma es :',suma(n1,n2))
print('La resta es :',resta(n1,n2))
print('El producto es :',producto(n1,n2))
print('El cociente es :',cociente(n1,n2))
print()
n3=int(input('ingrese un número entero del cual desea la tabla de multiplicar:'))
print('**- TABLA DE MULTIPLICAR DEL ',n3,'-**')
print(n3,'X 1 =',n3,' '*(20-(len(str((n3))))),'|',n3,'X 2 =',(n3*2))
print(n3,'X 3 =',(n3*3),' '*(20-(len(str((n3*3))))),'|',n3,'X 4 =',(n3*4))
print(n3,'X 5 =',(n3*5),' '*(20-(len(str((n3*5))))),'|',n3,'X 6 =',(n3*6))
print(n3,'X 7 =',(n3*7),' '*(20-(len(str((n3*7))))),'|',n3,'X 8 =',(n3*8))
print(n3,'X 9 =',(n3*9),' '*(20-(len(str((n3*9))))),'|',n3,'X 10 =',(n3*10))
print('_'*80)
#
# END OF FILE






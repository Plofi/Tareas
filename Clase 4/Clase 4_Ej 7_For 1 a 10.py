
# código original:
"""
numero = int(numero)
for numero = 1; numero<=10; numero ++;
if numero % 2 == 0
print (numero)
"""
# Esto da un error de sintaxis en la linea 5

# @OscarVasta  propone esta solución:

for numero in range (1, 10):
    if numero % 2 == 0:
        print(numero)

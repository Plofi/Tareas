# --  Oscar Vasta -- Curso Python -- Guia de ejercicios -- Ejercicio 9.2 --- #
"""
a) Escribir una función que reciba una cadena y devuelva un diccionario con la cantidad
de apariciones de cada palabra en la cadena. Por ejemplo, si recibe ”Qué lindo día que
hace hoy” debe devolver: { 'que': 2, 'lindo': 1, 'día': 1, 'hace': 1, 'hoy': 1}.
b) Escribir una función que cuente la cantidad de apariciones de cada caracter en una cadena
de texto, y los devuelva en un diccionario.
c) Escribir una función que reciba una cantidad de iteraciones de una tirada de 2 dados a
realizar y devuelva la cantidad de veces que se observa cada valor de la suma de los dos
dados.
"""
#
# a)_______________________________________
def cuentapalabra(texto):
    lista = texto.split(" ")
    cuentapalabra = {}
    for word in lista:
        word = word.lower()
        if word in cuentapalabra:
            cuentapalabra[word] += 1
        else:
            cuentapalabra[word] = 1
    return cuentapalabra
#
# b)_______________________________________
def cuentaletra(texto):
    cuentaletra = {}
    for letra in texto:
        if letra != ' ':
            le=letra.lower()
            if le in cuentaletra:
                cuentaletra[le] += 1
            else:
                cuentaletra[le] = 1
    return cuentaletra
#
# c)_______________________________________
from random import randint, uniform,random
cuentatiradas={}
def tiradasdados(texto):
    for letra in texto:
        dado1 = randint(1,6)
        dado2 = randint(1,6)
        sumatirada = dado1+dado2
        if sumatirada in cuentatiradas:
            cuentatiradas[sumatirada] += 1
        else:
            cuentatiradas[sumatirada] = 1
    return cuentatiradas
#==========================================================
# ------------------prueba de funcones --------------------
verocurrencias="El Gobierno nacional sumó un nuevo conflicto con otro de los sectores del comercio internacional. Mientras busca convencer a los exportadores para que aceleren la liquidación de divisas, una semana más tarde que los importadores pidieran exclusividad en el acceso a las dólares frente a un escenario de escasez, el Banco Central emitió una nueva resolución ajustando aún más el cepo para este sector. Mediante la Comunicación -A- 7138 de ayer, el Central anunció más restricciones para que los importadores accedan al mercado cambiario mayorista, como por ejemplo la exigencia de la aprobación previa de Aduana y que quienes hayan hecho hace un año pagos por importaciones de bienes que aún no ingresaron al país, regularicen su situación para poder volver a hacer pagos anticipados. Pero no sólo eso, sino que la autoridad monetaria bajó al 10% de lo establecido el ítem de - Anticipo de Operaciones Cambiarias - y la pasó de USD 500.000 a operaciones de USD 50.000, lo que hace que, básicamente, sean todas las operaciones las que tienen que ser informadas y, a partir de esto, que los importadores tengan que esperar el tiempo establecido para acceder el mercado cambiario, que es de 72 horas."
print('A'*80)
print()
print(cuentapalabra(verocurrencias))
print()
print('B'*80)
print()
print(cuentaletra(verocurrencias))
print()
print('C'*80)
print()
print(tiradasdados(verocurrencias))

#-------------------- E.O.F. -----------------------------

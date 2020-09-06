capital = int(input("Ingrese su capital inicial en pesos:"))
tasa_interes = int(input("Ingrese la tasa de interés:"))
años = int(input("Ingrese la cantidad de años a calcular:"))

def monto_final(capital, tasa_interes, años):
    monto_final = capital*(1+tasa_interes/100)**años
    return monto_final

print("El monto final a pagar será:", monto_final(capital, tasa_interes, años))

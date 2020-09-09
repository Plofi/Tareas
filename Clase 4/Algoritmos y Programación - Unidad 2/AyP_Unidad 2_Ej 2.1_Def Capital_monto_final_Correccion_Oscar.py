def monto_final(capital, tasa_interes, años):
        return capital*(1+(tasa_interes/100))**años

print(monto_final(100,5,8))
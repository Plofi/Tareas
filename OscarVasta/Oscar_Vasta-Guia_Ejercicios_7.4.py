"""
Oscar_Vasta-Guia_Ejercicios_7.4.py
7.4. Vectores
a) Escribir una función que reciba dos vectores y devuelva su producto escalar.
b) Escribir una función que reciba dos vectores y devuelva si son o no ortogonales.
c) Escribir una función que reciba dos vectores y devuelva si son paralelos o no.
d) Escribir una función que reciba un vector y devuelva su norma.
"""
#-- a) producto escalar
def prodesc(v1,v2):
    c=0
    vs=()
    vsl=list(vs)
    for i in range(0,3):
        #print('*',vs[i],'* |',v1[i],'|',v2[i])
        vsl.append(v1[i]*v2[i])
    vs=tuple(vsl)
    return vs
# -- b) verifica perpendicularidad en el plano X Y
def vort(v1,v2):
    c=0
    vs=()
    vsl=list(vs)
    for i in range(0,2):
        vsl.append(v1[i]*v2[i])
    vs=tuple(vsl)
    if sum(vs) == 0:
        return 'son ortogonales'
    else:
        return 'no son ortogonales'
# -- c) verifica paralelismo y sentido por el método del coseno
# -- del ángulo
def vpar(v1,v2):
    c=0
    vs=()
    vm=()
    vsl=list(vs)
    vml=list(vm)
    cosenov=0
    for i in range(0,2):
        vsl.append(v1[i]*v2[i])
        vml.append((v1[i]**2)+(v2[i]**2))
    vs=tuple(vsl)
    vm=tuple(vml)
    cossenov=sum(vs)/(sum(vm)**0.5)
    if abs(cosenov) == 1:
        if cosenov > 0:
            return 'son paralelos ', 'son del mismo sentido'
        else:
            return 'son paralelos', 'son de sentido contrario'
    else:
        return 'no son paralelos', ''
# -- d) norma o longitud o medida  de los 2 vectores
# --    por el método del teorema de pitágoras
def norma(v1,v2):
    c=0
    vn1=()
    vn2=()
    vnl1=list(vn1)
    vnl2=list(vn2)
    for i in range(0,2):
        vnl1.append(v1[i]**2)
        vnl2.append(v2[i]**2)
    vn1=tuple(vnl1)
    vn2=tuple(vnl2)
    n1=(sum(vn1)**0.5)
    n2=(sum(vn2)**0.5)
    return n1,n2

# ----- programa de prueba ----
m1=(3,1,6)
m2=(9,1,5)
print()
print('_ Dados los vectores : ',m1,'y',m2)
print()
print('_ El producto escalar es : ',prodesc(m1,m2))
print()
print()
print('_ Se verifica si los mismos vectores son ortogonales en el plano X Y')
print()
print('             **  ',vort(m1,m2),'  **')
print()
print()
print('_ Se verifica si los mismos vectores son paralelos en el plano X Y')
print()
print('      **  ',vpar(m1,m2),'  **')
print()
print()
print('_ Y la norma , medida o longitud de los dos vectores es : ')
print('{:>-10.6}'.format(norma(m1,m2)[0]),' y ','{:>-10.6}'.format(norma(m1,m2)[1]),'respectivamente')
print()
print('_'*80)



# E.O.F.

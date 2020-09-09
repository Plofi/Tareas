def fichas_juego(n):
    der = 0
    saltear =n-1

    for izq in range(0, n+1):
        while der<n:
            print(izq, "-", der)
            der = der+1
        print(izq, "-", der)
        der = der-saltear
        saltear = saltear-1

fichas_juego(n)
def fichas_domino():

    der = 0
    saltear = 5

    for izq in range(0,7):
        while der<6:
            print(izq, "-", der)
            der = der+1
        print(izq, "-", der)
        der= der-saltear
        saltear= saltear-1

fichas_domino()    
def busqueda(lista, x):
    if(len(lista)== 0):
        print("la lista esta vacia ")
        return -1
    elif(len(lista)== 0):
        if(lista[0]==1):
            return 0
        else:
            print("no esta")
            return -1
    else:
        izq = 0
        der = len(lista)
        mitad = (izq+der)//2

        if(x == lista[mitad]):
            return mitad
        elif(x>lista[mitad]):
            izq = mitad+1
        elif (x < lista[mitad]):
            der = mitad - 1


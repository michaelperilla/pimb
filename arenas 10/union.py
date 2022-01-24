def conjuntos(lista, lista1):
    lista2=[]
    lista3=[]
    if (len(lista)<=20 and len(lista1)<=20):
        lista2.append(lista)
        lista2.append(lista1)
    else:
        if(len(lista)>20 and len(lista1)<=20):
            print("la primera lista tiene mas de 20")
            return conjuntos
        elif(len(lista)<=20 and len(lista1)>20):
            print("la segunda lista tiene mas de 20")
            return conjuntos
        else:
            print("las dos listas tiene mas de 20")
            return conjuntos

    for i in lista2:
            if(i!=lista2[i]+1):
                lista3.append(lista2)
            else:
                lista3


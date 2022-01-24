def main(lis):
    #lis es el arreglo bidimencional
    lista = []
    for i in range(len(lis)):
        ct = 0
        #se pone un contador
        for j in range(len(lis[i])):
            ct += lis[i][j]
            #se va sumando las posiciones
        lista.append(ct)
        #se agrega a la lista vacia
    print(lista)

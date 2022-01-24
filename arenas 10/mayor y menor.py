def main(lista):
    def menor(lista):
        n = lista[0]
        for i in lista:
            if (i < n):
                n = i
        return (n)

    def mayor(lista):
        n = lista[0]
        for i in lista:
            if (i > n):
                n = i
        return (n)

    def promedio(lista):
        ct = 0
        for i in range(0,len(lista)):
            ct = ct+lista[i]
        ct = ct/len(lista)+1
        return (ct)

    print("su numero menor es",menor(lista))
    print("su numero mayor es",mayor(lista))
    print("el promedio es",promedio(lista))
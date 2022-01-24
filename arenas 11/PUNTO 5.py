from sys import stdin


def ordenar(lista):
    for pas in range(len(lista) - 1, 0, -1):
        for i in range(pas):
            if lista[i] > lista[i + 1]:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]

    return lista


lista = [5, 20, 3, 2, 50, 80]
lista1 = ordenar(lista)

n = int(stdin.readline().strip())
imprimir = []

for i in range(len(lista1)):

    for j in range(len(lista1)):
        if int(lista1[i]) - int(lista1[j]) == n:
            imprimir.append(lista1[i])
            imprimir.append(lista1[j])
            lista.append(i)
            lista.append(j)
        elif int(lista1[j]) - int(lista1[i]) == n:
            imprimir.append(lista1[i])
            imprimir.append(lista1[j])
            lista.append(i)
            lista.append(j)

if len(imprimir) == 0:
    print("pareja no encontrada")
else:
    print("{0} {1} {2}".format(imprimir[0], "y", imprimir[1]))

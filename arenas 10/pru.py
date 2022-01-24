from sys import stdin


def Main():
    lista = [int(i) for i in stdin.readline().strip().split(",")]
    listai = []

    Invertir(lista, listai)


def Invertir(lista, listai):
    if len(lista) == 0:

        Imprimir(listai)

    else:

        listai.append(lista[len(lista) - 1])
        Invertir(lista[0:len(lista) - 1], listai)


def Imprimir(listai, string=""):
    if len(listai) == 0:

        print(string)

    else:

        if len(listai) != 1:
            string += str(listai[0]) + ","
        else:
            string += str(listai[0])

        Imprimir(listai[1:], string)


Main()
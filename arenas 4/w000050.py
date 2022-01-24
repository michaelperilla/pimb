from sys import stdin


def main():
    lista = [int(i) for i in stdin.readline().strip().split(",")]
    lista1 = []
def invertir (lista,lista1):
    if(len(lista)):
        res = lista1
        return res
    else:
        lista1= lista[::-1]
        print(lista1)
main()

from sys import stdin

def inv(lista):
    if len(lista)==1:
        return lista
    else:
        return lista[-1]+inv(lista[:-1])


def main():
    x = stdin.readline().strip()
    while x!="":
        print(inv(x))
        lista = []
        lista.append(x)
        x = stdin.readline().strip()

main()

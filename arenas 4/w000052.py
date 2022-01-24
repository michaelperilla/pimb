from sys import stdin
def Main():
    n1 = int(stdin.readline().strip())
    n2 = int(stdin.readline().strip())

    if (n1 > n2):
        nummayor = n1
        nummenor = n2
    elif(n1 < n2):
        nummayor = n2
        nummenor = n1
    else:
        nummayor = n1
        nummenor = n2

    dividir(nummayor, nummenor)

def dividir(x, y):
    if (x / y == x // y):
        print(y)
    else:
        dividir(y,x % y)
Main()
from sys import stdin
x = (stdin.readline().strip())
x = int(x)
lista = []

for i in range(x):
    numero = []
    y = int(stdin.readline().strip())
    for j in range(y):
        z = list((stdin.readline().strip().split(" ")))
        z = int(z)
        res = (z[0]-z[1])
        res = w
        numero.append(w)
        suma = sum(numero)
        if(suma == (w*y)):
            lista.append(1)
        else:
            lista.append(0)

for h in range(len(lista)):
    if(lista[h] == 1):
        print("yes")
    else:
        print("no")

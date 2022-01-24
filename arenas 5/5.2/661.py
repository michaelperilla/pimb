from sys import stdin
res = []
n, m, c = stdin.readline().strip().split(' ')
while (n !='0' and m != '0' and c != '0'):
    max = 0
    ct = 0
    lista = []
    amperaje = []
    for i in range(int(n)):
        x = int(stdin.readline())
        amperaje.append(x)
        lista.append(0)
    for j in range(int(m)):
        x1 = int(stdin.readline())
        if(lista[x1-1]==0):
            ct += amperaje[x1-1]
            lista[x1 - 1] = 1
        else:
            ct -= amperaje[x1 - 1]
            lista[x1 - 1] = 0
        if(max < ct):
            max = ct
    if(max > int(c)):
        res.append('F')
    else:
        res.append(max)
    n, m, c = stdin.readline().strip().split(' ')
for h in range(len(res)):
    if (res[h] == 'F'):
        print("Sequence", str(h+1))
        print("Fuse was blown.")
    else:
        print("Sequence", str(h+1))
        print("Fuse was not blown.")
        print("Maximal power consumption was", str(res[h]), "amperes.")

    print('')
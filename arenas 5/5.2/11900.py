from sys import stdin

casos = int(stdin.readline().strip())
ct = 1
result = []
for i in range(casos):
    n, x, y = stdin.readline().strip().split()
    n = int(n)
    p = int(x)
    q = int(y)

    pesos = stdin.readline().strip().split()
    pesos = sorted(pesos)
    cant = 0
    peso = 0
    max = 0
    for j in range (n):
        peso += int(pesos[j])
        cant += 1
        if(peso > q or cant > p):
            if (max < cant-1):
                max = cant-1
            peso = int(pesos[j])
            cant = 1
    result.append(max)

for i in range(len(result)):
    print("Case " + str(i+1) + ": " + str(result[i]))


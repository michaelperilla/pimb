from sys import stdin


eventos = int(stdin.readline().strip())

ct = 0
res = []

while(ct < eventos):

    x = int(stdin.readline().strip())
    y = int(stdin.readline().strip())

    suma = 0
    while (x < y+1):
        if (x % 2 != 0):
            suma += x
        x +=1

    ct += 1
    res.append(suma)

ct = 1
while(ct <= len(res)):
    print('Case '+str(ct)+': '+str(res[ct-1]))
    ct +=1



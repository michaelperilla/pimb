from sys import stdin

def ordenMenor(lis):
    for i in range(len(lis)):
        mini = min(lis[i:])
        min_index = lis[i:].index(mini)
        lis[i + min_index] = lis[i]
        lis[i] = mini

def ordenMayor(lis):
    for i in range(len(lis)):
        maxi = max(lis[i:])
        max_index = lis[i:].index(maxi)
        lis[i + max_index] = lis[i]
        lis[i] = maxi

def stringToInt(lis):
    for i in range(0, len(lis)):
        lis[i] = int(lis[i])

n1, d1, r1 = stdin.readline().strip().split(' ')
list = []
while(n1 != '0' and d1 != '0' and r1 != '0'):
    n = int(n1)
    d = int(d1)
    r = int(r1)
    rm = stdin.readline().strip().split(' ')
    stringToInt(rm)
    ordenMayor(rm)

    rt = stdin.readline().strip().split(' ')
    stringToInt(rt)
    ordenMenor(rt)

    ct = 0
    z = 0
    while(ct < n):
        t = int(rm[ct])
        f = int(rt[ct])
        ct +=1

        x = t+f
        y = x-d
        if(y<0):
            y = 0
        z = z + y*r

    list.append(z)
    n1, d1, r1 = stdin.readline().strip().split(' ')

for e in list:
    print(e)

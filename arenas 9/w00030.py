from sys import stdin

def Burbuja(Lista):
    for numPasada in range(len(Lista)-1,0,-1):
        for i in range(numPasada):
            if Lista[i]>Lista[i+1]:
                Lista[i],Lista[i+1] = Lista[i+1],Lista[i]


def mul():

    x = stdin.readline().strip().split(',')
    y = stdin.readline().strip().split(',')
    
    l = []
    pos = 0
    a = len(x)
    while a!=0:
        h = int(x[pos])**int(y[pos])
        round(h,1)
        l.append(h)
        pos = pos+1
        a = a-1
    Burbuja(l)

    print(str(l).replace("[","").replace("]","").replace(" ",""))

mul()

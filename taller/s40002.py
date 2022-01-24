from sys import stdin
def Cel(n):
    C=(n-32)*(5/9)
    print(round (C,2))

def va(n):
    F=((9*n)/5)+32
    print(round(F,2))
    
x=str(stdin.readline().strip())
l=[]

if "F"in x:
    x = int(x[1::])
    for x1 in range(x):
        n = float(stdin.readline())
        l.insert(x1,n)
    for x1 in range(x):
        Cel(l[x1])
else:
    x = int(x[1::])
    for x1 in range(x):
        n = float(stdin.readline())
        l.insert(x1,n)
    for x1 in range(x):
        va(l[x1])
        
    

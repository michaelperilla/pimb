from sys import stdin
n = stdin.readline().strip().split()
x=int(n[0])
y=int(n[1])
z=int(n[-1])
for i in range(y,(z+1)):
    n1 = x*i
    print(str(x)+" x "+str(i)+" = "+str(n1))

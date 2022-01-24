from sys import stdin

def prom(x,y,z,z1):
    for i in range(x):
        k =((y[i]-z1)**2)
        z += k
        return z

x = int(stdin.readline())
y=[]
a = 0
D = 0

for i in range(x):
    n1 = float(stdin.readline())
    y.insert(i,x)
    a += n1
z1 = (a/Vd)
z = prom(x,T1,0,z1)
prom = ((z/x)**(1/2))
print("Promedio: "+ str(round(z1,2)))
print("D.Estandar: "+ str(round(prom,2)))
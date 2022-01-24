from sys import stdin
def var(Vd,T1,Pp,Pro):
    for i in range(Vd):
        K =((T1[i]-Pro)**2)
        Pp += K
    return Pp
Vd = int(stdin.readline())
T1=[]
pp = 0
D = 0
for i in range(Vd):
    N=float(stdin.readline())
    T1.insert(i,N)
    pp += N
Pro = (pp/Vd)
Pp = var(Vd,T1,0,Pro)
var =((Pp/Vd)**(1/2))
print("Promedio: "+ str(round(Pro,2)))
print("D.Estandar: "+ str(round(Des,2)))

from sys import stdin

m = float(stdin.readline())
b = float(stdin.readline())

if((m<0) and (b<0)):
    m = m*-1
    b = b*-1
if((m<0) and (b>0)):
    m = m*-1
if((m>0) and (b<0)):
    b = b*-1
if(m==0):
    print("Triangulo Imposible")
else:
    x = b / m
    x1 = ((x ** 2)+(b ** 2)) ** 0.5
    x2 = x1 + b + x
    x3 = (x * b) / 2
    print("El area es:","%.2f"%x3,"y el perimetro es:","%.2f"%x2)

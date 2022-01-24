from sys import stdin

def kaprecar():
    cuadrado=x**2
    factor=10
    c=0
    while cuadrado//factor!=0:
        num=cuadrado//factor
        r=cuadrado%factor
        suma=num+r
        if suma==x1 and r!=0:
            c=1
        factor*=10

def numeros_felices():
    x = 1
    while n != 1:
        a = 0
        s = str(n)
        for i in range(len(s)):
            a = a + int(s[i]) ** 2
        n = a
        if n == 1:
            return True
        x += 1
        if x == 20:
            return False

    for j in range():
        if j == 1:
            print(j)
        if numeroFeliz(j):
            print(j)

l=[]

while(" "):
    x1 = int(stdin.readline())
    l.append(x1)

numeros_felices(l)
kaprecar(l)

print("Lista Ordenada de Kaprekar:")
print(l)
print("Cantidad Total de Felices:",l)


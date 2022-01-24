#1)elevar el numero al cuadrado
#2)dividir el numero por el factor y que sea diferente a 0
#3)sacar el mot(%)
#4)sumar el mot al numero
#5)mirar su es kaprecar o no

def kaprecar(n):
    cuadrado=n**2
    factor=10
    c=0
    while cuadrado//factor!=0:
        num=cuadrado//factor
        r=cuadrado%factor
        suma=num+r
        if ((suma==n) and (r!=0)):
            c=1
            factor*=10
            print("es kaprecar")
        else:
            print("no es kaprecar")
 
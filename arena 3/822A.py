from sys import stdin

def factorial (n):
    if(n == 1):
        return 1
    else:
        return factorial(n-1) * n

def maximo(x,y):
    resto = 0
    while (y > 0):
        resto = y
        y = x % y
        x = resto
    return x


x = int(stdin.readline())
y = int(stdin.readline())


print((maximo(factorial(x), factorial(y))))

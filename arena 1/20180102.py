from sys import stdin

a = stdin.readline()
b = stdin.readline()
c = stdin.readline()
d = stdin.readline()
e = stdin.readline()
try:
    a = int(a)
    b = int(b)
    c = int(c)
    d = int(d)
    e = int(e)
    if a == 1 and b == 0 and c == 1 and d == 1 and e == 1:
        print("Recorrido Valido")
    elif a == 1 and b == 1 and c == 0 and d == 1 and e == 1:
        print("Recorrido Valido")
    elif a == 0 or b == 0 or c == 0 or d == 0 or e == 0:
        print("Recorrido No Valido")
    else:
        print("Valor Leido No Valido")
except ValueError:
    print("Valor Leido No Valido")


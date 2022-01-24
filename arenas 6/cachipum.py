from sys import stdin
x = int(stdin.readline().strip())
ct = 0
b = 0
m = 0
e = 0

while(ct < x):
    juego = stdin.readline().strip()
    numero = int(juego[0])
    ct2 = 1
    ben = 0
    while(ct2 <= numero ):
        ben += int(juego[ct2*2])
        ct2 += 1

    if(ben > numero - ben):
        b += 1
    elif(ben == numero - ben):
        e += 1
    else:
        m += 1
    ct += 1

print(str(m)+' '+str(b)+' '+str(e))



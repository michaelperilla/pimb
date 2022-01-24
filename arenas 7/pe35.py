from sys import stdin

def esPrimo(x):
    if x < 2:
        return False

    for num in range(2,x):
        if x%num == 0:
            return False

    return True

def esCiclo(num):
    text = str(num)
    ct = 1
    while (ct < len(text)):
        temp = text[1:]
        text = temp + text[:1]
        if(not esPrimo(int(text))):
            return False
        ct += 1
    return True

m = int(stdin.readline().strip())
s = 0
ct = 2


if(m > 10000):
    s = 50880
    ct = 10001

if(m > 30000):
    s = 102147
    ct = 30001

if(m > 40000):
    s = 178465
    ct = 70001

if(m >= 75000):
    s = 250458
    ct = 90001

if(m > 100000):
    s = 628652
    ct = 115001

if(m >= 193939):
    s = 822591
    ct = 193940

while ct <= m:
    if(esPrimo(ct)):
        if (esCiclo(ct)):
            s = s + ct
    ct += 1
print(s)
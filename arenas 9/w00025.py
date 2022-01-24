from sys import stdin

def es_potencia_de_dos(numero):
    if numero < 1:
        return False
    if numero <= 2:
        return True
    i = 2
    while True:
        i *= 2
        if i == numero:
            return True
        if i > numero:
            return False


x = int(stdin.readline())
lista = stdin.readline().strip().split(' ')

if es_potencia_de_dos(x):
    matriz = [lista[x*i : x*(i+1)] for i in range(x)]

    matriz[0][0] = True
    k = 1
    while k < x:
        i = 0;
        while i < k:
            j=0
            while j < k:
                matriz[i + k][j] = matriz[i][j]
                matriz[i][j + k] = matriz[i][j]
                matriz[i + k][j + k] = not matriz[i][j]
                j += 1
            i += 1
        k += k

    resp = []
    for i in range(x):
        resp += matriz[i]

    valid = "Hadamard";
    for i in range(len(resp)):
        if (resp[i] and lista[i] == 'F') or (not resp[i] and lista[i] == 'T'):
            valid = "No Hadamard"

    print(valid)
else:
    print("Imposible")
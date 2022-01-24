from sys import stdin
x = stdin.readline()
x1 = stdin.readline()
ataque = 0
defensa = 0
resta = 0
for j in range(6):
    x2,a,d = stdin.readline().strip().split(' ')
    ataque += int(a)
    defensa += int(d)
resta = ataque - defensa
#--------------------------------------------------------------------------------
y = stdin.readline()
y1 = stdin.readline()
ataque1 = 0
defensa1 = 0
resta1 = 0
for i in range(6):
    y2,a,d = stdin.readline().strip().split(' ')
    ataque1 += int(a)
    defensa1 += int(d)
resta1 = ataque1 - defensa1

if(resta > resta1):
    print(x)
elif(resta < resta1):
    print(y)
else:
    print("Empate")
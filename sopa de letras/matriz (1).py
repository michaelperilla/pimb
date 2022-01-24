from sys import stdin
print("bienvenido")

matriiz = open("matriz.ext","w")

print("tamaño")
roberto = int(stdin.readline().strip())
for i in range(roberto):
    print("fila")
    ##lista=[str(x) for x in stdin.readline().strip().split()]
    ##lista1.append(lista)
    matriiz.write(stdin.readline().strip()+'\n')

matriiz.close()


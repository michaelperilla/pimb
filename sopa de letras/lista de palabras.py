from sys import stdin
print("bienvenido")

lista_palabras = open("lista_palabras.ext","w")

print("cuantas plabras")
palabras = int(stdin.readline().strip())
for i in range(palabras):
    print("palabras")
    ##lista=[str(x) for x in stdin.readline().strip().split()]
    ##lista1.append(lista)
    lista_palabras.write(stdin.readline().strip()+'\n')

lista_palabras.close()


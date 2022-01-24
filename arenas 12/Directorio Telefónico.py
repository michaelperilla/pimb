from sys import stdin

def EncontrarDirectorio(llave):

    return directorio[llave]

def Directorio(llave,valor):

    if llave not in directorio:
        directorio[llave] = valor

    return directorio

def EncontrarHash(llave):

    LlaveHash = FuncionHash(llave)
    pedazo = TablaHash[LlaveHash]
    
    for i in pedazo:

        if i[0] == llave:
            return i[1]
        
def FuncionHash(llave):

    return hash(llave) % len(TablaHash)

def Insertar(llave,valor):

    LlaveHash = FuncionHash(llave)
    pedazo = TablaHash[LlaveHash]
    existe = False

    for i in pedazo:

        if llave in i:
            existe = True
            
            break

    if not existe:
        TablaHash[LlaveHash].append((llave,valor))
    #Si ya existe esa llave pero hay que agregarlo, se le suma 1 a la llave
    #y se guarda en la llave hash correspondiente
    #elif (valor not in TablaHash[LlaveHash]) and existe:
        #TablaHash[LlaveHash].append((str(llave)+str(1),valor))

    return TablaHash

def main():
    global TablaHash,directorio

    TablaHash = [[] for i in range(100)]
    directorio = {}
    datos = stdin.readline().strip().split()

    while datos != []:

        print(Insertar(datos[0],datos[1]))
        print(EncontrarHash(datos[0]))
        print()
        print(Directorio(datos[0],datos[1]))
        print(EncontrarDirectorio(datos[0]))
        datos = stdin.readline().strip().split()

main()
    

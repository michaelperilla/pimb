from sys import stdin
import heapq as h
#Kruskall inicio
def fpadre(x):
    global padre
    if x != padre[x]:
        padre[x] = fpadre(padre[x])
    return padre[x]
def union(x,y):
    global padre,rank
    padrex = fpadre(x)
    padrey = fpadre(y)
    if padrex != padrey:
        if rank[padrex] > rank[padrey]:
            padre[padrey]=padrex
            rank[padrex] +=1
        else:
            padre[padrex]=padrey
            rank[padrey] +=1
        return True
    return False
def Kruskall(ady):
    res = []
    for arco in ady:
        if union(arco[1],arco[2]):
            res.append(arco)
    return res
#kruskall fin
#dijkstra inicio
def dijkstra(ady,inicio,n,final):
    visited = [False for i in range(n)]
    distancias = [float('inf') for i in range(n)]
    distancias[inicio] = 0
    cola = []
    h.heapify(cola)
    caminos = 0
    h.heappush(cola,(0,inicio,caminos))
    rta = 0
    while len(cola) != 0:
        extractmin = h.heappop(cola)
        pesnod = extractmin[0]
        nodo = extractmin[1]
        caminos = extractmin[2]
        if not visited[nodo]:
            visited[nodo] = True
            if nodo == final:
                rta= caminos
                break
        for j in ady[nodo]:
            peso = j[0]
            fin = j[2]
            if distancias[fin] > peso+pesnod:
                if peso > caminos:
                    caminos = peso
                distancias[fin] = peso+pesnod
                h.heappush(cola,(distancias[fin],fin,caminos))
    return rta
#dijkstra fin
def main():
    global padre,rank
    k = int(stdin.readline().strip())
    for z in range(k):
        nodos,conexiones = [int(_) for _ in stdin.readline().strip().split()]
        padre = [l for l in range(nodos+1)]
        rank = [0 for l in range(nodos+1)]
        ady = []
        for j in range(conexiones):
            inicio,final,peso = [int(_) for _ in stdin.readline().strip().split()]
            ady.append((peso,inicio-1,final-1))
        ady.sort()
        #Armo el grafo, haciendo un arbol de expancion minima
        grafo = Kruskall(ady)
        ady = [[] for l in range(nodos)]
        for i in grafo:
            ady[i[1]].append(i)
            ady[i[2]].append((i[0],i[2],i[1]))
        casos = int(stdin.readline().strip())
        print('Case',z+1)
        for i in range(casos):
            inicio,final = [int(_) for _ in stdin.readline().strip().split()]
            #Se ejecuta el camino mas largo
            x = dijkstra(ady,inicio-1,nodos,final-1)
            print(x)
        print()
            
        
        
            
main()
            

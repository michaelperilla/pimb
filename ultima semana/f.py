from sys import stdin
from collections import deque
def bellman(adj,lol):
    for i in range(lol-1):
        for x in adj:
            if dist[x[0]]+x[2] < dist[x[1]]:
                dist[x[1]]=dist[x[0]]+x[2]    
    for j in adj:
        if dist[j[0]]+j[2] < dist[j[1]]:
            return True
    return False
                            
def main():
    global dist
    casos=int(stdin.readline().strip())
    for i in range(casos):
        lol,holes=[int(x) for x in stdin.readline().strip().split()]
        dist=[float('inf') for i in range(lol)]
        adj=deque()
        dist[0]=0
        for j in range(holes):
            tripla=[int(x) for x in stdin.readline().strip().split()]
            adj.append(tripla)
        if bellman(adj,lol):
            print('possible')
        else:
            print('not possible')     
            
main()
            

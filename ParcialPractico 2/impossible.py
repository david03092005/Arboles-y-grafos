# David Alejandro Salazar Zuleta
# 8972690

from collections import deque
from sys import stdin
import sys

sys.setrecursionlimit(10 ** 6)

def main():
    global grafo, n, m
    linea = stdin.readline()
    while (linea.split()):
        grafo = []
        n, m = map(int, linea.split())
        leerEntrada()
        print(manejarCaso())
        linea = stdin.readline()


def leerEntrada():
    global grafo, n, m
    for nodos in range(n):
        grafo.append([])
    for conexiones in range(m):
        linea = stdin.readline().split()
        K = int(linea[0])
        if (K == 1):
            I = int(linea[1]) - 1
            J = int(linea[2]) - 1
            grafo[I].append(J)
        else:
            iterador = 1
            while (iterador < K):
                I = int(linea[iterador]) - 1
                iterador += 1
                J = int(linea[iterador]) - 1
                grafo[I].append(J)
                
            grafo[int(linea[K])-1].append(int(linea[1]) - 1)


def manejarCaso():
    global grafo, visitados, orden
    resultado = 'NO'
    visitados = []
    orden = [0]
    for nodo in range(len(grafo)):
        visitados.append(0)
    dfsR(0)
    if (0 not in visitados):
        grafo = reverse(grafo.copy())
        visitados.clear()
        for nodo in range(len(grafo)):
            visitados.append(0)
        dfsR(orden[0])
        if (0 not in visitados):
            resultado = 'YES'
    return resultado
        


# def dfs(ordenDfs):
#     cantidadComponentes = 0
#     for nodo in range(len(grafo)):
#         visitados.append(0)
    
#     i = 0
#     while (i < len(ordenDfs) and cantidadComponentes <= 1):
#     # for nodoAdyacente in ordenDfs:
#         nodoAdyacente = ordenDfs[i]
#         if (visitados[nodoAdyacente] == 0):
#             cantidadComponentes += 1
#             dfsR(nodoAdyacente)
#         i += 1

#     return cantidadComponentes


def dfsR(nodo):
    visitados[nodo] = 1
    for nodoAdyacente in grafo[nodo]:
        if (visitados[nodoAdyacente] == 0):
            dfsR(nodoAdyacente)
    orden[0] = nodo


def reverse(G):
    ans = [ list() for _ in G ]
    for u in range(len(G)):
        for v in G[u]:
            ans[v].append(u)
    return ans


main()
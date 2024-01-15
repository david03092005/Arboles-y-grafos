# David Alejandro Salazar Zuleta
# 8972690

from collections import deque
from sys import stdin
import sys

sys.setrecursionlimit(10 ** 6)

def main():
    global Caso, visitados, orden
    Caso = []
    Caso = leerEntrada()
    while (Caso != deque()):
        visitados = deque()
        orden = deque()
        respuesta = 0
        if (comprobarConectividad() == 1):
            respuesta = 1
        print(respuesta)
        Caso = leerEntrada()


def leerEntrada():
    grafo = deque()
    n, m = map(int, stdin.readline().split())
    for n in range(n):
        grafo.append(deque())
    for conexiones in range(m):
        nodo1, nodo2, direccion = map(int, stdin.readline().split())
        nodo1 -= 1
        nodo2 -= 1
        if (direccion == 1):
            grafo[nodo1].append(nodo2)
        elif (direccion == 2):
            grafo[nodo1].append(nodo2)
            grafo[nodo2].append(nodo1)

    return grafo


def comprobarConectividad():
    global Caso
    dfs(range(len(Caso)))
    Caso = reverse(Caso)
    visitados.clear()
    return dfs(orden.copy())


def dfs(ordenDfs):
    cantidadComponentes = 0
    for nodo in range(len(Caso)):
        visitados.append(0)
    
    for nodoAdyacente in ordenDfs:
        if (visitados[nodoAdyacente] == 0):
            cantidadComponentes += 1
            dfsR(nodoAdyacente)

    return cantidadComponentes


def dfsR(nodo):
    visitados[nodo] = 1
    for nodoAdyacente in Caso[nodo]:
        if (visitados[nodoAdyacente] == 0):
            dfsR(nodoAdyacente)
    orden.appendleft(nodo)


def reverse(G):
    ans = [ list() for _ in G ]
    for u in range(len(G)):
        for v in G[u]:
            ans[v].append(u)
    return ans


main()
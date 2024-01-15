# David Alejandro Salazar Zuleta
# 8972690

from collections import deque
from sys import stdin

import sys

sys.setrecursionlimit(10 ** 6)

def main():
    global Caso
    Caso = []
    numCasos = int(stdin.readline())
    for num in range(numCasos):
        Caso = leerEntrada()
        cactus = 'NO'
        if (comprobarFConexo() == True):
            cactus = 'YES'

        print(cactus)


def leerEntrada():
    global n
    grafo = []
    n, m = int(stdin.readline()), int(stdin.readline())
    for n in range(n):
        grafo.append([])
    for conexion in range(m):
        nodo1, nodo2 = map(int, stdin.readline().split())
        grafo[nodo1].append(nodo2)

    return grafo


def comprobarFConexo():
    global visitados, cicloSimple, orden, Caso
    visitados = deque()
    cicloSimple = deque()
    orden = deque()
    visitados.append(-1)
    for nodo in range(n):
        visitados.append(0)
    fuertementeConexo = True
    fuertementeConexo = dfs(0, Caso, True)
    if (0 in visitados):
        fuertementeConexo = False
    else:
        TGrafo = reverse(Caso)
        if (dfsComprobar(orden.copy(), TGrafo) > 1):
            fuertementeConexo =  False

    return fuertementeConexo


def dfsComprobar(ordenDfs, grafo):
    cantidadComponentes = 0
    for nodo in range(len(visitados)):
        visitados[nodo] = 0

    for nodoAdyacente in ordenDfs:
        if (visitados[nodoAdyacente] == 0):
            cantidadComponentes += 1
            dfs(nodoAdyacente, grafo, False)
    
    return cantidadComponentes


def dfs(numNodo, grafo, comprobar):
    conexion = True
    visitados[numNodo] += 1
    cicloSimple.append(numNodo)
    n = 0
    while (n < len(grafo[numNodo]) and conexion == True):
        numNodoAdyacente = grafo[numNodo][n]
        if (numNodoAdyacente == 0 and comprobar == True):
            visitados[numNodoAdyacente] += 1
        elif (visitados[numNodoAdyacente] == 0):
            conexion = dfs(numNodoAdyacente, grafo, comprobar)
        else:
            if (numNodoAdyacente not in cicloSimple and comprobar == True):
                conexion = False
        n += 1

    orden.appendleft(numNodo)
    cicloSimple.pop()
    return conexion


def reverse(G):
    ans = [ list() for _ in G ]
    for u in range(len(G)):
        for v in G[u]:
            ans[v].append(u)
    return ans

main()

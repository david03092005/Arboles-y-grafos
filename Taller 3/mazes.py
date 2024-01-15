# David Alejandro Salazar Zuleta
# 8972690

from collections import deque
from sys import stdin
import sys

sys.setrecursionlimit(10 ** 6)


def main():
    global grafo, casos, visitados, low, padre, tiempo, puentes, componentes
    grafo = deque()
    casos = deque()
    componentes = deque()
    visitados = deque()
    low = deque()
    padre = deque()
    leerEntrada()
    while (len(grafo) > 0):
        puentes = set()
        manejarCasos()
        grafo = deque()
        casos = deque()
        componentes = deque()
        visitados = deque()
        low = deque()
        padre = deque()
        leerEntrada()


def leerEntrada():
    n, m, k = map(int, stdin.readline().split())
    for n in range(n):
        grafo.append(deque())
        visitados.append(0)
        low.append(-1)
        padre.append(-1)
    for conexiones in range(m):
        nodo1, nodo2 = map(int, stdin.readline().split())
        nodo1 -= 1
        nodo2 -= 1
        grafo[nodo1].append(nodo2)
        grafo[nodo2].append(nodo1)
    for posCasos in range(k):
        nodo1, nodo2 = map(int, stdin.readline().split())
        nodo1 -= 1
        nodo2 -= 1
        casos.append((nodo1, nodo2))


def manejarCasos():
    global visitadosCopia, caminoActual, puentes, tiempo, caminoFinal
    visitadosCopia = list(visitados)
    tiempo = 0
    for nodo in range(len(grafo)):
        if (visitadosCopia[nodo] == 0): 
            puentesTarjan(nodo)
    for nodo in range(len(grafo)):
        if (visitados[nodo] == 0):
            dfs(nodo, nodo+1)
    for caso in casos:
        if (visitados[caso[0]] == visitados[caso[1]] and visitados[caso[0]] != 0):
            print('Y')
        else:
            print('N')
    print('-')


def puentesTarjan(nodo):
    global visitadosCopia, low, padre, tiempo
    tiempo += 1
    visitadosCopia[nodo] = low[nodo] = tiempo

    for nodoAdyacente in grafo[nodo]:
        if (visitadosCopia[nodoAdyacente] == 0):
            padre[nodoAdyacente] = nodo
            puentesTarjan(nodoAdyacente)
            low[nodo] = min(low[nodo], low[nodoAdyacente])

            if (low[nodoAdyacente] > visitadosCopia[nodo]):
                puentes.add((nodo, nodoAdyacente))
                puentes.add((nodoAdyacente, nodo))
        
        elif (nodoAdyacente != padre[nodo]):
            low[nodo] = min(low[nodo], visitadosCopia[nodoAdyacente])


def dfs(nodo, numComponente):
    global visitados
    visitados[nodo] = numComponente
    for nodoAdyacente in grafo[nodo]:
        if (visitados[nodoAdyacente] == 0 and (nodo, nodoAdyacente) in puentes):
            dfs(nodoAdyacente, numComponente)


main()
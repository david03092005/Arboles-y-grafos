# David Alejandro Salazar Zuleta
# 8972690

from collections import deque
from sys import stdin
import sys

sys.setrecursionlimit(10 ** 6)

def main():
    global grafo, N
    casos = int(stdin.readline())
    for caso in range(casos):
        grafo = []
        leerEntrada()
        manejarCaso()


def leerEntrada():
    global grafo, N
    stdin.readline()
    N = int(stdin.readline())
    for i in range(N):
        grafo.append([])
    for i in range(N):
        linea = stdin.readline().split()
        cantidadEnemigos = int(linea[0])
        while (cantidadEnemigos > 0):
            nodoEnemigo = int(linea[cantidadEnemigos]) - 1
            if (nodoEnemigo < N):
                grafo[i].append(nodoEnemigo)
                grafo[nodoEnemigo].append(i)
            cantidadEnemigos -= 1


def manejarCaso():
    global grafo, tiempo, visitados, padres, cantidades
    cantidadesTotal = 0
    visitados = []
    padres = []
    for v in range(len(grafo)):
        visitados.append(-1)
        padres.append(-1)
    
    for nodos in range(len(grafo)):
        if (visitados[nodos] == -1):
            cantidades = [0, 0]
            tiempo = 0
            propiedad = dfsR(nodos, tiempo, True)
            if (propiedad != False):
                cantidadesTotal += max(cantidades)
    
    print(cantidadesTotal)
    

def dfsR(nodo, tiempo, propiedad):
    componente = tiempo % 2
    visitados[nodo] = componente
    cantidades[componente] += 1
    for nodosAdyacentes in grafo[nodo]:
        if (visitados[nodosAdyacentes] == -1):
            padres[nodosAdyacentes] = nodo
            propiedad = dfsR(nodosAdyacentes, tiempo+1, propiedad)
        else:
            if (visitados[nodo] == visitados[nodosAdyacentes]):
                propiedad = False
    return propiedad


main()
# David Alejandro Salazar Zuleta
# 8972690

from sys import stdin
import sys
import heapq

sys.setrecursionlimit(10 ** 6)


def main():
    global grafo, estaciones, distanciaInicial
    n = int(stdin.readline())
    stdin.readline()
    for caso in range(n):
        grafo = []
        estaciones = []
        leerEntrada()
        distanciaInicial =  dijkstra(list(estaciones))
        print(buscarPosibleEstacion() + 1)
        if (caso != n-1):
            print()


def leerEntrada():
    cantidadEstaciones, cantidadNodos = map(int, stdin.readline().split())
    for nodos in range(cantidadNodos):
        grafo.append([])

    for e in range(cantidadEstaciones):
        estacion = int(stdin.readline())
        estaciones.append((0, estacion - 1))
    
    linea = stdin.readline()
    while (linea.split()):
        nodou, nodov, peso = map(int, linea.split())
        nodou -= 1
        nodov -= 1
        grafo[nodou].append((nodov, peso))
        grafo[nodov].append((nodou, peso))
        linea = stdin.readline()


def dijkstra(colaNodos):
    distancias = []
    for d in range(len(grafo)):
        if((0, d) in colaNodos):
            distancias.append(0)
        else:
            distancias.append(float('inf'))

    while(colaNodos):
        dNodo, nodo = heapq.heappop(colaNodos)
        if (distancias[nodo] == dNodo):
            for nodoAdyacente, dNodoAdyacente in grafo[nodo]:
                if (dNodo + dNodoAdyacente < distancias[nodoAdyacente]):
                    distancias[nodoAdyacente] = dNodo + dNodoAdyacente
                    heapq.heappush(colaNodos, (distancias[nodoAdyacente], nodoAdyacente))

    return distancias


def buscarPosibleEstacion():
    global cantidadMejorada
    cantidadGrande = max(distanciaInicial)
    mejorNodo = 0
    for n in range(len(grafo)):
        if((0, n) not in estaciones):
            cantidadMejorada = 0
            maximo = dijkstraModificado(n)
            if (cantidadGrande > maximo):
                cantidadGrande = maximo
                mejorNodo = n
    
    return mejorNodo


def dijkstraModificado(nodo):
    global cantidadMejorada
    colaNodos = [(0, nodo)]
    distanciaActual = list(distanciaInicial)
    distanciaActual[nodo] = 0
    cantidadMejorada += distanciaInicial[nodo]
    
    while(colaNodos):
        dNodo, nodo = heapq.heappop(colaNodos)
        if (distanciaActual[nodo] == dNodo):
            for nodoAdyacente, dNodoAdyacente in grafo[nodo]:
                if (dNodo + dNodoAdyacente < distanciaActual[nodoAdyacente]):
                    cantidadMejorada += (distanciaInicial[nodoAdyacente] - (dNodo + dNodoAdyacente))
                    distanciaActual[nodoAdyacente] = dNodo + dNodoAdyacente
                    heapq.heappush(colaNodos, (distanciaActual[nodoAdyacente], nodoAdyacente))
    return max(distanciaActual)


main()
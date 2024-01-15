# David Alejandro Salazar Zuleta
# 8972690

from sys import stdin
import sys
import heapq

sys.setrecursionlimit(10 ** 6)


def main():
    global grafo, nodos, caminos, caminoImposible
    linea = stdin.readline()
    while (linea.split()):
        grafo = []
        nodos, caminos, jefe, oficina, casa, mercado = map(int, linea.split())
        leerEntrada()
        if (casa == oficina or casa == jefe or mercado == oficina or mercado == jefe):
            print('MISSION IMPOSSIBLE.')
        else:
            caminoImposible = [False] * len(grafo)
            buscarCaminoImposible(jefe - 1, oficina - 1)
            buscarCamino(casa - 1, mercado - 1)
        
        linea = stdin.readline()


def leerEntrada():
    for n in range(nodos):
        grafo.append([])

    for c in range(caminos):
        nodou, nodov, peso = map(int, stdin.readline().split())
        nodou -= 1
        nodov -= 1
        grafo[nodou].append((nodov, peso))
        grafo[nodov].append((nodou, peso))


def buscarCaminoImposible(nodoInicio, nodoFinal):
    predecesores = dijkstra(nodoInicio, nodoFinal, False)
    bloquearCamino(predecesores, nodoFinal)


def bloquearCamino(predecesores, nodo):
    caminoImposible[nodo] = True
    for nodoAdyacente in predecesores[nodo]:
        bloquearCamino(predecesores, nodoAdyacente)


def buscarCamino(nodoInicio, nodoFinal):
    respuesta = 'MISSION IMPOSSIBLE.'
    if (not caminoImposible[nodoInicio]):
        distanciaCamino = dijkstra(nodoInicio, nodoFinal, True)
        if (distanciaCamino != float('inf')):
            respuesta = distanciaCamino
    
    print(respuesta)


def dijkstra(nodoInicio, NodoFinal, buscar):
    distancias = [float('inf')] * len(grafo)
    predecesor = [[]] * len(grafo)
    distancias[nodoInicio] = 0
    colaNodos = [(0, nodoInicio)]

    while(colaNodos):
        dNodo, nodo = heapq.heappop(colaNodos)
        if (nodo != NodoFinal and distancias[nodo] == dNodo):
            for nodoAdyacente, dNodoAdyacente in grafo[nodo]:
                if (dNodo + dNodoAdyacente < distancias[nodoAdyacente]):
                    if (not buscar or not caminoImposible[nodoAdyacente]):
                        distancias[nodoAdyacente] = dNodo + dNodoAdyacente
                        predecesor[nodoAdyacente] = [nodo]
                        heapq.heappush(colaNodos, (distancias[nodoAdyacente], nodoAdyacente))
                elif (dNodo + dNodoAdyacente == distancias[nodoAdyacente]):
                    predecesor[nodoAdyacente].append(nodo)

    salida = predecesor
    if (buscar):
        salida = distancias[NodoFinal]
        
    return salida


main()
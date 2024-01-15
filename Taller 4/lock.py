# David Alejandro Salazar Zuleta
# 8972690

from sys import stdin
import sys
import heapq

sys.setrecursionlimit(10 ** 6)

def main():
    global grafo
    casos = int(stdin.readline())
    for caso in range(casos):
        grafo = []
        leerEntrada()
        distancias = prim()
        print(sum(distancias))


def leerEntrada():
    global colaNodos
    caso = stdin.readline().split()
    cantidadNodos = int(caso[0])
    colaNodos = [(float('inf'), 0)]
    for i in range(cantidadNodos):
        grafo.append([])
        movimientos =  encontrarDistancia("0000", caso[i + 1])
        if (movimientos < colaNodos[0][0]):
            colaNodos = [(movimientos, i)]

    for numNodo in range(cantidadNodos):
        posicionNodo = caso[numNodo + 1]
        for numConexiones in range(numNodo + 1, cantidadNodos):
            posicionCercano = caso[numConexiones + 1]
            cambios = encontrarDistancia(posicionCercano, posicionNodo)
            grafo[numNodo].append((numConexiones, cambios))
            grafo[numConexiones].append((numNodo, cambios))


def encontrarDistancia(primeraContraseña, segundaContraseña):
    cambios = 0
    for letra in range(len(primeraContraseña)):
        if (primeraContraseña[letra] != segundaContraseña[letra]):
            num1 = int(primeraContraseña[letra])
            num2 = int(segundaContraseña[letra])
            distancia = abs(num1 - num2)
            if (distancia <= 5):
                cambios += distancia
            else:
                distancia = abs(distancia - 10)
                cambios += distancia
    
    return cambios


def prim():
    visitados = [False] * len(grafo)
    distancias = [float('inf')] * len(grafo)
    distancias[colaNodos[0][1]] = colaNodos[0][0]

    while(colaNodos):
        dNodo, nodo = heapq.heappop(colaNodos)
        visitados[nodo] = True
        if (distancias[nodo] == dNodo):
            for nodoAdyacente, dNodoAdyacente in grafo[nodo]:
                if (dNodoAdyacente < distancias[nodoAdyacente] and not visitados[nodoAdyacente]):
                    distancias[nodoAdyacente] = dNodoAdyacente
                    heapq.heappush(colaNodos, (distancias[nodoAdyacente], nodoAdyacente))

    return distancias

main()
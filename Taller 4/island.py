# David Alejandro Salazar Zuleta
# 8972690

from sys import stdin
import sys
import heapq

sys.setrecursionlimit(10 ** 6)

def main():
    global grafo, habitantes
    linea = int(stdin.readline())
    contador = 0
    while (linea != 0):
        contador += 1
        grafo = []
        habitantes = []
        leerEntrada(linea)
        tiempo = calcularPromedio()
        print('Island Group:', contador, end=' ')
        print('Average', tiempo)
        print()
        linea = int(stdin.readline())


def leerEntrada(cantidadNodos):
    posiciones = []
    for nodos in range(cantidadNodos):
        grafo.append([])
    
    for nodo in range(cantidadNodos):
        entrada = stdin.readline().split()
        for num in range(3):
            entrada[num] = int(entrada[num])
        posiciones.append(entrada[0:2])
        habitantes.append(entrada[2])

    for numNodo in range(cantidadNodos):
        posicionNodo = posiciones[numNodo]
        for numConexiones in range(numNodo+1, cantidadNodos):
            posicionCercano = posiciones[numConexiones]
            distancia = (((posicionCercano[0] - posicionNodo[0])**2) + ((posicionCercano[1] - posicionNodo[1])**2))**0.5
            grafo[numNodo].append((numConexiones, distancia))
            grafo[numConexiones].append((numNodo, distancia))


def prim():
    visitados = [False] * len(grafo)
    distancias = [float('inf')] * len(grafo)
    predecesores = [-1] * len(grafo)
    distancias[0] = 0
    colaNodos = []
    heapq.heappush(colaNodos, (0, 0))

    while(colaNodos):
        dNodo, nodo = heapq.heappop(colaNodos)
        visitados[nodo] = True
        if (distancias[nodo] == dNodo):
            for nodoAdyacente, dNodoAdyacente in grafo[nodo]:
                if (dNodoAdyacente < distancias[nodoAdyacente] and not visitados[nodoAdyacente]):
                    distancias[nodoAdyacente] = dNodoAdyacente
                    predecesores[nodoAdyacente] = nodo
                    heapq.heappush(colaNodos, (distancias[nodoAdyacente], nodoAdyacente))

    return distancias, predecesores


def calcularPromedio():
    distancias, predecesores = prim()
    sumatoria1 = 0
    sumatoria2 = habitantes[0]
    for i in range(1, len(grafo)):
        pesoAristaMaxima = distancias[i]
        predecesor = predecesores[i]
        while (predecesor != -1):
            if (distancias[predecesor] > pesoAristaMaxima):
                pesoAristaMaxima = distancias[predecesor]
            predecesor = predecesores[predecesor]
        sumatoria1 += (pesoAristaMaxima * habitantes[i])
        sumatoria2 += habitantes[i]

    resultado = round(sumatoria1/sumatoria2, 2)
    resultado = "{:.2f}".format(resultado)
    return (resultado)


main()
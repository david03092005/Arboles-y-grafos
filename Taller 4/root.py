# David Alejandro Salazar Zuleta
# 8972690

from sys import stdin
from collections import deque
import sys
import heapq

sys.setrecursionlimit(10 ** 6)

def main():
    global arbol, mejoresRaices, peoresRaices
    linea = stdin.readline()
    while (linea.split()):
        cantidadNodos = int(linea)
        arbol = []
        leerEntrada(cantidadNodos)
        mejoresRaices = []
        peoresRaices = set()
        centro()
        for c in mejoresRaices:
            conjunto = buscarPeoresRaices(c - 1, cantidadNodos)
            peoresRaices = peoresRaices.union(conjunto)
        print('Best Roots  :', *mejoresRaices)
        peoresRaices = list(peoresRaices)
        peoresRaices.sort()
        print('Worst Roots :', *peoresRaices)
        linea = stdin.readline()
    

def leerEntrada(nodos):
    for n in range(nodos):
        arbol.append([])

    for n in range(nodos):
        conexiones = stdin.readline().split()
        numeroConexiones = int(conexiones[0])
        conexiones = conexiones[1::]
        for c in range(numeroConexiones):
            arbol[n].append(int(conexiones[c]) - 1)


def centro():
    global mejoresRaices
    nivelMax = 0
    nivel = [0 for _ in range(len(arbol))]
    grado = [len(arbol[v]) for v in range(len(arbol))]
    queue = deque()

    for i in range(len(arbol)):
        if grado[i] == 1:
            queue.append(i)

    while len(queue) > 0:
        v = queue.popleft()
        for w in arbol[v]:
            grado[w] -= 1
            if grado[w] == 1:
                queue.append(w)
                nivel[w] = nivel[v] + 1
                nivelMax = max(nivelMax, nivel[w])
    for i in range(len(arbol)):
        if nivel[i] == nivelMax:
            heapq.heappush(mejoresRaices, i + 1)


def buscarPeoresRaices(raiz, cantidadNodos):
    altura = 0
    alturaConjunto = 0
    visitados = []
    cola = deque()
    conjuntoHojas = []
    for nodos in range(cantidadNodos):
        visitados.append(0)

    cola.append((altura, raiz))
    visitados[raiz] = 1

    while(cola):
        altura, nodo = cola.popleft()
        altura += 1
        if (len(arbol[nodo]) == 1):
            nodoAdyacente = arbol[nodo][0]
            if(nodo in arbol[nodoAdyacente]):
                if (altura == alturaConjunto):
                    conjuntoHojas.add(nodo+1)
                elif (altura > alturaConjunto):
                    alturaConjunto = altura
                    conjuntoHojas = set()
                    conjuntoHojas.add(nodo+1)
        else:
            for nodoAdyacente in arbol[nodo]:
                if (visitados[nodoAdyacente] == 0):
                    cola.append((altura, nodoAdyacente))
                    visitados[nodoAdyacente] = 1

    return conjuntoHojas


main()
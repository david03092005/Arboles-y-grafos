# David Alejandro Salazar Zuleta
# 8972690

from collections import deque
from sys import stdin
import sys

sys.setrecursionlimit(10 ** 6)


def main():
    global Caso, visitados, tiempo, n, tiempoLow, padre, puntosArticulacion, m, nodosUsados
    Caso = []
    Caso = leerEntrada()
    while (Caso != deque()):
        puntosArticulacion = set()
        nodosUsados = set()
        buscarPuntosDeArticulacion()
        puntosArticulacion = sorted(list(puntosArticulacion), key=lambda tupla: (-tupla[1], tupla[0]))
        nodo = 0
        while (len(nodosUsados) < m):
            if (nodo not in nodosUsados):
                nodosUsados.add(nodo)
                puntosArticulacion.append((nodo, 1))
            nodo += 1
        
        for bombas in range(m):
            print(puntosArticulacion[bombas][0], puntosArticulacion[bombas][1])
        
        print()
        Caso = leerEntrada()


def leerEntrada():
    global m
    grafo = deque()
    n, m = map(int, stdin.readline().split())
    if (n >= 3):
        for n in range(n):
            grafo.append(deque())
        nodo1 = 0
        nodo2 = 0 
        while (nodo1 != -1 and nodo2 != -1):
            nodo1, nodo2 = map(int, stdin.readline().split())
            grafo[nodo1].append(nodo2)
            grafo[nodo2].append(nodo1)
    return grafo


def buscarPuntosDeArticulacion():
    global Caso, visitados, tiempo, n, tiempoLow, padre, puntosArticulacion
    tiempo = 0
    n = len(Caso)
    visitados = []
    tiempoLow = []
    padre = []
    for menos1 in range(n):
        visitados.append(-1)
        tiempoLow.append(-1)
        padre.append(-1)
    
    for numNodo in range(n):
        if (visitados[numNodo] == -1):
            tarjanAP(numNodo)


def tarjanAP(numNodo):
    global Caso, visitados, tiempo, n, tiempoLow, padre, puntosArticulacion
    numHijos = 0
    tiempo += 1
    visitados[numNodo] = tiempo
    tiempoLow[numNodo] = tiempo

    for nodoAdyacente in Caso[numNodo]:
        if (visitados[nodoAdyacente] == -1):
            numHijos += 1
            padre[nodoAdyacente] = numNodo
            tarjanAP(nodoAdyacente)
            tiempoLow[numNodo] = min(tiempoLow[numNodo], tiempoLow[nodoAdyacente])
            if (padre[numNodo] != -1 and tiempoLow[nodoAdyacente] >= visitados[numNodo]):
                cantidadComponentes = cantidadComponentesConexos(numNodo)
                puntosArticulacion.add((numNodo, cantidadComponentes))
                nodosUsados.add(numNodo)
        elif (nodoAdyacente != padre[numNodo]):
            tiempoLow[numNodo] = min(tiempoLow[numNodo], visitados[nodoAdyacente])

    if (padre[numNodo] == -1 and numHijos > 1):
        cantidadComponentes = cantidadComponentesConexos(numNodo)
        puntosArticulacion.add((numNodo, cantidadComponentes))
        nodosUsados.add(numNodo)


def cantidadComponentesConexos(numNodo):
    cantidadComponentes = 0
    visitadosComponentes = []
    for nodo in range(len(Caso)):
        if (nodo == numNodo):
            visitadosComponentes.append(-1)
        else:
            visitadosComponentes.append(0)
    
    for nodo in range(len(Caso)):
        if (visitadosComponentes[nodo] == 0):
            cantidadComponentes += 1
            dfs(nodo, visitadosComponentes)
    
    return cantidadComponentes


def dfs(numNodo, listaVisitados):
    listaVisitados[numNodo] = 1

    for nodoAdyacente in Caso[numNodo]:
        if (listaVisitados[nodoAdyacente] == 0):
            dfs(nodoAdyacente, listaVisitados)


main()
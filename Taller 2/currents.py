from collections import deque
from sys import stdin
import heapq


def leerEntrada():
    global matriz, casos
    casos = deque()
    matriz = deque()
    tamañoMatriz = str(stdin.readline()).split()
    for i in range(int(tamañoMatriz[0])):
        matriz.append(deque())
        linea = str(stdin.readline()).strip()
        for num in range(0, len(linea), 1):
            segmento = linea[num:num + 1]
            matriz[i].append(int(segmento))

    cantCasos = int(stdin.readline())
    for i in range(cantCasos):
        linea = str(stdin.readline()).split()
        linea = list(map(int, linea))
        casos.append(linea)
    
    crearMatrizConPesos(int(tamañoMatriz[0]), int(tamañoMatriz[1]))


def crearMatrizConPesos(filasMatriz, columnasMatriz):
    global grafo
    grafo = {}
    for fila in range(filasMatriz):
        for columna in range(columnasMatriz):
            nodo = (fila, columna)
            direccionCorriente = matriz[fila][columna]
            conexiones = crearConexiones(direccionCorriente, filasMatriz-1, columnasMatriz-1, fila, columna)
            grafo[nodo] = conexiones


def crearConexiones(corriente, filasMatriz, columnasMatriz, fila, columna):
    conexiones = []
    if (corriente == 0):
        if (fila != 0):
            conexiones.append([(fila-1, columna), 0])
        if (fila != 0 and columna != columnasMatriz):
            conexiones.append([(fila-1, columna+1), 1])
        if (columna != columnasMatriz):
            conexiones.append([(fila, columna+1), 1])
        if(columna != columnasMatriz and fila != filasMatriz):
            conexiones.append([(fila+1, columna+1), 1])
        if (fila != filasMatriz):
            conexiones.append([(fila+1, columna), 1])
        if (fila != filasMatriz and columna != 0):
            conexiones.append([(fila+1, columna-1), 1])
        if (columna != 0):
            conexiones.append([(fila, columna-1), 1])
        if (columna != 0 and fila != 0):
            conexiones.append([(fila-1, columna-1), 1])
    elif (corriente == 1):
        if (fila != 0):
            conexiones.append([(fila-1, columna), 1])
        if (fila != 0 and columna != columnasMatriz):
            conexiones.append([(fila-1, columna+1), 0])
        if (columna != columnasMatriz):
            conexiones.append([(fila, columna+1), 1])
        if(columna != columnasMatriz and fila != filasMatriz):
            conexiones.append([(fila+1, columna+1), 1])
        if (fila != filasMatriz):
            conexiones.append([(fila+1, columna), 1])
        if (fila != filasMatriz and columna != 0):
            conexiones.append([(fila+1, columna-1), 1])
        if (columna != 0):
            conexiones.append([(fila, columna-1), 1])
        if (columna != 0 and fila != 0):
            conexiones.append([(fila-1, columna-1), 1])
    elif (corriente == 2):
        if (fila != 0):
            conexiones.append([(fila-1, columna), 1])
        if (fila != 0 and columna != columnasMatriz):
            conexiones.append([(fila-1, columna+1), 1])
        if (columna != columnasMatriz):
            conexiones.append([(fila, columna+1), 0])
        if(columna != columnasMatriz and fila != filasMatriz):
            conexiones.append([(fila+1, columna+1), 1])
        if (fila != filasMatriz):
            conexiones.append([(fila+1, columna), 1])
        if (fila != filasMatriz and columna != 0):
            conexiones.append([(fila+1, columna-1), 1])
        if (columna != 0):
            conexiones.append([(fila, columna-1), 1])
        if (columna != 0 and fila != 0):
            conexiones.append([(fila-1, columna-1), 1])
    elif (corriente == 3):
        if (fila != 0):
            conexiones.append([(fila-1, columna), 1])
        if (fila != 0 and columna != columnasMatriz):
            conexiones.append([(fila-1, columna+1), 1])
        if (columna != columnasMatriz):
            conexiones.append([(fila, columna+1), 1])
        if(columna != columnasMatriz and fila != filasMatriz):
            conexiones.append([(fila+1, columna+1), 0])
        if (fila != filasMatriz):
            conexiones.append([(fila+1, columna), 1])
        if (fila != filasMatriz and columna != 0):
            conexiones.append([(fila+1, columna-1), 1])
        if (columna != 0):
            conexiones.append([(fila, columna-1), 1])
        if (columna != 0 and fila != 0):
            conexiones.append([(fila-1, columna-1), 1])
    elif (corriente == 4):
        if (fila != 0):
            conexiones.append([(fila-1, columna), 1])
        if (fila != 0 and columna != columnasMatriz):
            conexiones.append([(fila-1, columna+1), 1])
        if (columna != columnasMatriz):
            conexiones.append([(fila, columna+1), 1])
        if(columna != columnasMatriz and fila != filasMatriz):
            conexiones.append([(fila+1, columna+1), 1])
        if (fila != filasMatriz):
            conexiones.append([(fila+1, columna), 0])
        if (fila != filasMatriz and columna != 0):
            conexiones.append([(fila+1, columna-1), 1])
        if (columna != 0):
            conexiones.append([(fila, columna-1), 1])
        if (columna != 0 and fila != 0):
            conexiones.append([(fila-1, columna-1), 1])
    elif (corriente == 5):
        if (fila != 0):
            conexiones.append([(fila-1, columna), 1])
        if (fila != 0 and columna != columnasMatriz):
            conexiones.append([(fila-1, columna+1), 1])
        if (columna != columnasMatriz):
            conexiones.append([(fila, columna+1), 1])
        if(columna != columnasMatriz and fila != filasMatriz):
            conexiones.append([(fila+1, columna+1), 1])
        if (fila != filasMatriz):
            conexiones.append([(fila+1, columna), 1])
        if (fila != filasMatriz and columna != 0):
            conexiones.append([(fila+1, columna-1), 0])
        if (columna != 0):
            conexiones.append([(fila, columna-1), 1])
        if (columna != 0 and fila != 0):
            conexiones.append([(fila-1, columna-1), 1])
    elif (corriente == 6):
        if (fila != 0):
            conexiones.append([(fila-1, columna), 1])
        if (fila != 0 and columna != columnasMatriz):
            conexiones.append([(fila-1, columna+1), 1])
        if (columna != columnasMatriz):
            conexiones.append([(fila, columna+1), 1])
        if(columna != columnasMatriz and fila != filasMatriz):
            conexiones.append([(fila+1, columna+1), 1])
        if (fila != filasMatriz):
            conexiones.append([(fila+1, columna), 1])
        if (fila != filasMatriz and columna != 0):
            conexiones.append([(fila+1, columna-1), 1])
        if (columna != 0):
            conexiones.append([(fila, columna-1), 0])
        if (columna != 0 and fila != 0):
            conexiones.append([(fila-1, columna-1), 1])
    elif (corriente == 7):
        if (fila != 0):
            conexiones.append([(fila-1, columna), 1])
        if (fila != 0 and columna != columnasMatriz):
            conexiones.append([(fila-1, columna+1), 1])
        if (columna != columnasMatriz):
            conexiones.append([(fila, columna+1), 1])
        if(columna != columnasMatriz and fila != filasMatriz):
            conexiones.append([(fila+1, columna+1), 1])
        if (fila != filasMatriz):
            conexiones.append([(fila+1, columna), 1])
        if (fila != filasMatriz and columna != 0):
            conexiones.append([(fila+1, columna-1), 1])
        if (columna != 0):
            conexiones.append([(fila, columna-1), 1])
        if (columna != 0 and fila != 0):
            conexiones.append([(fila-1, columna-1), 0])
    return conexiones


def dijkstra(inicio, objetivo):
    distancias = {nodo: float('inf') for nodo in grafo}
    distancias[inicio] = 0
    cola = [(0, inicio)]

    while (cola):
        distancia_actual, nodo_actual = heapq.heappop(cola)

        if (nodo_actual == objetivo):
            return distancias[objetivo]

        if (distancia_actual > distancias[nodo_actual]):
            continue

        for vecino, peso in grafo[nodo_actual]:
            distancia_nueva = distancia_actual + peso
            if (distancia_nueva < distancias[vecino]):
                distancias[vecino] = distancia_nueva
                heapq.heappush(cola, (distancia_nueva, vecino))

    return float('inf')


def main():
    leerEntrada()
    for i in casos:
        inicio = (i[0]-1, i[1]-1)
        final = (i[2]-1, i[3]-1)
        print(dijkstra(tuple(inicio), tuple(final)))

main()
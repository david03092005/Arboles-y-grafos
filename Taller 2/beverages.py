from collections import deque
from sys import stdin

def leerEntrada():
    linea = stdin.readline().strip()
    numCaso = 0
    while(linea != '\n'):
        comparaciones.append(deque())
        cantBebidas = int(linea)
        numYBebidas = dict()
        for num in range(cantBebidas):
            linea = str(stdin.readline()).strip()
            numYBebidas[linea] = num
        casos.append(numYBebidas)
        numComparaciones = int(stdin.readline())
        while(numComparaciones > 0):
            linea = str(stdin.readline()).split()
            comparacion = list()
            comparacion.append(numYBebidas[linea[0]])
            comparacion.append(numYBebidas[linea[1]])
            comparaciones[numCaso].append(comparacion)
            numComparaciones -= 1
        numCaso += 1
        ignorar = stdin.readline()
        linea = stdin.readline().strip()
        if not (linea):
            break


def main():
    global casos, comparaciones, orden
    casos = deque()
    comparaciones = deque()
    orden = deque()
    leerEntrada()

    for numCaso, conexiones in enumerate(comparaciones):
        grafoBebidas = deque()
        llegadasNodos = deque()
        orden = deque()
        bebidas = deque(casos[numCaso].keys())

        for i in range(len(casos[numCaso])):
            grafoBebidas.append(deque())
            llegadasNodos.append(0)
        
        for conexionNueva in conexiones:
            grafoBebidas[conexionNueva[0]].append(conexionNueva[1])
            llegadasNodos[conexionNueva[1]] += 1
        
        ordenTopologico(grafoBebidas, llegadasNodos, bebidas)
        print(f"Case #{numCaso+1}: Dilbert should drink beverages in this order:", end=" ")
        print(*orden, end=".\n")
        print()


def ordenTopologico(grafo, llegadas, nombreBebidas):
    comprobacion = False
    while (comprobacion == False):
        comprobacion = True
        for posicion, cantidadEntrante in enumerate(llegadas):
            if (cantidadEntrante == 0):
                llegadas[posicion] -= 1
                orden.append(nombreBebidas[posicion])
                for salidas in grafo[posicion]:
                    llegadas[salidas] -= 1
            elif(cantidadEntrante != -1):
                comprobacion = False



main()
from collections import deque
from sys import stdin

def leerEntrada():
    Nodos = deque()
    linea = int(stdin.readline())
    casos = 0
    while(linea != 0):
        cantNodos = linea
        x = 0
        y = 1
        linea = str(stdin.readline()).split()
        linea = list(map(int, linea))
        Nodos.append(deque())
        while(cantNodos > 0):
            Nodos[casos].append([linea[x], linea[y]])
            x += 2
            y += 2
            cantNodos -= 1
        linea = int(stdin.readline())    
        casos += 1
    return Nodos


def calcularDistancia():
    global nodosAlcanzados
    estacionesTotal = leerEntrada()
    numCasoTorre = 0
    for torres in estacionesTotal:
        nodosAlcanzados = set()
        intentoDFS(0, 0, torres, 1)
        if (len(nodosAlcanzados) == len(estacionesTotal[numCasoTorre])):
            print("All stations are reachable.")
        else: 
            print("There are stations that are unreachable.")
        numCasoTorre += 1   


def crearConexiones(nodo, torres):
    listaDistancias = deque()
    for posicionNodo, posibleNodo in enumerate(torres):
        if(nodo != posibleNodo):
            distancia = (nodo[0]-posibleNodo[0])**2 + (nodo[1]-posibleNodo[1])**2
            tuplaPrioridades = (distancia, posibleNodo[0], posibleNodo[1], posicionNodo)
            listaDistancias.append(tuplaPrioridades)
    listaDistancias = sorted(listaDistancias)

    if (len(listaDistancias) == 1):
        conexiones = [listaDistancias[0][-1], None]
    else:
        conexiones = [listaDistancias[0][-1], listaDistancias[1][-1]]
    
    return conexiones
    
def intentoDFS(nodoActual, nodoAVisitar, torres, cancelarPrimero):
    if not(nodoAVisitar in nodosAlcanzados):
        conexionesNodo = crearConexiones(torres[nodoAVisitar], torres)
        nodosAlcanzados.add(nodoAVisitar)
        intentoDFS(nodoActual , conexionesNodo[0], torres, 0)
        if (conexionesNodo[1] != None):
            intentoDFS(nodoActual, conexionesNodo[1], torres, 0)
    else:
        pass


calcularDistancia()
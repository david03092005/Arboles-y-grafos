from collections import deque
from sys import stdin

def leerEntrada():
    tiempoDeCorredores = deque()
    linea = str(stdin.readline()).split()
    i = 0
    while(len(linea) > 0):
        linea = list(map(int, linea))
        tiempoDeCorredores.append(linea)
        linea = str(stdin.readline()).split()
        i += 1
    return tiempoDeCorredores

def encontrarN():
    tiempoDeCorredores = leerEntrada()
    for i in tiempoDeCorredores:
        vuelta = i[1]/(i[1]-i[0])
        if vuelta % 1 != 0:
            vuelta = round(vuelta + 0.5)
        else:
            vuelta = round(vuelta)
        print(vuelta)

encontrarN()

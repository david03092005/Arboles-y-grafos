# David Alejandro Salazar Zuleta
# 8972690

from collections import deque
from sys import stdin


def main():
    global movimientos, matriz
    cantEntrada = int(stdin.readline())
    ignorar = stdin.readline()
    movimientos = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
    for i in range(cantEntrada):
        matriz = []
        fila = stdin.readline().strip()
        while (len(fila) != 0):
            matriz.append(list(fila))
            fila = stdin.readline().strip()
        cantFilas = len(matriz)
        cantColumnas = len(matriz[0])
        mancha = 0
        siguienteNodoConUno =  buscarUnos()
        while (siguienteNodoConUno != False):
            matriz[siguienteNodoConUno[0]][siguienteNodoConUno[1]] = '0'
            nuevaMancha = buscarManchaBFS(i, siguienteNodoConUno, cantColumnas, cantFilas) + 1
            if (nuevaMancha > mancha):
                mancha = nuevaMancha
            siguienteNodoConUno =  buscarUnos()
        print(mancha)
        if (i != cantEntrada-1):
            print()
        


def buscarManchaBFS(caso, nodo, cantColumnas, cantFilas):
    cantMancha = 0
    colaDeEspera = []
    colaDeEspera.append(nodo)
    while (colaDeEspera):
        nodo = colaDeEspera.pop()
        for movimientoFila, movimientoColumna in movimientos:
            nuevaFila = nodo[0] + movimientoFila
            nuevaColumna = nodo[1] + movimientoColumna
            if((nuevaFila < cantFilas and nuevaFila >= 0) and (nuevaColumna < cantColumnas and nuevaColumna >= 0)):
                if(matriz[nuevaFila][nuevaColumna] == '1'):
                    matriz[nuevaFila][nuevaColumna] = '0'
                    colaDeEspera.append((nuevaFila, nuevaColumna))
                    cantMancha += 1 
    return cantMancha


def buscarUnos():
    siguienteUno = False
    for fila in range(len(matriz)):
        for columna in range(len(matriz[0])):
            if (matriz[fila][columna] == '1'):
                siguienteUno = (fila, columna)
    return siguienteUno



main()

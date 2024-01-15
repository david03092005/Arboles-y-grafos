# David Alejandro Salazar Zuleta
# 8972690

from collections import deque
from sys import stdin

def leerEntrada():
    global Casas, Torres
    Casas = deque()
    Torres = deque()
    cantEntrada = int(stdin.readline())
    for casos in range(cantEntrada):
        casasPorCaso = deque()
        linea = stdin.readline().split()
        wifi = int(linea[0])
        Torres.append(wifi)
        for i in range(int(linea[1])):
            posicionCasa = int(stdin.readline())
            casasPorCaso.append(posicionCasa)
        casasPorCaso = sorted(casasPorCaso)
        Casas.append(casasPorCaso)


def busquedaBinaria(caso, torres):
    low = 0
    hi = caso[-1]
    resultado = 0 

    while low <= hi:
        mid = (low + hi) / 2  
        mid = round(mid,1)
        if (esPosibleConectar(mid*2, caso, torres)):
            resultado = mid  
            hi = mid - 0.1
            hi = round(hi,1)
        else: 
            low = mid + 0.1
            low = round(low,1)
    
    return resultado


def esPosibleConectar(distancia, caso, torres):
    requisitos = True
    distanciasCT = [caso[0] + distancia]
    for conexiones in range(1, len(caso)):
        if (caso[conexiones] > distanciasCT[-1]):
            distanciasCT.append(caso[conexiones] + distancia)
        torresUsadas = len(distanciasCT)
    if (torresUsadas > torres):
        requisitos = False
    return requisitos


def main():
    leerEntrada()
    for numcaso, caso in enumerate(Casas):
        if (len(caso) <= Torres[numcaso]):
            print("0.0")
        else:
            print(busquedaBinaria(caso, Torres[numcaso]))

main()
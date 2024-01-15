# David Alejandro Salazar Zuleta
# 8972690

from sys import stdin
import sys

sys.setrecursionlimit(10 ** 6)

def main():
    linea = stdin.readline()
    while (linea.split()):
        procesarEntrada(linea.split())
        linea = stdin.readline()


def procesarEntrada(informacion):
    global arbol, arreglo
    tamaño = int(informacion[0])
    peticiones = int(informacion[1])
    arreglo = list(map(int, stdin.readline().split()))
    arbol = [float('inf')] * (tamaño * 2)
    construirArbol(arreglo, 0, 0, tamaño-1)
    for i in range(peticiones):
        peticion, rango = stdin.readline().split('(')
        rango = rango.split(')')[0].split(',')
        if (peticion == 'query'):
            procesarQuery(rango)
        elif (peticion == 'shift'):
            procesarShift(rango)
        

def procesarQuery(rango):
    print(encontrarMinimo(0, 0, len(arreglo) - 1, int(rango[0]) - 1, int(rango[1]) - 1))


def procesarShift(rango):
    numerosCambiar = []
    for numero in rango:
        num = arreglo[int(numero) - 1]
        numerosCambiar.append(num)

    for i in range(len(rango)):
        numero = numerosCambiar[i]
        posicionCambiar = int(rango[i - 1]) - 1
        modificaArbol(0, 0, len(arreglo) - 1, posicionCambiar, numero)
        arreglo[posicionCambiar] = numero   


def construirArbol(arreglo, posicion, izquierda, derecha):
    if (izquierda == derecha): 
        arbol[posicion] = arreglo[izquierda]
    else:
        mitad = izquierda + ((derecha - izquierda) >> 1)
        construirArbol(arreglo, posicion + 1, izquierda, mitad)
        construirArbol(arreglo, posicion + 2 * (mitad - izquierda + 1), mitad + 1, derecha)
        arbol[posicion] = min(arbol[posicion + 1], arbol[posicion + 2 * (mitad - izquierda + 1)])


def encontrarMinimo(posicion, rIzquierda, rDerecha, izquierda, derecha):
    respuesta = None
    if (izquierda > derecha): 
        respuesta = float('inf')
    elif (izquierda == rIzquierda and derecha == rDerecha): 
        respuesta = arbol[posicion]
    else:
        mitad = rIzquierda + ((rDerecha - rIzquierda) >> 1)
        segmentoI = encontrarMinimo(posicion + 1, rIzquierda, mitad, izquierda, min(derecha, mitad))
        segmentoR = encontrarMinimo(posicion + 2 * (mitad - rIzquierda+ 1), mitad + 1, rDerecha, max(izquierda, mitad + 1), derecha)
        respuesta = min(segmentoI, segmentoR)
    return respuesta


def modificaArbol(posicion, rIzquierda, rDerecha, aPosicion, numero):
    if (rIzquierda == rDerecha):
        arbol[posicion] = numero
    else:
        mitad = rIzquierda + ((rDerecha - rIzquierda) >> 1)
        if (aPosicion <= mitad):
            modificaArbol(posicion + 1, rIzquierda, mitad, aPosicion, numero)
        else:
            modificaArbol(posicion + 2 * (mitad - rIzquierda + 1), mitad + 1, rDerecha, aPosicion, numero)
        arbol[posicion] = min(arbol[posicion + 1], arbol[posicion + 2 * (mitad - rIzquierda + 1)])


main()
from collections import deque
from sys import stdin
from fractions import Fraction


def leerEntrada():
    global nodoEncontrado
    line = stdin.readline()
    while (line != '.\n'):
        tok = line.split()
        if tok[0][0]=='!':
            valor0,codigo0,valor1,codigo1 = int(tok[1]),encode(tok[2]),int(tok[4]),encode(tok[5])
            grafo[codigo0].append((codigo1, Fraction(valor1, valor0)))
            grafo[codigo1].append((codigo0, Fraction(valor0, valor1)))      
        else:
            visitados = deque()
            codigo0,codigo1 = encode(tok[1]),encode(tok[3])
            visitados.append(codigo0)
            respuesta = dfsEncontrarValor(codigo0, codigo1, visitados, Fraction(1, 1))
            if (respuesta == Fraction(0,1)):
                print(f"? {name[codigo0]} = ? {name[codigo1]}")
            else:
                print(f"{respuesta.denominator} {name[codigo0]} = {respuesta.numerator} {name[codigo1]}")
            nodoEncontrado = False
        line = stdin.readline()


def encode(s):
    if s not in code:
        code[s] = len(code)
        name.append(s)
        grafo.append(list())
    return code[s]

def dfsEncontrarValor(numNodoInicio, numNodoObjetivo, visitados, fraccion):
    global nodoEncontrado
    for nodoSiguiente in grafo[numNodoInicio]:
        if (nodoSiguiente[0] == numNodoObjetivo):
            nodoEncontrado = True
            fraccion = fraccion * nodoSiguiente[1]
        elif (nodoSiguiente[0] not in visitados and nodoEncontrado == False):
            visitados.append(nodoSiguiente[0])
            fraccion = dfsEncontrarValor(nodoSiguiente[0], numNodoObjetivo, visitados, nodoSiguiente[1])
    if (nodoEncontrado == False and numNodoInicio == visitados[0]):
        fraccion = Fraction(0, 1)
    return fraccion

def main():
    global name,code,grafo, nodoEncontrado
    nodoEncontrado = False
    grafo,name,code = list(),list(),dict()
    leerEntrada()

main()
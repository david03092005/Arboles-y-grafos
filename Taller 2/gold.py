from collections import deque
from sys import stdin


def leerEntrada():
    global matriz, personajes
    matriz = deque()
    personajes = deque()
    tamañoMatriz = str(stdin.readline())
    posicionCaso = 0
    while (tamañoMatriz.split()):
        tamañoMatriz = tamañoMatriz.split()
        matriz.append(deque())
        for i in range(int(tamañoMatriz[1])):
            if(i != 0 and i != int(tamañoMatriz[1])-1):
                linea = str(stdin.readline()).strip()
                fila = []
                for num in range(1, len(linea)-1, 1):
                    segmento = linea[num:num + 1]
                    if (segmento == 'P'):
                        personajes.append((i-1, num-1))
                    fila.append(segmento)
                matriz[posicionCaso].append(fila)
            else:
                ignorar = str(stdin.readline())
        tamañoMatriz = str(stdin.readline())
        posicionCaso += 1


def buscarT(nodo, grafoAbstracto, filasMatriz, columnasMatriz):
    encontroT = False
    fila, columna = nodo

    if (fila != 0):
        if (grafoAbstracto[fila-1][columna] == 'T'):
            encontroT = True
    if (columna != columnasMatriz and encontroT == False):
        if (grafoAbstracto[fila][columna+1] == 'T'):
            encontroT = True
    if (fila != filasMatriz and encontroT == False):
        if (grafoAbstracto[fila+1][columna] == 'T'):
            encontroT = True
    if (columna != 0 and encontroT == False):
        if (grafoAbstracto[fila][columna-1] == 'T'):
            encontroT = True

    return encontroT



def dfsEncontrarOro(nodo, visitados, grafoAbstracto, oro):
    visitados.add(nodo)
    fila, columna = nodo
    if not(buscarT(nodo, grafoAbstracto, len(grafoAbstracto)-1, len(grafoAbstracto[0])-1)):
        for num in range(4):
            nuevaFila = fila + movimientos[num][0]
            nuevaColumna = columna + movimientos[num][1]
            if (verificarNodo(nuevaFila, nuevaColumna, grafoAbstracto) and (nuevaFila, nuevaColumna) not in visitados):
                if(grafoAbstracto[nuevaFila][nuevaColumna] == 'G'):
                    oro = dfsEncontrarOro((nuevaFila, nuevaColumna), visitados, grafoAbstracto, oro+1)
                elif(grafoAbstracto[nuevaFila][nuevaColumna] == '.'):
                    oro = dfsEncontrarOro((nuevaFila, nuevaColumna), visitados, grafoAbstracto, oro)

    return oro


def verificarNodo(fila, columna, grafoAbstracto):
    verificacion = False
    if (fila >= 0 and fila < len(grafoAbstracto) and columna >= 0 and columna < len(grafoAbstracto[0])):
        verificacion = True
    return verificacion


def main():
    global movimientos
    movimientos = ((-1,0), (0,1), (1,0), (0,-1))
    leerEntrada()
    cantidadCasos = 0
    while(cantidadCasos < len(matriz)):
        visitados = set()
        caso = matriz[cantidadCasos]
        print(dfsEncontrarOro(personajes[cantidadCasos], visitados, caso, 0))

        cantidadCasos += 1
    

main()
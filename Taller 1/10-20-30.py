from collections import deque
from sys import stdin

def leerEntrada():
    numBaraja = 0
    baraja = deque()
    baraja.append(deque())
    linea = str(stdin.readline()).split()
    while(linea[0] != "0"):
        for numero in linea:
            if(len(baraja[numBaraja]) < 52):
                baraja[numBaraja].append(int(numero))
            else:
                numBaraja += 1
                baraja.append(deque())
                baraja[numBaraja].append(int(numero))
        linea = str(stdin.readline()).split()
    return baraja

def jugar():
    barajaJ = leerEntrada()
    cantBarajas = len(barajaJ)
    pila1 = deque()
    pila2 = deque()
    pila3 = deque()
    pila4 = deque()
    pila5 = deque()
    pila6 = deque()
    pila7 = deque()
    juegos = 0
    while(juegos < cantBarajas):
        empate = False
        estados = set()
        pila1.append(barajaJ[juegos].popleft())
        estados.add(crearEstado(pila1, pila2, pila3, pila4, pila5, pila6, pila7, barajaJ[juegos]))
        pila2.append(barajaJ[juegos].popleft())
        estados.add(crearEstado(pila1, pila2, pila3, pila4, pila5, pila6, pila7, barajaJ[juegos]))
        pila3.append(barajaJ[juegos].popleft())
        estados.add(crearEstado(pila1, pila2, pila3, pila4, pila5, pila6, pila7, barajaJ[juegos]))
        pila4.append(barajaJ[juegos].popleft())
        estados.add(crearEstado(pila1, pila2, pila3, pila4, pila5, pila6, pila7, barajaJ[juegos]))
        pila5.append(barajaJ[juegos].popleft())
        estados.add(crearEstado(pila1, pila2, pila3, pila4, pila5, pila6, pila7, barajaJ[juegos]))
        pila6.append(barajaJ[juegos].popleft())
        estados.add(crearEstado(pila1, pila2, pila3, pila4, pila5, pila6, pila7, barajaJ[juegos]))
        pila7.append(barajaJ[juegos].popleft())
        estados.add(crearEstado(pila1, pila2, pila3, pila4, pila5, pila6, pila7, barajaJ[juegos]))
        movimientos = 7

        while(len(barajaJ[juegos]) > 0 and empate == False and (len(pila1) > 0 or len(pila2) > 0 or len(pila3) > 0  or len(pila4) > 0  or len(pila5) > 0  or len(pila6) > 0 or len(pila7) > 0)):
            if(len(pila1) > 0 and len(barajaJ[juegos]) > 0 and empate == False):
                empate = nuevoMovimientoPila(pila1, pila1, pila2, pila3, pila4, pila5, pila6, pila7, barajaJ[juegos], estados)
                movimientos += 1

            if(len(pila2) > 0 and len(barajaJ[juegos]) > 0 and empate == False):
                empate = nuevoMovimientoPila(pila2, pila1, pila2, pila3, pila4, pila5, pila6, pila7, barajaJ[juegos], estados)
                movimientos += 1

            if(len(pila3) > 0 and len(barajaJ[juegos]) > 0 and empate == False):
                empate = nuevoMovimientoPila(pila3, pila1, pila2, pila3, pila4, pila5, pila6, pila7, barajaJ[juegos], estados)
                movimientos += 1

            if(len(pila4) > 0 and len(barajaJ[juegos]) > 0 and empate == False):
                empate = nuevoMovimientoPila(pila4, pila1, pila2, pila3, pila4, pila5, pila6, pila7, barajaJ[juegos], estados)
                movimientos += 1
            
            if(len(pila5) > 0 and len(barajaJ[juegos]) > 0 and empate == False):
                empate = nuevoMovimientoPila(pila5, pila1, pila2, pila3, pila4, pila5, pila6, pila7, barajaJ[juegos], estados)
                movimientos += 1
            
            if(len(pila6) > 0 and len(barajaJ[juegos]) > 0 and empate == False):
                empate = nuevoMovimientoPila(pila6, pila1, pila2, pila3, pila4, pila5, pila6, pila7, barajaJ[juegos], estados)
                movimientos += 1

            if(len(pila7) > 0 and len(barajaJ[juegos]) > 0 and empate == False):
                empate = nuevoMovimientoPila(pila7, pila1, pila2, pila3, pila4, pila5, pila6, pila7, barajaJ[juegos], estados)
                movimientos += 1

        if(len(barajaJ[juegos]) == 0):
            print("Loss:", movimientos)
        elif(empate == True):
            movimientos -= 1
            print("Draw:", movimientos)
        else:
            print("Win :", movimientos)
        juegos += 1
        pila1 = deque()
        pila2 = deque()
        pila3 = deque()
        pila4 = deque()
        pila5 = deque()
        pila6 = deque()
        pila7 = deque()

def nuevoMovimientoPila(pilaAgregar, pila1, pila2, pila3, pila4, pila5, pila6, pila7, barajaJ, estados):
    pilaAgregar.append(barajaJ.popleft())
    estadoActual = crearEstado(pila1, pila2, pila3, pila4, pila5, pila6, pila7, barajaJ)
    if (estadoActual in estados):
        return True
    estados.add(estadoActual)
    condicionWhile = True
    while(len(pilaAgregar) >= 3 and condicionWhile == True):
        primeras2Ultima = pilaAgregar[0] + pilaAgregar[1] + pilaAgregar[-1]
        primeraUltimas2 = pilaAgregar[0] + pilaAgregar[-2] + pilaAgregar[-1]
        ultimas3 = pilaAgregar[-3] + pilaAgregar[-2] + pilaAgregar[-1]
        condicionWhile = False
        if(primeras2Ultima == 10 or primeras2Ultima == 20 or primeras2Ultima == 30):
            barajaJ = agregarABaraja(barajaJ, pilaAgregar.popleft(), pilaAgregar.popleft(), pilaAgregar.pop())
            condicionWhile = True
        elif(primeraUltimas2 == 10 or primeraUltimas2 == 20 or primeraUltimas2 == 30):
            ultima = pilaAgregar.pop()
            barajaJ = agregarABaraja(barajaJ, pilaAgregar.popleft(), pilaAgregar.pop(), ultima)
            condicionWhile = True
        elif(ultimas3 == 10 or ultimas3 == 20 or ultimas3 == 30):
            condicionWhile = True
            tercera = pilaAgregar.pop()
            segunda = pilaAgregar.pop()
            barajaJ = agregarABaraja(barajaJ, pilaAgregar.pop(), segunda, tercera)
    return False

def crearEstado(pila1, pila2, pila3, pila4, pila5, pila6, pila7, barajaJ):
    estado = (tuple(pila1), tuple(pila2), tuple(pila3), tuple(pila4), tuple(pila5), tuple(pila6), tuple(pila7), tuple(barajaJ))
    return estado


def agregarABaraja(baraja, primerNum, segundoNum, tercerNum):
    baraja.extend([primerNum, segundoNum, tercerNum])
    return baraja

jugar()
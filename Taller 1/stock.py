from collections import deque
from sys import stdin
from heapq import heappush, heappop

def stockPrices():
    cantidadMercado = int(stdin.readline())
    while(cantidadMercado > 0):
        cantidadMovimientos = int(stdin.readline())
        movimientos = deque()
        while(cantidadMovimientos > 0):
            movimientos.append(str(stdin.readline()).split())
            cantidadMovimientos -= 1
        cantidadMercado -= 1
        ejecutarMovimientos(movimientos)
            

def ejecutarMovimientos(movimientos):
    venta = []  
    compra = []
    ultimaOperacion = 0
    for movimientoActual in movimientos:
        if(movimientoActual[0] == "buy"):
            precioYCantidad =  [-int(movimientoActual[4]), int(movimientoActual[1])]
            heappush(compra, precioYCantidad)
        elif(movimientoActual[0] == "sell"):
            precioYCantidad =  [int(movimientoActual[4]), int(movimientoActual[1])]
            heappush(venta, precioYCantidad)
        
        if(len(venta) > 0 and len(compra) > 0):
            if(venta[0][0] <= -compra[0][0]):
                cantidadVendida = venta[0][1]
                cantidadComprada = compra[0][1]
                ultimaOperacion = venta[0][0]
                if(cantidadVendida > cantidadComprada):
                    heappop(compra)
                    venta[0][1] = cantidadVendida - cantidadComprada
                elif(cantidadVendida < cantidadComprada):
                    heappop(venta)
                    compra[0][1] = cantidadComprada - cantidadVendida
                else:
                    heappop(venta)
                    heappop(compra)

        if(len(compra) == 0 and ultimaOperacion == 0):
            print(f"{venta[0][0]} - -")
        elif(len(venta) == 0 and ultimaOperacion == 0):
            print(f"- {-compra[0][0]} -")
        elif(ultimaOperacion == 0):
            print(f"{venta[0][0]} {-compra[0][0]} -")
        elif(len(venta) == 0 and ultimaOperacion != 0):
            print(f"- {-compra[0][0]} {ultimaOperacion}")
        elif(len(compra) == 0 and ultimaOperacion != 0):
            print(f"{venta[0][0]} - {ultimaOperacion}")
        else:
            print(f"{venta[0][0]} {-compra[0][0]} {ultimaOperacion}")


stockPrices()
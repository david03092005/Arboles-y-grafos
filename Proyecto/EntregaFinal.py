# David Alejandro Salazar Zuleta
# 8972690

import sys
import random as ran
import numpy as np
import matplotlib.pyplot as plt

# sys.set_int_max_str_digits(10000000)

def main():
    global tamañoGrafo, cantidadIteraciones
    tamañoGrafo = 10
    cantidadAristas = 3
    cantidadIntervalos = 5
    cantidadIteraciones = 10

    S = 0 # Semilla aleatoria
    ran.seed(S) # Generador de numeros random con S
    np.random.seed(S) # Generador de numeros random de numpy

    grafo, opiniones = GeneracionGrafoBA(tamañoGrafo, cantidadAristas) # Grafo, influencia y opiniones generados con Barabasi Albert
    print(grafo)
    print(opiniones)
    grafo = sorted(grafo)
    print(grafo)

    opinionFinal = actualizacionNVeces(grafo, opiniones, cantidadIteraciones, cantidadIntervalos) # Estado final de las opiniones después de n iteraciones
    plt.plot(range(0, len(opinionFinal)), opinionFinal, linestyle='', marker='o')
    plt.title("OPINIONES FINALES DE LAS PERSONAS")
    plt.xlabel("Número de persona")
    plt.ylabel("Opinion")
    plt.show()


"""
Funcion para actualizar las opiniones de los nodos n veces.
    Entrada:
            Grafo: representado como lista de aristas, incluyendo la influencia que tiene un nodo al otro 
                (Influenciador, Influenciado, Influencia).
            opiniones iniciales: representada como una lista, en la que cada posicion x tiene la opinion del nodo x.
            n: un numero natural que nos dice cuantas veces se va a hacer la actualizacion de las opiniones.
    
    Salida: 
            Lista de opiniones en el tiempo n.
"""
def actualizacionNVeces(grafo, opinionesIniciales, n, h):
    opinionesN = opinionesIniciales
    mostrar = 0
    polarizacionFinal = []
    for i in range(n):
        mascaraBits = ran.randrange(0, 1<<len(grafo))
        print("Mascara:", mascaraBits)
        opinionesN = actualizacionOpinion(grafo, opinionesN, mascaraBits)
        intervalos, cantidadNodos, polar = polarizacion(h, opinionesN)
        polarizacionFinal.append(polar)
        if (mostrar == 5 or i == 0 or i == n-1):
            mostrar = 0
            plt.figure(figsize=(8, 6))
            plt.polar(np.linspace(0, 2 * np.pi, len(intervalos), endpoint=False), cantidadNodos, marker='o', linestyle='')
            plt.text(i, max(cantidadNodos), i, ha='center', va='bottom')
            plt.thetagrids(range(0, 360, int(360/len(intervalos))), labels=intervalos)
            plt.title(f"Diagrama de Polarización en Redes Sociales en el tiempo {i}")
        else:
            mostrar += 1

    plt.show()
    plt.plot(range(0, len(polarizacionFinal)), polarizacionFinal, label=i, marker='o')
    plt.title("Polarización de la opinión sobre un tema en redes sociales")
    plt.xlabel("Tiempo")
    plt.ylabel("Polarización de las opiniones")
    plt.show()

    return opinionesN


"""
Funcion para actualizar las opiniones de los nodos
    Entrada:
            Grafo: representado como lista de aristas, incluyendo la influencia que tiene un nodo al otro 
                (Influenciador, Influenciado, Influencia).
            opiniones: representada como una lista, en la que cada posicion x tiene la opinion del nodo x.
            mascaraBits: Un numero natural, que nos dice que aristas del grafo se deben utilizar para la actualizacion de las opiniones
                el bit mas significativo pertenece a la primera posicion de las aristas y así sucesivamente hasta llegar al bit menos significativo
                que pertenece a la ultima arista del grafo.

    Salida: 
            opinionesActualizadas: Lista de opiniones actualizadas dependiendo de las aristas representadas en la mascara de bits.
"""
def actualizacionOpinion(grafo, opiniones, mascaraBits):
    global tamañoGrafo
    opinionesActualizadas = list(opiniones)
    sumatoria = [0] * tamañoGrafo
    cantidadInfluencia = [0] * tamañoGrafo
    contador = 0
    posicionBit = len(grafo) - 1
    while(posicionBit >= 0): # Se recorre la lista de aristas.
        comprobacion = 1 << posicionBit
        activo = comprobacion & mascaraBits # Operaciones para saber si la arista en la posicion contador hace parte de la actualizacion.
        if (activo == comprobacion): # Se añade el b(v, u) * (a(v) - a(u)) a la sumatoria del nodo u.
            arista = grafo[posicionBit]
            nodoInfluenciador = arista[0]
            nodoInfluenciado = arista[1]
            influencia = arista[2]
            diferencia = opiniones[nodoInfluenciador] - opiniones[nodoInfluenciado]
            opinion = influencia * diferencia
            sumatoria[nodoInfluenciado] += opinion
            cantidadInfluencia[nodoInfluenciado] += 1

        contador += 1
        posicionBit -= 1
    
    # Se hace un ciclo para aplicar la formula final de la actualizacion de opinion y sumarlo a la opinion actual del nodo. 
    for i in range(len(sumatoria)):
        suma, cantidad = sumatoria[i], cantidadInfluencia[i]
        if (cantidad != 0):
            opinionFinal  = suma / cantidad
            opinionesActualizadas[i] += opinionFinal
    
    return opinionesActualizadas


"""
Funcion para generar el grafo con el modelo de Barabasi Albert
    Entrada: 
            cantidadNodos:  Un numero natural, que es la cantidad de nodos que se van a agregar al grafo, enumerados de 0 hasta cantidadNodos - 1.
            cantidadAristas: un numero natural, que es la cantidad de aristas que se van a crear de nodos anteriores a un nodo nuevo.

    Salida:
            grafo: Retorna un grafo representado como lista de aristas con pesos (u, v, peso), generado por el modelo de Barabasi Albert.
            opiniones: Una lista de opiniones del mismo tamaño que la cantidad de nodos, en donde cada posicion x representa la opinion del nodo x.
"""
def GeneracionGrafoBA(cantidadNodos, cantidadAristas):
    grafo, adyacencia =  grafoInicial(cantidadAristas) # Se genera un grafo inicial con (cantidadAristas + 1) nodos y sus aristas conectadas.
    opiniones = generarOpiniones(cantidadNodos) # Se genera la lista de opiniones de los nodos.
    cantidadTotalAristas = len(grafo)
    for nodo in range(cantidadAristas + 1, cantidadNodos):
        probabilidades = [numero / cantidadTotalAristas for numero in adyacencia] # Las probabilidades de que un nodo sea elegido para formar una arista con el nuevo nodo.
        nuevasAristas = set()
        while(len(nuevasAristas) < cantidadAristas):
            nuevoNodo = np.random.choice(range(0, nodo-1), p=probabilidades)
            if (nuevoNodo not in nuevasAristas): # Esto para que no se sumen mas adyacencias de la que deberian.
                nuevasAristas.add(nuevoNodo)
                # Se crea la nueva arista de la siguiente forma (influenciador, influenciado(NodoNuevo), peso)
                # Esto con el fin de simular lo que ocurriria en una red social, que el nodo que entra nuevo a la red
                # es influenciado por alguno de los nodos famosos o de vez en cuando alguno no tan famoso.
                nuevaArista = (nuevoNodo, nodo, generarInfluencia(adyacencia[nuevoNodo], nodo))
                grafo.append(nuevaArista)
                adyacencia[nuevoNodo] += 1
                cantidadTotalAristas += 1

        cantidadTotalAristas += 1
        adyacencia.append(1)

    return grafo, opiniones


"""
Funcion para gnerar un grafo inicial, que se utilizara en el algoritomo de Barabasi Albert
    Entrada:
            cantidadNodos: Un numero natural, que nos da la cantidad de nodos que debe tener el grafo.

    Salida:
            Grafo: Un grafo representado con lista de aristas.
            adyacencia: Una lista con tamaño igual a cantidadNodos, que en cada posicion v tenga a cuantos nodos influye el nodo v. 
"""
def grafoInicial(cantidadNodos):
    grafo = []
    adyacencia = [0] * cantidadNodos
    for i in range(cantidadNodos + 1):
        j = i - 1
        while (j >= 0): # En este ciclo se conectan los nodos que se crearon anteriormente con el nuevo nodo, para así decir que los viejos influyen a los nuevos.
            arista = (j, i, generarInfluencia(adyacencia[j], i))
            grafo.append(arista)
            adyacencia[j] += 1
            j -= 1

    return grafo, adyacencia


"""
Funcion para sacar la influencia que tiene un nodo sobre otro, dependiendo de la cantidad de nodos a los que ya influya y de la cantidad de nodos en ese momento.
    Entrada:
            Influencias: Un numero natural, que nos da la cantidad de nodos a los que influye el nodo de salida.
            CantidadNodos: Un numero natural, que nos da la cantidad de nodos que hay en el grafo al momento de generar la influencia.

    Salida:
            Influencia: Un numero real en el intervalo [0, 1], que nos da la influencia que va a tener un nodo sobre otro.
"""
def generarInfluencia(influencias, cantidadNodos):
    numero = ran.randrange(0, cantidadNodos)
    influencia = 0
    # Se genera un numero aleatorio desde 0 hasta la cantidadNodos
    # si este numero que se genero aleatoriamente es menor o igual va a tener una mayor influencia entonces los nodos 
    # que mayor cantidad de nodos influenciados tengan van a tener una mayor influencia sobre los nuevos nodos
    if (numero <= influencias):
        influencia = ran.uniform(0.5, 1.0000000001)
    else:
        influencia = ran.uniform(0, 0.5)

    return influencia


"""
Funcion para generar las opiniones iniciales de los nodos
    Entrada:
            cantidadNodos: Un numero natural, que es la cantidad de nodos en el grafo y que nos da la cantidad de opiniones que se deben generar.

    Salida:
            opiniones: Una lista con tamaño igual a la cantidad de nodos del grafo, que en la posicion x tiene la opinion del nodo x.
"""
def generarOpiniones(cantidadNodos):
    opiniones = []
    for n in range(cantidadNodos):
        opinionN = ran.uniform(0, 1.00000000001)
        opiniones.append(opinionN)

    return opiniones


"""
Función que nos separa las opiniones en h intervalos y nos da la polarizacion de la red social.
    Entrada:
            CantidadIntervalos: Un numero natural, que nos dice en cuantos intervalos queremos dividir las opiniones.
            opiniones: Una lista de opiniones de cada nodo dentro del grafo, en donde la posicion x tiene la opinion del nodo x.
    Salida:
            intervalos: Una lista con el punto medio de un intervalo 1/h.
            cantidadNodos: Una lista que en cada posición tiene la cantidad de nodos que están en ese intervalo de opinión.
            polar: Un numero real, que nos dice cual es la polarización de la red en ese momento. 
"""
def polarizacion(cantidadIntervalos, opiniones):
    intervalos = generarIntervalos(cantidadIntervalos)
    cantidadNodos = generarCantidadNodos(intervalos, opiniones, cantidadIntervalos)
    print(cantidadNodos)

    polar = formulaPolarizacion(cantidadIntervalos, intervalos, cantidadNodos)
    print(polar)

    return intervalos, cantidadNodos, polar


"""
Funcion para dividir la lista de intervalos en h intervalos del mismo tamaño, y poner el punto medio del intervalo.
    Entrada:
            h: Un numero natural, que nos dice en cuantos intervalos queremos dividir la lista de intervalos.
    Salida:
            intervalos: Una lista de h posiciones, que va a tener el punto medio de los intervalos anteriormente divididos.
"""
def generarIntervalos(h):
    intervalos = []
    acumulador = 1/h
    while(acumulador <= 1):
        mitad = acumulador - (1/(h*2))
        intervalos.append(mitad)
        acumulador += 1/h
    
    return intervalos


"""
Funcion para saber a que intervalo de opinion pertenecen los nodos del grafo.
    Entrada:
            intervalo: Una lista de h posiciones que tiene el punto medio del intervalo que representa de tamaño 1/h
            opiniones: Una lista de opiniones de cada nodo dentro del grafo, en donde la posicion x tiene la opinion del nodo x.
            h: Un numero natural, que nos dice cual es la cantidad de intervalos en la lista de intervalos

    Salida:
            cantidadNodos: Una lista de tamaño igual a la cantidad de intervalos divididos anteriormente, que tenga en la posicion x cuantos 
            nodos pertenecen a ese intervalo.
"""
def generarCantidadNodos(intervalo, opiniones, h):
    cantidadNodos = [0] * len(intervalo)
    for opinionNodo in opiniones:
        menor = 0
        mayor = len(intervalo)
        colocado = False

        while (menor <= mayor and not colocado):
            mitad = (menor + mayor) >> 1
            numeroIntervalo = intervalo[mitad]
            intervaloMayor = numeroIntervalo + (1/(h*2))
            intervaloMenor = numeroIntervalo - (1/(h*2))
            if (opinionNodo <= intervaloMayor and opinionNodo > intervaloMenor):
                cantidadNodos[mitad] += 1
                colocado = True
            else:
                if (opinionNodo > numeroIntervalo):
                    menor = mitad + 1
                elif (opinionNodo < numeroIntervalo):
                    mayor = mitad - 1

    return cantidadNodos


"""
Funcion que aplica la fórmula de polarización.
    Entrada:
            h: Un número natural, que nos dice cuantos intervalos de opiniones distintos hay.
            intervalos: Una lista que tiene el punto medio de cada intervalo.
            cantidadNodos: Una lista que tiene la cantidad de nodos que su opinión pertenece a ese intervalo.
    Salida:
            sumatoria: Un número natural, que nos dice cual es la polarización de la red.
"""
def formulaPolarizacion(h, intervalos, cantidadNodos):
    sumatoria = 0

    for i in range(h):
        for j in range(h):
            c = cantidadNodos[i] ** 2.6
            c = c * cantidadNodos[j]
            r = abs(intervalos[i] - intervalos[j])
            resultado = c * r
            sumatoria += resultado

    sumatoria = sumatoria * 1000
    return sumatoria


main()
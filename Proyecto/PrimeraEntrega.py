# David Alejandro Salazar Zuleta
# 8972690


def main():
    # Organizacion del grafo
    # Primer valor: nodoAdyacente
    # Segundo valor: Influencia de ese nodo al nodo adyacente (peso)
    grafo = [
        [(1, 0.2), (2, 0.4)],
        [(2, 0.3)],
        [(3, 0.5), (4, 0.1)],
        [],
        []
    ]
    # Lista de opiniones de cada nodo
    opiniones = [0.5, 0.8, 0.6, 0.4, 0.7]
    # Lista de arcos que van a participar en las actualizaciones
    actualizaciones = [(0, 2), (1, 2), (2, 3), (2, 4)]
    # Lista de opiniones actualizada

    # grafo = [
    #     [(1, 0.3)],
    #     [(4, 0.5)],
    #     [(0, 0.2),(1, 0.8)],
    #     [(1, 0.7),(4, 0.1)],
    #     []
    # ]
    # actualizaciones = [(2, 0), (0, 1), (1, 4), (3, 1)]
    # opiniones = [0.3, 0.4, 1, 0.5, 0]
    opiniones = actualizacionOpinion(grafo, opiniones, actualizaciones)
    print(opiniones)


# Funcion para actualizar las opiniones de los nodos con un arreglo de aristas dado
def actualizacionOpinion(grafo, opiniones, arregloActualizar):
    opinionesActualizadas = list(opiniones)
    # Se ordena el arreglo de aristas por el segundo elemento con el fin de tener todas las aristas
    # que van a hacer influencia en un unico nodo juntas al momento de recorrerlo
    arregloActualizar = sorted(arregloActualizar, key=lambda x:x[1])
    i = 0
    while(i < len(arregloActualizar)): # Se recorre la lista de aristas
        nodoActualizar = arregloActualizar[i][1]
        opinionNodo = opiniones[nodoActualizar]
        cantidadInfluencias = 0
        influenciaFinal = 0
        j = i
        # Se hace un segundo ciclo en la lista para tener en cuenta en la actualizacion de la opinion
        # a todas las aristas que lleguen al mismo nodo, por esto se organizo anteriormente la lista por el segundo elemento
        while(j < len(arregloActualizar) and i == j):
            # Si el nodo es igual al que estamos actualizando en ese momento se aplica la formula B(u,v)*(a(v)-a(u))
            # siendo u->nodoActualizar y v->nodoInfluencia.
            if (arregloActualizar[j][1] == nodoActualizar): 
                nodoInfluencia = arregloActualizar[i][0]
                influencia = encontrarInfluencia(grafo, nodoActualizar, nodoInfluencia)
                diferenciaOpinion = (opiniones[nodoInfluencia] - opinionNodo)
                influenciaFinal += (influencia * diferenciaOpinion)
                cantidadInfluencias += 1 # Se cuentan las aristas que influenciaron al nodo u 
                i += 1 # Se va iterando en la lista
            j += 1 # Este iterador nos permite no pasarnos del valor en el que vamos y que ademas el segundo ciclo termine apenas no encuentre otro valor
        opinionesActualizadas[nodoActualizar] += (influenciaFinal/cantidadInfluencias) # Se termina de ejecutar la formula a(u)+sumatoria(influencias)/cantInfluencias

    return opinionesActualizadas


# Funcion para encontrar el peso de la influencia del nodoInfluencia sobre el nodoInfluenciado
# es decir, encuentra el peso de la arista que va de nodoInfluencia a nodoInfluenciado --> B(u,v)
def encontrarInfluencia(grafo, nodoInfluenciado, nodoInfluencia):
    iterador = 0
    influencia = False
    nodosAdyacentes = grafo[nodoInfluencia]
    while (iterador < len(nodosAdyacentes) and influencia == False):
        if (nodosAdyacentes[iterador][0] == nodoInfluenciado):
            influencia = nodosAdyacentes[iterador][1]
        iterador += 1
    
    return influencia


main()
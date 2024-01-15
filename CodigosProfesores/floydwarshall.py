"""
Implementación Algoritmo de Floyd-Warshall

"""

def floydWarshall(w):
    n = len(w)
    d = [[float("inf") for j in range(n)] for i in range(n)]
    nex = [[-1 for j in range(n)] for i in range(n)]

    for i in range(n):
        for j in range(n):
            d[i][j] = w[i][j]
            nex[i][j] = j
    for i in range(n):
        d[i][i], nex[i][i] = 0, i

    print(d)
    print("***************************")
        
    for k in range(0, n):
        for i in range(0, n):
            for j in range(0, n):
                if d[i][k] + d[k][j] < d[i][j]:
                    d[i][j] = d[i][k] + d[k][j]
                    nex[i][j] = nex[i][k]
        print(d)
        print("***************************")
    return d, nex

def main():
    #G = [[1, 2], [2, 3], [1, 3, 4], [0, 4], [0, 1]]
    w = [[0, 4, 5, float('inf'),float('inf')],
         [float('inf'), 0, -1, 1, float('inf')],
         [float('inf'), 2, 0, -1, 1],
         [2, float('inf'), float('inf'), 0, 2],
         [3, 3, float('inf'), float('inf'), 0]]
    d, nex = floydWarshall(w)
    print(d)
    print("***************************")
    print(nex)

main()

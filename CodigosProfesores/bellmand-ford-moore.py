"""
Implementación Algoritmo Bellman Ford Moore
Octubre 12 de 2023

"""

from sys import stdin

INF = float("inf")

# Retornar True o False dependiendo de si el grafo tiene o no
# ciclos negativos

# Complejidad: n = |V|, m = |E|  ---> O(n * m)
def bellmanFordMoore(G, s, dist):
  N = len(G)
  dist = [INF for _ in range(N)]
  pred = [-1 for _ in range(N)]
  dist[s] = 0

  i = 0
  while i < N - 1:
    for u in range(N):
      for (v, duv) in G[u]:
         if dist[u] + duv < dist[v]:
           dist[v] = dist[u] + duv
           pred[v] = u
      i += 1
  ans = False
  u = 0
  while u < N and not ans:
     j = 0
     while j < len(G[u]) and not ans:
        v, duv = G[u][j]
        if dist[u] + duv < dist[v]:
            ans = True
         j += 1
    u += 1
  return ans

  

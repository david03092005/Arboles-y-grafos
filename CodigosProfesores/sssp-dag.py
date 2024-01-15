"""
Implementación Algoritmo Caminos más Cortos para DAG

Octubre 12 de 2023

"""

INF = float("inf")

# Complejidad: n = |V|, m = |E| ---> O(n + m)
def ssspDAG(G, s):
  dist, pred = [INF for _ in range(len(G))], [-1 for _ in range(len(G))]
  dist[s] = 0

  topo = toposort(G)
  for u in topo:
    for (v, duv) in G[u]:
      if dist[u] + duv < dist[v]:
        dist[v] = dist[u] + duv
        pred[v] = u
  return dist, pred

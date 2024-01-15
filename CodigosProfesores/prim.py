"""
ImplementaciÃ³n algoritmo de Prim

"""

from heapq import heappush, heappop

INF = float("inf")

def prim(G):
  visited = [False for i in range(len(G))]
  c = [ INF ]*len(G) ; c[0] = 0
  p = [-1] * len(G)
  pqueue = list()
  heappush(pqueue, (c[0], 0))
  
  while len(pqueue)!=0:
    du,u = heappop(pqueue)
    visited[u] = True
    if c[u] == du:
      for v,duv in G[u]:
        if not visited[v] and duv<c[v]:
          c[v] = duv
          p[v] = u
          heappush(pqueue, (c[v], v))
  return c, p
  
G = [[(1, 10), (2, 14), (3, 2)], [(0, 10), (2, 16), (3, 12)],
      [(0, 14), (1, 16), (3, 12)], [(0, 2), (1, 12), (2, 12)]]
print(prim(G))
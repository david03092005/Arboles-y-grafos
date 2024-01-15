"""
Implementación BFS con Listas de Adyacencia
Agosto 8 de 2023

"""

from collections import deque

G, vis = None, None

def bfs():
  global vis
  vis = [False for _ in range(len(G))]
  for i in range(len(G)):
    if not vis[i]:
      bfsAux(i)

def bfsAux(u):
  global vis
  q = deque()
  vis[u] = True
  q.append(u)
  while len(q) > 0:
    u = q.popleft()
    print("visting %d" % u)
    for v in G[u]:
      if not vis[v]:
        vis[v] = True
        q.append(v)

def main():
  global vis, G
  G = [[3, 1, 2], [0, 2, 4, 5], [3, 4], [4, 1], [5, 0], [1, 2]]
  bfs()

main()

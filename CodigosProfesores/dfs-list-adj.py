"""
Implementación DFS con Listas de Adyacencia
Agosto 8 de 2023

"""

G, vis = None, None

def dfs():
  global vis
  vis = [False for _ in range(len(G))]
  for i in range(len(G)):
    if not vis[i]:
      dfsAux(i)

def dfsAux(u):
  global vis
  vis[u] = True
  print("visting %d" % u)
  for v in G[u]:
    if not vis[v]:
      dfsAux(v)

def main():
  global vis, G
  G = [[3, 1, 2], [0, 2, 4, 5], [3, 4], [4, 1], [5, 0], [1, 2]]
  dfs()

main()

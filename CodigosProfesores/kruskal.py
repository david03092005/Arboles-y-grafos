from sys import stdin
import math

#operaciones disjoint set union
#**************************************
p, rango = [0 for _ in range(13)], [0 for _ in range(13)]

def makeSet(v):
    p[v], rango[v] = v, 0

def findSet(v):
    ans = None
    if v == p[v]: ans = v
    else:
        p[v] = findSet(p[v])
        ans = p[v]
    return ans

def unionSet(u, v):
    u, v = findSet(u), findSet(v)
    if u != v:
        if rango[u] < rango[v]: u, v = v, u
        p[v] = u
        if rango[u] == rango[v]: rango[u] += 1

#****************************************

def kruskal(n, aristas):
  for i in range(1, n + 1): makeSet(i)
  aristas.sort(key = lambda x: x[2])
  mst = []

  for it in aristas:
    u, v, c = it

    if findSet(u) != findSet(v):
      unionSet(u, v)
      mst.append(it)
  return mst

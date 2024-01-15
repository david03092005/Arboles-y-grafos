"""
Radio y centro arbol n-ario representacion listas de adyacencia
Autor: Carlos Ramirez
Fecha: Septiembre 14 de 2023

"""

from sys import stdin
from collections import deque

distMax, nodoMax = None, None

def dfsAux(v, p, dist):
  global distMax, nodoMax
  dist += 1
  if dist > distMax: distMax, nodoMax = dist, v
  for w in  G[v]:
    if w != p:
      dfsAux(w, v, dist)

def diameter():
  global distMax
  distMax = 0

  #se escoge arbitrariamente iniciar en el nodo 0
  #el resultado seria el mismo asi se inicie en un nodo diferente
  dfsAux(0, -1, -1)
  dfsAux(nodoMax, -1, -1)
  return distMax

def radio():
  diam = diameter()
  ans = (diam + 1) // 2
  return ans

def center():
  nivelMax = 0
  nivel = [0 for _ in range(len(G))]
  grado = [len(G[v]) for v in range(len(G))]
  queue = deque()
  nodosCentro = set()

  for i in range(len(G)):
    if grado[i] == 1:
      queue.append(i)

  while len(queue) > 0:
   v = queue.popleft()
   for w in G[v]:
     grado[w] -= 1
     if grado[w] == 1:
       queue.append(w)
       nivel[w] = nivel[v] + 1
       nivelMax = max(nivelMax, nivel[w])
  for i in range(len(G)):
    if nivel[i] == nivelMax:
      nodosCentro.add(i)

  radio = nivelMax + 1 if len(nodosCentro) == 2 else  nivelMax
  if len(nodosCentro) == 2: diametro = 2 * radio - 1
  else: diametro = 2 * radio

  return radio, diametro, nodosCentro

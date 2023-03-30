import sys
from heapq import heappush, heappop
from math import floor, sqrt, pow

n,w = map(int, sys.stdin.readline().split())
m = float(sys.stdin.readline())
position = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
current = set([tuple(map(int, sys.stdin.readline().split())) for _ in range(w)])
graph = [[] for _ in range(n+1)]
INF = 1e9
distance = [INF]*(n+1)

for i in range(1, n+1):
  for j in range(1, n+1):
    if i == j:
      continue
    i_x, i_y = position[i-1]
    j_x, j_y = position[j-1]
    dist = sqrt(pow(i_x - j_x, 2) + pow(i_y - j_y, 2))
    
    if (i, j) in current or (j, i) in current:
      graph[i].append((j, 0))
    else:
      graph[i].append((j, dist))
      
def dijkstra(start):
  distance[start] = 0
  q = []
  heappush(q, (0, start))
  
  while q:
    dist, now = heappop(q)
    if dist > distance[now]:
      continue
    for i in graph[now]:
      cost = dist + i[1]
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heappush(q, (cost, i[0]))
dijkstra(1)
      
print(floor(distance[n]*1000))
    
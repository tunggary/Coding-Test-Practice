import sys
from heapq import heappush, heappop

n,m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
indegree = [0]*(n+1)
for _ in range(m):
  a,b = map(int, sys.stdin.readline().split())
  graph[a].append(b)
  indegree[b] += 1
  
q = []
for i in range(1, n+1):
  if indegree[i] == 0:
    heappush(q, i)
  
while q:
  now = heappop(q)
  print(now, end=' ')
  for i in graph[now]:
    indegree[i] -= 1
    if indegree[i] == 0:
      heappush(q, i)
      
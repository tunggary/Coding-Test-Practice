import sys
from collections import deque

n,m = map(int, sys.stdin.readline().split())
indegree = [0]*(n+1)
graph = [[] for _ in range(n+1)]
result = [0]*(n+1)
for _ in range(m):
  a,b = map(int, sys.stdin.readline().split())
  graph[a].append(b)
  indegree[b] += 1
  
def topology_sort():
  q = deque()
  for i in range(1, n+1):
    if indegree[i] == 0:
      q.append((i,1))
  while q:
    now, semester = q.popleft()
    result[now] = semester
    for i in graph[now]:
      indegree[i] -= 1
      if indegree[i] == 0:
        q.append((i, semester+1))

topology_sort()
print(' '.join(map(str, result[1:])))
  
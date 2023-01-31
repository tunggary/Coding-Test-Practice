import sys

sys.setrecursionlimit(10**7)

n = int(sys.stdin.readline().strip())
parent = [1] * (n+1)
visited = [False] * (n+1)
graph = [[] for _ in range(n+1)]


for _ in range(n-1):
  a, b = map(int, sys.stdin.readline().strip().split())
  graph[a].append(b)
  graph[b].append(a)
  
def find_children(current):
  visited[current] = True
  for child in graph[current]:
    if not visited[child]:
      parent[child] = current
      find_children(child)
  
find_children(1)
for i in range(2, n+1):
  print(parent[i])
import sys

n = int(sys.stdin.readline())
w = [int(sys.stdin.readline().strip()) for _ in range(n)]
graph = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
edges = []
parent = [i for i in range(n+1)]
answer = 0

def find_parent(parent, x):
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b

for i in range(n):
  edges.append((w[i], 0, i+1))
  
for i in range(n):
  for j in range(i+1, n):
    if graph[i][j]:
      edges.append((graph[i][j], i+1, j+1))
      
for edge in sorted(edges):
  cost, a, b = edge
  if find_parent(parent, a) != find_parent(parent, b):
    union_parent(parent, a, b)
    answer += cost
    
print(answer)
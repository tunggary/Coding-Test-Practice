import sys

n = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
parent = [i for i in range(n)]
edges = []
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
  for j in range(i+1, n):
    edges.append((graph[i][j], i, j))

edges.sort()

for edge in edges:
  c,a,b = edge
  if find_parent(parent, a) != find_parent(parent, b):
    union_parent(parent, a, b)
    answer += c
    
print(answer)
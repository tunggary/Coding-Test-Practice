import sys

def find_parent(parent, x):
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

def union_parent(parent, x, y):
  x = find_parent(parent, x)
  y = find_parent(parent, y)
  if x < y:
    parent[y] = x
  else:
    parent[x] = y
    
v = int(sys.stdin.readline())
e = int(sys.stdin.readline())

parent = [i for i in range(v+1)]
edges = []
answer = 0

for _ in range(e):
  a,b,c = map(int, sys.stdin.readline().split())
  edges.append((c,a,b))
  
edges.sort()

for edge in edges:
  cost, a, b = edge
  if find_parent(parent, a) != find_parent(parent, b):
    union_parent(parent, a, b)
    answer += cost

print(answer)
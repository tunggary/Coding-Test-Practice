import sys

v,e = map(int, sys.stdin.readline().split())

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
    
parent = [i for i in range(v+1)]
edges = []
answer = 0
max = 0

for _ in range(e):
  a,b,c = map(int, sys.stdin.readline().split())
  edges.append((c,a,b))
  
edges.sort()

for edge in edges:
  cost, a, b = edge
  if find_parent(parent, a) != find_parent(parent, b):
    union_parent(parent, a, b)
    answer += cost
    max = cost
    
print(answer-max)
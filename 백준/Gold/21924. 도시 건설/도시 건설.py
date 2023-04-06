import sys

v,e = map(int, sys.stdin.readline().split())

parent = [i for i in range(v+1)]
edges = []
total_cost = 0
min_cost = 0

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
    
for _ in range(e):
  a,b,c = map(int, sys.stdin.readline().split())
  edges.append((c,a,b))
  total_cost += c

edges.sort()

for edge in edges:
  cost, a, b = edge
  if find_parent(parent, a) != find_parent(parent, b):
    union_parent(parent, a, b)
    min_cost += cost

flag = True
for i in range(2, v+1):
  if find_parent(parent, i-1) != find_parent(parent, i):
    flag = False
    break
print(total_cost - min_cost if flag else -1)
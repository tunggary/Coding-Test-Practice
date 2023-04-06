import sys

n,m = map(int, sys.stdin.readline().split())
parent = [i for i in range(n+1)]
edges = set()
positions = []
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

for _ in range(n):
  x, y = map(int, sys.stdin.readline().split())
  positions.append((x,y))
  
for _ in range(m):
  a,b = map(int, sys.stdin.readline().split())
  edges.add((0,a,b))
  
for i in range(1,n+1):
  for j in range(i+1, n+1):
    if (0,i,j) in edges or (0,j,i) in edges:
      continue
    x1, y1 = positions[i-1]
    x2, y2 = positions[j-1]
    dist = ((x1-x2)**2 + (y1-y2)**2)**0.5
    edges.add((dist,i,j))
    
for edge in sorted(edges):
  cost, a, b = edge
  if find_parent(parent, a) != find_parent(parent, b):
    union_parent(parent, a, b)
    answer += cost
    
print("%.2f" % answer)
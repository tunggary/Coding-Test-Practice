import sys

n = int(sys.stdin.readline())
x, y, z = [], [], []
for i in range(1, n+1):
  a, b, c = map(int, sys.stdin.readline().strip().split())
  x.append((a, i))
  y.append((b, i))
  z.append((c, i))
parent = [i for i in range(n+1)]
edges = []
answer = 0

def find_parent(x):
  if parent[x] != x:
    parent[x] = find_parent(parent[x])
  return parent[x]

def union_parent(a, b):
  a = find_parent(a)
  b = find_parent(b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b
    
x.sort()
y.sort()
z.sort()

for i in range(n-1):
  edges.append((x[i+1][0]-x[i][0], x[i][1], x[i+1][1]))
  edges.append((y[i+1][0]-y[i][0], y[i][1], y[i+1][1]))
  edges.append((z[i+1][0]-z[i][0], z[i][1], z[i+1][1]))

for edge in sorted(edges):
  cost, a, b = edge
  if find_parent(a) != find_parent(b):
    union_parent(a, b)
    answer += cost
  
print(answer)
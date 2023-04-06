import sys

n,m = map(int, sys.stdin.readline().split())
info = list(sys.stdin.readline().strip().split())
parent = [i for i in range(n+1)]
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

for _ in range(m):
  a,b,c = map(int, sys.stdin.readline().split())
  if info[a-1] != info[b-1]:
    edges.append((c,a,b))
    
for edge in sorted(edges):
  cost,a,b = edge
  if find_parent(parent, a) != find_parent(parent, b):
    union_parent(parent, a, b)
    answer += cost

flag = True
for i in range(1, n+1):
  if find_parent(parent, i) != find_parent(parent, 1):
    flag = False
    break
print(answer if flag else -1)
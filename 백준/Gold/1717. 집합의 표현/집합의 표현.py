import sys
sys.setrecursionlimit(10**6)

n,m = map(int, sys.stdin.readline().split())
parents = [i for i in range(n+1)]

def find_parent(x):
  if parents[x] != x:
    parents[x] = find_parent(parents[x])
  return parents[x]

def union_parent(a, b):
  a = find_parent(a)
  b = find_parent(b)
  if a < b:
    parents[b] = a
  else:
    parents[a] = b

for _ in range(m):
  op, a, b = map(int, sys.stdin.readline().split())
  if op == 0:
    union_parent(a, b)
  else:
    if find_parent(a) == find_parent(b):
      print("YES")
    else:
      print("NO")
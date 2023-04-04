import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
parent = [i for i in range(n+1)]
commands = list(map(int, sys.stdin.readline().split()))

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

for i in range(n):
  for j in range(n):
    if graph[i][j] == 1:
      union_parent(i+1, j+1)

flag = True
for i in range(1, m):
  if find_parent(commands[i-1]) != find_parent(commands[i]):
    flag = False
    break
print("YES" if flag else "NO")
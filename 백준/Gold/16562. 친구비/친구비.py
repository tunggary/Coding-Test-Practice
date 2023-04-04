import sys
from collections import defaultdict

n,m,k = map(int, sys.stdin.readline().split())
costs = list(map(int, sys.stdin.readline().split()))
parents = [i for i in range(n+1)]
relations = defaultdict(lambda: int(1e9))

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
  a,b = map(int, sys.stdin.readline().split())
  if find_parent(a) != find_parent(b):
    union_parent(a, b)
    
for i in range(1, n+1):
  parent = find_parent(i)
  relations[parent] = min(relations[parent], costs[i-1])

answer = sum(relations.values())
print(answer if answer <= k else "Oh no")
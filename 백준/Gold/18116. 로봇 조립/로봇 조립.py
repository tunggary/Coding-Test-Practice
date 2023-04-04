import sys

n = int(sys.stdin.readline())
MAX = int(1e6) + 1
parents = [i for i in range(MAX)]
counts = [1]*(MAX)

def find_parent(x):
  if parents[x] != x:
    parents[x] = find_parent(parents[x])
  return parents[x]

def union_parent(a, b):
  a = find_parent(a)
  b = find_parent(b)
  if a < b:
    parents[b] = a
    counts[a] += counts[b]
  else:
    parents[a] = b
    counts[b] += counts[a]
    
for _ in range(n):
  inputs = sys.stdin.readline().split()
  if inputs[0] == 'I':
    if find_parent(int(inputs[1])) != find_parent(int(inputs[2])):
      union_parent(int(inputs[1]), int(inputs[2]))
  else:
    print(counts[find_parent(int(inputs[1]))])
import sys

n = int(sys.stdin.readline())
g = int(sys.stdin.readline())
parents = [i for i in range(n+1)]
entrance = [0]*(n+1)

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
    
def set_entrance(num):
  num = find_parent(num)
  entrance[num] = 1
  union_parent(num, num-1)

for _ in range(g):
  num = int(sys.stdin.readline())
  if find_parent(num) == 0:
    break
  set_entrance(num)
print(sum(entrance[1:]))
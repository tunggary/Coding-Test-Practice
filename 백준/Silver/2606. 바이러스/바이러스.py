n = int(input())
m = int(input())

def find_parent(parent,a):
  if parent[a] != a:
    parent[a] = find_parent(parent, parent[a])
  return parent[a]

def union_parent(parent, a, b):
  a = find_parent(parent,a)
  b = find_parent(parent, b)
  if a > b:
    parent[a] = b
  else:
    parent[b] = a
  
  
parent = [0]*(n+1)
for i in range(1,n+1):
  parent[i] = i

    
for _ in range(m):
  a,b = map(int, input().split())
  union_parent(parent,a,b)

count = 0    
for i in range(1,n+1):
  if find_parent(parent, i) == 1:
    count += 1
    
print(count-1)
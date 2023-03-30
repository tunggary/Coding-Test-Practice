import sys

n,m,r = map(int, sys.stdin.readline().split())
items = list(map(int, sys.stdin.readline().split()))
INF = int(1e9)
graph = [[INF]*(n) for _ in range(n)]
answer = 0

for _ in range(r):
  a,b,c = map(int, sys.stdin.readline().split())
  graph[a-1][b-1] = c
  graph[b-1][a-1] = c

for i in range(n):
  graph[i][i] = 0
  
for k in range(n):
  for i in range(n):
    for j in range(n):
      graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
  
for i in range(n):
  temp = 0
  for j in range(n):
    if graph[i][j] <= m:
      temp += items[j]
  answer = max(answer, temp)
print(answer)
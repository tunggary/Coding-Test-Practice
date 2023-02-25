import sys
from collections import deque

n,l,r = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dir = [(0,1), (0,-1), (1,0), (-1,0)]
answer = 0


def bfs(start, visited):
  x, y = start
  q = deque([start])
  visited[x][y] = 1
  count = 1
  sum = graph[x][y]
  union = [(x,y)]
  
  while q:
    x, y = q.popleft()
    for dx, dy in dir:
      nx, ny = x + dx, y + dy
      if nx < 0 or nx >= n or ny < 0 or ny >= n:
        continue
      if visited[nx][ny] == 1:
        continue
      if l <= abs(graph[nx][ny] - graph[x][y]) <= r:
        visited[nx][ny] = 1
        q.append((nx, ny))
        count += 1
        sum += graph[nx][ny]
        union.append((nx,ny))
  return (union, sum//count)

while True:
  visited = [[0] * n for _ in range(n)]
  union_list = []
  count = 0
  for i in range(n):
    for j in range(n):
      if visited[i][j] == 0:
        union_list.append(bfs((i,j), visited))
        count += 1
  if count == n*n:
    break
  answer += 1
  for union, value in union_list:
    for x, y in union:
      graph[x][y] = value

print(answer)
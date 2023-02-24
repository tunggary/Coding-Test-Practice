import sys
from collections import deque

n,m = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
answer = [[-1] * m for _ in range(n)]
dir = [(0,1), (0,-1), (1,0), (-1,0)]

def bfs(start):
  x, y = start
  q = deque([(start, 0)])
  graph[x][y] = -1
  
  while q:
    (x, y), dist = q.popleft()
    answer[x][y] = dist
    for dx,dy in dir:
      nx = x + dx
      ny = y + dy
      if 0<=nx<n and 0<=ny<m and graph[nx][ny] == 1:
        graph[nx][ny] = -1
        q.append(((nx,ny), dist+1))

for i in range(n):
  for j in range(m):
    if graph[i][j] == 2:
      bfs((i,j))
    elif graph[i][j] == 0:
      answer[i][j] = 0
      
for i in range(n):
  print(' '.join(map(str, answer[i])))
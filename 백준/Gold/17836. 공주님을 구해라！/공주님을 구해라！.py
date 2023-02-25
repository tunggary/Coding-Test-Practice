import sys
from collections import deque

INF = 10001
n,m,t = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
distance = [[-1]*m for _ in range(n)]
dir = [(0,1), (0,-1), (1,0), (-1,0)]
gx, gy = 0,0
x, y = 0,0


for i in range(n):
  for j in range(m):
    if graph[i][j] == 2:
      gx, gy = i, j

def bfs(start):
  x, y = start
  q = deque([(x,y)])
  distance[x][y] = 0
  
  while q:
    x, y = q.popleft()
    for dx, dy in dir:
      nx, ny = x+dx, y+dy
      if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue
      if graph[nx][ny] == 1 or distance[nx][ny] != -1:
        continue
      distance[nx][ny] = distance[x][y] + 1
      q.append((nx,ny))
   
  min_distance = INF
  if distance[-1][-1] != -1:
    min_distance = min(min_distance, distance[-1][-1])
  if distance[gx][gy] != -1:
    min_distance = min(min_distance, distance[gx][gy] + abs(gx-(n-1)) + abs(gy-(m-1))) 
  
  if min_distance == INF:
    return "Fail"
  return min_distance if min_distance <= t else "Fail"
      
print(bfs((0,0)))
  
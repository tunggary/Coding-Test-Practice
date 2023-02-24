import sys
from collections import deque

n = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
dir = [(0,1), (0,-1), (1,0), (-1,0)]
answer = []

def bfs(start, visited):
  x,y = start
  visited[x][y] = True
  q = deque([(x,y)])
  count = 1
  
  while q:
    x, y = q.popleft()
    for dx, dy in dir:
      nx = x + dx
      ny = y + dy
      if 0<=nx<n and 0<=ny<n and not visited[nx][ny] and graph[nx][ny] == 1:
        visited[nx][ny] = True
        q.append((nx,ny))
        count += 1
        
  return count

for i in range(n):
  for j in range(n):
    if graph[i][j] == 1 and not visited[i][j]:
      answer.append(bfs((i,j), visited))
      
print(len(answer))
print('\n'.join(map(str, sorted(answer))))
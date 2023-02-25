import sys
from collections import deque

m,n = map(int, sys.stdin.readline().split())
box = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
q = deque()
dir = [(0,1), (0,-1), (1,0), (-1,0)]

def bfs():   
  while q:
    x, y = q.popleft()
    for dx, dy in dir:
      nx, ny = x + dx, y + dy
      if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue
      if box[nx][ny] != 0:
        continue
      box[nx][ny] = box[x][y] + 1
      q.append((nx, ny))
        
def find_max():
  answer = 0
  for i in range(n):
    for j in range(m):
      if box[i][j] == 0:
        return -1
      answer = max(answer, box[i][j])
  return answer - 1

def find_tomato():
  for i in range(n):
    for j in range(m):
      if box[i][j] == 1:
        q.append((i,j))
  
find_tomato()
bfs()
print(find_max())
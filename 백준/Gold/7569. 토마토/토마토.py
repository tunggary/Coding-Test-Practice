import sys
from collections import deque

m,n,h = map(int, sys.stdin.readline().split())
box = [[list(map(int, sys.stdin.readline().split())) for _ in range(n)] for _ in range(h)]
q = deque()
dir = [(0,1,0), (0,-1,0), (1,0,0), (-1,0,0), (0,0,1), (0,0,-1)]

def find_tomato():
  for i in range(h):
    for j in range(n):
      for k in range(m):
        if box[i][j][k] == 1:
          q.append((i,j,k))

def bfs():
  while q:
    z, y, x = q.popleft()
    for dz, dy, dx in dir:
      nz, ny, nx = z + dz, y + dy, x + dx
      if nz < 0 or nz >= h or ny < 0 or ny >= n or nx < 0 or nx >= m:
        continue
      if box[nz][ny][nx] != 0:
        continue
      box[nz][ny][nx] = box[z][y][x] + 1
      q.append((nz, ny, nx))

def find_max():
  answer = 0
  for i in range(h):
    for j in range(n):
      for k in range(m):
        if box[i][j][k] == 0:
          return -1
        answer = max(answer, box[i][j][k])
  return answer - 1
    
find_tomato()
bfs()
print(find_max())
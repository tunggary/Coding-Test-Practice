import sys
from itertools import combinations
from collections import deque

n,m = map(int, sys.stdin.readline().strip().split())
lab = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
virus = []
empty = []
dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]

for i in range(n):
  for j in range(m):
    if lab[i][j] == 2:
      virus.append((i,j))
    elif lab[i][j] == 0:
      empty.append((i,j))
      
def spread_virus(visited):
  queue = deque([])
  for i, j in virus:
    queue.append((i, j))
    visited[i][j] = True
  
  while queue:
    x, y = queue.popleft()
    for dx, dy in dir:
      nx = x + dx
      ny = y + dy
      if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue
      if lab[nx][ny] == 1:
        continue
      if visited[nx][ny]:
        continue
      visited[nx][ny] = True
      queue.append((nx, ny))
  return visited

def get_safe_area(new_walls):
  visited = [[False] * m for _ in range(n)]
  for i, j in new_walls:
    lab[i][j] = 1
  visited = spread_virus(visited)
  count = 0
  for i in range(n):
    for j in range(m):
      if lab[i][j] == 0 and visited[i][j] == False:
        count += 1
  for i, j in new_walls:
    lab[i][j] = 0
  return count

def get_answer():
  answer = 0
  for new_walls in combinations(empty, 3):
    answer = max(answer, get_safe_area(new_walls))
  return answer

print(get_answer())
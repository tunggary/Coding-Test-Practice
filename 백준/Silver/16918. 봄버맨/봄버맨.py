import sys

r,c,n = map(int, sys.stdin.readline().split())
graph = [list(sys.stdin.readline().strip()) for _ in range(r)]
count = 1
dir = [(0,1), (0,-1), (1,0), (-1,0)]
        
def explode_bomb(prev_graph):
  for x in range(r):
    for y in range(c):
      if prev_graph[x][y] == '.':
        prev_graph[x][y] = 'N'
        continue
      if prev_graph[x][y] == 'B':
        continue
      prev_graph[x][y] = 'B'
      for dx, dy in dir:
        nx = x + dx
        ny = y + dy
        if 0<=nx<r and 0<=ny<c and prev_graph[nx][ny] != 'O':
          prev_graph[nx][ny] = 'B'
  return [['.' if prev_graph[i][j] == 'B' else 'O' for j in range(c)] for i in range(r)]
          
def print_map(graph):
  for i in range(r):
    for j in range(c):
      print(graph[i][j], end='')
    print()
    
if n == 1:
  print_map(graph)
elif n % 4 == 3:
  next = explode_bomb(graph)
  print_map(next)
elif n % 4 == 1:
  next = explode_bomb(graph)
  next = explode_bomb(next)
  print_map(next)
else:
  print_map([['O'] * c for _ in range(r)])
  
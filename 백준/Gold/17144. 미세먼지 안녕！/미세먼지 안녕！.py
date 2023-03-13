import sys

r,c,t = map(int, sys.stdin.readline().split())

graph = [list(map(int, sys.stdin.readline().split())) for _ in range(r)]

air_cleaner = []

for i in range(r):
  for j in range(c):
    if graph[i][j] == -1:
      air_cleaner.append((i,j))

def spread_dust(graph):
  new_graph = [[0]*c for _ in range(r)]
  for x in range(r):
    for y in range(c):
      if graph[x][y] < 0:
        new_graph[x][y] = -1
        continue
      if graph[x][y] > 0:
        spread = graph[x][y]//5
        for dx, dy in [(0,1), (0,-1), (-1,0), (1,0)]:
          nx, ny = x+dx, y+dy
          if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] != -1:
            new_graph[nx][ny] += spread
            graph[x][y] -= spread
        new_graph[x][y] += graph[x][y]
  return new_graph

def move_top_dust(graph, x, y):
  temp = 0
  for i in range(y+1, c):
    prev = graph[x][i]
    graph[x][i] = temp
    temp = prev
  
  for j in range(x-1, -1, -1):
    prev = graph[j][c-1]
    graph[j][c-1] = temp
    temp = prev
    
  for i in range(c-2, y-1, -1):
    prev = graph[0][i]
    graph[0][i] = temp
    temp = prev
  
  for j in range(1, x):
    prev = graph[j][y]
    graph[j][y] = temp
    temp = prev
    
  return graph

def move_bottom_dust(graph, x, y):
  temp = 0
  for i in range(y+1, c):
    prev = graph[x][i]
    graph[x][i] = temp
    temp = prev
  
  for j in range(x+1, r):
    prev = graph[j][c-1]
    graph[j][c-1] = temp
    temp = prev
    
  for i in range(c-2, y-1, -1):
    prev = graph[r-1][i]
    graph[r-1][i] = temp
    temp = prev
    
  for j in range(r-2, x, -1):
    prev = graph[j][y]
    graph[j][y] = temp
    temp = prev
    
  return graph

while t > 0:
  graph = spread_dust(graph)
  graph = move_top_dust(graph, air_cleaner[0][0], air_cleaner[0][1])
  graph = move_bottom_dust(graph, air_cleaner[1][0], air_cleaner[1][1])
  t -= 1
print(sum(map(sum, graph))+2)
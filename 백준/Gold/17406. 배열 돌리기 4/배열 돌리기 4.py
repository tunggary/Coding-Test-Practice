import sys
from itertools import permutations

n,m,k = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
operate = [list(map(int, sys.stdin.readline().split())) for _ in range(k)]
INF = 1_000_000_000

def rotate(x,y,s,graph):
  row, col = x-s-1, y-s-1
  temp = graph[row][col]
  for j in range(y-s, y+s):
    col = j
    prev = graph[row][col]
    graph[row][col] = temp
    temp = prev
  for i in range(x-s, x+s):
    row = i
    prev = graph[row][col]
    graph[row][col] = temp
    temp = prev
  for j in range(y-s, y+s):
    col = 2*y - j - 2
    prev = graph[row][col]
    graph[row][col] = temp
    temp = prev
  for i in range(x-s, x+s):
    row = 2*x - i - 2
    prev = graph[row][col]
    graph[row][col] = temp
    temp = prev
  return graph

answer = INF
for order in permutations(operate, k):
  new_graph = [row[:] for row in graph]
  for x,y,s in order:
    for i in range(1, s+1):
      new_graph = rotate(x,y,i,new_graph)
  min_array = INF
  for i in range(n):
    min_array = min(min_array, sum(new_graph[i]))
  answer = min(answer, min_array)

print(answer)
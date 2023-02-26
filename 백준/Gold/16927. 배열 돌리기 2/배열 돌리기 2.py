import sys
from collections import deque

N,M,R = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
border_list = []

for r in range(min(N,M)//2):
  border = deque([])
  row,col = r,r
  for i in range(r+1, N-r):
    row = i
    border.append(graph[row][col])
  for j in range(r+1, M-r):
    col = j
    border.append(graph[row][col])
  for i in range(r+1, N-r):
    row = N - i - 1
    border.append(graph[row][col])
  for j in range(r+1, M-r):
    col = M - j - 1
    border.append(graph[row][col])
  border_list.append(border)

for border in border_list:
  border.rotate(R % len(border))

for i in range(min(N,M)//2):
  border = border_list[i]
  row,col = i,i
  for j in range(i+1, N-i):
    row = j
    graph[row][col] = border.popleft()
  for j in range(i+1, M-i):
    col = j
    graph[row][col] = border.popleft()
  for j in range(i+1, N-i):
    row = N - j - 1
    graph[row][col] = border.popleft()
  for j in range(i+1, M-i):
    col = M - j - 1
    graph[row][col] = border.popleft()

for i in range(N):
  print(' '.join(map(str, graph[i])))
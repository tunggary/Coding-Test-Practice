import sys

n = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited = [False] * n
answer = 1000000000
start = 0

def backtracking(count, current, cost):
  global answer
  if cost > answer:
    return
  if count == n and graph[current][start] != 0:
    answer = min(answer, cost + graph[current][start])
    return
  for i in range(n):
    if not visited[i] and graph[current][i] != 0:
      visited[i] = True
      backtracking(count+1, i, cost + graph[current][i])
      visited[i] = False

for i in range(n):
  start = i
  visited[start] = True
  backtracking(1, i, 0)
  visited[start] = False
  
print(answer)
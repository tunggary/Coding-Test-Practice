import sys
from collections import deque

n,m = map(int, sys.stdin.readline().split())
visited = [0] * 100_001

def bfs():
  q = deque([(n,0)])
  visited[n] = 1
  
  while q:
    x, count = q.popleft()
    if x == m:
      return count
    for step in [2*x, x-1, x+1]:
      if 0 <= step <= 100_000 and visited[step] == 0:
        if step == 2*x:
          q.appendleft((step, count))
        else:
          q.append((step, count+1))
        visited[step] = 1
  
print(bfs())
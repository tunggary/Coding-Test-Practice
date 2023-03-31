import sys
from collections import deque

t = int(sys.stdin.readline())

def solve():
  n,k = map(int, sys.stdin.readline().split())
  craft_time = [0] + list(map(int, sys.stdin.readline().split()))
  indegree = [0]*(n+1)
  graph = [[] for _ in range(n+1)]  
  for _ in range(k):
    a,b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    indegree[b] += 1
  building_number = int(sys.stdin.readline())
  dp = [0]*(n+1)
  
  q = deque()
  for i in range(1, n+1):
    dp[i] = craft_time[i]
    if indegree[i] == 0:
      q.append(i)
  
  while q:
    now = q.popleft()
    for i in graph[now]:
      indegree[i] -= 1
      dp[i] = max(dp[now] + craft_time[i], dp[i])
      if indegree[i] == 0:
        q.append(i)
        
  return dp[building_number]
  
for _ in range(t):
  print(solve())
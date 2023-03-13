import sys

n,m = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))
array.sort()
visited = [False] * (n+1)

def backtracking(depth, current):
  if depth > m:
    print(current[:-1])
    return
  for i in range(n):
    if not visited[i]:
      visited[i] = True
      backtracking(depth+1, current+str(array[i])+' ')
      visited[i] = False
      
backtracking(1, '')
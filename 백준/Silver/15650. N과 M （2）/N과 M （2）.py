import sys

n,m = map(int, sys.stdin.readline().split())

visited = [False] * (n+1)

def backtracking(depth, current, min):
  if depth > m:
    print(' '.join(list(current)))
    return
  for i in range(min, n+1):
    if not visited[i]:
      visited[i] = True
      backtracking(depth+1, current+str(i), i)
      visited[i] = False

backtracking(1, '', 1)

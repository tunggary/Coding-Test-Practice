import sys

n,m = map(int, sys.stdin.readline().split())

def backtracking(depth, current, min):
  if depth > m:
    print(' '.join(list(current)))
    return
  for i in range(min, n+1):
    backtracking(depth+1, current+str(i), i)


backtracking(1, '', 1)

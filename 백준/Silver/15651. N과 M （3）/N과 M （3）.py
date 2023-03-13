import sys

n,m = map(int, sys.stdin.readline().split())

def backtracking(depth, current):
  if depth > m:
    print(' '.join(list(current)))
    return
  for i in range(1, n+1):
    backtracking(depth+1, current+str(i))

backtracking(1, '')
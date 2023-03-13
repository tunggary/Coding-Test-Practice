import sys

n,m = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))
array.sort()

def backtracking(depth, current, min):
  if depth > m:
    print(current[:-1])
    return
  for i in range(min, n):
    backtracking(depth+1, current+str(array[i])+' ', i)
      
backtracking(1, '', 0)
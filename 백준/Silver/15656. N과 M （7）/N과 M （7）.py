import sys

n,m = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))
array.sort()

def backtracking(depth, current):
  if depth > m:
    print(current[:-1])
    return
  for i in range(n):
    backtracking(depth+1, current+str(array[i])+' ')

      
backtracking(1, '')
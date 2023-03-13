import sys

n,m = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))
array.sort()

def backtracking(depth, current):
  if depth > m:
    print(current[:-1])
    return
  prev = -1
  for i in range(n):
    if prev == array[i]:
        continue
    prev = array[i]
    backtracking(depth+1, current+str(array[i])+' ')
      
backtracking(1, '')
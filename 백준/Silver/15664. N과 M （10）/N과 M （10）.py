import sys

n,m = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))
array.sort()
visited = [False] * n

def backtracking(depth, current, min):
  if depth > m:
    print(current[:-1])
    return
  prev = -1
  for i in range(min, n):
    if not visited[i]:
      if prev == array[i]:
        continue
      prev = array[i]
      visited[i] = True
      backtracking(depth+1, current+str(array[i])+' ', i)
      visited[i] = False
      
backtracking(1, '', 0)
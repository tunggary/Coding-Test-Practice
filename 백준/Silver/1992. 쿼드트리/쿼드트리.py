import sys
n = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]

def check(len,row,col):
  data = graph[row][col]
  for i in range(len):
    for j in range(len):
      if graph[row+i][col+j] != data:
        return None
  return data

def dfs(len,row,col):
  value = check(len,row,col)
  if value == 0:
    print("0", end="")
  elif value == 1:
    print("1", end="")
  else:
    half = len // 2
    print("(", end="")
    dfs(half,row,col)
    dfs(half,row,col+half)
    dfs(half,row+half,col)
    dfs(half,row+half,col+half)
    print(")", end="")
dfs(n,0,0)
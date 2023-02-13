import sys

n = int(sys.stdin.readline().strip())
board = [list(map(int,sys.stdin.readline().strip().split())) for _ in range(n)]
dp = [[0]*n for _ in range(n)]

def find(x, y):
  count = 0
  for i in range(x):
    if board[i][y] + i == x:
      count += dp[i][y]
  for i in range(y):
    if board[x][i] + i == y:
      count += dp[x][i]
  return count

for x in range(n):
  for y in range(n):
    if x == 0 and y == 0:
      dp[x][y] = 1
    else:
      dp[x][y] = find(x,y)
    
print(dp[n-1][n-1])
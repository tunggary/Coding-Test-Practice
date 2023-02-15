import sys

n = int(sys.stdin.readline().strip())

matrix = [[0]+list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
matrix.insert(0, [0]*(n+1))

dp = [[[0]*3 for _ in range(n+1)] for _ in range(n+1)]
dp[1][2][0] = 1

for i in range(3, n+1):
  if matrix[1][i] == 0:
    dp[1][i][0] = dp[1][i-1][0]

for i in range(2, n+1):
  for j in range(2, n+1):
    if matrix[i][j] == 0:
      dp[i][j][0] = dp[i][j-1][0] + dp[i][j-1][2]
      dp[i][j][1] = dp[i-1][j][1] + dp[i-1][j][2]
    if matrix[i][j] == 0 and matrix[i-1][j] == 0 and matrix[i][j-1] == 0:
      dp[i][j][2] = dp[i-1][j-1][0] + dp[i-1][j-1][1] + dp[i-1][j-1][2]

print(sum(dp[n][n]))


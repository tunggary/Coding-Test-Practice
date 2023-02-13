import sys

n,k = map(int, sys.stdin.readline().strip().split())
array = list(map(int, sys.stdin.readline().strip().split()))
array = [0] + array
dp = [[0]*(k+1) for _ in range(n+1)]

for i in range(1, n+1):
  for j in range(k+1):
    if array[i] % 2 == 0:
      dp[i][j] = dp[i-1][j] + 1
    else:
      if j == 0:
        dp[i][j] = 0
      else:
        dp[i][j] = dp[i-1][j-1]
    
print(max([dp[i][k] for i in range(1, n+1)]))

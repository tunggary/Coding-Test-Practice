import sys


n,k = map(int, sys.stdin.readline().strip().split())
array = list(map(int, sys.stdin.readline().strip().split()))
array = [0] + array
dp = [0]*(n+1)
dp = [[0]*(k+1) for _ in range(n+1)]

for i in range(1, n+1):
  if array[i] % 2 == 0:
    dp[i][0] = dp[i-1][0] + 1
  else:
    dp[i][0] = 0

for i in range(1, n+1):
  for j in range(1, k+1):
    if array[i] % 2 == 0:
      dp[i][j] = dp[i-1][j] + 1
    else:
      dp[i][j] = dp[i-1][j-1]
      
answer = 0
for i in range(1, n+1):
  if answer < dp[i][k]:
    answer = dp[i][k]
    
print(answer)

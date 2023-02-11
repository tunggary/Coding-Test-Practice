import sys

n = int(sys.stdin.readline().strip())
stairs = [int(sys.stdin.readline().strip()) for _ in range(n)]

dp = [0]*301

for i in range(1,n+1):
  if i == 1:
    dp[i] = stairs[i-1]
  elif i == 2:
    dp[i] = dp[i-1]+stairs[i-1]
  else:
    dp[i] = max(dp[i-2], dp[i-3]+stairs[i-2]) + stairs[i-1]
  
print(dp[n])
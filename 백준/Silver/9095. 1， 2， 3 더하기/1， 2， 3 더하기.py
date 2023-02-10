import sys

t = int(sys.stdin.readline().strip())

dp = [0] * 11
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, len(dp)):
  dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for _ in range(t):
  n = int(sys.stdin.readline().strip())
  print(dp[n])
  
import sys

n = int(sys.stdin.readline().strip())

INF = 1e9
dp = [INF] * 5001
dp[3] = 1
dp[5] = 1

for i in range(6, n+1):
  dp[i] = min(dp[i-3], dp[i-5]) + 1

print(-1 if dp[n] >= INF else dp[n])
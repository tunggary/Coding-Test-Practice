import sys

t = int(sys.stdin.readline().strip())

def solve():
  n, m = map(int, sys.stdin.readline().strip().split())
  dp = [[0] * (m+1) for _ in range(n+1)]
  
  for i in range(1, n+1):
    for j in range(i, m+1):
      if i > j:
        continue
      if i == 1:
        dp[i][j] = j
      else:
        for k in range(j, i-1, -1):
          dp[i][j] += dp[i-1][k-1]
  print(dp[n][m])

for _ in range(t):
  solve()
  
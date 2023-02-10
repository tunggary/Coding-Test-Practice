import sys

n = int(sys.stdin.readline().strip())

dp = [0] * (n+1)

for i in range(2, n+1):
  case1, case2, case3 = 1e9, 1e9, 1e9
  if i % 2 == 0:
    case1 = dp[i//2]
  if i % 3 == 0:
    case2 = dp[i//3]
  case3 = dp[i-1]
  dp[i] = min(case1, case2, case3) + 1
  
print(dp[n])
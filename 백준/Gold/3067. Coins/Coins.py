import sys

def solve():
  n = int(sys.stdin.readline().strip())
  coins = list(map(int, sys.stdin.readline().strip().split()))
  target = int(sys.stdin.readline().strip())
  dp = [0]*(target+1)
  dp[0] = 1
  
  for i in range(n):
    for j in range(1, target+1):
      if j - coins[i] >= 0:
        dp[j] += dp[j-coins[i]]
      
  print(dp[target])
  

t = int(sys.stdin.readline().strip())
for _ in range(t):
  solve()
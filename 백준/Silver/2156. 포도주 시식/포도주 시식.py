import sys

n = int(sys.stdin.readline().strip())
wines = [int(sys.stdin.readline().strip()) for _ in range(n)]
dp = [0]*n

for i in range(n):
  if i == 0:
    dp[i] = wines[0]
  elif i == 1:
    dp[i] = wines[0]+wines[1]
  elif i == 2:
    dp[i] = max(wines[0]+wines[1], wines[0]+wines[2], wines[1]+wines[2])
  else:
    dp[i] = max(dp[i-2]+wines[i], dp[i-3]+wines[i-1]+wines[i], dp[i-1]) 
  
print(max(dp))
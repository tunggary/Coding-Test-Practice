import sys

n = int(sys.stdin.readline().strip())
array = list(map(int,sys.stdin.readline().strip().split()))

max_value = array[0]
dp = [0]*n
dp[0] = array[0]
for i in range(1, n):
  dp[i] = max(dp[i-1]+array[i], array[i])
  max_value = max(max_value, dp[i])   
print(max_value)
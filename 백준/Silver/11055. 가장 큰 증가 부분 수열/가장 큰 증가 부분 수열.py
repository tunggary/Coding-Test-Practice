import sys

n = int(sys.stdin.readline().strip())
array = list(map(int,sys.stdin.readline().strip().split()))

dp = array[:]

for i in range(1, n):
  for j in range(i):
    if array[i] > array[j]:
      dp[i] = max(dp[j] + array[i], dp[i])      
print(max(dp))
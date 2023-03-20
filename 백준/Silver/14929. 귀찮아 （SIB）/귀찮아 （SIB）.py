import sys

n = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split()))

culmulative_sum = [0]*n
for i in range(n):
  if i == 0:
    culmulative_sum[i] = sum(array)
  else:
    culmulative_sum[i] = culmulative_sum[i-1] - array[i-1]
  
answer = 0
for i in range(n-1):
  answer += array[i] * culmulative_sum[i+1]
print(answer)
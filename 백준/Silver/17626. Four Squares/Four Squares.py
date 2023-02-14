import sys

n = int(sys.stdin.readline().strip())
MAX = 1e9
dp = [MAX]*50001
dp[0] = 0

def find(num):
  for i in range(1, int(num**0.5)+1):
    dp[i*i] = 1
  
  if dp[num] == 1:
    return 1
  
  for i in range(1, int(num**0.5)+1):
    if dp[num - i*i] == 1:
      return 2
    
  for i in range(1, int(num**0.5)+1):
    for j in range(1, int((num-i*i)**0.5)+1):
      if dp[num - i*i - j*j] == 1:
        return 3
      
  return 4

print(find(n))
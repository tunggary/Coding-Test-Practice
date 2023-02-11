import sys

dp = [0]*101

def factorial(n):
  if n == 0:
    return 1
  elif dp[n] != 0:
    return dp[n]
  else:
    dp[n] = n*factorial(n-1)
    return dp[n]

n,m = map(int,sys.stdin.readline().strip().split())

print(factorial(n)//(factorial(m)*factorial(n-m)))
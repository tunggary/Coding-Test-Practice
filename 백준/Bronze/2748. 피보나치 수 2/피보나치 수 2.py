import sys

n = int(sys.stdin.readline().strip())

dp = [0] * (n+1)

def 피보나치(n):
  if n == 0 or n == 1:
    return n
  if dp[n] != 0:
    return dp[n]
  dp[n] = 피보나치(n-1) + 피보나치(n-2)
  return dp[n]

print(피보나치(n))
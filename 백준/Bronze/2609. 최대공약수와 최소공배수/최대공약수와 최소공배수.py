import sys
import math

n, m = map(int, sys.stdin.readline().strip().split())

def gcd(a, b):
  if b == 0:
    return a
  return gcd(b, a % b)

print(gcd(n, m))
print(math.lcm(n,m))
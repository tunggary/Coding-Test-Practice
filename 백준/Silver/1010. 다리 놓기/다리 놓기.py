import sys
from math import factorial

t = int(sys.stdin.readline().strip())

def solve():
  n, m = map(int, sys.stdin.readline().strip().split())
  print(int(factorial(m) / (factorial(n)*factorial(m-n))))

for _ in range(t):
  solve()
  
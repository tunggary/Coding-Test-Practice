import sys
import math

n = int(sys.stdin.readline().strip())
numbers = list(map(int, sys.stdin.readline().strip().split()))
if n == 2:
  gcd = math.gcd(numbers[0], numbers[1])
else:
  gcd = math.gcd(numbers[0], numbers[1], numbers[2])

for i in range(1, gcd+1):
  if gcd % i == 0:
    print(i)

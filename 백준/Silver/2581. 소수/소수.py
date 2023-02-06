
import sys

m = int(sys.stdin.readline().strip())
n = int(sys.stdin.readline().strip())

MAX = 10_000
prime_number = [True]*(MAX+1)
prime_number[1] = False
def set_prime_number():
  for i in range(2, int(MAX**0.5)+1):
    if prime_number[i]:
      for j in range(i+i, MAX+1, i):
        prime_number[j] = False
        
set_prime_number()

sum = 0
min = 0
for i in range(m, n+1):
  if prime_number[i]:
    if sum == 0:
      min = i
    sum += i
print(-1 if sum == 0 else f"{sum}\n{min}")
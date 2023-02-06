import sys

n = int(sys.stdin.readline())

prime = [True]*(n+1)

for i in range(2, int(n**0.5)+1):
  if prime[i]:
    for j in range(i+i, n+1, i):
      prime[j] = False

while n > 1:
  for i in range(2, n+1):
    if prime[i] and n % i == 0:
      print(i)
      n //= i
      break

import sys

n = int(sys.stdin.readline().strip())
dists = list(map(int, sys.stdin.readline().strip().split()))
prices = list(map(int, sys.stdin.readline().strip().split()))

answer = 0
min = prices[0]

for i in range(n-1):
  if prices[i] < min:
    min = prices[i]
  answer += min * dists[i]
  
print(answer)
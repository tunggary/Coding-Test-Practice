import sys

n,k = map(int,sys.stdin.readline().strip().split())
coins = [int(sys.stdin.readline().strip()) for _ in range(n)]
coins.reverse()
answer = 0
for coin in coins:
  answer += k // coin
  k %= coin
  
print(answer)  

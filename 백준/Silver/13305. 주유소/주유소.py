import sys

n = int(sys.stdin.readline().strip())
distances = list(map(int, sys.stdin.readline().strip().split()))
prices = [ (price, i) for i, price  in enumerate(map(int, sys.stdin.readline().strip().split()[:-1]))]

prices.sort()
answer = 0
min_index = n
min_price = 1000000000
for price, index in prices:
  if index > min_index:
    answer += min_price * distances[index]
    continue
  min_price = price
  min_index = index
  answer += min_price * distances[index]
  
print(answer)
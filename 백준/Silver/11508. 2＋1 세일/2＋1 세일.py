import sys

n = int(sys.stdin.readline().strip())
products = [int(sys.stdin.readline().strip()) for _ in range(n)]
products.sort(reverse=True)
answer = sum(products)
for i in range(2, len(products),3):
  if i < len(products):
    answer -= products[i]
    
print(answer)

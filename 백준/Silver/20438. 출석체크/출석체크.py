import sys

n,k,q,m = map(int, sys.stdin.readline().split())
sleeps = set(map(int, sys.stdin.readline().split()))
codes = list(map(int, sys.stdin.readline().split()))
queries = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
check = [0] * (n+3)
sum_array = [0] * (n+3)

for code in codes:
  if code in sleeps:
    continue
  for i in range(code, n+3, code):
    if i in sleeps:
      continue
    check[i] = 1

for i in range(3, n+3):
  sum_array[i] = sum_array[i-1] +  (1 if check[i] == 0 else 0)
      
for query in queries:
  print(sum_array[query[1]] - sum_array[query[0]-1])

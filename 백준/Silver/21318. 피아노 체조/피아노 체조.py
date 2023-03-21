import sys

n = int(sys.stdin.readline())
levels = list(map(int, sys.stdin.readline().split()))
q = int(sys.stdin.readline())
queries = [list(map(int, sys.stdin.readline().split())) for _ in range(q)]
array_sum = [0] * (n+1)

for i in range(1, n):
  array_sum[i] = array_sum[i-1] + (1 if levels[i-1] > levels[i] else 0)
    
for query in queries:
  i,j = query
  print(array_sum[j-1] - array_sum[i-1])
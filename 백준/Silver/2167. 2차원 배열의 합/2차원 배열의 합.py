import sys

n,m = map(int, sys.stdin.readline().split())
array = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
sum_array = [[0] * (m+1) for _ in range(n+1)]
k = int(sys.stdin.readline())
queries = [list(map(int, sys.stdin.readline().split())) for _ in range(k)]

for i in range(1, n+1):
  for j in range(1, m+1):
    sum_array[i][j] = sum_array[i-1][j] + sum_array[i][j-1] - sum_array[i-1][j-1] + array[i-1][j-1]

for query in queries:
  i,j,x,y = query
  print(sum_array[x][y]+sum_array[i-1][j-1]-sum_array[i-1][y]-sum_array[x][j-1])
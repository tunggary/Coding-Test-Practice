import sys

n,s = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))

sum = 0
answer = 100_001
i,j = 0,0

while j < n:
  sum += array[j]
  if sum >= s:
    while sum - array[i] >= s:
      sum -= array[i]
      i += 1
    answer = min(answer, j-i+1)
  j += 1    
print(answer if answer != 100_001 else 0)
import sys

n,k = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))

i, j = 0, 0
count = 0
answer = 0

while j < n:    
  if array[j] % 2 == 1:
    count += 1
    while count > k:
      if array[i] % 2 == 1:
        count -= 1
      i += 1
  answer = max(answer, (j-i+1)-count)
  j += 1

print(answer)
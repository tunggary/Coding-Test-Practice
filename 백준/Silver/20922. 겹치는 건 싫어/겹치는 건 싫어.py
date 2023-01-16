import sys

n,k = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))
count_array = [0] * 100001
i,j = 0,1
count = 1
max_count = count
count_array[array[i]] += 1

while j < n:
  if count_array[array[j]] + 1 <= k:
    count_array[array[j]] += 1
    j += 1
    count += 1
    if count > max_count:
      max_count = count
  else:
    count_array[array[i]] -= 1
    i += 1
    count -= 1
      
print(max_count)
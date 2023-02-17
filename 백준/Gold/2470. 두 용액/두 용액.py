import sys

n = int(sys.stdin.readline().strip())
array = list(map(int, sys.stdin.readline().split()))

i,j = 0, n-1
min_value = 2_000_000_001
answer = ''
array.sort()

while i<j:
  sum_value = array[i] + array[j]
  if abs(sum_value) < min_value:
    min_value = abs(sum_value)
    answer = f'{array[i]} {array[j]}'

  if sum_value < 0:
    i += 1
  else:
    j -= 1
   
print(answer)
  

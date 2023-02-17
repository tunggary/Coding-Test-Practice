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

  if array[i] > 0 and array[j] > 0:
    j -= 1
  elif array[i] < 0 and array[j] < 0:
    i += 1
  else:
    if abs(array[i]) < array[j]:
      j -= 1
    else:
      i += 1
   
print(answer)
 
import sys

n = int(sys.stdin.readline().strip())
numbers = list(map(int, sys.stdin.readline().strip().split()))
check_point = -1

for i in range(n-1, 0, -1):
  if numbers[i] > numbers[i-1]:
    check_point = i-1
    break

if check_point < 0:
  print(-1)
else:
  sorted_numbers = sorted(numbers[check_point+1:])
  for i in range(len(sorted_numbers)):
    if sorted_numbers[i] > numbers[check_point]:
      numbers[check_point], sorted_numbers[i] = sorted_numbers[i], numbers[check_point]
      break
  print(' '.join(map(str,numbers[:check_point+1] + sorted_numbers )))
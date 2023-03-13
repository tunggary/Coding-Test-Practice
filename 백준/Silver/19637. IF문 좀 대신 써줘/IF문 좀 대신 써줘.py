import sys
n,m = map(int, sys.stdin.readline().split())
names = [sys.stdin.readline().split() for _ in range(n)]
numbers = [int(sys.stdin.readline()) for _ in range(m)]

for number in numbers:
  left, right = 0, n-1
  answer = 0
  while left <= right:
    middle = (left + right) // 2
    name, value = names[middle]
    if number <= int(value):
      right = middle - 1
      answer = middle
    else:
      left = middle + 1
  print(names[answer][0])
      
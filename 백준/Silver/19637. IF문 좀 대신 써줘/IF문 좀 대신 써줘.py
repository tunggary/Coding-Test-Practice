import sys

n,m = map(int, sys.stdin.readline().split())
names = [sys.stdin.readline().split() for _ in range(n)]
numbers = [int(sys.stdin.readline()) for _ in range(m)]

for number in numbers:
  start = 0
  end = n - 1
  while start <= end:
    mid = (start + end) // 2
    if number <= int(names[mid][1]):
      end = mid - 1
    else:
      start = mid + 1
  print(names[end+1][0])
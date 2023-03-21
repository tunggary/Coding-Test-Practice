import sys

n = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split()))
answer = 0

total = sum(array)
for i in range(n):
  total -= array[i]
  answer += array[i] * total
print(answer)
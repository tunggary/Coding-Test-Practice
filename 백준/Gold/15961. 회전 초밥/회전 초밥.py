import sys

n,d,k,c = map(int, sys.stdin.readline().split())
array = [int(sys.stdin.readline()) for _ in range(n)]

count = [0] * (d+1)
current = 0
answer = 0

for type in array[:k]+[c]:
  if count[type] == 0:
    current += 1
  count[type] += 1

answer = current
i, j = 1, k

while i != 0:
  count[array[i-1]] -= 1
  if count[array[i-1]] == 0:
    current -= 1
  count[array[j]] += 1
  if count[array[j]] == 1:
    current += 1
  answer = max(answer, current)
  i = (i+1) % n
  j = (j+1) % n
print(answer)
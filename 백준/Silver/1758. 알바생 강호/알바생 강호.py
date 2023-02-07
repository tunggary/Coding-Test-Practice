import sys

n = int(sys.stdin.readline().strip())
people = [int(sys.stdin.readline().strip()) for _ in range(n)]

people.sort(reverse=True)

sum = 0
for i in range(n):
  if people[i] - i < 0:
    break
  sum += people[i] - i
  
print(sum)

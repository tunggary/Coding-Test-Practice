import sys

n = int(sys.stdin.readline().strip())
people = list(map(int, sys.stdin.readline().strip().split()))
people.sort()
waiting = 0
for i in range(len(people)):
  waiting += people[i]
  people[i] = waiting
  
print(sum(people))
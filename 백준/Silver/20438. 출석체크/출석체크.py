import sys

n,k,q,m = map(int, sys.stdin.readline().split())
sleeps = set(map(int, sys.stdin.readline().split()))
check = list(map(int, sys.stdin.readline().split()))
commands = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
presents = [1]*(n+3)

for student in check:
  if student in sleeps:
    continue
  for i in range(student, n+3, student):
    if i in sleeps:
      continue
    presents[i] = 0
    
for i in range(1, n+3):
  presents[i] += presents[i-1]

for start, end in commands:
  print(presents[end] - presents[start-1])
import sys
from collections import deque

n,m = map(int, sys.stdin.readline().strip().split())
trains = [deque([0 for _ in range(20)]) for _ in range(n)]
commnads = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(m)]
answer = set()


for command in commnads:
  if command[0] == 1:
    trains[command[1]-1][command[2]-1] = 1
  elif command[0] == 2:
    trains[command[1]-1][command[2]-1] = 0
  elif command[0] == 3:
    trains[command[1]-1].pop()
    trains[command[1]-1].insert(0, 0)
  elif command[0] == 4:
    trains[command[1]-1].popleft()
    trains[command[1]-1].append(0)

for train in trains:
  key = ' '.join(map(str, train))
  if key in answer:
    continue
  answer.add(key)
print(len(answer))
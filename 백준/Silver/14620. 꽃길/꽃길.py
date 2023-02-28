import sys
from itertools import combinations

n = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
answer = 1_000_000_000
q = []
dir = [(0, 0), (0, 1), (0, -1), (1, 0), (-1, 0)]

for x in range(1, n-1):
  for y in range(1, n-1):
    q.append((x, y))
    
for positions in combinations(q, 3):
  current_position = set()
  plant_sum = 0
  flag = True
  for x, y in positions:
    plant_position = set([(x+dx, y+dy) for dx, dy in dir])
    plant_sum += sum([graph[x][y] for x, y in plant_position])
    if current_position & plant_position:
      flag = False
      break
    current_position |= plant_position
  if flag:
    answer = min(answer, plant_sum)
  
print(answer)
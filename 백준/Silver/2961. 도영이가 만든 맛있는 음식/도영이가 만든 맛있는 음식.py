import sys
from itertools import combinations

n = int(sys.stdin.readline())
foods = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
answer = 1_000_000_000

for i in range(1, n+1):
  for positions in combinations(range(n), i):
    sour = 1
    bitter = 0
    for position in positions:
      sour *= foods[position][0]
      bitter += foods[position][1]
    answer = min(answer, abs(sour - bitter))
      
print(answer)
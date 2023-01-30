import sys
from heapq import heappush, heappop

n = int(sys.stdin.readline())
heap = []

for _ in range(n):
  input = int(sys.stdin.readline())
  if input == 0:
    print(0 if len(heap) == 0 else -heappop(heap))
  else:
    heappush(heap, -input)
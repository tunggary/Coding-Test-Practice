import sys
from heapq import heappush, heappop

n = int(sys.stdin.readline().strip())
meetings = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
rooms = []

for start, end in sorted(meetings):
  if rooms and rooms[0] <= start:
    heappop(rooms)
  heappush(rooms, end)
    
print(len(rooms))
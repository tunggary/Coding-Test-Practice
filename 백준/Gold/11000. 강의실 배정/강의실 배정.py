import sys
from heapq import heappush, heappop

n = int(sys.stdin.readline().strip())
classes = [tuple(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

classes.sort(key=lambda x: (x[0], x[1]))
rooms = []

for start_time, end_time in classes:
  if len(rooms) > 0 and rooms[0] <= start_time:
    heappop(rooms)
  heappush(rooms, end_time)
    
print(len(rooms))
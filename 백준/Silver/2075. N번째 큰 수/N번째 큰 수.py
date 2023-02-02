import sys
from heapq import heappush, heappop

n = int(sys.stdin.readline().strip())
heap = []

for i in range(n):
  array = list(map(int, sys.stdin.readline().split()))
  for num in array:
    if len(heap) < n:
      heappush(heap, num)
    elif num > heap[0]:
      heappush(heap, num)
      heappop(heap)
      
print(heap[0])
import sys
import heapq

n = int(sys.stdin.readline().strip())
drinks = list(map(int, sys.stdin.readline().strip().split()))
heap = []
while drinks:
  heapq.heappush(heap, -heapq.heappop(drinks))

while len(heap) > 1:
  a = heapq.heappop(heap)
  b = heapq.heappop(heap)
  heapq.heappush(heap, -((-a) + (-b) / 2))
  
print(-heap[0])
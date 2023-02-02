import sys
from heapq import heappush, heappop
from collections import defaultdict

t = int(sys.stdin.readline().strip())

for _ in range(t):
  n = int(sys.stdin.readline().strip())
  max_heap = []
  min_heap = []
  sync = defaultdict(int)
  
  for _ in range(n):
    command, num = sys.stdin.readline().split()
    num = int(num)
    
    if command == 'I':
      sync[num] += 1
      heappush(max_heap, -num)
      heappush(min_heap, num)
    else:
      if num == 1:
        while max_heap and sync[-max_heap[0]] <= 0:
          heappop(max_heap)
        if max_heap:
          sync[-heappop(max_heap)] -= 1
      else:
        while min_heap and sync[min_heap[0]] <= 0:
          heappop(min_heap)
        if min_heap:
          sync[heappop(min_heap)] -= 1
  while max_heap and sync[-max_heap[0]] <= 0:
    heappop(max_heap)
  while min_heap and sync[min_heap[0]] <= 0:
    heappop(min_heap)
    
  if len(min_heap) == 0 or len(max_heap) == 0:
    print("EMPTY")
  else:
    print(-max_heap[0], min_heap[0])
      
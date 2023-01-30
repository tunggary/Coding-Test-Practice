#백준 7662번
#아이디어: heap 두개를 어떻게 동기화 시킬것인가가 중요

import sys
from heapq import heappop, heappush

for _ in range(int(sys.stdin.readline())):
  max_heap = []
  min_heap = []
  sync = [False]*1000001
  for i in range(int(sys.stdin.readline())):
    commmand, num = sys.stdin.readline().split()
    if commmand == "I":
      heappush(max_heap, (-int(num), i))
      heappush(min_heap, (int(num), i))
      sync[i] = True
    else:
      if num == '1':
        while max_heap and not sync[max_heap[0][1]]:
          heappop(max_heap)
        if max_heap:
          sync[max_heap[0][1]] = False
          heappop(max_heap)
      else:
        while min_heap and not sync[min_heap[0][1]]:
          heappop(min_heap)
        if min_heap:
          sync[min_heap[0][1]] = False
          heappop(min_heap)
          
  while max_heap and not sync[max_heap[0][1]]:
    heappop(max_heap)
  while min_heap and not sync[min_heap[0][1]]:
    heappop(min_heap)
  if min_heap and max_heap:
    print(-max_heap[0][0], min_heap[0][0])
  else:
    print("EMPTY")
import sys
from heapq import heappush, heappop

n = int(sys.stdin.readline())
# array = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
# count = [n-1]*n

# def find_max():
#   max_value = 0
#   max_index = 0
#   for i in range(n):
#     if count[i] < 0:
#       continue
#     if array[count[i]][i] > max_value:
#       max_value = array[count[i]][i]
#       max_index = i
#   return max_index, max_value
      

# for i in range(n):
#   max_index, max_value = find_max()
#   count[max_index] -= 1
#   if i == n-1:
#     print(max_value)

heap = []

for _ in range(n):
  numbers = map(int, sys.stdin.readline().split())
  for number in numbers:
    if len(heap) < n:
      heappush(heap, number)
    else:
      if heap[0] < number:
        heappop(heap)
        heappush(heap, number)
        
print(heap[0])
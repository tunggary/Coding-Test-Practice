import sys

n = int(sys.stdin.readline().strip())
cranes = list(map(int, sys.stdin.readline().strip().split()))
m = int(sys.stdin.readline().strip())
boxes = list(map(int, sys.stdin.readline().strip().split()))
count = [0]*n

cranes.sort()
boxes.sort(reverse=True)
max_crane = max(cranes)

for i in range(m):
  if boxes[i] > max_crane:
    print(-1)
    exit()
  min_count_value = 1e9
  min_count_index = -1
  for j in range(n):
    if cranes[j] >= boxes[i] and min_count_value > count[j]:
      min_count_value = count[j]
      min_count_index = j
  count[min_count_index] += 1

print(max(count))
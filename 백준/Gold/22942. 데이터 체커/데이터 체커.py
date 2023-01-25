import sys

n = int(sys.stdin.readline().strip())
# axis = [0]*2020001
# CENTER = 1010000

# for _ in range(n):
#   x,r = map(int, sys.stdin.readline().split())
#   left_boundary = CENTER + x - r
#   right_boundary = CENTER + x + r
#   if axis[left_boundary] > 0 or axis[right_boundary] > 0:
#     print("NO")
#     exit(0)
#   axis[left_boundary] += 1
#   axis[right_boundary] += 1
# print("YES")

circle = []
stack = []
LEFT = 0
RIGHT = 1
prev_x = 1e9

for i in range(n):
  x,r = map(int, sys.stdin.readline().split())
  circle.append((i, x-r, LEFT))
  circle.append((i, x+r, RIGHT))

for index, x, type in sorted(circle, key=lambda x: x[1]):
  if x == prev_x:
    print("NO")
    exit(0)
  if type == LEFT:
    stack.append(index)
  else:
    if stack.pop() != index:
      print("NO")
      exit(0)
  prev_x = x
  
print("YES")


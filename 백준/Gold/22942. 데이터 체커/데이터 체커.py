import sys

n = int(sys.stdin.readline().strip())

circle = []
stack = []
LEFT = 0
RIGHT = 1
prev_x = 1e9
flag = True

for i in range(n):
  x,r = map(int, sys.stdin.readline().split())
  circle.append((i, x-r, LEFT))
  circle.append((i, x+r, RIGHT))

for index, x, type in sorted(circle, key=lambda x: x[1]):
  if x == prev_x or (type == RIGHT and stack.pop() != index):
    flag = False
    break
    
  if type == LEFT:
    stack.append(index)
  
  prev_x = x
  
print("YES" if flag else "NO")

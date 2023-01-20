import sys
t = int(sys.stdin.readline().strip())

for _ in range(t):
  x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().strip().split())
  distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
  if x1 == x2 and y1 == y2:
    if r1 == r2:
      print(-1)
    else:
      print(0)
  elif distance <= r1 + r2:
    if distance == r1 + r2 or distance == abs(r1 - r2):
      print(1)
    else:
      if distance > abs(r1 - r2):
        print(2)
      else:
        print(0)
  else:
    print(0)

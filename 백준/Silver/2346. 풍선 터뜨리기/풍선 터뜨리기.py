import sys
from collections import deque

n = int(sys.stdin.readline())
ballons = deque((num, idx+1) for idx, num in enumerate(map(int, sys.stdin.readline().split())))

while len(ballons) > 0:
  num, idx = ballons.popleft()
  print(idx)
  ballons.rotate(-num + 1 if num > 0 else -num)
import sys

a, b, c, m = map(int, sys.stdin.readline().strip().split())

answer = 0
tired = 0

for _ in range(24):
  if tired + a <= m:
    tired += a
    answer += b
  else:
    tired -= c
    tired = max(tired, 0)
    
print(answer)
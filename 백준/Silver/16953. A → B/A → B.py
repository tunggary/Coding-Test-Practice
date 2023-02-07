import sys

a, b = map(int, sys.stdin.readline().strip().split())
answer = 0

while b != a:
  if b < a:
    print(-1)
    exit(0)
  if str(b)[-1] == '1':
    b = int(str(b)[:-1])
  elif b % 2 == 0:
    b //= 2
  else:
    print(-1)
    exit(0)
  answer += 1

print(answer+1)
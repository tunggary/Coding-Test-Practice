import sys

n = int(sys.stdin.readline().strip())
top = list(map(int, sys.stdin.readline().split()))
stack = []
answer = ['0'] * n

for idx, floor in enumerate(top[::-1]):
  while True:
    if len(stack) == 0 or stack[-1][1] > floor:
      stack.append((n-idx-1, floor))
      break
    answer[stack[-1][0]] = str(n-idx)
    stack.pop()

print(' '.join(answer))
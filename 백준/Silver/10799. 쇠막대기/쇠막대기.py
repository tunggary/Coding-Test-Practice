import sys

exp = sys.stdin.readline().strip()
answer = 0
stack = []
prev = ''

for i in range(len(exp)):
  if exp[i] == '(':
    stack.append(exp[i])
  elif exp[i] == ')':
    stack.pop()
    answer += len(stack) if prev == '(' else 1
  prev = exp[i]

print(answer)
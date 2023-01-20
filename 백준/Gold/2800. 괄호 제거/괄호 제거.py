import sys
from itertools import combinations

expression = sys.stdin.readline().strip()

stack = []
position = []
answer = set()
total = 0

for idx, exp in enumerate(expression):
  if exp == '(':
    stack.append(idx)
  elif exp == ')':
    start_idx = stack.pop()
    position.append((start_idx, idx))
    total+=1

for i in range(1, total+1):
  for comb in combinations(position, i):
    new_expression = expression
    for start, end in comb:
      new_expression = new_expression[:start] + '@' + new_expression[start+1:end] + '@' + new_expression[end+1:]
    answer.add(new_expression.replace('@',''))

print('\n'.join(sorted(answer)))
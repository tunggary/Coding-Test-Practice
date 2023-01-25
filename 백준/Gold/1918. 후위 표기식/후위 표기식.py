import sys

expression = sys.stdin.readline().strip()

def get_priority(exp):
  if exp == '(':
    return 3
  elif exp == '*' or exp == '/':
    return 2
  elif exp == '+' or exp == '-':
    return 1

def get_postfix(expression):
  postfix = []
  stack = []
  for exp in expression:
    if exp.isalpha():
      postfix.append(exp)
    elif exp == ')':
      while len(stack) > 0 and stack[-1] != '(':
        postfix.append(stack.pop())
      stack.pop()
    else:
      if len(stack) == 0 or stack[-1] == '(' or get_priority(stack[-1]) < get_priority(exp):
        stack.append(exp)
      else:
        while len(stack) > 0 and stack[-1] != '(' and get_priority(stack[-1]) >= get_priority(exp):
          postfix.append(stack.pop())
        stack.append(exp)
  while len(stack) > 0:
    postfix.append(stack.pop())
  return ''.join(postfix)

print(get_postfix(expression)) 
